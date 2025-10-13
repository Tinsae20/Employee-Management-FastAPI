# from supabase import create_client, Client

# supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

#inster new row
# new_row = {'first_name': 'John'}
# supabase.table('fastapi-demo-table').insert(new_row).execute()

#update row
# new_row = {'first_name': 'Mary'}
# supabase.table('fastapi-demo-table').update(new_row).eq('id', 2).execute()

#delete row
# supabase.table('fastapi-demo-table').delete().eq('id', 2).execute()

#get all rows
# results = supabase.table('fastapi-demo-table').select('*').execute()
# print(results)

# response = supabase.storage.from_('fastapi-demo-bucket').get_public_url('image_1.jpeg')
# print(response)


# from fastapi import FastAPI
#
# app = FastAPI()
#
#
# @app.get("/")
# async def root():
#     return {"message": "Hello World"}
#
#
# @app.get("/hello/{name}")
# async def say_hello(name: str):
#     return {"message": f"Hello {name}"}
