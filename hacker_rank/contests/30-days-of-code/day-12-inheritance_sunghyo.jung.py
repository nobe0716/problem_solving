class Grade(Student):
    def __init__(self,firstName,lastName,phone,score):
        self.firstName=firstName
        self.lastName=lastName
        self.phone=phone
        self.score=score

    def calculate(self):
        return 'D' if score < 40 else 'B' if score < 60 else 'A' if score < 75 else 'E' if score < 90 else 'O'
        