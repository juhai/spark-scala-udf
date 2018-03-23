# spark-scala-udf
Simple examples on how to use Scala UDF from pyspark

```
  mvn clean install
  (cd scalaudf && sbt package)
  cd myspark
  pip install -r requirements.txt
  spark-submit --master local[*] \
    --driver-class-path $(dirname $(pwd))/scalaudf/target/scala-2.11/scalaudf_2.11-0.1.jar:$(dirname $(pwd))/target/sparkoperations-1.0-SNAPSHOT.jar \
    run_spark.py
```

This runs simple task with a dataframe with numbers from 0..9, by adding one column with val++ and one column with val--.
The operation is done using a Java function defined in sparkoperations package. The interface is implemented in Scala in
scalaudf.
