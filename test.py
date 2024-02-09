import turtle




def main():
    input("input the color of the Square")

    MakeBigSquare()
    SquareMakerFunction(50,100)
    SquareMakerFunction(60,20)
    SquareMakerFunction(130,0)





    input("STOPS HERE")



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
    




def SquareMakerFunction(postionX,postionY):

    #the following code will create Squares in 3 spots
    x=70 
    y=70
    turtle.fillcolor("yellow")
    
    Side_of_square= 50
    turtle.up()
    turtle.goto(postionX,postionY)



    turtle.down()
    turtle.begin_fill()
    turtle .forward(Side_of_square)
    turtle.left(90)
    turtle.forward(Side_of_square)
    turtle.left(90)
    turtle.forward(Side_of_square)
    turtle.left(90)
    turtle.forward(Side_of_square)
    turtle.end_fill()

    endPointOf1stSquarepostionXCoordinate= turtle.xcor()
    EndpointOf1stSquareyCoordinate= turtle.ycor()
    print(endPointOf1stSquarepostionXCoordinate)
    print(EndpointOf1stSquareyCoordinate)




    #this finishes 1 Square
'''
def SquareAttempt(x):
    
    turtle.goto(0,0)
    x=50   
    y=50
    turtle.forward(x+200)
'''





main()





