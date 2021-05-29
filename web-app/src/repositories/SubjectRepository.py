from .abstracts.AbcSubjectRepository import AbcSubjectRepository
from .Repository import Repository
from ..models.Subject import Subject


class SubjectRepository(Repository, AbcSubjectRepository):

    def get_all():
        return Subject.query.all()

    def find_by_id(id):
        return Subject.query.get(id)