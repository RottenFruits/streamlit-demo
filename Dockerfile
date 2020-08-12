FROM ubuntu:18.04

ENV DEBIAN_FRONTEND=noninteractive

#set up timezone
#https://sleepless-se.net/2018/07/31/docker-build-tzdata-ubuntu/
RUN DEBIAN_FRONTEND=noninteractive
RUN apt-get update && apt-get install -y tzdata
# timezone setting
ENV TZ=Asia/Tokyo

RUN apt-get update && \
    apt-get install -y --no-install-recommends wget sudo language-pack-ja fonts-ipafont fonts-ipaexfont libboost-dev git-lfs maven nkf postgresql git

#install python
RUN apt-get update && \
    sudo apt install -y --no-install-recommends python3.7 python3-distutils python3-pip python3-setuptools

RUN pip3 install numpy pandas streamlit

COPY app app
WORKDIR app

#locale 
ENV LC_ALL C.UTF-8
ENV LANG C.UTF-8

EXPOSE 8501