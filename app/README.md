# Local 
## Docker

Build Image:
```
docker image build -t ecs-image .
```

Run Container:
```
docker container run --rm -p 9000:8080 -v $(pwd)/src:/src ecs-image:latest
```
Call lambda:
```
curl -XPOST "http://localhost:9000/2015-03-31/functions/function/invocations" -d '{}'
```
