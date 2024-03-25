import os

from pathlib import Path

import environ

ENV = environ.Env()

BASE_DIR = Path(__file__).resolve().parent.parent.parent

env_path = os.path.join(BASE_DIR, ".env")
if os.path.exists(env_path):
    ENV.read_env(env_path)

ENVIRONMENT = ENV.str("ENVIRONMENT", "unset")
