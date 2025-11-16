FROM alpine:3.19
RUN apk add --no-cache curl
WORKDIR /app
COPY client.sh .
RUN chmod +x client.sh
CMD ["./client.sh"]
