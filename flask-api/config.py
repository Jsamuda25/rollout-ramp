# Read configuration from environment variables
import os
from dotenv import load_dotenv

# Load environment variables from a .env file
load_dotenv()

# Configuration class to hold application settings
class Config:
    IPDB_API_KEY = os.getenv("ABUSEIPDB_API_KEY")
