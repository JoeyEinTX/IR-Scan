import csv
from collections import defaultdict

# Read the consolidated file
with open('Consolidated_Hospital_Equipment_Master.csv', 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    data = list(reader)

# Summary by Equipment Type
equipment_by_type = defaultdict(list)
for row in data:
    equipment_by_type[row['Equipment Type']].append(row)

with open('Summary_By_Equipment_Type.csv', 'w', encoding='utf-8', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['Equipment Type', 'Count', 'Locations'])
    for eq_type in sorted(equipment_by_type.keys()):
        count = len(equipment_by_type[eq_type])
        locations = set([f"{row['Floor']} - {row['Room Number']}" for row in equipment_by_type[eq_type]])
        writer.writerow([eq_type, count, '; '.join(sorted(locations)[:5]) + ('...' if len(locations) > 5 else '')])

# Summary by Floor
equipment_by_floor = defaultdict(list)
for row in data:
    equipment_by_floor[row['Floor']].append(row)

with open('Summary_By_Floor.csv', 'w', encoding='utf-8', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['Floor', 'Total Equipment Count', 'Transformers', 'Panels', 'Disconnects', 'Other'])
    for floor in sorted(equipment_by_floor.keys()):
        items = equipment_by_floor[floor]
        transformers = sum(1 for item in items if 'Transformer' in item['Equipment Type'])
        panels = sum(1 for item in items if 'Panel' in item['Equipment Type'])
        disconnects = sum(1 for item in items if 'Disconnect' in item['Equipment Type'])
        other = len(items) - transformers - panels - disconnects
        writer.writerow([floor, len(items), transformers, panels, disconnects, other])

# Emergency Equipment (Emergency System Type)
emergency_equipment = [row for row in data if row['System Type'] == 'Emergency']
with open('Emergency_Equipment_List.csv', 'w', encoding='utf-8', newline='') as f:
    fieldnames = ['Floor', 'Room Number', 'Equipment Type', 'Equipment Name/Label', 'Amperage/kVA', 'Voltage', 'System Type', 'Fed From', 'Notes']
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    for row in emergency_equipment:
        writer.writerow({field: row[field] for field in fieldnames})

# Equipment by Voltage
voltage_summary = defaultdict(int)
for row in data:
    voltage = row['Voltage'].strip()
    if voltage:
        voltage_summary[voltage] += 1

with open('Summary_By_Voltage.csv', 'w', encoding='utf-8', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['Voltage', 'Equipment Count'])
    for voltage in sorted(voltage_summary.keys()):
        writer.writerow([voltage, voltage_summary[voltage]])

print(f"Created summary files:")
print(f"  - Summary_By_Equipment_Type.csv ({len(equipment_by_type)} types)")
print(f"  - Summary_By_Floor.csv ({len(equipment_by_floor)} floors)")
print(f"  - Emergency_Equipment_List.csv ({len(emergency_equipment)} items)")
print(f"  - Summary_By_Voltage.csv ({len(voltage_summary)} voltages)")
print(f"Total equipment items: {len(data)}")
