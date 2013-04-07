#!/usr/bin/env python

from os import system, popen

def preadlines(cmd, split=True):
    f = popen(cmd,"r")
    r = f.read()
    if split:
        r = r.splitlines()
    f.close()
    return r

system("./geeknote.py login")

system('mkdir -p data')

notebookslist = preadlines("./geeknote.py notebook-list | awk -F\" : \" '{print $2}' | grep .")

for nb in notebookslist:
    print nb
    system("mkdir -p data/%s" % nb)
    notes = preadlines("./geeknote.py find --notebooks %s | grep ." % nb)
    for n in notes:
        try:
            n = n.split(' : ')
            id = n[0]
            name = n[1]
            name = name[12:].replace(' ','_')+'-'+name[0:12]
            print id, name
            system("./geeknote.py show --note %s > \"data/%s/%s\"" % (id, nb, name))
        except:
            print 'Error while getting', n
