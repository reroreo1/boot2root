#!/usr/bin/env python3

import os
import re
import sys

def extract_file_number(content):
    """Extract the file number from the content."""
    match = re.search(r'//file(\d+)', content)
    if match:
        return int(match.group(1))
    return None

def clean_content(content):
    """Remove useless functions and other unnecessary code."""
    # Remove void useless() function and its content
    content = re.sub(r'(}?void useless\(\)\s*{[^}]*}?)', '', content)
    # Remove any remaining curly braces at the beginning
    content = re.sub(r'^}', '', content)
    # Extract only the meaningful code
    return content.strip()

def process_pcap_files(directory):
    """Process all PCAP files in the directory and sort them by file number."""
    file_contents = []
    
    # Process each PCAP file
    for filename in os.listdir(directory):
        if filename.endswith('.pcap'):
            filepath = os.path.join(directory, filename)
            try:
                with open(filepath, 'r') as f:
                    content = f.read()
                
                file_num = extract_file_number(content)
                if file_num is not None:
                    cleaned_content = clean_content(content)
                    file_contents.append((file_num, cleaned_content, filename))
                    print(f"Processed {filename} - File number: {file_num}")
                else:
                    print(f"No file number found in {filename}")
                    
            except Exception as e:
                print(f"Error processing {filename}: {e}")
    
    # Sort by file number
    file_contents.sort(key=lambda x: x[0])
    return file_contents

def write_output_file(file_contents, output_file):
    """Write the sorted and cleaned content to the output file."""
    with open(output_file, 'w') as f:
        for file_num, content, filename in file_contents:
            if content.strip():  # Only write non-empty content
                f.write(f"// From file {filename} (file number {file_num})\n")
                f.write(content)
                f.write("\n\n")
    
    print(f"Output written to {output_file}")

def main():
    if len(sys.argv) < 2:
        print("Usage: python pcap_analyzer.py <pcap_directory> [output_file]")
        return
    
    directory = sys.argv[1]
    output_file = sys.argv[2] if len(sys.argv) > 2 else "reconstructed_code.c"
    
    if not os.path.isdir(directory):
        print(f"Error: {directory} is not a directory")
        return
    
    file_contents = process_pcap_files(directory)
    write_output_file(file_contents, output_file)
    
    print(f"Processed {len(file_contents)} files")

if __name__ == "__main__":
    main()
