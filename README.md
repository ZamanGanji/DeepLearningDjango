## DeepLearningDjango

In these files, I have meticulously worked on deploying an innovative solution that combines the power of a Django web application with a cutting-edge deep learning project implemented using OpenCV for highly accurate object detection. This unique fusion of technologies allows for seamless integration and provides an exceptional user experience.

To ensure optimal scalability and performance, we have chosen to deploy this solution on Kubernetes, a robust container orchestration platform. Kubernetes offers advanced features such as auto-scaling, load balancing, and efficient resource allocation, enabling our application to handle increasing user demands with ease.

Moreover, by leveraging the capabilities of Google Cloud Platform (GCP), we have achieved a high level of reliability, security, and flexibility in our deployment. GCP's infrastructure and services provide a solid foundation for our solution, ensuring uninterrupted operation and efficient utilization of resources.

Throughout the deployment process, careful attention has been paid to guarantee the solution's extendability. The modular architecture allows for easy integration of additional functionalities or future updates, enabling the application to adapt to evolving business requirements effortlessly.

To ensure smooth operation, we have implemented comprehensive monitoring and logging mechanisms. This allows us to track performance metrics, detect potential issues, and proactively address them, ensuring a stable and reliable deployment.

In conclusion, the successful deployment of this Django web application and OpenCV-based deep learning project on Kubernetes and GCP showcases our commitment to delivering a state-of-the-art solution that is both scalable and flexible. We are excited to witness the positive impact this deployment will have on enhancing object detection capabilities and providing an exceptional user experience.

To deploy the application on a localized Docker environment, follow these steps to create an image:

1. Set up a Dockerfile: Create a file called "Dockerfile" (with no file extension) in the root directory of your project. This file will define the steps needed to build your Docker image.

2. Specify the base image: In the Dockerfile, start by specifying the base image you want to use. For example, if you are working with Python, you can use the official Python base image. Add the following line at the beginning of your Dockerfile:
   ```
   FROM python:3.9
   ```

3. Copy project files: Next, copy your project files into the Docker image. Use the `COPY` command in your Dockerfile to copy the necessary files and directories from your local machine to the image. For example, if your project files are in the current directory, add the following line to your Dockerfile:
   ```
   COPY . /app
   ```

4. Install dependencies: If your project requires any dependencies, add the necessary commands to install them. Typically, you would use the `RUN` command in your Dockerfile to execute shell commands. For example, if you have a `requirements.txt` file listing your Python dependencies, add the following lines to your Dockerfile:
   ```
   WORKDIR /app
   RUN pip install -r requirements.txt
   ```

5. Expose necessary ports: If your application requires specific ports to be exposed, use the `EXPOSE` command in your Dockerfile. For example, if your Django application runs on port 8000, add the following line to your Dockerfile:
   ```
   EXPOSE 8000
   ```

6. Define the entry point: Finally, specify the command that should be executed when the Docker container starts. This is typically the command to run your application. Use the `CMD` or `ENTRYPOINT` command in your Dockerfile. For example, if your Django application uses `manage.py` to start the server, add the following line:
   ```
   CMD python manage.py runserver 0.0.0.0:8000
   ```

7. Build the Docker image: Open a terminal or command prompt and navigate to the directory where your Dockerfile is located. Run the following command to build the Docker image:
   ```
   docker build -t your-image-name .
   ```

   Replace "your-image-name" with a meaningful name for your Docker image.

After successfully building the Docker image, you can proceed with running a Docker container using the created image.


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