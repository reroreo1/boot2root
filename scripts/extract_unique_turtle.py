#!/usr/bin/env python3

# This script extracts unique lines from the turtle file
# and saves them to a new file

unique_lines = set()

with open('turtle', 'r') as file:
    for line in file:
        line = line.strip()
        if line and not line.startswith("Can you digest"):
            unique_lines.add(line)

# Sort the unique lines for better readability
sorted_unique_lines = sorted(unique_lines)

# Write unique lines to a new file
with open('unique_turtle_commands.txt', 'w') as outfile:
    for line in sorted_unique_lines:
        outfile.write(line + '\n')

print(f"Extracted {len(unique_lines)} unique lines to unique_turtle_commands.txt")

# Also create a simplified version with just the command types
command_types = set()
for line in unique_lines:
    if "Tourne gauche de" in line:
        command_types.add("Tourne gauche")
    elif "Tourne droite de" in line:
        command_types.add("Tourne droite")
    elif "Avance" in line:
        command_types.add("Avance")
    elif "Recule" in line:
        command_types.add("Recule")

print(f"Found {len(command_types)} unique command types: {', '.join(command_types)}")
