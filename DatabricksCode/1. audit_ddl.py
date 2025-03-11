# Databricks notebook source
# MAGIC %sql
# MAGIC CREATE SCHEMA IF NOT EXISTS audit;
# MAGIC --CREATE SCHEMA IF NOT EXISTS tt_hc_adb_ws.audit;

# COMMAND ----------

# MAGIC
# MAGIC %sql
# MAGIC CREATE TABLE IF NOT EXISTS audit.load_logs (
# MAGIC     data_source STRING,
# MAGIC     tablename STRING,
# MAGIC     numberofrowscopied INT,
# MAGIC     watermarkcolumnname STRING,
# MAGIC     loaddate TIMESTAMP
# MAGIC );

# COMMAND ----------

# MAGIC %sql
# MAGIC truncate table  audit.load_logs 

# COMMAND ----------

# MAGIC %sql 
# MAGIC select * from audit.load_logs limit 50;

# COMMAND ----------


