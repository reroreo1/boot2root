#!/bin/bash

# Script to push useful files to the boot2root repository
# Excludes pcap files and includes only useful scripts and documentation

echo "Setting up git repository..."

# Initialize git if not already done
if [ ! -d ".git" ]; then
    git init
fi

# Add remote origin
git remote add origin https://github.com/reroreo1/boot2root.git 2>/dev/null || echo "Remote already exists"

# Create .gitignore to exclude pcap files
cat > .gitignore << EOF
# Exclude pcap files
*.pcap

# Exclude compiled binaries
a.out
reconstructed_code

# Exclude temporary files
*.tmp
*.log
EOF

echo "Adding useful files to git..."

# Add useful scripts and files
git add bomb.c
git add reconstructed_code.c
git add turtle
git add EXPLOIT_ME.c

# Add Python analysis scripts
git add pcap_analyzer.py
git add analyze_turtle_sequence.py
git add extract_large_movements.py
git add extract_unique_turtle.py
git add visualize_turtle.py
git add visualize_turtle_simple.py
git add visualize_turtle_svg.py
git add compute_hmac.py

# Add visualization files
git add view_turtle.html
git add turtle_path.svg

# Add analysis results
git add simplified_commands.txt
git add unique_turtle_commands.txt

# Add .gitignore
git add .gitignore

echo "Files added to git. Ready to commit and push."
echo "Run the following commands to complete the push:"
echo ""
echo "git commit -m 'Add boot2root challenge scripts and analysis tools'"
echo "git branch -M main"
echo "git push -u origin main"
