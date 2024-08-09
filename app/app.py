import asyncio
from aiohttp import web
from peewee import IntegrityError
from playhouse.shortcuts import model_to_dict

from forms import ApiUserForm, LocationForm, DeviceForm
from models import ApiUser, Location, Device
from core.database.manager import db

from settings import ServerSettings


async def add_user(request):
    data = await request.json()
    user_data = ApiUserForm(**data)

    try:
        user = ApiUser.create(
            name=user_data.name,
            email=user_data.email,
            password=user_data.password
        )
        return web.json_response(
            {'status': f'User added successfully: ID {user}'}
        )
    except Exception as e:
        print(e)


async def add_location(request):
    data = await request.json()
    location_data = LocationForm(**data)

    try:
        location = Location.create(
            name=location_data.name
        )
        return web.json_response(
            {'status': f'Location added successfully: ID {location}'}
        )
    except Exception as e:
        print(e)


async def add_device(request):
    data = await request.json()
    device_data = DeviceForm(**data)

    if not all([
        device_data.name, device_data.type_data, device_data.login,
        device_data.password, device_data.location_id,
        device_data.api_user_id
    ]):
        return web.json_response(
            {'error': 'Missing required fields'}, status=400
        )

    try:
        device = Device.create(
            name=device_data.name,
            type_data=device_data.type_data,
            login=device_data.login,
            password=device_data.password,
            location_id=device_data.location_id,
            api_user_id=device_data.api_user_id
        )
        return web.json_response(
            {'status': f'Device added successfully: ID {device}'}
        )

    except IntegrityError:
        return web.json_response(
            {'error': 'Device already exists'}, status=400
        )
    except Exception as e:
        return web.json_response({'error': f'Error: {e}'})


async def get_device(request):
    try:
        device_id = int(request.match_info['id'])
        device = Device.get_by_id(device_id)
        device_dict = model_to_dict(device)

        return web.json_response(device_dict)

    except Device.DoesNotExist:
        return web.json_response({'error': 'Device not found'}, status=404)
    except Exception as e:
        return web.json_response({'error': f'Error: {e}'}, status=500)


async def update_device(request):
    device_id = request.match_info.get('id')
    data = await request.json()

    try:
        device = Device.get_by_id(device_id)

        device.name = data.get('name', device.name)
        device.type_data = data.get('type_data', device.type_data)
        device.login = data.get('login', device.login)
        device.password = data.get('password', device.password)
        device.location_id = data.get('location_id', device.location_id)
        device.api_user_id = data.get('api_user_id', device.api_user_id)

        device.save()

        return web.json_response(
            {'status': f'Device updated successfully: ID {device_id}'}
        )

    except Device.DoesNotExist:
        return web.json_response({'error': 'Device not found'}, status=404)
    except Exception as e:
        return web.json_response({'error': f'Error: {e}'})


async def delete_device(request):
    device_id = request.match_info.get('id')

    try:
        device = Device.get_by_id(device_id)
        device.delete_instance()
        return web.json_response(
            {'status': f'Device deleted successfully: ID {device_id}'}
        )

    except Device.DoesNotExist:
        return web.json_response({'error': 'Device not found'}, status=404)
    except Exception as e:
        return web.json_response({'error': f'Error: {e}'})


async def on_startup(app):
    print("Creating tables blin...")
    db.create_tables(ApiUser, Location, Device)
    print("Tables created.")


async def init_app():
    app = web.Application()
    app.router.add_post('/add_device', add_device)
    app.router.add_get('/device/{id}', get_device)
    app.router.add_put('/device/{id}', update_device)
    app.router.add_delete('/device/{id}', delete_device)
    app.router.add_post('/add_user', add_user)
    app.router.add_post('/add_location', add_location)

    app.on_startup.append(on_startup)

    return app


def main():
    loop = asyncio.get_event_loop()
    app = loop.run_until_complete(init_app())
    server_settings = ServerSettings()
    web.run_app(app, host=server_settings.host, port=server_settings.port)


if __name__ == '__main__':
    main()

