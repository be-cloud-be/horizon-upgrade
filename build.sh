#!/usr/bin/env bash

set -e

log INFO "Build docker image"

docker build -t be-cloud/horizon-upgrade:9.0 .