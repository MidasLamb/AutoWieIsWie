import requests
from html.parser import HTMLParser
import tkinter as tk
import time
import string
import itertools

root = tk.Tk()
# keep the window from showing
root.withdraw()

# read the clipboard


incontent = False
namenext = False
opleidingnext = False
found_name = ""
opleiding = ""
l = []

def analyseContent(string):
    if " " not in string:
        return [string, string]
    else:
        return string.split(" ")


def getWhoisWho(arr):
    global incontent
    global namenext
    global opleidingnext
    global found_name
    global opleiding
    global l
    incontent = False
    namenext = False
    opleidingnext = False
    l = []
    ret = {}
    found_name = ""
    opleiding = ""
    
    parser = MyHTMLParser()
    
    
    for x in range(len(arr)):
        for y in range(len(arr)):
            if (x == y):
                continue
            data= {
                'lang': 'N',
                'fnaam': arr[x],
                'vnaam': arr[y],
                }
            r = requests.post('http://cwisdb.kuleuven.be/studadm-bin/stududs.pl?lang=N', data=data)
            html = r.text
            parser.feed(html)
            
            if (len(l) > 0):
                ret[arr[x] + " " + arr[y]] = l
            l = []
    
    return ret


class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        global incontent
        global namenext
        for attr in attrs:
            if(attr[0] == "id"):
                if(attr[1] == "content"):
                    incontent = True
        if (incontent and tag=="h4"):
            namenext = True
                
    def handle_endtag(self, tag):
        global namenext
        global incontent
        if (incontent and tag=="h4" and namenext):
            namenext = False;

    def handle_data(self, data):
        global namenext
        global opleidingnext
        global found_name
        global opleiding
        if(namenext):
            found_name = data
        if(opleidingnext):
            l.append([found_name, data])
            opleidingnext = False
            
        if(data == "Opleiding: "):
            opleidingnext = True

clipcontent = ""

print()
while (True):
    c = root.clipboard_get()
    if (c != clipcontent):
        ret = analyseContent(c)
        r = getWhoisWho(ret)
        f = True
        
        for key, value in r.items():
            f = False
            print("Found " + str(len(value)) + " results for \"" + key + "\":")
            for w in value:
                print("    " + w[0])
                print("    " + w[1])
                print()
            print()
            
        if (f):
            print("Found no results for \"" + c + "\"")
            print()
        clipcontent = c;
    
    time.sleep(0.1)
