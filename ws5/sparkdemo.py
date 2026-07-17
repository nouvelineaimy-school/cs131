import sys
# A1
from pyspark.sql import SparkSession
from pyspark.ml.feature import VectorAssembler
from pyspark.ml import Pipeline
from pyspark.ml.regression import LinearRegression
from pyspark.ml.evaluation import RegressionEvaluator
ws5_regression = SparkSession.builder.appName("ws5-regression").getOrCreate()

# A2
path = sys.argv[1]
df = ws5_regression.read.csv(path, header=True, inferSchema=True)
df.show()

# A3
VecAssembler = VectorAssembler(inputCols=["total_bill","size"], outputCol="features"
)

# A4
trainDF, testDF = df.randomSplit([.8, .2], seed=3)

#A5
lr = LinearRegression(featuresCol="features", labelCol="tip")
vecTrainDF = VecAssembler.transform(trainDF)
lrModel = lr.fit(vecTrainDF)
pipeline = Pipeline(stages=[VecAssembler, lr])
pipelineModel = pipeline.fit(trainDF)

# A6
predDF = pipelineModel.transform(testDF)
predDF.show(10)

#A7
regressionEvaluator = RegressionEvaluator(
        predictionCol="prediction",
        labelCol="tip",
        metricName="rmse")
rmse = regressionEvaluator.evaluate(predDF)
regressionEvaluator.setMetricName("r2")
r2 = regressionEvaluator.evaluate(predDF)

# A8
lrModel = pipelineModel.stages[-1]
m = round(lrModel.coefficients[0], 2)
b = round(lrModel.intercept, 2)
print(f"Coefficients: {m}")
print(f"Intercept: {b}")
print(f"RMSE: {rmse}")
print(f"R2: {r2}")

