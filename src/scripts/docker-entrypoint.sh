#!/bin/bash

set -e

exec uvicorn app.main:app --host 127.0.0.1 --port 50
