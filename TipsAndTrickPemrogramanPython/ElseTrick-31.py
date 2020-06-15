speed = [60,40,30,20,10,100,300]
ambang = 100
for laju in speed:
	if laju > ambang:
		laju_normal = False
		print("exceed")
		break
else:
	print("normally")