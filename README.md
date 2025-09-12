# VisualProgramming
Instructions on setting up environment

1.) Install and Open Visual Studio Code  \
2.) Open a Terminal and run: `pip install processing-py`: https://pypi.org/project/processing-py/  \
3.) Create a new python file and paste this code: 

#! test_processing.py

from processing_py import * 

app = App(600,400) # create window: width, height \
app.background(0,0,0) # set background:  red, green, blue  \
app.fill(255,255,0) # set color for objects: red, green, blue  \
app.rect(100,100,200,100) # draw a rectangle: x0, y0, size_x, size_y  \
app.fill(0,0,255) # set color for objects: red, green, blue  \
app.ellipse(300,200,50,50) # draw a circle: center_x, center_y, size_x, size_y  \
app.redraw() # refresh the window  \

4.) Run and execute within the terminal: `python test_processing.py`. It will also download and install any java dependencies.  \
5.) Enjoy coding with art!

