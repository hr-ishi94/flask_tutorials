# FLASK TUTORIALS 

## 1. TO-DO APP

Now for our application, we are going to split the code into 3 parts
- app.py — the entry & exit point to our application
- service.py — converts the request into a response.
- models.py — handles everything that involves a Database.

## Why do we need 3 separate files?

Standards — One of the important things that is missed in a beginner tutorial is the standards or patterns that need to be followed. By separating the app into 3 different files we are separating *the business logic(service.py)*, *the application layer(app.py)*, and *the data(models.py)*. In technical terms, this is called an **MVC — Model View Controller Pattern**.


*Reference : Medium - https://medium.com/p/b039d11f101c#4d5a*
