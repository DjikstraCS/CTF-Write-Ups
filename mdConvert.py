import os

print('\n--==≡≡≡___Welcome_to_mdConvert!___≡≡≡==--')

if input('\nStart conversion? (Y/n) ').lower() != 'y':
    exit(0)

conversions = 0

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
                conversions = conversions + 1

if conversions == 1:
    print('\n1 file converted.')
elif conversions > 1:
    print('\n' + str(conversions) + ' files converted.')
else:
    print('\nNo files converted.')

if input('Press Enter to exit...'):
    exit(0)