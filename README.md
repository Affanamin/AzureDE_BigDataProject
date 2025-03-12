<h1 align="center">Healthcare RCM Data Engineering Pipeline (Azure)</h1>
<p align="left">This project implements an <b>end-to-end Azure Data Engineering pipeline</b> for <b>Healthcare Revenue Cycle Management (RCM)</b> using  <b>Medallion Architecture</b> (Landing → Bronze → Silver → Gold).
<!-- <a href="https://www.python.org" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" alt="python" width="40" height="40"/> </a>
<a href="https://www.oracle.com/" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/oracle/oracle-original.svg" alt="oracle" width="40" height="40"/> </a>
<a href="https://kafka.apache.org/" target="_blank" rel="noreferrer"> <img src="https://www.vectorlogo.zone/logos/apache_kafka/apache_kafka-icon.svg" alt="kafka" width="40" height="40"/> </a> <a href="https://www.mysql.com/" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/mysql/mysql-original-wordmark.svg" alt="mysql" width="40" height="40"/> </a> -->
</p>
<h3 align="left">Tech Stack:</h3>

<ul>
  <li><b>Storage:</b> Azure Data Lake Storage Gen2 (ADLS Gen2)</li>
  <li><b>ETL & Orchestration:</b> Azure Data Factory (ADF), Databricks</li>
  <li><b>Data Processing:</b> PySpark, Delta Lake, Unity Catalog</li>
  <li><b>Security:</b> Azure Key Vault, Linked Services</li>
  <li><b>Data Sources:</b> Azure SQL, APIs, JSON, CSV</li>
</ul>

<h3 align="left">Pipeline Overview:</h3>

<ul>
  <li><b>Landing Zone:</b> Raw CSV/JSON files are ingested</li>
  <li><b>Bronze Layer:</b> 
    <ul> 
      <li>Ingest data from Azure SQL using ADF (parameterized ETL, incremental/full loads)</li>
      <li>Store data in <b>Parquet format</b> (partitioned by Year/Month/Day) with <b>Snappy compression</b></li>
      <li>Maintain an <b>audit log</b> (file count, records inserted)</li>
      <li>Ingest <b>NPI, ICD, and CPT data</b> from APIs</li></ul>
  </li>
  <li><b>Silver Layer (Databricks):</b> 
    <ul> 
      <li>Data <b>Cleaning & Filtering</b> </li>
      <li><b>SCD Type 2 </b> Implementation</li>
      <li><b>Common Data Model</b>  (CDM) Integration</li>
      <li><b>Delta Tables with Unity Catalog</b> </li></ul>
  </li>
  <li><b>Gold Layer (Databricks):</b> 
    <ul> 
      <li>Transform data into <b>Fact & Dimension Models</b> with foreign key relationships</li>
  </li>
</ul>

<h3 align="left">Additional Features:</h3>
<ul>
  <li><b>Databricks Mount for ADLS Access</b></li>
  <li><b>Secure Credentials via Key Vault</b></li>
  <li><b>Metadata-driven ETL Processing</b></li>
</ul>

<p align="left"> This project ensures a <b>scalable, efficient, and secure data pipeline</b> for handling healthcare data. 🚀 <a href="https://azure.microsoft.com/en-in/" target="_blank" rel="noreferrer"> <img src="https://www.vectorlogo.zone/logos/microsoft_azure/microsoft_azure-icon.svg" alt="azure" width="40" height="40"/> </a> <a href="https://www.python.org" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" alt="python" width="40" height="40"/> </a>  </p>

