# coding:utf-8

import requests
import os
os.environ['NO_PROXY'] = '127.0.0.1'
# 请求url
url = "http://127.0.0.1:8000/hello/"

# 请求头
headers = {
    "Accept": "*/*",
    "Accept-Encoding": "gzip, deflate",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
}

# 查询字符串
params = {"name": "张三","age": "18"}

r = requests.get(url=url, headers=headers, params=params)

print(r.status_code)  # 获取响应状态码
print(r.content)  # 获取响应消息

if __name__ == "__main__":
    pass