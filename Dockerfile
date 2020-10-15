FROM tecnativa/odoo-base:10.0

ARG ODOO_VERSION=10.0
ENV ODOO_VERSION=$ODOO_VERSION \
    PGDATABASE=$DB_TARGET

CMD ["/opt/odoo/custom/src/upgrade-odoo"]

# Metadata
ARG BUILD_DATE
ARG VCS_REF
ARG VERSION
LABEL maintainer="LasLabs Inc <support@laslabs.com>" \
      org.label-schema.build-date=$BUILD_DATE \
      org.label-schema.name="Odoo Upgrade v10" \
      org.label-schema.description="Docker image used for upgrading Odoo v9 to v10 using OCA OpenUpgrade." \
      org.label-schema.url="https://laslabs.com/" \
      org.label-schema.vcs-ref=$VCS_REF \
      org.label-schema.vcs-url="https://github.com/LasLabs/docker-odoo-upgrade" \
      org.label-schema.vendor="LasLabs Inc." \
      org.label-schema.version=$VERSION \
      org.label-schema.schema-version="1.0"

USER root
