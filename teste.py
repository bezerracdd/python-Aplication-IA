import os
import sys

# Ajuste esses caminhos conforme o seu sistema
os.environ["JAVA_HOME"] = "/usr/lib/jvm/java-11-openjdk" # Exemplo: confirme com o comando acima
os.environ["SPARK_HOME"] = "/opt/spark" # Onde você instalou o Spark

# Adiciona o Spark ao Path do Python
sys.path.append(os.path.join(os.environ["SPARK_HOME"], "python"))
sys.path.append(os.path.join(os.environ["SPARK_HOME"], "python/lib/py4j-0.10.9.7-src.zip")) # Verifique a versão do py4j na pasta lib
from pyspark.sql import SparkSession

# Caminho absoluto para o seu JAR
jar_path = "/home/dsadb/postgresql-42.7.2.jar"

spark = SparkSession.builder \
    .appName("ConexaoPostgres") \
    .config("spark.jars", jar_path) \
    .getOrCreate()

# Configurações de conexão
properties = {
    "user": "dsadb_user",
    "password": "senha123", # a senha que você definiu no psql
    "driver": "org.postgresql.Driver"
}

url = "jdbc:postgresql://localhost:5432/vendas_spark"

# Testando a leitura (vai dar erro se a tabela não existir, o que é normal agora)
try:
    df = spark.read.jdbc(url=url, table="despachantes", properties=properties)
    df.show()
except Exception as e:
    print("Conectado com sucesso, mas a tabela ainda não existe!")