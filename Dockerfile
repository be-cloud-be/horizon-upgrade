FROM tecnativa/odoo-base:9.0

ARG ODOO_VERSION=9.0
ENV ODOO_VERSION=$ODOO_VERSION \
    PGDATABASE=$DB_SOURCE

CMD ["/opt/odoo/custom/src/run-odoo"]

# Metadata
ARG BUILD_DATE
ARG VCS_REF
ARG VERSION
LABEL maintainer="be-cloud.be <info@be-cloud.be>" \
      org.label-schema.build-date=$BUILD_DATE \
      org.label-schema.name="Odoo Run v9" \
      org.label-schema.description="Docker image used to run Horizon v9." \
      org.label-schema.url="https://horizon.be-cloud.be/" \
      org.label-schema.vcs-ref=$VCS_REF \
      org.label-schema.vcs-url="https://github.com/be-cloud-be/horizon-upgrade" \
      org.label-schema.vendor="be-cloud.be" \
      org.label-schema.version=$VERSION \
      org.label-schema.schema-version="1.0"

USER root
