import re
from functools

def replace_7t(s):
    return s.replace('7','t')

def replace_3e(s):
    return s.replace('3','e')

def replace_6g(s):
    return s.replace('6','g')

def replace_4a(s):
    return s.replace('4','a')

class chinese_matcher:
    def __init__(self):
        self.r = re.compile(r'[\u4e00 - \u9fff]+')

    def sub_chinese(self,s):
        return self.r.sub(s," ")

