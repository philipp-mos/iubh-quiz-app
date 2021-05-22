class SubjectDto:

    def __init__(self, id, name) -> None:
        self.id = id
        self.name = name


    def json(self):
        return {'id': self.id, 'name': self.name}
