# Install dependencies
python3 -m pip install -r requirements.txt

# Collect static files
python3.12 manage.py collectstatic --noinput --clear

# Create Vercel-compatible output vercel directory
#mkdir -p .vercel/output/static
#cp -r staticfiles/ .vercel/output/static/

python3.12 manage.py makemigrations
python3.12 manage.py migrate