# Databricks notebook source
# MAGIC %sql
# MAGIC CREATE TABLE IF NOT EXISTS tt_hc_adb_ws.gold.dim_department
# MAGIC (
# MAGIC Dept_Id string,
# MAGIC SRC_Dept_Id string,
# MAGIC Name string,
# MAGIC datasource string
# MAGIC )

# COMMAND ----------

# MAGIC %sql 
# MAGIC truncate TABLE tt_hc_adb_ws.gold.dim_department 

# COMMAND ----------

# MAGIC %sql
# MAGIC insert into tt_hc_adb_ws.gold.dim_department
# MAGIC select 
# MAGIC distinct
# MAGIC Dept_Id ,
# MAGIC SRC_Dept_Id ,
# MAGIC Name ,
# MAGIC datasource 
# MAGIC  from tt_hc_adb_ws.silver.departments
# MAGIC  where is_quarantined=false

# COMMAND ----------

# MAGIC %sql 
# MAGIC select * from tt_hc_adb_ws.gold.dim_department
