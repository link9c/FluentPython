import inspect

t2 = __import__("promotions")
t3 = __import__('promotions_func')
result = inspect.getmembers(t2, inspect.isclass)
result2 = inspect.getmembers(t2, inspect.isfunction)
result3 = inspect.getmembers(t2, inspect.ismodule)
result4 = inspect.getmembers(t2, inspect.ismethod)
result5 = inspect.getmembers(t2, inspect.isgeneratorfunction)
result6 = inspect.getmembers(t2, inspect.isbuiltin)

promos = [func for name, func in inspect.getmembers(t2, inspect.isclass)]


print(promos)
print(result)
print(result2)
print(result3)
print(result4)
print(result5)
print(result6)
