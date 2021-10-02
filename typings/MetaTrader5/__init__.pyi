import enum
from typing import Optional, Tuple


def initialize(
    path: Optional[str] = None,
    *,
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
    login: Optional[str] = None,
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


class ErrorCodes(enum.IntEnum):
    """Error code enum.

    |Constant                   |Description                     |
    |:--------------------------|:-------------------------------|
    |RES_S_OK                   |generic success                 |
    |RES_E_FAIL                 |generic fail                    |
    |RES_E_INVALID_PARAMS       |invalid arguments/parameters    |
    |RES_E_NO_MEMORY            |no memory condition             |
    |RES_E_NOT_FOUND            |no history                      |
    |RES_E_INVALID_VERSION      |invalid version                 |
    |RES_E_AUTH_FAILED          |authorization failed            |
    |RES_E_UNSUPPORTED          |unsupported method              |
    |RES_E_AUTO_TRADING_DISABLED|auto-trading disabled           |
    |RES_E_INTERNAL_FAIL        |internal IPC general error      |
    |RES_E_INTERNAL_FAIL_SEND   |internal IPC send failed        |
    |RES_E_INTERNAL_FAIL_RECEIVE|internal IPC recv failed        |
    |RES_E_INTERNAL_FAIL_INIT   |internal IPC initialization fail|
    |RES_E_INTERNAL_FAIL_CONNECT|internal IPC no ipc             |
    |RES_E_INTERNAL_FAIL_TIMEOUT|internal timeout                |
    """
    RES_S_OK = 1
    RES_E_FAIL = -1
    RES_E_INVALID_PARAMS = -2
    RES_E_NO_MEMORY = -3
    RES_E_NOT_FOUND = -4
    RES_E_INVALID_VERSION = -5
    RES_E_AUTH_FAILED = -6
    RES_E_UNSUPPORTED = -7
    RES_E_AUTO_TRADING_DISABLED = -8
    RES_E_INTERNAL_FAIL = -10000
    RES_E_INTERNAL_FAIL_SEND = -10001
    RES_E_INTERNAL_FAIL_RECEIVE = -10002
    RES_E_INTERNAL_FAIL_INIT = -10003
    RES_E_INTERNAL_FAIL_CONNECT = -10003
    RES_E_INTERNAL_FAIL_TIMEOUT = -10005


def last_error() -> Tuple[ErrorCodes, str]:
    """Return data on the last error.

    last_error() allows obtaining an error code in case of a failed execution of a MetaTrader 5 library function.
    It is similar to GetLastError(). However, it applies its own error codes.
  
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


class AccountInfo:
    @property
    def login() -> int: ...

    @property
    def trade_mode() -> int: ...

    @property
    def leverage() -> int: ...

    @property
    def limit_orders() -> int: ...

    @property
    def margin_so_mode() -> int: ...

    @property
    def trade_allowd() -> bool: ...

    @property
    def trade_expert() -> bool: ...

    @property
    def margin_mode() -> int: ...

    @property
    def currency_digits() -> int: ...

    @property
    def fifo_close() -> bool: ...

    @property
    def balance() -> float: ...

    @property
    def credit() -> float: ...

    @property
    def profit() -> float: ...

    @property
    def equity() -> float: ...

    @property
    def margin() -> float: ...

    @property
    def margin_free() -> float: ...

    @property
    def margin_level() -> float: ...

    @property
    def margin_so_call() -> float: ...

    @property
    def margin_so_so() -> float: ...

    @property
    def margin_initial() -> float: ...

    @property
    def margin_maintenance() -> float: ...

    @property
    def assets() -> float: ...

    @property
    def liabilities() -> float: ...

    @property
    def commission_blocked() -> float: ...

    @property
    def name() -> str: ...

    @property
    def server() -> str: ...

    @property
    def currency() -> str: ...

    @property
    def company() -> str: ...


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


class TerminalInfo():
    @property
    def community_account() -> bool: ...

    @property
    def community_connection() -> bool: ...

    @property
    def connected() -> bool: ...

    @property
    def dlls_allowed() -> bool: ...

    @property
    def trade_allowed() -> bool: ...

    @property
    def tradeapi_disabled() -> bool: ...

    @property
    def email_enabled() -> bool: ...

    @property
    def ftp_enabled() -> bool: ...

    @property
    def notifications_enabled() -> bool: ...

    @property
    def mqid() -> bool: ...

    @property
    def build() -> int: ...

    @property
    def maxbars() -> int: ...

    @property
    def codepage() -> int: ...

    @property
    def ping_last() -> int: ...

    @property
    def community_balance() -> float: ...

    @property
    def retransmission() -> float: ...

    @property
    def company() -> str: ...

    @property
    def name() -> str: ...

    @property
    def language() -> str: ...

    @property
    def path() -> str: ...

    @property
    def data_path() -> str: ...

    @property
    def commondata_path() -> str: ...


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
        The function is similar to SymbolsTotal(). However, it returns the number of all symbols including custom ones and the ones disabled in MarketWatch.
    
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


class SymbolInfo:
    @property
    def custom() -> bool: ...

    @property
    def chart_mode() -> int: ...

    @property
    def select() -> bool: ...

    @property
    def visible() -> bool: ...

    @property
    def session_deals() -> int: ...

    @property
    def session_buy_orders() -> int: ...

    @property
    def session_sell_orders() -> int: ...

    @property
    def volume() -> int: ...

    @property
    def volumehigh() -> int: ...

    @property
    def volumelow() -> int: ...

    @property
    def time() -> int: ...

    @property
    def digits() -> int: ...

    @property
    def spread() -> int: ...

    @property
    def spread_float() -> bool: ...

    @property
    def ticks_bookdepth() -> int: ...

    @property
    def trade_calc_mode() -> int: ...

    @property
    def trade_mode() -> int: ...

    @property
    def start_time() -> int: ...

    @property
    def expiration_time() -> int: ...

    @property
    def trade_stops_level() -> int: ...

    @property
    def trade_freeze_level() -> int: ...

    @property
    def trade_exemode() -> int: ...

    @property
    def swap_mode() -> int: ...

    @property
    def swap_rollover3days(): ...

    @property
    def margin_hedged_use_leg(): ...

    @property
    def expiration_mode(): ...

    @property
    def filling_mode(): ...

    @property
    def order_mode(): ...

    @property
    def order_gtc_mode(): ...

    @property
    def option_mode(): ...

    @property
    def option_right(): ...

    @property
    def bid(): ...

    @property
    def bidhigh(): ...

    @property
    def bidlow(): ...

    @property
    def ask(): ...

    @property
    def askhigh(): ...

    @property
    def asklow(): ...

    @property
    def last(): ...

    @property
    def lasthigh(): ...

    @property
    def lastlow(): ...

    @property
    def volume_real(): ...

    @property
    def volumehigh_real(): ...

    @property
    def volumelow_real(): ...

    @property
    def option_strike(): ...

    @property
    def point(): ...

    @property
    def trade_tick_value(): ...

    @property
    def trade_tick_value_profit(): ...

    @property
    def trade_tick_value_loss(): ...

    @property
    def trade_tick_size(): ...

    @property
    def trade_contract_size(): ...

    @property
    def trade_accrued_interest(): ...

    @property
    def trade_face_value(): ...

    @property
    def trade_liquidity_rate(): ...

    @property
    def volume_min(): ...

    @property
    def volume_max(): ...

    @property
    def volume_step(): ...

    @property
    def volume_limit(): ...

    @property
    def swap_long(): ...

    @property
    def swap_short(): ...

    @property
    def margin_initial(): ...

    @property
    def margin_maintenance(): ...

    @property
    def session_volume(): ...

    @property
    def session_turnover(): ...

    @property
    def session_interest(): ...

    @property
    def session_buy_orders_volume(): ...

    @property
    def session_sell_orders_volume(): ...

    @property
    def session_open(): ...

    @property
    def session_close(): ...

    @property
    def session_aw(): ...

    @property
    def session_price_settlement(): ...

    @property
    def session_price_limit_min(): ...

    @property
    def session_price_limit_max(): ...

    @property
    def margin_hedged(): ...

    @property
    def price_change(): ...

    @property
    def price_volatility(): ...

    @property
    def price_theoretical(): ...

    @property
    def price_greeks_delta(): ...

    @property
    def price_greeks_theta(): ...

    @property
    def price_greeks_gamma(): ...

    @property
    def price_greeks_vega(): ...

    @property
    def price_greeks_rho(): ...

    @property
    def price_greeks_omega(): ...

    @property
    def price_sensitivity(): ...

    @property
    def basis(): ...

    @property
    def category(): ...

    @property
    def currency_base(): ...

    @property
    def currency_profit(): ...

    @property
    def currency_margin(): ...

    @property
    def bank(): ...

    @property
    def description(): ...

    @property
    def exchange(): ...

    @property
    def formula(): ...

    @property
    def isin(): ...

    @property
    def name(): ...

    @property
    def page(): ...

    @property
    def path(): ...


def symbols_get(group: Optional[str] = None) -> Optional[Tuple[SymbolInfo]]:
    """Get all financial instruments from the MetaTrader 5 terminal.

    The group parameter allows sorting out symbols by name. '*' can be used at the beginning and the end of a string.
    The group parameter can be used as a named or an unnamed one. Both options work the same way. The named option (group="GROUP") makes the code easier to read.
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
