import os
from model import ThunderTask

class Thunder:
    def AddTask(self, task):
        r = ThunderTask.Query().filter_by(addr = task.addr).all()
        if not r:
            ThunderTask.Add(task)

#global
thunder = Thunder()
