FROM debian
RUN apt-get update && apt-get install -y apache2 libapache2-mod-php php7.3 && apt-get clean && rm -rf /var/lib/apt/lists/*
COPY app /var/www/html/
RUN rm /var/www/html/index.html
EXPOSE 80
CMD ["/usr/sbin/apache2ctl", "-D", "FOREGROUND"]