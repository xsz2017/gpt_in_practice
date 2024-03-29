import openai
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
        engine=deployment, # engine = "deployment_name".
        temperature = 0,
        messages=[
            {"role":"system","content":prompt},
            {"role": "user", "content": input}
        ]
      )
    return (response.choices[0].message.content)

print(convert("100"))

print(convert("15,70,50,23"))