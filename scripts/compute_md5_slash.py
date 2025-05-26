#!/usr/bin/env python3

import hashlib

# Read the turtle file
with open('turtle', 'rb') as f:
    turtle_content = f.read()

# Compute MD5 hash of turtle file + "SLASH"
combined_content = turtle_content + b"SLASH"
md5_hash = hashlib.md5(combined_content).hexdigest()

print("MD5 hash of turtle file + 'SLASH':")
print(md5_hash)

# Also try SLASH + turtle file
combined_content2 = b"SLASH" + turtle_content
md5_hash2 = hashlib.md5(combined_content2).hexdigest()

print("\nMD5 hash of 'SLASH' + turtle file:")
print(md5_hash2)

# Try just MD5 of "SLASH"
md5_slash = hashlib.md5(b"SLASH").hexdigest()
print("\nMD5 hash of just 'SLASH':")
print(md5_slash)
