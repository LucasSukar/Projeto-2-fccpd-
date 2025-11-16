#!/bin/sh

porta="http://web:8080/"
intervalo=5

echo "cliente: iniciando. Alvo: $porta. intervalo: ${intervalo}s"

while true; do
  TIMESTAMP=$(date -u +"Horario: %H:%M:%S")
  RESPONSE=$(curl -sS --max-time 3 "$porta")
  EXIT_CODE=$?
  if [ $EXIT_CODE -eq 0 ]; then
    echo "[$TIMESTAMP] sucesso: $RESPONSE"
  else
    echo "[$TIMESTAMP] ERROR: curl exit code $EXIT_CODE"
  fi
  sleep "$intervalo"
done
