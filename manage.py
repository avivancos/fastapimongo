import os
import subprocess
import click
from click_shell import shell
import os
import subprocess
from getpass import getpass
from setup.version import __version__   

@click.command()
def shell():
    """Starts the python shell."""
    subprocess.run(["python"])

@click.command(short_help="Creates a new superuser.")
def createsuperuser():
    """Creates a new superuser."""
    from main import create_superuser
    username = click.prompt('Username', type=str)
    email = click.prompt('Email', type=str)
    password = getpass('Password')
    create_superuser(username, email, password)

@click.command(short_help="Checks and verify starting project for warnings or errors.")
def check():
    """Checks and verify starting project for warnings or errors."""
    
    subprocess.run(["python", "manage.py", "check"])

@click.command(short_help="Tests the application.")
def test():
    """Runs the tests."""
    # Assuming tests are in a directory named 'tests'
    if not os.path.exists('tests'):
        click.echo("No 'tests' directory found.")
        return
    subprocess.run(["pytest", "tests"])
    
@click.group()
def cli():
    pass

@cli.command()
@click.pass_context
def help(ctx):
    """Shows help about the available commands"""
    click.echo("Available commands:")
    click.echo()
    for cmd_name in sorted(cli.commands.keys()):
        cmd = cli.commands[cmd_name]
        click.echo(f"{cmd_name}: {cmd.short_help}")
        
@click.command(short_help="Creates a new project with the standard directory structure.")
@click.argument('projectname')
def new(projectname):
    """Creates a new project with the standard directory structure."""
    os.makedirs(f'{projectname}/models', exist_ok=True)
    os.makedirs(f'{projectname}/schemas', exist_ok=True)
    os.makedirs(f'{projectname}/routers', exist_ok=True)
    os.makedirs(f'{projectname}/services', exist_ok=True)

    with open(f'{projectname}/main.py', 'w') as f:
        f.write("""from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Welcome to": "FastAPI SuperMongo v:{s}"}   )""".format(s=__version__)) )
    

    click.echo(f'Project {projectname} created with standard directory structure.')

cli.add_command(new)

@click.command(short_help="Creates a new model.")
@click.argument('modelname')
def createmodel(modelname):
    """Creates a new model."""
    model_content = f"""from odmantic import Model, Field

class {modelname}(Model):
    name: str = Field(...)
"""
    with open(f'models/{modelname.lower()}.py', 'w') as f:
        f.write(model_content)
    click.echo(f'Model {modelname} created.')

cli.add_command(createmodel)

@click.command(short_help="Runs the server.")
def run():
    """Run the server."""
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)

#CREATE a new version app directory

@click.command(short_help="Creates a new version app directory.")
@click.argument('versionnumber ')
def createversion(version_number):
    """Creates a new  # version app directory."""
    os.makedirs(f'v{version_number}/models', exist_ok=True)
    os.makedirs(f'v{version_number}/schemas', exist_ok=True)
    os.makedirs(f'v{version_number}/routers', exist_ok=True)
    os.makedirs(f'v{version_number}/services', exist_ok=True)

    with open(f'v{version_number}/main.py', 'w') as f:
        f.write("""from fastapi import FastAPI""")
    click.echo(f'Version {version_number} created with standard directory structure.')
    
@click.command(short_help="Creates a new module with a model, router, service, and schema.")
@click.argument('modulename')
def createmodule(modulename):
    """Creates a new module with a model, router, service, and schema."""
    model_content = f"""from odmantic import Model, Field

class {modulename}(Model):
    name: str = Field(...)
"""
    with open(f'models/{modulename.lower()}.py', 'w') as f:
        f.write(model_content)

    router_content = f"""from fastapi import APIRouter

router = APIRouter()

@router.get("/{modulename.lower()}")
async def get_items():
    return []
"""
    with open(f'routers/{modulename.lower()}.py', 'w') as f:
        f.write(router_content)

    schema_content = f"""from pydantic import BaseModel

class {modulename}(BaseModel):
    name: str
"""
    with open(f'schemas/{modulename.lower()}.py', 'w') as f:
        f.write(schema_content)

    crud_content = f"""from fastapi import HTTPException
from schemas.{modulename.lower()} import {modulename}

items = []

def get_item(item_id: int):
    for item in items:
        if item.id == item_id:
            return item
    raise HTTPException(status_code=404, detail="Item not found")

def create_item(item: {modulename}):
    items.append(item)
    return item
"""
    with open(f'services/{modulename.lower()}.py', 'w') as f:
        f.write(crud_content)

    click.echo(f'Module {modulename} created with model, router, service, and schema.')

cli.add_command(startproject)
cli.add_command(createmodel)        
cli.add_command(createmodule)
cli.add_command(shell)
cli.add_command(createsuperuser)
cli.add_command(test)
cli.add_command(run)
cli.add_command(createversion)
cli.add_command(help)
if __name__ == '__main__':
    cli()