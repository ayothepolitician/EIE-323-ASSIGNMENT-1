def cgpaCal():
    totScore = 0
    Gradegot = 0
    coursesNo = int(input("Enter total number of courses offered: "))
    print ("============================")
    for x in range(coursesNo):
        Course1 = input("Enter your course code :")
        unit = int(input("Enter Course Unit : "))
        score = input ("please enter your grade (A,B,C,D,F) : ")
        print ("==========================")
        totScore += unit*5
        '''grade range (A = 5 points ,B= 4 points , C = 3 points, D= 2 points , F= 0 points )'''
        if (score == 'A'):
            grade = 5
        elif (score == 'a'):
            grade = 5
        elif (score == 'B'):
            grade = 4
        elif (score == 'b'):
            grade = 4
        elif (score == 'C'):
            grade = 3
        elif (score == 'c'):
            grade = 3
        elif (score == 'D'):
            grade = 2
        elif (score == 'd'):
            grade = 2
        elif (score == 'F'):
            grade = 0
        elif (score == 'f'):
            grade = 0
        else:
            print(" You put a wrong grade value here!!!, therefore your cgpa value would be wrong. I'll advise you to restart ")
        Gradegot += unit*grade
    Cgpa = float((Gradegot/ totScore) * 5)
    print("YOUR CGPA IS : " + str(round(Cgpa,2)))
cgpaCal()
