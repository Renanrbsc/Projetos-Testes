from Interface_Terminal.Controller_Terminal.base_controller import BaseController
from Interface_Terminal.Dao_Terminal.pokemon_dao import PokemonDao


class PokemonController(BaseController):

    def __init__(self):
        super().__init__(PokemonDao())

    def get_all(self):
        return super().get()

    def get_by_id(self, id):
        return super().get(id)

    def get_image(self):
        return super().get_image()

    def post(self, Pokemon):
        return super().post(Pokemon)

    def put(self, id, Pokemon):
        return super().put(id, Pokemon)

    def delete(self, id):
        return super().delete(id)

