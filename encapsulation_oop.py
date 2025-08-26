# class Student:
#     def __init__(self, name, marks):
#         self.name = name
#         self._marks = marks
#         self.__subject = "Computer Science"
#
#     def can_submit_fee(self):
#         print(self.__subject)
#         self.__privatrefunctionprint()
#         print("You can submit fee.")
#
#     def __privatrefunctionprint(self):
#         print("This is a private function.")
#
#
#
#
#
# obj = Student("John", 100)
# print(obj.name)
# print(obj._marks)
#
# # obj.can_submit_fee()
# class Student:
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks
#         self._marks=marks
#         self.__subject="chemistry"
#
#     def submit_attendance(self):
#         print("Submit the  attendance")
#         print(self.__subject)
#
#
#
# obj=Student("umar jam",1111)
# print(obj.name)
# print(obj.marks)
# # object.submit_attendance()
#
#
#
# class Student:
#     def __init__(self,name ,marks,rollno,subject):
#      self.name=name
#      self.marks=marks
#      self.rollno=rollno
#      self.subject=subject
#
#
#
# S1=Student("umar jam",550,18,"chemistry")
# print(S1.name)
# print(S1.marks)
# print(S1.rollno)
# print(S1.subject)
# S2=Student("ali haider",559,18,"urdu")
# print(S2.name)
# print(S2.marks)
# print(S2.rollno)



class Student2:
    def __init__(self,name ,marks,rollno,subject):
        self.name=name
        self.__marks=marks
        self.rollno=rollno
        self._subject=subject


obj1=Student2("ali haider",555,18,"chemistry")
print(obj1.name)
print(obj1.__marks)
print(obj1.rollno)
print(obj1._subject)
