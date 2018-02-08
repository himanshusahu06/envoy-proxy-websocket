#!/usr/bin/env bash
python3 /code/tornado-server.py ${SERVICE_NAME} websockets-4.0.1.tar.gz &
envoy -c /etc/service-envoy.yaml --service-cluster service${SERVICE_NAME}