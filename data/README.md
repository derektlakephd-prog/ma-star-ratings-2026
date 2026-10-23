# Data

## Raw inputs (`data/raw`)

All inputs are public files released by the Centers for Medicare & Medicaid Services (CMS). They are works of the US government, are in the public domain, and are included here unchanged so that the analysis can be reproduced after CMS revises or retires them. Two large enrollment files are stored as ZIP archives that each contain the original CMS CSV; pandas reads them without unzipping.

| File | CMS release | Used for | Source page |
|---|---|---|---|
| `2026 Star Ratings Data Table - Measure Stars (Oct 8 2025).csv` | 2026 Star Ratings Data Tables, October 8, 2025 | Measure-level stars for the rating simulation | [Part C and D Performance Data](https://www.cms.gov/medicare/health-drug-plans/part-c-d-performance-data), "2026 Star Ratings Data Tables (ZIP)" |
| `2026 Star Ratings Data Table - Measure Data (Oct 8 2025).csv` | Same | Raw contract-level performance rates for the attainment scale | Same |
| `2026 Star Ratings Data Table - Summary Ratings (Oct 8 2025).csv` | Same | CMS-published Part C, Part D, and overall ratings; SNP flag; 2023 and 2024 disaster percentages | Same |
| `2026 Star Ratings Data Table - CAI (Oct 8 2025).csv` | Same | Categorical adjustment index final adjustment categories | Same |
| `2025 Star Ratings Data Table - Summary Ratings (Dec 2 2024).csv` | 2025 Star Ratings Data Tables | Diagnostic for disaster-affected contracts only | Same page, "2025 Star Ratings Data Tables (ZIP)" |
| `SCC_Enrollment_MA_2026_05.csv.zip` | Monthly MA Enrollment by State/County/Contract, May 2026 | County enrollment by contract for QBP pricing and contract enrollment | [Monthly MA Enrollment by State/County/Contract](https://www.cms.gov/data-research/statistics-trends-and-reports/medicare-advantagepart-d-contract-and-enrollment-data/monthly-ma-enrollment-state/county/contract) |
| `CPSC_Contract_Info_2026_05.csv` | Monthly Enrollment by Contract/Plan/State/County, May 2026 | Plan type, SNP status, and parent organization by plan | [Monthly Enrollment by Contract/Plan/State/County](https://www.cms.gov/data-research/statistics-trends-and-reports/medicare-advantagepart-d-contract-and-enrollment-data/monthly-enrollment-contract/plan/state/county) |
| `CPSC_Enrollment_Info_2026_05.csv.zip` | Same | Plan enrollment by county | Same |
| `RateBook2026.xlsx` | 2026 MA Rate Book (worksheet `CountyRate2026`) | County Parts A and B benchmark rates at the 5% and 0% bonus levels | [Ratebooks and Supporting Data, 2026](https://www.cms.gov/medicare/payment/medicare-advantage-rates-statistics/ratebooks-supporting-data/2026), "2026 MA Rate Book" |

### Checksums (SHA-256)

| File | SHA-256 |
|---|---|
| `2025 Star Ratings Data Table - Summary Ratings (Dec 2 2024).csv` | `60df62be3432db2d21d79b5087c98456f3f4b0fc269f1c416e90fa99ced1052c` |
| `2026 Star Ratings Data Table - CAI (Oct 8 2025).csv` | `61aae3a3fc22daca7d86242f189c947585a959dc9e1a64b670f128e40f67a5d7` |
| `2026 Star Ratings Data Table - Measure Data (Oct 8 2025).csv` | `aae62ac492bd56f7029375462b58aa3afc6beeeda7ae0ce5d18ccd1072737f99` |
| `2026 Star Ratings Data Table - Measure Stars (Oct 8 2025).csv` | `6fe3cf1d8c7a388a213b9da951b4b5949279e217da678a3c00d04285416a0138` |
| `2026 Star Ratings Data Table - Summary Ratings (Oct 8 2025).csv` | `bedbf52e11158c6ca91e7be6d7d3d937202e72a73183041e837f46e838dc98ae` |
| `CPSC_Contract_Info_2026_05.csv` | `83ae4951a630da0e79d61f0b3a5da4b2a12d2f120768902f68c973a4ed2e5dc2` |
| `CPSC_Enrollment_Info_2026_05.csv.zip` | `0eb28299fab4f1a34411db83ab827f6713ab1db57acce71090c11d6b6b16e92c` |
| `CPSC_Enrollment_Info_2026_05.csv` (inside the ZIP) | `0eed04c2b7f3ae08744f3c0da548ac78bd2b355505eb158da3a146490c52d706` |
| `RateBook2026.xlsx` | `46076565ca44356ffea7cf632c8d70ca7cf99737fbffea0a459f5aed4b629f59` |
| `SCC_Enrollment_MA_2026_05.csv.zip` | `29546d732d40ff163c4b4fcb35d56ca507933c8827c1ffa72eef80b7934d496c` |
| `SCC_Enrollment_MA_2026_05.csv` (inside the ZIP) | `7297a99a40d6c52044e30dd750001300faabd78b7e481f5f4a9ee5573ed083ab` |

To verify a file on macOS or Linux, run `shasum -a 256 "<file>"` from this folder.

### Obtaining the files from CMS

The Star Ratings files are inside the "2026 Star Ratings Data Tables" and "2025 Star Ratings Data Tables" ZIP archives on the Part C and D Performance Data page. The enrollment files are the May 2026 releases on the two enrollment pages listed above. The ratebook is inside the "2026 MA Rate Book" archive. CMS may update a release after this analysis; the checksums identify the versions used.

### Notes on the CMS files

- The Star Ratings tables begin with a title row. The Measure Stars and Measure Data tables carry measure labels on the third row and contract rows from the fifth row onward; the notebooks parse this layout explicitly.
- Text entries in the Star Ratings tables, such as "Plan too small to be measured" or "Not enough data available," are treated as missing.
- CMS suppresses enrollment counts of 10 or fewer. These cells appear as "." in the State/County/Contract file and are blank in the Contract/Plan/State/County enrollment file; they are counted as 0 and excluded, respectively.

## Derived files (`data/derived`)

Written by the notebooks and documented in `docs/data_dictionary.md`.

| File | Written by | Contents |
|---|---|---|
| `contract_level_results.csv` | Notebook 01 | One row per contract in the 2026 Star Ratings: ratings, enrollment, QBP values, exclusion reason |
| `sample_construction.csv` | Notebook 01 | Exclusion sequence from 769 contracts to the analytic cohort of 425 |
| `reward_factor_thresholds.csv` | Notebook 01 | Published 2026 and recalibrated reward factor thresholds |
| `disaster_mismatch_diagnostic.csv` | Notebook 01 | Disaster-affected contracts whose simulated rating differs from the CMS rating |
| `measure_weights.csv` | Notebook 01 | Weight and removal status of each measure |
| `measure_reference.csv` | Notebook 02 | Measure names, scales, transforms, and percentiles |
| `cohort_characteristics.csv` | Notebook 02 | Parent organization, plan type, and plan-level enrollment of cohort contracts |

Derived files are licensed under CC BY 4.0 (`LICENSE-DATA`). Please cite the article when using them.
