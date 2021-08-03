class DashboardHistoricQuizResultsDto:

    def __init__(self) -> None:
        """
        Initialization with 0 Games for each Month
        """
        historic_init = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

        self.won = historic_init[:]
        self.lost = historic_init[:]

    def to_json(self) -> str:
        """
        Return Won / Lost as JSON
        """
        return {
            'won': self.won,
            'lost': self.lost
        }
