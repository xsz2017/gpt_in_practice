from langchain import PromptTemplate, OpenAI, LLMChain

from langchain.chat_models import AzureChatOpenAI
from langchain.chat_models import ChatOpenAI #

import os
#os.environ["OPENAI_API_TYPE"]='azure'
#os.environ["OPENAI_API_VERSION"]='2023-08-01-preview'
#os.environ["OPENAI_API_BASE"]='https://<Your EndPoint>/'
os.environ["OPENAI_API_KEY"]='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'
prompt_template = "What is a good name for a company that makes {product}? And only return the best one.，请用中文"
llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0) #直接访问OpenAI的GPT服务
# llm = AzureChatOpenAI(deployment_name = deployment, model_name=model, temperature=0, max_tokens=200) # 通过Azure的OpenAI服务
llm_chain = LLMChain(
    llm=llm,
    prompt=PromptTemplate.from_template(prompt_template)
)
a=llm_chain.run("鼠标")
print(a)
products = [{"product":"鞋子"},
            {"product":"'键盘"}, 
            {"product":"沐浴露"}]
names=llm_chain.apply(products)
print(names)