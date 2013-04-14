TEMPLATE_DIR = './templates/admin'

THUNDER_ROOT = './thunder'
THUNDER_DOING_TASK = THUNDER_ROOT + '/task/doing'
THUNDER_DONE_TASK = THUNDER_ROOT + '/task/done'

DB_PATH = './static/db/router.sqlite'

TASK_TYPE_NORMAL_URL = 1
TASK_TYPE_TORRRENT_URL = 2
TASK_TYPE_TORRRENT_FILE = 3

TASK_TYPE_INIT = 1
TASK_TYPE_ING = 2
TASK_TYPE_DONE = 3

SITE_BAR = {
    "Thunder" : {
        "downloading" : {
            "href" : "downloading",
            "name" : "Downloading",
        },
        "new_task" : {
            "href" : "new_task",
            "name" : "New Task",
        },
    }
}
