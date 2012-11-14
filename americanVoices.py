import os, re, string, sys, urllib2
from BeautifulSoup import BeautifulSoup

"""
Reads American Voices entries from theonion.com and outputs to STDOUT.
"""

LAST_URL_FILE = 'lastUrl.txt'

def log(msg):
    print >> sys.stderr, msg

def saveLastUrl(url):
    with open(LAST_URL_FILE, 'w') as f:
        f.write(url)

def getLastUrl():
    file = LAST_URL_FILE
    if not os.path.exists(file):
        return None
    with open(file, 'r') as f:
        return f.read()
    return None

class AmericanVoices:

    def main(self, url):
        self.loop(url)

    def loop(self, url):
        log(url)
        page = urllib2.urlopen(url)
        imgs = []
        soup = BeautifulSoup(page)
        for div in soup('div', {'class': 'image'}):
            for img in div.findAll('img'):
                src = str(img['src'])
                if re.match('^http:\/\/', src):
                    imgs.append(src)
        names = []
        jobs = []
        try:

            for p in soup('p', {'class': 'occupation'}):
                name,br,job = [str(x).strip() for x in p.contents]
                names.append(name)
                jobs.append(job)

            # Write out the values
            for img,name,job in zip(imgs, names, jobs):
                print '|'.join([img,name,job,url])
            sys.stdout.flush()
            saveLastUrl(url)
        except:
            pass

        # Find the next link
        for li in soup('li', {'class': 'previous'}):
            a = li.find('a')
            newUrl = 'http://www.theonion.com' + a['href']
            self.loop(newUrl)

def main(argv):
    prog = argv.pop(0)
    if len(argv) > 0:
        url = argv.pop(0)
    else:
        url = getLastUrl()
        if not url:
            url = 'http://www.theonion.com/articles/apple-unveils-ipad-mini,30068/'
    AmericanVoices().main(url)

if __name__ == '__main__':
    main(sys.argv)
