import http.client
import json
def get_data_from_store():
    conn = http.client.HTTPSConnection("pd.na.a.pvp.net")

    payload = ""


    headers = {
        'X-Riot-Entitlements-JWT': "eyJraWQiOiJrMSIsImFsZyI6IlJTMjU2In0.eyJlbnRpdGxlbWVudHMiOltdLCJhdF9oYXNoIjoiS0JMMU9peGpoenRPbTBjN2lwLTY4QSIsInN1YiI6IjI4NjI3NDA5LTAxNjAtNWUxMy1iYTdmLTBkN2I1ODQ1MzU4OCIsImlzcyI6Imh0dHBzOlwvXC9lbnRpdGxlbWVudHMuYXV0aC5yaW90Z2FtZXMuY29tIiwiaWF0IjoxNzE2MDE3Mzg2LCJqdGkiOiJYdUhsZWx5VlNPUSJ9.ktQ7RiEMxBGGXLWiBxgPgrAYKQ_FAjgTeQSk0xfjRVjKewO3UVWlfbyiwk258wg95kTxKYtV7KqtXJXWHDucIim3RrczCfG6PSe24mcN1VyYO9ESXUjR_1U_AZYqC02lrm5wEB7vHbqU2jxZBwbYT-tn2AoWXctcgQ_mKecEUZtEYcgRtkt8heQ2k4_oykc0o5UXSXs85GfW208GNwfRwN1hSv_v8mnQ3_XfvE_SBL98eKCZCfT_j2hGSuG9uSDIKLeU8ahwUQQ6Btmhy-A1ZZ1jQyGsS8hmhElFyO7nUPjcQMoYf7F1UOjLQlp8t4FELvtQhQAlD4LuyFrflEJjTA",
        'X-Riot-ClientPlatform': "ew0KCSJwbGF0Zm9ybVR5cGUiOiAiUEMiLA0KCSJwbGF0Zm9ybU9TIjogIldpbmRvd3MiLA0KCSJwbGF0Zm9ybU9TVmVyc2lvbiI6ICIxMC4wLjE5MDQyLjEuMjU2LjY0Yml0IiwNCgkicGxhdGZvcm1DaGlwc2V0IjogIlVua25vd24iDQp9",
        'X-Riot-ClientVersion': "release-08.09-shipping-57-2521387",
        'Authorization': "Bearer eyJraWQiOiJzMSIsImFsZyI6IlJTMjU2In0.eyJwcCI6eyJjIjoiYW0ifSwic3ViIjoiMjg2Mjc0MDktMDE2MC01ZTEzLWJhN2YtMGQ3YjU4NDUzNTg4Iiwic2NwIjpbImFjY291bnQiLCJvcGVuaWQiXSwiY2xtIjpbImVtYWlsX3ZlcmlmaWVkIiwib3BlbmlkIiwicHciLCJwaG9uZV9udW1iZXJfdmVyaWZpZWQiLCJsb2NhbGUiLCJhY2NvdW50X3ZlcmlmaWVkIiwiZmVkZXJhdGVkX2lkZW50aXR5X2RldGFpbHMiLCJmZWRlcmF0ZWRfaWRlbnRpdHlfcHJvdmlkZXJzIiwiYWNjdF9nbnQiLCJyZ25fTkExIiwiYWNjdCIsImFnZSIsImFmZmluaXR5Il0sImRhdCI6eyJwIjpudWxsLCJyIjoiTkExIiwiYyI6InV3MSIsInUiOjI0ODEyODU5Njc0ODgxNjAsImxpZCI6Iko0YzNoeFBhVldJaW1UbEQwUU1vWFEifSwiaXNzIjoiaHR0cHM6Ly9hdXRoLnJpb3RnYW1lcy5jb20iLCJwbHQiOnsiZGV2IjoidW5rbm93biIsImlkIjoid2luZG93cyJ9LCJleHAiOjE3MTYwMjA5ODUsImlhdCI6MTcxNjAxNzM4NSwianRpIjoiWHVIbGVseVZTT1EiLCJjaWQiOiJwbGF5LXZhbG9yYW50LXdlYi1wcm9kIn0.PK4uJ6eB4LmRVWFm7TwTr6g4UTxTaFq5SdROg8rvHxyWrtYylkfJT0JjmfP6mv9iN8kRXUOuW2yoXJvnU_nM8i1J10Ebdn1Gk2jF8dD_zyJqu-iZ7xlgIQeMdS6y4ug91F9s2DRBYC6gBT7nC2Vo3jXbzj0cpx2PocgicgIsVIs"
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
    return Single_Item_Store_Offer

def Get_Current_Items(Single_Item_Store_Offer):
    items_in_store = []
    for i in range(len(Single_Item_Store_Offer)):
        id = Single_Item_Store_Offer[i]
        items_in_store.append(id)
    return items_in_store

data = get_data_from_store()
print(Get_Current_Items(data))