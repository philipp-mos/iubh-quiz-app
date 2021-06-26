from abc import ABC, abstractmethod
from typing import List

from ...models.subject.Subject import Subject
from ...api.v1.dtos.SubjectDto import SubjectDto
from ...modules.subjects.viewmodels.SubjectOverviewViewModel import SubjectOverviewViewModel


class AbcSubjectService(ABC):

    @abstractmethod
    def subjectlist_to_subjectdtolist_mapping(list_of_subjects: List[Subject]) -> List[SubjectDto]:
        raise NotImplementedError

    @abstractmethod
    def subjectlist_to_subjectoverviewviewmodellist_mapping(list_of_subjects: List[Subject]) -> List[SubjectOverviewViewModel]:
        raise NotImplementedError
