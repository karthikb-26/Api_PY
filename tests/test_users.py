# from tests.utils import APIClient
from tests.api_client import APIClient
from tests.schema_validator import validate_response_schema


user_schema = {
    "type": "object",
    "properties": {
        "page": {"type": "integer"},
        "per_page": {"type": "integer"},
        "total": {"type": "integer"},
        "data": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "id": {"type": "integer"},
                    "email": {"type": "string"},
                    "first_name": {"type": "string"},
                    "last_name": {"type": "string"}
                },
                "required": ["id", "email", "first_name", "last_name"]
            }
        }
    }
}

def test_get_users():
    """Test GET /users API"""
    response = APIClient.get("/users?page=2")

    assert response.status_code == 200, "Expected status code 200"
    assert response.elapsed.total_seconds() < 2, "Response time too high"

    data = response.json()
    assert validate_response_schema(data, user_schema), "Response does not match schema"

def test_create_user():
    """Test POST /users API"""
    payload = {"name": "John", "job": "QA Engineer"}
    response = APIClient.post("/users", payload)

    assert response.status_code == 201, "Expected status code 201"

    data = response.json()
    assert "id" in data, "Response JSON does not contain 'id'"
    assert "createdAt" in data, "Response JSON does not contain 'createdAt'"

def test_update_user():
    """Test PUT /users API"""
    payload = {"name": "John Updated", "job": "Senior QA"}
    response = APIClient.put("/users/2", payload)

    assert response.status_code == 200, "Expected status code 200"

    data = response.json()
    assert "updatedAt" in data, "Response JSON does not contain 'updatedAt'"

def test_delete_user():
    """Test DELETE /users API"""
    response = APIClient.delete("/users/2")

    assert response.status_code == 204, "Expected status code 204"
