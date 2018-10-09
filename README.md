# senate-data
Brazilian Senate OpenData downloader utilities

# Usage

* Create docker-compose.yml
```
version: '3.3'
services:
  senate-data:
    build: .
    image: flaviostutz/senate-data
    ports:
      - 6006:6006
      - 8888:8888
    volumes:
      - senate-input:/notebook/input
      - senate-output:/notebook/output
```

* Run ```docker-compose up```

* Open http://localhost:8888/
