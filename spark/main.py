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

# remove any row where any col of that row is null 
df.na.drop().show() # same as df.na.drop(how="any").show()

# remove any row where all the col values are null 
df.na.drop(how="all").show()

# indicate how many non-null values should be in any row 
df.na.drop(how="all", thresh=2).show()

# drop entire row if this col is null
df.na.drop(how="all", subset=["tip"]).show()

# fill cols that are null with the keyword passed. only works for same datatype. 
df.na.fill("Missing").show()

# explicitly fill missing values by supplying the column names
df.na.fill("Missing", ["sex", "day"]).show()


### Filling with mean values with an imputer
from pyspark.ml.feature import Imputer
### Create an imputer object
imputer = Imputer(
          inputCols= ["total_bill", "tip"],
          outputCols = ["{}_imputed".format(c) for c in ["total_bill", "tip"]]
    ).setStrategy("mean")
### Fit imputer on Data Frame and Transform it
imputer.fit(df).transform(df).show()

# filter based on condition 
df.filter("tip <= 2").show(5)

# filter and select
df.filter("tip <= 2").select(["total_bill", "tip"]).show(5)

# two filtering conditions 
df.filter((df["tip"] <= 1) | (df["tip"] >= 5)).select(["total_bill", "tip"]).show(5)

# ignore observaitons where tip<=2
df.filter(~(df["tip"] <= 2)).select(["total_bill", "tip"]).show(5)

# Groupby sex and performing sum -> return a df of two rows: male, female. col will show the sum of each int colums. 
df.groupBy("sex").sum().show()

# Group by day, max tip
df.groupBy("day").max().select(["day", "max(tip)"]).show()

# count number of objesrvations for each category 
df.groupBy("day").count().show()

# can get similar results by supplying the col as key and functionality as a value 
df.agg({"tip": "sum"}).show()

# caluclate the sum of tip and maximun of total_bill for each gender
df.groupBy("sex").agg({"tip": "sum", "total_bill": "max"}).show()

# close the spark session 
spark.stop()