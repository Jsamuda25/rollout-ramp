import os
from dotenv import load_dotenv


load_dotenv()

class Config:
    IPDB_API_KEY = os.getenv("ABUSEIPDB_KEY")
