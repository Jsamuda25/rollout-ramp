from urllib.parse import urlparse
import requests
import os
import json
import os
from config import Config



def get_ip_details(ip: str) -> dict:
    
    url = 'https://api.abuseipdb.com/api/v2/check'
    
    querystring = {
    'ipAddress': ip,
    'maxAgeInDays': '90'
    }

    headers = {
        'Accept': 'application/json',   
        'Key': Config.IPDB_API_KEY
    }

    response = requests.request(method='GET', url=url, headers=headers, params=querystring)

    # Formatted output
    decodedResponse = json.loads(response.text)
    return (json.dumps(decodedResponse, sort_keys=True, indent=4))


def get_blacklisted_ips(limit: str = '100') -> dict:
    url = 'https://api.abuseipdb.com/api/v2/blacklist'
    
    querystring = {
        'limit': limit
    }

    headers = {
        'Accept': 'application/json',
        'Key': Config.IPDB_API_KEY
    }

    response = requests.request(method='GET', url=url, headers=headers, params=querystring)

    # Formatted output
    decodedResponse = json.loads(response.text)
    return (json.dumps(decodedResponse, sort_keys=True, indent=4))


    


        

