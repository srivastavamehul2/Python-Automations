#Created by Mehul Srivastava
import re
import urllib.request

try:
    country = input('Enter the country:\n')
    url = "https://www.timeanddate.com/weather/" #darbhanga
    city = input('Enter the city:\n')
    url = url+country+'/'+city

    d = urllib.request.urlopen(url).read()
    d1 = d.decode('utf-8')

    #print(d1)
    m = re.search('</h1></header><section id=bk-focus class=bk-wt><div class=fixed><div id=tri-focus>&#9698;</div><div id=qlook class="three columns"><div class=h1>Now</div><img id=cur-weather class=mtt title="',d1)
    start = m.end()
    end = start+400
    s = d1[start:end]

    m = re.search('." src=',s)
    print(s[:m.start()])

    s = s[m.end():]

    m = re.search('Feels Like: ',s)
    s = s[m.start():]
    print(s[:14] + '°C')


    m = re.search('Forecast: ',s)
    s = s[m.start():]
    print(s[:17] + '°C')

    m = re.search('Wind blowing from ',s)
    s = s[m.start():]
    m = re.search('>↑</span>',s)
    s = s[:m.start()-1]


    print(s)
except:
    print('City not found')

input()
