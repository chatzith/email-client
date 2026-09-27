"""Load subject-pattern mappings for email use-case dispatch."""

from pathlib import Path

import yaml
from pydantic_settings import BaseSettings

APP_PATH = Path(__file__).parent.resolve()
SUBJECTS = Path.joinpath(APP_PATH, "scenario.yaml")

with open(SUBJECTS) as f:
    cases = f.read()


class Settings(BaseSettings):
    """Provide subject-pattern to use-case mappings loaded from YAML."""

    usecases: dict = yaml.safe_load(cases)
