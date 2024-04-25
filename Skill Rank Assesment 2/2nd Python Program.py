import json
with open('C:\Users\91770\OneDrive\Desktop\Skill Rank Assesment 2\EX 5.json', 'r') as f:
    ex5 = json.load(f)

for i in ex5:
    if i['type'] == 'donut':
        if i['name'] == 'Old Fashioned':
            i['batters']['batter'].append({'id':'1003','type': 'Tea'})
            break  
with open('C:\Users\91770\OneDrive\Desktop\Skill Rank Assesment 2\EX 5.json', 'w') as f:
    json.dump(ex5, f, indent=4)
