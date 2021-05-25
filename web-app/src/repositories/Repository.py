from .abstracts.AbcRepository import AbcRepository

# TODO: Switch to usage of Generics
class Repository(AbcRepository):

    def get_all():
        raise NotImplementedError

    def find_by_id(id):
        raise NotImplementedError