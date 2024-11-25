from flask import Blueprint, jsonify

animals_bp = Blueprint('animals', __name__)

from Models.animal import Gato, Perro, Huron, BoaConstrictor

@animals_bp.route('/animal/<nombre>', methods=['GET'])
def obtener_sonido(nombre):
    animales = {
        "gato": Gato(),
        "perro": Perro(),
        "huron": Huron(),
        "boa constrictor": BoaConstrictor()
    }

    animal = animales.get(nombre.lower())
    if not animal:
        return jsonify({"error": "Animal no encontrado"}), 404

    return jsonify({"nombre": animal.nombre, "sonido": animal.hacer_sonido()})