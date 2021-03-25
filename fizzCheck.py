class fizzChecker:
    
    @staticmethod
    def isCorrect(x):
        if x <= 0:
            raise(ArgumentError())
            return False

        elif (x%3) == 0 and (x%5 != 0):
            return True

        elif (x%5) == 0 and (x%3 != 0):
            return True

        elif (x%3 == 0) and (x%5 == 0):
            return True
        else:
            return False
            
            

class ArgumentError(Exception):
    def __init__(self):
        super()