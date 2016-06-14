#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
import sys
reload(sys)
sys.setdefaultencoding('utf8')
import re
import urllib2
import random
import xlwt
from bs4 import BeautifulSoup
import time

headers = [
    {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:34.0) Gecko/20100101 Firefox/34.0','Referer':'https://www.douban.com/'},
    {'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6','Referer':'https://www.douban.com/'},
    {'User-Agent': 'Mozilla/5.0 (Windows NT 6.2) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.12 Safari/535.11','Referer':'https://www.douban.com/'},
    {'User-Agent': 'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; Trident/6.0)','Referer':'https://www.douban.com/'},
    {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:40.0) Gecko/20100101 Firefox/40.0','Referer':'https://www.douban.com/'},
    {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/44.0.2403.89 Chrome/44.0.2403.89 Safari/537.36','Referer':'https://www.douban.com/'}
    ]

movie_type = ['悬疑']
#,爱情'喜剧','动画','剧情','科幻','动作','经典','悬疑','青春','犯罪','惊悚','文艺','搞笑','励志','恐怖','战争','短片'


def askUrl(url):
	old_url = url
	request = urllib2.Request(url,headers=random.choice(headers))
	try:
		response = urllib2.urlopen(request)
		print ("------------------old_url:",old_url)
		print ("------------------new_url:",response.geturl())
		html = response.read()
		
	except urllib2.URLError,e:
		if hasattr(e,"code"):
			print e.code
		if hasattr(e,"reason"):
			print e.reason
	return html

def get_Movielist(baseurl):
	movie_list = []
	pattern_movielink = re.compile(r'<a class="" href="(.+)">')
	pattern_moviename = re.compile(r'<span style="font-size:12px;">(.+)</span>')
	type = sys.getfilesystemencoding()
	middleurl = "?start="
	endurl="&type=T"
	for type_movie in movie_type:
		#used to choose different types
		for index in range(0,400,20):
			print ("page_index:",index)
			print(baseurl+str(type_movie)+middleurl+str(index)+endurl)
			html = askUrl(baseurl+str(type_movie)+middleurl+str(index)+endurl)
			#print html
			#html_content = html.decode("utf8").encode(type)
			soup = BeautifulSoup(html)
			for item in soup.find_all('tr',class_="item"):
				data = []
				item = str(item)
				#print item
				if re.findall(pattern_moviename,item):
					movie_name = re.findall(pattern_moviename,item)[0]#ATTENTION: NEED TO MAKE TWO CONTIONAS TOGETHER
				else:
					movie_name = "empty"
				data.append(movie_name)
				if re.findall(pattern_movielink,item):
					movie_link = re.findall(pattern_movielink,item)[0]
				else:
					movie_link = "empty"
				#print movie_link
				data.append(movie_link)
				movie_list.append(data)
				time.sleep(2)
	return movie_list



def getData(baseurl):
	datalist = []
	pattern_rating = re.compile(r'<span class="allstar(.+) rating" title="(.+)"></span>')
	pattern_comment = re.compile(r'<p class="">(.+)</p>',re.S)
	type = sys.getfilesystemencoding()
	endurl1 = "&limit=20&sort=new_score"
	for index in range(0,220,20):
		#used to change the page start=0 and gape=20
		print ("index",index)
		html = askUrl(baseurl+str(index)+endurl1)
		html_content = html.decode("utf8").encode(type)
		soup = BeautifulSoup(html)
		for item in soup.find_all('div',class_='comment'):
			data=[]
			item = str(item)#turn to string 
			#print ("item-----------",item)
			if re.findall(pattern_rating,item):
				star = re.findall(pattern_rating,item)[0]
			else:
				star = "empty"
			#print ("star-----------",star)
			data.append(star)
			if re.findall(pattern_comment,item):
				comment = re.findall(pattern_comment,item)[0]
			else:
				comment = "empty"
			#print type(comment)
			data.append(comment)
			#print ("comment-------",comment)

			datalist.append(data)
			#print ("data----------",data)
	return datalist

	#return datalist
"""
next step: we have already get the whole paragraph comment-item, then we need to use re.() to get the detail of comment
"""

def get_permovie_comment(baseurl):
	datalist = []

	pattern_moviename = re.compile(r'<span style="font-size:12px;">(.+)</span>')
	pattern_rating = re.compile(r'<span class="allstar(.+) rating" title="(.+)"></span>')
	pattern_comment = re.compile(r'<p class="">(.+)</p>',re.S)
	pattern_movielink = re.compile(r'<a class="" href="(.+)">')

	progress = 1

	type = sys.getfilesystemencoding()
	for type_movie in movie_type:#each type get the each movie information ;Eg: type is "Romantic"
		progress += 1
		for index in range(0,300,20):
			middleurl = "?start="
			endurl="&type=T"
			#the first page of Romantic type is 0
			print ("page index:",index)
			#print(baseurl+str(type_movie)+middleurl+str(index)+endurl)# https://movie.douban.com/tag/爱情?start=0&type=T
			html = askUrl(baseurl+str(type_movie)+middleurl+str(index)+endurl)
			soup = BeautifulSoup(html)#get the html code of the movie list which in the romantic type
			for item in soup.find_all('tr',class_="item"):
				#find the each movie name and link in this page
				data = []#used to store the data as the temp list
				data_output = []
				item = str(item)
				#print item
				if re.findall(pattern_moviename,item):
					movie_name = re.findall(pattern_moviename,item)[0]#ATTENTION: NEED TO MAKE TWO CONTIONAS TOGETHER
				else:
					movie_name = "empty"
				data.append(movie_name)
				if re.findall(pattern_movielink,item):
					movie_link = re.findall(pattern_movielink,item)[0]
				else:
					movie_link = "empty"
				data.append(movie_link)
				#print ("data list name:",data)
				#print data[0]
				#if the link is empty, then the whol list should be empty
				if movie_link != "empty":
					url_page = str(movie_link)+"comments?start="
					endurl1 = "&limit=20&sort=new_score"
					for item_comment in range(0,200,20):
						html_comment = askUrl(url_page+str(item_comment)+endurl1)
						soup = BeautifulSoup(html_comment)
						for moive_comment in soup.find_all('div',class_='comment'):
							data_output_tempo = []
							data_output_tempo.append(data[0])# store the movie name and link for each comment
							#print ("movie name :-----------",data[0])
							data_output_tempo.append(data[1])
							#print ("movie link :-----------",data[1])
							moive_comment = str(moive_comment)
							if re.findall(pattern_rating,moive_comment):
								star = re.findall(pattern_rating,moive_comment)[0]
							else:
								star = "empty"
							data_output_tempo.append(star)

							if re.findall(pattern_comment,moive_comment):
								comment = re.findall(pattern_comment,moive_comment)[0]
							else:
								comment = "empty"
							data_output_tempo.append(comment)
							#print ("----------------movie comment:"+moive_comment)
							datalist.append(data_output_tempo)
							#print data_output
						
					time.sleep(1)
				else:
					#think of every data should be empty when the link is empty
					star = "empty"
					comment = "empty"
					data_output.append(data[0])
					data_output.append(data[1])
					data_output.append(star)
					data_output.append(comment)
					datalist.append(data_output)
					time.sleep(1)

				# the comment of data part
				
			
		print("finished %d types movie"%progress)
	return datalist



def saveData(datalist,savePath):
	book = xlwt.Workbook(encoding='utf-8',style_compression = 0)
	sheet = book.add_sheet('Douban Movie Rating Data',cell_overwrite_ok=True)
	#col=('Rating_Star','Comment_content')
	col=('Movie Name','Movie Link','Movie_Rating','Movie Comment')
	for i in range(0,4):
		sheet.write(0,i,col[i])
	for i in range(0,len(datalist)):
		data = datalist[i]
		print data
		for j in range(0,4):
			sheet.write(i+1,j,data[j])
	book.save(savePath)



def main():
	"""url="https://movie.douban.com/subject/26322792/comments?start="
	datalist = getData(url)
	savepath="Movie_Rating.csv"
	saveData(datalist,savepath)
""
	url = "https://movie.douban.com/tag/"
	get_Movielist(url)
	datalist = get_Movielist(url)
	savepath="Movie_link.csv"
	saveData(datalist,savepath)
	
"""
	url = "https://movie.douban.com/tag/"
	datalist = get_permovie_comment(url)
	savepath="Movie_comment8.csv"
	saveData(datalist,savepath)
	

main()






















































