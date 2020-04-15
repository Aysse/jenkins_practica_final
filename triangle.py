import incompleteTriangle
import hypotenuse

def getTriangle(a, b):
    # Testing Jenkins 3
    initTriangle = incompleteTriangle.Incompletetriangle(a, b)
    hypo = hypotenuse.Hypotenuse(initTriangle)
    return round(hypo.hypotenuse)

