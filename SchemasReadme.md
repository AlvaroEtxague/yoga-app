- Teacher
    - id: IntegerField
    - name: CharField
    - teacher_photo: ImageField
    - description: TextField
    - email: CharField
    - phone: CharField
    

- Course
    - id: IntegerField
    - teacher: ForeignKey [teacher]
    - title: CharField
    - lessons: IntegerField
    - description: TextField
    - price: DecimalField
    - start_date: DateField
    - main_pic: ImageField
    - pic_1: ImageField
    - pic_2: ImageField
    - pic_3: ImageField
    - is_published: BOOLEAN (default==TRUE)
    - students: ManyToManyField[User]


- Contact
    - id: IntegerField
    - user_id: IntegerField
    - course: CharField
    - course_id: IntegerField
    - name: CharField
    - email: CharField
    - phone: CharField
    - message: TextField
    - contact_date: DateTimeField


- Accounts Model:
    - id: IntegerField
    - user: ForeignKey [User]
    - course: ForeignKey [Course]
    - txn_id: CharField
    - currency: CharField
    - amount: IntegerField
    - stripe_customer: CharField
    - is_paid: BooleanField
    - created_at: DateTimeField
    - updated_at: DateTimeField