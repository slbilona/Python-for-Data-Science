from datetime import datetime


x = datetime.now()
y = (x - datetime(1970, 1, 1)).total_seconds()
z = "%.2E"%y
date = x.strftime('%b %d %Y')
y = f"{y:,.5f}"
print("Seconds since January 1, 1970:", y, "or", z, "in scientific notation")
print(date)
