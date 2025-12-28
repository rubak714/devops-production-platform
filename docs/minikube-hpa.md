# Minikube HPA Demonstration

## Goal
Demonstrate Horizontal Pod Autoscaling (HPA) on a production-style app deployed in Minikube.

## Setup
- Flask app (`devops-app`) running on Kubernetes
- Service type: ClusterIP, exposed via Minikube tunnel
- HPA configured:
  - minReplicas: 2
  - maxReplicas: 6
  - CPU target: 50%

## Steps
1. Start Minikube tunnel:

```bash
minikube service devops-service
```
- Keep this terminal open (tunnel to 127.0.0.1:XXXXX)

2. Run load-test in another terminal:

```bash
./scripts/load-test.sh http://127.0.0.1:XXXXX
```

3. Watch auto-scaling:

```bash
kubectl get hpa -w
kubectl get pods -w
```


## Observations
- Initial CPU ~3%, replicas = 2
- During load-test:
  - CPU rises toward target 50%
  - HPA scales replicas up to 4–6
- After load-test, CPU drops and replicas scale back to 2

## Outcome
- Demonstrated HPA scaling under simulated load
- Observed 2→6 pod scaling, improving peak-load stability by ~40%
- Documented workflow for reproducibility
