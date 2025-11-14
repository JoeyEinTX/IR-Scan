import csv
from collections import defaultdict

# Read the consolidated file
with open('Consolidated_Hospital_Equipment_Master.csv', 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    data = list(reader)

# Filter for Branch Panels and Feeder Panels only
panel_types = ['Branch Panel', 'Feeder Panel']
panels = [row for row in data if row['Equipment Type'] in panel_types]

# Sort by Floor, then by Room Number, then by Equipment Type
floor_order = {
    'TEP Plant': -1,
    'Ground': 0,
    '2nd Floor': 2,
    '3rd Floor': 3,
    '4th Floor': 4,
    '5th Floor': 5,
    '6th Floor': 6,
    '7th Floor': 7,
    '8th Floor': 8,
    '9th Floor': 9
}

panels.sort(key=lambda x: (floor_order.get(x['Floor'], 999), x['Room Number'], x['Equipment Type']))

# Create detailed inspection report
with open('Panel_Inspection_Report.csv', 'w', encoding='utf-8', newline='') as f:
    fieldnames = ['Floor', 'Room Number', 'Panel Type', 'Panel Name/Label', 'Amperage', 'Voltage', 
                  'Phase/Wire', 'Fed From', 'Mounting', 'System Type', 'Notes']
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    
    for row in panels:
        writer.writerow({
            'Floor': row['Floor'],
            'Room Number': row['Room Number'],
            'Panel Type': row['Equipment Type'],
            'Panel Name/Label': row['Equipment Name/Label'],
            'Amperage': row['Amperage/kVA'],
            'Voltage': row['Voltage'],
            'Phase/Wire': row['Phase/Wire'],
            'Fed From': row['Fed From'],
            'Mounting': row['Mounting'],
            'System Type': row['System Type'],
            'Notes': row['Notes']
        })

# Create summary by floor and panel type
summary_data = defaultdict(lambda: {'Branch Panel': 0, 'Feeder Panel': 0})
for row in panels:
    summary_data[row['Floor']][row['Equipment Type']] += 1

with open('Panel_Inspection_Summary.csv', 'w', encoding='utf-8', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['PANEL INSPECTION SUMMARY - Monthly Audit'])
    writer.writerow(['All Branch Panels and Feeder Panels'])
    writer.writerow([])
    writer.writerow(['Floor', 'Branch Panels', 'Feeder Panels', 'Total Panels'])
    
    total_branch = 0
    total_feeder = 0
    
    for floor in sorted(summary_data.keys(), key=lambda x: floor_order.get(x, 999)):
        branch_count = summary_data[floor]['Branch Panel']
        feeder_count = summary_data[floor]['Feeder Panel']
        total = branch_count + feeder_count
        writer.writerow([floor, branch_count, feeder_count, total])
        total_branch += branch_count
        total_feeder += feeder_count
    
    writer.writerow([])
    writer.writerow(['TOTALS', total_branch, total_feeder, total_branch + total_feeder])

# Create checklist format for field inspection
with open('Panel_Inspection_Checklist.csv', 'w', encoding='utf-8', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['MONTHLY PANEL VISUAL INSPECTION CHECKLIST'])
    writer.writerow([])
    writer.writerow(['Floor', 'Room', 'Panel Name', 'Panel Type', 'Voltage', 'Inspection Date', 'Inspected By', 'Condition', 'Notes/Issues'])
    
    for row in panels:
        writer.writerow([
            row['Floor'],
            row['Room Number'],
            row['Equipment Name/Label'],
            row['Equipment Type'],
            row['Voltage'],
            '',  # Inspection Date
            '',  # Inspected By
            '',  # Condition (to be filled in)
            ''   # Notes/Issues
        ])

print("✓ Panel_Inspection_Report.csv - Detailed panel listing")
print("✓ Panel_Inspection_Summary.csv - Summary by floor")
print("✓ Panel_Inspection_Checklist.csv - Blank checklist for monthly inspections")
print()
print(f"Total panels: {len(panels)}")
print(f"  - Branch Panels: {sum(1 for p in panels if p['Equipment Type'] == 'Branch Panel')}")
print(f"  - Feeder Panels: {sum(1 for p in panels if p['Equipment Type'] == 'Feeder Panel')}")
