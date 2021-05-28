# flask-basic-auth

This project is a simple flask API with Basic auth in which user can access public API directly but needed some credentials to use private APIs. This is a simplest way to secure your API from public access using Flask.

## prerequisites-
- python
- Flask

## Details-
- Flask api with 2 URLs- public and private
- Private API can be accessible only after providing correct username and password

## Running this Project
- Download and Install python
- Install Flask using command - pip install flask
- extract this repository or clone it.
- go inside project directory and run command- python app.py
- in cmd you will get URL of project i.e. http://localhost:5000
- try both APIs in your favourite browser using URLs-
- public URL - http://localhost:5000/api/v1/public
- Private URL - http://localhost:5000/api/v1/private (Credentials- username- admin, password- password)

# Pictorial View

## Running App View -
![alt text](https://github.com/diwamishra21/flask-basic-auth/blob/main/images-for-git-readme/app_run.png)

## Private API View - asking Username and password
![alt text](https://github.com/diwamishra21/flask-basic-auth/blob/main/images-for-git-readme/private_api.png)

## Private API after providing credentials
![alt text](https://github.com/diwamishra21/flask-basic-auth/blob/main/images-for-git-readme/private_api_result.png)

## Public API
![alt text](https://github.com/diwamishra21/flask-basic-auth/blob/main/images-for-git-readme/public_api.png)
