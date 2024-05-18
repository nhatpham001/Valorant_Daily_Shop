
import http.client
import json

conn = http.client.HTTPSConnection("valorant-api.com")

payload = ""

headers = { 'User-Agent': "insomnia/9.2.0" }

conn.request("GET", "/v1/weapons/skins", payload, headers)

res = conn.getresponse()
data = res.read()
data = data.decode("utf-8")
skins_data = json.loads(data)
db = skins_data
def get_data(skins_data):
    data = skins_data
    return data
def find_skin_name(skins_data, skin_id):
    #check if id is in database
    if skin_id not in data:
        return "id not in data"
    #loop through data to find id and return name
    for skin in skins_data.get('data', []):
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
database = get_data(skins_data)
skin_id = "b0c661cd-47e6-9857-8831-ef92b880a7b3"
print(find_skin_name(database, skin_id))