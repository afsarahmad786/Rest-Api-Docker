REST API With Flask & SQL Alchemy && Docker
=======

> Products API using Python Flask, SQL Alchemy and Marshmallow, or Run using Docker

## Quick Start Using Pip

``` bash

# Install dependencies
$ pipenv install -r requirements.txt

# Create DB
$ python
>> from app import db
>> db.create_all()
>> exit()
$ python sqlapp.py


## Quick Start Using DOCKER
The way to get our Python code running in a container is to pack it as a Docker image and then run a container based on it. The steps are sketched below.
(docker)(dcr.png)
To generate a Docker image we need to create a Dockerfile which contains instructions needed to build the image. The Dockerfile is then processed by the Docker builder which generates the Docker image. Then, with a simple docker run command, we create and run a container with the Python service.

#### how to deploy using docker
create a dockerfile with no extension
$ touch Dockerfile and fil the requirements as shown below

```Dockerfile
FROM python:3.7

WORKDIR /user/src/app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY ./sqlapp.py /user/src/app

```
- after saving the file run the following command 
$ docker build -t myimage .
(build)(build.png)

- if you want to see docker image
$ docker images
you will see myimage there

to run the docker image
$ docker run -d -p 5000:5000 myimage
$ curl http://localhost:5000

or run 
$ docker run -it myimage python sqlapp.py

(image)(img.png)

## Postman
you need postman(https://www.postman.com/downloads/) to perform the queries like insert( method-> POST) , Update ( method-> PUT)  , Fetch ( method-> GET) , Delete ( method-> DELETE) 

- Open POSTMAN
- On the Right side you will find untitled request 
- First select Method as POST in search bar fill http://localhost:5000/product. go to header . Fill Key as Content-type and value as Application/JSON
----------------------------------------------------------------------------------------------------------------------------------------------------------
- Now go to body Fill data like this you need to fill detail as name type STR,  regular_price_value TYPE INT, currency TYPE INT, classification_l1 TYPE STR,classification_l2 TYPE STR,classification_l3 TYPE STR, classification_l4 TYPE STR,image_url TYPE STR
$ { "name": "updated", "brand_name": "icandy", 
"regular_price_value": 1080.0, "offer_price_value": 1080.0,
"currency": "GBP",
"classification_l1": "baby & child",
"classification_l2": "buggies & travel",
"classification_l3": "pushchairs & prams", 
"classification_l4": "",
"image_url": "https://johnlewis.scene7.com/is/image/JohnLewis/237781332?"}
---------------------------------------------------------------------------------------------------------------------------------------------------------
- Now click send and data insert successfully youll find success code 200 and data will be printed in response container as well


## Endpoints

* GET     /product
* GET     /product/:id
* POST    /product
* PUT     /product/:id
* DELETE  /product/:id
#### POST
(POST)(post.png)

#### PUT
(PUT)(put.png)

#### GET
(GET)(get.png)

#### DELETE
(DELETE)(del.png)

