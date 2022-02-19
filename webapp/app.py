from flask import Flask, render_template
from multiprocessing import Process, Queue
# to import from parent directory
import os
import sys
import inspect


liquid_levels = Queue()
to_reset = Queue()
drink_requests = Queue()


currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir) 

# import main

app = Flask(__name__)

@app.route('/')
def index():
    to_reset.put(["Carson"])
    result = []
    if liquid_levels.empty():
      result = ()
    else:
      for ind,num in enumerate(liquid_levels.get()):
        result[str(ind+1)] = num
    return render_template('index.html',result=result)

@app.route('/cakes')
def cakes():
    return 'Yummy cakes!'

def apprun():
  app.run(debug=True, host='0.0.0.0')

if __name__ == '__main__':

    
    webapp = Process(target=apprun)
    webapp.start()

    # hardware = Process(target=main, args=(liquid_levels,to_reset,drink_requests))
    # hardware.start()
    
    # while True:
    #   print("HeLLO!!!!!")