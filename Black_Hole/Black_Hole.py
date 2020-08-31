from tkinter import *

root = Tk()
# Width x Height
root.geometry("878x635")
# width,height
root.minsize(300,300)
root.maxsize(900, 900)

root.title("Black_Hole_Board_Game")
main_title = Label(text="Welcome to Black Hole",font= "Arial 14 bold",fg = "black")
main_title.pack()

def game_info():
   messagebox.showinfo("Game Rules", 
                         "1. The game will be started from the first tile in the grid i.e., start point and end at the end point.\n\
                        \n2. There will be a button by which the random will generate between 1 to 4.\n\
                        \n3. If the player the player gets on the black hole coordinate, he will lose and the game will be restarted.\n\
                        \n4. If the player successfully reached to the end point without getting caught in the black hole, he will win")
  
def leave():
    root.destroy()
    

                       
f1 = Frame(root, bg="silver", borderwidth=6, relief=GROOVE)
f1.pack(side=LEFT,anchor ="se" )

f2 = Frame(root,bg="silver", borderwidth= 5, relief = GROOVE)
f2.pack(side=RIGHT,anchor=CENTER)

f3 = Frame(root,bg="silver", borderwidth= 10, relief = GROOVE)
f3.pack(side= TOP)

l = Label(f1, text="MENU",font="Arial 14 bold")
l.pack(pady=30,padx=30)

b1 = Button(f1,fg="blue",text="Game Info",font="Arial 10 bold", command = game_info)
b1.pack(side = TOP)

b2 = Button(f1,fg="Green",text="Restart",font="Arial 10 bold")
b2.pack(side = TOP)

b3 = Button(f1,fg="red",text="Leave",font="Arial 10 bold", command = leave)
b3.pack(side = TOP)

b4 = Button(f2,fg="black",text="ROLL",font="Arial 20 bold")
b4.pack(side = TOP,pady=15,padx=15)
    
                                     
   
main_frame = Canvas(root, width=600, height=600, background= "white")                
main_frame.pack(fill = BOTH)

main_frame.create_rectangle(5,4,600,600,fill = "white",width = 4)                       
                                                                                 
 
root.mainloop()

