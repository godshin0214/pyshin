# func_hard_25.py

import os.path
from glob import glob


def traverse(dir, depth=0):
    global ndir, nfile
    for obj in glob(dir+'/*'):
        if LEVEL==1:
            print(os.path.basename(obj))
        else:
            if depth==0:
                prefix='|__'
            else:
                prefix='|     '*depth+'|__'

            
            # 디렉토리라면
            if os.path.isdir(obj):
                ndir+=1
                print(prefix+ os.path.basename(obj)) # 폴더이름이 나온다.
                traverse(obj,depth+1)
            # 파일이라면
            elif os.path.isfile(obj):
                nfile+=1
                print(prefix+ os.path.basename(obj)) # 파일이름이 나온다.
            # 나머지라면
            else:
                print(prefix+'unknown object')






#LEVEL=1 # 현재 폴더에 있는 파일들만 표시한다.
LEVEL=0 # 하위 폴더 안의 내용도 모두 출력한다.

ndir=0 # 폴더 개수
nfile=0 # 파일 개수

traverse('c:\zzz', 0)

print('\n',ndir,'directories,',nfile,'files')
