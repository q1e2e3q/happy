# coding=gbk
import psutil
import os
import time
 

dict = {'������': 'QyClient.exe', '��Ѷ��Ƶ': 'QQLive.exe','�Ѻ���Ƶ':'SohuVideo.exe','��ŭС��':'Angry Birds 2.exe'}

def printPids():
    pids = psutil.pids()
    for pid in pids:
        try:
            p = psutil.Process(pid)
            
            # �ر�excel����
            for v in dict.values():
                if p.name() == v:
                    # print('pid=%s,pname=%s' % (pid, p.name()))
                    cmd = ('taskkill /pid %d -t -f' % pid)
                    # print('%s' % cmd)
                    os.system(cmd)
                    # break
        except Exception as e:
            continue
 
if __name__ == '__main__':
    while True:
        printPids()
        time.sleep(10)



        