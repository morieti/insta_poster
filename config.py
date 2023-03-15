import os

from dotenv import load_dotenv

load_dotenv()


class Config:
    username = os.getenv('INSTA_USERNAME', '')
    password = os.getenv('INSTA_PASSWORD', '')
