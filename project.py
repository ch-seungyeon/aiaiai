import json

with open('student_info.json', 'rt', encoding='UTF8') as json_file:
    json_data = json.load(json_file)
print(json_data["Students"]['name'])