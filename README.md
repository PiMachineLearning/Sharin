# Sharin
PEP 503 compliant static pip repository generator

## Usage
Place all your files inside the directory wheels using the following system
```
main.py
wheels/
  <project name>/
    file.whl
```
Sharin will generate a folder called `dist` that has all the necessary files for it to function as a pip repository
