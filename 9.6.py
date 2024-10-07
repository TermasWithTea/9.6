def func(n):
    i = 0
    while i != n:
        yield i
        i += 1

obj = func(10)
for i in obj:
    print(i)

def all_variants(text):
    i = 0
    for i in text:
        

a = all_variants("abc")
for i in a:
    print(i)
