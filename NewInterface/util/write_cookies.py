import requests

import json

from util.operation_json import OperationJson


class WriteCookies:
    def __init__(self, response):
        self.response = response

    # 获取cookies
    def get_cookie(self):
        af = json.loads(self.response)['data']['accessToken']
        print(af)
        return af

    # 写cookies到指定文件
    def write_cookie(self):
        op = OperationJson()
        ab = self.get_cookie()
        dc = {
            "accessToken": ab
        }
        op.write_data(dc)


if __name__ == '__main__':
    url = 'http://capijcy.jcease.com/jcy-api/app/system/passwordLogin'
    data = {
        "channelMark": "00_OPPO",
        "mobi": "18520350227",
        "password": "03761decb8c83294b570fbc917b88729",
        "pre": "+86",
        "OSType": "A"
    }
    res = requests.post(url=url, json=data)
    wr = WriteCookies(res)
    print(wr.write_cookie())
