from datetime import datetime

date1 = "Wednesday, October 2, 2002"
date2 = "Friday, 11.10.13"
date3 = "Thursday, 18 August 1977"

datetime1 = datetime.strptime(date1, "%A, %B %d, %Y")
datetime2 = datetime.strptime(date2, "%A, %d.%m.%y")
datetime3 = datetime.strptime(date3, "%A, %d %B %Y")

print(datetime1)
print(datetime2)
print(datetime3)