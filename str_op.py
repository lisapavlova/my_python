s = "У лукоморья 123 дуб зеленый 456"
print(s.find('я'))
print(s.count('у'))
s.isalpha()
if not s.isalpha():
    print(s.upper())
len(s)
if len(s) > 4:
    print(s.lower())
print('О' + s[1:])
