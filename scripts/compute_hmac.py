#!/usr/bin/env python3

import hashlib
import hmac

# Read the turtle file
with open('turtle', 'rb') as f:
    turtle_content = f.read()

# Compute HMAC-SHA256 with "SLASH" as key
key = b"SLASH"
hmac_sha256 = hmac.new(key, turtle_content, hashlib.sha256).hexdigest()

# Also try regular SHA256 of turtle file + "SLASH"
sha256_combined = hashlib.sha256(turtle_content + key).hexdigest()

# Try SHA256 of "SLASH" + turtle file
sha256_combined2 = hashlib.sha256(key + turtle_content).hexdigest()

print("HMAC-SHA256 of turtle file with key 'SLASH':")
print(hmac_sha256)
print()
print("SHA256 of turtle file + 'SLASH':")
print(sha256_combined)
print()
print("SHA256 of 'SLASH' + turtle file:")
print(sha256_combined2)

# Also try with different hash algorithms
hmac_sha1 = hmac.new(key, turtle_content, hashlib.sha1).hexdigest()
hmac_md5 = hmac.new(key, turtle_content, hashlib.md5).hexdigest()

print()
print("HMAC-SHA1 of turtle file with key 'SLASH':")
print(hmac_sha1)
print()
print("HMAC-MD5 of turtle file with key 'SLASH':")
print(hmac_md5)
