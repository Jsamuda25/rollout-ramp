from urllib.parse import urlparse
import requests

def validate_url(url: str) -> dict:
    result = {
        "is_valid": False,
        "error": None,
        "https_supported": False,
        "status_code": None

    }

    # Check if the URL is well-formed 
    try: 
        parsed_url = urlparse(url)
        if not parsed_url.scheme or not parsed_url.netloc:
            result["error"] = "Invalid URL format"
            return result
        
    except Exception as e:
        result["error"] = str(e)
        return result

    # Check if the URL is reachable
    try: 
        print(f"Making GET request to: {url}")
        response = requests.get(url, timeout=20)
        result["is_valid"] = response.ok
        result["status_code"] = response.status_code

    except requests.RequestException as e:
        result["error"] = str(e)
        return result   
    

    # Check if HTTPS is supported
    if parsed_url.scheme == "https":
        result["https_supported"] = True
    else:
        https_url = f"https://{parsed_url.netloc}{parsed_url.path}"
        try:
            https_response = requests.get(https_url, timeout=5)
            result["https_supported"] = https_response.ok
        except requests.RequestException:
            result["https_supported"] = False
    
    return result

    
    


    


    



