
import http.client
import json

def Get_Data_From_Endpoint():
    conn = http.client.HTTPSConnection("valorant-api.com")

    payload = ""

    headers = { 'User-Agent': "insomnia/9.2.0" }

    conn.request("GET", "/v1/weapons/skins", payload, headers)

    res = conn.getresponse()
    data = res.read()
    data = data.decode("utf-8")
    skins_data = json.loads(data)
    return skins_data

def find_skin_name(skins_database, skin_id):
    #loop through data to find id and return name
    for skin in skins_database.get('data', []):
        skin_uuid = skin['uuid']
        skin_name = skin['displayName']
        if skin_id == skin_uuid:
            return skin_name
        
        for chroma in skin.get('chromas', []):
            skin_uuid = chroma['uuid']
            skin_name = chroma['displayName']
            if skin_id == skin_uuid:
                return skin_name
            
        for level in skin.get('levels', []):
            skin_uuid = level['uuid']
            skin_name = level['displayName']
            if skin_id == skin_uuid:
                return skin_name
    return "id not found"

