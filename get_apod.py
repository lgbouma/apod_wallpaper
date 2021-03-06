import urllib
import datetime
import lxml.html

# We're starting 1 yr ago
today_str = str(datetime.date.today().year-1)+'-'\
            +'0'+ str(datetime.date.today().month)+'-'\
            + str(datetime.date.today().day)

todays_url = 'http://apod.nasa.gov/apod/ap'+''.join(today_str.split('-'))[2:]+'.html'

# Get caption and send it to file to read & delete at desktop:
html_tree = lxml.html.parse(todays_url)
p_tags = html_tree.xpath('//p')
p_content = [p.text_content() for p in p_tags]
to_write = [p.replace('\n',' ').strip() for p in p_content[1:3]]

f_name = '/home/lgbouma/Desktop/'+today_str+'-apod'
o = open(f_name, 'w')
for line in to_write:
    o.write(line+'\n')
o.close()

# Open today's url, get links, find highest res of today's image.
link_list = [link for link in html_tree.xpath('//a/@href')]

link_list = [link for link in link_list if 'http:' not in link and '.jpg' in link
             and 'https:' not in link and ''.join(today_str.split('-'))[2:-2] in link]

assert len(link_list) == 1, 'else i need to debug'
image_url = 'http://apod.nasa.gov/apod/'+link_list[0]

save_name = '/home/lgbouma/Dropbox/apod_wallpaper/images/'+today_str+'-'+image_url.split('/')[-1]
urllib.urlretrieve(image_url, save_name)

print 'gsettings set org.gnome.desktop.background picture-uri file://'+save_name
