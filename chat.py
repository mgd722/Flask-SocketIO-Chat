#!/bin/env python
import eventlet
print('monkey patching python for websockets...')
eventlet.monkey_patch()

from app import create_app, socketio

app = create_app(debug=True)

if __name__ == '__main__':
    socketio.run(app)
