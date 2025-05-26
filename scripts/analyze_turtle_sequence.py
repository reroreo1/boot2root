#!/usr/bin/env python3

# This script analyzes the sequence of commands in the turtle file
# to look for patterns or hidden messages

def simplify_command(line):
    """Convert a turtle command to a simplified representation"""
    line = line.strip()
    if not line or "Can you digest" in line:
        return None
    
    if "Tourne gauche de" in line:
        degrees = line.split("de")[1].split("degrees")[0].strip()
        return f"L{degrees}"
    elif "Tourne droite de" in line:
        degrees = line.split("de")[1].split("degrees")[0].strip()
        return f"R{degrees}"
    elif "Avance" in line:
        spaces = line.split("Avance")[1].split("spaces")[0].strip()
        return f"F{spaces}"
    elif "Recule" in line:
        spaces = line.split("Recule")[1].split("spaces")[0].strip()
        return f"B{spaces}"
    return None

# Read the file and convert commands to simplified form
commands = []
with open('turtle', 'r') as file:
    for line in file:
        cmd = simplify_command(line)
        if cmd:
            commands.append(cmd)

# Write simplified commands to a file
with open('simplified_commands.txt', 'w') as outfile:
    for cmd in commands:
        outfile.write(cmd + '\n')

print(f"Wrote {len(commands)} simplified commands to simplified_commands.txt")

# Look for repeating patterns
pattern_length = 10  # Try to find patterns of this length
patterns = {}

for i in range(len(commands) - pattern_length + 1):
    pattern = tuple(commands[i:i+pattern_length])
    if pattern in patterns:
        patterns[pattern].append(i)
    else:
        patterns[pattern] = [i]

# Print repeating patterns
print("\nRepeating patterns:")
for pattern, positions in patterns.items():
    if len(positions) > 1:
        print(f"Pattern {pattern} appears at positions: {positions}")

# Look for ASCII encoding
# Try to interpret commands as ASCII codes
ascii_chars = []
current_value = 0

for cmd in commands:
    cmd_type = cmd[0]
    value = int(cmd[1:])
    
    if cmd_type == 'F':
        current_value += value
    elif cmd_type == 'B':
        current_value -= value
    elif cmd_type == 'R':
        current_value += value
    elif cmd_type == 'L':
        current_value -= value
    
    # If value is in ASCII range, convert to character
    if 32 <= current_value <= 126:
        ascii_chars.append(chr(current_value))
    
    # Reset after each potential character
    if len(ascii_chars) % 10 == 0:
        current_value = 0

if ascii_chars:
    print("\nPossible ASCII interpretation:")
    print(''.join(ascii_chars))
