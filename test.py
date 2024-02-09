import turtle




def main():
    print("hello world")
    MakeBigSquare()

    #TriangleMakerFunction()




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
    turtle.up()
    turtle.forward(200)
    turtle.left(90)
    turtle.forward(100)



main()





