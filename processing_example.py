from processing_py import *
from random import randint

def setup():
    app = App(980, 980) # create window: width, height
    app.background(100)
    width = 980
    num = 5
    app.stroke(0, 0, 255)    # blue outline
    app.strokeWeight(4)      # outline thickness

    w = width / num
    for y_j in range(num):
        for x_i in range(num):
            app.rect(x_i * w, y_j * w, w, w, 20) # rounded corners
            r = randint(0, 255)
            g = randint(0, 255)
            b = randint(0, 255)
            app.fill(r, g, b)
            app.ellipse(x_i * w + w / 2, y_j * w + w / 2, w / 2, w /2)
    app.redraw()

if '__main__' == __name__:
    setup()
