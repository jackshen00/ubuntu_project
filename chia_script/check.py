# -*- coding: utf-8 -*- 
# @Time : 2021/5/5 9:13 
# @Author : js
# @File : check.py
# @contact : jackshen00@outlook.com
import os
import subprocess

import psutil as psutil


def get_disk_info(paths):
    usage = {}
    for path in paths:
        path_info = psutil.disk_usage(path)
        total = round(path_info.total / 1024 / 1024, 3)
        used = round(path_info.used / 1024 / 1024, 3)
        free = round(path_info.free / 1024 / 1024, 3)
        free_rate = round(free/total*100, 2)
        usage[path] = [total, used, free, f"{free_rate}%"]
    print(usage)


def get_cpu_info():
    # cpu 逻辑数量
    logical_cpu = psutil.cpu_count()
    physical_cpu = psutil.cpu_count(logical=False)
    print(logical_cpu, physical_cpu)
    total_cpu = psutil.cpu_times().user + psutil.cpu_times().idle
    user_cpu = psutil.cpu_times().user
    cpu_syl = user_cpu / total_cpu * 100
    print("CPU使用率",cpu_syl)

if __name__ == '__main__':
    ssd_path = "/"
    hd1_path = "/mnt/hhd1"
    hd2_path = "/mnt/hhd2"
    hd3_path = "/mnt/hhd3"
    hd4_path = "/mnt/hhd4"
    path_list = [ssd_path, hd1_path, hd2_path, hd3_path, hd4_path]
    # get_disk_info(path_list)
    # get_cpu_info()
    # for pnum in psutil.pids():
    #     p = psutil.Process(pnum)
    #     print(p)
    subprocess.call(["/home/js/Desktop/chia-blockchain/venv/bin/chia", "init"])
    res = os.system("pwd")
    print(res)


