#-*-coding:utf-8-*-
import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )
from  crawl.crawl import *
from  crawl.filter import *
import MySQLdb
import time

#获取html 页面所需要的内容
def get_nashangban_content(url):
	html =  get_html(url)
	soup =  BeautifulSoup( html )
	job  =  {}
	job_detail = soup.findAll( "div" , attrs={'class':'nsb-block-content'} )
	job['content'] = filter_white(job_detail[0].get_text())
	job['title']   = soup.title.string
	return job

if __name__ == '__main__':

	#开始时间
	start_time = time.time()

	url    =  "https://www.nashangban.com/job_list?type=0"
	domain = "https://www.nashangban.com"
	reg = r"https://www.nashangban.com/jobs/[^\s]*" 
	urls = get_re_url_list( url , domain , reg )
	#print urls
	#print get_content("http://www.lagou.com/jobs/910244.html")

	conn = MySQLdb.connect(
			host='localhost',
			port=3306,
			user='root',
			passwd='',
			db='test',
			charset='utf8'
		)
	cur = conn.cursor()
	for url in urls:
		url = url.decode('utf-8')
		md5_url = md5(url)
		#先判断url是否存在
		sql_select = "select * from crawl_urls where md5 = %s "
		res_select = cur.execute( sql_select , md5_url )
		if res_select:
			print u"已经抓取"
		else:
			sql_insert = "insert into crawl_urls ( url , status , md5) values( %s,%s,%s )"
			result = cur.execute( sql_insert , ( url , 0 , md5_url ) )
			print u"插入 url 成功"
			job =  get_nashangban_content(url)
			print job['title']
			#插入爬取的职位内容
			sql_insert_job = " insert into crawl_contents( url , md5_url , title , content , time  ) values ( %s ,%s, %s, %s, %s ) "
			res_job        = cur.execute( sql_insert_job , ( url , md5_url , job['title'] , job['content'] , time.time() ) )
			#更新url池
			cur.execute( "update crawl_urls set status = 1 where md5 = %s " , (md5_url) )

			print u'插入职位成功'
	cur.close()
	conn.commit()
	conn.close()
	#结束时间
	end_time = time.time()
	time_diff = end_time - start_time
	print u'运行 %s  秒'%(time_diff)





