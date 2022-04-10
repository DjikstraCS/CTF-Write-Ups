import os

for path, dirs, files in os.walk('../'):
    for filename in files:
        if filename.endswith('.md'):
            lines = []
            file_edit = False
            with open(os.path.join(path, filename), 'r') as f: 
                lines = f.readlines()
                for idx, i in enumerate(lines): 
                    if i.find('![](P') == 0:
                        file_edit = True
                        line_edit_list = i.split('(')
                        line_edit_list.insert(1,'(./attachments/') #Edit path?
                        lines[idx] = ''.join(line_edit_list)
            if file_edit:          
                with open(os.path.join(path, filename), 'w') as f: 
                    f.writelines(lines)