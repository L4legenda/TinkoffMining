import ticker
import candel
from config import CURRENT_TICKER
import telegram_bot
from algor.fibonacci import get_signal
import time
from datetime import datetime


def main():
    figi = ticker.findFigiForTicker(CURRENT_TICKER)

    delta_days = 1
    is_short = True
    window_size = 20

    levels = [0.236, 0.382, 0.5, 0.618, 0.786]

    position = 0

    profit = 0
    investment = 0

    while True:
        str_now = datetime.strftime(datetime.now(), '%Y-%m-%d | %H:%M:%S')
        message_bot = f"== {str_now} ==\n"

        candel_last = candel.candel_last(figi, days=delta_days)

        data = candel_last.iloc[-window_size:]

        signal = get_signal(
            data,
            position=position,
            levels=levels,
            is_short=is_short
        )

        if signal == 'buy':
            message_bot += f"Signal: BUY\n"

            position += 1
            investment += data['close'].iloc(-1) * 1.0004  # Include commission
            profit -= data['close'].iloc(-1) * 1.0004

        elif signal == 'sell':
            message_bot += f"Signal: SELL\n"
            position -= 1
            profit += data['close'].iloc(-1)

        if signal:
            # Calculate percent profit
            if investment != 0:
                percent_profit = round(profit / investment * 100, 2)
            else:
                percent_profit = 0

            print("Total profit:", profit)
            print("Percent profit:", percent_profit)

            message_bot += f"Total profit: {profit}\n"
            message_bot += f"Percent profit: {percent_profit}\n"

            telegram_bot.send_message(message_bot)


        print("SLEEP 5 MIN")
        time.sleep(5 * 60)


if __name__ == "__main__":
    main()
