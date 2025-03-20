# Assignment 1: Big Data Processing 
 
## **1. Overview** 
This project involves processing a dataset using Docker, performing data preprocessing, exploratory data analysis, visualization, and clustering with K-Means. 
 
## **2. Docker Setup** 
```bash 
docker build -t bd-a1 . 
docker run -it --name bd-container bd-a1 
``` 
 
## **3. Running the Pipeline** 
Inside the container: 
```bash 
python3 load.py dataset.csv 
``` 
 
## **4. Retrieving Results** 
On your local machine: 
```bash 
./final.sh 
``` 
This copies the output and stops the container. 
 
## **Step 9: Bonus Tasks** 
1. **Push the Docker Image to Docker Hub**: 
```bash 
docker tag bd-a1 your-dockerhub-username/bd-a1 
docker push your-dockerhub-username/bd-a1 
``` 
 
2. **Push Code to GitHub**: 
```bash 
git init 
git add . 
git commit -m "Initial commit" 
git branch -M main 
git push -u origin main 
``` 
