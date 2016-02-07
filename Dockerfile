FROM python:2.7
ENV PYTHONUNBUFFERED 1
RUN git clone https://github.com/epanchee/brainlab
WORKDIR brainlab
RUN pip install -r requirements.txt
ADD . brainlab