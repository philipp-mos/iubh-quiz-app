from typing import List
from .TutorSuggestionAnswerViewModel import TutorSuggestionAnswerViewModel


class TutorSuggestionViewModel():

    id: int

    date: str

    question_text: str

    subject_name: str

    answer_viewmodels: List[TutorSuggestionAnswerViewModel]
