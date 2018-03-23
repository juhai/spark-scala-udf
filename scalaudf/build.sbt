name := "scalaudf"

version := "0.1"

scalaVersion := "2.11.12"

resolvers += Resolver.mavenLocal

libraryDependencies ++= Seq(
  "com.example.operations" % "sparkoperations" % "1.0-SNAPSHOT",
  "org.apache.spark" %% "spark-sql" % "2.3.0"
)
