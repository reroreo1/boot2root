#!/usr/bin/env python3

# This script extracts larger movements from the turtle file
# to see if there's a pattern

with open('turtle', 'r') as file:
    lines = file.readlines()

# Extract commands with larger values
large_movements = []
for line in lines:
    line = line.strip()
    if not line or "Can you digest" in line:
        continue
    
    if "Avance" in line and "spaces" in line:
        try:
            spaces = int(line.split("Avance")[1].split("spaces")[0].strip())
            if spaces > 1:
                large_movements.append(f"F{spaces}")
        except:
            pass
    elif "Recule" in line and "spaces" in line:
        try:
            spaces = int(line.split("Recule")[1].split("spaces")[0].strip())
            if spaces > 1:
                large_movements.append(f"B{spaces}")
        except:
            pass
    elif "Tourne gauche de" in line and "degrees" in line:
        try:
            degrees = int(line.split("de")[1].split("degrees")[0].strip())
            if degrees > 1:
                large_movements.append(f"L{degrees}")
        except:
            pass
    elif "Tourne droite de" in line and "degrees" in line:
        try:
            degrees = int(line.split("de")[1].split("degrees")[0].strip())
            if degrees > 1:
                large_movements.append(f"R{degrees}")
        except:
            pass

# Print the large movements
print("Large movements in order:")
print(' '.join(large_movements))

# Try to interpret as ASCII
ascii_values = []
for movement in large_movements:
    cmd_type = movement[0]
    value = int(movement[1:])
    
    if cmd_type == 'F':
        ascii_values.append(value)
    elif cmd_type == 'B':
        ascii_values.append(-value)
    elif cmd_type == 'R':
        ascii_values.append(value)
    elif cmd_type == 'L':
        ascii_values.append(-value)

print("\nPossible ASCII interpretation:")
for val in ascii_values:
    if 32 <= val <= 126:
        print(chr(val), end='')
    else:
        print(f"[{val}]", end='')
print()
