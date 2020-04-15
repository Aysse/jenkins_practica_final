import incompleteTriangle
import hypotenuse

def getTriangle(a, b):
    initTriangle = incompleteTriangle.Incompletetriangle(a, b)
    hypo = hypotenuse.Hypotenuse(initTriangle)
    return round(hypo.hypotenuse)

