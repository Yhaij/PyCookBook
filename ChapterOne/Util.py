#!/user/bin/python
# -*- coding: utf-8 -*-

import heapq
from collections import defaultdict
"""
可以实现一对多的字典（实际上是对应的key值下创建一个列表或集合，放入多个value）
d = defaultdict(list)
d['a'].append(1)
d['a'].append(2)
for key,value in paris:
    d[key].append(value) # 不需要考虑主键key是否存在

d = defaultdict(set)
d['a'].add(1)
d['a'].add(2)
"""


from collections import OrderedDict
"""
可以实现一个有顺序的字典（即按照字典插入的顺序排列）
d = OrderedDict()
d['a'] = 1
d['b'] = 2
d['c'] = 3
for key in d:
    print key,d[key]
"""

# zip(dict)能将字典的键值对转为值和键的映射

from operator import itemgetter
"""
itemgetter()是返回一个函数，得到列表、集合、元组中的某个位置的值或字典某个key值（完全可以用lambda表达式来完成,但itemgetter的性能更好一点）
teamitems = [{'team':'France'     , 'P':1 , 'GD':-3 , 'GS':1 , 'GA':4},
            {'team':'Uruguay'     , 'P':7 , 'GD':4  , 'GS':4 , 'GA':0},
            {'team':'SouthAfrica' , 'P':4 , 'GD':-2 , 'GS':3 , 'GA':5},
            {'team':'Mexico'      , 'P':4 , 'GD':1  , 'GS':3 , 'GA':2}]
print sorted(teamitems, key = lambda x:(x['P'],x['GD'],x['GS'],x['GA']),reverse=True)
print sorted(teanitems, key=itemgetter('P', 'GD', 'GS', 'GA'), reverse=True)
输出 
[{'P': 7, 'GD': 4, 'GS': 4, 'GA': 0, 'team': 'Uruguay'},  
 {'P': 4, 'GD': 1, 'GS': 3, 'GA': 2, 'team': 'Mexico'},  
 {'P': 4, 'GD': -2, 'GS': 3, 'GA': 5, 'team': 'SouthAfrica'},  
 {'P': 1, 'GD': -3, 'GS': 1, 'GA': 4, 'team': 'France'}]
 
 针对类的属性来比较的话，可以使用attrgetter()
"""

from collections import namedtuple
"""
对元组或列表中的索引（位置）进行命名,不能直接改变其属性值,用._replace(**kwargs)可以改变其值，
Stock = namedtuple('Stock', ['name', 'shares', 'price', 'date'])
s = Stock('ACME', 100, 12.56, '17/06/14')
>>> s
Stock(name='ACME', shares=100, price=12.56, date='17/06/14')
>>> s.name
ACME
s = s._replace(shares=70, price=12)
>>> s.shares
70
d = {name: 'BOB', shares=60, price=17, date='17/06/14'}
s = s._replace(**d)
>>> s
Stock(name='BOB', shares=60, price=17, date='17/06/14')

total = 0.0
for rec in records:
    s = Stock(rec)
    total = s.shares * s.price

"""



class PriorityQueue:
    """
    优先级队列
    heapq.heapify()将一个列表转化为堆
    """
    def __init__(self, queue=list()):
        self._queue = heapq.heapify(queue)
        self._index = 0

    def push(self, item, priority):
        # 传入了元组，因为元组中的可哈希对象是可以比较的，如（2,3）> (3,1)或（2,3）>(2,2) is True
        heapq.heappush(self._queue, (-priority, self._index, item))
        self._index += 1

    def pop(self):
        return heapq.heappop(self._queue)[-1]


def dequpe(items, key=None):
    """
    去除列表中的重复记录，并且保持原来的顺序
    :param items: 
    :param key: 如果元素是可哈希的则不需要，如果是不可哈希的，则需要key()方法转为可哈希对象（因为set中存放的元素必须是可哈希的）
    :return: 
    """
    seen = set()
    for item in items:
        val = item if key is None else key(item)
        if val not in seen:
            yield item
            seen.add(item)

# if __name__ == '__main__':
#     a = [{'x': 1, 'y': 2}, {'x': 1, 'y': 3}, {'x': 1, 'y': 2}, {'x': 4, 'y': 2}]
#     list(dequpe(a, key=lambda d: (d['x'], d['y'])))
