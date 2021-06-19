
def factor_powers(n):
    powers = {}
    while n > 1:
        for i in range(2, n + 1):
            if n % i == 0:
                n //= i
                if i in powers:
                    powers[i] += 1
                else:
                    powers[i] = 1
                break
    return powers


def kas_on_kokkuhoidlik(n):
    number_count = 0
    powers = factor_powers(n)
    for factor, power in powers.items():
        number_count += len(str(factor))
        if power > 1:
            number_count += len(str(power))
    original_count = len(str(n))
    if number_count < original_count:
        return "Kokkuhoidlik"
    elif number_count == original_count:
        return "Samanumbriline"
    else:
        return "Raiskav"


for num in (14, 125, 1024, 30):
    print(num, ":", kas_on_kokkuhoidlik(num))

