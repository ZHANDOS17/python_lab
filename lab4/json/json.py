import json
file = open('tasks.json')
data = json.load(file)
print("Interface Status")
print(80*'=')
lines='-------------------------------------------------- --------------------  ------  ------'
print("DN","Description",sep=49*' ',end=11*' ')
print("Speed","MTU",sep=4*' ')
print(lines)
for i in data["imdata"]:
    dn=i["l1PhysIf"]["attributes"]["dn"]
    zhyl=i["l1PhysIf"]["attributes"]["fecMode"]
    otvet=i["l1PhysIf"]["attributes"]["mtu"]
    print(dn,zhyl,sep='\t                         ',end=" ")
    print(otvet)