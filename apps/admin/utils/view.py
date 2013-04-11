import web, os
import config
from jinja2 import Environment,FileSystemLoader

class Render:
    def __init__(self, path, **context):
        self.env = Environment(loader = FileSystemLoader(config.TEMPLATE_DIR),
                **context)

    def __getattr__(self, name):
        env = web.ctx.env
        env['action'] = name
        env['site_bar'] = config.SITE_BAR
        self.env.globals.update({'env' : env})
        return self.env.get_template('%s.html' % name).render

render = Render(config.TEMPLATE_DIR)

