# Using turtle graphics to draw a dart board.
# A sample solution to the Alternate Assignment 2 of CISC101.
# by Alan McLeod

from turtle import *

def main() :
    # Set appearance and speed of turtle
    shape("turtle")
    speed(10)

    # Draw slices
    # Draw largest slice layer first and then move inwards
    penup()
    fillcolor("yellow")
    sliceLayer = 0
    sliceSizes = [300, 280, 150, 130] # pixels
    while sliceLayer < 4 :
        # Assign slice radius
        radius = sliceSizes[sliceLayer]
        # Position turtle to start the next slice layer
        home()
        right(90)
        forward(radius)
        left(90)
        circle(radius, 27)
        sliceCount = 0
        # Draw all slices in layer
        # One slice is 18 degrees of arc
        while sliceCount < 20 :
            if fillcolor() == "black" :
                fillcolor("yellow")
            else :
                fillcolor("black")
            begin_fill()
            circle(radius, 18)
            left(90)
            forward(radius)
            left(162)   # 180 - 18 degrees
            forward(radius)
            end_fill()
            left(90)
            circle(radius, 18)
            sliceCount = sliceCount + 1
        sliceLayer = sliceLayer + 1
        # Change color so next layer is in opposite colour order
        if fillcolor() == "black" :
            fillcolor("yellow")
        else :
            fillcolor("black")

    # Draw centre circles
    # Black one
    home()
    forward(25)
    left(90)
    fillcolor("black")
    begin_fill()
    circle(25)
    end_fill()
    left(90)
    forward(10)
    # Red one
    right(90)
    fillcolor("red")
    begin_fill()
    circle(15)
    end_fill()
    home()
    # dump = input("Press enter to close.") # Un-comment this line if you run
                                            # the program from the DOS window.
    
main()    
        
