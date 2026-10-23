# Measure Reference

The 45 measures in the 2026 Medicare Advantage Star Ratings. Names and measurement periods are from the 2026 Measure Data table; weights are from the 2026 Star Ratings Technical Notes. Percentiles are on the 0 to 100 attainment scale and use every contract that reports the measure. The same content is in `data/derived/measure_reference.csv`.

- Removed: one of the 13 measure components removed by the CMS final rule published April 6, 2026.
- Transform: `rate` (used directly), `100 - rate` (lower is better: readmissions and members choosing to leave the plan), or `100 - rate/10` (complaints per 1000 enrollees, expressed as the percentage of members without a complaint; display only).
- Topped out: the 10th-percentile contract reaches at least 90. The 2 complaint measures are not classified, and the 2 improvement measures have no raw rate.

| Code | CMS measure name | Part | Removed | Weight | Metric | Transform | Measurement period | Contracts | 10th pct | 90th pct | Topped out |
|---|---|---|---|---|---|---|---|---|---|---|---|
| C01 | Breast Cancer Screening | C | No | 1 | Percentage | rate | 01/01/2024 - 12/31/2024 | 499 | 61.0 | 84.0 | No |
| C02 | Colorectal Cancer Screening | C | No | 1 | Percentage | rate | 01/01/2024 - 12/31/2024 | 544 | 59.0 | 82.0 | No |
| C03 | Annual Flu Vaccine | C | No | 1 | Percentage | rate | 03/2025 - 05/2025 | 497 | 56.0 | 76.4 | No |
| C04 | Improving or Maintaining Physical Health | C | No | 1 | Percentage | rate | 07/17/2024 - 11/01/2024 | 295 | 67.0 | 75.0 | No |
| C05 | Improving or Maintaining Mental Health | C | No | 1 | Percentage | rate | 07/17/2024 - 11/01/2024 | 294 | 80.0 | 88.0 | No |
| C06 | Monitoring Physical Activity | C | No | 1 | Percentage | rate | 07/17/2024 - 11/01/2024 | 504 | 42.0 | 58.0 | No |
| C07 | Special Needs Plan (SNP) Care Management | C | Yes | 1 | Percentage | rate | 01/01/2024 - 12/31/2024 | 325 | 55.0 | 98.0 | No |
| C08 | Care for Older Adults - Medication Review | C | No | 1 | Percentage | rate | 01/01/2024 - 12/31/2024 | 331 | 88.0 | 100.0 | No |
| C09 | Care for Older Adults - Pain Assessment | C | No | 1 | Percentage | rate | 01/01/2024 - 12/31/2024 | 331 | 87.0 | 100.0 | No |
| C10 | Osteoporosis Management in Women who had a Fracture | C | No | 1 | Percentage | rate | 01/01/2024 - 12/31/2024 | 318 | 27.0 | 66.0 | No |
| C11 | Diabetes Care - Eye Exam | C | No | 1 | Percentage | rate | 01/01/2024 - 12/31/2024 | 549 | 65.0 | 88.0 | No |
| C12 | Diabetes Care - Blood Sugar Controlled | C | No | 3 | Percentage | rate | 01/01/2024 - 12/31/2024 | 554 | 77.0 | 92.0 | No |
| C13 | Kidney Health Evaluation for Patients with Diabetes | C | No | 1 | Percentage | rate | 01/01/2024 - 12/31/2024 | 551 | 48.0 | 78.0 | No |
| C14 | Controlling High Blood Pressure | C | No | 3 | Percentage | rate | 01/01/2024 - 12/31/2024 | 526 | 71.0 | 87.0 | No |
| C15 | Reducing the Risk of Falling | C | No | 1 | Percentage | rate | 07/17/2024 - 11/01/2024 | 457 | 49.0 | 70.0 | No |
| C16 | Improving Bladder Control | C | No | 1 | Percentage | rate | 07/17/2024 - 11/01/2024 | 388 | 39.0 | 51.3 | No |
| C17 | Medication Reconciliation Post-Discharge | C | No | 1 | Percentage | rate | 01/01/2024 - 12/31/2024 | 526 | 59.0 | 94.0 | No |
| C18 | Plan All-Cause Readmissions | C | No | 3 | Percentage | 100 - rate | 01/01/2024 - 12/31/2024 | 474 | 88.0 | 92.0 | No |
| C19 | Statin Therapy for Patients with Cardiovascular Disease | C | Yes | 1 | Percentage | rate | 01/01/2024 - 12/31/2024 | 471 | 83.0 | 91.0 | No |
| C20 | Transitions of Care | C | No | 1 | Percentage | rate | 01/01/2024 - 12/31/2024 | 524 | 46.0 | 81.0 | No |
| C21 | Follow-up after Emergency Department Visit for People with Multiple High-Risk Chronic Conditions | C | No | 1 | Percentage | rate | 01/01/2024 - 12/31/2024 | 533 | 51.0 | 75.8 | No |
| C22 | Getting Needed Care | C | No | 2 | Percentage | rate | 03/2025 - 05/2025 | 495 | 77.0 | 85.0 | No |
| C23 | Getting Appointments and Care Quickly | C | No | 2 | Percentage | rate | 03/2025 - 05/2025 | 431 | 80.0 | 87.0 | No |
| C24 | Customer Service | C | Yes | 2 | Percentage | rate | 03/2025 - 05/2025 | 460 | 88.0 | 93.0 | No |
| C25 | Rating of Health Care Quality | C | Yes | 2 | Percentage | rate | 03/2025 - 05/2025 | 488 | 84.0 | 89.0 | No |
| C26 | Rating of Health Plan | C | No | 2 | Percentage | rate | 03/2025 - 05/2025 | 497 | 83.0 | 90.0 | No |
| C27 | Care Coordination | C | No | 2 | Percentage | rate | 03/2025 - 05/2025 | 418 | 85.0 | 90.0 | No |
| C28 | Complaints about the Health Plan | C | Yes | 2 | Rate per 1000 | 100 - rate/10 | 01/01/2024 - 12/31/2024 | 531 | 100.0 | 100.0 | Not classified |
| C29 | Members Choosing to Leave the Plan | C | Yes | 2 | Percentage | 100 - rate | 01/01/2024 - 12/31/2024 | 525 | 66.0 | 96.6 | No |
| C30 | Health Plan Quality Improvement | C | No | 5 | Improvement score |  | Not Applicable |  |  |  | Not applicable |
| C31 | Plan Makes Timely Decisions about Appeals | C | Yes | 2 | Percentage | rate | 01/01/2024 - 12/31/2024 | 432 | 94.0 | 100.0 | Yes |
| C32 | Reviewing Appeals Decisions | C | Yes | 2 | Percentage | rate | 01/01/2024 - 12/31/2024 | 432 | 93.0 | 100.0 | Yes |
| C33 | Call Center - Foreign Language Interpreter and TTY Availability | C | Yes | 2 | Percentage | rate | 02/2025 - 05/2025 | 627 | 92.0 | 100.0 | Yes |
| D01 | Call Center - Foreign Language Interpreter and TTY Availability | D | Yes | 2 | Percentage | rate | 02/2025 - 05/2025 | 644 | 94.0 | 100.0 | Yes |
| D02 | Complaints about the Drug Plan | D | Yes | 2 | Rate per 1000 | 100 - rate/10 | 01/01/2024 - 12/31/2024 | 566 | 100.0 | 100.0 | Not classified |
| D03 | Members Choosing to Leave the Plan | D | Yes | 2 | Percentage | 100 - rate | 01/01/2024 - 12/31/2024 | 541 | 66.0 | 96.0 | No |
| D04 | Drug Plan Quality Improvement | D | No | 5 | Improvement score |  | Not Applicable |  |  |  | Not applicable |
| D05 | Rating of Drug Plan | D | No | 2 | Percentage | rate | 03/2025 - 05/2025 | 526 | 84.0 | 90.0 | No |
| D06 | Getting Needed Prescription Drugs | D | No | 2 | Percentage | rate | 03/2025 - 05/2025 | 447 | 87.0 | 92.0 | No |
| D07 | MPF Price Accuracy | D | Yes | 1 | Percentage | rate | 01/01/2024 - 9/30/2024 | 620 | 98.0 | 100.0 | Yes |
| D08 | Medication Adherence for Diabetes Medications | D | No | 3 | Percentage | rate | 01/01/2024 - 12/31/2024 | 625 | 83.0 | 91.0 | No |
| D09 | Medication Adherence for Hypertension (RAS antagonists) | D | No | 3 | Percentage | rate | 01/01/2024 - 12/31/2024 | 635 | 86.0 | 92.0 | No |
| D10 | Medication Adherence for Cholesterol (Statins) | D | No | 3 | Percentage | rate | 01/01/2024 - 12/31/2024 | 638 | 85.0 | 92.0 | No |
| D11 | MTM Program Completion Rate for CMR | D | No | 1 | Percentage | rate | 01/01/2024 - 12/31/2024 | 597 | 78.0 | 97.0 | No |
| D12 | Statin Use in Persons with Diabetes (SUPD) | D | No | 1 | Percentage | rate | 01/01/2024 - 12/31/2024 | 607 | 83.0 | 93.0 | No |
