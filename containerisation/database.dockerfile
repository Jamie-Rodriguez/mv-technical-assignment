FROM postgres:14.1-alpine3.15

RUN mkdir -p /data
COPY WA_Fn-UseC_-HR-Employee-Attrition.csv /data/
RUN chown postgres /data
RUN chmod +w /data

COPY ./schema/* /docker-entrypoint-initdb.d/