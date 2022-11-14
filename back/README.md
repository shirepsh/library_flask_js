
# shir's library
![Logo](project/static/library.png)

## **Library management**

This site was built to manage libraries in a good and convenient way for librarians

- Submitted by Shir epshtein
- As part of the John Bryce course

- using the following technologies: python, flask, flask-sqlAlchemy, jinja2

### **project locator:**
https://github.com/shirepsh/Library_management
1. enter into GitHub & serach my profil as - shirepsh
2. in my repositorie looking for - "Library management"
3. open the terminal in your Workspace 

### **guide line:**
- If you have not installed Python3, please do
- Please make sure you have 'pip' installed on your OS. 
If it is not installed, please refer to the link below and follow the steps: [Link to PyPa.io](https://pip.pypa.io/en/stable/cli/pip_install/)

1. download the project from GitHub by the comment:
```bash
git clone
```
2. install virtualenv
```bash 
pip install virtualenv
```
3. open venv named venv
```bash
python -m virtualenv venv
```
4. get into the venv 
```bash
venv\Scripts\active
```
5. install all the right packages with the requirements file
```bash
pip install -r requirements.txt  
``` 
6. run the application by the comment:
```
py app.py
```
7. once the code is active press ctrl+ click on the link that created ("http://127.0.0.1:5000")
### **The structure of the project**
the project build from:
- **instance folder** - contain the db

- **__init__db** file-  
This file's purpose is to insert pre-set data into the Library database

- **app.py file** - the run file  

- **README.md file** - Project description and visibility to the user

- **project folder**  
that contain:

    **1. static folder**- with all the images for the project   

    **2. _init__.py file**- Responsible for create the app, database setup, register blueprints

    ***3. subdirectory:*** **books**, **customers**, **loans**            
    each subdirectory contain:

    **templates folder**- whose contain the html pages,    

    **__init__.py file**- an empty file 
    this file allows us to import components into main app.py file
    python needs this for it to understand that this is a module that it can import
    its also use for initializing the prog  

    **models.py file**- Responsible for creating the model and initializing it  
    
    **views.py file**- contains all the end points





