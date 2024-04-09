from flask import Blueprint, request, render_template,jsonify, Response,flash, redirect
from models.Recetas import Galletas,Ingredientes,MateriaPrima,db
from models.proveedor import Proveedor
from lib.d import D
from lib.jwt import allowed_roles, token_required


recetas = Blueprint('recetas', __name__, template_folder='templates')

log = D(debug=True)

# @recetas.route('/proveedores')
# def proveedores():
#     proveedores = Proveedor.query.all()
#     # prov = [proveedor.serialize() for proveedor in proveedores]
#     return Response("ok")


def get_Galletas():
    galletas = Galletas.query.filter_by(enable=1).all()
    return [galleta.serialize() for galleta in galletas]

def get_names_materials():
    #obtener los nombres de los materiales
    materiales = MateriaPrima.query.with_entities(MateriaPrima.material).all()

    return [material[0] for material in materiales]


def getIDbyName(name):
    material = MateriaPrima.query.filter_by(material=name).first()
    return material.id


def get_ingrediente(id):
    #unir las tablas de ingredientes y materia prima
    ingredientes = Ingredientes.query.filter_by(galleta_id=id).all()
    materiales = MateriaPrima.query.all()

    #crear un diccionario con los materiales
    materiales_dict = {}
    for material in materiales:
        materiales_dict[material.id] = material.serialize()

    #crear un diccionario con los ingredientes
    ingredientes_dict = {}
    for ingrediente in ingredientes:
        ingredientes_dict[ingrediente.id] = ingrediente.serialize()

    #unir los diccionarios
        
    for key in ingredientes_dict:
        ingredientes_dict[key]['material'] = materiales_dict[ingredientes_dict[key]['material_id']]['material']
        ingredientes_dict[key]['tipo'] = materiales_dict[ingredientes_dict[key]['material_id']]['tipo']

        ingredientes_dict[key].pop('material_id')

    return [ingrediente for ingrediente in ingredientes_dict.values()]



def get_galleta_by_id(id):
    galleta = Galletas.query.get(id)
    return galleta.serialize()

def get_tipo_material():
    material = MateriaPrima.query.with_entities(MateriaPrima.tipo).distinct().all()
    return [material[0] for material in material]

"""
ingredientes = [{'id': '5', 'cantidad': '500.00', 'tipo': 'gramos'}, {'id': '6', 'cantidad': '50.00', 'tipo': 'mililitros'}, {'id': '7', 'cantidad': '45.00', 'tipo': 'gramos'}, {'id': '8', 'cantidad': '100.00', 'tipo': 'gramos'}]
"""
def update_ingredientes(ingredientes):
    #hacer un bulk update
    for ingrediente in ingredientes:
        ingrediente_id = ingrediente['id']
        cantidad = ingrediente['cantidad']
        material = ingrediente['material']


        ingrediente = Ingredientes.query.get(ingrediente_id)
        ingrediente.cantidad = cantidad
        ingrediente.material_id = material
        db.session.commit()


def addIngrediente(galleta_id, material_id, cantidad):
    ingrediente = Ingredientes(galleta_id=galleta_id, material_id=material_id, cantidad=cantidad)
    db.session.add(ingrediente)
    db.session.commit()
        

def delete_galleta(id):
    #en lugar de eliminar la galleta, cambiar el estatus a 0
    galleta = Galletas.query.get(id)
    galleta.enable = 0
    db.session.commit()




def update_receta(id,receta):
    galleta = Galletas.query.get(id)
    galleta.receta = receta
    db.session.commit()

def controller_updates(form):
    # form regresa ImmutableMultiDict([('csrf_token', 'IjZjOTRjOGUyMTlhNTdkYzAzOGZmODJkNDlkNTRiNDFmYTdiZjU4M2Yi.ZgNnGA.-KwbwaZvAj06QHd7N-Wibb8QCFk'), ('tipo_5', 'gramos'), ('cantidad_5', '500.00'), ('material_5', 'avena'), ('tipo_6', 'mililitros'), ('cantidad_6', '50.00'), ('material_6', 'esencia de vainilla'), ('tipo_7', 'gramos'), ('cantidad_7', '5.00'), ('material_7', 'bicarbonato de sodio'), ('tipo_8', 'gramos'), ('cantidad_8', '100.00'), ('material_8', 'cacao en polvo'), ('receta', 'Galleta de chocolate con chips'), ('id', '2'), ('save', 'Guardar')])
    ingredientes = []
    log.info(form)
    for key in form:
        if 'cantidad_' in key:
            #id es el id del ingrediente
            id = key.split('_')[1]
            log.warning(key.split('_'))
            ingredientes.append({
                'id': id,
                'cantidad': form['cantidad_'+id],
                'material': getIDbyName(form['material_'+id])
              
            })

    update_receta(form['id'], form['receta'])
    update_ingredientes(ingredientes)

    log.info(ingredientes)

def delete_ingredientes(id):
    ingrediente = Ingredientes.query.get(id)
    print(ingrediente)
    db.session.delete(ingrediente)

    db.session.commit()


@recetas.route('/recetas')
@token_required
@allowed_roles(['admin','produccion','compras'])
def index():
    recetas = get_Galletas()
    log.info(recetas)
    return render_template('pages/recetas/index.html', recetas=recetas)

@recetas.route('/recetas/<int:id>', methods=['GET', 'POST'])
@token_required
@allowed_roles(['admin','produccion','compras'])
def show(id):

    ingredientes = get_ingrediente(id)
    receta = get_galleta_by_id(id)
    receta = {key: receta[key] for key in ['id', 'receta', 'nombre', 'precio', 'descripcion', 'totalGalletas', 'pesoGalleta']}
    material_option = get_names_materials()
    tipo = get_tipo_material()

    log.info(receta)
    
    if request.method == 'POST':
        if 'delete' in request.form:
            delete_galleta(id)
            flash('Receta eliminada con éxito', 'success')
            return redirect('/recetas')
        if 'edit' in request.form:
            return render_template('pages/recetas/show.html', ingredientes=ingredientes, id=id, receta=receta, isEdit=True, material_options=material_option, tipos=tipo)
        elif 'regret' in request.form:
            return render_template('pages/recetas/show.html', ingredientes=ingredientes, id=id, receta=receta, isEdit=False)
        elif any([True for key in request.form if 'delete_' in key]):
            id_to_delete = [key.split('_')[1] for key in request.form if 'delete_' in key][0]
            delete_ingredientes(id_to_delete)
            # Después de eliminar, obtén la lista actualizada de ingredientes
            ingredientes = get_ingrediente(id)
            receta = get_galleta_by_id(id)
            return render_template('pages/recetas/show.html', ingredientes=ingredientes, id=id, receta=receta, isEdit=False)
        elif 'add' in request.form:
            material = request.form['ingrediente']
            cantidad = request.form['cantidad']
            addIngrediente(id, getIDbyName(material), cantidad)
            # Después de agregar, obtén la lista actualizada de ingredientes
            ingredientes = get_ingrediente(id)
            receta = get_galleta_by_id(id)
            return render_template('pages/recetas/show.html', ingredientes=ingredientes, id=id, receta=receta, isEdit=False)
        elif 'save' in request.form:
            receta = request.form['receta']
            id = request.form['id']
            
            controller_updates(request.form)
            
            receta = get_galleta_by_id(id)
            ingredientes = get_ingrediente(id)
            return render_template('pages/recetas/show.html', ingredientes=ingredientes, id=id, receta=receta, isEdit=False)
        elif 'change' in request.form:
            filename = f"static/img/{id}.webp"
            file = request.files['file']
            file.save(filename)

        



    return render_template('pages/recetas/show.html', ingredientes=ingredientes, id=id, receta=receta, isEdit=False)


def create_galleta(form):
    receta = form['receta']
    nombre = form['nombre']
    precio = form['precio']
    descripcion = form['descripcion']
    totalGalletas = form['totalGalletas']
    pesoGalleta = form['pesoGalleta']
    galleta = Galletas( nombre=nombre, precio=precio, descripcion=descripcion, totalGalletas=totalGalletas, pesoGalleta=pesoGalleta,receta=receta)
    db.session.add(galleta)
    db.session.commit()
    return galleta.id

def create_ingredientes(form, id):
    for key in form:
        if 'cantidad_' in key:
            #id es el id del ingrediente
            id = key.split('_')[1]
            addIngrediente(id, getIDbyName(form['material_'+id]), form['cantidad_'+id])

def save_image(id, file):
    filename = f"static/img/{id}.webp"
    file.save(filename)

@recetas.route('/recetas/new', methods=['GET', 'POST'])
@token_required
@allowed_roles(['admin','produccion','compras'])
def create():
    
    if request.method == 'POST':
        print(request.form)
        id = create_galleta(request.form)
        save_image(id, request.files['file'])
    if 'save' in request.form:
        id = create_galleta(request.form)
        save_image(id, request.files['file'])
        flash('Receta creada con éxito', 'success')
        return redirect(f"/recetas/{id}")
        
    
    return render_template('pages/recetas/create.html',receta="", ingredientes="", isEdit=True)

