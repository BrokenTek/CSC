# ----------------------------------------------------------------
# Author:
# Date:
#
# This program creates a class registration system.  It allows
# students to add courses, drop courses and list courses they are
# registered for.
# -----------------------------------------------------------------

import student_edit


def main():

    # ------------------------------------------------------------
    # This function manages the whole registration system.  It has
    # no parameter.  It creates student list, course list,
    # max class size list and roster list.  It uses a loop to serve
    # multiple students. Inside the loop, ask student to enter ID,
    # and call the login function to verify student's identity. Then
    # let student choose to add course, drop course or list courses.
    # This function has no return value.
    # -------------------------------------------------------------

    student_list = [('1001', '111'), ('1002', '222'), ('1003', '333'), ('1004', '444')]
    course_list = ['CSC101', 'CSC102', 'CSC103']
    roster_list = [['1004', '1003'], ['1001'], ['1002']]
    max_size_list = [3, 2, 1]

    login_s = input("Enter ID to log in, or 0 to quit: ")
    if login_s == '0':
    	print("Thank you for using our software!")
    else:
    	log = login(login_s,student_list)
    	if log:
    		choice = int(input("Enter 1 to add course, 2 to drop course, 3 to list courses, 0 to exit: "))
    		while choice != 0:
    			if choice == 1:
    				student_edit.add_course(login_s, course_list, roster_list, max_size_list)
    				choice = int(input("Enter 1 to add course, 2 to drop course, 3 to list courses, 0 to exit: "))
    			elif choice == 2:
    				student_edit.drop_course(login_s, course_list, roster_list)
    				choice = int(input("Enter 1 to add course, 2 to drop course, 3 to list courses, 0 to exit: "))
    			elif choice == 3:
    				student_edit.list_courses(login_s, course_list, roster_list)
    				choice = int(input("Enter 1 to add course, 2 to drop course, 3 to list courses, 0 to exit: "))
    			elif choice == 0:
    				print("Session ended")
		
    			

    		


def login(id, s_list):

    # ------------------------------------------------------------
    # This function allows a student to log in.
    # It has two parameters: id and s_list, which is the student
    # list. This function asks user to enter PIN. If the ID and PIN
    # combination is in s_list, display message of verification and
    # return True. Otherwise, display error message and return False.
    # -------------------------------------------------------------

    #pass # temporarily avoid empty function definition
    student_pin = input("Enter your PIN for your student account: ")
    t = (id,student_pin)
    if t in s_list:
    	print("ID and PIN verified")
    	return True
    else:
    	print("ID or PIN incorrect")
    	return False

    		

main()
