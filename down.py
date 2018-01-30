from lxml import etree
import re
import requests


def get_danmu(av):
    url = "http://www.bilibili.com/video/av" + av
    page = requests.get(url)
    match = re.search(r'cid=(\d+)', page.text)
    if match:       
        cid = match.group(1)
        #print(cid)
    else:
        print("Cannot find danmu!")
        return 
    xml_path = "http://comment.bilibili.tv/{0}.xml".format(cid)

    danmu = requests.get(xml_path)
    fp = open(cid+'.xml',"w+b")
    fp.write(danmu.text.encode('utf-8'))
    fp.close()
    #doc = etree.fromstring(danmu.text.encode('utf-8'))
    #with open(cid+'.xml', 'wb+') as f:
    #    for i in doc:
    #        content = i.text + '\n'
            #print(content)
    #        f.write(content.encode('utf-8'))
    #    f.close()
  

if __name__ == '__main__':
    av = input("input the av number:")
    get_danmu(av)
  