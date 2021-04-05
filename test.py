import json5
filename = 'game_information'
new_dict = {'high_score':300}
with open(filename,'w') as  f:
    json5.dump(new_dict,f)


with open(filename) as f:
    data = json5.load(f)
print(data['high_score'])