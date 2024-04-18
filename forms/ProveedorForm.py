from wtforms import Form, StringField, IntegerField, TextAreaField, SelectField, DateTimeField, BooleanField, validators
from wtforms.validators import DataRequired


class ProveedorForm(Form):
    nombre_empresa = StringField(
        "Nombre de la empresa",
        [validators.DataRequired(
            message="El nombre de la empresa es obligatorio."),
         validators.Length(
            min=4,
            max=25,
            message="El nombre de la empresa debe tener entre 4 y 25 caracteres.",
        )],
        render_kw={
            "class": "input input-bordered input-primary w-full max-w-xs text-black"},
    )

    direccion_empresa = StringField(
        "Dirección de la empresa",
        [validators.DataRequired(
            message="La dirección de la empresa es obligatoria."),
         validators.Length(
            min=4,
            max=25,
            message="La dirección de la empresa debe tener entre 4 y 25 caracteres.",
        )],
        render_kw={
            "class": "input input-bordered input-primary w-full max-w-xs text-black"},
    )

    telefono_empresa = IntegerField(
        "Teléfono de la empresa",
        [validators.DataRequired(
            message="El teléfono de la empresa es obligatorio."),
         validators.Length(
            message="El teléfono de la empresa debe tener 10 digitos.",
            max=10
        )],
        render_kw={
            "class": "input input-bordered input-primary w-full max-w-xs text-black"},
    )

    nombre_encargado = StringField(
        "Nombre de la persona de atención",
        [validators.DataRequired(
            message="El nombre de la persona de atención es obligatorio."),
         validators.Length(
            min=4,
            max=25,
            message="El nombre de la persona de atención debe tener entre 4 y 25 caracteres.",
        )],
        render_kw={
            "class": "input input-bordered input-primary w-full max-w-xs text-black"},
    )

    estatus = BooleanField("Estatus")

    created_at = DateTimeField("Fecha de creación")
    updated_at = DateTimeField("Fecha de actualización")
    deleted_at = DateTimeField("Fecha de eliminación")

    id_usuario = IntegerField("Id de usuario", render_kw={"class": "hidden"})


class ProveedorEditForm(Form):
    id = IntegerField("id")

    nombre_empresa_edit = StringField("Nombre de la empresa", render_kw={
                                      "class": "input input-bordered input-primary w-full max-w-xs text-black"})

    direccion_empresa_edit = StringField("Dirección de la empresa", render_kw={
                                         "class": "input input-bordered input-primary w-full max-w-xs text-black"})

    telefono_empresa_edit = StringField("Teléfono de la empresa", render_kw={
                                        "class": "input input-bordered input-primary w-full max-w-xs text-black"})

    nombre_encargado_edit = StringField("Nombre del encargado", render_kw={
                                        "class": "input input-bordered input-primary w-full max-w-xs text-black"})

    estatus = BooleanField("estatus")

    created_at = DateTimeField("created_at")

    updated_at = DateTimeField("updated_at")

    deleted_at = DateTimeField("deleted_at")

    id_usuario = IntegerField("id_usuario")


class ProveedorDelForm(Form):
    id = IntegerField("id")

    nombre_empresa_del = StringField("Nombre de la empresa", render_kw={
                                     "class": "input input-bordered input-primary w-full max-w-xs text-black", "readonly": "readonly"})

    direccion_empresa_del = StringField("Dirección de la empresa", render_kw={
                                        "class": "input input-bordered input-primary w-full max-w-xs text-black", "readonly": "readonly"})

    telefono_empresa_del = StringField("Teléfono de la empresa", render_kw={
                                       "class": "input input-bordered input-primary w-full max-w-xs text-black", "readonly": "readonly"})

    nombre_encargado_del = StringField("Nombre del encargad", render_kw={
                                       "class": "input input-bordered input-primary w-full max-w-xs text-black", "readonly": "readonly"})

    estatus = BooleanField("estatus")

    created_at = DateTimeField("created_at")

    updated_at = DateTimeField("updated_at")

    deleted_at = DateTimeField("deleted_at")

    id_usuario = IntegerField("id_usuario")
