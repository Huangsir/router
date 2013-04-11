# -*- coding: UTF-8 -*-
import web

class Index:
    def GET(self):
        return render.downloading()

class Default:
    def GET(self):
        return web.seeother('./admin/downloading')

