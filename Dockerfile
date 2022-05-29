FROM python:3
LABEL AUTHOR="Dimitris Kordas <dimitris@dkordas.com>"

ENV SERVERID=5188
ENV PROJECTNAME=cosmote

WORKDIR /
ADD init.sh .
ADD speedtest .
ADD extract.py .
RUN chmod +x init.sh
RUN chmod +x speedtest
RUN pip install requests
ENTRYPOINT [ "/init.sh" ]