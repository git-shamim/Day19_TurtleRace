
from turtle import Turtle, Screen
from random import randint

screen = Screen()
screen.setup(width=500, height=400)

colors = ['red', 'blue', 'violet', 'yellow', 'green', 'brown']
y_position = [100, 60, 20, -20, -60, -100]

turtles = []
for i in range(0, 6):
    t = Turtle(shape='turtle')
    t.color(colors[i])
    t.penup()
    t.goto(x=-230, y=y_position[i])
    turtles.append(t)

user_bet = screen.textinput(title="Make your best", prompt="Which turtle will win? Enter a color: \n "
                                                           "('red' 'blue' 'violet' 'yellow' 'green' 'brown')")

is_game_on = False

if user_bet:
    is_game_on = True

while is_game_on:
    for turtle in turtles:

        if turtle.xcor() <= 230:
            turtle.forward(randint(0, 10))

        else:
            is_game_on = False
            winning_turtle_color = turtle.pencolor()

            if winning_turtle_color == user_bet:
                print("You have won. The {} color turtle is the winner".format(winning_turtle_color))
            else:
                print("You have lost. The {} color turtle is the winner".format(winning_turtle_color))


screen.exitonclick()
