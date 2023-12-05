from openai import OpenAI


# print(os.environ)




# completion = client.chat.completions.create(
#   model="gpt-3.5-turbo",
#   messages=[
#     {"role": "system", "content": "who developed you?"}
#   ]
# )

# print(completion.choices[0].message.content)

def get_response(system_message, user_message):
    client = OpenAI(api_key="<API_KEY>")

    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": system_message},
            {"role": 'user', 'content': f"{user_message}"}
        ]
    )
    return completion.choices[0].message.content

# if __name__ == "__main__":
#     system_message = "You are a helpful assistant"
#     user_message = "Hello, how are you ?"
#     print(get_response(system_message, user_message))