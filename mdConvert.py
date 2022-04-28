#!/usr/bin/python3
#Author: DjikstraCS

import os

print('\n-=≡| Welcome to mdConvert! |≡=-')

if input('\nStart conversion? (Y/n) ').lower().strip() != 'y':
    exit(0)

conversions = 0

for path, dirs, files in os.walk('.'):
    for filename in files:
        if filename.endswith('.md'):
            lines = []
            file_edit = False
            with open(os.path.join(path, filename), 'r', encoding='utf8', errors='ignore') as f: 
                lines = f.readlines()
                for idx, i in enumerate(lines): 
                    if i.find('![]') == 0 and i.find('./') == -1:
                        line = i.split('(')
                        line.insert(1,'(./attachments/') #Edit path?
                        lines[idx] = ''.join(line)
                        file_edit = True
            if file_edit:          
                with open(os.path.join(path, filename), 'w', encoding='utf8') as f: 
                    f.writelines(lines)
                print('\nFile converted: ' + path.strip('.') + '\\' + filename)
                conversions = conversions + 1

if conversions == 1:
    print('\n1 file converted.')
elif conversions > 1:
    print('\n' + str(conversions) + ' files converted.')
else:
    print('\nNo files were converted.')

if input('Press Enter to exit...'):
    exit(0)