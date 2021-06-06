# encoding: utf-8
# @Time : 2021/5/26 17:13 
# @Author : js 
# @File : miningdatail.py
# @Contact : jackshen00@outlook.com
import datetime
import json

import requests

def parse_info(info, sum_value):
    # info = '{"code":200,"data":{"list":[{"block_reward":"0.00013252","coin":"chia","height":"338380","huge_reward":"0.00000000","mortgage_rate_k":0,"name":"CHIA","record_time":1622018597,"status":0,"status_str":"UNSETTLEMENT","type":"chia"},{"block_reward":"0.00024327","coin":"chia","height":"338260","huge_reward":"0.00000000","mortgage_rate_k":0,"name":"CHIA","record_time":1622017777,"status":0,"status_str":"UNSETTLEMENT","type":"chia"},{"block_reward":"0.00022123","coin":"chia","height":"338160","huge_reward":"0.00000000","mortgage_rate_k":0,"name":"CHIA","record_time":1622016061,"status":0,"status_str":"UNSETTLEMENT","type":"chia"},{"block_reward":"0.00012548","coin":"chia","height":"338120","huge_reward":"0.00000000","mortgage_rate_k":0,"name":"CHIA","record_time":1622014319,"status":0,"status_str":"UNSETTLEMENT","type":"chia"},{"block_reward":"0.00024353","coin":"chia","height":"338040","huge_reward":"0.00000000","mortgage_rate_k":0,"name":"CHIA","record_time":1622013171,"status":0,"status_str":"UNSETTLEMENT","type":"chia"},{"block_reward":"0.00011817","coin":"chia","height":"337980","huge_reward":"0.00000000","mortgage_rate_k":0,"name":"CHIA","record_time":1622011738,"status":0,"status_str":"UNSETTLEMENT","type":"chia"},{"block_reward":"0.00012561","coin":"chia","height":"337940","huge_reward":"0.00000000","mortgage_rate_k":0,"name":"CHIA","record_time":1622010985,"status":0,"status_str":"UNSETTLEMENT","type":"chia"},{"block_reward":"0.00012563","coin":"chia","height":"337900","huge_reward":"0.00000000","mortgage_rate_k":0,"name":"CHIA","record_time":1622010088,"status":0,"status_str":"UNSETTLEMENT","type":"chia"},{"block_reward":"0.00024382","coin":"chia","height":"337800","huge_reward":"0.00000000","mortgage_rate_k":0,"name":"CHIA","record_time":1622009363,"status":0,"status_str":"UNSETTLEMENT","type":"chia"},{"block_reward":"0.00023663","coin":"chia","height":"337700","huge_reward":"0.00000000","mortgage_rate_k":0,"name":"CHIA","record_time":1622008137,"status":0,"status_str":"UNSETTLEMENT","type":"chia"},{"block_reward":"0.00017036","coin":"chia","height":"337640","huge_reward":"0.00000000","mortgage_rate_k":0,"name":"CHIA","record_time":1622006639,"status":0,"status_str":"UNSETTLEMENT","type":"chia"},{"block_reward":"0.00014831","coin":"chia","height":"337600","huge_reward":"0.00000000","mortgage_rate_k":0,"name":"CHIA","record_time":1622005735,"status":0,"status_str":"UNSETTLEMENT","type":"chia"},{"block_reward":"0.00013338","coin":"chia","height":"337540","huge_reward":"0.00000000","mortgage_rate_k":0,"name":"CHIA","record_time":1622004768,"status":0,"status_str":"UNSETTLEMENT","type":"chia"},{"block_reward":"0.00021527","coin":"chia","height":"337440","huge_reward":"0.00000000","mortgage_rate_k":0,"name":"CHIA","record_time":1622004096,"status":0,"status_str":"UNSETTLEMENT","type":"chia"},{"block_reward":"0.00013409","coin":"chia","height":"337400","huge_reward":"0.00000000","mortgage_rate_k":0,"name":"CHIA","record_time":1622002663,"status":0,"status_str":"UNSETTLEMENT","type":"chia"}],"page":15,"total":1502}}'
    print(info)
    info = json.loads(info)
    for value in info['data']['list']:
        reward = value['block_reward']
        record_time = value['record_time']
        status = value['status_str']
        format_time = datetime.datetime.fromtimestamp(record_time).strftime("%Y-%m-%d %H:%M:%S")
        print(record_time, format_time, reward, status)
        if status == "UNSETTLEMENT":
            sum_value += float(reward)
    return sum_value


if __name__ == '__main__':
    # parse_info("a")
    sum_value = 0
    for i in range(15):
        url = f"https://www.hpool.com/api/pool/miningdetail?language=zh&type=chia&count=15&page={i+1}"

        payload = {}
        headers = {
            'authority': 'www.hpool.com',
            'pragma': 'no-cache',
            'cache-control': 'no-cache',
            'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="90", "Google Chrome";v="90"',
            'accept': 'application/json, text/plain, */*',
            'sec-ch-ua-mobile': '?0',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-mode': 'cors',
            'sec-fetch-dest': 'empty',
            'referer': 'https://www.hpool.com/center/mining',
            'accept-language': 'zh-CN,zh;q=0.9',
            'cookie': 'lang=zh; MEIQIA_TRACK_ID=1rnC4u5sXB3tQtxeVZwMhnxYlkZ; aliyungf_tc=cad565907f2687e55a156c2f09d91f4dba635d4fef2f6d345e98631576b78552; _ga=GA1.2.273711621.1620782876; auth_token=eyJldCI6MTYyMjQzMjg2NiwiZ2lkIjo2NCwidWlkIjoyNzY4MzJ9.kjFXg93gJ9pXAtvB9LCvorIjWOEMCQb3Aon/4GqRY1F5OJ0qHFtS8AyHuY5sRoYfJALzM/gH9/HAE+5q8aFLFH2XbZNiMr/w8JWHSPghQk4ftrz1BNPKaevhBA5s5yhtguW51/Z7dHy7Zj/L8+QC3JyGPJstj6wIzQdEpgt1Ch2uALDzGRGF9/0E1znY6cPWJU9Igc4ZzNzm6JnOqcZbhcfm5GO9B8BKImVAm75PCYRrRElip/umLjb4I7soHTH1p7li80jktrkpsz3RjMh5nKsoRCbWYsU/kqzEez1qsq5pnDKF49XPfpxYyO9k/zN1V8Cxgx8vJNKitVncpiGfMQ==; _gid=GA1.2.325166285.1621999139'
        }

        response = requests.request("GET", url, headers=headers, data=payload)
        sum_value = parse_info(response.text, sum_value)
    print(f"未结算收益：{sum_value} ")


