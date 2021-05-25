from .abstracts.AbcRepository import AbcRepository

# TODO: Switch to usage of Generics
class Repository(AbcRepository):

    def get_all():
        return NotImplementedError

    def find_by_id(id):
        return NotImplementedError