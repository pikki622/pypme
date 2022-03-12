"""
Types can be any of stock, etf, fund, crypto.
"""

from typing import List, Tuple
from datetime import date
import pandas as pd
import investpy

# FIXME What about crypto etc?

# FIXME What about currencies? (They are in the dataframe, should I check for them?
# Against what?)

# FIXME Also add a version based on SearchObj?


# Do the lookup:
def retrieve_from_investpy(
    ticker: str, type: str, country: str, from_date: date, to_date: date
) -> pd.DataFrame:

    return getattr(investpy, "get_" + type + "_historical_data")(
        **{
            type: ticker,
            "country": country,
            "from_date": from_date,
            "to_date": to_date,
        }
    )


def investpy_verbose_pme(
    dates: List[date],
    cashflows: List[float],
    prices: List[float],
    pme_ticker: str,
    pme_type: str = "stocks",
    pme_country: str = "united states",
) -> Tuple[float, float, pd.DataFrame]:
    """Calculate PME for unevenly spaced / scheduled cashflows and return vebose
    information.

    Requires the points in time as `dates` as an input parameter in addition to the ones
    required by `pme()`.
    """


def investpy_pme():
    pass
