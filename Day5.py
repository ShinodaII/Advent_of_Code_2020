file = open("Day5_input.txt",'r')
seats = file.readlines()
seat_nos = [int(seat.replace('B','1').replace('F','0').replace('R','1').replace('L','0'),2) for seat in seats]
max_seat = max(seat_nos)
for seat in range(max_seat):
	if seat - 1 in seat_nos and seat + 1 in seat_nos and seat not in seat_nos:
		print(seat)