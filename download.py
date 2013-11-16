import sys
from threading import Thread
from urllib.request import urlopen

class Down:
  def __init__(self):
    pass
  def dow(self,link):
    response=urlopen(link)
    filename=link.split('/')[-1]
    f=open(filename,'wb')
    meta=response.info()
    filesize=int(meta["Content-Length"])
    print("Downloading: %s Bytes: %s"%(filename,filesize))
    filesizedl = 0
    blocksz = 8192
    while True:
      buffer = response.read(blocksz)
      if not buffer:
        break
      filesizedl += len(buffer)
      f.write(buffer)
      status=filename+r"  %10d [%3.2f]"%(filesizedl,filesizedl*100./filesize)
      status = status + chr(8)*(len(status)+1)
      print(status,end='')
    print("")
    
    
    
def main():
  d=Down()
  threadlist=[]
  print(sys.argv[1],sys.argv[2])
  for i in range(len(sys.argv)-1):
    t=Thread(target=d.dow,args=(sys.argv[i+1],))
    t.start()
    threadlist.append(t)
  for i in threadlist:
    i.join()
  
if __name__=='__main__':
  main()
    
