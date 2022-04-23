import os

print('Welcome to mdConvert!')

for path, dirs, files in os.walk('.\\'):
    for filename in files:
        if filename.endswith('.md'):
            lines = []
            file_edit = False
            with open(os.path.join(path, filename), 'r', encoding='utf8', errors='ignore') as f: 
                lines = f.readlines()
                for idx, i in enumerate(lines): 
                    if i.find('![](P') == 0:
                        line = i.split('(')
                        line.insert(1,'(./attachments/') #Edit path?
                        lines[idx] = ''.join(line)
                        file_edit = True
            if file_edit:          
                with open(os.path.join(path, filename), 'w', encoding='utf8') as f: 
                    f.writelines(lines)
                print('\nFile converted: ' + path.strip('.') + '\\' + filename)
if input('\nDone!\n\nPress Enter to exit...'):
    exit(0)