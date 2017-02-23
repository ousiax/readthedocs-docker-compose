FROM qqbuby/readthedocs:uwsgi

MAINTAINER qqbuby <qqbuby@gmail.com>

WORKDIR $RTD_REPO_DIR

COPY ./files/local_settings.py ./readthedocs/settings/

VOLUME $RTD_REPO_DIR

CMD ["uwsgi", "--ini", "readthedocs.ini:dev"]
