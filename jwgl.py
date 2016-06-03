#-*- coding:gbk -*-

import urllib2
import cookielib
import urllib
import re

def getVIEW(Page):
    view = r'name="__VIEWSTATE" value="(.+)" '
    view = re.compile(view)
    return view.findall(Page)[0]

def main():
    ID = raw_input('Please Input the Scoolar_Num:')
    paswd= raw_input('Please Input the password')
    loginURL = 'http://jwgl.gdut.edu.cn/default2.aspx'
    checkURL = 'http://jwgl.gdut.edu.cn/CheckCode.aspx'
    cookie = cookielib.CookieJar()
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
    
#    ID = '3114006174'
 #   paswd = 'a88482131'
    
    start_headers = {
        'Host':'jwgl.gdut.edu.cn',
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:46.0) Gecko/20100101 Firefox/46.0',
        'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language':'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
        'Accept-Encoding':'gzip, deflate',
        'Connection':'keep-alive',
    }

    getImage_headers = {
        'Host':'jwgl.gdut.edu.cn',
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:46.0) Gecko/20100101 Firefox/46.0',
        'Accept':'image/png,image/*;q=0.8,*/*;q=0.5',
        'Accept-Language':'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
        'Accept-Encoding':'gzip, deflate',
        'Referer':'http://jwgl.gdut.edu.cn/default5.aspx',
        'Connection':'keep-alive',
    }        
    
    upload_headers = {
        'Host':'jwgl.gdut.edu.cn',
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:46.0) Gecko/20100101 Firefox/46.0',
        'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language':'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
        'Accept-Encoding':'gzip, deflate',
        'Referer':'http://jwgl.gdut.edu.cn/default5.aspx',
        'Connection':'keep-alive',
        'Content-Type':'application/x-www-form-urlencoded'
    }
    
    start_request = urllib2.Request(url = loginURL,headers = start_headers)
    start_receive = opener.open(start_request)
    start_page  = start_receive.read().decode('gbk')
    
    check_request = urllib2.Request(url = checkURL,headers = getImage_headers)
    check_receive = opener.open(check_request)
    check_content = check_receive.read()
    f = open('checkcode','wb')
    f.write(check_content)
    f.close()
    checkcode_num = raw_input('Input the CheckCode:')
    
    data ={
        '__VIEWSTATE':getVIEW(start_page),
        'txtUserName':ID,
        'TextBox2':paswd,
        'txtSecretCode':str(checkcode_num),
        'RadioButtonList1':u'学生'.encode('gb2312'),
        'Button1':'',
        'lbLanguage':'',
        'hidPdrs':'',
        'hidsc':''        
    }
    postdata = urllib.urlencode(data)
    
    upload_request = urllib2.Request(url = loginURL,data = postdata,headers = upload_headers)
    upload_receive = opener.open(upload_request)
    upload_content = upload_receive.read().decode('gbk')
    
    print upload_content
    print upload_receive.code
#    for i in postdata:
#        print i,


if __name__ == '__main__':
    main()
    print u'学生'.encode('gb2312')
