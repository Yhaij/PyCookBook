#!/user/bin/python
# -*- coding: utf-8 -*-
import re
from calendar import month_abbr
import unicodedata
import sys
from collections import namedtuple

def change_date(m):
    mon_str = month_abbr[int(m.group(1))]
    return '{} {} {}'.format(m.group(3), mon_str, m.group(2))


def example_2_4():
    """
    re的匹配和替换（部分知识）
    :return: 
    """
    text = 'Today is 11/27/2012. PyCon starts 3/13/2013'
    print text
    detepat = re.compile(r'\d+/\d+/\d') # 将正则表达式编程成一个模式对象
    print detepat.findall(text)  # findall 是返回一个列表,detepat.findall(text, flags=re.IGNORECASE)可以实现不区分大小写
    detepat = re.compile(r'(\d+)/(\d+)/(\d+)') # 将部分表达式用括号包起来引入捕获组,就是说会将括号内匹配出的放在各个group(num)中
    result = detepat.match(r'11/27/2012')
    print result.groups() # 显示元组，元素为捕获组的匹配内容
    print result.group()
    print result.group(0) # group()和group(0) 显示的是匹配的整个字段
    print result.group(1), result.group(2), result.group(3) # 这个显示的就是捕获组对应的内容
    l = detepat.findall(text)
    for item in l:
        print item # 捕获组以元组存储在其中
        month, date, year = item
        print year, month, date
        print '{}-{}-{}'.format(year, month, date)
    # re的替换
    text_new = detepat.sub(r'\3-\1-\2', text) # 这里的\3就是捕获组的第三个
    print text_new
    text_new = detepat.sub(change_date, text) # 使用回调函数实现复杂的情况,也可以使用lambda表达式来实现
    print text_new
    text_new = detepat.sub(lambda m: '{} {} {}'.format(m.group(3), month_abbr[int(m.group(1))], m.group(2)), text)
    print text_new


def exampie_2_9():
    """
    将Unicode文本统一表示为规范形式
    只讲了一点点，深入需要参考更多(代码有错误，没看懂)
    :return: 
    """
    s1 = 'Spicy Jalapa\u00f1o'
    s2 = 'Spicy Jalapa\u0303o'
    # s1 = s1.decode('utf-8')
    # s2 = s2.decode('utf-8')
    print(s1)
    print('进行规范化之前 s1 = s2 %s' % (s1 == s2))
    t1 = unicodedata.normalize('NFC', s1)
    t2 = unicodedata.normalize('NFC', s2)
    print('规范化处理之后 s1 = s2 %s' % (s1 == s2))


def example_2_13():
    """
    对齐文本字符串
    :return: 
    """
    text = 'Hello World'
    print(text.ljust(20))
    print(text.rjust(20))
    print(text.center(20, '*'))
    # 都可以使用format()来代替，其功能更强大
    # format()需要进一步深入了解，python在线手册
    print(format(text, '=>20'))
    print(format(text, '<20'))
    print(format(text, '*^20'))
    print('{:>10s} {:>10s}'.format('Hello', 'World'))


class safesub(dict):
    def __missing__(self, key):
        return '{'+ key +'}'


def sub(text):
    return text.format(**safesub(sys._getframe(1).f_locals))


def example_2_15():
    """
    使用局部变量来实现字符串的插值
    :return: 
    """
    name = 'jj'
    n = 99
    s = '{name} has {n} messages'
    print(sub(s))


def generate_tokens(pat, text):
    Token = namedtuple('Token', ['type', 'value']) # 第一章中的对列表元素命名
    scanner = pat.scanner(text) # 使用scanner()模式对象来进行操作
    for m in iter(scanner.match, None): # scanner.match()扫面匹配的串，iter根据方法产生迭代器（必须为迭代方法）
        yield Token(m.lastgroup, m.group())


def example_2_18():
    """
    简单分词处理
    :return: 
    """
    name = r'(?P<NAME>[a-zA-Z_][a-zA-Z_0-9]*)'
    num = r'(?P<NUM>\d+)'
    plus = r'(?P<PLUS>\+)'
    time = r'(?P<TIMES>\*)'
    eq = r'(?P<EQ>=)'
    ws = r'(?P<WS>\s+)'
    master_pat = re.compile('|'.join([name, num, plus, time, eq, ws])) # 还可以这样，就是一个满足的正则表达式字符串
    for tok in generate_tokens(master_pat, 'foo =12'):
        print tok

if __name__ == '__main__':
    # example_2_4()
    # exampie_2_9()
    # example_2_13()
    # example_2_15()
    example_2_18()