var_a = 100
var_b = 'string'

print(f"Now 'var_a' = {var_a} and var_b = {var_b}")

var_a, var_b = var_b, var_a

print(f"After var_a = {var_a}, var_b = {var_b}")