#!/bin/bash

# Create local service-result directory
mkdir -p /home/doc-bd-a1/service-result

# Copy output files
cp /home/doc-bd-a1/res_dpre.csv /home/doc-bd-a1/service-result/
cp /home/doc-bd-a1/eda-in-1.txt /home/doc-bd-a1/service-result/
cp /home/doc-bd-a1/eda-in-2.txt /home/doc-bd-a1/service-result/
cp /home/doc-bd-a1/eda-in-3.txt /home/doc-bd-a1/service-result/
cp /home/doc-bd-a1/vis.png /home/doc-bd-a1/service-result/
cp /home/doc-bd-a1/k.txt /home/doc-bd-a1/service-result/

# Copy results to host
docker cp bd-a1-container:/home/doc-bd-a1/service-result/ D:\Docker\bd-a1\service-result\

# Stop the container
docker stop bd-a1-container
