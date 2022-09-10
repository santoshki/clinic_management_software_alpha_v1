import datetime

from flask import request, render_template, Flask

#app = Flask(__name__)
import calendar

import time
current_GMT = time.gmtime()
time_stamp = int((datetime.datetime.now() - datetime.datetime(1970,1,1)).total_seconds())
print("Time:", time_stamp)


#if __name__ == '__main__':
   # app.run(host='localhost', port=5000)