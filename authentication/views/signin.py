from aiohttp import ClientSession, web
from urllib.parse import quote
from jwt import encode
from hashlib import sha256


async def signin(request):
    async with ClientSession() as session:
        data = await request.json()
        password_type = data["type"]
        password = data['password']
        username = data['username']

        validate_url = request.app['config']['users']['url'] + '/v1/users/{}/validate/'.format(
            quote(username, safe=""))

        if password_type.lower() not in ["plain", "sha256"]:
            return web.json_response(data={"error": "Invalid password type"}, status=400)

        if password_type.lower() == "plain":
            password = sha256("{}_{}".format(username, password).encode()).hexdigest()

        new_data = {
            "password": password
        }

        async with session.post(validate_url, json=new_data) as resp:
            if resp.status != 204:
                return web.json_response(data={"error": "Incorrect username or password"}, status=400)

        result = {"username": data['username']}
        token = encode(result, request.app["config"]["keys"]["private"], algorithm="ES256")

        return web.json_response(data={"token": token.decode()})
