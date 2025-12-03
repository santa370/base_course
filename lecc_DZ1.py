def mechanical_energy_1(m, v, h):
    g = 10
    Ek = 0.5 * m * v**2
    Ep = m * g * h
    return Ek + Ep




def mechanical_energy_2(m, v=0, h=0):
    g = 10
    Ek = 0.5 * m * v**2
    Ep = m * g * h
    return Ek + Ep





def mechanical_energy_3(**kwargs):
    if all(key in kwargs for key in ['m', 'v', 'h']):
        m = kwargs['m']
        v = kwargs['v']
        h = kwargs['h']
        g = 10
        Ek = 0.5 * m * v**2
        Ep = m * g * h
        return Ek + Ep
    else:
        return "Ошибка: Недостаточно параметров (требуются 'm', 'v', 'h')"


params = {'m': 10, 'v': 5, 'h': 2}
energy = mechanical_energy_3(**params)
print([energy])