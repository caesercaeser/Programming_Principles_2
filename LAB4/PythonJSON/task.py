import json
print("Interface Status")
print("================================================================================")
print("DN                                                 Description           Speed    MTU  ")
print("-------------------------------------------------- --------------------  ------  ------")

with open("LAB4/PythonJSON/sample-data.json", "r") as file:
    data = json.load(file)
    for item in data['imdata']:
        print(f"{item['l1PhysIf']['attributes']['dn']}                              {item['l1PhysIf']['attributes']['speed']}   {item['l1PhysIf']['attributes']['mtu']}")