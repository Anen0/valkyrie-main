#!/usr/bin/env python
from flaskapp import run_dammit

app = run_dammit()

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=6780, debug=True)