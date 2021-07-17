from pynput.keyboard import Listener

def get_key_name(key):
    if hasattr(key, 'char'):
        return key.char
    elif hasattr(key, 'name'):
        return key.name
    return None

import time
class KListener:
    keylist=[]
    def __init__(self):
        pass


    def presskey(self, key):
        key = get_key_name(key)
        self.keylist.append([key,time.time(),'press'])
        if key == 'f10':
            self.output()
    def releasekey(self,key):
        key = get_key_name(key)
        self.keylist.append([key,time.time(),'release'])

    def output(self):
        with open("key.txt",'a')as f:
            for key,time,mode in self.keylist:
                f.write(str(key)+' '+str(mode)+' '+str(time)+'\n')

    def join(self):
        with Listener(on_press=lambda x: self.presskey(x),on_release=lambda x: self.releasekey(x)) as listener:
            listener.join()
if __name__=="__main__":
    l = KListener()
    l.join()