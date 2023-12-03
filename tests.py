import subprocess

#list the commands bellow on a numered list
#1.init
#2.version
#3.createsuperuser
#4.check
#5.shell
#6.test
#7.create
#8.runtests
#9.run
#10.help
#11.module

def test_init_command():
    # Run the 'init' command
    result = subprocess.run(['python', 'manage.py', 'init'], capture_output=True, text=True)

    # Check that the command executed successfully
    assert result.returncode == 0

    # Check the output of the command (if applicable)
    # assert "Expected output" in result.stdout
    assert "Directory structure created." in result.stdout
    
def test_create_command():
    # Run the 'create' command
    result = subprocess.run(['python', 'manage.py', 'create', 'component', 'name'], capture_output=True, text=True)

    # Check that the command executed successfully
    assert result.returncode == 0

    # Check the output of the command (if applicable)
    # assert "Expected output" in result.stdout
    assert "Component name created with standard directory structure." in result.stdout
    
def test_runtests_command():
    # Run the 'runtests' command
    result = subprocess.run(['python', 'manage.py', 'runtests'], capture_output=True, text=True)

    # Check that the command executed successfully
    assert result.returncode == 0

    # Check the output of the command (if applicable)
    # assert "Expected output" in result.stdout
    assert "Ran 0 tests in" in result.stdout

def test_run_command():
    # Run the 'run' command
    result = subprocess.run(['python', 'manage.py', 'run'], capture_output=True, text=True)

    # Check that the command executed successfully
    assert result.returncode == 0

    # Check the output of the command (if applicable)
    # assert "Expected output" in result.stdout
    assert "Running on" in result.stdout

def test_version_command():
    # Run the 'version' command
    result = subprocess.run(['python', 'manage.py', 'version'], capture_output=True, text=True)

    # Check that the command executed successfully
    assert result.returncode == 0

    # Check the output of the command (if applicable)
    # assert "Expected output" in result.stdout
    assert "0.1.0" in result.stdout

def test_createsuperuser_command():
    # Run the 'createsuperuser' command
    result = subprocess.run(['python', 'manage.py', 'createsuperuser'], capture_output=True, text=True)

    # Check that the command executed successfully
    assert result.returncode == 0

    # Check the output of the command (if applicable)
    # assert "Expected output" in result.stdout
    assert "Superuser created successfully." in result.stdout
    
def test_check_command():
    # Run the 'check' command
    result = subprocess.run(['python', 'manage.py', 'check'], capture_output=True, text=True)

    # Check that the command executed successfully
    assert result.returncode == 0

    # Check the output of the command (if applicable)
    # assert "Expected output" in result.stdout
    assert "System check identified no issues (0 silenced)." in result.stdout
    
def test_shell_command():
    # Run the 'shell' command
    result = subprocess.run(['python', 'manage.py', 'shell'], capture_output=True, text=True)

    # Check that the command executed successfully
    assert result.returncode == 0

    # Check the output of the command (if applicable)
    # assert "Expected output" in result.stdout
    assert "Python" in result.stdout

def test_help_command():
    # Run the 'help' command
    result = subprocess.run(['python', 'manage.py', 'help'], capture_output=True, text=True)

    # Check that the command executed successfully
    assert result.returncode == 0

    # Check the output of the command (if applicable)
    # assert "Expected output" in result.stdout
    assert "Usage:" in result.stdout

def test_module_command():
    # Run the 'module' command
    result = subprocess.run(['python', 'manage.py', 'module', 'name'], capture_output=True, text=True)

    # Check that the command executed successfully
    assert result.returncode == 0

    # Check the output of the command (if applicable)
    # assert "Expected output" in result.stdout
    assert "Module name created with standard directory structure." in result.stdout
    
def test_test_command():
    # Run the 'test' command
    result = subprocess.run(['python', 'manage.py', 'test', 'name'], capture_output=True, text=True)

    # Check that the command executed successfully
    assert result.returncode == 0

    # Check the output of the command (if applicable)
    assert "Ran 0 tests in" in result.stdout
    # assert "Expected output" in result.stdout
    # assert "Module name created with standard directory structure." in result.stdout

def test_create_command():
    # Run the 'create' command
    result = subprocess.run(['python', 'manage.py', 'create', 'component', 'name'], capture_output=True, text=True)

    # Check that the command executed successfully
    assert result.returncode == 0
    assert "Component name created with standard directory structure." in result.stdout
    # Check the output of the command (if applicable)
    # assert "Expected output" in result.stdout
    # assert "Module name created with standard directory structure." in result.stdout
    
def test_runtests_command():
    # Run the 'runtests' command
    result = subprocess.run(['python', 'manage.py', 'runtests'], capture_output=True, text=True)

    # Check that the command executed successfully
    assert result.returncode == 0
    assert "Ran 0 tests in" in result.stdout
    # Check the output of the command (if applicable)
    # assert "Expected output" in result.stdout
    # assert "Module name created with standard directory structure." in result.stdout
    