import openai
import os

os.environ["OPENAI_API_KEY"]='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'

def convert(input):
    prompt = """
    按以下规则将0-100的数值，转化为A,B,C,D,E 5个等级:
    [80,100]之间 为 A
    [60,79]之间 为 B
    [40,59]之间 为 C
    [20,39]之间 为 D
    [0,19]之间 为 E
    仅输出数值对应的等级
    """
    response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    temperature = 0,
    messages=[
            {"role":"system","content":prompt},
            {"role": "user", "content": input}
        ]
      )
    return (response.choices[0].message.content)

# print(convert("100"))

# print(convert("15,70,50,23"))
message1="今天北京适合穿什么？一步步的思考，在你回答我的问题之前，请简要告诉我什么是Langchain的zeroShot"
message2="如果11 + 11 = 4， 12 + 12 = 6， 那么13 + 13是多少？一步步的思考"
response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    temperature = 0,
    messages=[
        {"role": "user", "content": message1,
        }
    ]
  )

  
print(response.choices[0].message.content)