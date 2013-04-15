import web, os
import config
from jinja2 import Environment,FileSystemLoader

class Render:
    def __init__(self, path, **context):
        self.env = Environment(loader = FileSystemLoader(path), **context)
        self.ctx = {}

    def __getattr__(self, name):
        env = web.ctx.env
        env.update(self.ctx)
        env['action'] = name
        self.env.globals['Link'] = CoverLink
        self.env.globals.update({'env' : env})
        return self.env.get_template('%s.html' % name).render

def CoverLink(path):
    return "%s://%s/%s" % (web.ctx.env['wsgi.url_scheme'], web.ctx.env['HTTP_HOST'], path)
