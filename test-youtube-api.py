#!/usr/bin/env python3
"""
Test YouTube API access with proxy
"""

import os
import sys
import requests

print("=== Testing YouTube API Access ===")
print()

# Print proxy settings
print("Proxy settings:")
print(f"HTTP_PROXY: {os.environ.get('HTTP_PROXY')}")
print(f"HTTPS_PROXY: {os.environ.get('HTTPS_PROXY')}")
print(f"http_proxy: {os.environ.get('http_proxy')}")
print(f"https_proxy: {os.environ.get('https_proxy')}")
print()

# Test 1: Direct YouTube access
print("Test 1: Direct YouTube access")
try:
    response = requests.get('https://www.youtube.com', timeout=10)
    print(f"Status: {response.status_code}")
    print(f"URL: {response.url}")
except Exception as e:
    print(f"Error: {e}")
print()

# Test 2: YouTube API endpoint
print("Test 2: YouTube API endpoint")
try:
    # Test YouTube Data API (no API key needed for this endpoint)
    response = requests.get('https://www.googleapis.com/youtube/v3/videos?part=snippet&id=vCoGfisdS8Y', timeout=10)
    print(f"Status: {response.status_code}")
    print(f"URL: {response.url}")
    # Print response content (first 500 chars)
    content = response.text
    print(f"Response (first 500 chars): {content[:500]}...")
except Exception as e:
    print(f"Error: {e}")
print()

# Test 3: Test if proxy is actually being used
print("Test 3: Testing proxy connectivity")
try:
    # Test with a service that shows your IP
    response = requests.get('https://httpbin.org/ip', timeout=10)
    print(f"Status: {response.status_code}")
    print(f"Response: {response.json()}")
except Exception as e:
    print(f"Error: {e}")
print()

print("=== Test Complete ===")