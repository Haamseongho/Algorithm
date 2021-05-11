shop_prices = [30000, 2000, 1500000]
user_coupons = [20, 40]


def get_max_discounted_price(prices, coupons):
    # 이 곳을 채워보세요!
    max_discounted_price_list = {}
    prices.sort()
    coupons.sort()

    inx = 0
    ans: int = 0
    while coupons and prices:
        price = prices.pop()
        coupon = coupons.pop()
        ans = int(((100 - coupon) / 100) * price) + ans

    if prices:
        while prices:
            price = prices.pop()
            ans = ans + price

    return ans


print(get_max_discounted_price(shop_prices, user_coupons))  # 926000 이 나와야 합니다.
