"""
存放配置文件
"""
import os

# 获取根目录
BASE_PATH = os.path.dirname(os.path.dirname(__file__))
# 拼接路径
USER_DATE_PATH = os.path.join(BASE_PATH, 'db', 'user_date')

