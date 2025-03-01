import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class Config:
    INPUT_FILE_PATH = os.getenv("INPUT_FILE_PATH")  # Path to the input file
    OUTPUT_FILE_PATH = os.getenv("OUTPUT_FILE_PATH")  # Path to the output file