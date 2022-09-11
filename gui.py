from tkinter import *
import Color
(couleur)=['red','blue','yellow','white','orange','green']

Color.RED ='red'
Color.ORANGE='orange'
Color.WHITE='white'
Color.GREEN='green'
Color.YELLOW='yellow'
Color.BLUE='blue'
 
CC=[] 

a = 800
b = 1100
i = int(a/12)
j = int(a/12)

fenetre = Tk()
fenetre.geometry(str(b)+"x"+str(a))
fond = Canvas(fenetre, width=b , heigh=a ,bg='#E4E4E4')
fond.pack(side=LEFT)

def CubeResolue() :
    global cr,red,orange,white,green,yellow,blue,CC
    cr=[[[Color.RED ,Color.RED ,Color.RED ],[Color.RED ,Color.RED ,Color.RED ],[Color.RED ,Color.RED ,Color.RED ]],
        [[Color.GREEN,Color.GREEN,Color.GREEN],[Color.GREEN,Color.GREEN,Color.GREEN],[Color.GREEN,Color.GREEN,Color.GREEN]],
        [[Color.YELLOW,Color.YELLOW,Color.YELLOW],[Color.YELLOW,Color.YELLOW,Color.YELLOW],[Color.YELLOW,Color.YELLOW,Color.YELLOW]],
        [[Color.BLUE,Color.BLUE,Color.BLUE],[Color.BLUE,Color.BLUE,Color.BLUE],[Color.BLUE,Color.BLUE,Color.BLUE]],
        [[Color.WHITE,Color.WHITE,Color.WHITE],[Color.WHITE,Color.WHITE,Color.WHITE],[Color.WHITE,Color.WHITE,Color.WHITE]],
        [[Color.ORANGE,Color.ORANGE,Color.ORANGE],[Color.ORANGE,Color.ORANGE,Color.ORANGE],[Color.ORANGE,Color.ORANGE,Color.ORANGE]]]
    CC=cr

CubeResolue ()

def AfficheGraphique ():
    global a,b
# F
    F4C1=fond.create_rectangle(4*i , 4*j , 5*i , 5*j ,  outline='black' , fill=CC [0] [0] [0])
    F4C2=fond.create_rectangle(5*i , 4*j , 6*i , 5*j ,  outline='black' , fill=CC [0] [0] [1])
    F4C3=fond.create_rectangle(6*i , 4*j , 7*i , 5*j ,  outline='black' , fill=CC [0] [0] [2])
    F4C4=fond.create_rectangle(4*i , 5*j , 5*i , 6*j ,  outline='black' , fill=CC [0] [1] [0])
    F4C5=fond.create_rectangle(5*i , 5*j , 6*i , 6*j ,  outline='black' , fill=CC [0] [1] [1])
    F4C6=fond.create_rectangle(6*i , 5*j , 7*i , 6*j ,  outline='black' , fill=CC [0] [1] [2])
    F4C7=fond.create_rectangle(4*i , 6*j , 5*i , 7*j ,  outline='black' , fill=CC [0] [2] [0])
    F4C8=fond.create_rectangle(5*i , 6*j , 6*i , 7*j ,  outline='black' , fill=CC [0] [2] [1])
    F4C9=fond.create_rectangle(6*i , 6*j , 7*i , 7*j ,  outline='black' , fill=CC [0] [2] [2])

# U
    F1C1=fond.create_rectangle(4*i , 1*j-10 , 5*i , 2*j-10 ,  outline='black' , fill=CC [1] [0] [0])
    F1C2=fond.create_rectangle(5*i , 1*j-10 , 6*i , 2*j-10 ,  outline='black' , fill=CC [1] [0] [1])
    F1C3=fond.create_rectangle(6*i , 1*j-10 , 7*i , 2*j-10 ,  outline='black' , fill=CC [1] [0] [2])
    F1C4=fond.create_rectangle(4*i , 2*j-10 , 5*i , 3*j-10 ,  outline='black' , fill=CC [1] [1] [0])
    F1C5=fond.create_rectangle(5*i , 2*j-10 , 6*i , 3*j-10 ,  outline='black' , fill=CC [1] [1] [1])
    F1C6=fond.create_rectangle(6*i , 2*j-10 , 7*i , 3*j-10 ,  outline='black' , fill=CC [1] [1] [2])
    F1C7=fond.create_rectangle(4*i , 3*j-10 , 5*i , 4*j-10 ,  outline='black' , fill=CC [1] [2] [0])
    F1C8=fond.create_rectangle(5*i , 3*j-10 , 6*i , 4*j-10 ,  outline='black' , fill=CC [1] [2] [1])
    F1C9=fond.create_rectangle(6*i , 3*j-10 , 7*i , 4*j-10 ,  outline='black' , fill=CC [1] [2] [2])
# L

    F3C1=fond.create_rectangle(1*i-10 , 4*j , 2*i-10 , 5*j ,  outline='black' , fill=CC [2] [0] [0])
    F3C2=fond.create_rectangle(2*i-10 , 4*j , 3*i-10 , 5*j ,  outline='black' , fill=CC [2] [0] [1])
    F3C3=fond.create_rectangle(3*i-10 , 4*j , 4*i-10 , 5*j ,  outline='black' , fill=CC [2] [0] [2])
    F3C4=fond.create_rectangle(1*i-10 , 5*j , 2*i-10 , 6*j ,  outline='black' , fill=CC [2] [1] [0])
    F3C5=fond.create_rectangle(2*i-10 , 5*j , 3*i-10 , 6*j ,  outline='black' , fill=CC [2] [1] [1])
    F3C6=fond.create_rectangle(3*i-10 , 5*j , 4*i-10 , 6*j ,  outline='black' , fill=CC [2] [1] [2])
    F3C7=fond.create_rectangle(1*i-10 , 6*j , 2*i-10 , 7*j ,  outline='black' , fill=CC [2] [2] [0])
    F3C8=fond.create_rectangle(2*i-10 , 6*j , 3*i-10 , 7*j ,  outline='black' , fill=CC [2] [2] [1])
    F3C9=fond.create_rectangle(3*i-10 , 6*j , 4*i-10 , 7*j ,  outline='black' , fill=CC [2] [2] [2])

# D :

    F2C1=fond.create_rectangle(4*i , 7*j+10 , 5*i , 8*j+10  , outline='black' , fill=CC [3] [0] [0])
    F2C2=fond.create_rectangle(5*i , 7*j+10 , 6*i , 8*j+10  , outline='black' , fill=CC [3] [0] [1])
    F2C3=fond.create_rectangle(6*i , 7*j+10 , 7*i , 8*j+10  , outline='black' , fill=CC [3] [0] [2])
    F2C4=fond.create_rectangle(4*i , 8*j+10 , 5*i , 9*j+10  , outline='black' , fill=CC [3] [1] [0])
    F2C5=fond.create_rectangle(5*i , 8*j+10 , 6*i , 9*j+10  , outline='black' , fill=CC [3] [1] [1])
    F2C6=fond.create_rectangle(6*i , 8*j+10 , 7*i , 9*j+10  , outline='black' , fill=CC [3] [1] [2])
    F2C7=fond.create_rectangle(4*i , 9*j+10 , 5*i , 10*j+10 , outline='black' , fill=CC [3] [2] [0])
    F2C8=fond.create_rectangle(5*i , 9*j+10 , 6*i , 10*j+10 , outline='black' , fill=CC [3] [2] [1])
    F2C9=fond.create_rectangle(6*i , 9*j+10 , 7*i , 10*j+10 , outline='black' , fill=CC [3] [2] [2])

# R

    F5C1=fond.create_rectangle(7*i+10 , 4*j , 8*i+10 , 5*j  ,  outline='black' , fill=CC [4] [0] [0])
    F5C2=fond.create_rectangle(8*i+10 , 4*j , 9*i+10 , 5*j  ,  outline='black' , fill=CC [4] [0] [1])
    F5C3=fond.create_rectangle(9*i+10 , 4*j , 10*i+10 , 5*j ,  outline='black' , fill=CC [4] [0] [2])
    F5C4=fond.create_rectangle(7*i+10 , 5*j , 8*i+10 , 6*j  ,  outline='black' , fill=CC [4] [1] [0])
    F5C5=fond.create_rectangle(8*i+10 , 5*j , 9*i+10 , 6*j  ,  outline='black' , fill=CC [4] [1] [1])
    F5C6=fond.create_rectangle(9*i+10 , 5*j , 10*i+10 , 6*j ,  outline='black' , fill=CC [4] [1] [2])
    F5C7=fond.create_rectangle(7*i+10 , 6*j , 8*i+10 , 7*j  ,  outline='black' , fill=CC [4] [2] [0])
    F5C8=fond.create_rectangle(8*i+10 , 6*j , 9*i+10 , 7*j  ,  outline='black' , fill=CC [4] [2] [1])
    F5C9=fond.create_rectangle(9*i+10, 6*j , 10*i+10 , 7*j ,  outline='black' , fill=CC [4] [2] [2])
    
# B

    F6C1=fond.create_rectangle(10*i+20 , 4*j , 11*i+20 , 5*j ,outline='black' , fill=CC [5] [0] [0])
    F6C2=fond.create_rectangle(11*i+20 , 4*j , 12*i+20 , 5*j ,outline='black' , fill=CC [5] [0] [1])
    F6C3=fond.create_rectangle(12*i+20 , 4*j , 13*i+20 , 5*j ,outline='black' , fill=CC [5] [0] [2])
    F6C4=fond.create_rectangle(10*i+20 , 5*j , 11*i+20 , 6*j ,outline='black' , fill=CC [5] [1] [0])
    F6C5=fond.create_rectangle(11*i+20 , 5*j , 12*i+20 , 6*j ,outline='black' , fill=CC [5] [1] [1])
    F6C6=fond.create_rectangle(12*i+20 , 5*j , 13*i+20 , 6*j ,outline='black' , fill=CC [5] [1] [2])
    F6C7=fond.create_rectangle(10*i+20 , 6*j , 11*i+20 , 7*j ,outline='black' , fill=CC [5] [2] [0])
    F6C8=fond.create_rectangle(11*i+20 , 6*j , 12*i+20 , 7*j ,outline='black' , fill=CC [5] [2] [1])
    F6C9=fond.create_rectangle(12*i+20 , 6*j , 13*i+20 , 7*j ,outline='black' , fill=CC [5] [2] [2])

AfficheGraphique ()
fenetre.mainloop()
