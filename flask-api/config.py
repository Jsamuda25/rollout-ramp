import os
from dotenv import load_dotenv


load_dotenv()

class Config:
    IP_LOOKUP_KEY = os.getenv("IP_LOOKUP_KEY")
