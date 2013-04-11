# -*- coding: UTF-8 -*-
import web, json
from utils import view

class login:
    def GET(self):
        return view.Render('login')
    def POST(self):
        rsl = {"c":0, "m":"登录成功，正在跳转...", "goto":""}
        return json.dumps(rsl)
