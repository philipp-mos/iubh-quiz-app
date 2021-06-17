from abc import ABC, abstractmethod
from typing import List

from ...api.v1.dtos.SubjectDto import SubjectDto

class AbcSubjectService(ABC):

    @abstractmethod
    def subjectlist_to_subjectdtolist_mapping(list_of_subjects) -> List[SubjectDto]:
        raise NotImplementedError