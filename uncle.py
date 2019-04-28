s = "Мой дядя самых честных правил, \
Когда не в шутку занемог, \
Он уважать себя заставил \
И лучше выдумать не мог"
i = 0
new = ''
while i < len(s):
    if s[i] == 'м' and s[i-1] == ' ':
        while s[i].isalpha():
                i = i + 1
                if i >= len(s):
                    break
    else:
        new = new + s[i]
        i = i + 1
print(new)
        
