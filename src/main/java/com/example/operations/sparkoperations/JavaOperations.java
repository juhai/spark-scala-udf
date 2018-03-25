package com.example.operations.sparkoperations;

import scala.collection.JavaConverters;
import scala.collection.Seq;

import static java.util.Arrays.asList;

public class JavaOperations {

    public static Seq<String> mySentenceSplitter(String text) {
        String[] sentences = text.split("[.?!]");
        return JavaConverters.asScalaIteratorConverter(asList(sentences).iterator()).asScala().toSeq();
    }

    public static Seq<String> myTokeniser(String text) {
        String[] sentences = text.split(" ");
        return JavaConverters.asScalaIteratorConverter(asList(sentences).iterator()).asScala().toSeq();
    }
}
