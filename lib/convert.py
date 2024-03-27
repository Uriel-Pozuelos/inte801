INGREDIENTES = {
    'harina': {'gramos': 1000, 'unidad': 1, 'id': 1},
    'avena': {'gramos': 500, 'unidad': 1, 'id': 2},
    'mantequilla': {'gramos': 500, 'unidad': 1, 'id': 3},
    'azúcar': {'gramos': 500, 'unidad': 1, 'id': 4},
    'huevo': {'gramos': 0, 'unidad': 12, 'id': 5},
    'esencia de vainilla': {'gramos': 50, 'unidad': 1, 'id': 6},
    'bicarbonato de sodio': {'gramos': 10, 'unidad': 1, 'id': 7},
    'pasas': {'gramos': 200, 'unidad': 1, 'id': 8},
    'cacao en polvo': {'gramos': 100, 'unidad': 1, 'id': 9},
    'chips de chocolate': {'gramos': 200, 'unidad': 1, 'id': 10},
    'azúcar glass': {'gramos': 200, 'unidad': 1, 'id': 11},
    'almendras fileteadas': {'gramos': 100, 'unidad': 1, 'id': 12},
    'jengibre molido': {'gramos': 15, 'unidad': 1, 'id': 13},  
    'canela': {'gramos': 25, 'unidad': 1, 'id': 14},
    'clavo molido': {'gramos': 5, 'unidad': 1, 'id': 15},
    'nuez moscada': {'gramos': 5, 'unidad': 1   , 'id': 16},
    'miel': {'gramos': 50, 'unidad': 1  , 'id': 17},
    'coco rallado': {'gramos': 150, 'unidad': 1, 'id': 18},
    'nueces picadas': {'gramos': 100, 'unidad': 1, 'id': 19},
}




def getIDbyName(name):
    for key, value in INGREDIENTES.items():
        if key == name:
            return value['id']
    return None

CONVERSION = {
    'galon': {'litro': 3.78541, 'mililitro': 3785.41},
    'tarro': {'gramo': 1000, 'miligramo': 1000000},
    'bulto': {'kilogramo': 1000, 'gramo': 1000},
    'caja': {'docena': 12, 'unidad': 1}
}

def getIDbyName(name):
    for key in INGREDIENTES:
        if INGREDIENTES[key]['id'] == name:
            return key
    return None

def convertirMaxToMin(cantidad, tipo):
    if tipo in CONVERSION:
        for key in CONVERSION[tipo]:
            cantidad = cantidad * CONVERSION[tipo][key]
            tipo = key
            break
    return cantidad, tipo


def convertirMinToMax(cantidad, tipo):
    if tipo in CONVERSION:
        for key in CONVERSION[tipo]:
            cantidad = cantidad / CONVERSION[tipo][key]
            tipo = key
            break
    return cantidad, tipo