from get_current_Items import Get_Data_From_Store, Get_Current_Items
from get_all_skins import Get_Data_From_Endpoint, find_skin_name
import streamlit as st

access_token = "Bearer eyJraWQiOiJzMSIsImFsZyI6IlJTMjU2In0.eyJwcCI6eyJjIjoiYW0ifSwic3ViIjoiMjg2Mjc0MDktMDE2MC01ZTEzLWJhN2YtMGQ3YjU4NDUzNTg4Iiwic2NwIjpbIm9wZW5pZCIsImxpbmsiLCJiYW4iLCJsb2xfcmVnaW9uIiwibG9sIiwic3VtbW9uZXIiLCJvZmZsaW5lX2FjY2VzcyJdLCJjbG0iOlsibG9sX2FjY291bnQiLCJlbWFpbF92ZXJpZmllZCIsIm9wZW5pZCIsInB3IiwibG9sIiwib3JpZ2luYWxfcGxhdGZvcm1faWQiLCJwaG9uZV9udW1iZXJfdmVyaWZpZWQiLCJwaG90byIsIm9yaWdpbmFsX2FjY291bnRfaWQiLCJwcmVmZXJyZWRfdXNlcm5hbWUiLCJsb2NhbGUiLCJiYW4iLCJsb2xfcmVnaW9uIiwiYWNjdF9nbnQiLCJyZWdpb24iLCJwdnBuZXRfYWNjb3VudF9pZCIsInJnbl9OQTEiLCJhY2N0IiwidXNlcm5hbWUiXSwiZGF0Ijp7InAiOm51bGwsInIiOiJOQTEiLCJjIjoidXcxIiwidSI6MjQ4MTI4NTk2NzQ4ODE2MCwibGlkIjoiSjRjM2h4UGFWV0lpbVRsRDBRTW9YUSJ9LCJpc3MiOiJodHRwczovL2F1dGgucmlvdGdhbWVzLmNvbSIsInBsdCI6eyJkZXYiOiJ1bmtub3duIiwiaWQiOiJ3aW5kb3dzIn0sImV4cCI6MTcxNjA4OTg4NiwiaWF0IjoxNzE2MDg2Mjg2LCJqdGkiOiJZUlo3V19ERGVyRSIsImNpZCI6InJpb3QtY2xpZW50In0.VUYrI9RJ0DRqL9Qwx5fOlYkOpjdMEXff4YxQKIo6q9SwXMA7G0a4-Sw3U9oXdVnuNaI3a2vJ9njKGlFAaHE3dFJNdLCMdervjFTadVbGlwF-XsIaO8a5Mq9wMfbzimPwbJ-5i_vvvUpoGA8s1xatq06h0OmYzfwQ2-SORyi1Z1I"

Data_From_Store = Get_Data_From_Store(access_token)
Current_Items_ID = Get_Current_Items(Data_From_Store)
database = Get_Data_From_Endpoint()

#create a list to store store items
Current_Items_Name = []
#loop through items' ids and find items' name and return
for i, key in enumerate(Current_Items_ID):
    skin_name = find_skin_name(database, key)
    Current_Items_Name.append(skin_name)



#--------------------------------------------------------------------- webpage ---------------------------------
def run_webpage(Current_Items):
    st.header('Valorant Daily Shop', divider='rainbow')
    st.title('Items From Today:')
    for idx in range(len(Current_Items)):
        item = Current_Items[idx]
        st.subheader(f':orange[{idx}]. :orange[{item}]')

run_webpage(Current_Items_Name)