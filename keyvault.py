from azure.keyvault import KeyVaultClient, KeyVaultAuthentication
from azure.common.credentials import ServicePrincipalCredentials

credential = None


def auth_callback(server, resource, scope):
    credentials = ServicePrincipalCredentials(
        client_id='952370c2-1f28-4256-b8c2-b241dca14159',
        secret='0n6rvVkXf9Q9uoFbKIvCdEGtGvlThri0bMQeA/4qgTk=',
        tenant='97df8ec2-114e-45ae-a59c-1f8c4ae0a138',
        resource="https://vault.azure.net"
    )
    token = credentials.token
    return token['token_type'], token['access_token']


client = KeyVaultClient(KeyVaultAuthentication(auth_callback))

# key_bundle = client.get_key(vault_url, key_name, key_version)

key_bundle = client.get_key('https://kv-dev-hk-peak-di-test.vault.azure.net/', 'mykey', 'e46409882744455c8a7ffee227777e09')
secret_bundle = client.get_secret('https://kv-dev-hk-peak-di-test.vault.azure.net/', 'mysecret', 'fd65e2dada364f9b9211b0a26743bb05')
print(secret_bundle.value)
print(key_bundle.key)