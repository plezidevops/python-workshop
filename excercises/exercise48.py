def convert_ust_to_aud(amount, rate=0.75) :
    return amount / rate

def convert_and_sum_list(usd_list, rate=0.75):
    total = 0
    for amount in usd_list:
        total += convert_ust_to_aud(amount, rate=rate)
    return total

print(convert_and_sum_list([1, 3]))