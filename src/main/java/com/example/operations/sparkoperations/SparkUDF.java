package com.example.operations.sparkoperations;

import org.apache.spark.sql.api.java.UDF1;


public class SparkUDF implements UDF1<Integer, Integer> {
    /*
    Although this should be correct, Scala serialisation somehow does not work
     */
    public Integer call(Integer value) throws Exception {
        return value + 1;
    }

    /*
    This on the other works fine but that's expected. Shows just how easy it is to call Java from Python
     */
    public static void hello(String name) {
        System.out.println("hello " + name);
    }
}