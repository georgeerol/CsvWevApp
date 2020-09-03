class PeopleInYear:

    def __init__(self, year, person):
        self.year = year
        self.person = person

    def json(self):
        return {'year': self.year, 'person': self.person}
