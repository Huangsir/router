#!/usr/bin/python
import web
from apps.admin import view

urls = (
    '^/admin/login$',                'apps.admin.view.Login',

    '^/admin/index$',                'apps.admin.view.Default',

    '^/admin/downloading$',          'apps.admin.view.Downloading',
    '^/admin/downloading/query$',    'apps.admin.view.Query',

    '^/admin/new_task$',             'apps.admin.view.NewTask',
    '^/admin/$',                     'apps.admin.view.Default',

    '^/(.+)$',                       'apps.admin.view.Default',
    '^/$',                           'apps.admin.view.Default',
)

if __name__ == '__main__':
    app = web.application(urls, globals())
    app.run()

