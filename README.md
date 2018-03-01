# sandboxed_weasyprint
WeasyPrint based web service that only accesses files provided in the request

Usage:
docker build -f Dockerfile -t sbwp .
ocker run -p8080:8080 --rm sbwp

curl -vX POST http://127.0.0.1:8080/v1/html2pdf -d @./test_data/test1.json --header "Content-Type: application/json" -otest1.pdf

No file acces and no access to external urls, everything is looked up from the extrafiles list
