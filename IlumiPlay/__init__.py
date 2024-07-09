from IlumiPlayer.core.bot import Anony
from IlumiPlayer.core.dir import dirr
from IlumiPlayer.core.git import git
from IlumiPlayer.core.userbot import Userbot
from IlumiPlayer.misc import dbb, heroku

from .logging import LOGGER

dirr()
git()
dbb()
heroku()

app = Anony()
userbot = Userbot()


from .platforms import *

Apple = AppleAPI()
Carbon = CarbonAPI()
SoundCloud = SoundAPI()
Spotify = SpotifyAPI()
Resso = RessoAPI()
Telegram = TeleAPI()
YouTube = YouTubeAPI()
