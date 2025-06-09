# !/usr/bin/python
# -*- coding: UTF-8 -*-

import re
import os
import stat
import time
import json
import logging
import chardet

py_dir = os.path.dirname(os.path.abspath(__file__))

logging.basicConfig(filename=os.path.join(py_dir, "brand_switch.log"), level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')


def deal_file(rule_json):
    """
    功能描述：单条规则处理
    返回值：NA
    异常描述：NA
    """
    file_dir = rule_json.get('FilePath')
    exclude_path = rule_json.get('ExcludePath')
    file_suffix = rule_json.get('FileSuffix')
    string_replace = rule_json.get('StringReplace')
    file_rename = rule_json.get('FileRename')
    file_names = os.listdir(file_dir if file_dir else ".")

    for file_name in file_names:
        if exclude_path and re.match(exclude_path, file_name):
            logging.info("=======> %s exclude_path %s", exclude_path, file_name)
            continue
        file_path = os.path.join(file_dir, file_name)
        logging.info("=======>begin... :%s", file_path)
        if os.path.isdir(file_path):
            # 文件夹处理
            rule_json['FilePath'] = file_path
            deal_file(rule_json)
        elif string_replace:
            # 字符串
            deal_str(file_path, file_suffix, string_replace)
        # 文件重命名
        if file_rename and file_name in file_rename:
            dst_path = os.path.join(file_dir, file_rename.get(file_name))
            time.sleep(1)
            logging.info("rename:%s --> %s", file_path, dst_path)
            os.rename(file_path, dst_path)
        logging.info("=======>end... :%s", file_path)


def deal_str(file_path, file_suffix, string_replace, encode="utf-8"):
    """
    功能描述：字符串替换
    返回值：NA
    异常描述：NA
    """
    # 文件后缀判断
    _, suffix = os.path.splitext(file_path)
    if file_suffix and not re.search(file_suffix, suffix, re.I):
        logging.info("%s mismatch suffix:%s", file_path, file_suffix)
        return
    with open(file_path, "rb") as file0:
        chardet_json = chardet.detect(file0.read())
        encode = chardet_json.get("encoding")
        logging.info("%s encoding:%s", file_path, encode)

    # 文件字符串替换
    data = ""
    with open(file_path, "r", encoding=encode) as file1:
        data = file1.read()
        for key in string_replace:
            logging.info("%s match count: %s", key, len(re.findall(key, data)))
            data = re.sub(key, string_replace.get(key), data)

    with os.fdopen(os.open(file_path, os.O_WRONLY | os.O_TRUNC, stat.S_IWUSR), 'w', encoding=encode) as file2:
        file2.write(data)


def deal_rule(rule_path=""):
    """
    功能描述：规则解析
    返回值：NA
    异常描述：NA
    """
    if not rule_path:
        rule_path = os.path.join(py_dir, "brand_switch.json")
    logging.info("rule_path is %s", rule_path)
    if not os.path.exists(rule_path):
        logging.info("%s is not exists", rule_path)
        return
    rule_json = {}
    with open(rule_path, "r", encoding="utf-8") as file1:
        rule_json = json.loads(file1.read())
    for rule in rule_json.get('Rules'):
        deal_file(rule)


if __name__ == "__main__":
    """
    功能描述：程序功能入口
    1. 如果不需要支持老服务器，需要把其他模板删除，需要支持就新增模板
    2. 现在zabbix服务器上全克隆模板生成新的uuid，导出后再替换
    """
    deal_rule()
