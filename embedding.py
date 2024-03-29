from langchain.embeddings.openai import OpenAIEmbeddings
import numpy as np
embedding = OpenAIEmbeddings() #如果直接使用OpenAI的GPT服务
sentence1 = "我是一名软件工程师"
sentence2 = "小张从事法律工作"
sentence3 = "我是一名程序员"

embedding1 = embedding.embed_query(sentence1)
embedding2 = embedding.embed_query(sentence2)
embedding3 = embedding.embed_query(sentence3)


print(np.dot(embedding1,embedding2))
print(np.dot(embedding2,embedding3))
print(np.dot(embedding1,embedding3))
