FROM        standbyme227/hackathon:base

ENV         BUILD_MODE production
ENV         DJANGO_SETTINGS_MODULE config.settings.${BUILD_MODE}

COPY        . /srv/hackathon

RUN         cp -f /srv/hackathon/.config/${BUILD_MODE}/nginx.conf   /etc/nginx/nginx.conf &&\
            cp -f /srv/hackathon/.config/${BUILD_MODE}/nginx-app.conf /etc/nginx/sites-available/ &&\
            rm -f /etc/nginx/sites-enabled/* &&\
            ln -sf /etc/nginx/sites-available/nginx-app.conf /etc/nginx/sites-enabled/

RUN         cp /srv/hackathon/.config/${BUILD_MODE}/supervisord.conf /etc/supervisor/conf.d/

CMD         pkill nginx; supervisord -n
EXPOSE      80

