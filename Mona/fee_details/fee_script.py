from db_ops import *


class FeeScript():
    def __init__(self):
        self.db_obj = DbOperations()

    def match_hall_ticket(self, hall_ticket_number):
        try:
            data = self.db_obj.get_student_details(hall_ticket_number)
            if data:
                return data[0]
            else:
                return False
        except Exception as e:
            return None

    def enter_details(self):
        while True:
            # hall_ticket_number = input("Enter hall ticket number :")
            hall_ticket_number = 'C01'
            student_details = self.match_hall_ticket(hall_ticket_number)
            if not student_details:
                print("Hall ticket details matched try again")
                continue
            print("Fetching fee details...")
            total_fee_for_semester_obj = self.db_obj.get_fee_details_for_semester(year=student_details[4], semester=student_details[5],
                                                                              course=student_details[3], department=student_details[2])
            if not total_fee_for_semester_obj:
                print("Fee details not found for course, please check db table")
            total_fee_for_semester = total_fee_for_semester_obj[0][0]
            print("Total Fee for current semester :{0}".format(total_fee_for_semester))

            fee_paid_obj = self.db_obj.get_fee_paid_for_semester(hall_ticket=hall_ticket_number,year=student_details[4],
                                semester=student_details[5], course=student_details[3], department=student_details[2])
            balance = total_fee_for_semester
            if not fee_paid_obj:
                print("Fee paid is zero, balance is {0}".format(total_fee_for_semester))
            else:
                for each_row in fee_paid_obj:
                    print("Paid {0} on {1}".format(each_row[0], each_row[1]))
                    balance-=each_row[0]

            print("Balance :{0}".format(balance))
            if balance < 0:
                print("No fee balance, Thank you")
                break
            pay_balance = input("Do you want to pay balance? y/n :")
            if pay_balance.lower() == 'n':
                print("Exiting")
            elif pay_balance.lower() == 'y':
                amount = input("Enter amount to be paid :")
                if int(amount) > balance:
                    print("Entered amount is greater than balance, please retry")
                    break
                else:
                    #insert into database
                    self.db_obj.insert_into_payment_history(hall_ticket=hall_ticket_number, year=student_details[4], semester=student_details[5],
                                                            course=student_details[3], department=student_details[2], fee=amount, name=student_details[1])
                    balance-=int(amount)

            print("Balance amount :{0}".format(balance))


            break



if __name__ == "__main__":
    obj = FeeScript()
    # data = obj.match_hall_ticket('C01')
    # print(data)
    obj.enter_details()
