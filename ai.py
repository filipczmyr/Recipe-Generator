from openai import OpenAI

def Ai(question, key):
    client = OpenAI(
        api_key=key,
)
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": question,
            }
        ],    
        model="gpt-3.5-turbo",
    )   
    return chat_completion.choices[0].message.content

