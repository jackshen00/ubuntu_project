import os
import pathlib
import shutil

import yaml


def _get_config():
    """
    使用时将cluster-sample.yaml 改为 cluster.yaml
    :return:
    """
    directory = pathlib.Path().resolve()
    file_name = 'cluster.yaml'
    file_path = os.path.join(directory, file_name)
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Unable to find the config.yaml file. Expected location: {file_path}")
    f = open(file_path, 'r')
    config = yaml.load(stream=f, Loader=yaml.Loader)
    f.close()
    return config


def make_dir(root_path, name):
    """
    创建节点文件夹
    """
    path = f"{root_path}/{name}"
    flag = os.path.exists(path)
    if not flag:
        print(f"节点 {name} 不存在，正在创建中......")
        os.makedirs(path)
    else:
        print(f"节点 {name} 已存在")

    bee_path = f"{path}/.bee"
    flag1 = os.path.exists(bee_path)
    if not flag1:
        print("创建 .bee 文件夹......")
        os.makedirs(bee_path)
    else:
        print(f"文件夹 .bee 已存在")
    return path, bee_path


def make_yaml(path, info):
    """
    在path路径下， 创建 bee.yaml 文件
    """
    file = f"{path}/bee.yaml"
    del info['name']
    info['data-dir'] = f"{path}/.bee"
    print(f"正在生成bee.yaml 文件.....")
    with open(file, "w", encoding="utf-8") as f:
        yaml.dump(info, f)
    print(f"bee.yaml 文件生成完毕！！！")


def copy_file(path):
    """
    将相关软件复制到目标文件夹
    """
    print(f"复制相关软件到 {path}")
    target = "../source/bee.exe"
    dest = f"{path}/bee.exe"
    shutil.copyfile(target, dest)


def deploy_bee(root_path, info):
    """
    部署 bee 节点
    :param root_path: 所有节点的根目录
    :param info: bee.yaml 所需的配置信息
    :return:
    """
    name = info['name']
    path, bee_path = make_dir(root_path, name)
    print(f"节点文件夹 {path} {bee_path} 创建完毕")
    make_yaml(path, info)
    copy_file(path)


def main():
    config = _get_config()
    root_path = config['path']
    for info in config['cluster']:
        node = info['name']
        deploy_bee(root_path, info)
        print(f"节点{node} 部署完成")


if __name__ == '__main__':
    main()
