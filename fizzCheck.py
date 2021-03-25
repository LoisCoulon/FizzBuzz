class fizzChecker:
    
    @staticmethod
    def isCorrect(x):
        if x <= 0:
            raise(ArgumentError())
        return False

        if (x%3) == 0 and (x%5 != 0):
            return True

        if (x%5) == 0 and (x%3 != 0):
            return True

        if (x%3 == 0) and (x%5 == 0):
            return True
            
            

class ArgumentError(Exception):
    def __init__(self):
        super()