#!/user/bin/python
# -*- coding: utf-8 -*-
import re
from calendar import month_abbr
import unicodedata


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
    print s1
    print '进行规范化之前 s1 = s2 %s' % (s1 == s2)
    t1 = unicodedata.normalize('NFC', s1)
    t2 = unicodedata.normalize('NFC', s2)
    print '规范化处理之后 s1 = s2 %s' % (s1 == s2)


def example_2_13():
    """
    对齐文本字符串
    :return: 
    """
    text = 'Hello World'
    print text.ljust(20)
    print text.rjust(20)
    print text.center(20, '*')
    # 都可以使用format()来代替，其功能更强大
    # format()需要进一步深入了解，python在线手册
    print format(text, '=>20')
    print format(text, '<20')
    print format(text, '*^20')
    print '{:>10s} {:>10s}'.format('Hello', 'World')


if __name__ == '__main__':
    # example_2_4()
    # exampie_2_9()
    example_2_13()