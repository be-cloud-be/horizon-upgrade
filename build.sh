#!/usr/bin/env bash

set -e

echo "Build docker image"

docker build -t be-cloud/horizon-upgrade:10.0-up . "$@"