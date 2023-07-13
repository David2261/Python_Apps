import json
from random import randint
from datetime import datetime


str_json = """
{
    "response": {
        "count": 11,
        "friends_count": 0,
        "items": [
            {
                "id": 481459141,
                "first_name": "Юлии",
                "last_name": "Нековской",
                "can_access_closed": true
            },
            {
                "id": 429360893,
                "first_name": "Артема",
                "last_name": "Ананьева",
                "can_access_closed": true
            }
        ]
    }
}
"""

data = json.loads(str_json)

# print(type(data['response']['items']))

for item in data['response']['items']:
    del item['id']
    item['likes'] = randint(100, 200)
    item['a'] = None
    item['now'] = datetime.now().strftime('%d.%m.%y')


with open('vk.json', 'w') as file:
    json.dump(data, file, indent=2)


# For read file
with open ('vk.json', 'r') as file:
    data = json.load(file)
    print(data)
