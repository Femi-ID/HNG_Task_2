# **Documentation on the HNG Task 2 CRUD Application**

## Standard Request Formats for the Endpoints

#### The API has **3** endpoints you can check out in the views.py:
1. **/:**  The home view to see all user profiles. HTTP Method: **GET**

2. **/api:**  To create/update/delete a person profile. 

- HTTP Methods: **['GET', 'POST', 'PUT', 'PATCH', 'DELETE']**

### Create New Person Profile
Example: NOTE: The first_name field must be a **unique** string value.
HTTP Method: **POST**
Request Format:
- Request Body & Content-Type: application/json
```json
{
  "name": "Doe",
  "bio": "Today's a good day! (optional)"
  }
```
* Response Format:
- HTTP Status: 201 Created
- Response Body: application/json 
```json
{ 
    "id": 1, "name": "Doe",
    "bio": "optional",
    "created": "date created"
}
```

### Retrieve Person Profile by FirstName
* HTTP Method: GET
* Query Parameter: - **name (string)**: The name of the user to retrieve.

* Response Format:
- HTTP Status: 200 OK
- Response Body: application/json 


### Update Person Profile by FirstName
* Description: Update user details by name.
* HTTP Method: **[PUT, PATCH]**
* Query Parameter: -**name (string)**: The name of the user to update.
* Request Format: - Request Body & Content-Type: application/json

* Response Format:
- HTTP Status: 202 Accepted
- Response Body: application/json


### Delete Person Profile by FirstName
* Description: Delete a user by name.
* Endpoint: /api
* HTTP Method: **DELETE**
* Query Parameter: -**name (string)**: The name of the user to delete.
* Response Format: - HTTP Status: 204 No Content



3. **/api/user_id:**  To view details of the person profile. This is where you can READ, DELETE and UPDATE profile details.
    The user_id should be an integer, any other variable type will **not be accepted**. It is the id of the user.
* HTTP Methods: **['GET', 'POST', 'PUT', 'PATCH', 'DELETE']**

### Retrieve Person by ID
* Description: Retrieves user details by their ID.
* Endpoint: /api/<user_id>
* HTTP Method: **GET**
* Response Format:
- HTTP Status: 200 OK  Response Body: application/json 

### Update Person by ID
* Description: Updates user details by their ID.
* Endpoint: /api/user_id
* HTTP Method: **PUT**

### Delete Person by ID
* Description: Deletes a user by their ID.
* Endpoint: /api/user_id
* HTTP Method: **DELETE**

### Example:
A user with the id=1, would view his/her profile by hitting the endpoint: ```domain.com/api/1```.
Then such user can **read, edit** and **delete** his/her profile.

## Error Handling
The common errors that are customised in this application: 400, 401, 403, 404, 405 and 500.
They return a html page with a brief explanation of what went wrong.

## Limitations/ Assumptions

The create user endpoint does not login the user This means the user data is not passed to the request session.
No form of authentication. The application only emphasis on basic **CRUD** functionalities.

## Deploying your application 

##### Locally:
* Add your app to the list of installed apps in your settings. In this format: 
```my_app.apps.MyAppConfig```
* Still in your settings; Add your template directory for django to find your error html files. Only do this if you've made changes to the current setup.
```TEMPLATE_DIR = os.path.join(BASE_DIR, 'templates/errors')```
* You can set _Debug = False_ to test the custom error handling.


##### Server:
* Set Debug = False
* Include your domain name in the allowed hosts list.

**Check the [README](https://github.com/Femi-ID/HNG_Internship_task_2) for more info on running the server locally.**
#### _And your good to go!_

