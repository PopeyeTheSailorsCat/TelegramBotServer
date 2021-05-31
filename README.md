Half of the fourth laboratory work in a cycle on the subject of User Interface Development.  
Other half located here: https://github.com/PopeyeTheSailorsCat/TelegramBot
# TelegramBotServer
This is a student project in which we create a Telegram bot, 
and a Django server to work with this bot. Interaction is carried out via the REST API. 
The server and bot are deployed on Heroku.

The interaction between this repository and the heroku repository is carried out via Jenkins with the push project build.
Programming language is Python 3.7

## Repository content
In this repository, we have two main folders:  
 * Django server folder(server)
 * Django's application folder (weather_gateway).

Also in this repository there is an MIT license and files related to the launch of the heroku server

## Running Django server locally
To start Django on you local machine you will need python at first.
Install Django running
```commandline
    > pip install Django
```

After that start server from a console in the project root.
```commandline
    > python manage.py runserver
```
After this you only need to do some additional stuff you can find later in this README.

## Deploy Django server on heroku
Repository already have all needed for running django application on heroku. All you need is to create heroku repo for your project and push this repo there (https://devcenter.heroku.com/articles/getting-started-with-python).
Also add your new server address to ALLOWED_HOSTS in 'server/setting.py'  

After this you only need to do some additional stuff you can find later in this README.


## Additional step
In order for the bot to interact with your server, you need to specify the url of your server in the bot's config.
### Running on server
Write yours server url at bot repository 'src/config.py' in server_gateway_api["root"], so it will look like this.
```python
    server_gateway_api = {"root": "your_server_url", "open_weather": "openweather"}
```
### Running on local
To allow the bot to access the local server, you need to make the local server available from the network/
There are several ways to achieve this. One of them is to use localhost.run to host access to your local server (https://localhost.run/).
On their website, you can find a simple guide to the host. 
After you want your local address, you should be given your url.
It should be added as indicated in Running on server
# Development team
1. Mamaeva Anastasia

     work email: mamaeva.as@edu.spbstu.ru
    
2. Vedenichev Dmitry

     work email: vedenichev.da@edu.spbstu.ru 
