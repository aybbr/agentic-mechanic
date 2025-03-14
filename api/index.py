from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import sys
import os

# Add the project root to the Python path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Import the app from the main module
from app.main import app

# This is needed for Vercel serverless functions
from mangum import Mangum

# Create handler for AWS Lambda / Vercel
handler = Mangum(app)
