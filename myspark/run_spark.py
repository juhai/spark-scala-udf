#!/usr/bin/env python3

from pyspark.sql import SparkSession
from pyspark.sql.column import Column, _to_java_column, _to_seq
from pyspark.sql.functions import column
from pyspark.sql.types import IntegerType

spark = SparkSession.builder.getOrCreate()


def do_dec_scala(col):
    _add_one = spark.sparkContext._jvm.com.example.scalaoperations.ScalaSparkUDF.getUDFDecrementByOne().apply
    print(_add_one)
    return Column(_add_one(_to_seq(spark.sparkContext, [col], _to_java_column)))


def do_add_scala(col):
    _add_one = spark.sparkContext._jvm.com.example.scalaoperations.ScalaSparkUDF.getUDFIncrementByOne().apply
    print(_add_one)
    return Column(_add_one(_to_seq(spark.sparkContext, [col], _to_java_column)))


def do_add_java(col):

    # This works
    spark.sparkContext._jvm.com.example.sparkoperations.SparkUDF.hello("Juha")

    # This does not work
    _add_one = spark.sparkContext._jvm.com.example.sparkoperations.SparkUDF().call
    return Column(_add_one(_to_seq(spark.sparkContext, [col], _to_java_column)))


def main():
    df = spark.createDataFrame(range(10), IntegerType())
    data_out_scala = (
        df
        .withColumn('value_inc', do_add_scala('value'))
        .withColumn('value_dec', do_dec_scala('value'))
    )
    print(data_out_scala)
    print(data_out_scala.collect())


if __name__ == '__main__':
    main()
