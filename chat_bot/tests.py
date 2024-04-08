# from django.test import TestCase
# from langchain.chains.retrieval_qa.base import RetrievalQA
# from langchain_openai import ChatOpenAI, OpenAIEmbeddings
#
# OPENAI_API_KEY = "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"
#
# embeddings = OpenAIEmbeddings(openai_api_key=OPENAI_API_KEY)
#
#
# def query_data(query):
#     llm = ChatOpenAI(
#         openai_api_key=OPENAI_API_KEY,
#         temperature=0,
#         max_tokens=30
#     )
#     retriever = vector_stores.as_retriever()
#     qa = RetrievalQA.from_chain_type(
#         llm=llm,
#         chain_type="stuff",
#         retriever=retriever,
#     )
#     retriever_output = qa.invoke(query)
#     return retriever_output
#
