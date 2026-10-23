# Data Dictionary

Variables in every file written by the notebooks. Ratings are on the CMS 1 to 5 star scale in half-star steps. Dollar amounts are annual 2026 US dollars. Missing values are blank. Terms are defined in `glossary.md`.

## data/derived/contract_level_results.csv

One row per contract in the 2026 Star Ratings (769 rows). Written by notebook 01.

| Variable | Type | Definition |
|---|---|---|
| `Contract_ID` | text | CMS contract number |
| `Organization_Type` | text | CMS organization type (for example, Local CCP, Regional CCP, PFFS, MSA, 1876 Cost, PDP) |
| `Contract_Type` | text | Rating type: MA-PD (Part C, Part D, and overall ratings), MA-Only (Part C only), or PDP (Part D only) |
| `Is_SNP` | true/false | Flagged as a special needs plan contract in the Summary Ratings table, or reports the SNP Care Management measure (C07) |
| `Disaster_Pct_2023`, `Disaster_Pct_2024` | number | Percentage of the contract's enrollees in FEMA-designated disaster areas in 2023 and 2024, from the Summary Ratings table |
| `Disaster_Affected` | true/false | `Disaster_Pct_2023` or `Disaster_Pct_2024` is at least 25 |
| `CMS_PartC`, `CMS_PartD`, `CMS_Overall` | number | Ratings published by CMS for 2026 |
| `Baseline_PartC`, `Baseline_PartD`, `Baseline_Overall` | number | Ratings simulated with all 2026 measures and the published reward factor thresholds |
| `Replication_Match` | true/false | `Baseline_Overall` equals `CMS_Overall`; blank when either is missing |
| `Projected_PartC`, `Projected_PartD`, `Projected_Overall` | number | Ratings simulated without the 13 removed components, with reward factor thresholds recalibrated to the post-removal distribution |
| `Rating_Change` | number | `Projected_Overall` minus `Baseline_Overall`; analytic cohort only |
| `Enrollment` | number | May 2026 contract enrollment, the sum of county counts in the State/County/Contract file with suppressed counts set to 0; blank when the contract does not appear in the file |
| `Benchmark_5pct` | number | Sum over counties of enrollment times the Parts A and B 5% bonus benchmark rate times 12 |
| `Benchmark_0pct` | number | Same with the 0% bonus benchmark rate |
| `Annual_QBP_Value` | number | `Benchmark_5pct` minus `Benchmark_0pct`: the annual QBP the contract receives when its overall rating is at least 4.0 |
| `Baseline_QBP_Eligible`, `Projected_QBP_Eligible` | true/false | Overall rating of at least 4.0 at baseline and after removal; analytic cohort only |
| `QBP_Change` | text | Lose (eligible at baseline, not after removal), Gain, Retain, or Never; analytic cohort only |
| `Baseline_QBP`, `Projected_QBP` | number | `Annual_QBP_Value` when eligible, otherwise 0; analytic cohort only |
| `Net_QBP_Change` | number | `Projected_QBP` minus `Baseline_QBP`; analytic cohort only |
| `Exclusion_Reason` | text | Included; No overall rating; Disaster affected; Below minimum measure threshold after removal; or No linkable May 2026 enrollment. Assigned in that order. No overall rating means that CMS did not publish one or that the simulation does not produce one; the second applies to 16 small SNP contracts with stars on fewer than half of the Part C measures the simulation counts toward the minimum (notebook 01, section 4). |
| `In_Analytic_Cohort` | true/false | `Exclusion_Reason` is Included (425 contracts) |

Five cohort contracts (H1969, H3536, H6898, H7389, R7444) appear in the May 2026 enrollment files with every county count suppressed. Their `Enrollment`, benchmark values, and QBP values are 0.

## data/derived/sample_construction.csv

The exclusion sequence reported in the eMethods (Sample Exclusions).

| Variable | Definition |
|---|---|
| `Step` | Starting population, each exclusion, and the analytic cohort |
| `Contracts` | Number of contracts; exclusions are negative |
| `Enrollees` | May 2026 enrollment of those contracts; exclusions are negative |

## data/derived/reward_factor_thresholds.csv

Reward factor thresholds before and after measure removal (eMethods, Reward Factor Recalibration).

| Variable | Definition |
|---|---|
| `Rating` | PartC, PartD_MAPD, PartD_PDP, or Overall |
| `Version` | `with_imp`: ratings that include the improvement measures; `no_imp`: ratings without them |
| `Threshold` | `vl` and `vh`: 30th and 70th percentiles of contract variance; `ml` and `mh`: 65th and 85th percentiles of the contract weighted mean |
| `Percentile` | Percentile that defines the threshold |
| `Published_2026` | Value published in the 2026 Technical Notes (Tables 8 and 9) |
| `Recalibrated` | Same percentile computed from the post-removal distribution |
| `N_Contracts` | Contracts in the post-removal distribution |

## data/derived/disaster_mismatch_diagnostic.csv

Disaster-affected contracts for which any simulated rating differs from the CMS rating, with the 2025 CMS rating for comparison. For each of Overall, PartC, and PartD:

| Variable | Definition |
|---|---|
| `Contract_ID`, `Disaster_Pct_2023`, `Disaster_Pct_2024` | As above |
| `Baseline_*` | Simulated 2026 rating |
| `CMS_2025_*` | CMS-published 2025 rating |
| `Higher_Of_*` | Larger of the simulated 2026 rating and the 2025 rating |
| `CMS_*` | CMS-published 2026 rating |

This is a summary-level check on the direction of the discrepancy. CMS applies its disaster policy at the measure level, which cannot be reproduced from public data.

## data/derived/measure_weights.csv

| Variable | Definition |
|---|---|
| `Measure` | CMS measure code (C01 to C33, D01 to D12) |
| `Part` | C or D |
| `Weight` | CMS measure weight, 2026 Star Ratings Technical Notes |
| `Improvement_Measure` | C30 or D04 |
| `Removed` | One of the 13 components removed by the April 2026 final rule |

## data/derived/measure_reference.csv

One row per measure (45 rows). `docs/measures.md` presents the same content.

| Variable | Definition |
|---|---|
| `Measure`, `Part`, `Weight`, `Improvement_Measure`, `Removed` | As in `measure_weights.csv` |
| `CMS_Name` | Measure name in the 2026 Measure Data table (dashes normalized to hyphens) |
| `Metric` | Percentage; Rate per 1000 enrollees; or Improvement score (no raw rate) |
| `Higher_Is_Better` | Direction of the raw rate |
| `Attainment_Transform` | Conversion to the 0 to 100 attainment scale: `rate`; `100 - rate`; `100 - rate/10 (display only)` for the complaint measures; or `Not applicable` for improvement measures |
| `Measurement_Period` | Measurement period in the Measure Data table |
| `N_Contracts` | Contracts reporting a numeric rate |
| `P10_Attainment`, `P90_Attainment` | 10th and 90th percentile contract on the attainment scale |
| `Topped_Out` | `P10_Attainment` of at least 90; blank for the 2 complaint measures, which are not classified, and for improvement measures |

## data/derived/cohort_characteristics.csv

Plan-level characteristics of the 425 analytic cohort contracts from the May 2026 CPSC files (MA organization types only). Written by notebook 02 and used for the HMO, SNP, and for-profit columns of the Table.

| Variable | Definition |
|---|---|
| `Contract_ID` | CMS contract number |
| `Parent_Organization` | Parent organization in the CPSC contract file; ownership is classified from it. Blank for the 2 cost contracts (H2450, H2461) that have no plans in the CPSC files; both are classified as nonprofit, and their plan type is Other |
| `Plan_Type` | HMO, PPO, or Other: the plan type with the most CPSC enrollment, or the most plans when every enrollment count is suppressed |
| `HMO_Enrollment`, `PPO_Enrollment`, `Other_Enrollment` | CPSC plan enrollment by plan type; suppressed counts excluded |
| `Plan_Enrollment` | Sum of the three |
| `SNP_Enrollment` | CPSC enrollment in special needs plans |

## outputs/topped_out_classification.csv

The 43 measures with raw rates, sorted by removal status and bottom-decile attainment.

| Variable | Definition |
|---|---|
| `Measure`, `Removed`, `N_Contracts`, `P10_Attainment`, `P90_Attainment` | As above |
| `Rate_Based` | Complaint measure reported per 1000 enrollees (C28, D02) |
| `Topped_Out` | `P10_Attainment` of at least 90 and not rate based |

## outputs/sensitivity_thresholds.csv

Classification counts for each combination of percentile floor and margin (eMethods, Topped-Out Definition).

| Variable | Definition |
|---|---|
| `Floor_Percentile` | Percentile of the contract distribution tested (5, 10, 15) |
| `Margin` | Points below the ceiling of 100 (5, 10, 15) |
| `Removed_Classified` | Removed components meeting the criterion, excluding the 2 complaint measures |
| `Removed_Including_Complaints` | Same, including them |
| `Retained` | Retained measures meeting the criterion |
| `Retained_Measures` | Codes of those retained measures |

## outputs/table_qbp_transitions.csv

Unrounded values behind the Table. One row per QBP eligibility group and a Total row.

| Variable | Definition |
|---|---|
| `QBP_Eligibility_Change` | Lose, Gain, Retain, Never, or Total |
| `Contracts`, `Enrollees`, `Enrollees_Pct` | Count, May 2026 enrollment, and share of cohort enrollment |
| `Median_Enrollment`, `Enrollment_P25`, `Enrollment_P75` | Median and interquartile range of contract enrollment |
| `HMO_Pct`, `SNP_Pct` | Share of plan-level CPSC enrollment in HMO plans and in SNP plans |
| `For_Profit_Pct` | Share of contract enrollment in contracts with a for-profit parent organization |
| `Baseline_QBP_Millions`, `Net_QBP_Change_Millions` | Baseline QBP and net change, millions of dollars |
| `Net_QBP_Change_Pct` | Net change as a percentage of the cohort's baseline QBP pool |

`table_qbp_transitions_formatted.csv` and `table_qbp_transitions_formatted.md` contain the same values formatted as in the article, rounded half up.

## outputs/results_text_values.csv

Each number quoted in the Results text, with full precision. Columns: `Quantity`, `Value`.

## outputs/figure_dot_plot.pdf and outputs/figure_dot_plot.png

The Figure. The PDF is vector with embedded TrueType fonts; the PNG is 300 dpi. Both carry the article citation in their metadata.

## site/explorer_data.js

The data file read by the contract explorer (`index.html`), written by `site/build_explorer_data.py`. It defines one JavaScript object, `EXPLORER_DATA`, with the article citation, the 13 removed components, and one record per MA contract (720; the 49 stand-alone prescription drug plans are omitted). Each record combines `contract_level_results.csv` and `cohort_characteristics.csv` with contract and marketing names from the 2026 Summary Ratings table, the states with nonsuppressed May 2026 enrollment in the State/County/Contract file (ordered by enrollment), and the contract's stars on the removed components from the Measure Stars table. Parent organization is taken from `cohort_characteristics.csv`, then the CPSC contract file, then the Summary Ratings table.

The CSV downloaded from the explorer holds the rows shown after filtering. Its columns are a subset of `contract_level_results.csv` with the same names (`Contract_ID`, `Organization_Type`, `Contract_Type`, `Is_SNP`, `Enrollment`, the CMS, baseline, and projected Part C, Part D, and overall ratings, `Rating_Change`, `QBP_Change`, `Annual_QBP_Value`, `Baseline_QBP`, `Net_QBP_Change`, `In_Analytic_Cohort`, and `Exclusion_Reason`), plus these columns:

| Variable | Definition |
|---|---|
| `Marketing_Name`, `Contract_Name` | Organization marketing name and contract name in the 2026 Summary Ratings table |
| `Parent_Organization` | As described above |
| `Plan_Type` | From `cohort_characteristics.csv`; blank outside the analytic cohort |
| `States_Served` | States with nonsuppressed May 2026 enrollment, ordered by enrollment, separated by spaces |
| `Stars_C07`, ..., `Stars_D07` | The contract's stars on each of the 13 removed components; blank when not rated |

Ratings carry one decimal, true/false values are written as True and False, and dollar amounts are rounded to whole dollars. `Rating_Change`, `QBP_Change`, `Baseline_QBP`, and `Net_QBP_Change` are blank outside the analytic cohort. For the remaining variables of `contract_level_results.csv`, such as disaster percentages and benchmark values, use that file.

