# Сборка образа

Завершив с Dockerfile, мы просто выполняем из каталога нашего проекта следующую команду:  

> sudo docker build -t directory-monitor .

# Запуск образа

> sudo docker run -d --restart=always -e DIRECTORY='/tmp/test' -v /tmp/:/tmp/ directory-monitor

### После запуска образа его состояние можно проверять с помощью команды:  

> sudo docker ps


# Делимся программой

> sudo docker login --username=tonycythony
> sudo docker tag directory-monitor tonycythony/alenaapp
> sudo docker push tonycythony/alenaapp


## Source

* [Как превратить скрипт на Python в «настоящую» программу при помощи Docker](https://habr.com/ru/company/vdsina/blog/555540/)
