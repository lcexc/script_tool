#coding=utf-8
import datetime
import re
import requests as R
import config as conf

class Stu(object):

    def __init__(self, xh, passwd):
        self.session = None
        self.name = None
        self.xh = xh
        self.passwd = passwd
        self.is_login = None
        self.headers = conf.HDS


    def login(self):
        self.session = R.Session()
        datas = conf.USER_DATE
        datas['barcode'] = 's'+self.xh # 读者编号是学号前加s
        datas['password'] = self.passwd
        res = None
        try:
            res =  self.session.post(conf.login_u, headers = self.headers, data=datas)
        except Exception, e:
            print("longin failed.")
        if res and res.status_code == 200 and res.content == 'ok':
            self.is_login = 1
        return self.is_login


    def get_name(self):
        '''
        获取用户名
        '''
        if not self.is_login: #未登录
            self.login()
        if self.name: #已经获取过就不用再获取了
            return self.name
        res = None
        try:
            res =  self.session.get(conf.info_u, headers = self.headers)
            content = res.content.decode('gbk')
            info_list = conf.UINFO_RE.findall(content)
            if len(info_list) > 3:
                self.name = info_list[1][3:]
        except Exception, e:
            print("get user name failed.")
        return self.name

    def get_book_list(self):
        '''获取已借书列表'''
        if not self.is_login: #未登录
            self.login()
        jy_list = None
        book_info = {}
        try:
            res =  self.session.get(conf.jyinfo_u, headers = self.headers)
            content = res.content.decode('gbk')
            jy_list = conf.JS_RE.findall(content)
            xj_info = conf.XJ_RE.findall(content)
            for b in xj_info:
                book_info[b[0]] = [b[1], b[2]]

            for book in jy_list:
                print "书名:", book[0], "编号:", book[1], "书库:", book[2],
                print "到期时间:", book[4]

        except Exception, e:
            print(e)
            print("get list failed.")


if __name__ == '__main__':
    s = Stu("学号", "密码")
    #print s.login()

    print s.get_name()

    s.get_book_list()





