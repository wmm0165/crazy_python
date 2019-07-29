# -*- coding: utf-8 -*-
# @Time : 2019/6/28 11:20
# @Author : wangmengmeng
from pathlib import *

p = Path('a_test.txt')
result = p.write_text("""有一个美丽的世界，它在远方等我""",encoding='utf-8')
print(result) # 返回输出的字符数
content = p.read_text(encoding='utf-8')
print(content)
