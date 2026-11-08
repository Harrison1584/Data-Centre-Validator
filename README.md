# Data Centre Materials Validator

### Python | Data Validation | Automation | CSV Processing

## Project Overview

This is a personal Python project I developed to practise data validation and automation in a data centre infrastructure environment.

The project uses a fictional dataset containing 100 materials records, including network switches, fibre cables, patch panels and rack cabinets.

The goal is to automate repetitive checks, identify potential discrepancies and produce a clear report for review.

## Features

- Detects duplicate equipment IDs
- Identifies missing information
- Compares required and ordered quantities
- Flags negative or invalid quantities
- Automatically generates a CSV discrepancy report
- Uses Python's built-in CSV processing tools

## Results

The program successfully processed 100 fictional material records and flagged 11 records requiring review.

**Example output:**

```text
Checked 100 material records
Flagged 11 records for review
Report saved to: discrepancy_report.csv
```

The identified issues included quantity mismatches, duplicate equipment identifiers and missing information.

## Technologies Used

- Python 3
- CSV
- Python `collections.Counter`
- Python `pathlib`
- Microsoft Excel for reviewing the input and output data

## How to Run

1. Download or clone the repository.
2. Ensure `validate_materials.py` and `quadconnect_materials.csv` are in the same folder.
3. Open a terminal in that folder.
4. Run:

```bash
python validate_materials.py
```

5. Open the generated `discrepancy_report.csv` to review the findings.

No additional Python packages are required.

## Possible Future Improvements

- Support multiple Excel and CSV formats
- Add automated column-name recognition
- Build a graphical dashboard
- Validate network cable endpoints and port assignments
- Explore AI-assisted mapping of unfamiliar spreadsheet layouts

## What I Learned

This project helped me practise Python automation, handling structured datasets, troubleshooting errors and generating reports.

It also demonstrated how programming can assist infrastructure teams by identifying potential errors before they affect project delivery.

## Disclaimer

This is an independent learning project using fictional data. It is not affiliated with or endorsed by any data centre company.
