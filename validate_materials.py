
# Import the required Python libraries
import csv
from collections import Counter
from pathlib import Path

# Set the input and output file paths
folder = Path(__file__).resolve().parent
source = folder / 'quadconnect_materials.csv'
output = folder / 'discrepancy_report.csv'

# Read the materials CSV file
with source.open(newline='', encoding='utf-8-sig') as file:
    records = list(csv.DictReader(file))

# Count equipment IDs to find duplicates
id_counts = Counter(
    r['Equipment ID'].strip()
    for r in records
    if r['Equipment ID'].strip()
)

# Create a list to store errors
issues = []

# Check each row for errors
for row_number, row in enumerate(records, start=2):
    problems = []

    # Check for missing information
    for field in [
        'Equipment ID', 'Zone', 'Material', 'Unit',
        'Required Qty', 'Ordered Qty', 'Design Ref', 'Purchase Ref'
    ]:
        if not row[field].strip():
            problems.append(f'Missing {field}')

    # Check for duplicate equipment IDs
    equipment_id = row['Equipment ID'].strip()

    if equipment_id and id_counts[equipment_id] > 1:
        problems.append('Duplicate equipment ID')

    # Check quantities for errors
    try:
        required = int(row['Required Qty'])
        ordered = int(row['Ordered Qty'])

        # Check for negative quantities
        if required < 0 or ordered < 0:
            problems.append('Negative quantity')

        # Check for quantity mismatches
        elif required != ordered:
            problems.append(
                f'Quantity mismatch ({ordered - required:+d})'
            )

    # Handle invalid quantity values
    except ValueError:
        if row['Required Qty'].strip() and row['Ordered Qty'].strip():
            problems.append('Invalid quantity')

    # Save records that contain errors
    if problems:
        issues.append({
            'Excel Row': row_number,
            'Equipment ID': equipment_id,
            'Material': row['Material'],
            'Issue': '; '.join(problems)
        })

# Create the discrepancy report CSV
with output.open('w', newline='', encoding='utf-8-sig') as file:
    writer = csv.DictWriter(
        file,
        fieldnames=[
            'Excel Row', 'Equipment ID', 'Material', 'Issue'
        ]
    )

    writer.writeheader()
    writer.writerows(issues)

# Display the results in the terminal
print(f'Checked {len(records)} material records')
print(f'Flagged {len(issues)} records for review')
print(f'Report saved to: {output.name}')

# Remind the user to verify errors before making changes
print('Check discrepancies against approved designs before changing records.')
