from typing import List

from .abstracts.AbcSubjectService import AbcSubjectService

from ..api.v1.dtos.SubjectDto import SubjectDto

class SubjectService(AbcSubjectService):

    @staticmethod    
    def subjectlist_to_subjectdtolist_mapping(list_of_subjects) -> List[SubjectDto]:
        """
        Mapps all Subjects in List to SubjectDto
        """
        subject_dto_list = []

        for subject in list_of_subjects:
            subject_dto_list.append(
                SubjectDto(subject.id, subject.name)
            )

        return subject_dto_list
