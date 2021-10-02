import MetaTrader5 as mt5

mt5.initialize()
print(mt5.symbols_get()[0])
mt5.shutdown()
