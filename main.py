import ticker
import candel
import algor.simple_moving_average as simple_moving_average

GCHE = ticker.findOneTicker("GCHE")
figi = GCHE['figi'].values[0]
candel_1mouth = candel.candel_last(figi, days=30)
# print(candel_7day)
simple_moving_average.run(candel_1mouth, graphic=True)


