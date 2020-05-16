from tools.lifeeasy import change_working_dir
from tools.lifeeasy import working_dir
from os import chdir
from os import getcwd

print(working_dir())
print(getcwd())
change_working_dir(working_dir() + '/tools')
print(working_dir())
print(getcwd())
