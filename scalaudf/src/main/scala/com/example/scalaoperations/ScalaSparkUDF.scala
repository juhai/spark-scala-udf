package com.example.scalaoperations

import org.apache.spark.sql.expressions.UserDefinedFunction
import org.apache.spark.sql.functions._

import com.example.operations.sparkoperations.JavaOperations.addByOne
import com.example.operations.sparkoperations.JavaOperations.decByOne

object ScalaSparkUDF {
  def getUDFIncrementByOne(): UserDefinedFunction = udf(addByOne _)
  def getUDFDecrementByOne(): UserDefinedFunction = udf(decByOne _)
}
