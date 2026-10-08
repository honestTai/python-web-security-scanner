#!/bin/sh
set -e

if [ ! -d "/usr/local/etc/redis" ]; then
    mkdir -p /usr/local/etc/redis
fi

if [ -n "$REDIS_PASSWORD" ]; then
    echo "requirepass $REDIS_PASSWORD" >> /usr/local/etc/redis/redis.conf
fi

exec "$@"
