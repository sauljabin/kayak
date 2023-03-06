FROM python:3.10
WORKDIR /kayak
COPY dist/ /kayak/
RUN pip install --no-cache-dir kayak*.whl \
    && rm ./*
ENTRYPOINT ["kayak"]
