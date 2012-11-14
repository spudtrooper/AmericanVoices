import fileinput, sys
from collections import OrderedDict

class Info:
    
    def __init__(self,name,job,url):
        self.name = name
        self.job = job
        self.url = url

def main(argv):
    prog = argv.pop(0)
    imgs2infos = {}
    for line in fileinput.input():
        line = line.strip()
        img,name,job,url = line.split('|')
        info = Info(name,job,url)
        lst = imgs2infos.get(img)
        if not lst:
            lst = []
        lst.append(info)
        imgs2infos[img] = lst
    print '<html>'
    print '<head>'
    print '<style>'
    print '.m li {'
    print ' display: inline;'
    print ' float: left;'
    print ' padding: 10px'
    print '}'
    print '</style>'
    print '</head>'
    print '<body>'
    print '<h1>The Onion - American Voices</h1>'
    print '<ul class="m" style="overflow:both; width:%dpx">' % (len(imgs2infos) * 300)
    odd = True
    sortedImgs2Infos = OrderedDict(sorted(imgs2infos.items(), 
                                          key=lambda x: -len(x[1])))
    for img,infos in sortedImgs2Infos.iteritems():
        print '<li>'
        print '<img src="%s"</img>' % (img)
        print '<br/>'
        for info in infos:
            print '<a href="%s">%s</a> - %s' % (info.url, info.name, info.job)
            print '<br/>'
        print '</li>'
    print '</body>'
    print '</html>'

if __name__ == '__main__':
    main(sys.argv)
