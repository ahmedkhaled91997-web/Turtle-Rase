from turtle import Turtle, Screen
import random

window=Screen()
window.title("turtle race")
window.setup(width=600, height=300)
turtle_colors=('red','blue','green')
turtle_setup=(90,0,-90)
window.bgpic("turtle_race_img.png")
turtle_list=[]

for i in range(3):
    new_turtle=Turtle('turtle')
    new_turtle.color(turtle_colors[i])
    new_turtle.penup()
    new_turtle.goto(-280,turtle_setup[i])
    turtle_list.append(new_turtle)
    new_turtle.pendown()

def race():
   game_on=True
   while game_on:
      for turtle in turtle_list:
         if turtle.xcor()>280:
            game_on=False
            winning_color=turtle.pencolor()
            return winning_color
         else:
            turtle.forward(random.randint(1,10))
while True:
   user_bet=window.textinput(title="make your bet", prompt="which turtle will win the race? (red/blue/green)or type 'exit' to quit: ").lower()
   if user_bet not in turtle_colors and user_bet!="exit":
      user_bet=window.textinput(title="invalid input", prompt="please enter a valid color (red/blue/green) or 'exit': ").lower()

   elif user_bet=="exit":
      window.bye()
   else:      
      break
   
def winner_turtle(winning_color):
   window.clearscreen()
   turtle_write=Turtle()
   turtle_write.hideturtle()
   turtle_write.pencolor(f'{winning_color}')
   window.bgcolor('lightblue')
   if user_bet==winning_color:  
      turtle_write.write(f"You won! The {winning_color} turtle is the winner!", align="center", font=("Arial", 25,"normal"))
   else:                
      turtle_write.write(f"You lost! The {winning_color} turtle is the winner!", align="center", font=("Arial", 25,"normal"))
winner_turtle(race())
window.exitonclick()
