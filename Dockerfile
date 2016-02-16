FROM alaindomissy/docker-miniconda2
MAINTAINER Alain Domissy alaindomissy@gmail.com

RUN pip install \
    six

COPY . /basespaceapp
WORKDIR /basespaceapp
RUN python setup.py install
CMD python -m sampleapp
