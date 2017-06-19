for i in range(1, 10):
	count_zero_remainder = 0
	for j in range(1, i+1):
		print i,j
		print "---"
		num_remainder = i % j
		
		print "sisa: ",num_remainder
		if num_remainder == 0:
			count_zero_remainder = count_zero_remainder + 1
	
		print "czr: ",count_zero_remainder
	
	if count_zero_remainder == 2:
		print i, " adalah bilangan prima\n"
	else:
		print i, " bukanlah bilangan prima\n"