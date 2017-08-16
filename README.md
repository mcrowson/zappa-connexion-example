# Connexion Example in Zappa

Using the [Hello World Example](https://github.com/zalando/connexion/tree/master/examples/helloworld) from Connexion and
deploying on [Zappa](https://github.com/Miserlou/Zappa).

```bash
virtualenv -p python3 env
source env/bin/activate
pip install -r requirements.txt
zappa init
zappa deploy
```

NOTE: Make sure you delete the `zappa_settings.json` file in this project so that your
call to `zappa init` creates yours correctly. 