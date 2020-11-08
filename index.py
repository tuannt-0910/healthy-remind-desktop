# try:
# 	import notify2 # pip3 install notify2
# 	import getpass # get system name
# 	import os
# 	import schedule	# pip3 install schedule
# 	import time
# except ImportError as ex:
# 	print(ex)
#     print("Import failed")
#     import sys
#     sys.exit(1)

import notify2 # pip3 install notify2
# import getpass # get system name
# import os
import schedule	# pip3 install schedule
import time

notify2.init('TAWK')

# PWD = os.getcwd()
# USER_NAME = getpass.getuser()
# HELLO_NAME = 'Chào bạn ' + USER_NAME + ', '
MESSAGE_WATER_NOTIFY = 'uống nước bạn tớ ơi! ^^'
MESSAGE_EXERCISE_NOTIFY = 'vận động nào bạn ơi! ^^'
MESSAGE_GOOD_MORNING = 'chào bủi sáng nha. Chúc bạn có ngày mới vui vẻ! ^^'
MESSAGE_GOOD_AFTERNOON = 'buổi chiều rồi, mong bạn tiếp tục hoàn thành công việc đã định! ^^'
MESSAGE_GOOD_EVENING = 'buổi tối rồi, try hard và thư giãn nào! ^^'

# minutes
WATER_SCHEDULE_TIME = 120
EXERCISE_SCHEDULE_TIME = 120

def start():
	current_time = time.localtime()
	if current_time[3] < 12:
		send_noti('Morning!!!', MESSAGE_GOOD_MORNING)
	elif current_time[3] in range(12, 18):
		send_noti('Afternoon!!!', MESSAGE_GOOD_AFTERNOON)
	else:
		send_noti('Evening!!!', MESSAGE_GOOD_EVENING)

def water_notification():
	send_noti('Water!!!', MESSAGE_WATER_NOTIFY)

def exercise_notification():
	send_noti('Do exercise!!!', MESSAGE_EXERCISE_NOTIFY)

def send_noti(title, content):
	n = notify2.Notification(title, content).show()
	# n.set_urgency(notify2.URGENCY_NORMAL)
	# n.set_timeout(100)
	# n.show()

if __name__=="__main__":
	start()
	schedule.every(WATER_SCHEDULE_TIME).minutes.do(water_notification)
	schedule.every(EXERCISE_SCHEDULE_TIME).minutes.do(exercise_notification)

	while True:
		schedule.run_pending()
		time.sleep(1)