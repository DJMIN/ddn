from ddn import DDN, LDN
import json

if __name__ == '__main__':
    data = json.loads(r"""{
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
                    "kkkey2": true
                }
            }
        }
    ]
}""")
    d = DDN(data)
    data1 = DDN(data)
    data2 = LDN(data)
    data3 = LDN([''])
    print(data1[-1])
    print(data2[-1])
    print(data3[-1])
    # print(data1['data'][1]["key3"])
    # print(data1['data'][1]["key2"]["url"])
    # print(data1['data'][1]["key3"]["kkey1"])
    if data1['data'][1]["key3"]["kkey1"]:
        print('ok')
    # print(data1['data'][1]["key3"]["kkey1"]['kkkey2'])
    print(data1['data'][1]["key265"]['151'])
    if data1['data'][1]["key265"]['151']:
        print('ok')

    # now
    if res1 := d['data'][1]["key3"]["kkey1"]['kkkey1']:  # '1234'
        print('ok', res1)
    if not (res2 := d['data'][88]["user"]["username"]['firstname']):  # ''
        print('no', res2 + '1234', repr(res2))  # no 1234 {}

    print(DDN({13: 1}) + {23: 4})  # {13: 1, 23: 4}
    print(DDN({13: 1}) + '123123', type(DDN({13: 1}) + '123123'))  # {13: 1}123123 <class 'str'>

    # vs old
    try:
        res3 = data['data'][1]["key3"]["kkey1"]['kkkey1']
    except (KeyError, IndexError):
        res3 = ''
    if res3:
        print(res3)

    try:
        res4 = data['data'][88]["user"]["username"]['firstname']
    except (KeyError, IndexError):
        res4 = ''
    if not res4:
        print('no', res4 + '1234', repr(res4))

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
    print(data_ddn_format['res'][1]['user_info']['name'] + ' lastname')  # 'dj lastname'
    print(data_ddn_format['res'][99]['user_info']['name'])  # ''

    if img_url := data_ddn_format['res'][1]['user_info']['img']:  # False
        print("https://a.com/img" + img_url)  # if None 这行代码不执行
    if img_url := data_ddn_format['res'][0]['user_info']['img']:  # True
        print("https://a.com/img" + img_url)  # https://a.com/img/1.jpg
