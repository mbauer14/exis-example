FROM exis/exis-python
MAINTAINER Lance Hartung

ENV WS_URL ws://sandbox.exis.io:8000/ws
ENV DOMAIN xs.example

# Go run it.
CMD ["python", "-m", "example.example"]
