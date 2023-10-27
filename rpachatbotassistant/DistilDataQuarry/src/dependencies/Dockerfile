FROM mcr.microsoft.com/azureml/openmpi4.1.0-ubuntu20.04:latest

RUN wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh && \
    chmod +x Miniconda3-latest-Linux-x86_64.sh && \
    ./Miniconda3-latest-Linux-x86_64.sh -b -p /opt/conda && \
    rm Miniconda3-latest-Linux-x86_64.sh

# Set the PATH environment variable to include Miniconda
ENV PATH="/opt/conda/bin:$PATH"

# Install system dependencies
RUN apt update && apt install -y \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

RUN apt-get update && apt-get install -y ca-certificates

# Update conda and activate the base environment
RUN conda update -n base -c defaults conda && \
    conda init bash && \
    . ~/.bashrc

# Install Python dependencies
RUN pip install --upgrade pip \
    && pip install "pandas" \
    "mlflow" \
    "azureml-mlflow" \
    "charset-normalizer" \
    "transformers" \
    "datasets" \
    "requests" \
    "torch==2.0.1" \
    "torchvision" \
    "torchaudio" \
    "scikit-learn" \
    "xformers" \
    "accelerate" \
    "azureml-inference-server-http" \
    && pip install --upgrade datasets

RUN ln -sf /usr/share/zoneinfo/Europe/Lisbon /etc/localtime

# Inference requirements
COPY --from=mcr.microsoft.com/azureml/o16n-base/python-assets:20230419.v1 /artifacts /var/
RUN /var/requirements/install_system_requirements.sh && \
    cp /var/configuration/rsyslog.conf /etc/rsyslog.conf && \
    cp /var/configuration/nginx.conf /etc/nginx/sites-available/app && \
    ln -sf /etc/nginx/sites-available/app /etc/nginx/sites-enabled/app && \
    rm -f /etc/nginx/sites-enabled/default

ENV SVDIR=/var/runit
ENV WORKER_TIMEOUT=400
EXPOSE 5001 8883 8888

# Install SSH for passwordless login
RUN apt-get update && apt-get install -y openssh-server openssh-client

# Start the SSH service
RUN service ssh start
