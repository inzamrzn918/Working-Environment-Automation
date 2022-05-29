from datetime import datetime
import pytz
from services import Startup

tz_NY = pytz.timezone("Asia/Calcutta")
st = Startup()
st.start()

# while True:
#     datetime_NY = datetime.now(tz_NY)
#     s = str(datetime_NY.strftime("%H:%M:%S"))
#     if s=='14:13:40':
#         st.start()