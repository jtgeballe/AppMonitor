from datetime import datetime
from dateutil.relativedelta import relativedelta
from dateutil.relativedelta import TH


def sec_to_next_third_thursday_of_month(current_dt=datetime.now()):
    """Compute the next 3rd Thursday of the current or next month"""
    d = current_dt
    i = relativedelta(day=1, weekday=TH(3))

    while (d + i) < current_dt:
        d = datetime(current_dt.year, current_dt.month + 1, 1)

    next_d = d + i

    return (next_d - current_dt).total_seconds()
