import os
import sys

# 环境变量
sys.path.append(os.path.dirname(__file__))

from core import src

if __name__ == '__main__':
    src.run()
