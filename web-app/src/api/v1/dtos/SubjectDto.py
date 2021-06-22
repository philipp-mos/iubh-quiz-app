class SubjectDto:

    def __init__(self, id, name) -> None:
        self.id = id
        self.name = name

    def json(self):
        """
        Return SubjectDto in JSON
        """
        return {'id': self.id, 'name': self.name}
