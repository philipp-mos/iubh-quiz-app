from .abstracts.AbcRepository import AbcRepository
from ..models.Subject import Subject

# TODO: Switch to usage of Generics
class Repository(AbcRepository):

    def get_all():
        return Subject.query.all()

    def find_by_id(id):
        return Subject.query.get(id)