import csv
import random
with open('Student.csv', 'rb') as csvfile:
	with open('student_course.csv', 'wb') as csvwrite:
		writer = csv.writer(csvwrite, delimiter=',')
		spamreader = csv.reader(csvfile, delimiter=',')
		cslist = [1,2,3,4,5,6]
		mathlist = [3,4,1,2,5,6]
		statlist = [5,6,3,1,4,2]
		acctlist = [7,8,1,3,4,6]
		mislist = [9,10,3,7,8,4,5,6]
		balist = [11,12,9,10,3,5,6]
		finlist = [13,14,11,12,9,10,1,2,3,4,5,6]
		elist = [15,16,1,3,5,9]
		prlist = [17,18,11,12,13,3,4,5,6]
		mclist = [19,20,11,12,13,4,5,6]
		for row in spamreader:
			#print row[0], row[1]
			numofclasses = random.randint(2,6)
			if row[1] == '1':
				#print 'random num', numofclasses
				for i in range(0,numofclasses):
					writer.writerow([row[0], cslist[i]])
					print row[0], cslist[i]
			if row[1] == '2':
				#print 'random num', numofclasses
				for i in range(0,numofclasses):
					writer.writerow([row[0], mathlist[i]])
					print row[0], mathlist[i]

			if row[1] == '3':
				#print 'random num', numofclasses
				for i in range(0,numofclasses):
					writer.writerow([row[0], statlist[i]])
					print row[0], statlist[i]

			if row[1] == '4':
				#print 'random num', numofclasses
				for i in range(0,numofclasses):
					writer.writerow([row[0], acctlist[i]])
					print row[0], acctlist[i]
			if row[1] == '5':
				#print 'random num', numofclasses
				for i in range(0,numofclasses):
					writer.writerow([row[0], mislist[i]])
					print row[0], mislist[i]
			if row[1] == '6':
				#print 'random num', numofclasses
				for i in range(0,numofclasses):
					writer.writerow([row[0], balist[i]])
					print row[0], balist[i]
			if row[1] == '7':
				#print 'random num', numofclasses
				for i in range(0,numofclasses):
					writer.writerow([row[0], finlist[i]])
					print row[0], finlist[i]
			if row[1] == '8':
				#print 'random num', numofclasses
				for i in range(0,numofclasses):
					writer.writerow([row[0], elist[i]])
					print row[0], elist[i]
			if row[1] == '9':
				#print 'random num', numofclasses
				for i in range(0,numofclasses):
					writer.writerow([row[0], prlist[i]])
					print row[0], prlist[i]
			if row[1] == '10':
				#print 'random num', numofclasses
				for i in range(0,numofclasses):
					writer.writerow([row[0], mclist[i]])
					print row[0], mclist[i]
