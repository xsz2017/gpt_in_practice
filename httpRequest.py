from langchain import PromptTemplate, OpenAI, LLMChain
from langchain.chains import LLMRequestsChain
from langchain.chat_models import AzureChatOpenAI
from langchain.chat_models import ChatOpenAI #直接访问OpenAI的GPT服务
import os

os.environ["OPENAI_API_KEY"]='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'
llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0) #直接访问OpenAI的GPT服务

def query_baidu(question):
      template = """Between >>> and <<< are the raw search result text from web.
      Extract the answer to the question '{query}' or say "not found" if the information is not contained.
      Use the format
      Extracted:<answer or "not found">
      >>> {requests_result} <<<
      Extracted:"""

      PROMPT = PromptTemplate(
          input_variables=["query", "requests_result"],
          template=template,
      )

      inputs = {
          "query": question,
          "url": "http://www.baidu.com/s?wd=" + question.replace(" ", "+")
      }
      requests_chain = LLMRequestsChain(llm_chain = LLMChain(llm=llm, prompt=PROMPT), output_key="query_info", verbose=True)
      res = requests_chain.run(inputs)
      return res

print(query_baidu("武汉未来3天天气？回答结果请去掉无关信息"))
