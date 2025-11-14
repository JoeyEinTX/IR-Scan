import csv
import os

# List of all cleaned CSV files
files = [
    'IR Scan Ground_Cleaned.csv',
    'Ground Floor Elec Rms ZL0.904E_ZL0.904E1_Cleaned.csv',
    'IR Scan 2nd Floor_Cleaned.csv',
    'IR Scan 3rd Floor_Cleaned.csv',
    'IR Scan 4th Floor_Cleaned.csv',
    'IR Scan 5th Floor_Cleaned.csv',
    'IR Scan 6th Floor_Cleaned.csv',
    'IR Scan 7th Floor_Cleaned.csv',
    'IR Scan 8th Floor_Cleaned.csv',
    'IR Scan 9th Floor_Cleaned.csv',
    'IR Scan TEP Plant_Cleaned.csv'
]

for filename in files:
    if os.path.exists(filename):
        # Read the file
        with open(filename, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        
        # Update header
        header = lines[0].replace('Tag Color', 'System Type')
        
        # Update data rows - convert Red/White to Emergency/Normal
        new_lines = [header]
        for line in lines[1:]:
            line = line.replace(',Red,', ',Emergency,')
            line = line.replace(',White,', ',Normal,')
            new_lines.append(line)
        
        # Write back
        with open(filename, 'w', encoding='utf-8') as f:
            f.writelines(new_lines)
        
        print(f"Updated: {filename}")

print("\nAll files updated!")
print("- Column renamed: 'Tag Color' → 'System Type'")
print("- Values updated: 'Red' → 'Emergency', 'White' → 'Normal'")
