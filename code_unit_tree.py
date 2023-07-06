""" 
Given a Salesforce debug log file, this script generates a text file with CODE_UNIT_STARTED and CODE_UNIT_FINISHED lines
nested via tabs. This is useful for finding recursive processes when debugging Salesforce governor limit errors. 

Example usage: 
	python code_unit_tree.py logfile.log output.txt

"""
import sys

if len(sys.argv) < 3:
    print("Usage: python code_unit_tree.py [source_file] [output_file]")
    sys.exit(1)

source_file = sys.argv[1]
output_file = sys.argv[2]

with open(source_file, encoding='utf-8', errors='ignore') as f:
    lines = f.readlines()

output = ''
indentation_level = 0

for line in lines:
    if 'CODE_UNIT_STARTED' in line or 'CODE_UNIT_FINISHED' in line or '***' in line:
        output += '\t' * indentation_level + line
        if 'CODE_UNIT_STARTED' in line:
            indentation_level += 1
        elif 'CODE_UNIT_FINISHED' in line:
            indentation_level = max(0, indentation_level - 1)

with open(output_file, 'w') as f:
    f.write(output)
