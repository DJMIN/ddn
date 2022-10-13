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
