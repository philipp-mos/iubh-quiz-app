from typing import List

from src.services.SubjectService import SubjectService
from src.models.subject.Subject import Subject
from src.api.v1.dtos.SubjectDto import SubjectDto


def test_subjectservice_subjectlist_to_subjectdtolist_mapping():

    list_of_subjects = [
        Subject('Mathematik I'),
        Subject('Mathematik II'),
        Subject('Grundlagen der industriellen Softwaretechnik'),
        Subject('Financial Services Management')
    ]

    list_of_subjectdtos = [
        SubjectDto(None, 'Mathematik I'),
        SubjectDto(None, 'Mathematik II'),
        SubjectDto(None, 'Grundlagen der industriellen Softwaretechnik'),
        SubjectDto(None, 'Financial Services Management')
    ]

    result = SubjectService.subjectlist_to_subjectdtolist_mapping(list_of_subjects)

    assert is_equal_list_of_subjectdtos(list_of_subjectdtos, result)


def is_equal_list_of_subjectdtos(first_list: List[SubjectDto], second_list: List[SubjectDto]) -> bool:

    if len(first_list) != len(second_list):
        return False

    for i in range(0, len(first_list)):
        if first_list[i].name != second_list[i].name:
            return False

    return True
