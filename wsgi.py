#!/usr/bin/python
import web
from apps.admin import login

urls = (
    '^/admin/login$',                'apps.admin.login.login',

    '^/admin/index$',                'apps.admin.index.Default',

    '^/admin/downloading$',          'apps.admin.down.Downloading',
    '^/admin/downloading/query$',    'apps.admin.down.Query',

    '^/admin/new_task$',             'apps.admin.down.NewTask',
    '^/admin/$',                     'apps.admin.index.Default',

    '^/(.+)$',                       'apps.admin.index.Default',
    '^/$',                           'apps.admin.index.Default',
)

if __name__ == '__main__':
    app = web.application(urls, globals())
    app.run()

