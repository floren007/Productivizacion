from databricks.connect import DatabricksSession as SparkSession
from databricks.sdk.core import Config
from utils import read_yaml
from datetime import datetime
if __name__ == "__main__":
    config = Config(profile="DEFAULT", cluster_id="0720-124253-8h00x845")
    spark = SparkSession.builder.sdkConfig(config).getOrCreate()
    spark.sql("show databases").show()

    # 2.- yaml con todos los parametros
    config = read_yaml()

    # 3.- fecha de ejecucion del proceso completso
    exec_time = datetime.now()
    exec_time = exec_time.strftime('%Y-%m-%dT%H:%M:%S')
    print(f'Fecha de ejecucion {exec_time}')
