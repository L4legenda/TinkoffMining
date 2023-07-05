import ticker
import candel
# import algor.simple_moving_average as simple_moving_average
import algor.moving_average_crossover as moving_average_crossover
import algor.relative_strength_index as relative_strength_index
import algor.bollinger_bands as bollinger_bands
import algor.MACD_alg as MACD_alg
import algor.fibonacci as fibonacci
import test_code as test_code
import algor.ema_crossover as EMA_Crossover
import matplotlib.pyplot as plt
import tikets


delta_days = 30
is_short = True

slice_tikets = ["IRKT" , "ISKJ" , "KAZT" , "KLSB" , "KRKNP" , "LIFE" , "LNZLP" , "MGTSP" , "MOEX" , "MRKC" ,
                "MRKU" , "MRKY" , "MSNG" , "OKEY" , "PIKK" , "PLZL" , "PMSBP" , "RUGR" , "SFIN" , "TGKBP"]
"LNZLP"
# CNTL , DSKY , IRKT , ISKJ , KAZT , KLSB , KRKNP , KZOSP , LIFE , LNZLP , MGTSP , MOEX , MRKC , MRKU , MRKY , MSNG , OKEY , PIKK , PLZL , PMSBP , RUGR , SFIN , TGKBP 
# RUAL 5.19% in 30 days
# MAGN 4.91% in 30 days
# APTK 5.4% in  30 days
# for __ticker in tikets.RUSSIAN_TICKER:
for __ticker in slice_tikets:
    _ticker = __ticker

    figi = ticker.findFigiForTicker(_ticker)
    try:
        candel_last = candel.candel_last(figi, days=delta_days)
    except:
        print("Empty data")

    fiba = fibonacci.test_algorithm(candel_last)

    print(figi)
    print(_ticker, fiba['profit'], fiba['percent_profit'], len(candel_last))
    print("=======")
    # fiba = fibonacci.run(candel_last)
    # print(fiba)
    # fibonacci.plot_data(candel_last, fiba['buy_signals'], fiba['sell_signals'])
    fibonacci.plot_trading_signals(candel_last, fiba['buy_signals'], fiba['sell_signals'])

