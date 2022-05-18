# Readme 
 - Firstly i'd like to thank jobscore for giving me the chance of showing them what i am capable of! =) <br>
 - I think its important to mention that i've never done anything like this and its the first time that i'm doing multiple things during the creation of this project.

> The following sections explain how to install and run each part of the project.
>> - The backend was made using Flask 2.0.3. 
>> - The Frontend was made using React.
>> - The database connections were made using SQLite.


## Backend
 - You must be in the backend directory to use the makefile.
 - /backend
```
make                    -installs dependencies 

make database           -cleans and creates a table

make start              -starts the backend
```


## Frontend
 - You must be in the frontend directory to use the npm commands.
 - /frontend
```
npm install             -installs dependencies 

npm start               -starts the frontend
```
 
---

Its important that a post request is made to the server via http://localhost:5000/jobs otherwise nothing will appear on the webpage.
The application used to do this was Postman, there i sent a POST request with the JSON that Fernando gave me. 
The link to the JSON is https://careers-demo.jobscore.com/careers/reveltn/feed.json. 

