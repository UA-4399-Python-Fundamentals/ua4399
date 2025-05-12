def cal_chars(string):
    lst = list(string)
    rez = {}
    for i in lst:
        if i not in rez.keys():
            rez.update({i:1})
        else: rez.update({i:rez.get(i) + 1 })
    return rez

string = str(input('Enter string: '))

print(cal_chars(string))