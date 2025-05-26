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
            try:
                degrees = float(line.split("de")[1].split("degrees")[0].strip())
                heading = (heading + degrees) % 360
            except:
                pass
        elif "Tourne droite de" in line:
            try:
                degrees = float(line.split("de")[1].split("degrees")[0].strip())
                heading = (heading - degrees) % 360
            except:
                pass
        elif "Avance" in line:
            try:
                spaces = float(line.split("Avance")[1].split("spaces")[0].strip())
                # Convert heading to radians and calculate new position
                rad = math.radians(heading)
                x += spaces * math.cos(rad)
                y += spaces * math.sin(rad)
                path.append((x, y))
            except:
                pass
        elif "Recule" in line:
            try:
                spaces = float(line.split("Recule")[1].split("spaces")[0].strip())
                # Convert heading to radians and calculate new position
                rad = math.radians(heading)
                x -= spaces * math.cos(rad)
                y -= spaces * math.sin(rad)
                path.append((x, y))
            except:
                pass

# Calculate bounds
xs, ys = zip(*path)
min_x, max_x = min(xs), max(xs)
min_y, max_y = min(ys), max(ys)
width = max_x - min_x + 20
height = max_y - min_y + 20

# Normalize coordinates
normalized_path = [(x - min_x + 10, height - (y - min_y + 10)) for x, y in path]

# Create SVG
svg = f'<svg width="{width}" height="{height}" xmlns="http://www.w3.org/2000/svg">\n'
svg += '  <path d="M'

for i, (x, y) in enumerate(normalized_path):
    if i == 0:
        svg += f"{x},{y} "
    else:
        svg += f"L{x},{y} "

svg += '" stroke="blue" fill="none" />\n'
svg += '</svg>'

# Write SVG to file
with open('turtle_path.svg', 'w') as f:
    f.write(svg)

print(f"SVG file created: turtle_path.svg")
print(f"Width: {width}, Height: {height}")
