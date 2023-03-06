## DeepLearningDjango

In these files, I try to deploy the combination of the Django web application and deep learning project implemented by openCV for object detection.
The deployment is employed on Kubernetes and GCP.



For deployment on localized Docker, first, create an image by 
```bash
docker build . -t django-face 
```

And after making an image in Docker Desktop, write in cmd as

```bash
docker run -p 8001:8000 -it --rm django-face
```
## Running on Kubernetes and GCP

Create an account in google and go to the google cloud platform console.
Then in Cloud Shell Editor, write 

```bash
gcloud builds submit --tag gcr.io/spheric-almanac-379120/django-face-gke .
```
For running applications on Docker-based GCP, execute this command on Cloud Shell

```bash
gcloud container clusters create django-face-gke-clusters \
    --num-nodes 1 \
    --enable-basic-auth \
    --issue-client-certificates \
    --zone us-central1-a
```
For applying the Kubernetes on GCP, type the following commands on Cloud Shell Editor

```bash
kubectl apply -f deployment.yaml
```
and then

```bash
kubectl apply -f services.yaml
```

Finally, the external id for LoadBalancer can be used as the primary IP for running the application.