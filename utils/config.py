import os

#root path
ROOT_PATH = os.getcwd()

#applications path
APPS_PATH = os.path.join(ROOT_PATH, 'apps')

#templates path
TEMPLATES_PATH = os.path.join(ROOT_PATH, 'templates')

#static file path
STATIC_PATH = os.path.join(ROOT_PATH, 'static')

#utils path
UTILS_PATH = os.path.join(ROOT_PATH, 'utils')

#database
DB_PATH = os.path.join(STATIC_PATH, 'db', 'router.db')

#thunder
THUNDER_TORRRENT_PATH = "/jffs/mnt/"
THUNDER_DOWNLOAD_PATH = "/jffs/mnt/TDDOWNLOAD/"
THUNDER_TASK_PATH = os.path.join(ROOT_PATH, 'thunder', 'task')
THUNDER_DOING_TASK = os.path.join(THUNDER_TASK_PATH, 'doing')
THUNDER_DONE_TASK = os.path.join(THUNDER_TASK_PATH, 'done')
#Type
THUNDER_TYPE_NORMAL_URL = "1"
THUNDER_TYPE_TORRRENT_URL = "2"
THUNDER_TYPE_TORRRENT_FILE = "3"
#Status
THUNDER_TASK_TYPE_INIT = "1"
THUNDER_TASK_TYPE_ING = "2"
THUNDER_TASK_TYPE_DONE = "3"
