import logging
logging.basicConfig(filename="task3.log",level=logging.DEBUG, format='%(asctime)s %(name)s %(levelname)s %(message)s')

#s = "this is My First Python programming class and i am learNING python string and its function"
#1 . Try to extract data from index one to index 300 with a jump of 3
#2. Try to reverse a string without using reverse function
#3. Try to split a string after conversion of entire string in uppercase
#4. try to convert the whole string into lower case
#5 . Try to capitalize the whole string
#6 . Write a diference between isalnum() and isalpha()
#7. Try to give an example of expand tab
#8 . Give an example of strip , lstrip and rstrip
#9. Replace a string charecter by another charector by taking your own example
#"sudhanshu"
#10 . Try to give a defination of string center function with and exmple
#11 . Write your own definition of compiler and interpretor without copy paste form internet in your
#own language
#12 . Python is a interpreted of compiled language give a clear ans with your understanding
#13 . Try to write a usecase of python with your understanding.


class strg:

    logging.info("We are already inside the class")
    def __init__(self,s):
        self.s=s

    try:

        def extr(self):
            logging.info("We will now extract index from 0 to 300 with a jump of 3")
            a=self.s[1:301:3]
            logging.info("alphabets from 1 to 300 is %s",a)
            return a
    except Exception as e:
        logging.exception(e)

    try:
        def rev(self):
            logging.info("We are going to reverse a string")
            a=self.s[::-1]
            logging.info("String after reversing it is : %s",a)
            return a
    except Exception as e:
        logging.exception(e)

    try:

        def splt_upper(self):
            logging.info("We are going to split and change the entire string to upperclass")
            a=self.s
            up=a.upper()
            sp=up.split()
            logging.info("Final string is %s",sp)
            return sp

    except Exception as e:
        logging.exception(e)

    try:

        def lower(self):
            logging.info("We are going to change the entire string to lowerclass")
            a=self.s
            low=a.lower()
            logging.info("Final string is %s",low)
            return low

    except Exception as e:
        logging.exception(e)

obj=strg("this is My First Python programming class and i am learNING python string and its function")
print(obj.lower())