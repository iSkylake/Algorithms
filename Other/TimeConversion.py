from nose.tools import assert_equal

def time_Con(time):
	if time[8:] == "PM":
		if time[:2] == "12":
			return time[:8]
		else:
			hour = int(time[:2]) + 12
			return str(hour) + time[2:8]
	else:
		if time[:2] == "12":
			return "00" + time[2:8]
		else:
			return time[:8]

class Time_Con(object):
	def test(self, func):
		assert_equal(func("12:00:00AM"), "00:00:00")
		assert_equal(func("01:50:00AM"), "01:50:00")
		assert_equal(func("06:25:10AM"), "06:25:10")
		assert_equal(func("12:00:00PM"), "12:00:00")
		assert_equal(func("02:00:00PM"), "14:00:00")
		assert_equal(func("07:59:00PM"), "19:59:00")
		assert_equal(func("11:33:59PM"), "23:33:59")
		print("TESTS PASSED")

t = Time_Con()
t.test(time_Con)