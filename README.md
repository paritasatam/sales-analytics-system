# bitsom_ba_2507609 sales-analytics-system
**Student Name:** Parita Satam
**Student Code:** bitsom_ba_2507609
**Email:** satamparita@gmail.com
**Date:** 20/01/2026

## Sales Data Analytics System

A comprehensive Python system for processing, analyzing, and reporting on sales data. This system handles messy sales transaction files, cleans data according to business rules, performs analysis, and integrates with external APIs for product enrichment.

## Features
Data Cleaning: Automatically detects and removes invalid records 

Data Validation: Enforces business rules (positive quantities, valid IDs, etc.)

Sales Analysis: Provides regional, product-wise, and customer analysis

API Integration: Fetches real-time product information

Report Generation: Creates comprehensive JSON and text reports

Error Handling: Robust error handling and logging





# Setup and Execution

Python version: 3.7 or higher

Required libraries are listed in requirements.txt

# To execute the complete workflow:

python main.py

This command performs data cleaning, analytics, API enrichment, and report generation in a single run.

# Output Artifacts

sales_data_cleaned.txt: Validated and cleaned sales records

invalid_records.txt: Records excluded during validation

enriched_sales_data.txt: Cleaned data enhanced with API attributes

sales_report.txt: Comprehensive analytical report



# Repository Structure
sales-analytics-system/
  ├── README.md
  ├── main.py
  ├── utils/
  │   ├── file_handler.py
  │   ├── data_processor.py
  │   └── api_handler.py
  ├── data/
  │   └── sales_data.txt (provided)
  ├── output/
  └── requirements.txt


