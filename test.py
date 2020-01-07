import datetime
import workdays
start_date = datetime.datetime(2020, 1, 1)
end_date = datetime.datetime(2020,1,31)

wd = workdays.networkdays(start_date, end_date)
work_time = int(wd) * 7.5
ov_time = int(input("想定する残業時間を入力してください: "))
total_time = work_time + ov_time
print("総稼働時間: " + str(total_time) + "H(内残業" + str(ov_time) + "H)" )
