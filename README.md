# Poker Data Warehouse & Analytics

## 📌 Project Overview
A data engineering project focused on building an ETL pipeline to load raw poker tournament data into an SQLite database. This project demonstrates database design, advanced SQL querying, and data-driven insights on player behavior.

## 🛠️ Tech Stack
- **Language:** Python
- **Data Processing:** Pandas
- **Database:** SQLite3, SQL (Window Functions, Aggregations)
- **Tools:** Git, VS Code, MacOS

## 🔄 Pipeline Workflow
1. **Data Exploration (`src/explore.py`):** Loaded raw CSV data and inspected schema, missing values, and data types.
2. **Data Ingestion (`src/load_to_db.py`):** Built a Python ETL script to clean and load raw records into an SQLite database (`poker.db`).
3. **SQL Analytics (`sql/queries.sql`):** Applied advanced SQL to analyze player performance, ROI, and risk factors.

## 📊 Key Insights
Based on the analysis of 45,000 records:

1. **Skill & Profitability:** Players who ended up profitable (`profitable=1`) had an average `skill` score of **5.94**, compared to **4.78** for losing players. This confirms that technical skill is the primary driver of financial success.
2. **Emotional Control:** Using `tilt_control` as a proxy for emotional stability, profitable players scored **5.56** on average, while losing players scored **4.92**. This demonstrates that risk management and psychological stability are just as important as raw skill.
3. **Data Pipeline Execution:** Built a robust SQLite data warehouse to ingest and query 45,000 records, showcasing end-to-end data engineering proficiency.

## 🚀 How to Run
1. Clone the repository and navigate to the project directory.
2. Run the data loading script:
   ```bash
   python3 src/load_to_db.py