from app import app

def test_homepage():
    # Create a test client for the Flask app
    client = app.test_client()
    
    # Make a request to the homepage
    response = client.get('/')
    
    # Check if the status code is 200 (OK)
    assert response.status_code == 200
    
    # Check if the text "Hello" is in the response
    assert b'Hello' in response.data
