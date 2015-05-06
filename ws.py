#!/usr/bin/env python
# coding: utf-8
# Copyright (c) 2014
# Gmail:liuzheng712
#

import tornado.web
import tornado.ioloop
import tornado.websocket
import os,sys
import subprocess
import time
import StringIO

class Index(tornado.web.RequestHandler):
    def get(self):
        self.render('./static/index.html')

class SocketHandler(tornado.websocket.WebSocketHandler):
    waiters = set()
    cache = []
    cache_size = 300
    def allow_draft76(self):
# for iOS 5.0 Safari
        return True
    def check_origin(self, origin):
        return True
    def open(self):
        print "open socket"
    def on_close(self):
        print "close socket"
    def on_message(self,e):
        command = e
        print command
        #stdout = sys.stdout
        #sys.stdout = file = StringIO.StringIO()

        child = subprocess.Popen(command,shell=True,
                stdout=subprocess.PIPE,bufsize=0)
       # self.write_message(file.getvalue())
       # for nextline in iter(child.stdout.readline, b''):
       #     self.write_message("[ "+time.strftime('%Y-%m-%d %H:%M:%S',time.localtime())+"] "+nextline)
       # child.stdout.close()
       # child.wait()
        while True:
            nextline = child.stdout.readline()
            if nextline.strip() == "" and child.poll() != None:
                break
            self.write_message("[ "+time.strftime('%Y-%m-%d %H:%M:%S',time.localtime())+"] "+nextline)

if __name__ == '__main__':
    app = tornado.web.Application([
        ('/',Index),
        ('/ws', SocketHandler),
        ])
    app.listen(8001)
    tornado.ioloop.IOLoop.instance().start()
