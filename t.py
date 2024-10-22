d = """
alembic==1.13.3 ;
annotated-types==0.7.0 ; 
anyio==3.7.1 ; 
async-timeout==4.0.3 ;
asyncpg==0.29.0 ; 
bcrypt==4.0.1 ; 
cffi==1.17.1 ;
click==8.1.7 ; 
colorama==0.4.6 ;
cryptography==43.0.3 ; 
dnspython==2.7.0 ; 
email-validator==2.2.0 ; 
environs==9.5.0 ; 
fastapi-cache2==0.2.2 ; 
fastapi==0.104.1 ; 
greenlet==3.1.1
h11==0.14.0 ; 
idna==3.10 ; 
mako==1.3.6 ; 
markupsafe==3.0.2 ; 
marshmallow==3.23.0 ; 
packaging==24.1 ; 
passlib==1.7.4 ; 
pendulum==3.0.0 ; 
pycparser==2.22 ;
pydantic-core==2.23.4 ; 
pydantic-settings==2.6.0 ; 
pydantic==2.9.2 ; 
pydantic[email]==2.9.2 ; 
pyjwt[crypto]==2.9.0 ; 
python-dateutil==2.9.0.post0 ; 
python-dotenv==1.0.1 ; 
python-multipart==0.0.9 ; 
redis==5.1.1 ; 
six==1.16.0 ; 
sniffio==1.3.1 ; 
sqlalchemy==2.0.36 ; 
sqlalchemy[asyncio]==2.0.36 ; 
starlette==0.27.0 ; 
typing-extensions==4.12.2 ; 
tzdata==2024.2 ; 
uvicorn[all]==0.24.0.post1 ; 
"""

with open("requirements.txt", "w") as f:
    while True:
        if " " in d:
            d = d.replace(" ", "")
        elif ";" in d:
            d = d.replace(";", "")
        else:
            break
    f.write(d)
