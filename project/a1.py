import threading
from queue import Queue

from attr import attrs, attrib


class ThreadBot(threading.Thread):
    def __init__(self):
        super().__init__(target=self.manage_table)
        self.cutlery = Cutlery(knives=0, forks=0)
        self.tasks = Queue()
    
    def manage_table(self):
        while True:
            task = self.tasks.get()
            if task == 'prepare':
                kitchen.give(to=self.cutlery, knives=4, forks=4)
            elif task == 'clear':
                self.cutlery.give(to=kitchen, knives=4, forks=4)
            elif task == 'shutdown':
                return

@attrs
class Cutlery:
    knives = attrib(default=0)
    forks = attrib(default=0)
    
    def give(self, to: 'Cutlery', knives=0, forks=0):
        self.change(-knives, -forks)
        to.change(knives, forks)
    
    def change(self, knives=0, forks=0):
        self.knives += knives
        self.forks += forks
    
kitchen = Cutlery(knives=100, forks=100)
bot = [ThreadBot() for _ in range(10000)]

for b in bot:
    for _ in range(10000):
        b.tasks.put('prepare')
        b.tasks.put('clear')
    b.tasks.put('shutdown')

print('Stan kuchni przed obsługą:', kitchen)
for b in bot:
    b.start()

for b in bot:
    b.join()
print('Stan kuchni po obsłudze:', kitchen)
