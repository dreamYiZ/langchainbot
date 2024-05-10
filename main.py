from flask import Flask, request
from langchain_community.chat_models import ChatOllama
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate

app = Flask(__name__)
llm = ChatOllama(model="llama3")
prompt = ChatPromptTemplate.from_template("你只用中文回答。你能提供很高的情绪价值，根据用户对话：{topic}")
chain = prompt | llm | StrOutputParser()

# 存储每个用户的对话历史
user_histories = {}

@app.route('/chat', methods=['POST'])
def chat():
    # 获取用户的问题和用户 ID
    data = request.get_json()
    user_id = data['user_id']
    topic = data['topic']

    # 获取用户的对话历史
    history = user_histories.get(user_id, [])

    # 生成回答
    result = chain.invoke({"topic": topic, "history": history})

    # 更新用户的对话历史
    history.append(result)
    user_histories[user_id] = history

    # 返回回答
    return result
