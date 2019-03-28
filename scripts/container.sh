#! /bin/bash
SRC_DIR=${SRC_DIR:-`pwd`}

# Build container for use of testing or notebook
if [[ $* == *--build* ]]; then
    echo "Building Docker Image"
    docker build \
        -t bayesian-model-evaluation \
        -f $SRC_DIR/scripts/Dockerfile \
        --build-arg SRC_DIR=. $SRC_DIR \
        --rm
fi


if [[ $* == *--notebook* ]]; then
    docker run \
            --mount type=bind,source="$(pwd)",target=/opt/bayesian-model-evaluation/ bayesian-model-evaluation:latest \
            -it -d -p 8888:8888 bayesian-model-evaluation \
            bash -c "--ip 0.0.0.0 --no-browser --allow-root"
fi
