#   1. 北京出租车计价器:
#     收费标准：
#       3公里以内收费 13元
#       基本单价 2.3元／公里（超出3公里以外)
#       空驶费: 超过15公里后，每公里加收单价的50%的
#            空驶费(3.45元／公里)
#     要求: 输入公里数，打印出费用金额

km = float(input('请输入公里数:'))
pay = 13

if km > 3:
    pay += 2.3 * (km - 3)

if km > 15:
    pay += 2.3 * .5 * (km - 15)

print("您需要支付:", pay, )