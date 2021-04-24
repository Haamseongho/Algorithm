shop_menus = ["만두", "떡볶이", "오뎅", "사이다", "콜라"]
shop_orders = ["오뎅", "콜라", "만두"]


def is_available_to_order(menus, orders):
    # 이 부분을 채워보세요!
    menus.sort()
    orders.sort()

    count = 0
    for order in orders:
        start_index = 0
        end_index = len(menus) - 1
        index = (start_index + end_index) // 2
        while start_index <= end_index:

            if menus[index] == order:
                count += 1
                break

            if menus[index] < order:
                # 메뉴판에 있는 음식들보다 내가 주문하려는 메뉴가 뒤에 있는 경우
                start_index = index + 1
            elif menus[index] > order:
                # 메뉴판의 메뉴들보다 내가 찾는 음식이 앞에 있는 경우
                end_index = index - 1

            index = (start_index + end_index) // 2

    if count == len(orders):
        return True
    else:
        return False


result = is_available_to_order(shop_menus, shop_orders)
print(result)
