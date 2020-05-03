# Docker-Images
Docker images and compose yamls for local dev

# Prerequisites:
1.  Docker Engine - Docker Compose
2.  Python - Pandas, Pymongo
3.  Jupyter
4.  Optional - VS Code with Docker extension

# Usage:
1. Clone repo
2. run docker-compose up in the directory
3. This should pull mongo / mongo express images (if not available locally)
   and start containers.
4. Docker is configured to run mongodb on port 27017 and express on 8081.
5. Open jupyter notebook/lab in the directory and you should be able to 
   connect to the db out of the box.