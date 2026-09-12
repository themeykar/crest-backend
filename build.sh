#!/usr/bin/env bash
# build.sh — Render / production build script
set -o errexit

pip install -r requirements.txt

python manage.py collectstatic --noinput --upload-unhashed-files
python manage.py migrate

# Create superuser from env vars (skip silently on re-runs)
if [ -n "$DJANGO_SUPERUSER_USERNAME" ]; then
    python manage.py createsuperuser --noinput 2>/dev/null || echo "Superuser already exists — skipping."
fi
