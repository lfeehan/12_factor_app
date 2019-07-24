#!/usr/bin/env python

# model import is required to set up database correctly
from app.models import db, User, Filter
from app import create_app
from config import base
from app.api.utils import init_demo_state

from app.api.routes import init_demo

app = create_app(base, db)


if __name__ == '__main__':
    #do some setup
    
    example_users = [
        {
            "id": 1,
            "name": "person one",
            "wallet": "0x487f2982bd1593cc1fdd9104b618909deae0aafa",
            "balance": 100,
            "filters": [
                {"name": "criteria_a", "type": "bool", "goal": "max", "value": 1},
                {"name": "criteria_b", "type": "bool", "goal": "min", "value": 0},
            ]
        },
        {
            "id": 2,
            "name": "person two",
            "wallet": "0x75a36fe489a8a6aac8f3b72af7dee6bfaed3728e",
            "balance": 200,
            "filters": [
                {"name": "criteria_a", "type": "bool", "goal": "max", "value": 1},
                {"name": "criteria_b", "type": "bool", "goal": "min", "value": 0},
            ]
        },
    ]

    ## Seed the database if empty
    if not list(User.query.filter({})):
        for e in example_users:
            filters = []
            for f in d['filters']:
                filters.append(Filter(name=f['name'], type=f['type'], goal=f['goal'], value=f['value']))
            usr = User(name= d["name"], wallet= d["blockchain"], balance= d["balance"], filters=filters)
            usr.save()
    
    with app.app_context():
        init_demo(unlock=True)
        app.run(host='0.0.0.0', use_reloader=False)
