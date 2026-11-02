# Name: Qinyun Zhu
# Assignment One

# Part 1: Turtle Drawing
import turtle


screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Colourful Turtle Drawing")

t = turtle.Turtle()
t.speed(0)
t.pensize(2)

colors = ["red", "orange", "yellow", "green",
          "cyan", "blue", "purple", "pink"]

for i in range(72):

    t.pencolor(colors[i % 8])
    length = 50 + i * 2

    for j in range(4):
        t.forward(length)
        t.right(90)

    t.right(5)

t.hideturtle()



# Part 2: QA Bot

print("Question Answering Bot")

question = input("Ask me something: ").lower()

if "hku" in question:
    print("Bot: HKU stands for the University of Hong Kong.")

elif "robot" in question:
    print("Bot: A robot is a machine that can perform tasks.")

elif "jetson" in question:
    print("Bot: Jetson is an AI computing platform by NVIDIA.")

elif "ai" in question:
    print("Bot: AI means Artificial Intelligence.")

elif "human" in question:
    print("Bot: Humans are living beings with intelligence.")

else:
    print("Bot: Sorry, I don't understand.")
