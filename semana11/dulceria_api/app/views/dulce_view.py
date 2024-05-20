def render_dulce_list(dulces):
    # Representa una lista de dulcees como una lista de diccionarios
    return [
        {
            "id": dulce.id,
            "titulo": dulce.marca,
            "autor": dulce.peso,
            "edicion": dulce.sabor,
            "disponibilidad":dulce.origen
        }
        for dulce in dulces
    ]


def render_dulce_detail(dulce):
    # Representa los detalles de un dulce como un diccionario
    return {
            "id": dulce.id,
            "titulo": dulce.marca,
            "autor": dulce.peso,
            "edicion": dulce.sabor,
            "disponibilidad":dulce.origen
    }
