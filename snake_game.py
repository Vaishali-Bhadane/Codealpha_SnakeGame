import turtle
import time
import random

# Set up the screen
wn = turtle.Screen()
wn.title("Snake Game")
wn.bgcolor("white")
wn.setup(width=600, height=600)
wn.tracer(0)

# Score
score = 0

# Score display
score_display = turtle.Turtle()
score_display.speed(0)
score_display.color("black")
score_display.penup()
score_display.hideturtle()
score_display.goto(0, 260)
score_display.write("Score: {}".format(score), align="center", font=("Courier", 24, "normal"))

# Snake head
head = turtle.Turtle()
head.speed(0.1)  # Reduced snake speed
head.shape("square")
head.color("green")
head.penup()
head.goto(0, 0)
head.direction = "stop"  # Use lowercase "stop"

# Snake food
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0, 100)

# Snake body
segments = []

# Functions
def go_up():
    if head.direction != "down":
        head.direction = "up"

def go_down():
    if head.direction != "up":
        head.direction = "down"

def go_left():
    if head.direction != "right":
        head.direction = "left"

def go_right():
    if head.direction != "left":
        head.direction = "right"

def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)

    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)

    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)

    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)

# Generate food
def generate_food():
    x = random.randint(-280, 280)
    y = random.randint(-280, 280)
    food.goto(x, y)

# Keyboard bindings
wn.listen()
wn.onkeypress(go_up, "Up")
wn.onkeypress(go_down, "Down")
wn.onkeypress(go_left, "Left")
wn.onkeypress(go_right, "Right")

# Main game loop
while True:
    wn.update()

    # Check for collision with food
    if head.distance(food) < 20:
        x = random.randint(-280, 280)
        y = random.randint(-280, 280)
        food.goto(x, y)

        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("green")
        new_segment.penup()
        segments.append(new_segment)

        # Update score
        score += 10
        score_display.clear()
        score_display.write("Score: {}".format(score), align="center", font=("Courier", 24, "normal"))

    # Move the segments in reverse order
    for i in range(len(segments) - 1, 0, -1):
        x = segments[i - 1].xcor()
        y = segments[i - 1].ycor()
        segments[i].goto(x, y)

    # Move the first segment to where the head is
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)

    move()

    # Check for collision with the wall
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        time.sleep(1)
        head.goto(0, 0)
        head.direction = "stop"  # Use lowercase "stop"

        # Hide the segments
        for segment in segments:
            segment.goto(1000, 1000)

        # Clear the segments list
        segments.clear()

        # Game over message
        game_over_message = turtle.Turtle()
        game_over_message.speed(0)
        game_over_message.color("black")
        game_over_message.penup()
        game_over_message.hideturtle()
        game_over_message.goto(0, 0)
        game_over_message.write("Game Over", align="center", font=("Courier", 36, "normal"))

        # Wait for a moment
        time.sleep(2)

        # Clear the "Game Over" message
        game_over_message.clear()

        # Reset score
        score = 0
        score_display.clear()
        score_display.write("Score: {}".format(score), align="center", font=("Courier", 24, "normal"))

    # Check for collision with the body
    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "stop"  # Use lowercase "stop"

            # Hide the segments
            for segment in segments:
                segment.goto(1000, 1000)

            # Clear the segments list
            segments.clear()

            # Game over message
            game_over_message = turtle.Turtle()
            game_over_message.speed(0)
            game_over_message.color("black")
            game_over_message.penup()
            game_over_message.hideturtle()
            game_over_message.goto(0, 0)
            game_over_message.write("Game Over", align="center", font=("Courier", 36, "normal"))

            # Wait for a moment
            time.sleep(2)

            # Clear the "Game Over" message
            game_over_message.clear()

            # Reset score
            score = 0
            score_display.clear()
            score_display.write("Score: {}".format(score), align="center", font=("Courier", 24, "normal"))

    time.sleep(0.1)  # Reduced snake speed
