import pytest
import json
import os
import allure


@pytest.fixture(scope="session")
def env_config(request):
    env = os.getenv('ENV', 'dev')
    with open(f'config/{env}_config.json', 'r') as config_file:
        config = json.load(config_file)

    allure.attach(
        json.dumps(config, indent=2),
        name="env_request_data",
        attachment_type=allure.attachment_type.JSON
    )

    return config


@pytest.fixture(scope="session")
def env_request_data(request):
    env = os.getenv('ENV', 'dev')
    with open(f'data/{env}_request_data.json', 'r') as request_data_file:
        request_data = json.load(request_data_file)

    return request_data


@pytest.fixture(scope="session")
def env_response_data(request):
    env = os.getenv('ENV', 'dev')
    with open(f'data/{env}_response_data.json', 'r') as response_data_file:
        response_data = json.load(response_data_file)

    return response_data
