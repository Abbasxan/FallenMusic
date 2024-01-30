from os import getenv

from dotenv import load_dotenv

load_dotenv()


API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")

BOT_TOKEN = getenv("BOT_TOKEN", None )
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "90"))

OWNER_ID = int(getenv("OWNER_ID", "5045429385"))

PING_IMG = getenv("PING_IMG", "https://telegra.ph/file/a85a94c666e60602e0ec3.jpg")
START_VIDOE = getenv("START_VIDOE", "https://graph.org/file/6e8a634809daa3c0ddff6.mp4")

SESSION = getenv("SESSION", "AgHGBPAApE9Sedjt9mV_6rNszqBp6vSdcj-7MbJk_KLMb-W3qvQUBgeGwyADCtK_qKxf7L4cFexnmcQHqQtHgxftiY4KwY19z6SChoIOFWmfshN9GO535Pr9uYb8KieiavhB9e9YqYY3ME3t56zypoDZ5D-7e_s9OMxLJdCovC1MquZEBaUYSkzyWNJtco9zEHZHfA2_2aDhnT9NvULzc3f8Ir2rh1Jf63Dke8xvfN4Grjkc4-34ELTS9BldcrEAu4xsGOT8kpNyM-fJyeGYGsu_ajC4mJL5yeYirL1mwHfaWzL5JxgKK13Zh9QN4fQt2B7HJgNrgwAHrtec3PvstXQqcRr6LQAAAAF4FZRNAA")

SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/neonfedchat")
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/neonfedresmi")

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5045429385").split()))


FAILED = "https://te.legra.ph/file/4c896584b592593c00aa8.jpg"
