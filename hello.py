#!/usr/bin/env python3
import connexion

app = connexion.FlaskApp(__name__, specification_dir='swagger/')


def post_greeting(name: str) -> str:
    return 'Hello {name}'.format(name=name)


app.add_api('helloworld-api.yaml', arguments={'title': 'Hello World Example'})

if __name__ == '__main__':
    app.run()
