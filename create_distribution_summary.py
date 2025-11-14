import csv
from collections import Counter

# Read the consolidated file
with open('Consolidated_Hospital_Equipment_Master.csv', 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    data = list(reader)

# Define equipment types to exclude (elevator-specific components)
excluded_types = ['DC Output Filter', 'Resistor Box']

# Filter to only distribution equipment
distribution_equipment = [row for row in data if row['Equipment Type'] not in excluded_types]

# Count by equipment type
type_counts = Counter([item['Equipment Type'] for item in distribution_equipment])

# Create summary report
with open('Electrical_Distribution_Equipment_Summary.csv', 'w', encoding='utf-8', newline='') as f:
    writer = csv.writer(f)
    
    # Title
    writer.writerow(['ELECTRICAL DISTRIBUTION & CONTROL EQUIPMENT SUMMARY'])
    writer.writerow(['Hospital-wide inventory excluding elevator drive components'])
    writer.writerow([])
    
    # Headers
    writer.writerow(['Equipment Type', 'Count', 'Percentage'])
    
    total = len(distribution_equipment)
    
    # Sort by count (descending)
    for eq_type in sorted(type_counts.keys(), key=lambda x: type_counts[x], reverse=True):
        count = type_counts[eq_type]
        percentage = f"{(count/total*100):.1f}%"
        writer.writerow([eq_type, count, percentage])
    
    writer.writerow([])
    writer.writerow(['TOTAL DISTRIBUTION EQUIPMENT', total, '100.0%'])
    writer.writerow([])
    writer.writerow(['Excluded from this summary:'])
    
    # Show excluded items
    excluded_equipment = [row for row in data if row['Equipment Type'] in excluded_types]
    excluded_counts = Counter([item['Equipment Type'] for item in excluded_equipment])
    for eq_type in sorted(excluded_counts.keys()):
        writer.writerow([f'  {eq_type} (Elevator Components)', excluded_counts[eq_type], 'N/A'])
    
    writer.writerow([])
    writer.writerow(['GRAND TOTAL - ALL EQUIPMENT', len(data), ''])

print(f"Created: Electrical_Distribution_Equipment_Summary.csv")
print(f"\nElectrical Distribution Equipment: {total} items")
print(f"\nBreakdown:")
for eq_type in sorted(type_counts.keys(), key=lambda x: type_counts[x], reverse=True):
    count = type_counts[eq_type]
    percentage = f"{(count/total*100):.1f}%"
    print(f"  {eq_type}: {count} ({percentage})")
print(f"\nExcluded (Elevator Components): {len(excluded_equipment)} items")
for eq_type in sorted(excluded_counts.keys()):
    print(f"  {eq_type}: {excluded_counts[eq_type]}")
print(f"\nGrand Total: {len(data)} items")
