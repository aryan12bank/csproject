import mysql.connector as m
n=m.connect(host='localhost',user='root',passwd='ARYANop007',database='BANK')
s=n.cursor()
a=int(input("Enter 1:for employee\nEnter 2:if you are customer\n-->"))
if a==1:
  emp_id=int(input("Enter your employee ID"))
  print("loggin succesful;)")

elif a==2:
  print("0 if you want to create a new account in the place of account number\n write the name to be register and set a password")
  cust_ac=int(input("enter your account number"))
  cust_name=input("enter your registered name")
  cust_pass=int(input('Enter your password'))
  print("login Successful ;)")
  j=int(input("Enter 0:For creating an account\nEnter 1: For checking your account details\n"))
  if j==0:
    try:
      s.execute("select ACNO from ad")
      y=s.fetchall()
      z=y[-1][0]
      t=z+1
      c_nm=input("enter your name")
      c_ph=int(input("enter your ph no."))
      c_i=int(input("enter your identity number example adhar"))
      act_type=input("enter your account type")
      s.execute("insert into AD values({},{},{},0,null,null").format(t,c_nm,c_ph,act_type)
      print("The bill of your account creation is succefully generated....")
      s.execute("select ENA FROM emp where ED={}").format("CASHIER")
      EMP_N=s.fetcone()
      print("kindly visit to the bank for KYC and biometrics\n GO TO\n EMPLOYEE NAME:",EMP_N)
      print("The request for creating an account is succefully sent to the employee shown above")
    except ValueError:
      print("invalid data is recorded kindly check again")