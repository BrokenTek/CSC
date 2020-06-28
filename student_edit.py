def list_courses(id, c_list, r_list):

    # ------------------------------------------------------------
    # This function displays and counts courses a student has
    # registered for.  It has three parameters: id is the ID of the
    # student; c_list is the course list; r_list is the list of
    # class rosters. This function has no return value.
    # -------------------------------------------------------------

    #pass # temporarily avoid empty function definition
    print("Courses registered:")
    for i in range(3):
        if id in r_list[i]:
            print(c_list[i])    
    total = 0
    for i in range(3):
        for p in r_list[i]:
            if id == p:
                total+=1
    print("Total classes:", total)
            


def add_course(id, c_list, r_list, m_list):

    # ------------------------------------------------------------
    # This function adds a student to a course.  It has four
    # parameters: id is the ID of the student to be added; c_list
    # is the course list; r_list is the list of class rosters;
    # m_list is the list of maximum class sizes.  This function
    # asks user to enter the course he/she wants to add.  If the
    # course is not offered, display error message and stop.
    # If the course is full, display error message and stop.
    # If student has already registered for this course, display
    # error message and stop.  Add student ID to the course’s
    # roster and display a message if there is no problem.  This
    # function has no return value.
    # -------------------------------------------------------------

    #pass # temporarily avoid empty function definition
    course_add = input("Enter course you want to add (IS CASE SENSITIVE): ")
    if course_add in c_list:
        ind = c_list.index(course_add)
        t = int(m_list[ind])
        if id not in r_list[ind] and len(r_list[ind]) < t:
            r_list[ind].append(id)
            print("Successfully added course")
        elif id in r_list[ind]:
            print("Error: Already enrolled")
        elif len(r_list[ind]) >= m_list[ind]:
            print("No available seats, already full session")             
    else:
        print("Course not found")    


def drop_course(id, c_list, r_list):

    # ------------------------------------------------------------
    # This function drops a student from a course.  It has three
    # parameters: id is the ID of the student to be dropped;
    # c_list is the course list; r_list is the list of class
    # rosters. This function asks user to enter the course he/she
    # wants to drop.  If the course is not offered, display error
    # message and stop.  If the student is not enrolled in that
    # course, display error message and stop. Remove student ID
    # from the course’s roster and display a message if there is
    # no problem.  This function has no return value.
    # -------------------------------------------------------------

    #pass # temporarily avoid empty function definition
    course_drop = input("Enter course you want to drop (IS CASE SENSITIVE): ")
    if course_drop in c_list:
        ind = c_list.index(course_drop)
        if id in r_list[ind]:
            r_list[ind].remove(id)
            print("Successfully removed course!")
        elif id not in r_list[ind]:
            print("Course not enrolled")         
    else:
        print("Course not found")    