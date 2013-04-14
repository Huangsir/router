import web, os
import config
from subprocess import call
import sqlite3

class Thunder:
    def __init__(self, addr):
        self.addr = addr
    
    def Start(self):
        conn = sqlite3.connect(config.DB_PATH)
        c = conn.cursor()
        task = {"id":None, "name":None, "addr":None, "type":None, "status":None}
        for r in c.execute('SELECT * FROM `thunder_task` WHERE `status` = 1 LIMIT 1;'):
            c.execute('UPDATE `thunder_task` SET STATUS = 2 WHERE `id` = %s;' % r[0])
            task.id = r[0]
            task.name = r[1]
            task.addr = r[2]
            task.type = r[3]
            task.status = r[4]
            break


