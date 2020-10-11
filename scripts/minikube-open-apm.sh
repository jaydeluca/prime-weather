#!/bin/bash
# Port forward to allow access to the the APM server on port 8200
pod=`kubectl get pods | grep "apm-server" | awk '{print $1}'`
echo $pod
kubectl port-forward $(echo $pod) 8200