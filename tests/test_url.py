import httpx

try:
    response = httpx.get('https://rgsearchaisr.search.windows.net')
    print(response.status_code)
except httpx.ConnectError as e:
    print(f"Connection error: {e}")
