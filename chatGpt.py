

import openai

# 设置OpenAI API的访问密钥
openai.api_key = "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"


# 创建一个对话历史列表
conversation_history = []

while True:
    # 获取用户输入
    user_input = input("You: ")
    
    # 将用户输入添加到对话历史中
    conversation_history.append({"role": "user", "content": user_input})
    
    # 使用 OpenAI API 生成响应
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        #控制响应的随机性和创造性。值越高,响应越随机和创造性。通常取值范围为 0 到 1 之间。默认值为 1
        temperature=0.8 ,
        max_tokens=100,  # 限制最大 token 数为 100
        messages=conversation_history
    )
    # 循环遍历所有候选响应
    for i, choice in enumerate(response.choices):
        print(f"候选响应 {i+1}:")
        print(choice.message["content"])
        print()
    # 获取 AI 助手的响应
    ai_response = response.choices[0].message["content"]
    
    # 将 AI 助手的响应添加到对话历史中
    conversation_history.append({"role": "assistant", "content": ai_response})
    
    # 打印 AI 助手的响应
    print("ChatGPT: " + ai_response)
    
    # 检查是否要退出对话
    if user_input.lower() == "exit":
        break