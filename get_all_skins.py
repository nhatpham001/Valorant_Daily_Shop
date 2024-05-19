
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
    #return a list of skinname and display icon
    result = {}
    #loop through data to find id and return name
    for skin in skins_database.get('data', []):
        skin_uuid = skin['uuid']
        skin_name = skin['displayName']
        icon_link = skin['displayIcon']
        if skin_id == skin_uuid:
            result[skin_name] = icon_link
            return result
        
        for chroma in skin.get('chromas', []):
            skin_uuid = chroma['uuid']
            skin_name = chroma['displayName']
            icon_link = skin['displayIcon']
            if skin_id == skin_uuid:
                result[skin_name] = icon_link
                return result
        
        for level in skin.get('levels', []):
            skin_uuid = level['uuid']
            skin_name = level['displayName']
            icon_link = skin['displayIcon']
            if skin_id == skin_uuid:
                result[skin_name] = icon_link
                return result
        
    return "id not found"

# data = Get_Data_From_Endpoint()
# skin_id = "85c76090-4de5-3a3a-a763-f4a7b779e8ed"
# x = find_skin_name(data, skin_id)
# print(x)