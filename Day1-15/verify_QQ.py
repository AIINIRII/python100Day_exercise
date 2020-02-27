import re


def verify(username, qq_num):
    """
    Can verify if the User name or QQ number is valid
    用户名必须由字母、数字或下划线构成且长度在6~20个字符之间，QQ号是5~12的数字且首位不能为0
    """

    valid_username = re.compile(r"^[0-9a-zA-Z_]{6,20}$")
    valid_qq_num = re.compile(r"^[1-9]\d{4,11}$")
    while True:
        if re.match(valid_username, username):
            print(f"username: {username} is valid")
            if re.match(valid_qq_num, qq_num):
                print(f"qq number: {qq_num} is valid")
                return
            else:
                print(f"qq number: {qq_num} is not valid, please try another one: ")
                qq_num = input()
        else:
            print(f"username: {username} is not valid, please try another one: ")
            username = input()


if __name__ == '__main__':
    user_name = input("Please enter user name: ")
    qq_numb = input("Please enter qq number: ")
    verify(user_name, qq_numb)
