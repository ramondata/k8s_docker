# k8s_docker

docker build -t hello-world-image:0.3.0 .

kubectl apply -f kub_config.yaml

kubectl get pods

kubectl describe pod <pod-name>

kubectl delete -f kub_config.yaml

kubectl logs hellopwd --previous
