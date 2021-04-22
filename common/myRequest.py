# -*- coding: utf-8 -*-
import requests
from common.myLogger import logger


def request_post(url, data):
    header_dict = {
        'Content-Type': 'application/json'
    }
    try:
        r = requests.post(url=url,  headers=header_dict, json=data)  # 发送请求
        data_str = r.text
        # logger.debug("###" + data_str)
        logger.info("请求url:{};请求头:{};请求数据:{};服务器响应:{}".format(url, header_dict, data, data_str))
    except Exception as e:
        data_str = -1
        logger.error("请求url:{};请求头:{};请求数据:{};系统异常信息:{}".format(url, header_dict, data, e))
    return data_str


def request_get(url):
    # url = 'http://bg-fair.tojoycloud.com/mCloud/new_payments.html?qrCodeNo=QR20200206214823985220'  # 请求地址

    headers = {
        'content-type': 'application/xhtml+xml',
        'user-agent': r'Mozilla/5.0 (Linux; Android 8.0.0; Pixel 2 XL Build/OPD1.170816.004) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Mobile Safari/537.36'}  # 创建头部信息
    response = requests.get(url, headers=headers)  # 发送网络请求
    print(response.content.replace(b"\xc2\xab", b"<").replace(b"\xc2\xbb", b">").decode('utf-8'))  # 以字节流形式打印网页源码


if __name__ == '__main__':
    url = "https://tojoyboss.tojoycloud.org/bosscloud-live/v2/api-docs"
    request_get(url)


