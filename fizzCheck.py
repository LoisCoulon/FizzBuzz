class fizzChecker:
    
    @staticmethod
    def isCorrect(x):
        if x <= 0:
            raise(ArgumentError())
        return False

class ArgumentError(Exception):
    def __init__(self):
        super()