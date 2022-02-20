from flask import Flask, render_template, request
from multiprocessing import Process, Queue
# to import from parent directory
import os
import sys
import inspect
import threading


liquid_levels = Queue()
to_reset = Queue()
drink_requests = []


currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir) 

# import main

app = Flask(__name__)

@app.route('/')
def index():
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

@app.route('/requested')
def requested():
    result = []
    if liquid_levels.empty():
      result = [(1,75),(2,75),(3,75),(4,75)]
    else:
      for ind,num in enumerate(liquid_levels.get()):
       result.append((ind+1,num))
      # never have an empty queue; if no new data has come in, then repeat old data 
      if liquid_levels.empty():
        liquid_levels.put(result)
    return render_template('requested.html',names=drink_requests, result=result)

@app.route('/request_sent')
def request_sent():
    result = []
    if liquid_levels.empty():
      result = [(1,75),(2,75),(3,75),(4,75)]
    else:
      for ind,num in enumerate(liquid_levels.get()):
       result.append((ind+1,num))
      # never have an empty queue; if no new data has come in, then repeat old data 
      if liquid_levels.empty():
        liquid_levels.put(result)
    return render_template('request_sent.html',result=result)

@app.route('/handle_data', methods=['POST','GET'])
def handle_data():
  if request.method == 'POST':
    name = request.form['requester']
    print(request.form)
    print(name, "received")
    if name not in drink_requests:
      drink_requests.append(name)
  return request_sent()


@app.route('/reset_button', methods=['POST','GET'])
def reset_button():
  if request.method == 'POST':
    pump_to_reset = request.form['reset-button']
    to_reset.put(pump_to_reset)
    print("RESET BUTTON", pump_to_reset)
  return requested()

@app.route('/reset_drinks', methods=['POST','GET'])
def reset_drinks():
  if request.method == 'POST':
    name = request.form['remove-name']
    if name in drink_requests:
      drink_requests.remove(name)
  return requested()


def apprun():
  app.run(debug=True, host='0.0.0.0')

if __name__ == '__main__':

    webapp = Process(target=apprun)
    webapp.start()

    # hardware = Process(target=main, args=(liquid_levels,to_reset,drink_requests))
    # hardware.start()
    
    # while True:
    #   print("HeLLO!!!!!")