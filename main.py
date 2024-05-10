from langchain_community.chat_models import ChatOllama
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate

llm = ChatOllama(model="llama3")

prompt = ChatPromptTemplate.from_template("根据关键字： {topic}，生成一篇文章，使用中文回复。")
chain = prompt | llm | StrOutputParser()

print(chain.invoke({"topic": "湖南旅游景点"}))
