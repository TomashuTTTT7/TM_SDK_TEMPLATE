import os

name = ''

for path in os.listdir('.'):
    if path.endswith('.sln'):
        name = path[:-4]
        break

def init_file(filename, name):
    if os.path.isfile(filename):
        with open(filename, 'r') as file:
            filedata = file.read()
        filedata = filedata.replace('TM_SDK_TEMPLATE', name)
        with open(filename, 'w') as file:
            file.write(filedata)

init_file(f'{name}.sln', name)
init_file(f'{name}\{name}.vcxproj', name)
init_file(f'{name}\{name}.vcxproj.user', name)
init_file(f'{name}\{name}.vcxproj.filters', name)
init_file(f'{name}\FileInfo.h', name)
init_file(f'MyLibs\README.md', name)