# Databricks notebook source
# MAGIC %sql
# MAGIC CREATE TABLE IF NOT EXISTS tt_hc_adb_ws.gold.dim_provider
# MAGIC (
# MAGIC ProviderID string,
# MAGIC FirstName string,
# MAGIC LastName string,
# MAGIC DeptID string,
# MAGIC NPI long,
# MAGIC datasource string
# MAGIC )

# COMMAND ----------

# MAGIC %sql 
# MAGIC truncate TABLE tt_hc_adb_ws.gold.dim_provider 

# COMMAND ----------

# MAGIC %sql
# MAGIC insert into tt_hc_adb_ws.gold.dim_provider
# MAGIC select 
# MAGIC ProviderID ,
# MAGIC FirstName ,
# MAGIC LastName ,
# MAGIC concat(DeptID,'-',datasource) deptid,
# MAGIC NPI ,
# MAGIC datasource 
# MAGIC  from tt_hc_adb_ws.silver.providers
# MAGIC  where is_quarantined=false
