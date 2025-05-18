# def calc_symbols(string):
#     result = {}
#     for i in set(string):
#         num = string.count(i)
#         result[i] = num
#     print(result)
# 
def calc_symbols(string):
    result = {key: string.count(key) for key in set(string)}
    print(result)

calc_symbols('hello')
calc_symbols('parse Factors e-enable')
