#coding=utf-8
import re

login_u  = "http://222.24.3.7:8080/opac_two/include/login_app.jsp"

info_u   = "http://222.24.3.7:8080/opac_two/reader/infoList.jsp" #个人信息
jyinfo_u = "http://222.24.3.7:8080/opac_two/reader/jieshuxinxi.jsp" #借书信息
jyhis_u  = "http://222.24.3.7:8080/opac_two/reader/jieshulishi.jsp" #借阅历史

#个人信息 昵称,姓名,条码
UINFO_RE = re.compile(r'<div class="hiddenOverFlow">(.+)</div>')

#借书信息
JS_RE = re.compile(r'<td>(.+)&nbsp;</td><td>(\d+)&nbsp;</td><td>(.+)&nbsp;</td><td>(.+)&nbsp;</td><td>([/\d]+)&nbsp;</td>')

#续借
XJ_RE = re.compile(r'Renew\(\'(\d+)\',\'(.+)\',\'(.+)\'\);"')

HDS = {
    'Content-Type':"application/x-www-form-urlencoded",

    'Host': "222.24.3.7:8080",
    'Origin': "http://222.24.3.7:8080",
    'Referer': "http://222.24.3.7:8080/opac_two/reader/infoList.jsp",
    'User-Agent':"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.106 Safari/537.36"
}

USER_DATE = {
    'login_type': "barcode",
    'barcode': "",
    'password': ""
}

