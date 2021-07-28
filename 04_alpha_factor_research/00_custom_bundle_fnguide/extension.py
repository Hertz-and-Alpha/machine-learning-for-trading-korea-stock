import sys
from pathlib import Path
sys.path.append(Path('~', '.zipline').expanduser().as_posix())
from zipline.data.bundles import register
from fnguide_kr_stocks import fnguide_kr_to_bundle
from datetime import time
from pytz import timezone
import pandas as pd
from zipline.utils.calendars import get_calendar

start_session = pd.Timestamp('1990-01-03', tz='utc')
end_session = pd.Timestamp('2021-07-26', tz='utc')

register('fnguide',
         fnguide_kr_to_bundle(),
         calendar_name='XKRX',
         start_session=start_session,
         end_session=end_session,
         )