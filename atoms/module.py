def parse_molecule(formula):
    formula += "!"
    d = {}
    atom = ""
    num = 0
    for i in formula:
        if i.isalpha():
            if i.isupper():
                if atom != "":
                    d[atom] = num
                    num = 0
                atom = i
            else:
                atom += i
        elif i.isdigit():
            num = num*10 + int(i)
        elif i == "!":
            d[atom] = num
    for k in d:
        if d[k] == 0:
            d[k] = 1
    return d