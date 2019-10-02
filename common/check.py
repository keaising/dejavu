import re
import string


def check_mobile(s):
    """To check a mobile is properly or not."""
    reg = "1[3|4|5|6|7|8|9][0-9]{9}"
    return True if re.findall(reg, s) else False


def check_password(s):
    """To check a password is properly or not.

    密码必须符合以下规则
    1.长度 >= 8
    2.包含数字、大写字母、小写字母以及特殊符号中的至少3种
    3.不能包含支持的字符以外的字符
    """
    s = s.strip()
    a = len(s) >= 8
    b1 = re.findall(r"\d", s)
    b2 = re.findall(r"[A-Z]", s)
    b3 = re.findall(r"[a-z]", s)
    b4 = re.findall(r"[^0-9A-Za-z]", s)
    c = re.findall(r"[0-9a-zA-Z!@#$%^&*()_+,./?]", s)
    return (
        True
        if a and [b1, b2, b3, b4].count([]) < 2 and len(c) == len(s)
        else False
    )
