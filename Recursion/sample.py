# dict1 = {"Age":11}
# dict2 = dict1
# dict2["Age"] = 20
# print(dict1,dict2)    



head = {
    "value":"Nashir",
        "next":{
            "value":'Ajmal',
              "next":{
                  "value":'Rayees',
                  "next":None
            }
        }
    }

print(head['next']['next']['next'])