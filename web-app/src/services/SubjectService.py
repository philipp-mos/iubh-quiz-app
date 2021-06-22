from typing import List

from .abstracts.AbcSubjectService import AbcSubjectService

from ..models.Subject import Subject
from ..api.v1.dtos.SubjectDto import SubjectDto
from ..modules.subjects.viewmodels.SubjectOverviewViewModel import SubjectOverviewViewModel


class SubjectService(AbcSubjectService):

    @staticmethod
    def subjectlist_to_subjectdtolist_mapping(list_of_subjects: List[Subject]) -> List[SubjectDto]:
        """
        Mapps all Subjects in List to SubjectDto
        """
        subject_dto_list: List[SubjectDto] = []

        for subject in list_of_subjects:
            subject_dto_list.append(
                SubjectDto(subject.id, subject.name)
            )

        return subject_dto_list

    @staticmethod
    def subjectlist_to_subjectoverviewviewmodellist_mapping(list_of_subjects: List[Subject]) -> List[SubjectOverviewViewModel]:
        """
        Mapps all Subjects in List to SubjectOverviewViewModel
        """
        subjectviewmodel_list: List[SubjectOverviewViewModel] = []

        for subject in list_of_subjects:
            subjectviewmodel_list.append(
                SubjectOverviewViewModel(
                    subject.name,
                    subject.short,
                    subject.image_path
                )
            )

        return subjectviewmodel_list
