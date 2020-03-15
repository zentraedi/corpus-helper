#!/bin/bash

export LC_ALL=en_US.utf8
export LANG=en_US.utf8
export FLASK_APP=run.py
export FLASK_DEBUG=1
flask run --host=0.0.0.0
