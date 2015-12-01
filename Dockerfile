FROM debian:stable
MAINTAINER Lance Hartung

# Install python interpreter.
RUN apt-get update && apt-get install -y python python-pip python-dev
RUN pip install --upgrade pip

# Install python dependencies.
COPY requirements.txt /tmp/requirements.txt
RUN pip install --requirement /tmp/requirements.txt

# Install our python code to the filesystem.
COPY example /opt/example

# Drop down to an unprivileged user.
USER daemon

# Tell python where to find our code.
ENV PYTHONPATH /opt/example

# Go run it.
CMD ["python", "-m", "example"]
