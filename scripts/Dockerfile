FROM conda/miniconda3

LABEL maintainer="Ravin Kumar"

ARG SRC_DIR

# Change behavior of create_test.sh script
ENV DOCKER_BUILD=true

# For Sphinx documentation builds
ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8

# Update container
RUN apt-get update && apt-get install -y git build-essential pandoc vim ffmpeg \
    && rm -rf /var/lib/apt/lists/*


# Copy requirements and environment installation scripts
COPY $SRC_DIR/requirements.txt  opt/bayesian-model-evaluation/
COPY $SRC_DIR/scripts/ opt/bayesian-model-evaluation/scripts
WORKDIR /opt/arviz


# Create conda environment. Defaults to Python 3.6
RUN ./scripts/create_testenv.sh


# Set automatic conda activation in non interactive and shells
ENV BASH_ENV="/root/activate_conda.sh"
RUN echo ". /root/activate_conda.sh" > /root/.bashrc


# Remove conda cache
RUN conda clean --all

COPY $SRC_DIR /opt/arviz

