# NMAMIT CHATBOT Source
## Steps to install
- clone the repo using ```git clone "https://github.com/PramathNaik/chatbotapiNmamit.git"```.
- ```cd``` to folder ```cd chatbotapi```.
- build environment using ```python -m venv env```.
- activate environment using ```source env/bin/activate``` for linux and ```env/scripts/activate``` for windows.
- install required packages using ```pip install -r requirements.txt```.
- create database using ```python manage.py migrate```.
- create admin user using ```python manage.py createsuperuser``` and follow the steps.
- run server using ```python manage.py runserver```.


## Steps to add Responses
In ```response.py``` file of main app.
```
from simple_chatbot.responses import GenericRandomResponse


class your_tag(GenericRandomResponse):
    choices = ("your_response",
               "your_responce",)


class your_tag2(GenericRandomResponse):
    choices = ("your_response",
               "your_responce",)
```               
> Always end the list by using ```,```.even only one response in the list.
Add this Response to your ```SIMPLE_CHATBOT``` in ```setting.py```

```
SIMPLE_CHATBOT = {
    'responses': (
        ("main.responses.your_tag", "yourtag"),
        ("main.responses.your_tag2", "yourtag2"),
    ),
}
```
# Raw Documentation

## Database Models

```Pattern``` - message which might be send by a user. Add a tag to the pattern for being able to identify and response to that message

```Tag``` - includes information about Response class for a specific method.

```Token``` - tokenized words which are referencing to different patterns. The user-input will be identified by different tokens.

```UserMessageInput``` - new inputs from production. It contains information about chosen pattern. You can label that messages later and include them into the system.

## GenericRandomResponse
> It will choose a generic answer from class property choices.

