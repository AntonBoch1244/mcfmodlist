import re, urllib2

def getdata():
    req = urllib2.Request('http://modlist.mcf.li/api/v3/all.json')
    resp = urllib2.urlopen(req)
    return re.findall(re.compile('{(?P<mod>.*?)}'), resp.read())
modlist = getdata()
maxpages = modlist.__len__()-1
class getInfo():
    def getName(self, page):
        try:
            return re.findall(re.compile('"name":"(?P<name>.*?)"'), modlist[page])[0]
        except:
            pass

    def getOther(self, page):
        try:
            return re.findall(re.compile('"other":"(?P<other>.*?)"'), modlist[page])[0]
        except:
            pass

    def getDesc(self, page):
        try:
            return re.findall(re.compile('"desc":"(?P<desc>.*?)"'), modlist[page])[0]
        except:
            pass

    def getLink(self, page):
        try:
            return re.findall(re.compile('"link":"(?P<link>.*?)"'), modlist[page])[0]
        except:
            pass

    def getSource(self, page):
        try:
            return re.findall(re.compile('"source":"(?P<source>.*?)"'), modlist[page])[0]
        except:
            pass

    def getAuthor(self, page):
        try:
            a=""
            authors = re.findall(re.compile('"author":\[(?P<author>.*?)\]'), modlist[page])[0]
            for i in re.findall(re.compile('\"(?P<author>.*?)\"'), authors):
                a += i + "\n"
            return a
        except:
            pass

    def getType(self, page):
        try:
            a=""
            type = re.findall(re.compile('"type":\[(?P<type>.*?)\]'), modlist[page])[0]
            for i in re.findall(re.compile('"(?P<type>.*?)"'), type):
                a += i + "\n"
            return a
        except:
            pass

    def getDependencies(self, page):
        try:
            a=""
            dep = re.findall(re.compile('"dependencies":\[(?P<dependencies>.*?)\]'), modlist[page])[0]
            for i in re.findall(re.compile('"(?P<dep>.*?)"'), dep):
                a += i + "\n"
            return a
        except:
            pass

    def getVersions(self, page):
        try:
            a=""
            ver = re.findall(re.compile('"versions":\[(?P<versions>.*?)\]'), modlist[page])[0]
            for i in re.findall(re.compile('"(?P<ver>.*?)"'), ver):
                a += i + "\n"
            return a
        except:
            pass

