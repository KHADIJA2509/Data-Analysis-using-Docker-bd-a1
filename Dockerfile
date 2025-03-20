# Use Ubuntu as the base image
FROM ubuntu:latest

# Set non-interactive mode for package installation
ENV DEBIAN_FRONTEND=noninteractive

# Update packages and install dependencies
RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    && rm -rf /var/lib/apt/lists/*

# Install required Python libraries
RUN pip3 install pandas numpy seaborn matplotlib scikit-learn scipy --break-system-packages

RUN apt-get update && apt-get install -y bash

RUN mkdir -p /home/doc-bd-a1

# Create a working directory in the container
WORKDIR /home/doc-bd-a1

# Copy dataset from local machine to the container
COPY Titanic-Dataset.csv /home/doc-bd-a1/

# Set bash as the default shell
CMD ["/bin/bash"]
