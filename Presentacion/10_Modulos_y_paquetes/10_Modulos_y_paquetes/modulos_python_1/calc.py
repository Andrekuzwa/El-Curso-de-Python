def masa_del_planeta(gravedad, radio):
    masa = (gravedad*radio**2)/(6.67*10**-11)
    return masa


def volumen_del_planeta(radio):
    vol = (4*3.142*radio**2)/3
    return vol
