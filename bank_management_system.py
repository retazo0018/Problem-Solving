import cx_Oracle
class New_customer():
    def set_first_name(self ,fname):
        self.first_name = fname

    def set_last_name(self ,lname):
        self.last_name = lname

    def set_customer_id(self ,id):
        self.customer_id = id
        
    def set_address(self ,addr):
        self.addr = addr

    def set_PIN(self, pin):
        self.PIN = pin

    def get_first_name(self):
        return self.first_name

    def get_last_name(self):
        return self.last_name

    def get_customer_id(self):
        return self.customer_id

    def get_addr_line1(self):
        return self.addr.line1

    def get_addr_line2(self):
        return self.addr.line2

    def get_addr_city(self):
        return self.addr.city

    def get_addr_state(self):
        return self.addr.state

    def get_addr_pincode(self):
        return self.addr.pincode

    def disp_info(self):
        print(self.first_name)
        print(self.last_name)
        print(self.customer_id)

        
class Address():
    def set_line_1(self, a1):
        self.line1 = a1

    def set_line_2(self, a2):
        self.line2 = a2

    def set_city(self, ci):
        self.city = ci

    def set_state(self, st):
        self.state = st

    def set_pincode(self, pc):
        self.pincode = pc

class Loan():

    def set_loan_no(self,no):
        self.loan_no=no
    
    def set_amount(self ,amt):
        self.amount = amt
    def set_loan_type(self,type):
        self.type=type
    def get_loan_no(self):
        return(self.loan_no)

    def get_amount(self ):
        return(self.amount)
    
    def get_account_type(self):
        return self.type
    
class Account():
        
    min_balance = 5000
    def set_no_of_terms(self ,terms):
        self.no_of_terms = terms
    def set_account_no(self ,acc_no):
        self.account_no = acc_no

    def set_account_type(self ,type):
        self.type = type

    def set_balance(self ,bal):
        self.balance = bal

    def get_no_of_terms(self):
        return self.no_of_terms
    def get_account_no(self):
        return self.account_no
    
    def get_balance(self):
        return self.balance

    def get_account_type(self):
        return self.type

class FD(Account):
    
    def open_account(self ,amount):
        if amount < 0:
            print("Please input a valid amount")
            return False
        else:
            self.balance = amount
            return True
        
    def deposit(self ,amount):
        if amount < 0:
            print("Please input a valid amount");
            return False
        else:
            self.balance += amount;
            return True

    def withdraw(self ,amount):
        print("Not Applicable")
        return False
    
    def close(self):
        self.balance = 0;
        return True

class Savings(Account):

    def open_account(self ,amount):
        if amount < 0:
            print("Please input a valid amount")
            return False
        else:
            self.balance = amount
            return True

    def deposit(self ,amount):
        if amount < 0:
            print("Please input a valid amount");
            return False
        else:
            self.balance += amount;
            return True


    def withdraw(self ,amount):
        if amount > self.balance:
            print("Sorry You don't have enough balance");
            return False
        else:
            self.balance -= amount;
            return True

class Current(Account):

    def open_account(self ,amount):
        if amount < self.min_balance:
            print("Please input a valid amount")
            return False
        else:
            self.balance = amount
            return True

    def deposit(self ,amount):
        if amount < 0:
            print("Please input a valid amount");
            return False
        else:
            self.balance += amount;
            return True


    def withdraw(self ,amount):
        if amount > self.balance:
            print("Sorry You don't have enough balance");
            return False
        elif self.balance - amount < self.min_balance:
            print("Sorry You can't withdraw this much money as you need at least Rs" ,self.min_balance
                  ," to maintain this account")
            return False
        else:
            self.balance -= amount;
            return True

class database:
    def create_all_tables():
        con = cx_Oracle.connect('scott/tiger@oracle')
        cur = con.cursor()
        sql = "select count(*) from user_tables where table_name = 'CUSTOMERS'"
        cur.execute(sql)
        res = cur.fetchall()
        if res[0][0] != 0:
            return
        sql = """create table customers(
                  customer_id number(15) primary key,
                  first_name varchar2(30),
                  last_name varchar2(30), pin number(4))"""
        cur.execute(sql)
       
        sql = """create table address(
                  customer_id number(15),
                  line1 varchar2(30),
                  line2 varchar2(30),
                  city varchar2(30),
                  state varchar2(30),
                  pincode number(6),
                  constraint fk_addr foreign key(customer_id) references customers(customer_id))"""
        cur.execute(sql)
        
        sql = """create table accounts(
                  customer_id number(5),
                  account_no number(5) primary key,
                  account_type varchar2(20),
                  balance number(8),
                  constraint fk_acc foreign key(customer_id) references customers(customer_id))"""
        cur.execute(sql)
        sql = """create table transactions(
                  transaction_id number(5) primary key,
                  account_no number(5),
                  type varchar2(15),
                  amount number(8),
                  balance number(8),
                  constraint fk_transaction_account_no foreign key(account_no) references accounts(account_no))"""
        cur.execute(sql)
        sql = """create table loans(
                  customer_id number(5), 
                  loan_no number(5) primary key,
                  type varchar2(15),
                  amount number(10),
                  constraint fk_loan_no foreign key(customer_id) references customers(customer_id))"""
        
        cur.execute(sql)
        sql = """create sequence customer_id_sequence
            start with 1
            increment by 1
            nocycle"""
        cur.execute(sql)

        sql = """create sequence account_no_sequence
            start with 1
            increment by 1
            nocycle"""
        cur.execute(sql)

        sql = """create sequence transaction_id_sequence
            start with 1
            increment by 1
            nocycle"""
        cur.execute(sql)
        sql = """create sequence loan_no_sequence
            start with 1
            increment by 1
            nocycle"""
        cur.execute(sql)
        con.commit()
        con.close()
    def get_new_loan(id):
        loan=Loan()
        con = cx_Oracle.connect('scott/tiger@oracle')
        cur = con.cursor()
        amt=int(input("Enter the Loan amount\n"))
        type=input("Enter the type of the Loan\n")
        sql=None
        sql="select loan_no_sequence.nextval from dual"
        cur.execute(sql)
        res = cur.fetchall()
        loan_no = res[0][0]
        loan.set_loan_no(loan_no)
        loan.set_amount(amt)
        loan.set_loan_type(type)
        sql = "insert into loans values(:id,:ln_no,:type,:amount)"
        cur.execute(sql, {"id" :id, "ln_no" :loan_no, "type" :type, "amount" :amt})
        con.commit()
        print("Congratulations ! Your Loan was Ganted Successfully")
        print("Your Loan no is : " ,loan_no)
        con.close()
    def get_new_account(ch,id):
        account=Account()
        con = cx_Oracle.connect('scott/tiger@oracle')
        cur = con.cursor()
        bal=int(input("Enter the Balance\n"))
        term=0
        sql = "select account_no_sequence.nextval from dual"
        cur.execute(sql)
        res = cur.fetchall()
        ac_no = res[0][0]
        account.set_account_no(ac_no)
        account.set_balance(bal)
        if ch==1:
            type1="savings"
        elif ch==2:
            type1="current"
        elif ch==3:
            type1="fp"
            term=int(input("enter the no of terms of deposit\n"))
        account.set_account_type(type1)
        account.set_no_of_terms(term)
        sql = "insert into accounts values(:id,:ac_no,:type1,:bal)"
        cur.execute(sql, {"id" :id, "ac_no" :ac_no, "type1" :type1, "bal" :bal})
        con.commit()
        print("Congratulations ! Your Account was Created Successfully")
        print("Your Account no is : " ,ac_no)
        con.close()

    def sign_up_customer(customer):
        con = cx_Oracle.connect('scott/tiger@oracle')
        cur = con.cursor()
        fname = customer.get_first_name()
        lname = customer.get_last_name()
        pin = customer.PIN
        sql = "select customer_id_sequence.nextval from dual"
        cur.execute(sql)
        res = cur.fetchall()
        id = res[0][0]
        sql = "insert into customers values(:id,:fname,:lname,:pin)"
        cur.execute(sql, {"id" :id, "fname" :fname, "lname" :lname, "pin" :pin})
        line1 = customer.get_addr_line1()
        line2 = customer.get_addr_line2()
        city = customer.get_addr_city()
        state = customer.get_addr_state()
        pincode = customer.get_addr_pincode()
        sql = "insert into address values(:id,:line1,:line2,:city,:state,:pincode)"
        cur.execute(sql, {"id" :id, "line1" :line1, "line2" :line2, "city" :city, "state" :state, "pincode" :pincode} )
        con.commit()
        print("Congrats! Login for your account was created successfully.")
        print("Your Customer ID : " ,id)
        con.close()

    def get_pin(id):
        con = cx_Oracle.connect('scott/tiger@oracle')
        cur = con.cursor()
        sql = "select pin from customers where customer_id = :id"
        cur.execute(sql, {"id" :id})
        res = cur.fetchall()
        pin=res[0][0]
        return pin
        con.commit()
        con.close()
        
    def get_all_info_customer(id):
        con = cx_Oracle.connect('scott/tiger@oracle')
        cur = con.cursor()
        sql = "select * from customers where customer_id = :id"
        cur.execute(sql, {"id" :id})
        res = cur.fetchall()
        #print(res)
        if len(res) == 0:
            return None
        customer = Customer()
        customer.set_customer_id(id)
        customer.set_first_name(res[0][1])
        customer.set_last_name(res[0][2])
        return customer
        con.commit()
        con.close()

    def get_loan_info(loan_no,id):
        con = cx_Oracle.connect('scott/tiger@oracle')
        cur = con.cursor()
        sql = "select * from loans where loan_no = :ln_no "
        cur.execute(sql, {"ln_no" :loan_no})
        res = cur.fetchall()
        if len(res) == 0:
            return None
        loan_no = res[0][1]
        loan_type = res[0][2]
        amt = res[0][3]
        loan=Loan()
        loan.set_loan_no(loan_no)
        loan.set_loan_type(loan_type)
        loan.set_amount(amt)
        return loan
        con.commit()
        con.close()
    
    def get_all_info_account(acc_no ,id ,msg):
        con = cx_Oracle.connect('scott/tiger@oracle')
        cur = con.cursor()
        sql = None
        if msg == "transfer":
            sql = "select * from accounts where account_no = :acc_no "
            cur.execute(sql, {"acc_no" :acc_no})
        else:
            sql = "select * from accounts where account_no = :acc_no and customer_id = :id "
            cur.execute(sql, {"acc_no" :acc_no, "id" :id})

        res = cur.fetchall()
        if len(res) == 0:
            return None
         
        account_no = res[0][1]
        acc_type = res[0][2]
        balance = res[0][3]
        if acc_type=='fd':
            return
        elif acc_type=="savings":
            account=Savings()
        else:
            account=Current()
        account.set_account_type(acc_type)
        account.set_balance(balance)
        account.set_account_no(account_no)
        return account
        con.commit()
        con.close()


    def money_deposit_customer(account ,amount):
        con = cx_Oracle.connect('scott/tiger@oracle')
        cur = con.cursor()
        bal = account.get_balance()
        acc_no = account.get_account_no()
        type = "credit"
        sql = "update accounts set balance = :bal where account_no = :acc_no"
        cur.execute(sql , {"bal" :bal, "acc_no" :acc_no})
        sql = "select transaction_id_sequence.nextval from dual"
        cur.execute(sql)
        res = cur.fetchall()
        t_id = res[0][0]
        sql = "insert into transactions values (:t_id,:acc_no,:type,:amount,:bal)"
        cur.execute(sql , {"t_id" :t_id, "acc_no" :acc_no, "type" :type , "amount" :amount , "bal" :bal})
        con.commit()
        con.close()

    def money_withdraw_customer(account ,amount ,msg):
        con = cx_Oracle.connect('scott/tiger@oracle')
        cur = con.cursor()
        acc_type = account.get_account_type()
        bal = account.get_balance()
        acc_no = account.get_account_no()
        type = msg
        sql = "update accounts set balance = :bal where account_no = :acc_no"
        cur.execute(sql , {"bal" :bal, "acc_no" :acc_no})
        sql = "select transaction_id_sequence.nextval from dual"
        cur.execute(sql)
        res = cur.fetchall()
        t_id = res[0][0]
        sql = "insert into transactions values (:t_id,:acc_no,:type,:amount,:bal)"
        cur.execute(sql , {"t_id" :t_id ,"acc_no": acc_no, "type": type, "amount": amount, "bal": bal})
        con.commit()
        con.close()


    def transfer_money_customer(account_sender, account_receiver, amount):
        con = cx_Oracle.connect('scott/tiger@oracle')
        cur = con.cursor()
        if account_sender.withdraw(amount) == True:
            account_receiver.deposit(amount)
            database.money_withdraw_customer(account_sender, amount, "transfer")
            database.money_deposit_customer(account_receiver, amount)
            print("Transfer was completed successfully.")
            print("The New Balance for Account No ", account_sender.get_account_no(), " : ", account_sender.get_balance())
            print("The New Balance for Account No ", account_receiver.get_account_no(), " : ", account_receiver.get_balance())
        con.commit()
        con.close()


class functions:
    def sign_up_new_customer():
        c1 = New_customer()
        first_name = input("Enter the First Name\n")
        last_name = input("Enter the Last Name\n")
        add_line1 = input("Enter the Address Line 1\n")
        add_line2 = input("Enter the Address Line 2\n")
        city = input("Enter the City\n")
        state = input("Enter the State\n")
        PIN = int(input("Enter your four digit PIN of your choice as password\n"))
        try:
            pincode = int(input("Enter your 6 digit Pincode\n"))
            if pincode < 100000 or pincode > 999999:
                print("Invalid Pincode")
                return
        except:
            print("Sorry, No such Pincode")
            return
        c1.set_first_name(first_name)
        c1.set_last_name(last_name)
        c1.set_PIN(PIN)
        ad = Address()
        ad.set_line_1(add_line1)
        ad.set_line_2(add_line2)
        ad.set_city(city)
        ad.set_state(state)
        ad.set_pincode(pincode)
        c1.set_address(ad)
        database.sign_up_customer(customer)


    def sign_in_old_customer():
            id = int(input("Enter your ID\n"))
            pin = int(input("Enter your 4 digit PIN:\n"))
            apin=database.get_pin(id)
            if (pin==apin):
                print("welcome to the bank")                           
            else:
                print("Invalid ID")
                return

            ch = 1
            while ch != 0:
                print("\n*** Menu ***")
                print("\nYou want to,")
                print("1. Open New Account")
                print("2. Money Deposit")
                print("3. Money Withdrawal")
                print("4. Transfer Money")
                print("5. Print Statement")

                try:
                    ch = int(input())
                except:
                    print("Sorry, Enter a proper choice.")
                    ch = 1
                    continue

                if ch == 1:
                    login_menu.open_new_account(id)
                elif ch == 2:
                    login_menu.deposit_money(id)
                elif ch == 3:
                    login_menu.withdraw_money(id)
                elif ch == 4:
                    login_menu.transfer_money(id)
                elif ch == 5:
                     print("\n*** Menu ***")
                     print("1. Account")
                     print("2. Loan")
                     try:
                        ch = int(input())
                     except:
                        print("Sorry, Enter a proper choice.")
                        ch = 1
                     if ch==1:
                         login_menu.print_statement(id)
                     else:
                          login_menu.print_loan_statement(id)  
                else:
                    print("Sorry, Invalid Choice")

class login_menu:
    def open_new_account(id):
        account = None
        print("\n *** Menu *** ")
        print("1. Open a Savings Account")
        print("2. Open a Current Account")
        print("3. Fixed Deposit(FD) Account")
        print("4. Loan")

        try:
            ch = int(input())
        except:
            print("Sorry, Enter a proper choice.")
            return
        if ch==4:
            database.get_new_loan(id)
            return
        database.get_new_account(ch, id)
        

    def deposit_money(id):
        try:
            acc_no = int(input("Enter your account Number\n"))
        except:
            print("Invalid Account Number")
            return
        account = database.get_all_info_account(acc_no, id, "deposit")
        if account is not None:
            try:
                amount = int(input("Enter the amount to Deposit\n"))
            except:
                print("Invalid Amount")
                return
            if account.deposit(amount) == True:
                database.money_deposit_customer(account, amount)
                print("Rs ", amount, "Successfully deposited to your account.");
                print("Balance : Rs ", account.get_balance())

        else:
            print("Sorry, Entered Account Number doesn't match")


    def withdraw_money(id):
        try:
            acc_no = int(input("Enter your account No\n"))
        except:
            print("Invalid Account No")
            return
        account = database.get_all_info_account(acc_no, id, "withdraw")
        if account is not None:                  
            try:
                amount = int(input("Enter the amount to Withdraw\n"))
            except:
                print("Invalid Amount")
                return
            if account.withdraw(amount) == True:
                database.money_withdraw_customer(account, amount, "withdraw")
                print("Rs ", amount, "was Successfully withdrawn");
                print("Balance : Rs ", account.get_balance())

        else:
            print("Sorry, Entered Account Number doesn't match")


    def print_statement(id):
        try:
            acc_no = int(input("Enter your account No\n"))
        except:
            print("Invalid Account No")
            return
        account = database.get_all_info_account(acc_no, id, "statement")
        if account.get_account_type()=="fp":
            print("Number of terms for deposit is",account.get_no_of_terms())
        print("Account Number\t\t\tTransaction Type \t\t\t Balance \t")
        print(account.get_account_no(),"\t\t\t",account.get_account_type(),"\t\t\t",account.get_balance())

    def print_loan_statement(id):
        try:
            ln_no = int(input("Enter your Loan Number\n"))
        except:
            print("Sorry, Invalid Loan No")
            return
        loan = database.get_loan_info(ln_no, id)
        print("loan Number\t\t\tloan Type \t\t\t amount \t")
        print(loan.get_loan_no(),"\t\t\t",loan.get_loan_type(),"\t\t\t",loan.get_amount())

    def transfer_money(id):
        try:
            acc_no_sender = int(input("Enter Account No From : "))
        except:
            print("Invalid Account Number")
            return
        account_sender = database.get_all_info_account(acc_no_sender, id, "withdraw")
        if account_sender is not None:
            try:
                acc_no_receiver = int(input("Enter Account No To Transfer Money To : "))
            except:
                print("Invalid Account No")
                return
            account_receiver = database.get_all_info_account(acc_no_receiver, -1, "transfer")
            if account_receiver is not None:
                try:
                    amount = int(input("\nEnter Amount To Transfer : "))
                except:
                    print("Invalid Amount")
                    return
                database.transfer_money_customer(account_sender, account_receiver, amount)
            else:
                print("Sorry Account doesn't exist")

        else:
            print("Sorry Account Number doesn't match")


database.create_all_tables()
choice = 1
while choice != 0:

    print("********** MAIN MENU ********** ")
    print("Enter '1' for Sign up (New customer)")
    print("Enter '2' for Sign in(Pre-registered customers)")
    print("Enter '0' to quit")
    try:
        choice = int(input())
    except:
        print("Sorry, Enter a valid choice...")
        choice = 1
    if choice == 1:
        functions.sign_up_new_customer()
    elif choice == 2:
        functions.sign_in_old_customer()
    else:
        print("Invalid Choice")
