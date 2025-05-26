# Boot2Root Challenge - Complete Solution Guide

This repository documents the complete solution to a multi-stage Boot2Root challenge involving reverse engineering, cryptography, and privilege escalation. The challenge consists of interconnected puzzles that must be solved sequentially to gain access to different user accounts.

## 🎯 Challenge Overview

The Boot2Root challenge is structured as follows:
1. **PCAP Forensics** → Extract and reconstruct hidden code
2. **Binary Reverse Engineering** → Solve a "bomb lab" with multiple phases
3. **Cryptographic Analysis** → Decode visual hints and apply hash functions
4. **Privilege Escalation** → Use discovered credentials to access user accounts

## 📁 Repository Contents

### Core Challenge Files
- `bomb.c` - Decompiled bomb lab source code (6 phases + secret phase)
- `reconstructed_code.c` - Reconstructed C program from PCAP analysis
- `turtle` - Turtle graphics commands that encode cryptographic hints
- `EXPLOIT_ME.c` - Additional challenge component

### Analysis Tools
- `pcap_analyzer.py` - PCAP file analysis and code extraction
- `visualize_turtle_svg.py` - Generate SVG visualization of turtle graphics
- `compute_md5_slash.py` - MD5 hash computation for password generation
- `analyze_turtle_sequence.py` - Pattern analysis in turtle commands

## 🔍 Detailed Solution Walkthrough

### Stage 1: PCAP Forensics and Code Reconstruction

**Challenge**: Hundreds of PCAP files containing fragmented code pieces

**Approach**:
1. **Mass PCAP Analysis**: Created `pcap_analyzer.py` to process all PCAP files
2. **Code Fragment Extraction**: Each PCAP contained small C code snippets with file markers
3. **Reconstruction Logic**: Assembled fragments based on file number ordering
4. **Validation**: Compiled and executed reconstructed code

**Key Discovery**:
```c
// Reconstructed program reveals:
printf("MY PASSWORD IS: Iheartpwnage\n");
printf("Now SHA-256 it and submit\n");
```

**Tools Used**:
```bash
python3 pcap_analyzer.py  # Extract and sort code fragments
gcc reconstructed_code.c -o reconstructed_code  # Compile
./reconstructed_code  # Execute to reveal password
```

### Stage 2: Bomb Lab Reverse Engineering

**Challenge**: Binary "bomb" with 6 phases that explode on wrong input

**Analysis Method**:
1. **Static Analysis**: Examined decompiled C code in `bomb.c`
2. **Function Flow**: Traced execution paths for each phase
3. **Input Validation**: Understood expected input formats and constraints

**Phase Solutions**:

#### Phase 1: String Comparison
```c
// Simple string comparison
iVar1 = strings_not_equal(param_1, "Public speaking is very easy.");
```
**Solution**: `"Public speaking is very easy."`

#### Phase 2: Mathematical Sequence
```c
// Factorial sequence validation
read_six_numbers(param_1, aiStack_20 + 1);
if (aiStack_20[1] != 1) explode_bomb();
// Each number = position * previous_number
```
**Solution**: `"1 2 6 24 120 720"`

#### Phase 3: Switch Statement
```c
// Switch case with character and number validation
sscanf(param_1, "%d %c %d", &local_10, &local_9, &local_8);
switch(local_10) {
    case 2: cVar2 = 'b'; if (local_8 != 0x2f3) explode_bomb();
}
```
**Solution**: `"2 b 755"` (0x2f3 = 755 in decimal)

#### Phase 4: Fibonacci + Secret Phase Trigger
```c
// Fibonacci function that must return 0x37 (55)
iVar1 = func4(local_8);
if (iVar1 != 0x37) explode_bomb();
```
**Solution**: `"9 austinpowers"` (9 produces 55, "austinpowers" triggers secret phase)

#### Phase 5: Character Mapping
```c
// Maps input characters to spell "giants"
local_c[iVar1] = (&array_123)[(char)(*(byte *)(iVar1 + param_1) & 0xf)];
iVar1 = strings_not_equal(local_c, "giants");
```
**Solution**: `"opekma"` (maps to "giants" through character transformation)

#### Phase 6: Linked List Reordering
```c
// Reorders linked list nodes based on input
read_six_numbers(param_1, local_1c);
// Complex linked list manipulation
```
**Solution**: `"4 2 6 3 1 5"` (specific node ordering)

#### Secret Phase: Binary Tree Traversal
```c
// Accessed after completing all phases with "austinpowers" in phase 4
iVar2 = fun7(n1, iVar2);
if (iVar2 != 7) explode_bomb();
```
**Solution**: `"1001"` (navigates binary tree to return value 7)

### Stage 3: Turtle Graphics Cryptographic Analysis

**Challenge**: Turtle graphics file with cryptic hint "Can you digest the message? :)"

**Analysis Process**:
1. **Visualization**: Created SVG renderer to see what turtle commands draw
2. **Pattern Recognition**: Turtle path forms the letters "MD5"
3. **Hint Interpretation**: "digest" in cryptography refers to hash functions

**Visualization**:
```bash
python3 visualize_turtle_svg.py  # Generate turtle_path.svg
open view_turtle.html  # View in browser
```

**Key Insight**: The visual pattern "MD5" + hint "digest" indicates MD5 hashing is required

### Stage 4: Password Generation and User Access

**Password Derivation Chain**:

1. **Base Password**: `"Iheartpwnage"` (from reconstructed code)
2. **Thor User**: MD5 hash of "Iheartpwnage"
   ```bash
   echo -n "Iheartpwnage" | md5sum
   # Result: 02e74f10e0327ad868d138f2b4fdd6f0
   ```
3. **Zaz User**: MD5 hash of turtle file + "SLASH"
   ```bash
   python3 compute_md5_slash.py
   # Result: 7c8b271d27e0c086425fdce5fc360c9a
   ```

**SSH Access**:
```bash
ssh thor@target -p 22  # Password: 02e74f10e0327ad868d138f2b4fdd6f0
ssh zaz@target -p 22   # Password: 7c8b271d27e0c086425fdce5fc360c9a
```

## 🔧 Tools and Scripts Usage

### PCAP Analysis
```bash
# Analyze all PCAP files and reconstruct code
python3 pcap_analyzer.py

# Compile and run reconstructed program
gcc reconstructed_code.c -o reconstructed_code
./reconstructed_code
```

### Bomb Lab Analysis
```bash
# Compile bomb (if source available)
gcc bomb.c -o bomb

# Run with solution file
echo -e "Public speaking is very easy.\n1 2 6 24 120 720\n2 b 755\n9 austinpowers\nopekma\n4 2 6 3 1 5\n1001" > solutions.txt
./bomb solutions.txt
```

### Turtle Graphics Analysis
```bash
# Generate visualization
python3 visualize_turtle_svg.py

# View result
open view_turtle.html

# Analyze patterns
python3 analyze_turtle_sequence.py
```

### Password Generation
```bash
# Generate MD5 hashes for user access
python3 compute_md5_slash.py
```

## 🧠 Key Problem-Solving Insights

### 1. Multi-Stage Information Flow
- Each stage provides information needed for subsequent stages
- The bomb's secret phase requires information from phase 4
- Turtle graphics provides the hash function hint (MD5)
- PCAP analysis provides the base password

### 2. Visual Cryptography
- Turtle graphics encodes "MD5" as a visual pattern
- The hint "Can you digest the message?" uses cryptographic terminology
- Visual analysis was crucial for understanding the hash function requirement

### 3. Reverse Engineering Techniques
- **Static Analysis**: Reading decompiled code to understand logic
- **Dynamic Analysis**: Testing inputs to validate understanding
- **Pattern Recognition**: Identifying mathematical sequences and algorithms

### 4. Cryptographic Chain
```
PCAP Files → "Iheartpwnage" → MD5 → Thor Access
Turtle Graphics → "MD5" hint → MD5(turtle + "SLASH") → Zaz Access
```

## 🛡️ Security Lessons Learned

1. **Defense in Depth**: Multiple layers of obfuscation and encoding
2. **Information Correlation**: Clues scattered across different file types
3. **Visual Steganography**: Important information hidden in graphical patterns
4. **Hash Function Security**: Proper use of cryptographic hash functions
5. **Reverse Engineering Countermeasures**: Code obfuscation and anti-analysis techniques

## 📊 Challenge Statistics

- **PCAP Files Analyzed**: 750+
- **Code Fragments Reconstructed**: 750+
- **Bomb Phases Solved**: 7 (6 regular + 1 secret)
- **Hash Functions Used**: MD5
- **Programming Languages**: C, Python
- **Total Solution Time**: Multiple hours of analysis

## 🔄 Reproduction Steps

1. **Clone Repository**:
   ```bash
   git clone https://github.com/reroreo1/boot2root.git
   cd boot2root
   ```

2. **Run PCAP Analysis**:
   ```bash
   python3 pcap_analyzer.py
   gcc reconstructed_code.c -o reconstructed_code
   ./reconstructed_code
   ```

3. **Solve Bomb Lab**:
   ```bash
   # Use solutions documented above
   ```

4. **Analyze Turtle Graphics**:
   ```bash
   python3 visualize_turtle_svg.py
   open view_turtle.html
   ```

5. **Generate Passwords**:
   ```bash
   python3 compute_md5_slash.py
   ```

## 🎓 Educational Value

This challenge demonstrates:
- **Forensic Analysis**: Extracting information from network captures
- **Reverse Engineering**: Understanding binary behavior through static analysis
- **Cryptographic Analysis**: Recognizing and applying hash functions
- **Problem Decomposition**: Breaking complex challenges into manageable parts
- **Tool Development**: Creating custom scripts for specific analysis tasks

---

**⚠️ Disclaimer**: This repository is for educational purposes only. All techniques should be used only in authorized environments and for legitimate security research.
