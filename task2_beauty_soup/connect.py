import os
from dotenv import load_dotenv
from pymongo import MongoClient
from pymongo.server_api import ServerApi

load_dotenv()


client = MongoClient(os.getenv("CONNECT"), server_api=ServerApi("1"))

db = client.book
