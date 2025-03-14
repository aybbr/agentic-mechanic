from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import sys
import os
from typing import Dict, Any
import json
from mangum import Mangum

# Add the project root to the Python path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Import the app from the main module
from app.main import app
from app.core.config import settings

# Create the Mangum handler - this is what Vercel will use
handler = Mangum(app, lifespan="off")
