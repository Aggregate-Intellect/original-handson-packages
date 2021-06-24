There are 2 folders in MLOps
1) Building the model and packaging
	- Build an Iris classification model
	- Serialize/De-Serialize the model
	- MLflow for packaging and configuring model environment
	- Convert the model to ONNX format for interoperability between different frameworks
	- Serve the model with Flask framework
2) Containerize and serve the model
        - Dockerize the Flask model previously built
	- Push the image to Docker hub
	- Pull and Serve the Container on AWS EC2 instance
	- Use Docker Container as Development Environment