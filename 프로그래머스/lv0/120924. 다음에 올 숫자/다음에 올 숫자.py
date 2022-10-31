def solution(common):
	# 등차인지 chk
	if common[1] - common[0] == common[2] - common[1]:
		r = common[1] - common[0]
		return common[-1] + r
	elif common[1] // common[0] == common[2] // common[1]:
		r = common[1] // common[0]
		return common[-1] * r