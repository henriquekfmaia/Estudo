import math
angles = {'graus':math.pi/180, 'rad':1}
measure = {'mm':0.001, 'cm':0.01, 'm':1, 'in':0.0254}


def convert(initial, target, value):
    if initial in angles and target in angles:
        value = value*angles[initial]/angles[target]
        return value

    elif initial in measure and target in measure:
        value = value*measure[initial]/measure[target]
        return value

    elif (initial in angles and target in measure) or (initial in measure and target in angles):
        print('Unidades diferentes')

    elif initial in angles or initial in measure:
        print ('Unidade desejada invalida')

    elif target in angles or target in measure:
        print(initial)
        print('Unidade fornecida invalida')

    else:
        print('Unidades fornecidas invalidas')



