from flask import Blueprint, request, render_template
from models.Recetas import MateriaPrima,RecetasGalletas
recetas = Blueprint('recetas', __name__, template_folder='templates')


def get_Recetas():
    #obtener todas las recetas haciendo un distinct del nombre de la receta
    recetas = RecetasGalletas.query.with_entities(RecetasGalletas.nombre_receta).distinct().all()
    return recetas


@recetas.route('/recetas')
def index():
    recetas = get_Recetas()
    print(recetas)
    return render_template('pages/recetas/index.html', recetas=recetas)