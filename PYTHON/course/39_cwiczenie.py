
def slittekst(element: str) -> str:
    """
    Zamiana liter: co druga duża i mała
    :param element: String
    :return: Zamieniony String
    """
    ile = int(len(element))
    s = ''
    for i in range(0, ile):
        if i % 2 == 0:
            s += element[i].upper()
        else:
            s += element[i].lower()
    return s


print(slittekst('Jsystems'))

# print(slittekst.__doc__)
#  print(slittekst.__annotations__)

# tekst_in = 'Jsystems'
# tekst_out = ''.join([ tekst_in[i] if i % 2 else tekst_in[i].upper() for i in range(0, len(tekst_in)) ])
# print(tekst_out)
