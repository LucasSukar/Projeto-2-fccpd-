#!/bin/sh

case "$1" in
  stop)
    echo "Parando containers..."
    docker-compose down -v
    ;;
  *)
    echo "Iniciando containers..."
    docker-compose up -d
    ;;
esac
