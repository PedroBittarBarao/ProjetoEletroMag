def Xc(c,omega):
    return -1j/(omega*c)

def Xl(l,omega):
    return 1j*omega*l

def paralelo(impeds):
    sum=0
    for imped in impeds:
        sum+=1/imped
    return 1/sum