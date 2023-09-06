<p align="center">
<img src="http://nano.sahaj.ai/27ad2091b1714f583886.png" width="320" height="162" alt="Logo" title="NaN(O) logo">
</p>

# Employee Management - a NaN(O) problem
  
## What is NaN(O)

At Sahaj, tech consultants operate at the intersection between engineering and art. Simply put, they are artisans who take on complex engineering problems in the software industry across a wide spectrum of domains. Their work is deeply rooted in first principles thinking - asking fundamental questions to dissect and understand a problem which eventually leads to one-of-a-kind solutions, each as distinct as a fingerprint.

Through NaN(O), a hackathon driven by Sahaj across multiple colleges in India, they want to instill a culture of applying first principles thinking to a problem statement.

## Problem statement

You are writing an employee management system. This is a huge task for a limited amount of time, therefore, the client has asked you to only work on the backend. This has also been done a lot of times, so the client only needs you to implement 4 funtionalities only. He wants to see how well you code, therefore, he isn't a fan of AI pair programing tools (ChatGPT, BingAI or Bard or anything of the sort).

The 4 functionalities you need to implement are: Create, Read (by ID), Search and Find-All. The client also has a starter project (which is based on Flask framework), which he has given you - because he is a nice person. If you do not want to use micronaut, you are welcome to swap things out. However, if you are a beginner, we do not recommend this.

Requests will be accepted over HTTP as mentioned in the ([API contract](#api-contract)). No databases/libraries can be used to store/maintain data.

There is also an `api-sample.md` you can look at 😄.

(Fastest applications win)[https://knowyourmeme.com/memes/i-am-speed].

------

### Technical details
1. Your repository needs to have a `Dockerfile` that starts your HTTP web app (This is already given!)
2. Your HTTP app need to expose APIs ([API contract](#api-contract)) on port 8080 (Also all done, unless you mess around and break things)
3. No existing databases, libraries and services can be used to store the data
4. Application needs to persist data across restarts
5. No limitation on the programming language
6. Do not touch the GitHub actions code. It is used to test your code automatically and score it. Any modifications will lead to immediate disqualification.
7. Maximum time a single request can take is 5 seconds
8. Data should be persisted in `/home/`
9. Do not touch the GreetingController. Let it be.

#### FAQ
1. Do not run a development webserver with watch enabled in your app. Your tests will fail.
2. If your greeting end point test is not passing, please check the output you produce. It needs to be exactly what is requested.
3. When in doubt, please check the Github Actions logs for details
4. Logs for the performance tests will not be shared

## Data to be stored
```
{
    employeeId: string,
    name: string,
    city: string
}
```

---
## API contract

***
>##### GET /greeting
Checks whether the service is available.

###### Response
* Code: 200
* Content: `Hello world!`
---

>##### POST /employee
Creates a new Employee and returns the employeeId

###### Request & Response headers
Content-Type: application/json

###### Body
```
{
    name: string,
    city: string
}
```
###### Success Response
* Status code: 201
* Content: `{ "employeeId": "<employee_id>" }` (Note: Employee ID is a `string`)
---

>##### GET /employee/:id
Returns the specified employee.

###### URL Params
`id=[string]` *Required*

###### Success Response
* Status code: 200
* Content: `{ <employee_object> }`

###### Error Response
* Status code: 404
* Content: `{ message : "Employee with <employee_id> was not found" }`
---

##### POST /employees/search
Search employees with different criteria.

Search by name
###### Headers
Content-Type: application/json

###### Body

```
{
    "fields": [<filter-criterion>],
    "condition": "<AND|OR>" 
}
```

*   `fields` is *required*, and  `filter-criterion` is of the following shape
  ```
  {
      fieldName: string,
      eq: string,
      neq: string
  }
  ```

`fieldName` is *required* and can be either of
* `name`
  * `city`

Either of `eq` or `neq` needs to be supplied - never both.
`eq` and `neq` hold string values to check for, respectively, equality or non-equality of the value stored in the requested `fieldName`.

* `condition` is *optional* and its value is *AND* by default. Allowed values are
  * AND
  * OR

Examples:
```json
{
    "fields": [
        {
            "fieldName": "name",
            "eq": "Apple"
        }
    ]
}
```

```json
{
    "fields": [
        {
            "fieldName": "name",
            "eq": "Apple"
        },
        {
            "fieldName": "city",
            "neq": "Mumbai"
        }
    ],
  "condition": "OR"
}
```

###### Success Response
* Status code: 200
  * Content: `[{ <employee_object> }]`
---


##### GET /employees/all
Return the list of all employees.

###### Headers
Content-Type: application/json

There is no request body or Params.

###### Success Response
* Status code: 200
* Content: `[{ <employee_object> }]`

----
[API Sample Request Response](api-sample.md)
---
## Competition rules

Check <a href="http://nano.sahaj.ai/rules.html" target="_blank">rules and scoring</a> pages for details. When in doubt, ask the organizers and we will add clarifications to the page.


## Sample Instructions for coding/committing
* git clone `git repository url` (Skip this step if using github codespaces)
* cd `repository name` (Skip this step if using github codespaces)
* Check for health check [GreetingController.java](src/main/java/ai/sahaj/nano/controller/GreeingController.java)
* Goto [EmployeeController.java](src/main/java/ai/sahaj/nano/controller/EmployeeController.java)
* Begin coding
* Code needs to be tested via github? Execute following commands in the terminal location of your repository
  * git add .
  * git commit -m 'any message regarding your changes'
  * git push
* Wait for build to complete in github actions logs.
* If build is green, you should see the score on the leader board, else check with actions logs.

## Sample Instructions for Codespaces installation
* On your browser after accepting the github invitation,
  * Celect "Code" dropdown
  * Select the "Codespaces" tab.
  * Select "Create codespace on main"
* Inside codespace terminal
  * sdk install java 17.0.7-tem
  * Enter "y" once installation is complete
* Continue from step 3 of Sample Instructions for coding/commit
