from flask import Flask, render_template
from multiprocessing import Process, Queue

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
    l_levels = Queue()
    to_reset = Queu()
    
    webapp = Process(target=apprun, args=())
    webapp.start()

    hardware = Process(target=apprun, args=())
    hardware.start()
    
    # while True:
    #   print("HeLLO!!!!!")