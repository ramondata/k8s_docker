# k8s_docker

docker build -t hello-world-image:0.3.0 .

kubectl apply -f kub_config.yaml

kubectl get pods

kubectl get nodes

kubectl describe pod <pod-name>

kubectl delete -f kub_config.yaml

kubectl logs hellopwd --previous

Resources Kubernetes:
- pod: encapsula containers
- rs
- deploy
- vol
- hpa
- pv
- irg
- pvc
- svc
- sc
- ds
- quota

Cluster:
- master = control plane<api, etcd, scheduler, c-m>: gerencia o cluster
- node = <kubelet, k-proxy>: executa as aplicaçoes
