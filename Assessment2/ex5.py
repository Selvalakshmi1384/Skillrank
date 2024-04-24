import json

with open('ex5.json') as f:
    ex5 = json.load(f)
for item in ex5:
    if item['name'] == "Old Fashioned":
        item['batters']['batter'].append({"id":"1005", "type": "Tea"})
        break
with open('ex5.json','w') as f:
    json.dump(ex5,f,indent=4)