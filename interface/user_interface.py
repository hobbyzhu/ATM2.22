# 用户验证模块
import os
from conf import settings
import json


def register_interface(username, passwd, balance=15000):
    user_dic = {
        'username': username,
        'password': passwd,
        'balance': balance,
        # 记录流水
        'flow': [],
        # 记录用户购物车
        'shop_car': {},
        # locked： 用户状态
        'locked': False,
    }

    # 路径拼接
    user_path = os.path.join(
        settings.USER_DATE_PATH, f'{username}.json'
    )
    print(user_path)
    with open(user_path, mode='w', encoding='utf-8') as f:
        json.dump(user_dic, f, ensure_ascii=False)
