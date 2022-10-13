DictDefaultNone

Get data from nested lists and dictionaries use Simple syntax, if can‘t return None, no raise IndexError or KeyError
用简单的python语法快速获取嵌套列表或者字典里的数据，如果没取到则返回空，而不是抛出IndexError或者KeyError

eg.: dict1["k1"]["k2"][0]["k"]

```python
from ddn import DDN


data = {
    "res": [
        {
            'user_info': {
                "uid": 123,
                "name": 'sam',
                'img': '/1.jpg'
            }
        },
        {
            'user_info': {
                "uid": 1,
                "name": 'dj'
            }
        },
    ]
}

data_ddn_format = DDN(data)

# 例子1：字典取不到key 或者 列表长度不够，则返回空
print(data_ddn_format['res'][1]['user_info']['name'] + ' lastname')  # 'dj lastname'
print(data_ddn_format['res'][99]['user_info']['name'])  # ''

# 例子2：取不到key(用户头像链接)，则跳过后续处理
if img_url := data_ddn_format['res'][0]['user_info']['img']:  # True
    print("https://a.com/img" + img_url)  # https://a.com/img/1.jpg
if img_url := data_ddn_format['res'][1]['user_info']['img']:  # False
        print("https://a.com/img" + img_url)  # if None 这行代码不执行

# 例子3：字典可以相加，或者与字符串相加表现和javascript一致
print(DDN({13: 1}) + {23: 4})  # {13: 1, 23: 4}
tmp = DDN({13: 1}) + '123123'
print(tmp, type(tmp))  # {13: 1}123123 <class 'str'>


```