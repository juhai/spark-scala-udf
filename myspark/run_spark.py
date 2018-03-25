#!/usr/bin/env python3

from pyspark.sql import SparkSession
from pyspark.sql.column import Column, _to_java_column, _to_seq
from pyspark.sql.functions import column, size, explode, lit
from pyspark.sql.types import IntegerType

spark = SparkSession.builder.getOrCreate()


def do_split(col):
    _add_one = spark.sparkContext._jvm.com.example.scalaoperations.ScalaSparkUDF.getSentenceSplitter().apply
    print(_add_one)
    return Column(_add_one(_to_seq(spark.sparkContext, [col], _to_java_column)))


def do_tokenise(col):
    _add_one = spark.sparkContext._jvm.com.example.scalaoperations.ScalaSparkUDF.getTokeniser().apply
    print(_add_one)
    return Column(_add_one(_to_seq(spark.sparkContext, [col], _to_java_column)))


def do_add_java(col):

    # This works
    spark.sparkContext._jvm.com.example.sparkoperations.SparkUDF.hello("Juha")

    # This does not work
    _add_one = spark.sparkContext._jvm.com.example.sparkoperations.SparkUDF().call
    return Column(_add_one(_to_seq(spark.sparkContext, [col], _to_java_column)))


def main():
    df = spark.read.text('/var/tmp/coursera-data/final/en_US/en_US.news.txt')
    # df = spark.createDataFrame(range(int(1e6)), IntegerType())
    data_out_scala = (
        df
        .withColumn('sentences', do_split('value'))
        .select(explode(column('sentences')).alias('sentence'))
        .withColumn('tokens', do_tokenise('sentence'))
        .select(explode(column('tokens')))
        .groupBy('col')
        .count()
        .orderBy('count', ascending=False)
    )
    data_out_scala.show()


if __name__ == '__main__':
    main()
