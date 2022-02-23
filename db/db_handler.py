"""
数据处理
"""
import json
import os
from conf import settings


def find_user(username):
    # 校验是否存在用户
    # 拼接路径
    user_path = os.path.join(
        settings.USER_DATE_PATH, f'{username}.json'
    )

    # 当用户存在读取文件
    if os.path.exists(user_path):
        with open(user_path, 'r', encoding='utf-8') as f:
            user_dir = json.load(f)
            return user_dir
