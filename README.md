## Watcher 😷

- Face-mask detection, Person identification &amp; Alerting Web Application

#### Watcher Frontend

- Watcher front end created in html with flask jinja

#### Watcher Backend

- Watcher backend will be created in flask

#### Watcher Model

- Watcher uses cascade classifier to detect a person face
- Watcher model created using CNN which will be used for face mask detection and face recognition

## Folder Structure

- **data_science_component** - This folder have watcher application's core compoents which are face detection, mask detection and face recognition
- **watcher** - This folder have the `Watcher` application
- **features** - Features folder have the features that are planned to add in future

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

## Creating Local Environment

- Use `python3 -m venv venv` to create new vitual environment
- Then use `venv\Scripts\activate` to activate the virtual environment 

## Installing Required Packages

#### Development

- **opencv** - `pip install opencv-python`
- **tensorflow** - `pip install tensorflow`
- **numpy** - `pip install numpy`
- **Keras** - `pip install Keras`
- **Flask** - `pip install flask`
- **Pillow** - `pip install Pillow`
- **twilio** - `pip install twilio`
- **gunicorn** - `pip install gunicorn`
- **pytest** - `pip install pytest`

#### Run

- **opencv** - `pip install opencv-python`
- **tensorflow** - `pip install tensorflow`
- **Flask** - `pip install flask`

### Running Watcher Application

- Open command prompt
- Change the directory to `Watcher\watcher` folder
- Then use `python watcher.py` command to run the watcher application
