FROM ubuntu:18.04

# Set character encoding environment variables
ENV LC_ALL=C.UTF-8 LANG=C.UTF-8

# Allow apt-get install without interaction from console
ENV DEBIAN_FRONTEND=noninteractive

# Set the working dir to the root user home folder
WORKDIR /root

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
	echo 'source $HOME/miniconda/bin/activate' >> .bashrc && \
	rm Miniconda3-4.5.1-Linux-x86_64.sh

# Set the path env to include miniconda
ENV PATH /root/miniconda/bin:$PATH

RUN mkdir -p ~/.jupyter 

COPY jupyter_notebook_config.py /root/.jupyter/jupyter_notebook_config.py

# Install python packages
COPY requirements.txt .
RUN pip install --upgrade pip setuptools && \
	pip install -r requirements.txt --no-cache-dir

RUN pip install torch==1.4.0+cpu -f https://download.pytorch.org/whl/torch_stable.html

RUN mkdir -p /root/work

CMD ["jupyter", "lab", "--no-browser","--NotebookApp.token=''","--NotebookApp.password=''"]
