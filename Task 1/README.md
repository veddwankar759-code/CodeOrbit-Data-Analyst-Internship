# Data Cleaning Using Microsoft Excel

## Project Overview

This project was completed as part of the **CodeOrbit Tech Data Analyst Internship**.

The objective was to clean and organize a sales dataset by identifying duplicate records, inconsistent text formatting, extra whitespace, mixed date formats, and currency formatting issues.

## Dataset Description

The dataset contains sales transaction records with information about orders, customers, products, pricing, discounts, payment methods, and salespersons.

**Dataset details:**
- Original records: 57 rows
- Cleaned records: 55 rows
- Original columns: 13
- Cleaned columns: 14

## Tools Used

- Microsoft Excel
- Excel functions: `TRIM`, `PROPER`, and `SUBSTITUTE`
- Find and Replace
- Text to Columns

## Data Cleaning Steps

### 1. Duplicate Records
Identified and removed duplicate order records using Excel's Remove Duplicates feature.

### 2. Extra Whitespace
Used the `TRIM` function to remove unnecessary spaces from text fields, including customer names and region values.

### 3. Inconsistent Capitalization
Standardized text capitalization using `PROPER` and `TRIM` where appropriate.

### 4. Date Standardization
Standardized mixed date formats into a consistent `yyyy-mm-dd` format using Text to Columns and formulas.

### 5. Currency Formatting
Used Find and Replace and `SUBSTITUTE` to remove currency symbols and commas from price values where required.

### 6. Total Sales Calculation
Added a `Total_Sales` column to the cleaned dataset to represent the calculated sales amount after applying the discount.

## Files Included

- `sales_data.csv` — Original dataset before cleaning.
- `sales_data_cleaned.xlsx` — Cleaned dataset with standardized values and the calculated `Total_Sales` column.
- `cleaning_log.xlsx` — Documentation of the identified issues and fixes applied.
- `README.md` — Project documentation.

## Outcome

The dataset was organized into a consistent format for further analysis. Duplicate records were removed, text formatting was standardized, dates were made consistent, and a total sales field was added.

The cleaned dataset was subsequently used for sales analysis and visualization.

## Internship

**Organization:** CodeOrbit Tech  
**Role:** Data Analyst Intern  
**Task:** Data Cleaning using Excel
