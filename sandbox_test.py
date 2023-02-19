from tinkoff.invest import Client, MoneyValue, OrderDirection, OrderType
from tinkoff.invest.services import SandboxService
from config import TOKEN
import pandas as pd
from datetime import datetime

# figi = TCS00A0DQZE3
# ID = ae9fcd5a-e9b0-45ba-9c99-00f2bee918a5


def main():
    with Client(TOKEN, sandbox_token=TOKEN) as cl:

        sb: SandboxService = cl.sandbox

        # sb.open_sandbox_account()
        # sb.sandbox_pay_in(
        #     account_id="ae9fcd5a-e9b0-45ba-9c99-00f2bee918a5",
        #     amount=MoneyValue(units=130_000, nano=0, currency='rub')
        # )

        r = sb.post_sandbox_order(
            figi="TCS00A0DQZE3",
            quantity=1,
            account_id="ae9fcd5a-e9b0-45ba-9c99-00f2bee918a5",
            order_id=datetime.now().strftime("%Y-%m-%dT%H:%M:%S"),
            direction=OrderDirection.ORDER_DIRECTION_BUY,
            order_type=OrderType.ORDER_TYPE_MARKET
        )

        r = sb.get_sandbox_portfolio(
            account_id="ae9fcd5a-e9b0-45ba-9c99-00f2bee918a5")
        p = pd.DataFrame(r.positions)
        print(p)

        # r = sb.get_sandbox_accounts().accounts
        # [print(acc) for acc in r]


if __name__ == '__main__':

    main()
