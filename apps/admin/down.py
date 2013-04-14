# -*- coding: UTF-8 -*-
import web
import threading, os, json, re, md5
from utils import view, config, task

render = view.render
Thunder = task.Thunder

class Downloading:
    def GET(self):
        return render.downloading()

class NewTask:
    def GET(self):
        return render.new_task()
    def POST(self):
        i = web.input(addr={}, type=None, torfile={})
        if i.type == 'normal_url':
            task = Thunder(addr=i.addr)
            task.Start()
        elif i.type == 'torrent_url':
            print i
        elif i.type == 'torrent_file':
            print i
        return json.dumps({"c":0})

#Ajax
class Query:
    def GET(self):
        t = web.input(type = None)
        tasks = []
        if t == 'downing':
            tasks += QueryDoingTask()
        elif t == 'done':
            tasks += QueryDoneTask()
        else:
            tasks += QueryDoingTask()
            tasks += QueryDoneTask()
        return json.dumps(tasks)


def QueryDoingTask():
    tasks = []
    for filename in os.listdir(config.THUNDER_DOING_TASK):
        filepath = os.path.join(config.THUNDER_DOING_TASK, filename)
        fp = open(filepath, 'r')
        content = fp.read()
        fp.close()
        pattern = '\s*(\d+K|M|G)((\s+(.){10}){5}\s+)(\d+)%\s+([0-9]*\.?[0-9]+(K|M|G))\s+(.+)'
        match = re.findall(pattern, content)
        if match:
            match = match[-1]
            info = {
                "taskid" : md5.new(filename).hexdigest(),
                "name" : filename,
                "downed" : match[0],
                "progres" : match[4] + '%',
                "speed" : match[5],
                "runtime" : match[7],
                "type" : "doing",
            }
            tasks.append(info)
    return tasks

def QueryDoneTask():
    tasks = []
    for filename in os.listdir(config.THUNDER_DONE_TASK):
        tasks.append({"name" : filename, "type" : "done"})
    return tasks

