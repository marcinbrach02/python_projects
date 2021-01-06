s = 5
while s > 0:
    rok = int(input('W którym roku odbyła się bitwa pod Grunwaldem? \n'))
    s -= 1
    if rok == 1410:
        print('Brawo!')
        break
    elif rok >= 1400 and rok <= 1420:
        print('Blisko')
    else:
        print('Żle')


