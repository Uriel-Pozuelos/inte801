INGREDIENTES = {
    'harina': {'gramos': 1000, 'unidad': 1},
    'avena': {'gramos': 500, 'unidad': 1},
    'mantequilla': {'gramos': 500, 'unidad': 1},
    'azúcar': {'gramos': 500, 'unidad': 1},
    'huevo': {'gramos': 0, 'unidad': 12},
    'esencia de vainilla': {'gramos': 50, 'unidad': 1},
    'bicarbonato de sodio': {'gramos': 10, 'unidad': 1},
    'pasas': {'gramos': 200, 'unidad': 1},
    'cacao en polvo': {'gramos': 100, 'unidad': 1},
    'chips de chocolate': {'gramos': 200, 'unidad': 1},
    'azúcar glass': {'gramos': 200, 'unidad': 1},
    'almendras fileteadas': {'gramos': 100, 'unidad': 1},
    'jengibre molido': {'gramos': 15, 'unidad': 1},
    'canela': {'gramos': 25, 'unidad': 1},
    'clavo molido': {'gramos': 5, 'unidad': 1},
    'nuez moscada': {'gramos': 5, 'unidad': 1},
    'miel': {'gramos': 50, 'unidad': 1},
    'coco rallado': {'gramos': 150, 'unidad': 1},
    'nueces picadas': {'gramos': 100, 'unidad': 1}
}


CONVERSION = {
    'galon': {'litro': 3.78541, 'mililitro': 3785.41},
    'tarro': {'gramo': 1000, 'miligramo': 1000000},
    'bulto': {'kilogramo': 1000, 'gramo': 1000},
    'caja': {'docena': 12, 'unidad': 1}
}


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