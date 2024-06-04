from get_current_Items import Get_Data_From_Store, Get_Current_Items
from get_all_skins import Get_Data_From_Endpoint, find_skin_name
from get_entitlement_token import get_lockfile_port, get_entitlement_token
import streamlit as st

# access_token = "Bearer eyJraWQiOiJzMSIsImFsZyI6IlJTMjU2In0.eyJwcCI6eyJjIjoiYW0ifSwic3ViIjoiMjg2Mjc0MDktMDE2MC01ZTEzLWJhN2YtMGQ3YjU4NDUzNTg4Iiwic2NwIjpbIm9wZW5pZCIsImxpbmsiLCJiYW4iLCJsb2xfcmVnaW9uIiwibG9sIiwic3VtbW9uZXIiLCJvZmZsaW5lX2FjY2VzcyJdLCJjbG0iOlsibG9sX2FjY291bnQiLCJlbWFpbF92ZXJpZmllZCIsIm9wZW5pZCIsInB3IiwibG9sIiwib3JpZ2luYWxfcGxhdGZvcm1faWQiLCJwaG9uZV9udW1iZXJfdmVyaWZpZWQiLCJwaG90byIsIm9yaWdpbmFsX2FjY291bnRfaWQiLCJwcmVmZXJyZWRfdXNlcm5hbWUiLCJsb2NhbGUiLCJiYW4iLCJsb2xfcmVnaW9uIiwiYWNjdF9nbnQiLCJyZWdpb24iLCJwdnBuZXRfYWNjb3VudF9pZCIsInJnbl9OQTEiLCJhY2N0IiwidXNlcm5hbWUiXSwiZGF0Ijp7InAiOm51bGwsInIiOiJOQTEiLCJjIjoidXcxIiwidSI6MjQ4MTI4NTk2NzQ4ODE2MCwibGlkIjoiSjRjM2h4UGFWV0lpbVRsRDBRTW9YUSJ9LCJpc3MiOiJodHRwczovL2F1dGgucmlvdGdhbWVzLmNvbSIsInBsdCI6eyJkZXYiOiJ1bmtub3duIiwiaWQiOiJ3aW5kb3dzIn0sImV4cCI6MTcxNjA5MzUxNCwiaWF0IjoxNzE2MDg5OTE0LCJqdGkiOiJNZW4ydGpWcW1uNCIsImNpZCI6InJpb3QtY2xpZW50In0.YOJH04BGTN5LPho-TtW5-sw8OIqBPmAskzkJBcRQsbePwZc3y5JdUAroupF3Iq7_IxqAthgYwpurcJXuk7V6NunAQhnUA0ra0O9k0bMqWlBubPRAPwu7JqPLFt6cC_79hJh76_dXqtecswCAQrwk05n0liGE8edGzfY4P3T7ZAI"
#get entitlement token
# port =  get_lockfile_port()
# access_token = get_entitlement_token(port)
access_token = "Bearer eyJraWQiOiJzMSIsImFsZyI6IlJTMjU2In0.eyJwcCI6eyJjIjoiYW0ifSwic3ViIjoiMjg2Mjc0MDktMDE2MC01ZTEzLWJhN2YtMGQ3YjU4NDUzNTg4Iiwic2NwIjpbImFjY291bnQiLCJvcGVuaWQiXSwiY2xtIjpbImVtYWlsX3ZlcmlmaWVkIiwib3BlbmlkIiwicHciLCJwaG9uZV9udW1iZXJfdmVyaWZpZWQiLCJsb2NhbGUiLCJhY2NvdW50X3ZlcmlmaWVkIiwiZmVkZXJhdGVkX2lkZW50aXR5X2RldGFpbHMiLCJmZWRlcmF0ZWRfaWRlbnRpdHlfcHJvdmlkZXJzIiwiYWNjdF9nbnQiLCJyZ25fTkExIiwiYWNjdCIsImFnZSIsImFmZmluaXR5Il0sImRhdCI6eyJwIjpudWxsLCJyIjoiTkExIiwiYyI6InV3MSIsInUiOjI0ODEyODU5Njc0ODgxNjAsImxpZCI6Ijd2YTJMWWVXc2dIdVBjRnZ2TFJyencifSwiaXNzIjoiaHR0cHM6Ly9hdXRoLnJpb3RnYW1lcy5jb20iLCJwbHQiOnsiZGV2IjoidW5rbm93biIsImlkIjoid2luZG93cyJ9LCJleHAiOjE3MTc0NjI5MjUsImlhdCI6MTcxNzQ1OTMyNSwianRpIjoiWmNRTGpuZlV6NkkiLCJjaWQiOiJwbGF5LXZhbG9yYW50LXdlYi1wcm9kIn0.h9ukewk6-G8SZxN3VrWq74vINAVh-2POB-TwbyjHnOlt0oSx_fZndnfbyVOezC39enkaVt6ZfW7dmHcqcpl13dXX0d6l-KCa8rl7_zom11RtCxWDPnuxUMl4d4YjCFuc4L2xU0uR4vc-GNn15qTgN17tRuKq7bLZiUX3W0lL5gY"
Data_From_Store = Get_Data_From_Store(access_token)
Current_Items_ID = Get_Current_Items(Data_From_Store)
database = Get_Data_From_Endpoint()

#create a hashmap to store items
Current_Items_Name = {}
#loop through items' ids and find items' name and return
for i, key in enumerate(Current_Items_ID):
    skin_found = find_skin_name(database, key)
    Current_Items_Name.update(skin_found)



#--------------------------------------------------------------------- webpage ---------------------------------
def run_webpage(Current_Items):
    st.header('Valorant Daily Shop', divider='rainbow')
    st.title('Items From Today:')
    idx = 1
    for skin_name, icon_link in Current_Items.items():
        st.subheader(f':orange[{idx}]. :orange[{skin_name}]')

        # Display the image
        st.image(icon_link, caption="Valorant Skin Icon", use_column_width=True)
        
        #advance idx for item's place
        idx += 1
    st.header("WishList", divider= 'rainbow')
    wished_skin = st.text_input("Enter name here")

    if wished_skin in Current_Items:
        st.header(":rainbow[Your Skin Is In Shop Today!]", )


run_webpage(Current_Items_Name)