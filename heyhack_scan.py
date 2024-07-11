import requests
import json
import os

def main():
    heyhack_api_key = os.environ['HEYHACK_API_KEY']
    target_url = os.environ['TARGET_URL']
    heyhack_url = "https://app.heyhack.com/img/scanning.json"
    
    # Configura el payload para iniciar el escaneo
    payload = {
        "target": target_url,  # URL objetivo del escaneo
        "scan_type": "full"
    }
    
    headers = {
        "Authorization": f"Bearer {heyhack_api_key}",
        "Content-Type": "application/json"
    }
    
    response = requests.post(heyhack_url, headers=headers, data=json.dumps(payload))
    
    if response.status_code == 200:
        print("Scan initiated successfully")
        print(response.json())
    else:
        print(f"Error initiating scan: {response.status_code}")
        print(response.text)

if __name__ == "__main__":
    main()
