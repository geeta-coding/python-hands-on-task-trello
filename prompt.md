✅ Prompt 1:
Walk me through installing Python 3.12 on my OS step by step. Include verifying the installation

✅ Response:
Go to the official Python website: https://www.python.org

Download Python 3.12 for your OS (Windows).

Run the installer and check “Add Python to PATH”.

Click Install Now.

After installation, open Command Prompt.

Type:



python --version
If it shows Python 3.12.x, installation is successful.

✅ Prompt 2:
Set up VS Code for Python development — what extensions should I install? Configure linting and formatting

✅ Response:
Install VS Code.

Install extensions:

Python (by Microsoft)

Pylance

Open settings and enable:

Linting (for error checking)

Formatting (auto code formatting)

Recommended formatter:

Black

Enable format on save.

✅ Prompt 3:
Explain the difference between Python 2 and Python 3. Why should I always use Python 3?

✅ Response:
Python 2 is old and no longer supported.

Python 3 is modern and actively maintained.

Differences:

Print syntax: Python 2 → print "Hi"
Python 3 → print("Hi")

Better Unicode support in Python 3

Always use Python 3 because it is updated, secure, and widely used.

✅ Prompt 4:
Show me 10 beginner-friendly Python commands to test my setup in the terminal

✅ Response:


print("Hello World")
x = 5
y = 10
print(x + y)
name = "Geeta"
print(name)
for i in range(5):
    print(i)
print(type(x))
print(len(name))
print(10 > 5)
print("Done")
✅ Prompt 5:
Help me configure VS Code settings.json for the best Python development experience

✅ Response:


{
  "python.defaultInterpreterPath": "python",
  "editor.formatOnSave": true,
  "python.formatting.provider": "black",
  "python.linting.enabled": true,
  "python.linting.pylintEnabled": true
}
