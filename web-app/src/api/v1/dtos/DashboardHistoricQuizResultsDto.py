class DashboardHistoricQuizResultsDto:

    def __init__(self) -> None:
        """
        Initialization with 0 Games for each Month
        """
        self.won = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.lost = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    def to_json(self) -> str:
        """
        Return Won / Lost as JSON
        """
        counter: int = 0
        for lost_item in self.lost:
            self.lost[counter] = lost_item * -1
            counter += 1

        return {
            'won': self.won,
            'lost': self.lost
        }
