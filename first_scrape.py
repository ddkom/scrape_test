# Tutorial by https://youtu.be/ng2o98k983k Cory Schafer 

from bs4 import BeautifulSoup
import requests

# Can open file, the below returns a BS object
# with open('simple.html') as html_file:
	# soup = BeautifulSoup(html_file, 'lxml')

# Shows all neatly
# print(soup.prettify())

# Show first title
# match = soup.title.text
# print(match)

# Show first div
# match = soup.title.text
# print(match)

# Find specific (e.g. div with class of footer)
# match = soup.find('div', class_='footer')
# print(match)

# Get each headline
# right click then 'Inspect'
	# first get headline and summary for first article
# article = soup.find('div', class_='article')
# print(article)
# headline = article.h2.a.text
# print(headline)
# summary = article.p.text
# print(summary)
	# for loop for getting any or all
# for article in soup.findall('div', class_='article'):
	# headline = article.h2.a.text
	# print(headline)

	# summary = article.p.text
	# print(summary)

	# print()



# Source a website
source = requests.get('http://coreyms.com').text
soup = BeautifulSoup(html_file, "lxml")
#print(soup.prettify()))

# Get first headline and snippet
# right click on headline and click inspect
# hover over to see which values in inspect contain
# all info we want
article = soup.find('article')
#print(article.prettify())

headline = article.hr.a.text
#print(headline)

# We dont need to put all parent tags (h2, p) but it is
# good to be a little specific
summary = article.find('div', class_='entry_content').p.text
#print(summary)

vid_src = article.find('iframe', class_='youtube-player')
#print(vid_src)

# We want to source value from the attribute of the tag
vid_src = article.find('iframe', class_='youtube-player')['src']
#print(vid_src)

vid_id = vid_src.split('/')[4] #4 is arbitrary test
#print(vid_id)

# Value for vid id is in certain spot 
vid_id = vid_id.split('?'[0])
#print(vid_id)

yt_link = f'https://youtube/com/watch?v={vid_id}'
print(yt_link)

# now the info is scraped for one article
# we can loop for all articles now

for article in soup.find_all('article'):
	headline = article.h2.a.text
	print(headline)

	summary = article.find('div', class_='entry-content').p.text
	print(summary)

	vid_src = article.find('iframe', class_='youtube-player')['src']
	
	vid_id = vid_src.split('/')[4]
	vid_id = vid_id.split('?')[0]

	yt_link = f'https://youtube.com/watch?V={vid_id}'
	print(yt_link)
	
	print()


# be weary of breaking scraper!!!
# e.g. type is not subscriptable
# we can skip by it with a try except block

	try:
	        vid_src = article.find('iframe', class_='youtub$

        	vid_id = vid_src.split('/')[4]
 	        vid_id = vid_id.split('?')[0]

 	        yt_link = f'https://youtube.com/watch?V={vid_id$

	except Exception as e:
		yt_link = None

                print(yt_link)
	        
	print()

# the above prints to screen
# save to CSV

import csv
# right before for loop
csv_file = open('first_scrape.csv', 'w') #w means write
csv_writer = csv.writer(csv_file)
# column names
csv_writer.writerow(['headline', 'summary', 'vid_link'])
#at end of for loop try
csv_writer.writerow([headline, summary, yt_link])
csv_file.close()
#csv file should be in local directory

# sometimes larger websites have a public API's for 
web scraping
# some websites will block scraping, will slow down 
servers
