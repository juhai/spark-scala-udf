package com.example.scalaoperations

import org.apache.spark.sql.expressions.UserDefinedFunction
import org.apache.spark.sql.functions._

import com.example.operations.sparkoperations.JavaOperations.mySentenceSplitter
import com.example.operations.sparkoperations.JavaOperations.myTokeniser



object ScalaSparkUDF {
  def getSentenceSplitter(): UserDefinedFunction = udf(mySentenceSplitter _)
  def getTokeniser(): UserDefinedFunction = udf(myTokeniser _)
}
