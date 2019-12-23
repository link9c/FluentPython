"""
from collections import defaultdict
from collections import OrderedDict
dict
三种常用的映射方法
"""

import sys
import re

WORD_RE = re.compile(r'\w+')


def demo():
    index = {}
    print(sys.argv[0])
    with open(sys.argv[0], encoding='utf-8') as fp:
        for line_no, line in enumerate(fp, 1):
            for match in WORD_RE.finditer(line):
                word = match.group()
                column_no = match.start() + 1
                location = (line_no, column_no)

                occurrences = index.get(word, [])
                occurrences.append(location)
                index[word] = occurrences
                # index.setdefault(word,[]).append(location)

    for word in sorted(index, key=str.upper):
        print(word, index[word])


if __name__ == '__main__':
    demo()
