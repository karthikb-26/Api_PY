from jsonschema import validate

def validate_response_schema(response_json, expected_schema):
    """
    Validate API response structure against expected JSON schema.
    """
    try:
        validate(instance=response_json, schema=expected_schema)
        return True
    except Exception as e:
        print(f"Schema Validation Error: {e}")
        return False
