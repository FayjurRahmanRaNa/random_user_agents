# outer dependencies
import json


# reading all the JSON files from the us_json_files folder
# return a list of all the user agents
def userAgent_jsonReader(file_name):
    with open(f'./ua_json_files/ua_{file_name}.json', mode='r', encoding='utf-8') as json_file:
        user_agents_str = json_file.read()
    user_agents_lst = json.loads(user_agents_str)
    print(f'Found Total : {len(user_agents_lst)} agents from {file_name}')
    return user_agents_lst
