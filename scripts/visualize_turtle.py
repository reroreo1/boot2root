import matplotlib.pyplot as plt
import math

# Initialize position and heading
x, y = 0, 0
heading = 0  # in degrees, 0 is east
path = [(x, y)]

# Process the turtle file
with open('turtle', 'r') as file:
    for line in file:
        line = line.strip()
        if not line or "Can you digest" in line:
            continue
        
        if "Tourne gauche de" in line:
            degrees = float(line.split("de")[1].split("degrees")[0].strip())
            heading = (heading + degrees) % 360
        elif "Tourne droite de" in line:
            degrees = float(line.split("de")[1].split("degrees")[0].strip())
            heading = (heading - degrees) % 360
        elif "Avance" in line:
            spaces = float(line.split("Avance")[1].split("spaces")[0].strip())
            # Convert heading to radians and calculate new position
            rad = math.radians(heading)
            x += spaces * math.cos(rad)
            y += spaces * math.sin(rad)
            path.append((x, y))
        elif "Recule" in line:
            spaces = float(line.split("Recule")[1].split("spaces")[0].strip())
            # Convert heading to radians and calculate new position
            rad = math.radians(heading)
            x -= spaces * math.cos(rad)
            y -= spaces * math.sin(rad)
            path.append((x, y))

# Plot the path
xs, ys = zip(*path)
plt.figure(figsize=(10, 10))
plt.plot(xs, ys, 'b-')
plt.axis('equal')
plt.grid(True)
plt.title('Turtle Path Visualization')
plt.savefig('turtle_path.png')
plt.show()
