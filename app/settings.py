import os

class Settings:

    BASE_API_PREFIX = os.getenv("BASE_API_PREFIX")
    SERVICE_URL = os.getenv("SERVICE_URL")
    SERVICE_AUDIENCE_URL = os.getenv("SERVICE_AUDIENCE_URL")
    ROOT_PATH = "" if os.getenv("LOCAL") == "True" else "/hc-middle"
