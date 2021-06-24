FROM ubuntu:18.04

# Set character encoding environment variables
ENV LC_ALL=C.UTF-8 LANG=C.UTF-8

# Allow apt-get install without interaction from console
ENV DEBIAN_FRONTEND=noninteractive

# Set the workign directory to /root
WORKDIR /root

# System updates and configurations
RUN apt-get update && apt-get -y --no-install-recommends install \
		ca-certificates \
		git \
		ssh \
		wget && \
	apt-get clean && \
	apt-get autoremove && \
	rm -rf /var/lib/apt/lists/*

# Install Miniconda
RUN wget --quiet https://repo.anaconda.com/miniconda/Miniconda3-4.5.1-Linux-x86_64.sh && \
	bash Miniconda3-4.5.1-Linux-x86_64.sh -b -p $HOME/miniconda && \
	rm Miniconda3-4.5.1-Linux-x86_64.sh

# Set the path env to include miniconda
ENV PATH /root/miniconda/bin:$PATH

# Copy over model and API code into the container
COPY ./api /root
COPY start.sh /root

# Create a conda environment from the specified conda.yaml
RUN conda env create --file /root/model/conda.yaml

# Add to .bashrc
RUN echo "source activate mlflow-env" >> .bashrc

# Pip install api requirements into the conda env
RUN /bin/bash -c "source activate mlflow-env" && \
	pip install --upgrade pip setuptools && \
	pip install -r /root/requirements.txt --no-cache-dir

# Make our start script executable
RUN ["chmod", "+x", "/root/start.sh"]

# Start the API
ENTRYPOINT [ "/root/start.sh" ]
