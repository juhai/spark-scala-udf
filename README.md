# spark-scala-udf
Simple examples on how to use Scala UDF from pyspark

  mvn clean install
  (cd scalaudf && sbt package)
  cd myspark
  spark-submit --master local[*] \
    --driver-class-path ../scalaudf/target/scala-2.11/scalaudf_2.11-0.1.jar:../target/sparkoperations-1.0-SNAPSHOT.jar \
    run_spark.py

