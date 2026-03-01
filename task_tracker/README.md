# Task tracker

> This project is a backend project from roadmap.sh

To build and run this project just follow theses steps

## 1. Clone the repository
````
git clone git@github.com:onomojiji/roadmap.sh-Backend-projects.git
````

## 2. Navigate to task_tracker folder
````
cd task_tracker
````

## 3. Create a python virtual environment
````
python3 -m venv your_venv_name
````
> **NB : Make sure that you have installed python3 in your machine**
>
> If it is not the case, install it by typing
> ````
> sudo apt update && sudo apt install python3
> ````

## 4. Activate the python virtual env
````
source your_venv_name/bin/activate
````

## 5. Install requirements.txt packages into you venv
````
pip install -r requirements.txt
````

> Now everything is ready to buil your python CLI app

## 6. Build the task_tracker app folder into a CLI package
````
pip install -e .
````
> This command mean that, we are making our folder to executable python package
> 
> -e or --executable : make executable
>
> . : This folder

And the our project is now a python CLI executable package and we can now test it features.

## 7. To see the available option of our package
````
task-cli --help
````

**Thank You**