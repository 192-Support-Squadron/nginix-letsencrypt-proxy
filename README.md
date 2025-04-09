# nginix-letsencrypt-proxy

This repository uses jinja to generate a docker compose file for nginx and certbot.

## Getting Started

1. Ensure you have python and pip installed.
2. Then install the requirements.txt
3. Activate the venv.
4. python3 render.py -y variables.yml -t nginx.jinja
