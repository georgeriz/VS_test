from collections import defaultdict

def parse_molecule(formula):
    formula = formula.replace('[','(').replace(']',')').replace('{','(').replace('}',')')

    while '(' in formula:
        t = formula.split('(')[-1].split(')')[0]
        c = ''
        for i in formula.split('(')[-1].split(')')[1]:
            if i.isdigit():
                c += i
            else:
				break
        if c == '':
            formula = formula.replace('(' + t + ')', t)
        else:
            formula = formula.replace('(' + t + ')' + c, t*int(c))

    formula += 'Q'
    d = defaultdict(lambda: 0)
    atom = ''
    n = ''
    for i in formula:
        if i.isalpha():
            if i.isupper():
                if atom != '':
                    if n == '':
                        n = '1'
                    d[atom] += int(n)
                    n = ''
                atom = i
            else:
                atom += i
        else:
            n += i

    return d


assert parse_molecule('Mg') == {'Mg': 1}
assert parse_molecule('H2') == {'H': 2}
assert parse_molecule('H2O') == {'H': 2, 'O': 1}
assert parse_molecule('Fe(MgO3)2') == {'Mg': 2, 'Fe': 1, 'O': 6}
assert parse_molecule('Fe(Mg3H)10Au2') == {'Au': 2, 'Fe': 1, 'Mg': 30, 'H': 10}
assert parse_molecule('FeH2O[(MgH2)2O]3O(Fe)3') == {'H': 14, 'Mg': 6, 'Fe': 4, 'O': 5}
assert parse_molecule('(FeO)H') == {'H': 1, 'Fe': 1, 'O': 1}