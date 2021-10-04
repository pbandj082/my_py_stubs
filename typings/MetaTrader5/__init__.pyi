import datetime as dt
from typing import Optional, Tuple, NamedTuple, Union
import numpy as np

__version__: str
__author__: str

# timeframes
TIMEFRAME_M1: int
TIMEFRAME_M2: int
TIMEFRAME_M3: int
TIMEFRAME_M4: int
TIMEFRAME_M5: int
TIMEFRAME_M6: int
TIMEFRAME_M10: int
TIMEFRAME_M12: int
TIMEFRAME_M15: int
TIMEFRAME_M20: int
TIMEFRAME_M30: int
TIMEFRAME_H1: int
TIMEFRAME_H2: int
TIMEFRAME_H4: int
TIMEFRAME_H3: int
TIMEFRAME_H6: int
TIMEFRAME_H8: int
TIMEFRAME_H12: int
TIMEFRAME_D1: int
TIMEFRAME_W1: int
TIMEFRAME_MN1: int
# tick copy flags
COPY_TICKS_ALL: int
COPY_TICKS_INFO: int
COPY_TICKS_TRADE: int
# tick flags						  
TICK_FLAG_BID: int
TICK_FLAG_ASK: int
TICK_FLAG_LAST: int
TICK_FLAG_VOLUME: int
TICK_FLAG_BUY: int
TICK_FLAG_SELL: int
# position type, ENUM_POSITION_TYPE
POSITION_TYPE_BUY: int  # Buy
POSITION_TYPE_SELL: int  # Sell
# position reason, ENUM_POSITION_REASON
# The position was opened as a result of activation of an order placed from a desktop terminal
POSITION_REASON_CLIENT: int
# The position was opened as a result of activation of an order placed from a mobile application
POSITION_REASON_MOBILE: int
# The position was opened as a result of activation of an order placed from the web platform
POSITION_REASON_WEB: int
# The position was opened as a result of activation of an order placed from an MQL5 program, i.e. an Expert Advisor or a script
POSITION_REASON_EXPERT: int
# order types, ENUM_ORDER_TYPE
ORDER_TYPE_BUY: int  # Market Buy order
ORDER_TYPE_SELL: int  # Market Sell order
ORDER_TYPE_BUY_LIMIT: int  # Buy Limit pending order
ORDER_TYPE_SELL_LIMIT: int  # Sell Limit pending order
ORDER_TYPE_BUY_STOP: int  # Buy Stop pending order
ORDER_TYPE_SELL_STOP: int  # Sell Stop pending order
# Upon reaching the order price, a pending Buy Limit order is placed at the StopLimit price
ORDER_TYPE_BUY_STOP_LIMIT: int
# Upon reaching the order price, a pending Sell Limit order is placed at the StopLimit price
ORDER_TYPE_SELL_STOP_LIMIT: int
ORDER_TYPE_CLOSE_BY: int  # Order to close a position by an opposite one
# order state, ENUM_ORDER_STATE
ORDER_STATE_STARTED: int  # Order checked, but not yet accepted by broker
ORDER_STATE_PLACED: int  # Order accepted
ORDER_STATE_CANCELED: int  # Order canceled by client
ORDER_STATE_PARTIAL: int  # Order partially executed
ORDER_STATE_FILLED: int  # Order fully executed
ORDER_STATE_REJECTED: int  # Order rejected
ORDER_STATE_EXPIRED: int  # Order expired
# Order is being registered (placing to the trading system)
ORDER_STATE_REQUEST_ADD: int
# Order is being modified (changing its parameters)
ORDER_STATE_REQUEST_MODIFY: int
# Order is being deleted (deleting from the trading system)
ORDER_STATE_REQUEST_CANCEL: int
# ENUM_ORDER_TYPE_FILLING
ORDER_FILLING_FOK: int
ORDER_FILLING_IOC: int
ORDER_FILLING_RETURN: int
# ENUM_ORDER_TYPE_TIME
ORDER_TIME_GTC: int  # Good till cancel order
ORDER_TIME_DAY: int  # Good till current trade day order
ORDER_TIME_SPECIFIED: int      # Good till expired order
# The order will be effective till 23:59:59 of the specified day. If this time is outside a trading session, the order expires in the nearest trading time.
ORDER_TIME_SPECIFIED_DAY: int
# ENUM_ORDER_REASON
ORDER_REASON_CLIENT: int  # The order was placed from a desktop terminal
ORDER_REASON_MOBILE: int  # The order was placed from a mobile application
ORDER_REASON_WEB: int  # The order was placed from a web platform
# The order was placed from an MQL5-program, i.e. by an Expert Advisor or a script
ORDER_REASON_EXPERT: int
ORDER_REASON_SL: int  # The order was placed as a result of Stop Loss activation
ORDER_REASON_TP: int  # The order was placed as a result of Take Profit activation
ORDER_REASON_SO: int  # The order was placed as a result of the Stop Out event
# deal types, ENUM_DEAL_TYPE
DEAL_TYPE_BUY: int  # Buy
DEAL_TYPE_SELL: int  # Sell
DEAL_TYPE_BALANCE: int  # Balance
DEAL_TYPE_CREDIT: int  # Credit
DEAL_TYPE_CHARGE: int  # Additional charge
DEAL_TYPE_CORRECTION: int  # Correction
DEAL_TYPE_BONUS: int  # Bonus
DEAL_TYPE_COMMISSION: int  # Additional commission
DEAL_TYPE_COMMISSION_DAILY: int  # Daily commission
DEAL_TYPE_COMMISSION_MONTHLY: int  # Monthly commission
DEAL_TYPE_COMMISSION_AGENT_DAILY: int  # Daily agent commission
DEAL_TYPE_COMMISSION_AGENT_MONTHLY: int  # Monthly agent commission
DEAL_TYPE_INTEREST: int  # Interest rate
DEAL_TYPE_BUY_CANCELED: int  # Canceled buy deal.
DEAL_TYPE_SELL_CANCELED: int  # Canceled sell deal.
DEAL_DIVIDEND: int  # Dividend operations
DEAL_DIVIDEND_FRANKED: int  # Franked (non-taxable) dividend operations
DEAL_TAX: int  # Tax charges
# ENUM_DEAL_ENTRY
DEAL_ENTRY_IN: int  # Entry in
DEAL_ENTRY_OUT: int  # Entry out
DEAL_ENTRY_INOUT: int  # Reverse
DEAL_ENTRY_OUT_BY: int  # Close a position by an opposite one
# ENUM_DEAL_REASON
# The deal was executed as a result of activation of an order placed from a desktop terminal
DEAL_REASON_CLIENT: int
# The deal was executed as a result of activation of an order placed from a mobile application
DEAL_REASON_MOBILE: int
# The deal was executed as a result of activation of an order placed from the web platform
DEAL_REASON_WEB: int
# The deal was executed as a result of activation of an order placed from an MQL5 program, i.e. an Expert Advisor or a script
DEAL_REASON_EXPERT: int
DEAL_REASON_SL: int  # The deal was executed as a result of Stop Loss activation
DEAL_REASON_TP: int  # The deal was executed as a result of Take Profit activation
DEAL_REASON_SO: int  # The deal was executed as a result of the Stop Out event
DEAL_REASON_ROLLOVER: int  # The deal was executed due to a rollover
# The deal was executed after charging the variation margin
DEAL_REASON_VMARGIN: int
# The deal was executed after the split (price reduction) of an instrument, which had an open position during split announcement
DEAL_REASON_SPLIT: int
# ENUM_TRADE_REQUEST_ACTIONS, Trade Operation Types
# Place a trade order for an immediate execution with the specified parameters (market order)
TRADE_ACTION_DEAL: int
# Place a trade order for the execution under specified conditions (pending order)
TRADE_ACTION_PENDING: int
# Modify Stop Loss and Take Profit values of an opened position
TRADE_ACTION_SLTP: int
TRADE_ACTION_MODIFY: int  # Modify the parameters of the order placed previously
TRADE_ACTION_REMOVE: int  # Delete the pending order placed previously
TRADE_ACTION_CLOSE_BY: int  # Close a position by an opposite one
# ENUM_SYMBOL_CHART_MODE
SYMBOL_CHART_MODE_BID: int
SYMBOL_CHART_MODE_LAST: int
# ENUM_SYMBOL_CALC_MODE
SYMBOL_CALC_MODE_FOREX: int
SYMBOL_CALC_MODE_FUTURES: int
SYMBOL_CALC_MODE_CFD: int
SYMBOL_CALC_MODE_CFDINDEX: int
SYMBOL_CALC_MODE_CFDLEVERAGE: int
SYMBOL_CALC_MODE_FOREX_NO_LEVERAGE: int
SYMBOL_CALC_MODE_EXCH_STOCKS: int
SYMBOL_CALC_MODE_EXCH_FUTURES: int
SYMBOL_CALC_MODE_EXCH_OPTIONS: int
SYMBOL_CALC_MODE_EXCH_OPTIONS_MARGIN: int
SYMBOL_CALC_MODE_EXCH_BONDS: int
SYMBOL_CALC_MODE_EXCH_STOCKS_MOEX: int
SYMBOL_CALC_MODE_EXCH_BONDS_MOEX: int
SYMBOL_CALC_MODE_SERV_COLLATERAL: int
# ENUM_SYMBOL_TRADE_MODE
SYMBOL_TRADE_MODE_DISABLED: int
SYMBOL_TRADE_MODE_LONGONLY: int
SYMBOL_TRADE_MODE_SHORTONLY: int
SYMBOL_TRADE_MODE_CLOSEONLY: int
SYMBOL_TRADE_MODE_FULL: int
# ENUM_SYMBOL_TRADE_EXECUTION
SYMBOL_TRADE_EXECUTION_REQUEST: int
SYMBOL_TRADE_EXECUTION_INSTANT: int
SYMBOL_TRADE_EXECUTION_MARKET: int
SYMBOL_TRADE_EXECUTION_EXCHANGE: int
# ENUM_SYMBOL_SWAP_MODE
SYMBOL_SWAP_MODE_DISABLED: int
SYMBOL_SWAP_MODE_POINTS: int
SYMBOL_SWAP_MODE_CURRENCY_SYMBOL: int
SYMBOL_SWAP_MODE_CURRENCY_MARGIN: int
SYMBOL_SWAP_MODE_CURRENCY_DEPOSIT: int
SYMBOL_SWAP_MODE_INTEREST_CURRENT: int
SYMBOL_SWAP_MODE_INTEREST_OPEN: int
SYMBOL_SWAP_MODE_REOPEN_CURRENT: int
SYMBOL_SWAP_MODE_REOPEN_BID: int
# ENUM_DAY_OF_WEEK
DAY_OF_WEEK_SUNDAY: int
DAY_OF_WEEK_MONDAY: int
DAY_OF_WEEK_TUESDAY: int
DAY_OF_WEEK_WEDNESDAY: int
DAY_OF_WEEK_THURSDAY: int
DAY_OF_WEEK_FRIDAY: int
DAY_OF_WEEK_SATURDAY: int
# ENUM_SYMBOL_ORDER_GTC_MODE
SYMBOL_ORDERS_GTC: int
SYMBOL_ORDERS_DAILY: int
SYMBOL_ORDERS_DAILY_NO_STOPS: int
# ENUM_SYMBOL_OPTION_RIGHT
SYMBOL_OPTION_RIGHT_CALL: int
SYMBOL_OPTION_RIGHT_PUT: int
# ENUM_SYMBOL_OPTION_MODE
SYMBOL_OPTION_MODE_EUROPEAN: int
SYMBOL_OPTION_MODE_AMERICAN: int
# ENUM_ACCOUNT_TRADE_MODE
ACCOUNT_TRADE_MODE_DEMO: int
ACCOUNT_TRADE_MODE_CONTEST: int
ACCOUNT_TRADE_MODE_REAL: int
# ENUM_ACCOUNT_STOPOUT_MODE
ACCOUNT_STOPOUT_MODE_PERCENT: int
ACCOUNT_STOPOUT_MODE_MONEY: int
# ENUM_ACCOUNT_MARGIN_MODE
ACCOUNT_MARGIN_MODE_RETAIL_NETTING: int
ACCOUNT_MARGIN_MODE_EXCHANGE: int
ACCOUNT_MARGIN_MODE_RETAIL_HEDGING: int
# ENUM_BOOK_TYPE
BOOK_TYPE_SELL: int
BOOK_TYPE_BUY: int
BOOK_TYPE_SELL_MARKET: int
BOOK_TYPE_BUY_MARKET: int
# order send/check return codes
TRADE_RETCODE_REQUOTE: int
TRADE_RETCODE_REJECT: int
TRADE_RETCODE_CANCEL: int
TRADE_RETCODE_PLACED: int
TRADE_RETCODE_DONE: int
TRADE_RETCODE_DONE_PARTIAL: int
TRADE_RETCODE_ERROR: int
TRADE_RETCODE_TIMEOUT: int
TRADE_RETCODE_INVALID: int
TRADE_RETCODE_INVALID_VOLUME: int
TRADE_RETCODE_INVALID_PRICE: int
TRADE_RETCODE_INVALID_STOPS: int
TRADE_RETCODE_TRADE_DISABLED: int
TRADE_RETCODE_MARKET_CLOSED: int
TRADE_RETCODE_NO_MONEY: int
TRADE_RETCODE_PRICE_CHANGED: int
TRADE_RETCODE_PRICE_OFF: int
TRADE_RETCODE_INVALID_EXPIRATION: int
TRADE_RETCODE_ORDER_CHANGED: int
TRADE_RETCODE_TOO_MANY_REQUESTS: int
TRADE_RETCODE_NO_CHANGES: int
TRADE_RETCODE_SERVER_DISABLES_AT: int
TRADE_RETCODE_CLIENT_DISABLES_AT: int
TRADE_RETCODE_LOCKED: int
TRADE_RETCODE_FROZEN: int
TRADE_RETCODE_INVALID_FILL: int
TRADE_RETCODE_CONNECTION: int
TRADE_RETCODE_ONLY_REAL: int
TRADE_RETCODE_LIMIT_ORDERS: int
TRADE_RETCODE_LIMIT_VOLUME: int
TRADE_RETCODE_INVALID_ORDER: int
TRADE_RETCODE_POSITION_CLOSED: int
TRADE_RETCODE_INVALID_CLOSE_VOLUME: int
TRADE_RETCODE_CLOSE_ORDER_EXIST: int
TRADE_RETCODE_LIMIT_POSITIONS: int
TRADE_RETCODE_REJECT_CANCEL: int
TRADE_RETCODE_LONG_ONLY: int
TRADE_RETCODE_SHORT_ONLY: int
TRADE_RETCODE_CLOSE_ONLY: int
TRADE_RETCODE_FIFO_CLOSE: int
# function error codes, last_error()
RES_S_OK: int  # generic success
RES_E_FAIL: int  # generic fail
RES_E_INVALID_PARAMS: int  # invalid arguments/parameters
RES_E_NO_MEMORY: int  # no memory condition
RES_E_NOT_FOUND: int  # no history
RES_E_INVALID_VERSION: int  # invalid version
RES_E_AUTH_FAILED: int  # authorization failed
RES_E_UNSUPPORTED: int  # unsupported method
RES_E_AUTO_TRADING_DISABLED: int  # auto-trading disabled
RES_E_INTERNAL_FAIL: int  # internal IPC general error
RES_E_INTERNAL_FAIL_SEND: int  # internal IPC send failed
RES_E_INTERNAL_FAIL_RECEIVE: int  # internal IPC recv failed
RES_E_INTERNAL_FAIL_INIT: int  # internal IPC initialization fail
RES_E_INTERNAL_FAIL_CONNECT: int  # internal IPC no ipc
RES_E_INTERNAL_FAIL_TIMEOUT: int  # internal timeout


def initialize(
    path: Optional[int] = None,
    /,
    login: Optional[str] = None,
    password: Optional[str] = None,
    server: Optional[str] = None,
    timeout: int = 60_000,
    portable: bool = False,
) -> bool:
    """ Establish a connection with the MetaTrader 5 terminal.

    If required, the MetaTrader 5 terminal is launched to establish connection when executing the initialize() call.

    Args:
        path: Path to the metatrader.exe or metatrader64.exe file.
            Optional unnamed parameter. It is indicated first without a parameter name.
            If the path is not specified, the module attempts to find the executable file on its own.
        login: Trading account number. Optional named parameter.
            If not specified, the last trading account is used.
        password: Trading account password. Optional named parameter.
            If the password is not set, the password for a specified trading account saved in the terminal database is applied automatically.
        server: Trade server name. Optional named parameter.
            If the server is not set, the server for a specified trading account saved in the terminal database is applied automatically.
        timeout: Connection timeout in milliseconds. Optional named parameter. If not specified, the value of 60 000 (60 seconds) is applied.
        portable: Flag of the terminal launch in portable mode. Optional named parameter. If not specified, the value of False is used.
    
    Returns:
        Returns True in case of successful connection to the MetaTrader 5 terminal, otherwise - False

    Examples:
        import MetaTrader5 as mt5
        # display data on the MetaTrader 5 package
        print("MetaTrader5 package author: ",mt5.__author__)
        print("MetaTrader5 package version: ",mt5.__version__)
        
        # establish MetaTrader 5 connection to a specified trading account
        if not mt5.initialize(login=25115284, server="MetaQuotes-Demo",password="4zatlbqx"):
            print("initialize() failed, error code =",mt5.last_error())
            quit()
        
        # display data on connection status, server name and trading account
        print(mt5.terminal_info())
        # display data on MetaTrader 5 version
        print(mt5.version())
        
        # shut down connection to the MetaTrader 5 terminal
        mt5.shutdown()
    """


def login(
    login: Optional[int],
    /,
    password: Optional[str] = None,
    server: Optional[str] = None,
    timeout: int = 60_000,
) -> bool:
    """Connect to a trading account using specified parameters.

    Args:
        login: Trading account number. Required unnamed parameter.
        password: Trading account password. Optional named parameter.
            If the password is not set, the password saved in the terminal database is applied automatically.
        server: Trade server name. Optional named parameter.
            If no server is set, the last used server is applied automatically.
        timeout: Connection timeout in milliseconds. Optional named parameter.
            If not specified, the value of 60 000 (60 seconds) is applied.
            If the connection is not established within the specified time,
            the call is forcibly terminated and the exception is generated.

    Returns:
        True in case of a successful connection to the trade account, otherwise – False.

    Example:
        import MetaTrader5 as mt5
        # display data on the MetaTrader 5 package
        print("MetaTrader5 package author: ",mt5.__author__)
        print("MetaTrader5 package version: ",mt5.__version__)
        
        # establish connection to the MetaTrader 5 terminal
        if not mt5.initialize():
            print("initialize() failed, error code =",mt5.last_error())
            quit()
        
        # display data on MetaTrader 5 version
        print(mt5.version())
        # connect to the trade account without specifying a password and a server
        account=17221085
        authorized=mt5.login(account)  # the terminal database password is applied if connection data is set to be remembered
        if authorized:
            print("connected to account #{}".format(account))
        else:
            print("failed to connect at account #{}, error code: {}".format(account, mt5.last_error()))
        
        # now connect to another trading account specifying the password
        account=25115284
        authorized=mt5.login(account, password="gqrtz0lbdm")
        if authorized:
            # display trading account data 'as is'
            print(mt5.account_info())
            # display trading account data in the form of a list
            print("Show account_info()._asdict():")
            account_info_dict = mt5.account_info()._asdict()
            for prop in account_info_dict:
                print("  {}={}".format(prop, account_info_dict[prop]))
        else:
            print("failed to connect at account #{}, error code: {}".format(account, mt5.last_error()))
        
        # shut down connection to the MetaTrader 5 terminal
        mt5.shutdown()
    """


def shutdown() -> None:
    """Close the previously established connection to the MetaTrader 5 terminal.

    Example:
        import MetaTrader5 as mt5
        # display data on the MetaTrader 5 package
        print("MetaTrader5 package author: ",mt5.__author__)
        print("MetaTrader5 package version: ",mt5.__version__)
        
        # establish connection to the MetaTrader 5 terminal
        if not mt5.initialize():
            print("initialize() failed")
            quit()
        
        # display data on connection status, server name and trading account
        print(mt5.terminal_info())
        # display data on MetaTrader 5 version
        print(mt5.version())
        
        # shut down connection to the MetaTrader 5 terminal
        mt5.shutdown()
    """


def version() -> Optional[Tuple[int, int, str]]:
    """Return the MetaTrader 5 terminal version.

    The version() function returns the terminal version, build and release date as a tuple of three values:
    |Type|Description                  |Sample Value |
    |:---|:---                         |:---         |
    |int |MetaTrader 5 terminal version|500          |
    |int |Build                        |2007         |
    |str |Build release date           |'25 Feb 2019'|

    Returns:
        Return the MetaTrader 5 terminal version, build and release date. Return None in case of an error. The info on the error can be obtained using last_error().
    
    Example:
        import MetaTrader5 as mt5
        import pandas as pd
        # display data on the MetaTrader 5 package
        print("MetaTrader5 package author: ",mt5.__author__)
        print("MetaTrader5 package version: ",mt5.__version__)
        
        # establish connection to the MetaTrader 5 terminal
        if not mt5.initialize():
            print("initialize() failed, error code =",mt5.last_error())
            quit()
        
        # display data on MetaTrader 5 version
        print(mt5.version())
        
        # display data on connection status, server name and trading account 'as is'
        print(mt5.terminal_info())
        print()
        
        # get properties in the form of a dictionary
        terminal_info_dict=mt5.terminal_info()._asdict()
        # convert the dictionary into DataFrame and print
        df=pd.DataFrame(list(terminal_info_dict.items()),columns=['property','value'])
        print("terminal_info() as dataframe:")
        print(df[:-1])
        
        # shut down connection to the MetaTrader 5 terminal
        mt5.shutdown()
        
        """


def last_error() -> Tuple[int, str]:
    """Return data on the last error.

    last_error() allows obtaining an error code in case of a failed execution of a MetaTrader 5 library function.
    It is similar to GetLastError(). However, it applies its own error codes.
    |Constant                   |Value |Description                     |
    |:--------------------------|:-------------------------------|
    |RES_S_OK                   |1     |generic success                 |
    |RES_E_FAIL                 |-1    |generic fail                    |
    |RES_E_INVALID_PARAMS       |-2    |invalid arguments/parameters    |
    |RES_E_NO_MEMORY            |-3    |no memory condition             |
    |RES_E_NOT_FOUND            |-4    |no history                      |
    |RES_E_INVALID_VERSION      |-5    |invalid version                 |
    |RES_E_AUTH_FAILED          |-6    |authorization failed            |
    |RES_E_UNSUPPORTED          |-7    |unsupported method              |
    |RES_E_AUTO_TRADING_DISABLED|-8    |auto-trading disabled           |
    |RES_E_INTERNAL_FAIL        |-10000|internal IPC general error      |
    |RES_E_INTERNAL_FAIL_SEND   |-10001|internal IPC send failed        |
    |RES_E_INTERNAL_FAIL_RECEIVE|-10002|internal IPC recv failed        |
    |RES_E_INTERNAL_FAIL_INIT   |-10003|internal IPC initialization fail|
    |RES_E_INTERNAL_FAIL_CONNECT|-10004|internal IPC no ipc             |
    |RES_E_INTERNAL_FAIL_TIMEOUT|-10005|internal timeout                |
  
    Returns:
        Return the last error code and description as a tuple.
    
    Example:
        import MetaTrader5 as mt5
        # display data on the MetaTrader 5 package
        print("MetaTrader5 package author: ",mt5.__author__)
        print("MetaTrader5 package version: ",mt5.__version__)
        
        # establish connection to the MetaTrader 5 terminal
        if not mt5.initialize():
            print("initialize() failed, error code =",mt5.last_error())
            quit()
        
        # shut down connection to the MetaTrader 5 terminal
        mt5.shutdown()
    """


class AccountInfo(NamedTuple):
    login: int
    trade_mode: int
    leverage: int
    limit_orders: int
    margin_so_mode: int
    trade_allowed: bool
    trade_expert: bool
    margin_mode: int
    currency_digits: int
    fifo_close: bool
    balance: float
    credit: float
    profit: float
    equity: float
    margin: float
    margin_free: float
    margin_level: float
    margin_so_call: float
    margin_so_so: float
    margin_initial: float
    margin_maintenance: float
    assets: float
    liabilities: float
    commission_blocked: float
    name: str
    server: str
    currency: str
    company: str


def account_info() -> Optional[AccountInfo]:
    """Get info on the current trading account.

    The function returns all data that can be obtained using AccountInfoInteger, AccountInfoDouble and AccountInfoString in one call.

    Rertuns:
        Return info in the form of a named tuple structure (namedtuple). Return None in case of an error. The info on the error can be obtained using last_error().
    
    Example:
        import MetaTrader5 as mt5
        import pandas as pd
        # display data on the MetaTrader 5 package
        print("MetaTrader5 package author: ",mt5.__author__)
        print("MetaTrader5 package version: ",mt5.__version__)
        
        # establish connection to the MetaTrader 5 terminal
        if not mt5.initialize():
            print("initialize() failed, error code =",mt5.last_error())
            quit()
        
        # connect to the trade account specifying a password and a server
        authorized=mt5.login(25115284, password="gqz0343lbdm")
        if authorized:
            account_info=mt5.account_info()
            if account_info!=None:
                # display trading account data 'as is'
                print(account_info)
                # display trading account data in the form of a dictionary
                print("Show account_info()._asdict():")
                account_info_dict = mt5.account_info()._asdict()
                for prop in account_info_dict:
                    print("  {}={}".format(prop, account_info_dict[prop]))
                print()
        
                # convert the dictionary into DataFrame and print
                df=pd.DataFrame(list(account_info_dict.items()),columns=['property','value'])
                print("account_info() as dataframe:")
                print(df)
        else:
            print("failed to connect to trade account 25115284 with password=gqz0343lbdm, error code =",mt5.last_error())
        
        # shut down connection to the MetaTrader 5 terminal
        mt5.shutdown()
    """


class TerminalInfo(NamedTuple):
    community_account: bool
    community_connection: bool
    connected: bool
    dlls_allowed: bool
    trade_allowed: bool
    tradeapi_disabled: bool
    email_enabled: bool
    ftp_enabled: bool
    notifications_enabled: bool
    mqid: bool
    build: int
    maxbars: int
    codepage: int
    ping_last: int
    community_balance: float
    retransmission: float
    company: str
    name: str
    language: str
    path: str
    data_path: str
    commondata_path: str


def terminal_info() -> Optional[TerminalInfo]:
    """Get the connected MetaTrader 5 client terminal status and settings.

    Returns:
        Return info in the form of a named tuple structure (namedtuple). Return None in case of an error. The info on the error can be obtained using last_error().
        The function returns all data that can be obtained using TerminalInfoInteger, TerminalInfoDouble and TerminalInfoDouble in one call.

    Examples:
        import MetaTrader5 as mt5
        import pandas as pd
        # display data on the MetaTrader 5 package
        print("MetaTrader5 package author: ",mt5.__author__)
        print("MetaTrader5 package version: ",mt5.__version__)
        # display data on the MetaTrader 5 package
        print("MetaTrader5 package author: ",mt5.__author__)
        print("MetaTrader5 package version: ",mt5.__version__)
        
        # establish connection to the MetaTrader 5 terminal
        if not mt5.initialize():
            print("initialize() failed, error code =",mt5.last_error())
            quit()
        
        # display data on MetaTrader 5 version
        print(mt5.version())
        # display info on the terminal settings and status
        terminal_info=mt5.terminal_info()
        if terminal_info!=None:
            # display the terminal data 'as is'
            print(terminal_info)
            # display data in the form of a list
            print("Show terminal_info()._asdict():")
            terminal_info_dict = mt5.terminal_info()._asdict()
            for prop in terminal_info_dict:
                print("  {}={}".format(prop, terminal_info_dict[prop]))
            print()
        # convert the dictionary into DataFrame and print
            df=pd.DataFrame(list(terminal_info_dict.items()),columns=['property','value'])
            print("terminal_info() as dataframe:")
            print(df)
        
        # shut down connection to the MetaTrader 5 terminal
        mt5.shutdown()
    """


def symbols_total() -> int:
    """Get the number of all financial instruments in the MetaTrader 5 terminal.

    Returns:
        Integer value.
        The function is similar to SymbolsTotal().
        However, it returns the number of all symbols including custom ones and the ones disabled in MarketWatch.
    
    Examples:
        import MetaTrader5 as mt5
        # display data on the MetaTrader 5 package
        print("MetaTrader5 package author: ",mt5.__author__)
        print("MetaTrader5 package version: ",mt5.__version__)
        
        # establish connection to the MetaTrader 5 terminal
        if not mt5.initialize():
            print("initialize() failed, error code =",mt5.last_error())
            quit()
        
        # get the number of financial instruments
        symbols=mt5.symbols_total()
        if symbols>0:
            print("Total symbols =",symbols)
        else:
            print("symbols not found")
        
        # shut down connection to the MetaTrader 5 terminal
        mt5.shutdown()
    """


class SymbolInfo(NamedTuple):
    custom: bool
    chart_mode: int
    select: bool
    visible: bool
    session_deals: int
    session_buy_orders: int
    session_sell_orders: int
    volume: int
    volumehigh: int
    volumelow: int
    time: int
    digits: int
    spread: int
    spread_float: bool
    ticks_bookdepth: int
    trade_calc_mode: int
    trade_mode: int
    start_time: int
    expiration_time: int
    trade_stops_level: int
    trade_freeze_level: int
    trade_exemode: int
    swap_mode: int
    swap_rollover3days: int
    margin_hedged_use_leg: bool
    expiration_mode: int
    filling_mode: int
    order_mode: int
    order_gtc_mode: int
    option_mode: int
    option_right: int
    bid: float
    bidhigh: float
    bidlow: float
    ask: float
    askhigh: float
    asklow: float
    last: float
    lasthigh: float
    lastlow: float
    volume_real: float
    volumehigh_real: float
    volumelow_real: float
    option_strike: float
    point: float
    trade_tick_value: float
    trade_tick_value_profit: float
    trade_tick_value_loss: float
    trade_tick_size: float
    trade_contract_size: float
    trade_accrued_interest: float
    trade_face_value: float
    trade_liquidity_rate: float
    volume_min: float
    volume_max: float
    volume_step: float
    volume_limit: float
    swap_long: float
    swap_short: float
    margin_initial: float
    margin_maintenance: float
    session_volume: float
    session_turnover: float
    session_interest: float
    session_buy_orders_volume: float
    session_sell_orders_volume: float
    session_open: float
    session_close: float
    session_aw: float
    session_price_settlement: float
    session_price_limit_min: float
    session_price_limit_max: float
    margin_hedged: float
    price_change: float
    price_volatility: float
    price_theoretical: float
    price_greeks_delta: float
    price_greeks_theta: float
    price_greeks_gamma: float
    price_greeks_vega: float
    price_greeks_rho: float
    price_greeks_omega: float
    price_sensitivity: float
    basis: str
    category: str
    currency_base: str
    currency_profit: str
    currency_margin: str
    bank: str
    description: str
    exchange: str
    formula: str
    isin: str
    name: str
    page: str
    path: str


def symbols_get(group: Optional[str] = None) -> Optional[Tuple[SymbolInfo, ...]]:
    """Get all financial instruments from the MetaTrader 5 terminal.

    The group parameter allows sorting out symbols by name. '*' can be used at the beginning and the end of a string.
    The group parameter can be used as a named or an unnamed one. Both options work the same way.
    The named option (group="GROUP") makes the code easier to read.
    The group parameter may contain several comma separated conditions. A condition can be set as a mask using '*'.
    The logical negation symbol '!' can be used for an exclusion. All conditions are applied sequentially,
    which means conditions of including to a group should be specified first followed by an exclusion condition. For example, group="*,
    !EUR" means that all symbols should be selected first and the ones containing "EUR" in their names should be excluded afterwards.
    Unlike symbol_info(), the symbols_get() function returns data on all requested symbols within a single call.

    Args:
        group: The filter for arranging a group of necessary symbols.
            Optional parameter. If the group is specified,
            the function returns only symbols meeting a specified criteria.
    
    Returns:
        Return symbols in the form of a tuple. Return None in case of an error. The info on the error can be obtained using last_error().
    
    Example:
        import MetaTrader5 as mt5
        # display data on the MetaTrader 5 package
        print("MetaTrader5 package author: ",mt5.__author__)
        print("MetaTrader5 package version: ",mt5.__version__)
        
        # establish connection to the MetaTrader 5 terminal
        if not mt5.initialize():
            print("initialize() failed, error code =",mt5.last_error())
            quit()
        
        # get all symbols
        symbols=mt5.symbols_get()
        print('Symbols: ', len(symbols))
        count=0
        # display the first five ones
        for s in symbols:
            count+=1
            print("{}. {}".format(count,s.name))
            if count==5: break
        print()
        
        # get symbols containing RU in their names
        ru_symbols=mt5.symbols_get("*RU*")
        print('len(*RU*): ', len(ru_symbols))
        for s in ru_symbols:
            print(s.name)
        print()
        
        # get symbols whose names do not contain USD, EUR, JPY and GBP
        group_symbols=mt5.symbols_get(group="*,!*USD*,!*EUR*,!*JPY*,!*GBP*")
        print('len(*,!*USD*,!*EUR*,!*JPY*,!*GBP*):', len(group_symbols))
        for s in group_symbols:
            print(s.name,":",s)
        
        # shut down connection to the MetaTrader 5 terminal
        mt5.shutdown()
    """


def symbol_info(symbol: str, /) -> Optional[SymbolInfo]:
    """Get data on the specified financial instrument.

    The function returns all data that can be obtained using SymbolInfoInteger,
    SymbolInfoDouble and SymbolInfoString in one call

    Args:
        symbol: Financial instrument name. Required unnamed parameter.

    Returns:
        Return info in the form of a named tuple structure (namedtuple).
        Return None in case of an error. The info on the error can be obtained using last_error().
    
    Example:
        import MetaTrader5 as mt5
        # display data on the MetaTrader 5 package
        print("MetaTrader5 package author: ",mt5.__author__)
        print("MetaTrader5 package version: ",mt5.__version__)
        
        # establish connection to the MetaTrader 5 terminal
        if not mt5.initialize():
            print("initialize() failed, error code =",mt5.last_error())
            quit()
        
        # attempt to enable the display of the EURJPY symbol in MarketWatch
        selected=mt5.symbol_select("EURJPY",True)
        if not selected:
            print("Failed to select EURJPY")
            mt5.shutdown()
            quit()
        
        # display EURJPY symbol properties
        symbol_info=mt5.symbol_info("EURJPY")
        if symbol_info!=None:
            # display the terminal data 'as is'    
            print(symbol_info)
            print("EURJPY: spread =",symbol_info.spread,"  digits =",symbol_info.digits)
            # display symbol properties as a list
            print("Show symbol_info(\"EURJPY\")._asdict():")
            symbol_info_dict = mt5.symbol_info("EURJPY")._asdict()
            for prop in symbol_info_dict:
                print("  {}={}".format(prop, symbol_info_dict[prop]))
        
        # shut down connection to the MetaTrader 5 terminal
        mt5.shutdown()
    """


class Tick(NamedTuple):
    time: int
    bid: float
    ask: float
    last: float
    volume: int
    time_msc: int
    flags: int
    volume_real: float


def symbol_info_tick(symbol: str, /) -> Optional[Tick]:
    """Get the last tick for the specified financial instrument.

    The function is similar to SymbolInfoTick.

    Args:
        symbol: Financial instrument name. Required unnamed parameter.
    
    Returns:
        Return info in the form of a tuple. Return None in case of an error.
        The info on the error can be obtained using last_error().

    Example:
        import MetaTrader5 as mt5
        # display data on the MetaTrader 5 package
        print("MetaTrader5 package author: ",mt5.__author__)
        print("MetaTrader5 package version: ",mt5.__version__)
        
        # establish connection to the MetaTrader 5 terminal
        if not mt5.initialize():
            print("initialize() failed, error code =",mt5.last_error())
            quit()
        
        # attempt to enable the display of the GBPUSD in MarketWatch
        selected=mt5.symbol_select("GBPUSD",True)
        if not selected:
            print("Failed to select GBPUSD")
            mt5.shutdown()
            quit()
        
        # display the last GBPUSD tick
        lasttick=mt5.symbol_info_tick("GBPUSD")
        print(lasttick)
        # display tick field values in the form of a list
        print("Show symbol_info_tick(\"GBPUSD\")._asdict():")
        symbol_info_tick_dict = mt5.symbol_info_tick("GBPUSD")._asdict()
        for prop in symbol_info_tick_dict:
            print("  {}={}".format(prop, symbol_info_tick_dict[prop]))
        
        # shut down connection to the MetaTrader 5 terminal
        mt5.shutdown()
    """


def symbol_select(symbol: int, enable: bool = True, /) -> bool:
    """Select a symbol in the MarketWatch window or remove a symbol from the window.

    The function is similar to SymbolSelect.

    Args:
        symbol: Financial instrument name. Required unnamed parameter.
        enable: Switch. Optional unnamed parameter. If 'false', a symbol should be removed from the MarketWatch window.
            Otherwise, it should be selected in the MarketWatch window.
            A symbol cannot be removed if open charts with this symbol are currently present or positions are opened on it

    Returns:
        True if successful, otherwise – False.

    Example:
        import MetaTrader5 as mt5
        import pandas as pd
        # display data on the MetaTrader 5 package
        print("MetaTrader5 package author: ",mt5.__author__)
        print("MetaTrader5 package version: ",mt5.__version__)
        print()
        # establish connection to the MetaTrader 5 terminal
        if not mt5.initialize(login=25115284, server="MetaQuotes-Demo",password="4zatlbqx"):
            print("initialize() failed, error code =",mt5.last_error())
            quit()
        
        # attempt to enable the display of the EURCAD in MarketWatch
        selected=mt5.symbol_select("EURCAD",True)
        if not selected:
            print("Failed to select EURCAD, error code =",mt5.last_error())
        else:
            symbol_info=mt5.symbol_info("EURCAD")
            print(symbol_info)
            print("EURCAD: currency_base =",symbol_info.currency_base,"  currency_profit =",symbol_info.currency_profit,"  currency_margin =",symbol_info.currency_margin)
            print()
        
            # get symbol properties in the form of a dictionary
            print("Show symbol_info()._asdict():")
            symbol_info_dict = symbol_info._asdict()
            for prop in symbol_info_dict:
                print("  {}={}".format(prop, symbol_info_dict[prop]))
            print()
        
            # convert the dictionary into DataFrame and print
            df=pd.DataFrame(list(symbol_info_dict.items()),columns=['property','value'])
            print("symbol_info_dict() as dataframe:")
            print(df)
        
        # shut down connection to the MetaTrader 5 terminal
        mt5.shutdown()
    """


def market_book_add(symbol: str, /) -> bool:
    """Subscribes the MetaTrader 5 terminal to the Market Depth change events for a specified symbol.

    The function is similar to MarketBookAdd.

    Args:
        symbol: Financial instrument name. Required unnamed parameter.

    Returns:
        True if successful, otherwise – False.
    """


class BookInfo(NamedTuple):
    type: int
    price: float
    volume: int
    volume_dbl: float


def market_book_get(symbol: str, /) -> Optional[Tuple[BookInfo, ...]]:
    """Returns a tuple from BookInfo featuring Market Depth entries for the specified symbol.

    The subscription to the Market Depth change events should be preliminarily performed using the market_book_add() function.
    The function is similar to MarketBookGet.

    Args:
        symbol: Financial instrument name. Required unnamed parameter.
    
    Returns:
        Returns the Market Depth content as a tuple from BookInfo entries featuring order type, price and volume in lots.
        BookInfo is similar to the MqlBookInfo structure.
        Return None in case of an error. The info on the error can be obtained using last_error().
    
    Example:
        import MetaTrader5 as mt5
        import time
        # display data on the MetaTrader 5 package
        print("MetaTrader5 package author: ",mt5.__author__)
        print("MetaTrader5 package version: ",mt5.__version__)
        print("")
        
        # establish connection to the MetaTrader 5 terminal
        if not mt5.initialize():
            print("initialize() failed, error code =",mt5.last_error())
        # shut down connection to the MetaTrader 5 terminal
            mt5.shutdown()
            quit()
        
        # subscribe to market depth updates for EURUSD (Depth of Market)
        if mt5.market_book_add('EURUSD'):
        # get the market depth data 10 times in a loop
        for i in range(10):
                # get the market depth content (Depth of Market)
                items = mt5.market_book_get('EURUSD')
                # display the entire market depth 'as is' in a single string
                print(items)
                # now display each order separately for more clarity
                if items:
                    for it in items:
                        # order content
                        print(it._asdict())
                # pause for 5 seconds before the next request of the market depth data
                time.sleep(5)
        # cancel the subscription to the market depth updates (Depth of Market)
        mt5.market_book_release('EURUSD')
        else:
            print("mt5.market_book_add('EURUSD') failed, error code =",mt5.last_error())
        
        # shut down connection to the MetaTrader 5 terminal
        mt5.shutdown()
        """


def market_book_release(symbol: str, /) -> bool:
    """Cancels subscription of the MetaTrader 5 terminal to the Market Depth change events for a specified symbol.

    The function is similar to MarketBookRelease.

    Args:
        symbol: Financial instrument name. Required unnamed parameter.
    
    Returns:
        True if successful, otherwise – False.
    """


def copy_rates_from(
    symbol: str,
    timeframe: int,
    date_from: Union[dt.datetime, int],
    count: int,
    /,
) -> Optional[np.ndarray[np.void]]:
    """Get bars from the MetaTrader 5 terminal starting from the specified date.

    See the CopyRates() function for more information.
    MetaTrader 5 terminal provides bars only within a history available to a user on charts.
    The number of bars available to users is set in the "Max. bars in chart" parameter.
    When creating the 'datetime' object, Python uses the local time zone,
    while MetaTrader 5 stores tick and bar open time in UTC time zone (without the shift).
    Therefore, 'datetime' should be created in UTC time for executing functions that use time.
    Data received from the MetaTrader 5 terminal has UTC time.
    TIMEFRAME is an enumeration with possible chart period values
    |ID           |Description|
    |:------------|:----------|
    |TIMEFRAME_M1 |1 minute   |
    |TIMEFRAME_M2 |2 minutes  |
    |TIMEFRAME_M3 |3 minutes  |
    |TIMEFRAME_M4 |4 minutes  |
    |TIMEFRAME_M5 |5 minutes  |
    |TIMEFRAME_M6 |6 minutes  |
    |TIMEFRAME_M10|10 minutes |
    |TIMEFRAME_M12|12 minutes |
    |TIMEFRAME_M12|15 minutes |
    |TIMEFRAME_M20|20 minutes |
    |TIMEFRAME_M30|30 minutes |
    |TIMEFRAME_H1 |1 hour     |
    |TIMEFRAME_H2 |2 hours    |
    |TIMEFRAME_H3 |3 hours    |
    |TIMEFRAME_H4 |4 hours    |
    |TIMEFRAME_H6 |6 hours    |
    |TIMEFRAME_H8 |8 hours    |
    |TIMEFRAME_H12|12 hours   |
    |TIMEFRAME_D1 |1 day      |
    |TIMEFRAME_W1 |1 week     |
    |TIMEFRAME_MN1|1 month    |

    Args:
        symbol: Financial instrument name, for example, "EURUSD". Required unnamed parameter.
        timeframe: Timeframe the bars are requested for.
            Set by a value from the TIMEFRAME enumeration. Required unnamed parameter.
        date_from: Date of opening of the first bar from the requested sample.
            Set by the 'datetime' object or as a number of seconds elapsed since 1970.01.01.
            Required unnamed parameter.
        count: Number of bars to receive. Required unnamed parameter.
    
    Returns:
        Returns bars as the numpy array with the named time, open, high, low, close, tick_volume,
        spread and real_volume columns. Return None in case of an error.
        The info on the error can be obtained using last_error().

    Example:
        from datetime import datetime
        import MetaTrader5 as mt5
        # display data on the MetaTrader 5 package
        print("MetaTrader5 package author: ",mt5.__author__)
        print("MetaTrader5 package version: ",mt5.__version__)
        
        # import the 'pandas' module for displaying data obtained in the tabular form
        import pandas as pd
        pd.set_option('display.max_columns', 500) # number of columns to be displayed
        pd.set_option('display.width', 1500)      # max table width to display
        # import pytz module for working with time zone
        import pytz
        
        # establish connection to MetaTrader 5 terminal
        if not mt5.initialize():
            print("initialize() failed, error code =",mt5.last_error())
            quit()
        
        # set time zone to UTC
        timezone = pytz.timezone("Etc/UTC")
        # create 'datetime' object in UTC time zone to avoid the implementation of a local time zone offset
        utc_from = datetime(2020, 1, 10, tzinfo=timezone)
        # get 10 EURUSD H4 bars starting from 01.10.2020 in UTC time zone
        rates = mt5.copy_rates_from("EURUSD", mt5.TIMEFRAME_H4, utc_from, 10)
        
        # shut down connection to the MetaTrader 5 terminal
        mt5.shutdown()
        # display each element of obtained data in a new line
        print("Display obtained data 'as is'")
        for rate in rates:
            print(rate)
        
        # create DataFrame out of the obtained data
        rates_frame = pd.DataFrame(rates)
        # convert time in seconds into the datetime format
        rates_frame['time']=pd.to_datetime(rates_frame['time'], unit='s')
                                
        # display data
        print("\nDisplay dataframe with data")
        print(rates_frame)  
    """


def copy_rates_from_pos(
    symbol: str,
    timeframe: int,
    start_pos: int,
    count: int,
    /,
) -> Optional[np.ndarray[np.void]]:
    """Get bars from the MetaTrader 5 terminal starting from the specified index.

    See the CopyRates() function for more information.
    MetaTrader 5 terminal provides bars only within a history available to a user on charts. The number of bars available to users is set in the "Max. bars in chart" parameter.

    Args:
        symbol: Financial instrument name, for example, "EURUSD". Required unnamed parameter.
        timeframe: Timeframe the bars are requested for. Set by a value from the TIMEFRAME enumeration. Required unnamed parameter.
        start_pos: Initial index of the bar the data are requested from. The numbering of bars goes from present to past. Thus, the zero bar means the current one. Required unnamed parameter.
        count: Number of bars to receive. Required unnamed parameter.

    Example:
        from datetime import datetime
        import MetaTrader5 as mt5
        # display data on the MetaTrader 5 package
        print("MetaTrader5 package author: ",mt5.__author__)
        print("MetaTrader5 package version: ",mt5.__version__)
        
        # import the 'pandas' module for displaying data obtained in the tabular form
        import pandas as pd
        pd.set_option('display.max_columns', 500) # number of columns to be displayed
        pd.set_option('display.width', 1500)      # max table width to display
        
        # establish connection to MetaTrader 5 terminal
        if not mt5.initialize():
            print("initialize() failed, error code =",mt5.last_error())
            quit()
        
        # get 10 GBPUSD D1 bars from the current day
        rates = mt5.copy_rates_from_pos("GBPUSD", mt5.TIMEFRAME_D1, 0, 10)
        
        # shut down connection to the MetaTrader 5 terminal
        mt5.shutdown()
        # display each element of obtained data in a new line
        print("Display obtained data 'as is'")
        for rate in rates:
            print(rate)
        
        # create DataFrame out of the obtained data
        rates_frame = pd.DataFrame(rates)
        # convert time in seconds into the datetime format
        rates_frame['time']=pd.to_datetime(rates_frame['time'], unit='s')
        
        # display data
        print("\nDisplay dataframe with data")
        print(rates_frame) 
    """


def copy_rates_range(
    symbol: str,
    timeframe: int,
    date_from: Union[dt.datetime, int],
    date_to: Union[dt.datetime, int],
    /,
) -> Optional[np.ndarray[np.void]]:
    """Get bars in the specified date range from the MetaTrader 5 terminal.

    See the CopyRates() function for more information.
    MetaTrader 5 terminal provides bars only within a history available to a user on charts.
    The number of bars available to users is set in the "Max. bars in chart" parameter.
    When creating the 'datetime' object, Python uses the local time zone,
    while MetaTrader 5 stores tick and bar open time in UTC time zone (without the shift).
    Therefore, 'datetime' should be created in UTC time for executing functions that use time.
    Data received from the MetaTrader 5 terminal has UTC time.

    Args:
        symbol: Financial instrument name, for example, "EURUSD". Required unnamed parameter.
        timeframe: Timeframe the bars are requested for. Set by a value from the TIMEFRAME enumeration. Required unnamed parameter.
        date_from: Date the bars are requested from. Set by the 'datetime' object or as a number of seconds elapsed since 1970.01.01.
            Bars with the open time >= date_from are returned. Required unnamed parameter.
        date_to: Date, up to which the bars are requested. Set by the 'datetime' object or as a number of seconds elapsed since 1970.01.01.
            Bars with the open time <= date_to are returned. Required unnamed parameter.
    
    Returns:
        Returns bars as the numpy array with the named time, open, high, low, close, tick_volume,
        spread and real_volume columns. Returns None in case of an error. The info on the error can be obtained using last_error().
    
    Example:
        rom datetime import datetime
        import MetaTrader5 as mt5
        # display data on the MetaTrader 5 package
        print("MetaTrader5 package author: ",mt5.__author__)
        print("MetaTrader5 package version: ",mt5.__version__)
        
        # import the 'pandas' module for displaying data obtained in the tabular form
        import pandas as pd
        pd.set_option('display.max_columns', 500) # number of columns to be displayed
        pd.set_option('display.width', 1500)      # max table width to display
        # import pytz module for working with time zone
        import pytz
        
        # establish connection to MetaTrader 5 terminal
        if not mt5.initialize():
            print("initialize() failed, error code =",mt5.last_error())
            quit()
        
        # set time zone to UTC
        timezone = pytz.timezone("Etc/UTC")
        # create 'datetime' objects in UTC time zone to avoid the implementation of a local time zone offset
        utc_from = datetime(2020, 1, 10, tzinfo=timezone)
        utc_to = datetime(2020, 1, 11, hour = 13, tzinfo=timezone)
        # get bars from USDJPY M5 within the interval of 2020.01.10 00:00 - 2020.01.11 13:00 in UTC time zone
        rates = mt5.copy_rates_range("USDJPY", mt5.TIMEFRAME_M5, utc_from, utc_to)
        
        # shut down connection to the MetaTrader 5 terminal
        mt5.shutdown()
        
        # display each element of obtained data in a new line
        print("Display obtained data 'as is'")
        counter=0
        for rate in rates:
            counter+=1
            if counter<=10:
                print(rate)
        
        # create DataFrame out of the obtained data
        rates_frame = pd.DataFrame(rates)
        # convert time in seconds into the 'datetime' format
        rates_frame['time']=pd.to_datetime(rates_frame['time'], unit='s')
        
        # display data
        print("\nDisplay dataframe with data")
        print(rates_frame.head(10))
    """


def copy_ticks_from(
    symbol: str,
    date_from: Union[dt.datetime, int],
    count: int,
    flags: int,
    /,
) -> Optional[np.ndarray[np.void]]:
    """Get ticks from the MetaTrader 5 terminal starting from the specified date.

    See the CopyTicks function for more information.
    When creating the 'datetime' object, Python uses the local time zone,
    while MetaTrader 5 stores tick and bar open time in UTC time zone (without the shift).
    Therefore, 'datetime' should be created in UTC time for executing functions that use time.
    Data received from the MetaTrader 5 terminal has UTC time.
    COPY_TICKS defines the types of ticks that can be requested using the copy_ticks_from() and copy_ticks_range() functions.
    |ID              |Description                                      |
    |:---------------|:------------------------------------------------|
    |COPY_TICKS_ALL  |all ticks                                        |
    |COPY_TICKS_INFO |ticks containing Bid and/or Ask price changes    |
    |COPY_TICKS_TRADE|ticks containing Last and/or Volume price changes|
    TICK_FLAG defines possible flags for ticks. These flags are used to describe ticks obtained by the copy_ticks_from() and copy_ticks_range() functions.
    |ID              |Description            |
    |:---------------|:----------------------|
    |TICK_FLAG_BID   |Bid price changed      |
    |TICK_FLAG_ASK   |Ask price changed      |
    |TICK_FLAG_LAST  |Last price changed     |
    |TICK_FLAG_VOLUME|Volume changed         |
    |TICK_FLAG_BUY   |last Buy price changed |
    |TICK_FLAG_SELL  |last Sell price changed|

    Args:
        symbol: Financial instrument name, for example, "EURUSD". Required unnamed parameter.
        from: Date the ticks are requested from.
            Set by the 'datetime' object or as a number of seconds elapsed since 1970.01.01.
            Required unnamed parameter.
        count: Number of ticks to receive. Required unnamed parameter.
        flags: A flag to define the type of the requested ticks.
            COPY_TICKS_INFO – ticks with Bid and/or Ask changes,
            COPY_TICKS_TRADE – ticks with changes in Last and Volume,
            COPY_TICKS_ALL – all ticks. Flag values are described in the COPY_TICKS enumeration.
            Required unnamed parameter.
    
    Returns:
        Returns ticks as the numpy array with the named time, bid, ask, last and flags columns.
        The 'flags' value can be a combination of flags from the TICK_FLAG enumeration.
        Return None in case of an error. The info on the error can be obtained using last_error().
    
    Example:
        from datetime import datetime
        import MetaTrader5 as mt5
        # display data on the MetaTrader 5 package
        print("MetaTrader5 package author: ",mt5.__author__)
        print("MetaTrader5 package version: ",mt5.__version__)
        
        # import the 'pandas' module for displaying data obtained in the tabular form
        import pandas as pd
        pd.set_option('display.max_columns', 500) # number of columns to be displayed
        pd.set_option('display.width', 1500)      # max table width to display
        # import pytz module for working with time zone
        import pytz
        
        # establish connection to MetaTrader 5 terminal
        if not mt5.initialize():
            print("initialize() failed, error code =",mt5.last_error())
            quit()
        
        # set time zone to UTC
        timezone = pytz.timezone("Etc/UTC")
        # create 'datetime' object in UTC time zone to avoid the implementation of a local time zone offset
        utc_from = datetime(2020, 1, 10, tzinfo=timezone)
        # request 100 000 EURUSD ticks starting from 10.01.2019 in UTC time zone
        ticks = mt5.copy_ticks_from("EURUSD", utc_from, 100000, mt5.COPY_TICKS_ALL)
        print("Ticks received:",len(ticks))
        
        # shut down connection to the MetaTrader 5 terminal
        mt5.shutdown()
        
        # display data on each tick on a new line
        print("Display obtained ticks 'as is'")
        count = 0
        for tick in ticks:
            count+=1
            print(tick)
            if count >= 10:
                break
        
        # create DataFrame out of the obtained data
        ticks_frame = pd.DataFrame(ticks)
        # convert time in seconds into the datetime format
        ticks_frame['time']=pd.to_datetime(ticks_frame['time'], unit='s')
        
        # display data
        print("\nDisplay dataframe with ticks")
        print(ticks_frame.head(10))  
        """


def copy_ticks_range(
    symbol: str,
    date_from: Union[dt.datetime, int],
    date_to: Union[dt.datetime, int],
    flags: int,
    /,
) -> Optional[np.ndarray[np.void]]:
    """Get ticks for the specified date range from the MetaTrader 5 terminal.

    See the CopyTicks function for more information.
    When creating the 'datetime' object, Python uses the local time zone,
    while MetaTrader 5 stores tick and bar open time in UTC time zone (without the shift).
    Therefore, 'datetime' should be created in UTC time for executing functions that use time.
    The data obtained from MetaTrader 5 have UTC time,
    but Python applies the local time shift again when trying to print them.
    Thus, the obtained data should also be corrected for visual presentation.

    Args:
        symbol: Financial instrument name, for example, "EURUSD". Required unnamed parameter.
        date_from: Date the ticks are requested from.
            Set by the 'datetime' object or as a number of seconds elapsed since 1970.01.01.
            Required unnamed parameter.
        date_to: Date, up to which the ticks are requested.
            Set by the 'datetime' object or as a number of seconds elapsed since 1970.01.01.
            Required unnamed parameter.
        flags: A flag to define the type of the requested ticks.
            COPY_TICKS_INFO – ticks with Bid and/or Ask changes,
            COPY_TICKS_TRADE – ticks with changes in Last and Volume,
            COPY_TICKS_ALL – all ticks. Flag values are described in the COPY_TICKS enumeration.
            Required unnamed parameter.
    
    Returns:
        Returns ticks as the numpy array with the named time, bid, ask, last and flags columns.
        The 'flags' value can be a combination of flags from the TICK_FLAG enumeration.
        Return None in case of an error. The info on the error can be obtained using last_error().
    
    Example:
        from datetime import datetime
        import MetaTrader5 as mt5
        # display data on the MetaTrader 5 package
        print("MetaTrader5 package author: ",mt5.__author__)
        print("MetaTrader5 package version: ",mt5.__version__)
        
        # import the 'pandas' module for displaying data obtained in the tabular form
        import pandas as pd
        pd.set_option('display.max_columns', 500) # number of columns to be displayed
        pd.set_option('display.width', 1500)      # max table width to display
        # import pytz module for working with time zone
        import pytz
        
        # establish connection to MetaTrader 5 terminal
        if not mt5.initialize():
            print("initialize() failed, error code =",mt5.last_error())
            quit()
        
        # set time zone to UTC
        timezone = pytz.timezone("Etc/UTC")
        # create 'datetime' objects in UTC time zone to avoid the implementation of a local time zone offset
        utc_from = datetime(2020, 1, 10, tzinfo=timezone)
        utc_to = datetime(2020, 1, 11, tzinfo=timezone)
        # request AUDUSD ticks within 11.01.2020 - 11.01.2020
        ticks = mt5.copy_ticks_range("AUDUSD", utc_from, utc_to, mt5.COPY_TICKS_ALL)
        print("Ticks received:",len(ticks))
        
        # shut down connection to the MetaTrader 5 terminal
        mt5.shutdown()
        
        # display data on each tick on a new line
        print("Display obtained ticks 'as is'")
        count = 0
        for tick in ticks:
            count+=1
            print(tick)
            if count >= 10:
                break
        
        # create DataFrame out of the obtained data
        ticks_frame = pd.DataFrame(ticks)
        # convert time in seconds into the datetime format
        ticks_frame['time']=pd.to_datetime(ticks_frame['time'], unit='s')
        
        # display data
        print("\nDisplay dataframe with ticks")
        print(ticks_frame.head(10)) 
        """


def orders_total() -> int:
    """Get the number of active orders.

    The function is similar to OrdersTotal.

    Returns:
        Integer value.
    
    Example:
        import MetaTrader5 as mt5
        # display data on the MetaTrader 5 package
        print("MetaTrader5 package author: ",mt5.__author__)
        print("MetaTrader5 package version: ",mt5.__version__)
        
        # establish connection to MetaTrader 5 terminal
        if not mt5.initialize():
            print("initialize() failed, error code =",mt5.last_error())
            quit()
        
        # check the presence of active orders
        orders=mt5.orders_total()
        if orders>0:
            print("Total orders=",orders)
        else:
            print("Orders not found")
        
        # shut down connection to the MetaTrader 5 terminal
        mt5.shutdown()
    """


class TradeOrder(NamedTuple):
    ticket: int
    time_setup: int
    time_setup_msc: int
    time_expiration: int
    type: int
    type_time: int
    type_filling: int
    state: int
    magic: int
    volume_current: float
    price_open: float
    sl: float
    tp: float
    price_current: float
    symbol: str
    comment: str
    external_id: str


def orders_get(
    symbol: Optional[str] = None,
    group: Optional[str] = None,
    ticket: Optional[int] = None
) -> Tuple[TradeOrder, ...]:
    """Get active orders with the ability to filter by symbol or ticket. There are three call options.

    The function allows receiving all active orders within one call similar to the OrdersTotal and OrderSelect tandem.
    The group parameter allows sorting out orders by symbols. '*' can be used at the beginning and the end of a string.
    The group parameter may contain several comma separated conditions.
    A condition can be set as a mask using '*'. The logical negation symbol '!' can be used for an exclusion.
    All conditions are applied sequentially, which means conditions of including to a group should be specified first
    followed by an exclusion condition. For example, group="*, !EUR" means that orders for all symbols should be selected
    first and the ones containing "EUR" in symbol names should be excluded afterwards.


    Args:
        symbol: Symbol name. Optional named parameter.
            If a symbol is specified, the ticket parameter is ignored.
        group: The filter for arranging a group of necessary symbols.
            Optional named parameter. If the group is specified,
            the function returns only active orders meeting a specified criteria for a symbol name.
        ticket: Order ticket (ORDER_TICKET). Optional named parameter.
    
    Returns:
        Return info in the form of a named tuple structure (namedtuple).
        Return None in case of an error. The info on the error can be obtained using last_error().
    
    Example:
        import MetaTrader5 as mt5
        import pandas as pd
        pd.set_option('display.max_columns', 500) # number of columns to be displayed
        pd.set_option('display.width', 1500)      # max table width to display
        # display data on the MetaTrader 5 package
        print("MetaTrader5 package author: ",mt5.__author__)
        print("MetaTrader5 package version: ",mt5.__version__)
        print()
        # establish connection to the MetaTrader 5 terminal
        if not mt5.initialize():
            print("initialize() failed, error code =",mt5.last_error())
            quit()
        
        # display data on active orders on GBPUSD
        orders=mt5.orders_get(symbol="GBPUSD")
        if orders is None:
            print("No orders on GBPUSD, error code={}".format(mt5.last_error()))
        else:
            print("Total orders on GBPUSD:",len(orders))
            # display all active orders
            for order in orders:
                print(order)
        print()
        
        # get the list of orders on symbols whose names contain "*GBP*"
        gbp_orders=mt5.orders_get(group="*GBP*")
        if gbp_orders is None:
            print("No orders with group=\"*GBP*\", error code={}".format(mt5.last_error()))
        else:
            print("orders_get(group=\"*GBP*\")={}".format(len(gbp_orders)))
            # display these orders as a table using pandas.DataFrame
            df=pd.DataFrame(list(gbp_orders),columns=gbp_orders[0]._asdict().keys())
            df.drop(['time_done', 'time_done_msc', 'position_id', 'position_by_id', 'reason', 'volume_initial', 'price_stoplimit'], axis=1, inplace=True)
            df['time_setup'] = pd.to_datetime(df['time_setup'], unit='s')
            print(df)
        
        # shut down connection to the MetaTrader 5 terminal
        mt5.shutdown()
    """


def order_calc_margin(
    action: int,
    symbol: str,
    volume: float,
    price: float,
    /,
) -> Optional[float]:
    """Return margin in the account currency to perform a specified trading operation.

    The function allows estimating the margin necessary for a specified order type on the current account and in the current market environment without considering the current pending orders and open positions. The function is similar to OrderCalcMargin.
    |ID                         |Description                                                                         |
    |:--------------------------|:-----------------------------------------------------------------------------------|
    |ORDER_TYPE_BUY             |Market buy order                                                                    |
    |ORDER_TYPE_SELL            |Market sell order                                                                   |
    |ORDER_TYPE_BUY_LIMIT       |Buy Limit pending order                                                             |
    |ORDER_TYPE_SELL_LIMIT      |Sell Limit pending order                                                            |
    |ORDER_TYPE_BUY_STOP        |Buy Stop pending order                                                              |
    |ORDER_TYPE_SELL_STOP       |Sell Stop pending order                                                             |
    |ORDER_TYPE_BUY_STOP_LIMIT  |Upon reaching the order price, Buy Limit pending order is placed at StopLimit price |
    |ORDER_TYPE_SELL_STOP_LIMIT |Upon reaching the order price, Sell Limit pending order is placed at StopLimit price|
    |ORDER_TYPE_CLOSE_BY        |Order for closing a position by an opposite one                                     |

    Args:
        action: Order type taking values from the ORDER_TYPE enumeration. Required unnamed parameter.
        symbol: Financial instrument name. Required unnamed parameter.
        volume: Trading operation volume. Required unnamed parameter.
        price: Open price. Required unnamed parameter.
    
    Returns:
        Real value if successful, otherwise None. The error info can be obtained using last_error().

    Example:
        import MetaTrader5 as mt5
        # display data on the MetaTrader 5 package
        print("MetaTrader5 package author: ",mt5.__author__)
        print("MetaTrader5 package version: ",mt5.__version__)
        
        # establish connection to MetaTrader 5 terminal
        if not mt5.initialize():
            print("initialize() failed, error code =",mt5.last_error())
            quit()
        
        # get account currency
        account_currency=mt5.account_info().currency
        print("Account сurrency:",account_currency)
        
        # arrange the symbol list
        symbols=("EURUSD","GBPUSD","USDJPY", "USDCHF","EURJPY","GBPJPY")
        print("Symbols to check margin:", symbols)
        action=mt5.ORDER_TYPE_BUY
        lot=0.1
        for symbol in symbols:
            symbol_info=mt5.symbol_info(symbol)
            if symbol_info is None:
                print(symbol,"not found, skipped")
                continue
            if not symbol_info.visible:
                print(symbol, "is not visible, trying to switch on")
                if not mt5.symbol_select(symbol,True):
                    print("symbol_select({}}) failed, skipped",symbol)
                    continue
            ask=mt5.symbol_info_tick(symbol).ask
            margin=mt5.order_calc_margin(action,symbol,lot,ask)
            if margin != None:
                print("   {} buy {} lot margin: {} {}".format(symbol,lot,margin,account_currency));
            else:
                print("order_calc_margin failed: , error code =", mt5.last_error())
        # shut down connection to the MetaTrader 5 terminal
        mt5.shutdown()       
    """


def order_calc_profit(
    action: int,
    symbol: str,
    volume: float,
    price_open: float,
    price_close: float,
    /,
) -> Optional[float]:
    """Return profit in the account currency for a specified trading operation.

    The function allows estimating a trading operation result on
    the current account and in the current trading environment.
    The function is similar to OrderCalcProfit.

    Args:
        action: Order type may take one of the two ORDER_TYPE enumeration values:
            ORDER_TYPE_BUY or ORDER_TYPE_SELL. Required unnamed parameter.
        symbol: Financial instrument name. Required unnamed parameter.
        volume: Trading operation volume. Required unnamed parameter.
        price_open: Open price. Required unnamed parameter.
        price_close: Close price. Required unnamed parameter.
    
    Returns:
        Real value if successful, otherwise None. The error info can be obtained using last_error().

    Example:
        import MetaTrader5 as mt5
        # display data on the MetaTrader 5 package
        print("MetaTrader5 package author: ",mt5.__author__)
        print("MetaTrader5 package version: ",mt5.__version__)
        
        # establish connection to MetaTrader 5 terminal
        if not mt5.initialize():
            print("initialize() failed, error code =",mt5.last_error())
            quit()
        
        # get account currency
        account_currency=mt5.account_info().currency
        print("Account сurrency:",account_currency)
        
        # arrange the symbol list
        symbols = ("EURUSD","GBPUSD","USDJPY")
        print("Symbols to check margin:", symbols)
        # estimate profit for buying and selling
        lot=1.0
        distance=300
        for symbol in symbols:
            symbol_info=mt5.symbol_info(symbol)
            if symbol_info is None:
                print(symbol,"not found, skipped")
                continue
            if not symbol_info.visible:
                print(symbol, "is not visible, trying to switch on")
                if not mt5.symbol_select(symbol,True):
                    print("symbol_select({}}) failed, skipped",symbol)
                    continue
            point=mt5.symbol_info(symbol).point
            symbol_tick=mt5.symbol_info_tick(symbol)
            ask=symbol_tick.ask
            bid=symbol_tick.bid
            buy_profit=mt5.order_calc_profit(mt5.ORDER_TYPE_BUY,symbol,lot,ask,ask+distance*point)
            if buy_profit!=None:
                print("   buy {} {} lot: profit on {} points => {} {}".format(symbol,lot,distance,buy_profit,account_currency));
            else:
                print("order_calc_profit(ORDER_TYPE_BUY) failed, error code =",mt5.last_error())
            sell_profit=mt5.order_calc_profit(mt5.ORDER_TYPE_SELL,symbol,lot,bid,bid-distance*point)
            if sell_profit!=None:
                print("   sell {} {} lots: profit on {} points => {} {}".format(symbol,lot,distance,sell_profit,account_currency));
            else:
                print("order_calc_profit(ORDER_TYPE_SELL) failed, error code =",mt5.last_error())
            print()
        
        # shut down connection to the MetaTrader 5 terminal
        mt5.shutdown()
    """


class TradeRequest(NamedTuple):
    action: int
    magic: int
    order: int
    symbol: str
    volume: float
    price: float
    stoplimit: float
    sl: float
    tp: float
    deviation: int
    type: int
    type_filling: int
    type_time: int
    expiration: Union[dt.datetime, int]
    comment: str
    position: int
    position_by: int


class OrderCheckResult(NamedTuple):
    retcode: int
    balance: float
    equity: float
    profit: float
    margin: float
    margin_free: float
    margin_level: float
    comment: str
    request: TradeRequest


def order_check(request: dict, /) -> Optional[OrderCheckResult]:
    """Check funds sufficiency for performing a required trading operation.

    Check result are returned as the MqlTradeCheckResult structure.
    Successful sending of a request does not entail that
    the requested trading operation will be executed successfully.
    The order_check function is similar to OrderCheck.
    TRADE_REQUEST_ACTIONS
    |ID                   |Description                                             |
    |:--------------------|:-------------------------------------------------------|
    |TRADE_ACTION_DEAL    |Place an order for an instant deal with                 |
    |                     |the specified parameters (set a market order)           |
    |TRADE_ACTION_PENDING |Place an order for performing a deal at specified\      |
    |                     |conditions (pending order)                              |
    |TRADE_ACTION_SLTP    |Change open position Stop Loss and Take Profit          |
    |TRADE_ACTION_MODIFY  |Change parameters of the previously placed trading order|
    |TRADE_ACTION_REMOVE  |Remove previously placed pending order                  |
    |TRADE_ACTION_CLOSE_BY|Close a position by an opposite one                     |
    ORDER_TYPE_FILLING
    |ID                  |Description                                                |
    |:-------------------|:----------------------------------------------------------|
    |ORDER_FILLING_FOK   |This execution policy means that an order can be           |
    |                    |executed only in the specified volume.                     |
    |                    |If the necessary amount of a financial instrument          |
    |                    |is currently unavailable in the market, the order          |
    |                    |will not be executed. The desired volume can be made up    |
    |                    |of several available offers.                               |
    |ORDER_FILLING_IOC   |An agreement to execute a deal at the maximum volume       |
    |                    |available in the market within the volume specified in     |
    |                    |the order. If the request cannot be filled completely,     |
    |                    |an order with the available volume will be executed,       |
    |                    |and the remaining volume will be canceled.                 |
    |ORDER_FILLING_RETURN|This policy is used only for market (ORDER_TYPE_BUY        |
    |                    |and ORDER_TYPE_SELL), limit and stop limit orders          |
    |                    |(ORDER_TYPE_BUY_LIMIT, ORDER_TYPE_SELL_LIMIT,              |
    |                    |ORDER_TYPE_BUY_STOP_LIMIT and ORDER_TYPE_SELL_STOP_LIMIT)  |
    |                    |and only for the symbols with Market or Exchange execution |
    |                    |modes. If filled partially, a market or limit order with   |
    |                    |the remaining volume is not canceled, and is processed     |
    |                    |further. During activation of the ORDER_TYPE_BUY_STOP_LIMIT|
    |                    |and ORDER_TYPE_SELL_STOP_LIMIT orders, an appropriate limit|
    |                    |order ORDER_TYPE_BUY_LIMIT/ORDER_TYPE_SELL_LIMIT with the  |
    |                    |ORDER_FILLING_RETURN type is created.                      |
    ORDER_TYPE_TIME
    |ID                      |Description                                               |
    |:-----------------------|:---------------------------------------------------------|
    |ORDER_TIME_GTC          |The order stays in the queue until it is manually canceled|
    |ORDER_TIME_DAY          |The order is active only during the current trading day   |
    |ORDER_TIME_SPECIFIED    |The order is active until the specified date              |
    |ORDER_TIME_SPECIFIED_DAY|The order is active until 23:59:59 of the specified day.  |
    |                        |If this time appears to be out of a trading session,      |
    |                        |the expiration is processed at the nearest trading time.  |

    Args:
        request: MqlTradeRequest type structure describing a required trading action.
            Required unnamed parameter. Example of filling in a request and the enumeration
            content are described below.
    
    Returns:
        Check result as the MqlTradeCheckResult structure. The request field in the answer contains the structure of a trading request passed to order_check().

    Example:
        import MetaTrader5 as mt5
        # display data on the MetaTrader 5 package
        print("MetaTrader5 package author: ",mt5.__author__)
        print("MetaTrader5 package version: ",mt5.__version__)
        
        # establish connection to MetaTrader 5 terminal
        if not mt5.initialize():
            print("initialize() failed, error code =",mt5.last_error())
            quit()
        
        # get account currency
        account_currency=mt5.account_info().currency
        print("Account сurrency:",account_currency)
        
        # prepare the request structure
        symbol="USDJPY"
        symbol_info = mt5.symbol_info(symbol)
        if symbol_info is None:
            print(symbol, "not found, can not call order_check()")
            mt5.shutdown()
            quit()
        
        # if the symbol is unavailable in MarketWatch, add it
        if not symbol_info.visible:
            print(symbol, "is not visible, trying to switch on")
            if not mt5.symbol_select(symbol,True):
                print("symbol_select({}}) failed, exit",symbol)
                mt5.shutdown()
                quit()
        
        # prepare the request
        point=mt5.symbol_info(symbol).point
        request = {
            "action": mt5.TRADE_ACTION_DEAL,
            "symbol": symbol,
            "volume": 1.0,
            "type": mt5.ORDER_TYPE_BUY,
            "price": mt5.symbol_info_tick(symbol).ask,
            "sl": mt5.symbol_info_tick(symbol).ask-100*point,
            "tp": mt5.symbol_info_tick(symbol).ask+100*point,
            "deviation": 10,
            "magic": 234000,
            "comment": "python script",
            "type_time": mt5.ORDER_TIME_GTC,
            "type_filling": mt5.ORDER_FILLING_RETURN,
        }
        
        # perform the check and display the result 'as is'
        result = mt5.order_check(request)
        print(result);
        # request the result as a dictionary and display it element by element
        result_dict=result._asdict()
        for field in result_dict.keys():
            print("   {}={}".format(field,result_dict[field]))
            # if this is a trading request structure, display it element by element as well
            if field=="request":
                traderequest_dict=result_dict[field]._asdict()
                for tradereq_filed in traderequest_dict:
                    print("       traderequest: {}={}".format(tradereq_filed,traderequest_dict[tradereq_filed]))
        
        # shut down connection to the MetaTrader 5 terminal
        mt5.shutdown()
    """


class OrderSendResult(NamedTuple):
    retcode: int
    deal: int
    order: int
    volume: float
    price: float
    bid: float
    ask: float
    comment: str
    request_id: int
    retcode_external: int
    request: TradeRequest


def order_send(request: dict, /) -> Optional[OrderSendResult]:
    """Send a request to perform a trading operation from the terminal to the trade server.

    The function is similar to OrderSend.
    A trading request passes several verification stages on the trade server.
    First, the validity of all the necessary request fields is checked.
    If there are no errors, the server accepts the order for further handling.
    See the OrderSend function description for the details about executing trading operations.
    The MqlTradeRequest trading request structure
    |Field       |Description                                                                    |
    |:-----------|:------------------------------------------------------------------------------|
    |action      |Trading operation type. The value can be one of the values of the              |
    |            |TRADE_REQUEST_ACTIONS enumeration                                              |
    |magic       |EA ID. Allows arranging the analytical handling of trading orders.             |
    |            |Each EA can set a unique ID when sending a trading request                     |
    |order       |Order ticket. Required for modifying pending orders                            |
    |symbol      |The name of the trading instrument, for which the order is placed.             |
    |            |Not required when modifying orders and closing positions                       |
    |volume      |Requested volume of a deal in lots. A real volume when making a deal depends   |
    |            |on an order execution type.                                                    |
    |price       |Price at which an order should be executed. The price is not set in case of    |
    |            |market orders for instruments of the "Market Execution"                        |
    |            |(SYMBOL_TRADE_EXECUTION_MARKET) type having the TRADE_ACTION_DEAL type         |
    |stoplimit   |A price a pending Limit order is set at when the price reaches the 'price'     |
    |            |value (this condition is mandatory). The pending order is not passed to the    |
    |            |trading system until that moment                                               |
    |sl          |A price a Stop Loss order is activated at when the price moves in an           |
    |            |unfavorable direction                                                          |
    |tp          |A price a Take Profit order is activated at when the price moves in a favorable|
    |            |direction                                                                      |
    |deviation   |Maximum acceptable deviation from the requested price, specified in points     |
    |type        |Order type. The value can be one of the values of the ORDER_TYPE enumeration   |
    |type_filling|Order filling type. The value can be one of the ORDER_TYPE_FILLING values      |
    |type_time   |Order type by expiration. The value can be one of the ORDER_TYPE_TIME values   |
    |expiration  |Pending order expiration time (for TIME_SPECIFIED type orders)                 |
    |comment     |Comment to an order                                                            |
    |position    |Position ticket. Fill it when changing and closing a position for its clear    |
    |            |identification. Usually, it is the same as the ticket of the order that opened |
    |            |the position.                                                                  |
    |position_by |Opposite position ticket. It is used when closing a position by an opposite one|
    |            |(opened at the same symbol but in the opposite direction).                     |

    Args:
        request: MqlTradeRequest type structure describing a required trading action.
            Required unnamed parameter. Example of filling in a request and the enumeration
            content are described below.

    Returns:
        Execution result as the MqlTradeResult structure. The request field in the answer contains the structure of a trading request passed to order_send().
    
    Example:
        import time
        import MetaTrader5 as mt5
        
        # display data on the MetaTrader 5 package
        print("MetaTrader5 package author: ", mt5.__author__)
        print("MetaTrader5 package version: ", mt5.__version__)
        
        # establish connection to the MetaTrader 5 terminal
        if not mt5.initialize():
            print("initialize() failed, error code =",mt5.last_error())
            quit()
        
        # prepare the buy request structure
        symbol = "USDJPY"
        symbol_info = mt5.symbol_info(symbol)
        if symbol_info is None:
            print(symbol, "not found, can not call order_check()")
            mt5.shutdown()
            quit()
        
        # if the symbol is unavailable in MarketWatch, add it
        if not symbol_info.visible:
            print(symbol, "is not visible, trying to switch on")
            if not mt5.symbol_select(symbol,True):
                print("symbol_select({}}) failed, exit",symbol)
                mt5.shutdown()
                quit()
        
        lot = 0.1
        point = mt5.symbol_info(symbol).point
        price = mt5.symbol_info_tick(symbol).ask
        deviation = 20
        request = {
            "action": mt5.TRADE_ACTION_DEAL,
            "symbol": symbol,
            "volume": lot,
            "type": mt5.ORDER_TYPE_BUY,
            "price": price,
            "sl": price - 100 * point,
            "tp": price + 100 * point,
            "deviation": deviation,
            "magic": 234000,
            "comment": "python script open",
            "type_time": mt5.ORDER_TIME_GTC,
            "type_filling": mt5.ORDER_FILLING_RETURN,
        }
        
        # send a trading request
        result = mt5.order_send(request)
        # check the execution result
        print("1. order_send(): by {} {} lots at {} with deviation={} points".format(symbol,lot,price,deviation));
        if result.retcode != mt5.TRADE_RETCODE_DONE:
            print("2. order_send failed, retcode={}".format(result.retcode))
            # request the result as a dictionary and display it element by element
            result_dict=result._asdict()
            for field in result_dict.keys():
                print("   {}={}".format(field,result_dict[field]))
                # if this is a trading request structure, display it element by element as well
                if field=="request":
                    traderequest_dict=result_dict[field]._asdict()
                    for tradereq_filed in traderequest_dict:
                        print("       traderequest: {}={}".format(tradereq_filed,traderequest_dict[tradereq_filed]))
            print("shutdown() and quit")
            mt5.shutdown()
            quit()
        
        print("2. order_send done, ", result)
        print("   opened position with POSITION_TICKET={}".format(result.order))
        print("   sleep 2 seconds before closing position #{}".format(result.order))
        time.sleep(2)
        # create a close request
        position_id=result.order
        price=mt5.symbol_info_tick(symbol).bid
        deviation=20
        request={
            "action": mt5.TRADE_ACTION_DEAL,
            "symbol": symbol,
            "volume": lot,
            "type": mt5.ORDER_TYPE_SELL,
            "position": position_id,
            "price": price,
            "deviation": deviation,
            "magic": 234000,
            "comment": "python script close",
            "type_time": mt5.ORDER_TIME_GTC,
            "type_filling": mt5.ORDER_FILLING_RETURN,
        }
        # send a trading request
        result=mt5.order_send(request)
        # check the execution result
        print("3. close position #{}: sell {} {} lots at {} with deviation={} points".format(position_id,symbol,lot,price,deviation));
        if result.retcode != mt5.TRADE_RETCODE_DONE:
            print("4. order_send failed, retcode={}".format(result.retcode))
            print("   result",result)
        else:
            print("4. position #{} closed, {}".format(position_id,result))
            # request the result as a dictionary and display it element by element
            result_dict=result._asdict()
            for field in result_dict.keys():
                print("   {}={}".format(field,result_dict[field]))
                # if this is a trading request structure, display it element by element as well
                if field=="request":
                    traderequest_dict=result_dict[field]._asdict()
                    for tradereq_filed in traderequest_dict:
                        print("       traderequest: {}={}".format(tradereq_filed,traderequest_dict[tradereq_filed]))
        
        # shut down connection to the MetaTrader 5 terminal
        mt5.shutdown()
    """


def positions_total() -> int:
    """Get the number of open positions.

    The function is similar to PositionsTotal.

    Returns:
        Integer value.

    Example:
        import MetaTrader5 as mt5
        # display data on the MetaTrader 5 package
        print("MetaTrader5 package author: ",mt5.__author__)
        print("MetaTrader5 package version: ",mt5.__version__)
        
        # establish connection to MetaTrader 5 terminal
        if not mt5.initialize():
            print("initialize() failed, error code =",mt5.last_error())
            quit()
        
        # check the presence of open positions
        positions_total=mt5.positions_total()
        if positions_total>0:
            print("Total positions=",positions_total)
        else:
            print("Positions not found")
        
        # shut down connection to the MetaTrader 5 terminal
        mt5.shutdown()
    """


class TradePosition(NamedTuple):
    ticket: int
    time: int
    time_msc: int
    time_update: int
    time_update_msc: int
    type: int
    magic: int
    identifier: int
    reason: int
    volume: float
    price_open: float
    sl: float
    tp: float
    price_current: float
    swap: float
    profit: float
    symbol: str
    comment: str
    external_id: str


def positions_get(
    symbol: Optional[str] = None,
    group: Optional[str] = None,
    ticket: Optional[int] = None,
) -> Optional[Tuple[TradePosition, ...]]:
    """Get open positions with the ability to filter by symbol or ticket.

    There are three call options.
    The function allows receiving all open positions within one call similar
    to the PositionsTotal and PositionSelect tandem.
    The group parameter may contain several comma separated conditions.
    A condition can be set as a mask using '*'. The logical negation
    symbol '!' can be used for an exclusion. All conditions are applied sequentially,
    which means conditions of including to a group should be specified first followed
    by an exclusion condition. For example, group="*, !EUR" means that positions for
    all symbols should be selected first and the ones containing "EUR" in symbol names
    should be excluded afterwards.

    Args:
        symbol: Symbol name. Optional named parameter.
            If a symbol is specified, the ticket parameter is ignored.
        group: The filter for arranging a group of necessary symbols.
            Optional named parameter. If the group is specified, the function
            returns only positions meeting a specified criteria for a symbol name.
        ticket: Position ticket (POSITION_TICKET). Optional named parameter.

    Returns:
        Return info in the form of a named tuple structure (namedtuple).
        Return None in case of an error. The info on the error
        can be obtained using last_error().

    Example:
        import MetaTrader5 as mt5
        import pandas as pd
        pd.set_option('display.max_columns', 500) # number of columns to be displayed
        pd.set_option('display.width', 1500)      # max table width to display
        # display data on the MetaTrader 5 package
        print("MetaTrader5 package author: ",mt5.__author__)
        print("MetaTrader5 package version: ",mt5.__version__)
        print()
        # establish connection to the MetaTrader 5 terminal
        if not mt5.initialize():
            print("initialize() failed, error code =",mt5.last_error())
            quit()
        
        # get open positions on USDCHF
        positions=mt5.positions_get(symbol="USDCHF")
        if positions==None:
            print("No positions on USDCHF, error code={}".format(mt5.last_error()))
        elif len(positions)>0:
            print("Total positions on USDCHF =",len(positions))
            # display all open positions
            for position in positions:
                print(position)
        
        # get the list of positions on symbols whose names contain "*USD*"
        usd_positions=mt5.positions_get(group="*USD*")
        if usd_positions==None:
            print("No positions with group=\"*USD*\", error code={}".format(mt5.last_error()))
        elif len(usd_positions)>0:
            print("positions_get(group=\"*USD*\")={}".format(len(usd_positions)))
            # display these positions as a table using pandas.DataFrame
            df=pd.DataFrame(list(usd_positions),columns=usd_positions[0]._asdict().keys())
            df['time'] = pd.to_datetime(df['time'], unit='s')
            df.drop(['time_update', 'time_msc', 'time_update_msc', 'external_id'], axis=1, inplace=True)
            print(df)
        
        # shut down connection to the MetaTrader 5 terminal
        mt5.shutdown()
    """


def history_orders_total(
    date_from: Union[dt.datetime, int],
    date_to: Union[dt.datetime, int],
    /,
) -> int:
    """Get the number of orders in trading history within the specified interval.

    Args:
        date_from: Date the orders are requested from.
            Set by the 'datetime' object or as a number of seconds elapsed since 1970.01.01.
            Required unnamed parameter.
        date_to: Date, up to which the orders are requested.
            Set by the 'datetime' object or as a number of seconds elapsed since 1970.01.01.
            Required unnamed parameter.
    
    Returns:
        Integer value.

    Example:
        from datetime import datetime
        import MetaTrader5 as mt5
        # display data on the MetaTrader 5 package
        print("MetaTrader5 package author: ",mt5.__author__)
        print("MetaTrader5 package version: ",mt5.__version__)
        
        # establish connection to MetaTrader 5 terminal
        if not mt5.initialize():
            print("initialize() failed, error code =",mt5.last_error())
            quit()
        
        # get the number of orders in history
        from_date=datetime(2020,1,1)
        to_date=datetime.now()
        history_orders=mt5.history_orders_total(from_date, datetime.now())
        if history_orders>0:
            print("Total history orders=",history_orders)
        else:
            print("Orders not found in history")
        
        # shut down connection to the MetaTrader 5 terminal
        mt5.shutdown()
    """


def history_orders_get(
    date_from: Optional[Union[dt.datetime, int]] = None,
    date_to: Optional[Union[dt.datetime, int]] = None,
    /,
    group: Optional[str] = None,
    ticket: Optional[int] = None,
    position: Optional[int] = None,
) -> Optional[Tuple[TradeOrder, ...]]:
    """Get orders from trading history with the ability to filter by ticket or position.

    The function allows receiving all history orders within a specified period in
    a single call similar to the HistoryOrdersTotal and HistoryOrderSelect tandem.
    The group parameter may contain several comma separated conditions.
    A condition can be set as a mask using '*'. The logical negation symbol
    '!' can be used for an exclusion. All conditions are applied sequentially,
    which means conditions of including to a group should be specified first followed by
    an exclusion condition. For example, group="*, !EUR" means that deals for all symbols
    should be selected first and the ones containing "EUR" in symbol names should be
    excluded afterwards.

    Args:
        date_from: Date the orders are requested from.
            Set by the 'datetime' object or as a number of seconds elapsed since 1970.01.01.
            Required unnamed parameter is specified first.
        date_to: Date, up to which the orders are requested.
            Set by the 'datetime' object or as a number of seconds elapsed since 1970.01.01.
            Required unnamed parameter is specified second.
        group: The filter for arranging a group of necessary symbols.
            Optional named parameter. If the group is specified,
            the function returns only orders meeting a specified criteria for a symbol name.
        ticket: Order ticket that should be received. Optional parameter.
            If not specified, the filter is not applied.
        position: Ticket of a position (stored in ORDER_POSITION_ID)
            all orders should be received for. Optional parameter. If not specified,
            the filter is not applied.
    
    Returns:
        Return info in the form of a named tuple structure (namedtuple). Return None in case of an error. The info on the error can be obtained using last_error().

    Example:
        from datetime import datetime
        import MetaTrader5 as mt5
        import pandas as pd
        pd.set_option('display.max_columns', 500) # number of columns to be displayed
        pd.set_option('display.width', 1500)      # max table width to display
        # display data on the MetaTrader 5 package
        print("MetaTrader5 package author: ",mt5.__author__)
        print("MetaTrader5 package version: ",mt5.__version__)
        print()
        # establish connection to the MetaTrader 5 terminal
        if not mt5.initialize():
            print("initialize() failed, error code =",mt5.last_error())
            quit()
        
        # get the number of orders in history
        from_date=datetime(2020,1,1)
        to_date=datetime.now()
        history_orders=mt5.history_orders_get(from_date, to_date, group="*GBP*")
        if history_orders==None:
            print("No history orders with group=\"*GBP*\", error code={}".format(mt5.last_error()))
        elif len(history_orders)>0:
            print("history_orders_get({}, {}, group=\"*GBP*\")={}".format(from_date,to_date,len(history_orders)))
        print()
        
        # display all historical orders by a position ticket
        position_id=530218319
        position_history_orders=mt5.history_orders_get(position=position_id)
        if position_history_orders==None:
            print("No orders with position #{}".format(position_id))
            print("error code =",mt5.last_error())
        elif len(position_history_orders)>0:
            print("Total history orders on position #{}: {}".format(position_id,len(position_history_orders)))
            # display all historical orders having a specified position ticket
            for position_order in position_history_orders:        
                print(position_order)
            print()
            # display these orders as a table using pandas.DataFrame
            df=pd.DataFrame(list(position_history_orders),columns=position_history_orders[0]._asdict().keys())
            df.drop(['time_expiration','type_time','state','position_by_id','reason','volume_current','price_stoplimit','sl','tp'], axis=1, inplace=True)
            df['time_setup'] = pd.to_datetime(df['time_setup'], unit='s')
            df['time_done'] = pd.to_datetime(df['time_done'], unit='s')
            print(df)
        
        # shut down connection to the MetaTrader 5 terminal
        mt5.shutdown()
    """


def history_deals_total(
    date_from: Union[dt.datetime, int],
    date_to: Union[dt.datetime, int],
    /,
) -> int:
    """Get the number of deals in trading history within the specified interval.

    The function is similar to HistoryDealsTotal.

    Args:
        date_from: Date the deals are requested from.
            Set by the 'datetime' object or as a number of seconds elapsed since 1970.01.01.
            Required unnamed parameter.
        date_to: Date, up to which the deals are requested.
            Set by the 'datetime' object or as a number of seconds elapsed since 1970.01.01.
            Required unnamed parameter.

    Example:
        from datetime import datetime
        import MetaTrader5 as mt5
        # display data on the MetaTrader 5 package
        print("MetaTrader5 package author: ",mt5.__author__)
        print("MetaTrader5 package version: ",mt5.__version__)
        
        # establish connection to MetaTrader 5 terminal
        if not mt5.initialize():
            print("initialize() failed, error code =",mt5.last_error())
            quit()
        
        # get the number of deals in history
        from_date=datetime(2020,1,1)
        to_date=datetime.now()
        deals=mt5.history_deals_total(from_date, to_date)
        if deals>0:
            print("Total deals=",deals)
        else:
            print("Deals not found in history")
        
        # shut down connection to the MetaTrader 5 terminal
        mt5.shutdown()
    """


class TradeDeal(NamedTuple):
    ticket: int
    order: int
    time: int
    time_msc: int
    type: int
    entry: int
    magic: int
    position_id: int
    reason: int
    volume: float
    price: float
    commission: float
    swap: float
    profit: float
    fee: float
    symbol: str
    comment: str
    external_id: str


def history_deals_get(
    date_from: Optional[Union[dt.datetime, int]] = None,
    date_to: Optional[Union[dt.datetime, int]] = None,
    /,
    group: Optional[str] = None,
    ticket: Optional[int] = None,
    position: Optional[int] = None,
) -> Optional[Tuple[TradeDeal, ...]]:
    """Get deals from trading history within the specified interval with the ability to filter by ticket or position.

    The function allows receiving all history deals within a specified period in
    a single call similar to the HistoryDealsTotal and HistoryDealSelect tandem.
    The group parameter allows sorting out deals by symbols.
    '*' can be used at the beginning and the end of a string.
    The group parameter may contain several comma separated conditions.
    A condition can be set as a mask using '*'. The logical negation symbol
    '!' can be used for an exclusion. All conditions are applied sequentially,
    which means conditions of including to a group should be specified first followed by
    an exclusion condition. For example, group="*, !EUR" means that deals for all symbols
    should be selected first and the ones containing "EUR" in symbol names should be
    excluded afterwards.

    Args:
        date_from: Date the orders are requested from.
            Set by the 'datetime' object or as a number of seconds elapsed since 1970.01.01.
            Required unnamed parameter is specified first.
        date_to: Date, up to which the orders are requested.
            Set by the 'datetime' object or as a number of seconds elapsed since 1970.01.01.
            Required unnamed parameter is specified second.
        group: The filter for arranging a group of necessary symbols.
            Optional named parameter. If the group is specified,
            the function returns only deals meeting a specified criteria for a symbol name.
        ticket: Ticket of an order (stored in DEAL_ORDER) all deals should be received for.
            Optional parameter. If not specified, the filter is not applied.
        position: Ticket of a position (stored in DEAL_POSITION_ID) all deals should be
            received for. Optional parameter. If not specified, the filter is not applied.

    Returns:
        Return info in the form of a named tuple structure (namedtuple).
        Return None in case of an error. The info on the error can be obtained using last_error().

    Example:
        import MetaTrader5 as mt5
        from datetime import datetime
        import pandas as pd
        pd.set_option('display.max_columns', 500) # number of columns to be displayed
        pd.set_option('display.width', 1500)      # max table width to display
        # display data on the MetaTrader 5 package
        print("MetaTrader5 package author: ",mt5.__author__)
        print("MetaTrader5 package version: ",mt5.__version__)
        print()
        # establish connection to the MetaTrader 5 terminal
        if not mt5.initialize():
            print("initialize() failed, error code =",mt5.last_error())
            quit()
        
        # get the number of deals in history
        from_date=datetime(2020,1,1)
        to_date=datetime.now()
        # get deals for symbols whose names contain "GBP" within a specified interval
        deals=mt5.history_deals_get(from_date, to_date, group="*GBP*")
        if deals==None:
            print("No deals with group=\"*USD*\", error code={}".format(mt5.last_error()))
        elif len(deals)> 0:
            print("history_deals_get({}, {}, group=\"*GBP*\")={}".format(from_date,to_date,len(deals)))
        
        # get deals for symbols whose names contain neither "EUR" nor "GBP"
        deals = mt5.history_deals_get(from_date, to_date, group="*,!*EUR*,!*GBP*")
        if deals == None:
            print("No deals, error code={}".format(mt5.last_error()))
        elif len(deals) > 0:
            print("history_deals_get(from_date, to_date, group=\"*,!*EUR*,!*GBP*\") =", len(deals))
            # display all obtained deals 'as is'
            for deal in deals:
                print("  ",deal)
            print()
            # display these deals as a table using pandas.DataFrame
            df=pd.DataFrame(list(deals),columns=deals[0]._asdict().keys())
            df['time'] = pd.to_datetime(df['time'], unit='s')
            print(df)
        print("")
        
        # get all deals related to the position #530218319
        position_id=530218319
        position_deals = mt5.history_deals_get(position=position_id)
        if position_deals == None:
            print("No deals with position #{}".format(position_id))
            print("error code =", mt5.last_error())
        elif len(position_deals) > 0:
            print("Deals with position id #{}: {}".format(position_id, len(position_deals)))
            # display these deals as a table using pandas.DataFrame
            df=pd.DataFrame(list(position_deals),columns=position_deals[0]._asdict().keys())
            df['time'] = pd.to_datetime(df['time'], unit='s')
            print(df)
        
        # shut down connection to the MetaTrader 5 terminal
        mt5.shutdown()
    """
