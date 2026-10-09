import os
from dotenv import load_dotenv
from supabase import create_client, Client

load_dotenv()

URL = os.getenv("SUPABASE_URL")
KEY = os.getenv("SUPABASE_KEY")

supabase: Client = create_client(URL, KEY)

response = (
    supabase.table("productos")
    .select("*")
    .execute()
)
print(response)



""" response = (
    supabase.table("productos")
    .insert(data)
    .execute()
) """

"""response = (
    supabase.table("productos")
    .update({"nombre": "PC gamer"})
    .eq("id", 2)
    .execute()
)"""