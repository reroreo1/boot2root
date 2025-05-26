import turtle

# Set up the turtle
t = turtle.Turtle()
t.speed(0)  # Fastest speed
screen = turtle.Screen()
screen.title("Turtle Visualization")

# Function to process commands
def process_command(line):
    line = line.strip()
    if not line or "Can you digest" in line:
        return
    
    if "Tourne gauche de" in line:
        try:
            degrees = float(line.split("de")[1].split("degrees")[0].strip())
            t.left(degrees)
        except:
            pass
    elif "Tourne droite de" in line:
        try:
            degrees = float(line.split("de")[1].split("degrees")[0].strip())
            t.right(degrees)
        except:
            pass
    elif "Avance" in line:
        try:
            spaces = float(line.split("Avance")[1].split("spaces")[0].strip())
            t.forward(spaces)
        except:
            pass
    elif "Recule" in line:
        try:
            spaces = float(line.split("Recule")[1].split("spaces")[0].strip())
            t.backward(spaces)
        except:
            pass

# Read the file and process each line
with open('turtle', 'r') as file:
    for line in file:
        process_command(line)

# Keep the window open
turtle.mainloop()
