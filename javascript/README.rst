=========
This is a basic Nodejs application that utilizes the express library to respond 
with message when a request is made to localhost:8080.
=========

## How to run
1. Install Node.js.
2. Install Docker
3. Clone the repository to your local machine
4. Navigate to the project directory in your terminal or command prompt
5. Build command: 

```bash
$ docker build -f Dockerfile -t javascript:1.0 .
````
6. Run command

```bash
$  docker run -p 8080:8080 --rm javascript:1.0
```