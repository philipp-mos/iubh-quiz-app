import enum


class QuizGameStatus(enum.Enum):
    IN_PROGRESS = 1,
    FINISHED = 2,
    OPPONENT_IN_PROGRESS = 3,
    CLOSED = 4
