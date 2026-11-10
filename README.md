# Pandas Sales ETL Pipeline

A beginner-friendly ETL (Extract, Transform, Load) project built using Python and Pandas.

## Project Overview

This project demonstrates how to build a simple ETL pipeline that extracts data from multiple CSV files, cleans and validates the data, integrates datasets, and saves the processed output into CSV files.

## Technologies Used

- Python
- Pandas
- CSV
- Git and GitHub

## Project Structure

```text
pandas-sales-etl/
│
├── data/
│   ├── raw/
│   │   ├── customers.csv
│   │   ├── products.csv
│   │   └── orders.csv
│   │
│   ├── processed/
│   └── rejected/
│
├── main.py
├── requirements.txt
├── .gitignore
└── README.md
```

## ETL Pipeline

### 1. Extract
- Read customer, product, and order data from CSV files using Pandas.

### 2. Transform
- Remove duplicate records.
- Handle missing values.
- Standardize text data.
- Validate customer and product IDs.
- Identify invalid records.
- Merge multiple datasets using Pandas.

### 3. Load
- Export processed data into CSV files.
- Store rejected orders separately for further investigation.

## Data Validation

The project uses Pandas `.isin()` to validate foreign-key relationships between orders, customers, and products.

Invalid records are separated from valid records to prevent incorrect data from entering the final dataset.

## How to Run

### 1. Clone the repository

```bash
git clone https://github.com/FaisalFazal5432/pandas-sales-etl.git
```

### 2. Navigate to the project directory

```bash
cd pandas-sales-etl
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the pipeline

```bash
python main.py
```

## Project Goal

The goal of this project is to understand fundamental Data Engineering concepts by building a practical ETL pipeline using Python and Pandas.

## Author

Faisal
