Write-Console "Generate Self Signed Certificate to use for inital NGINX"
New-Item -ItemType "Directory" "/opt/project_name/certbot/conf/live/test.notreal.mil"

docker compose run --rm --entrypoint "\
  openssl req -x509 -nodes -newkey rsa:2048 -days 1\
    -keyout '/etc/letsencrypt/live/test.notreal.mil/privkey.pem' \
    -out '/etc/letsencrypt/live/test.notreal.mil/fullchain.pem' \
    -subj '/CN=localhost'" certbot

Write-Console "Starting nginx"
docker compose up --force-recreate -d nginx

Write-Console "Deleting Self Signed Certificate"
docker-compose run --rm --entrypoint "\
  rm -Rf /etc/letsencrypt/live/test.notreal.mil && \
  rm -Rf /etc/letsencrypt/archive/test.notreal.mil && \
  rm -Rf /etc/letsencrypt/renewal/test.notreal.mil.conf" certbot

Write-Console "Requesting Let's Encrypt certificate for test.notreal.mil"
docker-compose run --rm --entrypoint "\
  certbot certonly --webroot -w /var/www/certbot \
    0 \
    --email noreply@notreal.mil \
    -d  \
    --key-type ecdsa \
    --elliptic-curve secp384r1 \
    --agree-tos \
    --force-renewal" certbot

Write-Console  "Reloading nginx"
docker compose exec nginx nginx -s reload