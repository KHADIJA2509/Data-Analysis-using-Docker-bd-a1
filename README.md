# **Big Data Processing**

## **1. Overview**  
This project involves processing a dataset using Docker. The workflow includes data preprocessing, exploratory data analysis, visualization, and clustering with K-Means. The pipeline runs inside a Docker container, ensuring a reproducible environment.

---

## **2. Prerequisites**  
Ensure you have the following installed on your system:  
- [Docker](https://www.docker.com/get-started)  
- Python 3 (included in Docker image)  

---

## **3. Docker Setup** 
```bash 
docker build -t bd-a1 . 
docker run -it --name bd-container bd-a1 
``` 
 
---

## **4. Running the Pipeline** 
Inside the container: 
```bash 
python load.py dataset.csv 
``` 
 
---

## **5. Retrieving Results** 
On your local machine: 
```bash 
./final.sh 
``` 
This copies the output and stops the container. 

---

## 6. Output Files
After execution, the following output files will be available:

| File Name               | Description                                      |
|-------------------------|--------------------------------------------------|
| `processed_data.csv`    | Cleaned dataset after preprocessing             |
| `res_dpre.csv`         | Results from the data pipeline                   |
| `eda-in-1.txt`, `eda-in-2.txt`, `eda-in-3.txt` | Exploratory Data Analysis reports |
| `vis.png`              | Data visualization output                        |

---

## 7. Bonus Tasks: Pushing to Docker Hub and GitHub

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

---

## Notes

-  Docker Image on Docker Hub Link :https://hub.docker.com/r/khadijaxx/bd-a1-image
-  GitHub repositrey :https://github.com/KHADIJA2509/Data-Analysis-using-Docker-bd-a1

