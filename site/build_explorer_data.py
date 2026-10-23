"""Build site/explorer_data.js, the data file read by the contract explorer (index.html).

Run from the repository root after notebooks 01 and 02:

    python site/build_explorer_data.py

Inputs are the derived files written by the notebooks and four public CMS files in
data/raw. The output defines one global object, EXPLORER_DATA, so the page works when
opened directly from disk as well as when served.
"""
import json
import zipfile
from pathlib import Path

import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / "data" / "raw"
DERIVED = ROOT / "data" / "derived"
OUT = ROOT / "site" / "explorer_data.js"

SUMMARY_2026 = RAW / "2026 Star Ratings Data Table - Summary Ratings (Oct 8 2025).csv"
MEASURE_STARS_2026 = RAW / "2026 Star Ratings Data Table - Measure Stars (Oct 8 2025).csv"
CPSC_CONTRACT = RAW / "CPSC_Contract_Info_2026_05.csv"
SCC_ZIP = RAW / "SCC_Enrollment_MA_2026_05.csv.zip"

# The 13 removed components, in the order of the Measure Stars table.
REMOVED = ["C07", "C19", "C24", "C25", "C28", "C29", "C31", "C32", "C33", "D01", "D02", "D03", "D07"]


def strip_text(frame):
    return frame.apply(lambda col: col.str.strip() if col.dtype == object else col)


# Contract-level results and cohort characteristics from the notebooks
results = pd.read_csv(DERIVED / "contract_level_results.csv")
cohort = pd.read_csv(DERIVED / "cohort_characteristics.csv")
measures = pd.read_csv(DERIVED / "measure_reference.csv")

# Contract names and the Star Ratings parent organization
summary = strip_text(pd.read_csv(SUMMARY_2026, encoding="utf-8-sig", header=1, dtype=str))
summary = summary.rename(columns={"Contract Number": "Contract_ID", "Contract Name": "Contract_Name",
                                  "Organization Marketing Name": "Marketing_Name",
                                  "Parent Organization": "Star_Parent"})

# Parent organization in the May 2026 CPSC contract file (first listed plan)
cpsc = strip_text(pd.read_csv(CPSC_CONTRACT, encoding="cp1252", dtype=str))
cpsc_parent = (cpsc.dropna(subset=["Parent Organization"])
               .groupby("Contract ID")["Parent Organization"].first()
               .rename("CPSC_Parent"))

# States served: May 2026 county enrollment summed by state, suppressed counts as 0
with zipfile.ZipFile(SCC_ZIP) as archive:
    scc = pd.read_csv(archive.open(archive.namelist()[0]), dtype=str)
scc["Contract_ID"] = scc["Contract ID"].str.strip()
scc["State"] = scc["State"].str.strip()
scc["Enrolled"] = pd.to_numeric(scc["Enrolled"].str.strip().str.replace(",", "", regex=False),
                                errors="coerce").fillna(0)
by_state = (scc[scc["Enrolled"] > 0].groupby(["Contract_ID", "State"])["Enrolled"].sum()
            .reset_index().sort_values(["Contract_ID", "Enrolled"], ascending=[True, False]))
states = by_state.groupby("Contract_ID")["State"].apply(list)

# Stars on the removed components
raw = pd.read_csv(MEASURE_STARS_2026, encoding="utf-8-sig", header=None, dtype=str, low_memory=False)
labels = raw.iloc[2].tolist()
columns = {0: "Contract_ID"}
for i, label in enumerate(labels):
    if isinstance(label, str) and ":" in label and label.split(":")[0].strip() in REMOVED:
        columns[i] = label.split(":")[0].strip()
stars = raw.iloc[4:, list(columns)].rename(columns=columns)
stars["Contract_ID"] = stars["Contract_ID"].str.strip()
stars = stars[stars["Contract_ID"].str.fullmatch(r"[A-Z0-9]{5}", na=False)].set_index("Contract_ID")
stars = stars.apply(lambda col: pd.to_numeric(col.str.strip(), errors="coerce"))

table = (results
         .merge(summary[["Contract_ID", "Contract_Name", "Marketing_Name", "Star_Parent"]],
                on="Contract_ID", how="left")
         .merge(cohort[["Contract_ID", "Parent_Organization", "Plan_Type"]], on="Contract_ID", how="left")
         .merge(cpsc_parent, left_on="Contract_ID", right_index=True, how="left"))
# Parent organization: the cohort classification used in the article, then the CPSC
# contract file, then the Star Ratings table.
table["Parent"] = table["Parent_Organization"].fillna(table["CPSC_Parent"]).fillna(table["Star_Parent"])
assert table["Parent"].notna().all()
assert len(table) == 769 and table["In_Analytic_Cohort"].sum() == 425


def value(x, digits=None):
    if pd.isna(x):
        return None
    if isinstance(x, (bool,)) or str(x) in ("True", "False"):
        return bool(x) if not isinstance(x, str) else x == "True"
    if digits is not None:
        return round(float(x), digits)
    return x


# The explorer lists MA contracts only; stand-alone prescription drug plans are omitted.
ma = table[table["Contract_Type"] != "PDP"]
assert len(ma) == 720

records = []
for row in ma.itertuples(index=False):
    cid = row.Contract_ID
    removed_stars = [None if cid not in stars.index or pd.isna(stars.at[cid, m]) else int(stars.at[cid, m])
                     for m in REMOVED]
    records.append({
        "id": cid,
        "name": value(row.Marketing_Name),
        "contract": value(row.Contract_Name),
        "parent": row.Parent,
        "orgType": value(row.Organization_Type),
        "type": row.Contract_Type,
        "plan": value(row.Plan_Type),
        "snp": bool(row.Is_SNP),
        "states": states.get(cid, []),
        "enr": None if pd.isna(row.Enrollment) else int(row.Enrollment),
        "cmsC": value(row.CMS_PartC, 1), "cmsD": value(row.CMS_PartD, 1), "cms": value(row.CMS_Overall, 1),
        "baseC": value(row.Baseline_PartC, 1), "baseD": value(row.Baseline_PartD, 1),
        "base": value(row.Baseline_Overall, 1),
        "projC": value(row.Projected_PartC, 1), "projD": value(row.Projected_PartD, 1),
        "proj": value(row.Projected_Overall, 1),
        "qbpValue": value(row.Annual_QBP_Value, 0),
        "qbp": value(row.QBP_Change),
        "baseQbp": value(row.Baseline_QBP, 0),
        "netQbp": value(row.Net_QBP_Change, 0),
        "cohort": bool(row.In_Analytic_Cohort),
        "reason": row.Exclusion_Reason,
        "removed": removed_stars,
    })

names = measures.set_index("Measure")["CMS_Name"]
data = {
    "citation": ("Lake DT, Civelek Y, Bond AM, Khullar D. Characteristics and financial implications of "
                 "measures removed from Medicare Advantage star ratings. JAMA Netw Open. "
                 "2026;9(10):e2640240. doi:10.1001/jamanetworkopen.2026.40240"),
    "removedMeasures": [{"code": m, "name": names[m]} for m in REMOVED],
    "contracts": records,
}

# Totals the page must reproduce (the Table in the article)
c = table[table["In_Analytic_Cohort"]]
assert (c["QBP_Change"] == "Lose").sum() == 33 and (c["QBP_Change"] == "Gain").sum() == 6
assert round(c["Net_QBP_Change"].sum() / 1e6) == -2093
assert round(c["Baseline_QBP"].sum() / 1e6) == 15057

OUT.write_text("// Generated by site/build_explorer_data.py. Do not edit by hand.\n"
               "window.EXPLORER_DATA = " + json.dumps(data, separators=(",", ":"), ensure_ascii=False) + ";\n",
               encoding="utf-8")
print(f"Wrote {OUT.relative_to(ROOT)}: {len(records)} contracts, {OUT.stat().st_size / 1024:.0f} KB")
