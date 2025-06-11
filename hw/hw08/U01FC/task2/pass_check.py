def pass_check(password):
    
    special_symbols = {"$#@"}
    numeric_symbols = set("0123456789")
    alphabetic_symbols_lower = set([chr(i) for i in range(ord('a'),ord('z')+1)])
    alphabetic_symbols_upper = set([chr(i) for i in range(ord('A'),ord('Z')+1)])

    match password:
        case password if len(password) < 6:
            print("Your password is too short. It should contain 6-16 symbols")
        case password if len(password) > 16:
            print("Your password is too long. It should contain 6-16 symbols")
        case password if (special_symbols.isdisjoint(set(password))):
            print("Your password should contain at least 1 special symbol: $, #, @")
        case password if (numeric_symbols.isdisjoint(set(password))):
            print("Your password should contain at least 1 number 0-9")
        case password if (alphabetic_symbols_lower.isdisjoint(set(password))):
            print("Your password should contain at least 1 lowercase letter")
        case password if (alphabetic_symbols_upper.isdisjoint(set(password))):
            print("Your password should contain at least 1 uppercase letter")
        case _:
            print("Ypur password is valid!")


pass_check("412343214")