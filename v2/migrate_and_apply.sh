#!/bin/bash

# Step 1: Delete migration files (*.py) except __init__.py
find . -path "*/migrations/*.py" -not -name "__init__.py" -delete

# Step 2: Delete compiled migration files (*.pyc)
find . -path "*/migrations/*.pyc" -delete

# Step 3: Create new migration files
python3 manage.py makemigrations

# Step 4: Apply the migrations to the database
python3 manage.py migrate
