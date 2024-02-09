import turtle




def main():
    
    MakeBigSquare()

    TriangleMakerFunction()




    input("any text")

# this is for the square for all to be inside of 
def MakeBigSquare():
    
    turtle.right(90)
    turtle.up()
    turtle.right(90)
    #this is the begining of the rectangle
    turtle.fillcolor("light blue")
    turtle.begin_fill()
    turtle.forward(200)
    turtle.down()
    turtle.right(90)
    turtle.forward(200)
    turtle.right(90)
    turtle.forward(400)
    turtle.right(90)
    turtle.forward(400)
    turtle.right(90)
    turtle.forward(400)
    turtle.right(90)
    turtle.forward(200)
    turtle.end_fill()
    




def TriangleMakerFunction():
    #the following code will create Squares in 3 spots
    x=70 
    y=70
    
    Side_of_square= 50
    turtle.up()
    turtle.goto(x,y)
    turtle.down()
    turtle .forward(Side_of_square)
    turtle.left(90)
    turtle.forward(Side_of_square)
    turtle.left(90)
    turtle.forward(Side_of_square)
    turtle.left(90)
    turtle.forward(Side_of_square)

    endPointOf1stSquarepostionXCoordinate= turtle.xcor()
    EndpointOf1stSquareyCoordinate= turtle.ycor()
    print(endPointOf1stSquarepostionXCoordinate)
    print(EndpointOf1stSquareyCoordinate)

    


    #this finishes 1 Square

    




main()





