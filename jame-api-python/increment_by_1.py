dict={}
for i in range(10):
    key=str('x'=str(i))
    dict[key]=i
print(dict)
for key,value in dict.items():
    exec(f'{key}={value}')
print(x1)