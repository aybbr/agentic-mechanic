from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import sys
import os
from typing import Dict, Any
import json

# Add the project root to the Python path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Import the app from the main module
from app.main import app
from app.core.config import settings

def create_error_response(status_code: int, message: str) -> Dict[str, Any]:
    return {
        "statusCode": status_code,
        "body": json.dumps({"detail": message}),
        "headers": {
            "Content-Type": "application/json",
            "Access-Control-Allow-Origin": settings.CORS_ORIGINS,
            "Access-Control-Allow-Credentials": "true",
        },
    }

def handler(event: Dict[str, Any]) -> Dict[str, Any]:
    """Vercel serverless function handler with security measures."""
    try:
        # Validate request
        if not isinstance(event, dict):
            return create_error_response(400, "Invalid request format")

        method = event.get("method", "").upper()

        # Handle CORS preflight
        if method == "OPTIONS":
            return {
                "statusCode": 200,
                "headers": {
                    "Access-Control-Allow-Origin": settings.CORS_ORIGINS,
                    "Access-Control-Allow-Methods": "GET, POST, PUT, DELETE, OPTIONS",
                    "Access-Control-Allow-Headers": "Content-Type, Authorization",
                    "Access-Control-Allow-Credentials": "true",
                    "Access-Control-Max-Age": "86400",  # 24 hours
                },
            }

        # Basic request validation
        if not method:
            return create_error_response(400, "Missing HTTP method")

        # Handle the actual request through FastAPI
        response = app(event)

        # Ensure proper response format
        return {
            "statusCode": response.status_code,
            "body": response.body.decode(),
            "headers": {
                **response.headers,
                "Access-Control-Allow-Origin": settings.CORS_ORIGINS,
                "Access-Control-Allow-Credentials": "true",
                "X-Content-Type-Options": "nosniff",
                "X-Frame-Options": "DENY",
                "X-XSS-Protection": "1; mode=block",
                "Strict-Transport-Security": "max-age=31536000; includeSubDomains",
            },
        }

    except Exception as e:
        # Log the error (you should set up proper logging)
        print(f"Error processing request: {str(e)}")
        return create_error_response(500, "Internal server error")
