from flask import Flask, render_template
from multiprocessing import Process, Queue
# to import from parent directory
import os
import sys
import inspect

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir) 

import main

# def f(q):
#   count = 0
#   while True:
#     count+=1
#     q.put([count])
#     sleep(1)

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/cakes')
def cakes():
    return 'Yummy cakes!'

def apprun():
  app.run(debug=True, host='0.0.0.0')

if __name__ == '__main__':
    liquid_levels = Queue()
    to_reset = Queue()
    drink_requests = Queue()
    
    webapp = Process(target=apprun, args=(liquid_levels,to_reset,drink_requests))
    webapp.start()

    hardware = Process(target=main, args=(liquid_levels,to_reset,drink_requests))
    hardware.start()
    
    # while True:
    #   print("HeLLO!!!!!")