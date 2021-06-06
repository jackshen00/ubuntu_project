# encoding: utf-8
# @Time : 2021/5/26 10:17 
# @Author : js 
# @File : soft-monitor.py
# @Contact : jackshen00@outlook.com
import json
import os
import pathlib
import re

import requests
import yaml
from loguru import logger

Webhook = "https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=937482f5-7ee6-4ba8-8040-33edf4141543"


def monitor_github(soft):
    prefix = "https://github.com/"
    suffix = "/releases/latest"
    url = prefix + soft + suffix
    response = requests.get(url)
    match = re.search(r"<title>(.*?)</title>", response.text)
    if match:
        title = match.group(1)
        return True, title, url
    else:
        return False, "DO NOT MATCH ANYTHING, PLEASE CHECK SCRIPT", url


def _get_config():
    directory = pathlib.Path().resolve()
    file_name = 'version.yaml'
    file_path = os.path.join(directory, file_name)
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Unable to find the config.yaml file. Expected location: {file_path}")
    f = open(file_path, 'r')
    config = yaml.load(stream=f, Loader=yaml.Loader)
    f.close()
    return config


def sent_msg(msg):
    """

    """
    logger.info(msg)
    connet = {"msgtype": "text", "text": {"content": msg}}
    headers = {'Content-Type': 'application/json'}
    payload = json.dumps(connet)
    response = requests.request("POST", Webhook, headers=headers, data=payload)
    return response


def update_yaml(key, value):
    """
    更新yaml中的文件信息
    """
    directory = pathlib.Path().resolve()
    file_name = 'version.yaml'
    file_path = os.path.join(directory, file_name)
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Unable to find the config.yaml file. Expected location: {file_path}")
    with open(file_path) as f:
        doc = yaml.safe_load(f)
    doc[key] = value
    with open(file_path, "w") as f:
        yaml.safe_dump(doc, f, default_flow_style=False)


def main():
    """
    监控chia以及hpool软件更新，及时通知企业微信机器人
    """
    soft_list = {"swar": "swar/Swar-Chia-Plot-Manager", "chia": "Chia-Network/chia-blockchain",
                 "hpool": "hpool-dev/chia-miner"}
    ver = _get_config()
    for soft, values in soft_list.items():
        flag, title, url = monitor_github(values)
        if flag:
            version = title.split("·")[0].replace("Release", "").strip()
            # logger.info([title, version])
            if version == ver[soft]:
                logger.info(f"软件 {soft} 已经是最新版。")
            else:
                msg = f"软件 {soft} 有最新版本 {title}, 请前往 {url} 进行更新"
                logger.info(msg)
                response = sent_msg(msg)
                update_yaml(soft, version)
                if response.status_code == 200 and response.text == '{"errcode":0,"errmsg":"ok"}':
                    logger.info(f"企业微信机器人通知 {soft} 完毕")
        else:
            logger.error(title)


if __name__ == '__main__':
    main()
    # update_yaml("swar", "Release v.0.1.0 · swar/Swar-Chia-Plot-Manager · GitHub")
