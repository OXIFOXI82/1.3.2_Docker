Выполняемые команды в терминале
docker build . --tag=fapp7  

docker run -d -p 8002:8000 fapp7 
В браузере :
http://localhost:8002/api/v1/products/
