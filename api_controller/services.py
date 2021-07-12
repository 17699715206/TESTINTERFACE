# coding:utf-8

import requests
import json

class api():
    def api_func(self, req_json):
        # req_json = json.loads(r_json)
        # 请求url
        # url = "http://www.baidu.com/s"
        # print(req_json)
        url = req_json["url"]
        # 请求头
        # headers = {
        #     "Accept": "*/*",
        #     "Accept-Encoding": "gzip, deflate",
        #     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        # }
        headers = req_json["headers"]

        # 查询字符串
        # params = {'ie': 'utf-8', 'wd': '测试'}
        params = req_json["params"]

        # 文件
        # files = {'upload_img': ('report.xlsx', open('report.xlsx', 'rb'), 'image/png')}

        # 判断如果是get就用get请求
        if req_json['request_method'] == 'get':
            print(url,headers,params)
            r = requests.get(url=url, headers=headers, params=params)
            data = {
                "code": r.status_code,
                "total_seconds": r.elapsed.total_seconds(),
                "content":r.content
            }
            print(data)
            return r
        elif req_json['request_method'] == 'post':  # 如果是post在判断files是否为空
            if req_json['files'] == '':
                r = requests.post(url=url, headers=headers, data=params)
            else:
                pass
                # r = requests.post(url=url, data=params, headers=headers, files=files)
        else:
            pass




        # print(r.status_code)  # 获取响应状态码
        # print(r.content)# 获取响应消息
        # print()  # 获取响应时间
        # return data


if __name__ == "__main__":
    req_json = {"url": "http://www.baidu.com/s","headers": {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"},"params": {"ie": "utf-8","wd": "测试"}}
    print(type(req_json))
    api().api_func(req_json)