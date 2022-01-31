import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument('path')
args = parser.parse_args()
print(args.path)

def get_new_lines(file):
    with open(file) as f:
        lines = f.readlines()
        replace_count = 0
        decl_end = len(lines)
        for i in range(len(lines)):
            line = lines[i]
            if line.startswith('owner') or line.startswith('controller') or line.startswith('add_core'):
                replace_count += 1
            
            if line.startswith('1861.1.1'):
                decl_end = i
                break
        
        return [
            *lines[replace_count : decl_end],
            '1800.1.1 = {\n',
            *lines[:replace_count],
            '}\n',
            *lines[decl_end:],
        ]


path = args.path
if path != None:
    file_list = os.listdir(path)
    for file in file_list:
        new_lines = get_new_lines(path + file)
        with open(path + file, 'w') as f:
            f.writelines(new_lines)


