#!/usr/bin/env sh

docker build \
       --file=django.Dockerfile \
       --tag="metas:2021.1" \
       .
docker create \
       --interactive \
       --tty \
       --rm \
       --name=metas \
       --publish-all \
       --mount type=bind,source="$(pwd)/.",target=/app \
       --workdir /app \
       metas:2021.1

docker start metas
docker port metas
docker attach metas