import ssl

__author__ = 'alonk'

__doc__ = """Usage: SteerData.py [--id <id>] [--filename <filename>]
# python SteerData.py --id 4E554F --filename lrnhack2.csv

Options:
    --id=<id> neurosteer device id
    --filename=<filename> file name to write
"""
import websocket
import csv
import json
import docopt
from datetime import datetime
from StringIO import StringIO
import thread
import time

ws = websocket.WebSocket()
device_id = ""
filename = ""
closing = False

class BrainWave:
    def __init__(self):
        pass

    def __init__(self, message):
        self.alpha = message['alpha']
        self.beta = message['beta']
        self.gamma = message['gamma']
        self.delta = message['delta']
        self.theta = message['theta']
        self.sigma = message['sigma']
        self.h1 = message['h1']
        self.h2 = message['h2']
        self.e1 = message['e1']
        self.e2 = message['e2']
        self.e3 = message['e3']
        self.c1 = message['c1']
        self.c2 = message['c2']
        self.c3 = message['c3']
        self.time = datetime.utcnow()

    def to_row(self):
        return [self.time, self.alpha, self.beta, self.gamma, self.delta, self.theta, self.sigma, self.h1, self.h2, self.e1,
                self.e2, self.e3, self.c1, self.c2, self.c3]


def process_message(message):
    try:
        io = StringIO(message)
        j = json.load(io)
        # print str(j)
        print j
        feat = j["features"]
        print str(feat)
        br = BrainWave(feat)
        write_message(br)

    finally:
        pass


def on_message(socket, message):
    print "Message" + message
    if message is not None and message != "{}":
        process_message(message)


def on_error(socket, error):
    print "ERROR!"
    print error
    init_socket(socket)


def on_close(socket):
    print "### closed ###"
    if not closing:
        init_socket(socket)


def on_open(socket):
    print "Socket opened"


def init_socket(socket):
    socket_path = "ws://cloud.neurosteer.com:8080/v1/features/000666" + device_id + "/pull" # "4e5401"
    print socket_path
    websocket.enableTrace(True)
    socket = websocket.WebSocketApp(socket_path,
                                    on_message=on_message,
                                    on_error=on_error,
                                    on_close=on_close, on_open=on_open,
                                    )
    print "running ..."

    socket.run_forever()
    #socket.keep_running = True
    return socket


def write_message(message):
    row = message.to_row()
    #print '****   \t ' + str(row)
    writer.writerow(row)
    fileout.flush()


def cancel_thread():
    x = raw_input("Press enter to terminate")
    print x

    ws.keep_running = False
    ws.close()
    #fileout.flush()
    #fileout.close()



if __name__ == "__main__":
    arguments = docopt.docopt(__doc__)
    closing = False
    device_id = arguments.get('--id')
    filename = arguments.get('--filename')
    fileout = open(filename, 'ab')
    writer = csv.writer(fileout)
    print "File columns are: time(utc), alpha, beta, gamma, delta, theta, sigma, h1, h2, e1, e2, e3, c1, c2, c3"


    print "Using device id: " + device_id
    print "Output to file: " + filename
    thread.start_new_thread(cancel_thread, ())
    ws = init_socket(ws)
    #msg = "{u'features': {u'alpha': 1, u'h2': 2, u'sigma': 3, u'h1': 4, u'c2': 5, u'beta': 6, u'gamma': 7, u'delta': 8, u'c3': 9, u'theta': 10, u'c1': 11, u'e1': 12, u'e3': 13, u'e2': 14}}".replace("'", '"').replace('u"', '"')
    #process_message(msg)
    while not closing:
        pass




