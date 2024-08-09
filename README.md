# Global mind
This is a simple HTTP server for checking and downloading device firmware.

## Installation
- Clone the repository: 
``` Copy code
git clone https://github.com/Goltzishpt/global_mind
```

- Navigate to the project directory: 
``` bash Copy code
cd global_mind
```

## Usage
- Enter the command below into the terminal or run it by clicking on the arrows on the left.
``` bash Copy code
docker-compose up --build -d
```
- After build create a user and location(example below)

``` bash Copy code
curl -X POST http://0.0.0.0:8080/add_user \
-H "Content-Type: application/json" \
-d '{"name": "User1", "email": "user1@example.com", "password": "password"}'
```
``` bash Copy code
curl -X POST http://0.0.0.0:8080/add_user \
-H "Content-Type: application/json" \
-d '{"name": "User1", "email": "user1@example.com", "password": "password"}'
```

- After you could make CRUD operation with device

``` bash Copy code
curl -X POST http://0.0.0.0:8080/add_device \  
-H "Content-Type: application/json" \
-d '{"name": "Device1", "type_data": "TypeA", "login": "user1", "password": "pass1", "location_id": 1, "api_user_id": 1}'
```

``` bash Copy code
curl -X GET http://0.0.0.0:8080/device/1  
```

``` bash Copy code
curl -X PUT http://0.0.0.0:8080/device/1 \
-H "Content-Type: application/json" \
-d '{"name": "Device1Updated", "type_data": "TypeB"}'
```

``` bash Copy code
curl -X DELETE http://0.0.0.0:8080/device/1
```
