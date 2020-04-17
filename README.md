# Broadcasthe.net api client

Implements the broadcasthe.net client in python. See https://apidocs.broadcasthe.net/docs.php for specifications about the basis for this implementation

# Example

    from btn import btn
    apikey = 'APIKEY'
    client = btn(apikey)
    client.get_user()


# For forks
Create a secret with name APIKEY and input an appropriate APIKEY you will use to test via github actions

# Tests
In tests dir setup a config.py with APIKEY = 'somekey'
Then run tox
