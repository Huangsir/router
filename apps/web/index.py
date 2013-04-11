import web

render = web.template.render('templates/web/')

class index:
    def GET(self):
        return render.index('')
