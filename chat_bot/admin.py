from django.contrib import admin, messages
from langchain_community.document_loaders.pdf import PyPDFLoader
from langchain_community.vectorstores.faiss import FAISS
from langchain_openai import OpenAIEmbeddings
from langchain_text_splitters import CharacterTextSplitter

from chat_bot.models import ChatBot
# from chat_bot.serializer import ChatBotSerializer
# from chat_bot.tests import OPENAI_API_KEY
#
#
# # Register your models here.
#
# @admin.action(description="DOC TO VECTOR")
# def doc_to_vector(self, request, queryset):
#     loader = PyPDFLoader("/home/abhishek/Projects/sellerhub_backend/media/documents/abhiii22.pdf")
#     documents = loader.load()
#     text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
#     docs = text_splitter.split_documents(documents)
#     embeddings = OpenAIEmbeddings(openai_api_key=OPENAI_API_KEY)
#     db = FAISS.from_documents(docs, embeddings)
#     print(db.index.ntotal)
#     # update vector_db field is tTrue
#     queryset.update(vector_db=True)
#     messages.success(request, "Data save to sheet successfully")
#     return docs
#

@admin.register(ChatBot)
class ChatBotAdmin(admin.ModelAdmin):
    list_display = [
        "user", "vector_db", "documents", "user_chat", "response_chat",
        "created_at", "updated_at"
    ]
    # actions = ["doc_to_vector"]