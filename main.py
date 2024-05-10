from langchain_community.chat_models import ChatOllama
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate

llm = ChatOllama(model="llama3")
prompt = ChatPromptTemplate.from_template("你只用中文回答。你能提供很高的情绪价值，根据用户对话：{topic}")
chain = prompt | llm | StrOutputParser()

# 初始化对话历史
history = []

# 第一次对话
result = chain.invoke({"topic": "肚子痛怎么办"})
print(result)
history.append(result)

# 第二次对话
result = chain.invoke({"topic": "饿了", "history": history})
print(result)
history.append(result)

# 以此类推...
