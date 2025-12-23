# Pattern Match Estrutural
# Novidade do Python 3.10
# https://docs.python.org/3/tutorial/controlflow.html#match-statements
# https://docs.python.org/3/reference/compound_stmts.html#the-match-statement

from turtle import Turtle

turtle = Turtle()
turtle.shape("turtle")
turtle.speed(3)
turtle.color("blue", "yellow")

while True:

# icone de tartaruga no input
    command = input("🐢>").strip()
    if command == "exit":
        break
    if command == "draw":
        turtle.pendown()
        turtle.forward(20)