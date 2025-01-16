from flask import Flask
import datetime
import math

server = Flask(__name__)

def generate_cpu_load():
    start = datetime.datetime.now()
    while True:
         a = math.sqrt(64*64*64*64*64)
         end = datetime.datetime.now()
         diff = end - start
         check = diff.microseconds / 1000
         # let's generete load for 100 ms
         if check > 100:
            return

@server.route("/")
def hello():
   generate_cpu_load()
   return "Hello World!"

if __name__ == "__main__":
   server.run(host='0.0.0.0', port=80)