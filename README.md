# ws-pie

[![image size](https://img.shields.io/badge/image%20size-339MB-blue.svg)](https://hub.docker.com/r/maslick/wspie)

### Dev mode:
```
pip3 install -r requirements.txt
python3 run.py
open http://localhost:8080/maslick
```

### Prod mode (gunicorn):
```
pip3 install -r requirements.txt
gunicorn run:app -c gunicorn.config.py
open http://localhost:5000/unicorn
```

### Docker:
```
docker build . -t maslick/wspie
docker run -d -p 8080:5000 maslick/wspie
open http://`docker-machine ip`:8080/maslick
```

```
docker run -d -p 8081:5000 maslick/wspie
open http://`docker-machine ip`:8081
```

### k8s:
```
kubectl apply -f k8s
open http://wspie.maslick.ru
```