from get_current_Items import Get_Data_From_Store, Get_Current_Items
from get_all_skins import Get_Data_From_Endpoint, find_skin_name

Data_From_Store = Get_Data_From_Store()
Current_Items_ID = Get_Current_Items(Data_From_Store)
database = Get_Data_From_Endpoint()
skin_id = "b0c661cd-47e6-9857-8831-ef92b880a7b3"

Current_Items_Name = []

for i, key in enumerate(Current_Items_ID):
    skin_name = find_skin_name(database, key)
    Current_Items_Name.append(skin_name)

print(Current_Items_Name)