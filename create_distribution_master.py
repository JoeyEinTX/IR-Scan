import csv

# Read the consolidated file
with open('Consolidated_Hospital_Equipment_Master.csv', 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    data = list(reader)

# Define equipment types to exclude (elevator-specific components)
excluded_types = ['DC Output Filter', 'Resistor Box']

# Filter to only distribution equipment
distribution_equipment = [row for row in data if row['Equipment Type'] not in excluded_types]

# Define floor order (TEP Plant at bottom/basement, then Ground, then numbered floors)
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

# Sort equipment by floor order
distribution_equipment.sort(key=lambda x: floor_order.get(x['Floor'], 999))

# Write the filtered master list
with open('Distribution_Equipment_Master.csv', 'w', encoding='utf-8', newline='') as f:
    if distribution_equipment:
        fieldnames = distribution_equipment[0].keys()
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(distribution_equipment)

print(f"Created: Distribution_Equipment_Master.csv")
print(f"Total Distribution Equipment: {len(distribution_equipment)} items")
print(f"\nExcluded Items: {len(data) - len(distribution_equipment)}")
print(f"  - DC Output Filter: 5 items")
print(f"  - Resistor Box: 1 item")
print(f"\nOriginal Total: {len(data)} items")
