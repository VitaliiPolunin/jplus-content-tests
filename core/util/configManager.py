from dynaconf import Dynaconf
from definitions import ROOT_DIR

config = Dynaconf(
    envvar_prefix="DYNACONF",
    settings_files=[f'{ROOT_DIR}/settings.toml', f'{ROOT_DIR}/.secrets.toml'],
    environments=True,
    env="dev"
)


def allureJiraUrl(key):
    return f'{config.JIRA_PATTERN}{key}'

