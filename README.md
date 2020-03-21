## Container build
```bash
docker build -t qr-generator .
```
## Container launch
```bash
docker run --rm -p 8000:80 -it qr-generator
```

## dotenv .env
```
HTTP_PORT=8000
HTTP_HOST=0.0.0.0
```

## Notes
http://0.0.0.0:8000/?text=QRtext
