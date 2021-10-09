Teacher
    -id: INT
    -name: STR
    -teacher_photo: STR
    -description: TEXT
    -email: STR
    -phone: STR
    

Course
    -id
    -teacher INT (foreign key [teacher])
    -title: STR
    -number of lessons: INT
    -description: TEXT
    -price: FLOAT
    -start_date: DATE
    -main_pic: STR
    -pic_1: STR
    -pic_2: STR
    -pic_3: STR
    -is_published: BOOLEAN (default==TRUE)



Payment
    -
    -
    -
    -
    -
    -


Contact
    -id: INT
    -user_id: INT
    -course: INT
    -course_id: INT
    -name: STR
    -email: STR
    -phone: STR
    -message: TEXT
    -contact_date: DATE
