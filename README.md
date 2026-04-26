
#  E-commerce Data Pipeline (ETL Project)

##  Overview
This project demonstrates a complete end-to-end **ETL (Extract, Transform, Load) pipeline** built using Python.

It simulates a real-world e-commerce data system where raw transactional data is:
- Extracted from CSV files
- Cleaned and transformed using Python
- Loaded into a structured SQLite database for analytics

The goal is to convert messy raw data into analysis-ready structured data for business insights.

---

##  Project Objective
In real companies, e-commerce data comes from multiple sources and is often messy.  
This pipeline solves:

- Inconsistent data formatting  
- Missing values  
- Unstructured datasets  

And converts them into a clean, queryable database system.

---

##  Architecture

```

Raw CSV Data
↓
Extract (extract.py)
↓
Transform (transform.py)
↓
Cleaned Data (processed/)
↓
Load (load.py)
↓
SQLite Database (ecommerce.db)
↓
Data Analysis (SQL queries)

```

---

## Tech Stack

- Python 🐍  
- Pandas 📊  
- SQLite 🗄️  
- SQLAlchemy 🔗  

---

##  Project Structure

```

ecommerce_pipeline/
│
├── data/
│   ├── raw/                # Raw CSV files
│   ├── processed/          # Cleaned data output
│
├── scripts/
│   ├── extract.py          # Extract data from CSV
│   ├── transform.py        # Data cleaning & preprocessing
│   ├── load.py             # Load data into database
│   ├── db_check.py         # Verify database contents
│
├── ecommerce.db            # SQLite database
├── etl_process.py          # Main pipeline runner
├── README.md

````

---

##  ETL Pipeline Workflow

### Extract
- Reads raw e-commerce datasets (Orders, Customers)
- Loads them into Pandas DataFrames

### Transform
- Handles missing values
- Cleans inconsistent records
- Merges datasets for a unified view

### Load
- Stores processed data into SQLite database
- Enables SQL-based querying for analytics

---

##  How to Run

###  Step 1: Clone repository
```bash
git clone <your-repo-link>
cd ecommerce_pipeline
````

###  Step 2: Run ETL pipeline

```bash
python etl_process.py
```

###  Step 3: Verify database

```bash
python scripts/db_check.py
```

---

## Output

* Cleaned dataset stored in:

```
data/processed/cleaned_data.csv
```

* Structured database created:

```
ecommerce.db (SQLite)
```

* Ready for SQL-based business analytics

---

##  Skills Learned

* ETL pipeline development (Extract, Transform, Load)
* Data cleaning & preprocessing using Pandas
* SQL database integration (SQLite)
* Modular Python project structure
* Real-world data engineering workflow
* Debugging and pipeline execution

---

##  Business Use Case

This pipeline simulates how companies process raw e-commerce data to:

* Track customer behavior
* Analyze sales trends
* Generate business reports
* Support data-driven decision making

---

##  Future Improvements

* Add PostgreSQL / MySQL support
* Build dashboard using Power BI or Streamlit
* Automate pipeline using Apache Airflow
* Add logging & error tracking system
* Deploy as cloud-based ETL service

```


