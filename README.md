# EnsemblSearchGeneApi
RESTful API that allows user to search for a gene in Ensembl Database


### **DESCRIPTION ON CI/CD PIPELINE IMPLEMENTED BY APPLICATION**
This project aims to build a simple flask-based REST API to search for genes in ensembl test database.
In addition to it, It uses _pytest_ to ensure api end-point unit testing and employs _Travis_ to 
provide CI/CD in steps such that, whenever a change is pushed to this GitHub repository, It:
1. Activates the server.
2. Automatically runs the tests. ( Tests Automation ).
3. If all tests are passed successfully, It runs a script that builds a docker image and 
deploys it to my DockerHub public repository.
4. The image is being uploaded to DockerHub. Meanwhile, Travis re-deploys the application to Heroku; 
where the older version of app resides.

In this manner, Flask, GitHub, Travis CI, Docker and Heroku is used to build a modern CI/CD pipeline.
For each commit, a build is created and the automated tests are run against it to validate 
it before it moves to the next stage in the CI/CD pipeline. 

Anytime you make changes and commit them, Travis CI will go through the same process, 
and will finally deploy changes to Heroku when no error exists. 
However, when a process fails, Travis CI will alert you via email and stop the process, 
and a previous version of your application will be released instead.

Therefore, you just need to commit to the GitHub repository in order to build and deploy the code.
The application is already deployed on Heroku at provided URL.

**DockerHub URL:** _https://hub.docker.com/r/mariumali/ensembl-search-gene-api_

**Heroku URL:** _https://ensembl-search-gene-api.herokuapp.com/_


### INSTRUCTIONS ON HOW TO RUN APPLICATION ON DOCKER

The application is already dockerized and can be found on above specified DockerHub URL. Any new 
change to the application; once pushed will automatically upgrade the DockerHub image as well. 

But, for the purpose of testing the application, following steps should be 
followed. These steps make use of _Dockerfile_, included in repository to build a docker image 
and run the docker container. As a result, the application starts running 
on _localhost:80_ of your local machine. 

```
git clone https://github.com/MariumAli/EnsemblSearchGeneApi.git
cd EnsemblSearchGeneApi/
docker build -t ensembl-search-gene-api .
docker run -p 80:5000 ensembl-search-gene-api:latest
```

**NOTE**: _In case of Vagrant, same instructions will be followed and you can curl from within vagrant VM 
to `localhost:80` in order to access API. Also, please note that in order to run docker in background 
replace `docker run -p 80:5000 ensembl-search-gene-api:latest` with 
`docker run -d -p 80:5000 ensembl-search-gene-api:latest`. And then execute following instruction to 
ensure proper working of the application.
`curl -X GET "localhost:80".` You should see this message: `Welcome to Search Gene API.`_

From here on, please test according to the documentation. To learn more about available exposed 
endpoints see Documentation section below.  

### **API DOCUMENTATION**
This project provides a OpenApi(Swagger) description of API under file _openApiDocumentation.yaml_ .
The API documentation is public and has been published to SwaggerHub. It can be accessed via SwaggerHub 
URL.

**SwaggerHub Documentation URL:** _https://app.swaggerhub.com/apis-docs/MariumAli/EnsemblSearchGeneRestApi/1.0.0_
**SwaggerHub Published Documentation Code URL:** _https://app.swaggerhub.com/apis/MariumAli/EnsemblSearchGeneRestApi/1.0.0_

Additionally, to check for available responses; an auto mocking server has been setup using SwaggerHub
that mocks API responses.

The following two requests will yield a `201 Response`, with some mock data being returned.
https://virtserver.swaggerhub.com/MariumAli/EnsemblSearchGeneRestApi/1.0.0/tbr
https://virtserver.swaggerhub.com/MariumAli/EnsemblSearchGeneRestApi/1.0.0/tbr/bison_bison_bison

Curl requests ( POST / PUT / PATCH / DELETE ) other that GET to this server will result in a 405 response. 

### **LICENSE**
MIT License

**Note:** _Please mention credits to this repository and the author whenever you make use of it._