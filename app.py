
"""
import os
from bottle import route, run

@route('/hello/:name')
def index(name='World'):
    return '<b>Hello %s!</b>' % name


if __name__ == '__main__':
    # Get required port, default to 5000.
    port = os.environ.get('PORT', 5000)

    # Run the app.
    run(host='0.0.0.0', port=port)
""""

import os
port = int(os.environ.get('PORT', 17995))

a=1+1
b=2+2
a+b
