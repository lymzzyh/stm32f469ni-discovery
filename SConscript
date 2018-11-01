# for module compiling
import os
from building import *

cwd = GetCurrentDir()
CPPPATH = [cwd]
src = []
objs = []

objs += DefineGroup('Application', src, depend = [''], CPPPATH = CPPPATH)

list = os.listdir(cwd)

for d in list:
    path = os.path.join(cwd, d)
    if os.path.isfile(os.path.join(path, 'SConscript')):
        objs = objs + SConscript(os.path.join(d, 'SConscript'))

Return('objs')
