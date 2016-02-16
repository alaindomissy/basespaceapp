FROM alaindomissy/docker-miniconda2
MAINTAINER Alain Domissy alaindomissy@gmail.com

RUN pip install \
    six
    path.py==8.1.2 \
    py==1.4.31 \
    pyparsing==2.0.3 \
    python-dateutil==2.4.2 \
    pytz==2015.7 \


COPY . /pybasespace
WORKDIR /pybasespace
RUN python setup.py install
CMD python -m sampleapp
