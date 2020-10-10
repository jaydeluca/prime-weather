#!/bin/bash
# Port forward to allow access to the API on port 5000
pod=`kubectl get pods | grep "prime-weather" | awk '{print $1}'`
echo $pod
kubectl port-forward $(echo $pod) 5000