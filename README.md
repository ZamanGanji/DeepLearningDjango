# DeepLearningDjango
In this files I try to deploy the combination of the Django web application and deeplearning project implement by openCV for object detections.
The deployment is employed on Kubernetes and GCP



For deploy on localaised Docker at first create an images by 

docker build . -t django-face 


in cmd.

and after making ana image in Docker Deslktop write in cmd as

docker run -p 8001:8000 -it --rm django-face

# running on Kubernetes and GCP

create an account in google ang go to google cloud platform console.
Then in Cloud Shell Editor write 

gcloud builds submit --tag gcr.io/spheric-almanac-379120/django-face-gke .

for running application on docker based GCP excute this command on Cloud Shell

gcloud container clusters create django-face-gke-clusters \
    --num-nodes 1 \
    --enable-basic-auth \
    --issue-client-certificates \
    --zone us-central1-a

for applynig the Kubernetes on GCP type the following commands on Cloud Shell Editor

kubectl apply -f deployment.yaml

and

kubectl apply -f services.yaml


finally the external id for LoadBalancer can be used as main IP for runing the apllication.


