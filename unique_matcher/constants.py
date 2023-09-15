"""Constants and configuration."""
import tomllib
from pathlib import Path

ROOT_DIR = Path(__file__).parent.parent.resolve()

# Load version
with open(ROOT_DIR / "pyproject.toml", "rb") as fread:
    _data = tomllib.load(fread)
    VERSION = _data["tool"]["poetry"]["version"]

# Directory definitions
ITEM_DIR = ROOT_DIR / "items"
SOCKET_DIR = ROOT_DIR / "socket"
TEMPLATES_DIR = ROOT_DIR / "templates"

DATA_DIR = ROOT_DIR / "data"
QUEUE_DIR = DATA_DIR / "queue"
ERROR_DIR = DATA_DIR / "errors"
DONE_DIR = DATA_DIR / "done"
LOG_DIR = DATA_DIR / "logs"
RESULT_DIR = DATA_DIR / "results"

# Maximum size of an item image for comparison
# (might differ from artwork found on wiki)
ITEM_MAX_SIZE: tuple[int, int] = (104, 208)

# If enabled, the Matcher object will gather debug data for later use
DEBUG: bool = True

# Allow screenshots that are not 1920x1080px, it will reduce accuracy
# Default: False
OPT_ALLOW_NON_FULLHD: bool = True

# Enable item name matching for identified items
# Default: True
OPT_FIND_ITEM_BY_NAME: bool = False

# Ignore non-global drops, i.e. boss drops, metamorph drops, etc.
# Default: True
OPT_IGNORE_NON_GLOBAL_ITEMS: bool = True
