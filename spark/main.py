import pyspark
from pyspark.sql import SparkSession
import pandas as pd

spark = SparkSession.builder.appName("Introduction to Spark").getOrCreate()

df = spark.read.csv("tips.csv", header=True, inferSchema=True) #inferSchema infers the data types

# print df
df.show(5) # or df.head()
print()

# print schema / types / nullability 
df.printSchema()
print()

# return cols as a list of strs
print(df.columns)
print()

# select col 
df.select("sex").show(5)
print()

# select cols 
df.select(["sex", "tip"]).show(5)
print()

# print count, mean, stddev, min, max
df.describe().show() 
print()

# create a new col 
df = df.withColumn("tip_bill_ratio", (df["tip"]/df["total_bill"])*100)
print()

# print df 
df.show(5)
print()

# drop a col 
df = df.drop("tip_bill_ratio")
print()

# rename cols 
df.withColumnRenamed("sex", "gender").show(5)