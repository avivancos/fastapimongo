import getpass
import os
import subprocess
from multiprocessing import Process
from time import sleep
import click
import requests

#short description of this file and what it does
#Available commands: 
# shell,  init, createsuperuser, check, test, runtests, run, help

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
    template_path = f'templates/default_{choice}.py'
    if not os.path.exists(template_path):
        click.echo(f"Template for {choice} does not exist.")
        return

    with open(template_path, 'r') as f:
        template = f.read()

    content = template.replace('%_name_%', name)

    # Ensure the directory exists before writing the file
    os.makedirs(f'{choice}s', exist_ok=True)

    output_path = f'{choice}s/{name.lower()}.py'
    with open(output_path, 'w') as f:
        f.write(content)

    click.echo(f'{choice.capitalize()} {name} created.')
    
    
@click.command(short_help="Runs the server.")
def run():
    """Run the server."""
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)

@click.command(short_help="Creates a new module.")
@click.argument('module_name')
def create_module(module_name):
    """Creates a new standard module with model.py, router.py, service.py, and schema.py under /modules/module_name directory."""
    os.makedirs(f'modules/{module_name}', exist_ok=True)
    
    # Create model.py from template default model.py
    #templates are in the templates folder
    
    template_path = 'templates/default_model.py'
    if not os.path.exists(template_path):
        click.echo("Model template does not exist.")
        return
    
    with open(template_path, 'r') as f:
        template = f.read()
        
    content = template.replace('%_name_%', module_name)
    
    output_path = f'modules/{module_name}/model.py'
    with open(output_path, 'w') as f:
        f.write(content)
    
    # Create router.py from template default router.py
    template_path = 'templates/default_router.py'
    if not os.path.exists(template_path):
        click.echo("Router template does not exist.")
        return
    
    with open(template_path, 'r') as f:
        template = f.read()
    
    content = template.replace('%_name_%', module_name)
    
    output_path = f'modules/{module_name}/router.py'
    with open(output_path, 'w') as f:
        f.write(content)
    
    # Create service.py from template default service.py
    template_path = 'templates/default_service.py'
    if not os.path.exists(template_path):
        click.echo("Service template does not exist.")
        return
    
    with open(template_path, 'r') as f:
        template = f.read()
    
    content = template.replace('%_name_%', module_name)
    
    # Create schema.py from template default schema.py
    template_path = 'templates/default_schema.py'
    if not os.path.exists(template_path):
        click.echo("Schema template does not exist.")
        return
    
    with open(template_path, 'r') as f:
        template = f.read()
        
    content = template.replace('%_name_%', module_name)
    
    output_path = f'modules/{module_name}/schema.py'
    with open(output_path, 'w') as f:
        f.write(content)
    
    click.echo(f'Module {module_name} created.')

# Add the new command to the CLI
cli.add_command(create_module, name="create_module")
    
    

cli.add_command(version, name="version")
cli.add_command(create, name="create")  
cli.add_command(create_module, name="module")     
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