DictDefaultNone

Get data from nested lists and dictionaries use Simple syntax, if can‘t return None, no raise IndexError or KeyError
用简单的python语法快速获取嵌套列表或者字典里的数据，如果没取到则返回空，而不是抛出IndexError或者KeyError

eg.: dict1["k1"]["k2"][0]["k"]

```python
from ddn import DDN

data = {
    "data": [
        {
            "key1": "123",
            "key2": {
                "kkey1": {
                    "kkkey1": "1234",
                    "kkkey2": 12345
                }
            }
        },
        {
            "key1": "'1234'",
            "key3": {
                "kkey1": {
                    "kkkey1": "1234",
                    "kkkey2": True
                }
            }
        }
    ]
}

d = DDN(data)

if d['data'][1]["key3"]["kkey1"]['kkkey1']:
    print('ok')
if d['data'][88]["user"]["username"]['firstname']:
    print('no')

```