def calculate_chars(string=""):
    """
        Counts each symbol in a string and returns them as a dict
        Args:
            string(str): string to count symbols in
    """
    s = list(string)
    d = {key: 0 for key in s}
    for x in s:
        d[x]+=1
    return d




