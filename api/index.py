from http.server import BaseHTTPRequestHandler
from urllib.parse import parse_qs
import sys
import os
import json

# Add the project root to the Python path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

def handler(event, context):
    """
    Simple handler for Vercel serverless functions.
    """
    path = event.get('path', '/')

    # Basic routing
    if path == '/':
        return {
            'statusCode': 200,
            'body': json.dumps({
                'message': 'Welcome to Agentic Mechanic API',
                'version': '0.1.0'
            }),
            'headers': {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Methods': 'GET, POST, PUT, DELETE, OPTIONS',
                'Access-Control-Allow-Headers': 'Content-Type, Authorization'
            }
        }
    elif path == '/health':
        return {
            'statusCode': 200,
            'body': json.dumps({'status': 'healthy'}),
            'headers': {
                'Content-Type': 'application/json'
            }
        }
    else:
        return {
            'statusCode': 404,
            'body': json.dumps({'detail': 'Not Found'}),
            'headers': {
                'Content-Type': 'application/json'
            }
        }
