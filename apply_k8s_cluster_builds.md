## kubernetes yaml configuration

apiVersion: v1
kind: Deployment
metadata:
  name: hour_minute
spec:
  containers:
    - name: container-1
      image: gcr.io/cerc2-gestop-stg/hour-minute-test:v0.1.0
  restartPolicy: Never

## cloud build yaml steps
  steps:
- name: "gcr.io/cloud-builders/gke-deploy"
  args:
  - run
  - --filename=pod_config.yaml
  - --location=southamerica-east1
  - --cluster=gestop-stg-gke-01
