
Clone the repository:
git clone https://github.com/m-romeu/python_api.git
cd python_api

Start the services:
docker-compose up --build

Verify the API is running:
http://localhost:8002/ping

Interact with all endpoints:
http://localhost:8002/docs

Testing endpoints:
Health check: curl http://localhost:8002/ping

Running tests:
docker-compose exec web pytest