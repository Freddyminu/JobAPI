# Readme 

> The following sections explain how to install and run each part of the project.
>> - The backend was made using Flask 2.0.3. 
>> - The frontend was made using React.
>> - The database connections were made using SQLite.

## Environment
 - To install and run the backend it is recomended to use the virtual environment. 
 - /JobscoreInternship
 ```
 source backend/venv/bin/activate
 ```

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


