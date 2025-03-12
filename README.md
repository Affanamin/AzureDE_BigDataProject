**Healthcare RCM Data Engineering Pipeline (Azure)**

This project implements an end-to-end Azure Data Engineering pipeline for Healthcare Revenue Cycle Management (RCM) using Medallion Architecture (Landing → Bronze → Silver → Gold).

Tech Stack:
Storage: Azure Data Lake Storage Gen2 (ADLS Gen2)
ETL & Orchestration: Azure Data Factory (ADF), Databricks
Data Processing: PySpark, Delta Lake, Unity Catalog
Security: Azure Key Vault, Linked Services
Data Sources: Azure SQL, APIs, JSON, CSV
Pipeline Overview:
Landing Zone: Raw CSV/JSON files are ingested.
Bronze Layer:
Ingest data from Azure SQL using ADF (parameterized ETL, incremental/full loads).
Store data in Parquet format (partitioned by Year/Month/Day) with Snappy compression.
Maintain an audit log (file count, records inserted).
Ingest NPI, ICD, and CPT data from APIs.
Silver Layer (Databricks):
Data Cleaning & Filtering
SCD Type 2 Implementation
Common Data Model (CDM) Integration
Delta Tables with Unity Catalog
Gold Layer:
Transform data into Fact & Dimension Models with foreign key relationships.
Additional Features:
Databricks Mount for ADLS Access
Secure Credentials via Key Vault
Metadata-driven ETL Processing
This project ensures a scalable, efficient, and secure data pipeline for handling healthcare data. 🚀
