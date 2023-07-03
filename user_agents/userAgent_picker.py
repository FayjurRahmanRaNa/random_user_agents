# outer dependencies
import random

# local dependencies
from au_json_reader import userAgent_jsonReader


# user agent fiels list name
USER_AGENT_FILES = ['mobile', 'desktop']

# all user agent place holder
header_list = []

## ------------------------------##


def userAgent_Combiner(list):
    dump_list = []
    for file in USER_AGENT_FILES:
        user_agent_list = userAgent_jsonReader(file)
        dump_list.extend(user_agent_list)

    for ua in dump_list:
        list.append(ua)
    return f'Found Total: {len(list)} USER AGENTS'


userAgent_Combiner(header_list)


# will select a single header from the list of all_user_agents in au_json_reader file
def random_headerSelector():
    random_user_agent = random.choice(header_list)
    random_header = random_user_agent['ua']
    return random_header
