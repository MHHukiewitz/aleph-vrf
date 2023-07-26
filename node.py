from aleph.sdk.vm.app import AlephApp
from fastapi import FastAPI

http_app = FastAPI()
app = AlephApp(http_app)

