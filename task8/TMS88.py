import csv
import json
user_data = []
while len(user_data) < 4:
    names_user = input("Your name:")
    age_user = input("Your age:")
    data_storeg = { 
        "Your name":names_user,
        "Your age":age_user
    }
    user_data.append(data_storeg)
print(user_data)

with open("user.json","w") as user_file:
    json.dump(user_data,user_file)
with open("user.csv","w") as csvfile:
    parametres = ["Your name","Your age"]
    writer = csv.DictWriter(csvfile, fieldnames=parametres )
    writer.writeheader()
    writer.writerows(user_data)
