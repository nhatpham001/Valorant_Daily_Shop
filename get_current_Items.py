import http.client
import json


def Get_Data_From_Store(access_token):
    conn = http.client.HTTPSConnection("pd.na.a.pvp.net")

    payload = ""


    headers = {
        'X-Riot-Entitlements-JWT': "eyJraWQiOiJrMSIsImFsZyI6IlJTMjU2In0.eyJlbnRpdGxlbWVudHMiOltdLCJhdF9oYXNoIjoiOTNpTjA1OGgxUi1vbVFBZk5WYWY2ZyIsInN1YiI6IjI4NjI3NDA5LTAxNjAtNWUxMy1iYTdmLTBkN2I1ODQ1MzU4OCIsImlzcyI6Imh0dHBzOlwvXC9lbnRpdGxlbWVudHMuYXV0aC5yaW90Z2FtZXMuY29tIiwiaWF0IjoxNzE2MDIxMDIyLCJqdGkiOiJlTkZHLVdndlNKOCJ9.Kt7uoOo8L8ndgJkbLfRWN7rfuMPHpAHgGvR1HxBEC8s9xIIXr7ZQ16uS5MKpep5vtpEPga0tPb7sPJkUMn078tUeWQ2C49mmBf31aoodeJT0DR9JnJsyIdz0WZO1LbBW43wdooMOSWinay2IFW8gBrBHADG2xWyIUVQ-Gdp2MkhhtQMMBAHpf7JWXCy1WXxpvqp9JEUUBxh3CDqJCrHCeE6B6QMDtzTDx0MbkRYapzBROPCLGXvGuWXI4pPTSheuMqFmaN9PgycQUkIxcYHVDLvGZ9rNkO0EjKMqDxdweUJD-TW3kxVvRwQZFzdPLtyMPu-u9zX8BXti49EBKK1Ttg",
        'X-Riot-ClientPlatform': "ew0KCSJwbGF0Zm9ybVR5cGUiOiAiUEMiLA0KCSJwbGF0Zm9ybU9TIjogIldpbmRvd3MiLA0KCSJwbGF0Zm9ybU9TVmVyc2lvbiI6ICIxMC4wLjE5MDQyLjEuMjU2LjY0Yml0IiwNCgkicGxhdGZvcm1DaGlwc2V0IjogIlVua25vd24iDQp9",
        'X-Riot-ClientVersion': "release-08.09-shipping-57-2521387",
        'Authorization': access_token
    }
    conn.request("GET", "/store/v2/storefront/28627409-0160-5e13-ba7f-0d7b58453588?ItemTypeID=%22e7c63390-eda7-46e0-bb7a-a6abdacd2433%22", payload, headers)

    res = conn.getresponse()
    data = res.read()
    data = data.decode("utf-8")
    parsed_data = json.loads(data)

    # Access the bundle data
    featured_bundle = parsed_data.get('FeaturedBundle', {}).get('Bundle', {})
    bundle_id = featured_bundle.get('ID', 'N/A')
    items = featured_bundle.get('Items', [])


    # Access and print SingleItemOffers
    single_item_offers = parsed_data.get('SkinsPanelLayout', [])
    Single_Item_Store_Offer =  single_item_offers.get('SingleItemOffers', "not found")
    print("getting Item Store Offer Successful!")
    return Single_Item_Store_Offer

def Get_Current_Items(Single_Item_Store_Offer):
    items_in_store = []
    for i in range(len(Single_Item_Store_Offer)):
        id = Single_Item_Store_Offer[i]
        items_in_store.append(id)
    print("Getting Current Items")
    return items_in_store
