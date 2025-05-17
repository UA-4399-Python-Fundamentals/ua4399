def class_name_changer(cls, new_name):
    if new_name[0].lower() == new_name[0] or not(new_name.isalnum()):
        raise ValueError
    
    cls.__name__ = new_name