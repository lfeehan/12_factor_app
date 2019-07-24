from app.models import User
from flask import current_app, jsonify


def get_config():
    config_val = current_app.config['A_CONFIG_VALUE']
    return (config_val)

def init_demo(somethings=False):
    #do some init
    return

def my_utility_function(contract):
    for user in User.query.all():
        user.balance = 0
        user.save()
    return
