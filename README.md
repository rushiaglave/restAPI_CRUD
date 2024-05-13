# Django REST API for CRUD Operations

This project is a Django-based RESTful API implementation for CRUD operations on employee details.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Endpoints](#endpoints)
- [Examples](#examples)
- [Contributing](#contributing)
- [License](#license)

## Features

- Implements CRUD operations (Create, Read, Update, Delete) for managing employee details.
- Utilizes Django Framework and Django Rest Framework for efficient API development.

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/rushiaglave/restAPI_CRUD.git
   ```
2. Install dependencies:
   ```
   pip install djangorestframework
   ```
3. Apply database migrations:
   ```
   python manage.py migrate
   ```
   
## Usage

To start the server, run:
```
python manage.py runserver
```

## Endpoints

- **admin/** - Django administration panel.(username and password both is admin)
- **task-list/** - Get a list of all employees.
- **task-listid/{pk}/** - Get a list of employees by there unique id
- **task-create/** - Create a new employee record.
- **task-update/{pk}/** - Update an employee record by ID.
- **task-delete/{pk}/** - Delete an employee record by ID.

## Examples

### Create a new employee
```http
POST /task-create/
Content-Type: application/json

{
  "id": 1,
  "firstname": "John",
  "lastname": "Doe",
  "emp_id": 1234
}
```

### Update an employee
```http
PUT /task-update/1/
Content-Type: application/json

{
  "id": 1,
  "firstname": "John",
  "lastname": "Doe",
  "emp_id": 5678
}
```

### Delete an employee
```http
DELETE /task-delete/1/
```

## Contributing

Contributions are welcome! Feel free to open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).

