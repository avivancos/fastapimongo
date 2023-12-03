import getpass
import os
import subprocess
from multiprocessing import Process
from time import sleep
import click
import requests


@click.command()
def shell():
    """Starts the python shell."""
    subprocess.run(["python"])

#app initialization command
@click.command(short_help="Initializes the application.")
def init():
    """
    Initializes the application.

    This function checks if the file "main.py" already exists. If it does, it prints a message indicating that the application is already initialized. If the file doesn't exist, it creates a new file "main.py" and writes a basic FastAPI import statement into it. Finally, it prints a message indicating that the application has been initialized.
    """
    if os.path.exists("main.py"):
        click.echo("The application is already initialized.")
        return
    with open("main.py", "w") as f:
        f.write("""from fastapi import FastAPI""")
    click.echo("Application initialized.")
    
#CREATE a new version app directory

@click.command(short_help="Creates a new version app directory.")
@click.argument('versionnumber ')
def version(version_number):
    """Creates a new  # version app directory."""
    os.makedirs(f'v{version_number}/models', exist_ok=True)
    os.makedirs(f'v{version_number}/schemas', exist_ok=True)
    os.makedirs(f'v{version_number}/routers', exist_ok=True)
    os.makedirs(f'v{version_number}/services', exist_ok=True)

    with open(f'v{version_number}/main.py', 'w') as f:
        f.write("""from fastapi import FastAPI""")
    click.echo(f'Version {version_number} created with standard directory structure.')

@click.command(short_help="Creates a new superuser.")
def createsuperuser():
    """Creates a new superuser.

    This function prompts the user for a username, email, and password to create a new superuser.
    It then calls the `create_superuser` function from the `main` module to create the superuser.
    """
    from main import create_superuser
    username = click.prompt('Username', type=str)
    email = click.prompt('Email', type=str)
    password = getpass('Password')
    create_superuser(username, email, password)


@click.command(short_help="Checks the application for errors and correct directory structure.")
def check():
    """Checks the application for errors and correct directory structure."""

    def start_server():
        subprocess.run(["uvicorn", "main:app", "--port", "8000"])

    # Start the server in a separate process
    server = Process(target=start_server)
    server.start()

    # Wait for the server to start
    sleep(5)

    # Make a request to the home page
    try:
        response = requests.get("http://localhost:8000")
        response.raise_for_status()
        click.echo("FastAPI started successfully.")
    except requests.exceptions.RequestException as e:
        click.echo(f"FastAPI failed to start: {e}")
    finally:
        # Stop the server
        server.terminate()
        server.join()

    # Check directory structure
    assert os.path.exists("models"), "The 'models' directory does not exist"
    assert os.path.exists("main.py"), "The 'main.py' file does not exist"
    # Add more assertions for other directories and files as needed
    click.echo("Directory structure is correct.")
    
    
@click.command(short_help="Creates a new test.")
@click.argument('name')
def test(name):
    """
    Creates a new test.

    Args:
        name (str): The name of the test.

    Returns:
        None
    """
    template_path = 'default_test.py'
    if not os.path.exists(template_path):
        click.echo("Test template does not exist.")
        return

    with open(template_path, 'r') as f:
        template = f.read()

    content = template.replace('%_name_%', name)

    output_path = f'tests/test_{name.lower()}.py'
    with open(output_path, 'w') as f:
        f.write(content)

    click.echo(f'Test {name} created.')

import subprocess

@click.command(short_help="Runs all tests.")
def runtests():
    """
    Runs all tests.

    Returns:
        None
    """
    result = subprocess.run(['pytest', 'tests'], stdout=subprocess.PIPE)
    click.echo(result.stdout.decode('utf-8'))
    
@click.group()
def cli():
    """
    This function is the command line interface for the application.
    It is responsible for handling command line arguments and executing the appropriate actions.
    """
    pass
def cli():
    pass

@cli.command()
@click.pass_context
def help(ctx):
    """
    Shows help about the available commands

    Parameters:
    - ctx: The click context object

    Returns:
    None
    """
    click.echo("Available commands:")
    click.echo()
    for cmd_name in sorted(cli.commands.keys()):
        cmd = cli.commands[cmd_name]
        click.echo(f"{cmd_name}: {cmd.short_help}")
import os
import click

@click.command(short_help="Creates a new component.")
@click.argument('choice', type=click.Choice(['model', 'router', 'service', 'schema']))
@click.argument('name')
def create(choice, name):
    """
    Creates a new component.

    Args:
        choice (str): The type of the component to create.
        name (str): The name of the component.

    Returns:
        None
    """
    template_path = f'default_{choice}.py'
    if not os.path.exists(template_path):
        click.echo(f"Template for {choice} does not exist.")
        return

    with open(template_path, 'r') as f:
        template = f.read()

    content = template.replace('%_name_%', name)

    output_path = f'{choice}s/{name.lower()}.py'
    with open(output_path, 'w') as f:
        f.write(content)

    click.echo(f'{choice.capitalize()} {name} created.')
    
@click.command(short_help="Runs the server.")
def run():
    """Run the server."""
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)

@click.command(short_help="Creates a new module with a model, router, service, and schema directory.")
@click.argument('module')
def module(module):
    """
    Creates a new module with a model, router, service, and schema directory.

    Args:
        module (str): The name of the module.

    """
    model_content = f"""from odmantic import Model, Field

class {module}(Model):
    name: str = Field(...)
"""
    with open(f'models/{module.lower()}.py', 'w') as f:
        f.write(model_content)

    router_content = f"""from fastapi import APIRouter
from models.{module.lower()} import {module}
from fastapi import HTTPException

router = APIRouter()

items = []

@router.get("/{module.lower()}")
async def get_items():
    return items

@router.post("/{module.lower()}")
async def create_item(item: {module}):
    items.append(item)
    return item

@router.get("/{module.lower()}/{{item_id}}")
async def get_item(item_id: int):
    for item in items:
        if item.id == item_id:
            return item
    raise HTTPException(status_code=404, detail="Item not found")
""" 
    with open(f'routers/{module.lower()}.py', 'w') as f:
        f.write(router_content)

    service_content = f"""from models.{module.lower()} import {module}

def get_all_items():
    return items

def create_item(item: {module}):
    items.append(item)
    return item
"""
    with open(f'services/{module.lower()}.py', 'w') as f:
        f.write(service_content)

    schema_content = f"""from pydantic import BaseModel

class {module}Base(BaseModel):
    name: str

class {module}({module}Base):
    id: int

    class Config:
        orm_mode = True
"""
    os.makedirs(f'schemas/{module.lower()}', exist_ok=True)
    with open(f'schemas/{module.lower()}/{module.lower()}.py', 'w') as f:
        f.write(schema_content)

click.echo(f'Module {module} created with standard directory structure.')


cli.add_command(version, name="version")
cli.add_command(create, name="create")  
cli.add_command(module, name="module")     
cli.add_command(check, name="check")
cli.add_command(shell, name="shell")
cli.add_command(createsuperuser, name="createsuperuser")
cli.add_command(test, name="test")
cli.add_command(runtests, name="runtests")
cli.add_command(run, name="run")
cli.add_command(help, name="help")
cli.add_command(init, name="init")




if __name__ == '__main__':
    cli()