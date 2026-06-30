# Databricks notebook source
# /// script
# [tool.databricks.environment]
# environment_version = "5"
# ///
# Inspecting the Data: The Five-Method Ritual

# step 1: show the first 5 rows
(
    pd.read_csv(path_1)
    .head()
)
# Step 2: returns the exact dimensions as a tuple (num_of_rows, num_of_columns)
(
    
    pd.read_csv(path_1)
    .shape()
)
# Step 3: print to the console information on the variables including count, memory usage, non-null and data type
(
    pd.read_csv(path_1)
    .info
)
# Step 4: a cleaner view of the type column
(
    pd.read_csv(path_1)
    .dtypes
)
# Step 5: produces a precise count of missing values per column.
(
    pd.read_csv(path_1)
    .isnull().sum()
)

# Section 2: Building a cleaning pipeline

# Step 1: Drop missing values
(
    pd.read_csv(path_1)
    .dropna()  # Remove rows where values are missing
    
)
# Step 2: The Complete Chain and saving the clean file
df1 = (
    pd.read_csv(path_1)
# 1. Drop rows with missing critical data
    .dropna()
# 2. Create clean numeric columns using `.assign()`
# We use 'lambda x' to refer to the data at this specific step in the chain
# We overwrite 'price_usd' by accessing the current df (x in our lambda function) and cleaning the string
    .assign(
        price_usd = lambda x: x["price_usd"]
                          .str.replace("$", "", regex=False)
                          .str.replace(",", "", regex=False)
                          .astype(float)
    )
)


# COMMAND ----------

import pandas as pd

# Define the path to our data file
path_1 = "wqu.mexico_housing.mexico_real_estate_1"
path_2 = "wqu.mexico_housing.mexico_real_estate_2"
path_3 = "wqu.mexico_housing.mexico_real_estate_3"

# COMMAND ----------

# Load the dataset using the variable we defined
(
    pd.read_csv(path_1)
)
