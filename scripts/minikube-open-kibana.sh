#!/bin/bash
 Port forward to allow access to the Kibana on port 5601
pod=`kubectl -n logging get pods | grep "kibana" | awk '{print $1}'`
echo $pod
kubectl -n logging port-forward $(echo $pod) 5601
