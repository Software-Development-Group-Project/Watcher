# Watcher 😷

**Face-mask detection, Person identification &amp; Alerting Web Application.**

**Watcher front end created in html/css with jinja. Watcher backend created in flask.**

**Watcher uses cascade classifier to detect a person's face and uses CNN for face recognition and face mask detection.**

## Folder Structure

- **data_science_component** - This folder have watcher application's core compoents which are face detection, mask detection and face recognition (models and notebooks).
- **watcher** - This folder have the `Watcher` application
- **features** - Features folder have the features that are planned to add in future.

## Required Packages

`opencv_python==4.5.1.48`
`tensorflow==2.4.1`
`numpy==1.19.5`
`Keras==2.4.3`
`Flask==1.1.2`
`Pillow==8.2.0`
`twilio==6.56.0`
`gunicorn==19.9.0`
`pytest==5.4.1`

## Creating Virtual Environment

- Use `python3 -m venv venv` to create new vitual environment.
- Then use `venv\Scripts\activate` to activate the virtual environment. 

## Installing Required Packages

- **opencv** - `pip install opencv-python`
- **tensorflow** - `pip install tensorflow`
- **numpy** - `pip install numpy`
- **Keras** - `pip install Keras`
- **Flask** - `pip install flask`
- **Pillow** - `pip install Pillow`
- **twilio** - `pip install twilio`
- **gunicorn** - `pip install gunicorn`
- **pytest** - `pip install pytest`

### Running Watcher Application

- Clone the Watcher github repository.
- Then open new command prompt.
- Change the directory to `Watcher\watcher` folder
- Create new virtual environment for the cloned repositary.
- Activate the environment.
- Install the required packages.
- Then use `python watcher.py` command to run the watcher application
