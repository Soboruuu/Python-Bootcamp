import turtle
import pandas

score = 0
canvas = turtle.Screen()
canvas.title("U.S. States Game")
image = "blank_states_img.gif"
canvas.addshape(image)
turtle.shape(image)
timmy = turtle.Turtle()
timmy.hideturtle()

def write_state_name(state_name, x_cor, y_cor):
    timmy.speed("fastest")
    timmy.penup()
    timmy.goto(x_cor, y_cor)
    timmy.write(arg=state_name, align="center", font=("arial", 10, "normal"))

dt = pandas.read_csv("50_states.csv")
states_guessed = []

while score < 50:
    answer_state = canvas.textinput(title=f"Score:{score}/50 Guess the State",
                                    prompt="What's another state's name?")
    if answer_state == "exit":
        states_not_guessed = [state for state in dt.state if state not in states_guessed]
        tostudy = pandas.Series(states_not_guessed)
        tostudy.to_csv("states_to_learn.csv")
        break

    for state_name in dt.state:
        if answer_state == state_name:
            states_guessed.append(answer_state)
            state_row = dt[dt.state == answer_state]
            x_cor = int(state_row.x)
            y_cor = int(state_row.y)
            write_state_name(state_name, x_cor,y_cor)
            score +=1

canvas.exitonclick()