#!/bin/bash

./docker-build.sh
minikube start
kubectl apply -f kubernetes/deployment.yml
echo "Waiting for pods to come online"
pod=`kubectl get pods | grep "prime-weather" | awk '{print $1}'`
echo $pod

echo "Sleeping 5 seconds"
sleep 5

kubectl port-forward $(echo $pod) 5000