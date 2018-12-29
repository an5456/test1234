import requests
import json


class RunMethod:
    def post_main(self, url, data, cookies=None, data_type=None):
        res = None
        if data_type == 'json':
            if cookies is None:
                res = requests.post(url=url, json=data, verify=False)
            else:
                res = requests.post(url=url, json=data, cookies=cookies, verify=False)
            return res.json()
        else:
            if cookies is not None:
                res = requests.post(url=url, json=data, cookies=cookies, verify=False)
            else:
                res = requests.post(url=url, json=data, verify=False)
            return res.json()

    def get_main(self, url, data=None, cookies=None):
        res = None
        if cookies is not None:
            res = requests.get(url=url, data=data, cookies=cookies, verify=False)
        else:
            res = requests.get(url=url, data=data, verify=False)
        return res.json()

    def run_main(self, method, url, data=None, cookies=None, data_type=None):
        res = None
        if method == 'post':
            res = self.post_main(url=url, data=data, cookies=cookies, data_type=data_type)
        else:
            res = self.get_main(url=url, data=data, cookies=cookies)
        # return json.dumps(res, ensure_ascii=False, sort_keys=True, indent=2)
        return json.dumps(res, ensure_ascii=False)


if __name__ == '__main__':
    ru = RunMethod()
    url = 'http://192.168.2.153/yyjapi/api/purchorder/getpurchorder'
    data = {"ticketno": "PO20181114000481",
            "flag": 0
            }
    cookies = {
        "SESSION": "783c9616-6f70-4aef-b734-587921c7f59f"
    }
    res = ru.run_main(method='post', url=url, data=data, cookies=cookies, data_type='json')
    print(res)
