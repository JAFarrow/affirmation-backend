import os


class Config:
    OPENAI_API_KEY = os.environ.get('OPENAI_API_KEY') or None
    FRONTEND_URL = os.environ.get('FRONTEND_URL') or 'http://localhost:5173'
