# idle-remade
# Interactive Python Shell

This simple Python script provides an interactive shell environment where you can write and execute Python code. It allows you to perform various operations such as creating, changing, and deleting files, as well as running and printing the code.

## Usage

1. Run the script by executing it in a Python environment.

    ```bash
    python interactive_shell.py
    ```

2. Enter the desired filename when prompted.

3. Use the following commands in the shell:

- `help`: Display a list of available commands.
- `quit`: Exit the shell.
- `clear`: Clear the content of the current file.
- `new file`: Create a new file and switch to it.
- `change file`: Change the current working file.
- `delete file`: Delete a specified file.
- `print`: Display the content of the current file.
- `run`: Execute the code in the current file.

## Example

```bash
Filename: example.py
>>> print("Hello, world!")
>>> run
Hello, world!
>>> quit
```

Notes
- The script uses a loop to continuously prompt the user for input until the quit command is issued.
- Commands are case-sensitive.
- Ensure proper file extensions (e.g., ".py") when creating or changing files.
- Feel free to explore and experiment with Python code in this interactive shell!