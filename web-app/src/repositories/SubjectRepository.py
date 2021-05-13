from .abstracts.AbcSubjectRepository import AbcSubjectRepository
from ..models.subject import Subject


class SubjectRepository(AbcSubjectRepository):

    def get_all():
        return Subject.query.all()

    def get_all_new():
        return Subject.query.get(1)