import requests
import json
import os

def main():
    #heyhack_api_key = os.environ['23UdMkr/F+6FirDbAHFjsPhenpMg3Y2EviuEKxCLjrE=']
    #target_url = os.environ['https://arcadia.f5latam.app/']
    #heyhack_url = "https://app.heyhack.com/img/scanning.json"
    heyhack_url = "https://app.heyhack.com/api/scanjobs"
    profile_id = "3b2f8285-6cb8-40d4-a286-b4d07870f36e"
    application_id = "9c098294-da9f-4529-b424-9a8a88efc7b5"
    
    # Configura el payload para iniciar el escaneo
    params = {
        #"target": target_url,  # URL objetivo del escaneo
        #"scan_type": "full"
        
        "profile_id": profile_id,
        "application_id": application_id
    }
    
    headers = {
        #"Authorization": f"Bearer {heyhack_api_key}",
        "accept": "*/*",
        "Authorization": 'Heyhack 23UdMkr/F+6FirDbAHFjsPhenpMg3Y2EviuEKxCLjrE='
        #"Content-Type": "application/json"
        
    }
    
    #response = requests.post(heyhack_url, headers=headers, data=json.dumps(payload))
    response = requests.post(heyhack_url, headers=headers, params=params, data="")
    
    if response.status_code == 200:
        print("Scan initiated successfully")
        print(response.json())
    else:
        print(f"Error initiating scan: {response.status_code}")
        print(response.text)

if __name__ == "__main__":
    main()
