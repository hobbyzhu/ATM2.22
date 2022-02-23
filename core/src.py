"""
用户视图层
1.用户注册
2.用户登录
3.余额查询
4.用户提现
5.用户还款
6.用户转账
7.流水查询
8.用户购物
9.购物车
10.管理员功能
"""
from db.db_handler import find_user
from interface import user_interface


# 1.用户注册
def register():
    while True:
        username = input('username：').strip()
        passwd = input('password：').strip()
        re_passwd = input('re_passwd：').strip()

        if passwd == re_passwd:
            find_user(username)
            user_interface(username, passwd)








# 2.用户登录
def login():
    pass


# 3.余额查询
def check_balance():
    pass


# 4.用户提现
def withdraw():
    pass


# 5.用户还款
def repay():
    pass


# 6.用户转账
def transfer():
    pass


# 7.流水查询
def check_flow():
    pass


# 8.用户购物
def shopping():
    pass


# 9.购物车
def check_shop_car():
    pass


# 10.管理员功能
def admin():
    pass


# 函数功能字典
function_dict = {
    '1': register,
    '2': login,
    '3': check_balance,
    '4': withdraw,
    '5': repay,
    '6': transfer,
    '7': check_flow,
    '8': shopping,
    '9': check_shop_car,
    '10': admin

}


def run():
    while True:
        print("""
            1.用户注册
            2.用户登录
            3.余额查询
            4.用户提现
            5.用户还款
            6.用户转账
            7.流水查询
            8.用户购物
            9.购物车
            10.管理员功能
    
    """)
        choose = input('请输入:')
        if choose not in function_dict:
            print('请重新输入:')
            continue

        function_dict.get(choose)()
