from .abstracts.AbcRepository import AbcRepository
from ..models.subject import Subject


class SubjectRepository(AbcRepository):

    def get_all():
        return Subject.query.all()