import requests
import os
import environ
env = environ.Env()
# reads .env file
environ.Env.read_env("../bot/.env")

token = os.environ["TOKEN"]


def setWebHook(hook_url):
    url = f"https://api.telegram.org/bot{token}"
    r = requests.get(f"{url}/setWebHook", params={"url": hook_url})
    print(r.status_code)
    print(r.json())


if __name__ == "__main__":
    setWebHook("")
