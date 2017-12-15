#! usr/bin/python 
#coding=utf-8 
import http
from repeater import Repeate


data = """GET /src-kun/api-test HTTP/1.1
Host: github.com
User-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64; rv:57.0) Gecko/20100101 Firefox/57.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2
Accept-Encoding: gzip, deflate
Cookie: 
Connection: close
Upgrade-Insecure-Requests: 1"""
request = http.analysis_request(data)
repeate = Repeate(request['url'], request['params'], request['method'], request['headers'])
response = repeate.replay()
print response.read()