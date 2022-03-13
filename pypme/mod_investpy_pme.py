"""
Types can be any of stock, etf, fund, crypto.
"""

from typing import List, Tuple
from datetime import date
import pandas as pd
import investpy
from .pme import verbose_xpme

# FIXME Also add a version based on SearchObj?

# FIXME Take care of rate limiting issues on investing.

# FIXME Add a version that also takes a ticker for the asset and looks up its prices?

# FIXME Add documentation (here and in README)


def get_historical_data(ticker: str, type: str, **kwargs) -> pd.DataFrame:
    """Small wrapper to make the investpy interface accessible in a more unified fashion.
    """
    kwargs[type] = ticker
    if type == "crypto" and "country" in kwargs:
        del kwargs["country"]
    return getattr(investpy, "get_" + type + "_historical_data")(**kwargs)


def investpy_verbose_pme(
    dates: List[date],
    cashflows: List[float],
    prices: List[float],
    pme_ticker: str,
    pme_type: str = "stock",
    pme_country: str = "united states",
) -> Tuple[float, float, pd.DataFrame]:
    """Calculate PME for unevenly spaced / scheduled cashflows and return vebose information. FIXME
    """
    dates_as_str = [x.strftime("%d/%m/%Y") for x in sorted(dates)]
    pmedf = get_historical_data(
        pme_ticker,
        pme_type,
        country=pme_country,
        from_date=dates_as_str[0],
        to_date=dates_as_str[-1],
    )
    # Pick the nearest price if there is no price for an exact date:
    pme_prices = [
        pmedf.iloc[pmedf.index.get_indexer([x], method="nearest")[0]]["Close"]
        for x in dates_as_str
    ]
    return verbose_xpme(dates, cashflows, prices, pme_prices)


def investpy_pme(
    dates: List[date],
    cashflows: List[float],
    prices: List[float],
    pme_ticker: str,
    pme_type: str = "stock",
    pme_country: str = "united states",
) -> Tuple[float, float, pd.DataFrame]:
    """Calculate PME for unevenly spaced / scheduled cashflows and return the PME IRR only. FIXME
    """
    return investpy_verbose_pme(
        dates, cashflows, prices, pme_ticker, pme_type, pme_country
    )[0]
