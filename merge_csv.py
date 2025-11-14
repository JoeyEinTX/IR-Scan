import os

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

output_file = 'Consolidated_Hospital_Equipment_Master.csv'

with open(output_file, 'w', encoding='utf-8') as outfile:
    for i, filename in enumerate(files):
        if os.path.exists(filename):
            with open(filename, 'r', encoding='utf-8') as infile:
                lines = infile.readlines()
                if i == 0:
                    # Write all lines from first file (including header)
                    outfile.writelines(lines)
                else:
                    # Skip header for subsequent files
                    outfile.writelines(lines[1:])

print(f"Successfully merged {len(files)} files into {output_file}")
