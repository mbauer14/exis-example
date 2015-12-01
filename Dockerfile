FROM debian:stable
MAINTAINER Lance Hartung

# Install python interpreter.
RUN apt-get update && apt-get install -y python python-pip
RUN pip install --upgrade pip
RUN pip install --requirement requirements.txt

# Install our python code to the filesystem.
COPY example /opt/example

# Drop down to an unprivileged user.
USER daemon

# Tell python where to find our code.
ENV PYTHONPATH /opt/example

# Go run it.
CMD ["python", "-m", "example"]
