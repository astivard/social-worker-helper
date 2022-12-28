import os

from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv('TOKEN')
ROOT_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
