#!/usr/bin/python3
#Author: DjikstraCS

import os
conversions = 0

print('\n Welcome to...\n\n  8888b   d8888 8888888.\n  88888b d88888 888  \'88b\n  888Y88888P888 888   888\n  888 Y888P 888 888   888\n  888 _Y8P_ 888 888  d88P            __\n  888 ____/_888 888888P\' _____  ____/ /_\n   / /   / __ \/ __ \ | / / _ \/ __/ __/\n  / /___/ /_/ / / / / |/ /  __/ / / /_\n  \____/\____/_/ /_/|___/\___/_/  \__/')

user_input = input('\n\n Start conversion? (Y/n) ').lower().strip()
if user_input: 
    if user_input != 'y':
        exit(0)

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
                print('\n File converted: ' + path.strip('.')[1:] + '\\' + filename)
                conversions = conversions + 1

if conversions == 1:
    print('\n 1 file converted.')
elif conversions > 1:
    print('\n ' + str(conversions) + ' files converted.')
else:
    print('\n No files were converted.')

if input(' Press Enter to exit...'):
    exit(0)