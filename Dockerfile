FROM python:3.9-slim

WORKDIR /app

#Dockerize Challenge B
COPY challenge_b.py .
#reads the output from Challenge A as an Input 
COPY objects.txt . 

CMD ["python", "challenge_b.py"]

#run:
#docker build -t challenge-b -f Dockerfile .
#docker run --rm challenge-b > processed_output.txt
