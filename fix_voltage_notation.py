import csv
import os

# List of all cleaned CSV files
cleaned_files = [
    'IR Scan Ground_Cleaned.csv',
    'IR Scan 2nd Floor_Cleaned.csv',
    'IR Scan 3rd Floor_Cleaned.csv',
    'IR Scan 4th Floor_Cleaned.csv',
    'IR Scan 5th Floor_Cleaned.csv',
    'IR Scan 6th Floor_Cleaned.csv',
    'IR Scan 7th Floor_Cleaned.csv',
    'IR Scan 8th Floor_Cleaned.csv',
    'IR Scan 9th Floor_Cleaned.csv',
    'IR Scan TEP Plant_Cleaned.csv',
    'Ground Floor Elec Rms ZL0.904E_ZL0.904E1_Cleaned.csv'
]

files_updated = 0

for filename in cleaned_files:
    if not os.path.exists(filename):
        print(f"Skipping {filename} - file not found")
        continue
    
    # Read the file
    with open(filename, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        data = list(reader)
    
    # Update voltage notation: replace → with -
    updated = False
    for row in data:
        if '→' in row['Voltage']:
            row['Voltage'] = row['Voltage'].replace('→', '-')
            updated = True
    
    # Write back if updated
    if updated:
        with open(filename, 'w', encoding='utf-8', newline='') as f:
            if data:
                fieldnames = data[0].keys()
                writer = csv.DictWriter(f, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerows(data)
        print(f"Updated: {filename}")
        files_updated += 1
    else:
        print(f"No changes needed: {filename}")

print(f"\nTotal files updated: {files_updated}")
print(f"Voltage notation changed from → to -")
