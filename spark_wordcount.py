from pyspark.sql import SparkSession
import nltk
import re
import time

spark = SparkSession.builder\
  .master("local[*]")\
  .appName("WordCount")\
  .getOrCreate()

sc=spark.sparkContext 

start_time = time.time()

review_rdd = sc.textFile("hdfs:///Books_review.csv")
review_rdd = review_rdd.map(lambda x: re.sub(r'\t', '', x))
review_rdd = review_rdd.map(lambda x: re.sub(r'[^\w\s]', '', x))

review_rdd = review_rdd.flatMap(lambda line: line.split(" "))
review_rdd = review_rdd.filter(lambda x:x!='')
review_count = review_rdd.map(lambda word: (word, 1))
review_wc = review_count.reduceByKey(lambda x , y : (x+y))

review_wc.saveAsTextFile('hdfs:///spark_wordcount_output.csv')

#Display the execution time for pyspark
end_time = time.time()
execution_time = end_time - start_time
print("Execution time: {:.2f} seconds".format(execution_time))

sc.stop()
