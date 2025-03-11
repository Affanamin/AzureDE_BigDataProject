# Databricks notebook source
# MAGIC %sql
# MAGIC CREATE TABLE IF NOT EXISTS tt_hc_adb_ws.gold.dim_cpt_code
# MAGIC (
# MAGIC cpt_codes string,
# MAGIC procedure_code_category string,
# MAGIC procedure_code_descriptions string,
# MAGIC code_status string,
# MAGIC refreshed_at timestamp
# MAGIC )

# COMMAND ----------

# MAGIC %sql 
# MAGIC truncate TABLE tt_hc_adb_ws.gold.dim_cpt_code 

# COMMAND ----------

# MAGIC %sql
# MAGIC insert into tt_hc_adb_ws.gold.dim_cpt_code
# MAGIC select 
# MAGIC cpt_codes,
# MAGIC procedure_code_category,
# MAGIC procedure_code_descriptions ,
# MAGIC code_status,
# MAGIC current_timestamp() as refreshed_at
# MAGIC  from tt_hc_adb_ws.silver.cptcodes
# MAGIC  where is_quarantined=false and is_current=true

# COMMAND ----------

# MAGIC %sql 
# MAGIC select * from tt_hc_adb_ws.gold.dim_cpt_code
