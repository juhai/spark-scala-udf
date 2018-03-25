# spark-scala-udf

## Dowdload the HCCorpora files

```$bash
./setup.sh
``` 

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

This runs a word count task with one of the files in the database.

The operation is done using a Java functions defined in sparkoperations package. The interface is implemented in Scala in
scalaudf.
