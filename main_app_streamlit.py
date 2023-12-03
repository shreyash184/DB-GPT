import streamlit as st 
import dbConnect 
import pandas as pd
from prompts.prompts import SYSTEM_MESSAGE
import openai_test 
import json

def query_database(query):
    return pd.read_sql_query(query, conn)

conn = dbConnect.create_connection()

schemas = dbConnect.get_schema_representation()

st.title("SQL Query Generator with GPT-3.5-turbo")
st.write("enter your message to generate SQL and view results.")

user_message = st.text_input("Enter your message: ")

if user_message:
    formatted_system_message = SYSTEM_MESSAGE.format(schema=schemas['employees'])

    response = openai_test.get_response(formatted_system_message, user_message)
    json_response = json.loads(response)
    query = json_response['query']

    st.write("Generated SQL Query: ")
    st.code(query, language="sql")

    try:
        sql_results = query_database(query)
        st.write("Query Results: ")
        st.dataframe(sql_results)
    except Exception as e:
        st.write(f"An error occured: {e}")