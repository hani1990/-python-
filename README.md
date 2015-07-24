# -python-
crawl 目录下中的 filter.py 里面是一些过滤函数，主要是 通过黑名单(blacklist)过滤不要的 和 通过正则re 匹配对应的
                crawl.py 里面封装的是一些常用的方法，通过url 获取html , 获取html中的所有链接

代码其实很简单，是自己写的写一个小爬虫的demo , 里面的代码可以爬取，哪工作网里面的职位信息(只分出了标题，和职位内容)，因为之后是打算 
做全文索引的，所以没有太细分字段。
数据表，有两张，一张存放 urls 另一张存放爬取的内容，爬取到的url 通过md5运算一次，这样，下次爬取到某个链接的时候也是通过 md5运算之后与crawl_urls数据表里面的md5 字段里面的内容做对比，找到了就不用抓取，没有找到才抓取。

用到的第三方库
BeautifulSoup
MySQLdb

下面是安装方法

1. 安装 BeautifulSoup

方法一：

下载：http://www.crummy.com/software/BeautifulSoup/bs4/download/4.2/

解压：tar -xzvf beautifulsoup4-4.2.0.tar.gz

安装：进入解压后的目录

python setup.py build
sudo python setup.py install

方法二（快速安装）

(Ubuntu) sudo apt-get install python-bs4
或者
install beautifulsoup4
或着
easy_install beautifulsoup4


MySQLdb 安装
yum -y install mysql-dev
wget http://downloads.sourceforge.net/project/mysql-python/mysql-python-test/1.2.4b4/MySQL-python-1.2.4b4.tar.gz?r=http%3A%2F%2Fsourceforge.net%2Fprojects%2Fmysql-python%2F&ts=1364895531&use_mirror=nchc
 
tar zxvf  MySQL-python-1.2.4b4.tar.gz
cd MySQL-python-1.2.4b4
python setup.py build
python setup.py install

仅做为交流和学习。
