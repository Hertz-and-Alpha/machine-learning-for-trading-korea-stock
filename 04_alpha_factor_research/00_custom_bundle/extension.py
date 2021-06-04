import sys
from pathlib import Path
sys.path.append(Path('~', '.zipline').expanduser().as_posix())
from zipline.data.bundles import register
from finance_datareader_kr_stocks import finance_datareader_kr_to_bundle
from datetime import time
from pytz import timezone
import pandas as pd

start_session = pd.Timestamp('2010-1-4', tz='utc')
end_session = pd.Timestamp('2020-12-30', tz='utc')

register('finance_datareader',
         finance_datareader_kr_to_bundle(),
         calendar_name='XKRX',
         start_session=start_session,
         end_session=end_session
         )