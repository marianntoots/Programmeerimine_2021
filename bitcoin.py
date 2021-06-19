from datetime import datetime, timedelta
import json
from urllib.request import urlopen

today_str = datetime.today().strftime("%Y-%m-%d")
api_url = "https://api.coindesk.com/v1/bpi/historical/close.json?start=2010-07-17&end=" + today_str

with urlopen(api_url) as f:
    price_data = json.load(f)["bpi"]

highest_date, highest_price = max(price_data.items(), key=lambda it: it[1])
print("Tänane kõrgeim BitCoini hind: {} ({} USD1)".format(highest_date, highest_price))

zipped_items = list(zip(price_data.items(), list(price_data.items())[1:]))
diffkey = lambda item: item[1][1] - item[0][1]
biggest_surge = max(zipped_items, key=diffkey)
biggest_fall = min(zipped_items, key=diffkey)
print("Kõige suurema BitCoini tõusuga päev: {} (+{:.4f} USD)".format(
    biggest_surge[1][0],
    diffkey(biggest_surge)
))
print("Kõige suurema BitCoini langusega päev: {} ({:.4f} USD)".format(
    biggest_fall[1][0],
    diffkey(biggest_fall),
))

longest_surge_period_start = None
longest_surge_period_days = 0
longest_surge_period_end = None
longest_fall_period_start = None
longest_fall_period_days = 0
longest_fall_period_end = None
current_surge_period_start = list(price_data.keys())[0]
current_surge_period_days = 0
current_fall_period_start = list(price_data.keys())[0]
current_fall_period_days = 0

for (prev_date, prev_price), (date, price) in zipped_items:
    if price > prev_price:
        current_surge_period_days += 1
    if current_surge_period_days > longest_surge_period_days:
        longest_surge_period_start = current_surge_period_start
        longest_surge_period_days = current_surge_period_days
        longest_surge_period_end = date
    if price <= prev_price:
        current_surge_period_start = date
        current_surge_period_days = 1

    if price < prev_price:
        current_fall_period_days += 1
    if current_fall_period_days > longest_fall_period_days:
        longest_fall_period_start = current_fall_period_start
        longest_fall_period_days = current_fall_period_days
        longest_fall_period_end = date
    if price >= prev_price:
        current_fall_period_start = date
        current_fall_period_days = 1

print("Pikim periood, mille jooksul Bitcoini hind...")
print("  ... tõusis: {} kuni {} ({} päeva)".format(
    longest_surge_period_start, longest_surge_period_end, longest_surge_period_days
))
print("  ... langes: {} kuni {} ({} päeva)".format(
    longest_fall_period_start, longest_fall_period_end, longest_fall_period_days
))

date_format = "%Y-%m-%d"
start_date = datetime.strptime(list(price_data.keys())[0], date_format)
end_date = datetime.strptime(list(price_data.keys())[-1], date_format)

cur_date = datetime(start_date.year, start_date.month, 1)

best_month = None
best_month_surge = None
worst_month = None
worst_month_fall = None

while cur_date < end_date:
    next_year = cur_date.year
    next_month = cur_date.month + 1
    if next_month > 12:
        next_year += 1
        next_month = 1
    next_date = datetime(next_year, next_month, 1)
    if cur_date >= start_date:
        last_day_of_month = next_date - timedelta(days=1)
        last_day_of_month_str = last_day_of_month.strftime(date_format)
        if last_day_of_month_str not in price_data:
            break
        cur_diff = price_data[last_day_of_month_str] - \
                   price_data[cur_date.strftime(date_format)]
        if best_month_surge is None or cur_diff > best_month_surge:
            best_month = cur_date.strftime("%Y-%m")
            best_month_surge = cur_diff
        if worst_month_fall is None or cur_diff < worst_month_fall:
            worst_month = cur_date.strftime("%Y-%m")
            worst_month_fall = cur_diff
    cur_date = next_date

print("Parim kuu Bitcoini ajaloos: {} (tõus: +{:.4f} USD)".format(
    best_month,
    best_month_surge
))
print("Halvim kuu Bitcoini ajaloos: {} (langus: {:.4f} USD)".format(
    worst_month,
    worst_month_fall
))

best_week = None
best_week_surge = None
worst_week = None
worst_week_fall = None

cur_date = start_date
cur_date += timedelta(days=(7 - cur_date.weekday()) % 7)

while cur_date < end_date:
    next_date = cur_date + timedelta(weeks=1)
    last_day_of_week = next_date - timedelta(days=1)
    last_day_of_week_str = last_day_of_week.strftime(date_format)
    if last_day_of_week_str not in price_data:
        break
    cur_diff = price_data[last_day_of_week_str] - \
                   price_data[cur_date.strftime(date_format)]
    if best_week_surge is None or cur_diff > best_week_surge:
        best_week = cur_date
        best_week_surge = cur_diff
    if worst_week_fall is None or cur_diff < worst_week_fall:
        worst_week = cur_date
        worst_week_fall = cur_diff
    cur_date = next_date

print("Parim nädal Bitcoini ajaloos: {} kuni {} (tõus: +{:.4f} USD)".format(
    best_week.strftime(date_format),
    (best_week + timedelta(days=6)).strftime(date_format),
    best_week_surge,
    best_week_surge,
))
print("Halvim nädal Bitcoini ajaloos: {} kuni {} (langus: {:.4f} USD)".format(
    worst_week,
    (worst_week + timedelta(days=6)).strftime(date_format),
    worst_week_fall,
))
