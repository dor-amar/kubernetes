# Deploying a Kubernetes Pod

Follow these steps to create and deploy a pod.

### Step 1: Create the Pod Definition

Save the following YAML configuration to a file:

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: pod-with-env
spec:
  containers:
  - name: my-app
    image: nginx
    env:
    - name: MY_ENV_VAR
      value: "Hello, Kubernetes!"
    ports:
    - containerPort: 80
```

### Step 2: Apply the Pod Definition
Use kubectl to apply the pod definition and create the pod in your Kubernetes cluster:

```sh
kubectl apply -f pod.yaml
```

### Step 3: Verify the Pod is Running
Check the status of the pod to ensure it’s running:

```sh
kubectl get pods
```