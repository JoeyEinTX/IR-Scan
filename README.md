# Hospital Electrical Equipment Database - Documentation

## Overview
This project contains a comprehensive, cleaned, and organized database of all electrical equipment in the hospital, extracted and reformatted from the original IR scan text files.

## What Was Done

### 1. **Identified and Fixed Formatting Issues**
The original files had multiple inconsistencies:
- Mixed delimiters (tabs vs pipes)
- Inconsistent voltage notation (?, →, –)
- Markdown formatting (bold text with **)
- Incomplete entries (8th floor had truncated data)
- Inconsistent spacing and column names
- Different mounting descriptions

### 2. **Standardization Applied**
All cleaned files now use:
- **CSV format** with comma delimiters
- **Consistent voltage notation** using → (e.g., 480→208Y/120V)
- **Standardized mounting** descriptions (e.g., "Wall-mounted" not "Wall")
- **Removed markdown** formatting
- **Fixed incomplete** entries
- **Uniform column headers** across all files

## File Structure

### Original Files (Untouched)
- `IR Scan Ground.txt`
- `IR Scan 2nd Floor.txt` through `IR Scan 9th Floor.txt`
- `IR Scan - TEP Plant.txt`
- `Ground Floor Elec Rms ZL0.904E_ZL0.904E1.txt`

### Cleaned Source Files
- `IR Scan Ground_Cleaned.csv`
- `IR Scan 2nd Floor_Cleaned.csv` through `IR Scan 9th Floor_Cleaned.csv`
- `IR Scan TEP Plant_Cleaned.csv`
- `Ground Floor Elec Rms ZL0.904E_ZL0.904E1_Cleaned.csv`

### Master Database
**`Consolidated_Hospital_Equipment_Master.csv`** - Complete hospital equipment inventory
- **293 total equipment items**
- All floors consolidated into one file
- Standardized format ready for Excel, database import, or analysis

### Summary Reports
1. **`Summary_By_Equipment_Type.csv`**
   - 12 equipment types identified
   - Shows count and locations for each type

2. **`Summary_By_Floor.csv`**
   - 10 floors/areas covered
   - Breakdown by equipment category per floor

3. **`Emergency_Equipment_List.csv`**
   - 164 emergency (red-tagged) equipment items
   - Quick reference for critical systems

4. **`Summary_By_Voltage.csv`**
   - 10 different voltage levels
   - Count of equipment at each voltage

## Database Schema

Each record contains:
- **Floor** - Location (Ground, 2nd Floor, etc.)
- **Room Number** - Specific room/area identifier
- **Equipment Type** - Category (Transformer, Panel, Disconnect, etc.)
- **Equipment Name/Label** - Specific equipment identifier
- **Amperage/kVA** - Electrical rating
- **Voltage** - Operating voltage
- **Phase/Wire** - Electrical configuration (3P4W, etc.)
- **Fed From** - Power source/upstream equipment
- **Mounting** - Installation type (Wall-mounted, Floor-mounted, etc.)
- **System Type** - Emergency (generator-backed) or Normal (utility power)
- **Notes** - Additional information

## Equipment Statistics

- **Total Items**: 293
- **Emergency Equipment**: 164 (56%)
- **Equipment Types**: 12 distinct categories
- **Floors Covered**: 10 locations
- **Voltage Levels**: 10 different voltages

## Usage Recommendations

### For Maintenance Planning
- Use `Emergency_Equipment_List.csv` for prioritizing critical generator-backed equipment maintenance
- Use `Summary_By_Floor.csv` for floor-by-floor inspection planning
- Filter by "System Type" to separate Emergency (generator-backed) from Normal (utility) power systems

### For Database Import
- Use `Consolidated_Hospital_Equipment_Master.csv` for importing into:
  - Excel for filtering and analysis
  - Database systems (SQL, Access, etc.)
  - Asset management software
  - CMMS (Computerized Maintenance Management System)

### For Quick Reference
- Use `Summary_By_Equipment_Type.csv` to quickly find all equipment of a specific type
- Use `Summary_By_Voltage.csv` for voltage-specific work planning

## Next Steps

You can now:
1. **Import into Excel** - Open the consolidated CSV for sorting, filtering, and pivot tables
2. **Create reports** - Use the summary files for management presentations
3. **Database integration** - Import into your facility management system
4. **Further analysis** - Add maintenance schedules, warranty info, etc.

## Scripts Included

- `merge_csv.py` - Merges all cleaned files into master database
- `create_summaries.py` - Generates all summary reports

---
*Generated: November 13, 2025*
