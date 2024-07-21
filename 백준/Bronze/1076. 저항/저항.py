tab = {'ck': 0, 'wn': 1, 'ed': 2, 'ge': 3, 'ow': 4, 'en': 5, 'ue': 6, 'et': 7, 'ey': 8, 'te': 9}
print(sum(tab[input()[-2:]]*10**(1-i) for i in range(2)) * int(10**tab[input()[-2:]]))