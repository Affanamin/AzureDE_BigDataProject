# Databricks notebook source
# %sql
# CREATE CATALOG tt_hc_adb_ws
# MANAGED LOCATION 'abfss://unity-catalog-storage@dbstorageou6dicfq6jvd2.dfs.core.windows.net/2538088739818750';



# COMMAND ----------

# %sql
# CREATE SCHEMA IF NOT EXISTS tt_hc_adb_ws.audit;

# CREATE TABLE IF NOT EXISTS tt_hc_adb_ws.audit.load_logs (
#     data_source STRING,
#     tablename STRING,
#     numberofrowscopied INT,
#     watermarkcolumnname STRING,
#     loaddate TIMESTAMP
# );

# COMMAND ----------

# %sql
# truncate table  tt_hc_adb_ws.audit.load_logs 

# COMMAND ----------

# MAGIC %sql
# MAGIC select * from tt_hc_adb_ws.audit.load_logs limit 20;

# COMMAND ----------

# MAGIC %sql
# MAGIC CREATE SCHEMA IF NOT EXISTS tt_hc_adb_ws.silver;

# COMMAND ----------

# MAGIC %sql
# MAGIC CREATE SCHEMA IF NOT EXISTS tt_hc_adb_ws.gold;

# COMMAND ----------


