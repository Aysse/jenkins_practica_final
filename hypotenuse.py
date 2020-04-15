import math
import incompleteTriangle
class Hypotenuse:
    def __init__(self, incompleteTriangle):
        powCatA = pow(int(incompleteTriangle.catA), 2)
        powCatB = pow(int(incompleteTriangle.catB), 2)
        sumCat = powCatA + powCatB
        self.hypotenuse = math.sqrt(sumCat)

