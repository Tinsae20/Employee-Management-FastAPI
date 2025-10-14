# database.py
import os
from supabase import create_client, Client
from dotenv import load_dotenv
from typing import cast

# Load environment variables from .env file
load_dotenv()

SUPABASE_URL = os.getenv('SUPABASE_URL')
SUPABASE_KEY = os.getenv('SUPABASE_KEY')
SUPABASE_BUCKET = os.getenv('SUPABASE_BUCKET')
SUPABASE_JWT_SECRET = os.getenv('SUPABASE_JWT_SECRET')

if not all([SUPABASE_URL, SUPABASE_KEY, SUPABASE_BUCKET, SUPABASE_JWT_SECRET]):
    raise EnvironmentError("One or more Supabase environment variables are missing.")

# Initialize Supabase client
supabase: Client = create_client(cast(str,SUPABASE_URL), cast(str,SUPABASE_KEY))