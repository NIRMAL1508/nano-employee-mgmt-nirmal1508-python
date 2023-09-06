## Data to be stored
```
{
    employeeId: string,
    name: string,
    city: string
}
```
---
## API
***

>##### GET /greeting
###### Response
* Code: 200
* Content: `Hello world!`
---

>##### POST /employee
###### Request & Response headers
Content-Type: application/json
###### Body
```
{
    "name": "Big(O)",
    "city": "Mumbai"
}
```
###### Success Response
* Status code: 201
* Content:
```
{
  "employeeId": 1,
  "name": "Big(O)",
  "city": "Mumbai"
}
```
---

>##### GET /employee/1
###### URL Params
###### Success Response
* Status code: 200
* Content:
```
{
  "employeeId": 1,
  "name": "Big(O)",
  "city": "Mumbai"
}
```
>##### GET /employee/3
###### Error Response
* Status code: 404
* Content:
```
{ message : "Employee with 3 was not found" }
```
---

>#### GET /employees/all
###### URL Params: None
###### Success Response
* Status Code: 200
* Content:
```
[
   {
      "employeeId": 1,
      "name" : "Big(O)",
      "city", "Mumbai"
   }
]
```
-----

> ##### POST /employees/search
###### URL Params: None

###### Request Body
```
{
    "fields": [
        {
            "fieldName": "name",
            "eq": "Big(O)"
        }
    ]
}
```

Response Body
```
[
    {
        "employeeId": 1,
        "name": "Big(O)",
        "city": "Mumbai"
    }
]
```
----

> #### Another example:
###### Request body:
```
{
    "fields": [
        {
            "fieldName": "name",
            "neq": "Apple"
        }
    ]
}
```
Response Body
```
[
    {
        "employeeId": 1,
        "name": "Big(O)",
        "city": "Mumbai"
    }
]
```

-------

> #### Another example:
###### Request body:

```JSON
{
    "fields": [
        {
            "fieldName": "name",
            "eq": "Apple"
        },
        {
            "fieldName": "city",
            "eq": "Mumbai"
        }
    ],
    "condition": "OR"
}
```

###### Response body:

```
[
    {
        "employeeId": 1,
        "name": "Big(O)",
        "city": "Mumbai"
    }
]
```
-----

#### Few other requests

```json
{
    "fields": [
        {
            "fieldName": "name",
            "eq": "Apple"
        },
        {
            "fieldName": "city",
            "eq": "Mumbai"
        }
    ]
}
```


```json
{
    "fields": [
        {
            "fieldName": "city",
            "neq": "Mumbai"
        }
    ]
}
```