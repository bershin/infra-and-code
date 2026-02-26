FROM python

WORKDIR /usr/src/app

COPY app.py .

RUN pip install --no-cache-dir flask

ENV USR=pyusr
ENV GRP=pygrp

RUN groupadd -r ${GRP} && useradd -m -r -g ${GRP} ${USR}
RUN chown -R ${USR}:${GRP} /usr/src/app

USER ${USR}

CMD ["python", "app.py"]
EXPOSE 5000