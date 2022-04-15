FROM python:3.10.4-slim-bullseye as base
RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends python3-pip python3-cffi libcairo2 libpango-1.0-0 libpangocairo-1.0-0 libgdk-pixbuf2.0-0 shared-mime-info file && useradd -d /sandboxed_weasyprint sandboxed_weasyprint
WORKDIR /sandboxed_weasyprint


FROM base as build
RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y build-essential python3-dev libffi-dev
COPY requirements.txt /sandboxed_weasyprint/
RUN mkdir wheels && cd wheels && pip wheel -r ../requirements.txt

FROM base
COPY --from=build /sandboxed_weasyprint/wheels /sandboxed_weasyprint/wheels
RUN pip3 install /sandboxed_weasyprint/wheels/* && rm -rf /sandboxed_weasyprint/wheels && apt-get clean autoclean && apt-get autoremove --yes && rm -rf /var/lib/{apt,dpkg,cache,log}/ 
WORKDIR /sandboxed_weasyprint
COPY swagger_server /sandboxed_weasyprint/swagger_server/
USER sandboxed_weasyprint

ENTRYPOINT ["python3"]

CMD ["-m", "swagger_server"]
