# Technical exercise

![Me trying to explain this](CharlieDay.jpg)

Thank you all for being here today, I hope that this *readme* explains the layout of this project clearly. It's not as crazy as it looks, I promise!

# Requirements
These are usually already present on any developer's system, but just in case:
- *Bash* shell, in order to run `start-docker-compose.sh`
- Docker, to run the web API and database
- Python 3, to run the CLI app

Once you have these requirements, we are ready to go!

# Instructions
## Start up the web API and database
Simply run `start-docker-compose.sh` - told you it was easy!

When finished, enter `Control + C` to stop the process. The Bash script should gracefully stop and remove the Docker containers for you.

## CLI app
I've provided a `requirements.txt` that you can use to install the same versions of the Python `requests` library as me into your virtual environment - you do use virtual environments, *don't you*?

```bash
# Using pip
pip install -r requirements.txt

# Using Conda (it's okay, we all make mistakes)
conda create --name <env_name> --file requirements.txt
```

To run:
```bash
python3 cli-app.py
```

# Architecture
This project has the following architecture:
```
  Containers     Local Machine
+-------------+
| Web UI Site |
|   (Nginx)   |
|     80      |
+------+------+
       |
  +----V----+    +------------+
  | Web API <----+  CLI App   |
  | (Flask) |    | (Python 3) |
  |  8080   |    +------------+
  +----+----+
       |
+------V-----+
|  Database  |
| (Postgres) |
|    5432    |
+------------+
```

To be explicit, the project uses *Docker Compose* to spin up the web API and database inside Docker containers.

Meanwhile the CLI app is designed to just be run on the local machine.

# Database
This database is populated with table containing the *IBM HR Analytics Employee Attrition & Performance* dataset, avaliable at https://www.kaggle.com/pavansubhasht/ibm-hr-analytics-attrition-dataset.

I've opted to use a Postgres database to store the data. I chose this because although the dataset is a single CSV file, it looks to be relational in nature i.e. there are a few columns which look like they should have a foreign key with a reference table for their values (namely `Business Travel`, `Department`, `Education Field`, `Job Role` and `Marital Status`).

However it should be noted that the choice between a *NoSQL* and a relational database shouldn't really matter for the purposes of this exercise, I just feel a relational implementation it makes it a bit of a more realistic scenario.

Ideally I would examine the columns for unique values and recreate the corresponding reference tables I mentioned but I don't think any additional value would be added doing this.

For similar reasons, the table `employees` is simply placed in the public schema.

Note: I have made all the columns nullable (except the primary key, `Employee Number`, obviously) to make inserting new data into the table easier. In real life it would have to be considered which columns should be nullable and which aren't, but that's outside the scope of this exercise.

# Web Server
I chose to write the web server using the Python framework *Flask*, mainly because I haven't created a server in Python before and it was the simplest to get started with quickly.

*Note*: The documentation states that server Flask provides is not appropriate for production; do not fear 'cause in production you would have a *real* web server like *Nginx* in front of it anyway to handle SSL, CSP and potentially other things like load balancing etc.

*Note 2*: The web server is "*publically*" exposed on port 8080, but internally in the container it's running with Flask's native port 5000.

## Endpoints

### Get the percentage of attrition
```
GET http://localhost:8080/attrition
```

How much attrition is there?

Calculated as the percentage of employees that had attrition, out of the total employees.

Example cURL request:
```bash
curl http://localhost:8080/attrition
```

### Get the percentage of people with attrition, who also worked overtime
```
GET http://localhost:8080/attrition-overtime
```

I wanted to see if the employees being overworked could potentially be a cause of attrition. i.e. the percentage of employees that worked overtime, out of the total number of employees *that had attrition*.

Example cURL request:
```bash
curl http://localhost:8080/attrition-overtime
```

### Add an employee to the database
```
POST http://localhost:8080/add-row
{"employeeNumber": 123, "attrition": true}
```

As it says on the tin. Allows the user to add an employee to the database and record if they had attrition. I didn't add any other fields because it would quickly become extremely tedious to input manually and this is just a demonstration.

Example cURL request:
```bash
curl --request POST \
    --header "Content-Type: application/json" \
    --data '{"employeeNumber": 123, "attrition": true}' \
    http://localhost:8080/add-row
```

# CLI App
I think it explains itself. Run it and see!

```bash
python3 cli-app.py
```

I would recommend creating a virtual environment in this directory to install the dependencies. See [Instructions](#Instructions).

# Web UI Site

I also made a small frontend that communicates with the server, this essentially replaces the CLI app with a webpage that does the same things.

The site runs on port 80. I use a small Nginx server to serve the static files and host them.

The site can be accessed at
```
http://localhost:80/
```

Navigate to it in your favourite browser.

