# Boot2Root Challenge Solutions

This repository contains scripts and analysis tools used to solve the Boot2Root challenge, which involves multiple phases of reverse engineering, cryptography, and system exploitation.

## Challenge Overview

The Boot2Root challenge consists of several interconnected puzzles:
1. **PCAP Analysis**: Extracting and reconstructing code from network packet captures
2. **Bomb Lab**: Reverse engineering a binary "bomb" with multiple phases
3. **Turtle Graphics**: Analyzing turtle graphics commands to reveal cryptographic hints
4. **User Privilege Escalation**: Using discovered passwords to access different user accounts

## Files and Scripts

### Core Challenge Files

- **`bomb.c`** - Decompiled bomb lab source code with 6 phases + secret phase
- **`reconstructed_code.c`** - Reconstructed C code from PCAP analysis revealing password "Iheartpwnage"
- **`turtle`** - Turtle graphics commands file that draws "MD5" when visualized
- **`EXPLOIT_ME.c`** - Additional challenge file

### Analysis Scripts

#### PCAP Analysis
- **`pcap_analyzer.py`** - Script to analyze and extract data from PCAP files

#### Turtle Graphics Analysis
- **`analyze_turtle_sequence.py`** - Analyzes turtle command sequences for patterns
- **`extract_large_movements.py`** - Extracts significant movements from turtle commands
- **`extract_unique_turtle.py`** - Finds unique commands in the turtle file
- **`visualize_turtle.py`** - Creates turtle graphics visualization using Python turtle module
- **`visualize_turtle_simple.py`** - Simplified turtle visualization
- **`visualize_turtle_svg.py`** - Generates SVG visualization of turtle path

#### Cryptographic Analysis
- **`compute_hmac.py`** - Computes various hash functions (HMAC, SHA, MD5) for password generation

### Visualization Files
- **`view_turtle.html`** - HTML file to view turtle graphics SVG in browser
- **`turtle_path.svg`** - SVG visualization showing "MD5" pattern

### Analysis Results
- **`simplified_commands.txt`** - Simplified turtle commands for analysis
- **`unique_turtle_commands.txt`** - List of unique turtle commands

## Solution Summary

### Phase 1: PCAP Analysis
1. Analyzed hundreds of PCAP files to extract code fragments
2. Reconstructed complete C program revealing password "Iheartpwnage"
3. Compiled and executed to confirm password

### Phase 2: Bomb Lab
Solved 6 phases + secret phase:
- **Phase 1**: "Public speaking is very easy."
- **Phase 2**: "1 2 6 24 120 720" (factorial sequence)
- **Phase 3**: "2 b 755" (switch case with character and number)
- **Phase 4**: "9 austinpowers" (Fibonacci + secret phase trigger)
- **Phase 5**: "opekma" (character mapping to "giants")
- **Phase 6**: "4 2 6 3 1 5" (linked list reordering)
- **Secret Phase**: "1001" (binary tree traversal)

### Phase 3: Turtle Graphics
1. Visualized turtle commands to reveal "MD5" pattern
2. Interpreted "Can you digest the message? :)" hint
3. Applied MD5 hash to "Iheartpwnage" → `02e74f10e0327ad868d138f2b4fdd6f0`

### Phase 4: User Access
- **thor user**: MD5 hash of "Iheartpwnage"
- **zaz user**: HMAC-SHA with "SLASH" key on turtle file

## Key Insights

1. **Multi-layered puzzle**: Each phase builds on previous discoveries
2. **Cryptographic hints**: Visual patterns (MD5) indicate hash function usage
3. **Cross-references**: Bomb phases contain triggers for secret content
4. **File relationships**: Different files contain pieces of the complete solution

## Usage

### Running Visualizations
```bash
# Generate turtle graphics visualization
python3 visualize_turtle_svg.py

# View in browser
open view_turtle.html
```

### Computing Hashes
```bash
# Compute various hashes for password generation
python3 compute_hmac.py
```

### Analyzing Patterns
```bash
# Extract unique turtle commands
python3 extract_unique_turtle.py

# Analyze command sequences
python3 analyze_turtle_sequence.py
```

## Tools Used

- **Python 3**: For analysis scripts and visualizations
- **GCC**: For compiling reconstructed C code
- **Git**: For version control
- **Web browser**: For viewing SVG visualizations

## Security Lessons

This challenge demonstrates:
- Importance of analyzing all available data sources
- How visual patterns can encode cryptographic hints
- Multi-stage authentication and privilege escalation
- Reverse engineering techniques for binary analysis

## Repository Structure

```
boot2root/
├── README.md                    # This file
├── bomb.c                       # Bomb lab source
├── reconstructed_code.c         # Reconstructed password program
├── turtle                       # Turtle graphics commands
├── analysis/                    # Analysis scripts
│   ├── pcap_analyzer.py
│   ├── turtle_analysis/
│   └── crypto/
└── visualizations/              # Generated visualizations
    ├── turtle_path.svg
    └── view_turtle.html
```

---

**Note**: This repository contains educational content for cybersecurity learning purposes. All techniques should only be used in authorized environments.
