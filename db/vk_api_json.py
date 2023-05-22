import json
from random import randint
from datetime import datetime

# https://oauth.vk.com/blank.html#access_token=vk1.a.ApFlMtkFZVsGn4cMEmpZkY5GkKL8wT-dticoGYd2yb9_PY5GkYftzp-vx3-XCSzzKUgpDRxQRFz2PmEwp__Rdcq4Et70kTcMoIXer_RvUnjwEqcrkPPLDqvvXKREeOEPA2fZ17Nz9XUoD4dL6i-ZcqTYYII4BZzZcPObJ389qxP3R2sX_am_eQh9C8WdSRG9nN3_FTfg_5pGWzuv3aFgjQ&expires_in=86400&user_id=223917500\
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
