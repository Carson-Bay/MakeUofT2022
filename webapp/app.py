from flask import Flask, render_template, request
from multiprocessing import Process, Queue
# to import from parent directory
import os
import sys
import inspect
import threading


liquid_levels = Queue()
to_reset = Queue()
drink_requests = Queue()


currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir) 

import main

app = Flask(__name__)

@app.route('/')
def index():
    to_reset.put(["Carson"])
    result = []
    if liquid_levels.empty():
      result = [(1,75),(2,75),(3,75),(4,75)]
    else:
      for ind,num in enumerate(liquid_levels.get()):
       result.append((ind+1,num))
      # never have an empty queue; if no new data has come in, then repeat old data 
      if liquid_levels.empty():
        liquid_levels.put(result)
    return render_template('index2.html',result=result)


@app.route('/handle_data', methods=['POST'])
def handle_data():
    name = request.form['requester']
    print(name, "received")
    drink_requests.put(name)
    return index()

def apprun():
  app.run(debug=True, host='0.0.0.0')

if __name__ == '__main__':

    webapp = Process(target=apprun)
    webapp.start()

    hardware = Process(target=main, args=(liquid_levels,to_reset,drink_requests))
    hardware.start()
    
    # while True:
    #   print("HeLLO!!!!!")