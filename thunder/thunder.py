import os, threading, time
from model import ThunderTask

class Thunder:
    def __init__(self):
        self.run = False

    def Run(self):
        if not self.run:
            self.run = True
            threading.Thread(target = run_task, args = (), name = "run_task").start()


    def AddTask(self, task):
        ThunderTask.Add(task)
        self.Run()

#global
thunder = Thunder()

#global run_task thread
def run_task():
    for i in xrange(1000):
        print i
    thunder.run = False
