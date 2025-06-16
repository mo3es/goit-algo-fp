def greedy(items: dict, cash: int) -> dict:
    products_weight = []

    for product_name, values in items.items():
        cost = values["cost"]
        calories = values["calories"]
        weight = calories / cost
            
        products_weight.append({"name": product_name, "cost": cost, "calories": calories, "weight": weight})

    products_weight.sort(key=lambda x: x["weight"], reverse=True)

    #print(products_weight) #Виводить список продуктів зі значеннями питомої ваги (якщо розкоментувати); найбільша питома вага у коли

    products_list = {}
    current_amount = cash

    for item in products_weight:
        item_name = item["name"]
        item_cost = item["cost"]
        
        if item_cost > current_amount:
            continue
            
        quantity = current_amount // item_cost
        
        if quantity > 0:
            products_list[item_name] = products_list.get(item_name, 0) + quantity
            current_amount -= quantity * item_cost
            
            if current_amount <= 0:
                break
                
    return products_list



def dynamic(items: dict, cash: int) -> dict:

    dp_max_calories = [0] * (cash + 1)

    products = [None] * (cash + 1) 

    product_list_data = []
    for product_name, values in items.items():
        product_list_data.append({
            "name": product_name,
            "cost": values["cost"],
            "calories": values["calories"]
        })

    for i in range(1, cash + 1): 
        dp_max_calories[i] = dp_max_calories[i-1] if i > 0 else 0 
        products[i] = products[i-1] if i > 0 else None

        for product_data in product_list_data:
            product_name = product_data["name"]
            cost = product_data["cost"]
            calories = product_data["calories"]

            if i >= cost:
                
                if dp_max_calories[i - cost] + calories > dp_max_calories[i]:
                    dp_max_calories[i] = dp_max_calories[i - cost] + calories
                    products[i] = product_name
    
    best_cash = 0
    max_calories = 0
    for i in range(cash + 1):
        if dp_max_calories[i] > max_calories:
            max_calories = dp_max_calories[i]
            best_cash = i

    result = {}
    current_cash = best_cash
    
    if max_calories > 0:

        while current_cash > 0:
            chosen_product = products[current_cash]

            if chosen_product is None:
                break
            
            result[chosen_product] = result.get(chosen_product, 0) + 1
            current_cash -= items[chosen_product]['cost']

    return result



if __name__ == '__main__':
    cash_amount = 1200
    items = {
        "pizza": {"cost": 50, "calories": 300},
        "hamburger": {"cost": 40, "calories": 250},
        "hot-dog": {"cost": 30, "calories": 200},
        "pepsi": {"cost": 10, "calories": 100},
        "cola": {"cost": 15, "calories": 220},
        "potato": {"cost": 25, "calories": 350}
    }
    
    list_greedy = greedy(items, cash_amount)
    print(f'Набір продуктів на суму {cash_amount}: {list_greedy}, розрахований жадібним алгоритмом.')


    list_dynamic = dynamic(items, cash_amount)
    print(f'\n\nНабір продуктів на суму {cash_amount}: {list_dynamic}, розрахований динамічним способом.')