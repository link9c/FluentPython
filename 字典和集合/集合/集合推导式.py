from unicodedata import name

set_list = {chr(i) for i in range(32, 256) if 'SIGN' in name(chr(i), '')}
print(set_list)
