#-*-coding:utf-8-*-
import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )
from bs4 import BeautifulSoup
import urllib2
from  filter import *

#通过url 获取html
def get_html(url):
	page = urllib2.urlopen(url , timeout=10)
	html = page.read()
	return html


#通过url获取html 再从html里面 过滤blacklist 中的url获取需要的url 链接
def get_filter_url_list(url , domain):
	html = get_html(url)
	soup = BeautifulSoup(html)
	#遍历所有链接 href
	urls = []
	for link in soup.find_all('a'):
		href = link.get('href')
		if  "http" not in href : # 没有http 的链接 加上 域名地址
			url = domain+href
		urls.append( url )
	filter_urls = filter( in_lists , urls )
		
	return filter_urls

#采用正则匹配的方式匹配url
def get_re_url_list( url , domain , reg ):
	html = get_html(url)
	soup = BeautifulSoup(html)
	#遍历所有链接 href
	urls = []
	for link in soup.find_all('a'):
		href = link.get('href')
		if  "http" not in href :
			url = domain+href
		urls.append( url )

	re_urls = []
	#正则匹配
	pattern = re.compile( reg )
	for u in urls:
		match = pattern.match(u)
		if match:
			re_urls.append(u)
		
	return re_urls


#获取html 页面所需要的内容
def get_content(url):
	html =  get_html(url)
	soup =  BeautifulSoup( html )
	#print soup.title.string
	job_detail = soup.findAll( "div" , attrs={'class':'content_l'} )
	job = job_detail[0].get_text()
	return filter_tags(job)

#md5 加密
def md5(str):
    import hashlib
    m = hashlib.md5()   
    m.update(str)
    return m.hexdigest()