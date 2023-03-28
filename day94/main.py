import turtle
import xwing
from invaders import Invaders

# Create a Screen object and set its properties
screen = turtle.Screen()
screen.setup(width=800, height=600)
screen.title("Space Invader")
screen.tracer(0)

# Add Background image and deploy it on screen.
screen.addshape('assets/background-black.gif')
screen.bgpic('assets/background-black.gif')

# Create an instance of the Xwing class and add event listeners for the arrow keys and space bar
x_wing = xwing.Xwing((0, -250))
screen.onkeypress(x_wing.go_left, "Left")
screen.onkeypress(x_wing.go_right, "Right")

# Create an empty list to hold the missiles.
missiles=[]

# Bound space key to fire missile. hold every missiles in list.
screen.onkeypress(lambda: missiles.append(x_wing.fire()), "space")

# Create an empty list to hold invaders.
invaders = []

# Start the game when the Enter key is pressed
turtle.pencolor('white')
turtle.hideturtle()
start = turtle.write('Press Enter to Start Game', False, 'center', font=('arial', 24, 'normal'))
game_started = False


# Start the game when the Enter key is pressed
def start_game():
    global game_started
    game_started = True
    turtle.clear()
    # Create Invaders
    global invaders
    y = 120
    for i in range(3):
        positions = [(x, y) for x in range(-320, 321, 80)]
        y += 60
        for position in positions:
            invader = Invaders(position)
            invaders.append(invader)


screen.onkeypress(start_game, "Return")

# Start listening for keyboard events
screen.listen()


# Game play main flow
def play_game():
    # Update the screen and move the X-wing if the game has started
    screen.update()
    if game_started:
        # Move the missiles
        for missile in missiles:
            if missile.ycor() > 300:
                missiles.remove(missile)
                missile.hideturtle()
            else:
                for invader in invaders:
                    if missile.distance(invader) < 20 and missile.collide_rect(invader):
                        missiles.remove(missile)
                        # invader.explode()
                        invaders.remove(invader)
                        invader.hideturtle()
                        missile.hideturtle()
                        break
        # Check if all invaders have been destroyed
        if not invaders:
            turtle.write("You win!", align="center", font=("Arial", 24, "normal"))
            return

    # Call invade() method at a fixed interval of time
    turtle.ontimer(invaders_invade, 50)

    # Call the play_game() function again
    turtle.ontimer(play_game, 10)


def invaders_invade():
    for invader in invaders:
        invader.invade()


# Call play_game() function to start the game
play_game()

# Start main loop
turtle.mainloop()

