# Methods Sources

The source of each computational step. Section references are to the documents listed at the end. With these parameters, the simulated baseline overall rating equals the CMS-published 2026 overall rating for 431 of the 436 non-disaster contracts that both CMS and the simulation rate; the other 5 differ by 0.5 stars.

## Star rating simulation (notebook 01)

| Step | Implementation | Source |
|---|---|---|
| Measure stars | Taken as published; unchanged by measure removal | 2026 Star Ratings Data Tables, Measure Stars table [1] |
| Measure weights | `MEASURE_WEIGHTS`; 1, 2, or 3, and 5 for improvement measures; new measures weighted 1 | Technical Notes, Attachment G, Tables G-1 and G-2 [2] |
| Summary and overall ratings as weighted means of measure stars | `weighted_mean` | Technical Notes [2]; 42 CFR 422.166(c) and (d) [4] |
| Minimum number of rated measures | At least half of applicable non-improvement measures | Technical Notes, Tables 6 and 7 [2]; 42 CFR 422.166(c)(2)(i) [4] |
| Overall rating measures | Part C measures plus Part D measures, with D02 and D03 counted through C28 and C29 | Technical Notes [2] |
| SNP Care Management (C07) | Applies only to SNP contracts | Technical Notes [2] |
| Weighted variance | `weighted_variance`; improvement measures excluded | Technical Notes, reward factor section [2] |
| Reward factor | 0.1 to 0.4 stars by mean (65th and 85th percentiles) and variance (30th and 70th percentiles) categories | Technical Notes, Tables 8 and 9 [2]; 42 CFR 422.166(f)(1) [4] |
| Reward factor thresholds, ratings with improvement measures | Row (Improvement: With; New Measures: With) | Technical Notes, Tables 8 and 9 [2] |
| Reward factor thresholds, ratings without improvement measures | Row (Improvement: Without; New Measures: With). The with and without new-measure comparison applies only to disaster-affected contracts, which are excluded | Technical Notes, Tables 8 and 9, and the disaster provisions [2] |
| Categorical adjustment index | Published 2026 value by final adjustment category; held fixed after removal | Technical Notes, Tables 12 (overall), 15 (Part C), 18 (MA-PD Part D), 21 (PDP Part D) [2]; CAI table [1]; 42 CFR 422.166(f)(2) [4] |
| Improvement measure hold harmless | Rating without improvement measures replaces the rating with them when it is at least 4 stars and higher | Technical Notes [2]; 42 CFR 422.166(g)(1) [4] |
| Rounding | Nearest half star, ties up | Technical Notes, rounding rules [2]; 42 CFR 422.166(c)(3) and (d)(2)(iv) [4] |
| Disaster-affected contracts | Excluded when at least 25% of enrollees were in FEMA-designated areas in 2023 or 2024 | Summary Ratings table, disaster percentages [1]; Technical Notes, disaster provisions [2]; 42 CFR 422.166(i) [4] |
| Disaster mismatch diagnostic | Compares 2026 CMS ratings with the higher of the simulated 2026 rating and the 2025 CMS rating | 2025 Star Ratings Data Tables, Summary Ratings table [1] |
| Removed measures | C07, C19, C24, C25, C28, C29, C31, C32, C33, D01, D02, D03, D07 | CMS final rule, April 6, 2026, section "Adding, Updating, and Removing Measures" [3]. The rule applies the removals to future Star Ratings years; this analysis applies them to the 2026 Star Ratings to isolate their effect |
| Reward factor recalibration | Same percentiles computed from the post-removal distribution of contract means and variances | eMethods, Reward Factor Recalibration [8]; percentile definitions from Technical Notes, Tables 8 and 9 [2] |

## Payment estimates (notebook 01)

| Step | Implementation | Source |
|---|---|---|
| QBP eligibility | Overall rating of at least 4.0 | 42 CFR 422.258(d)(7) [5] |
| Bonus amount | Increase in the applicable percentage of 5 percentage points, doubled in qualifying counties; both are reflected in the ratebook's 5% bonus rate | 42 CFR 422.258(d)(7) [5]; 2026 MA Rate Book [6] |
| County benchmark rates | Parts A and B 5% bonus and 0% bonus rates, worksheet CountyRate2026 | 2026 MA Rate Book [6] |
| Enrollment | May 2026 county enrollment by contract; suppressed counts set to 0 | Monthly MA Enrollment by State/County/Contract [7] |
| Annual QBP value | (5% rate minus 0% rate) times enrollment times 12, summed over counties | eMethods, Quality Bonus Payment Calculation [8] |

## Measure characteristics (notebook 02)

| Step | Implementation | Source |
|---|---|---|
| Raw performance rates | Measure Data table; text entries treated as missing | 2026 Star Ratings Data Tables, Measure Data table [1] |
| Attainment scale | `rate`, `100 - rate`, or `100 - rate/10` | eMethods, Topped-Out Definition [8] |
| Topped-out criterion | 10th-percentile contract at least 90 | Lee 2007 [9]; eMethods [8] |
| Sensitivity analysis | Floors of 5, 10, 15; margins of 5, 10, 15 | eMethods, Topped-Out Definition [8] |
| Plan type, SNP status, parent organization | Plan-level CPSC files, MA organization types only | Monthly Enrollment by Contract/Plan/State/County [7] |
| Ownership | Explicit classification of parent organizations | eMethods, Ownership Classification [8] |

## Sources

1. Centers for Medicare & Medicaid Services. 2026 Star Ratings Data Tables (October 8, 2025) and 2025 Star Ratings Data Tables. Part C and D Performance Data. https://www.cms.gov/medicare/health-drug-plans/part-c-d-performance-data
2. Centers for Medicare & Medicaid Services. Medicare 2026 Part C & D Star Ratings Technical Notes, updated September 25, 2025. https://www.cms.gov/files/document/2026-star-ratings-technical-notes.pdf
3. Centers for Medicare & Medicaid Services. Medicare Program; Contract Year 2027 and Certain Contract Year 2026 Policy and Technical Changes to the Medicare Advantage Program, Medicare Prescription Drug Benefit Program, and Medicare Cost Plan Program. Final rule. *Fed Regist*. 2026;91(65):17384-17602. Document 2026-06600. https://www.federalregister.gov/documents/2026/04/06/2026-06600/medicare-program-contract-year-2027-and-certain-contract-year-2026-policy-and-technical-changes-to
4. 42 CFR 422.166, Calculation of Star Ratings. https://www.ecfr.gov/current/title-42/chapter-IV/subchapter-B/part-422/subpart-D/section-422.166
5. 42 CFR 422.258, Calculation of benchmarks. https://www.ecfr.gov/current/title-42/chapter-IV/subchapter-B/part-422/subpart-G/section-422.258
6. Centers for Medicare & Medicaid Services. 2026 MA Rate Book. Ratebooks and Supporting Data, 2026. https://www.cms.gov/medicare/payment/medicare-advantage-rates-statistics/ratebooks-supporting-data/2026. See also: Announcement of Calendar Year (CY) 2026 Medicare Advantage (MA) Capitation Rates and Part C and Part D Payment Policies, April 7, 2025. https://www.cms.gov/newsroom/fact-sheets/2026-medicare-advantage-part-d-rate-announcement
7. Centers for Medicare & Medicaid Services. Medicare Advantage/Part D Contract and Enrollment Data: Monthly MA Enrollment by State/County/Contract and Monthly Enrollment by Contract/Plan/State/County, May 2026. https://www.cms.gov/data-research/statistics-trends-and-reports/medicare-advantagepart-d-contract-and-enrollment-data
8. Lake DT, Civelek Y, Bond AM, Khullar D. Characteristics and financial implications of measures removed from Medicare Advantage star ratings. *JAMA Netw Open*. 2026;9(10):e2640240. Supplement 1, eMethods. doi:10.1001/jamanetworkopen.2026.40240
9. Lee TH. Eulogy for a quality measure. *N Engl J Med*. 2007;357(12):1175-1177. doi:10.1056/NEJMp078102
