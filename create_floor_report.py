import csv
from collections import defaultdict, Counter

# Read the consolidated file
with open('Consolidated_Hospital_Equipment_Master.csv', 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    data = list(reader)

# Define floor order (TEP Plant at bottom, then Ground, then numbered floors)
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

# Group equipment by floor
equipment_by_floor = defaultdict(list)
for row in data:
    equipment_by_floor[row['Floor']].append(row)

# Sort floors according to our custom order
sorted_floors = sorted(equipment_by_floor.keys(), key=lambda x: floor_order.get(x, 999))

# Track grand totals by type
grand_totals = Counter()

# Create the Excel-friendly report
with open('Equipment_Report_By_Floor.csv', 'w', encoding='utf-8', newline='') as f:
    writer = csv.writer(f)
    
    # Write title
    writer.writerow(['HOSPITAL ELECTRICAL EQUIPMENT INVENTORY REPORT'])
    writer.writerow(['Organized by Floor with Equipment Type Breakdown'])
    writer.writerow([])  # Blank row
    
    total_count = 0
    
    # Process each floor
    for floor in sorted_floors:
        items = equipment_by_floor[floor]
        floor_count = len(items)
        total_count += floor_count
        
        # Count equipment types for this floor
        type_counts = Counter([item['Equipment Type'] for item in items])
        grand_totals.update(type_counts)
        
        # Floor header with total count
        writer.writerow([f'FLOOR: {floor}', f'Total Equipment: {floor_count}'])
        writer.writerow([])  # Blank row
        
        # Column headers
        writer.writerow(['Room Number', 'Equipment Type', 'Equipment Name/Label', 'Amperage/kVA', 
                        'Voltage', 'Phase/Wire', 'Fed From', 'Mounting', 'System Type', 'Notes'])
        
        # Write equipment for this floor
        for item in items:
            writer.writerow([
                item['Room Number'],
                item['Equipment Type'],
                item['Equipment Name/Label'],
                item['Amperage/kVA'],
                item['Voltage'],
                item['Phase/Wire'],
                item['Fed From'],
                item['Mounting'],
                item['System Type'],
                item['Notes']
            ])
        
        # Floor summary by equipment type
        writer.writerow([])
        writer.writerow(['FLOOR SUMMARY - Equipment by Type:'])
        for eq_type in sorted(type_counts.keys()):
            writer.writerow(['', eq_type, type_counts[eq_type]])
        writer.writerow(['', 'FLOOR TOTAL', floor_count])
        
        # Add blank rows between floors
        writer.writerow([])
        writer.writerow([])
    
    # Grand total section
    writer.writerow(['=' * 80])
    writer.writerow(['GRAND TOTAL - ALL FLOORS'])
    writer.writerow(['=' * 80])
    writer.writerow([])
    writer.writerow(['Equipment Type', 'Total Count'])
    for eq_type in sorted(grand_totals.keys()):
        writer.writerow([eq_type, grand_totals[eq_type]])
    writer.writerow([])
    writer.writerow(['GRAND TOTAL - ALL EQUIPMENT', total_count])
    writer.writerow(['=' * 80])

print(f"Created: Equipment_Report_By_Floor.csv")
print(f"\nFloor Order (basement to top):")
for floor in sorted_floors:
    count = len(equipment_by_floor[floor])
    print(f"  {floor}: {count} items")
print(f"\nGrand Total by Equipment Type:")
for eq_type in sorted(grand_totals.keys()):
    print(f"  {eq_type}: {grand_totals[eq_type]}")
print(f"\nGrand Total: {total_count} items")
print(f"\nThis file is ready to open in Excel!")
