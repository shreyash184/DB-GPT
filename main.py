import dbConnect
from prompts.prompts import SYSTEM_MESSAGE
import openai_test
import json
import pandas as pd

def query_datanase(query):
    return pd.read_sql_query(query, conn)

conn = dbConnect.create_connection()

schemas = dbConnect.get_schema_representation()

productSchema = schemas['products']
orderSchema = schemas['orders']
# formated the system message with schema
formatted_system_message = SYSTEM_MESSAGE.format(productSchema, orderSchema)
print(formatted_system_message)

user_message = "Show me all employee names which has salary more thatn 5000"

response = openai_test.get_response(formatted_system_message, user_message)
print(response)

json_response = json.loads(response)
query = json_response['query']
print(query)


sql_results = query_datanase(query)
print(sql_results)

