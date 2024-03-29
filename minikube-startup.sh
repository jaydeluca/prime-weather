#!/bin/bash

./docker-build.sh

# Elasticsearch and fluent
kubectl create namespace logging
kubectl create -f kubernetes/elastic.yaml -n logging

kubectl create -f kubernetes/kibana.yaml -n logging

kubectl create -f kubernetes/fluentd-rbac.yaml

kubectl create -f kubernetes/fluentd-daemonset.yaml

#helm repo add elastic https://helm.elastic.co
#helm init
#helm install --name apm-server --version 7.9.2 elastic/apm-server

# Prime Weather App
kubectl apply -f kubernetes/deployment.yml

