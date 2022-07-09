import logging

logging.basicConfig(filename="task1.log",level=logging.DEBUG, format='%(asctime)s %(name)s %(levelname)s %(message)s')

#l = [3,4,5,6,7 , [23,456,67,8,78,78] , [345,56,87,8,98,9] , (234,6657,6) , {"key1" :"sudh" ,
#234:[23,45,656]}]
#1 . Try to reverse a list
#2. try to access 234 out of this list
#3 . try to access 456
#4 . Try to extract only a list collection form list l
#5 . Try to extract "sudh"
#6 . Try to list all the key in dict element avaible in list

class lis :
    logging.info("entering into class lis")

    try:
        def rev_lis(self,l):
            logging.info("we are into function")
            rev=l[::-1]
            logging.info("WE HAVE COMPLETED REVERSING %s",rev)
            return rev

        def acce(self,l):
            logging.info("we are into function")
            acc=l[8][234]
            logging.info("WE HAVE access to 234 in the list %s", acc)
            return acc

        def acces(self,l):
            logging.info("we are into function")
            a=l[5][1]
            logging.info("WE HAVE access to 456 in the list %s", a)
            return a

        def only_lis(self,l):
            logging.info("we are into function")
            for i in l:
               if type(i) == list:
                logging.info("Here are your only lists from the list %s", i)


        def sud(self,l):
            logging.info("we are into function")
            for i in l:
                if type(i)==list or type(i)==tuple or type(i)==set:
                     for j in l:
                        if j=="sudh":
                            logging.info("sudh found in list tuple and set %s",j)
                elif type(i)==dict:
                    for k,v in i.items():
                        if k=="sudh" or v=="sudh":
                            logging.info("sudh found in key elements in dict %s",k)
                            logging.info("sudh found in value in dict %s", v)
        def keysss(self,l):
            logging.info("we are into function")
            for i in l:
                if type(i) == dict:
                    for k in i.keys():
                        logging.info(" ALL KEYS FROM DICTIONARY %s",k)


    except Exception as e:
        logging.info("its giving an error")
        logging.exception("error")

obj1=lis()
print(obj1.rev_lis(l = [3,4,5,6,7 , [23,456,67,8,78,78] , [345,56,87,8,98,9] , (234,6657,6) , {"key1" :"sudh" ,234:[23,45,656]}]))
print(obj1.acce(l = [3,4,5,6,7 , [23,456,67,8,78,78] , [345,56,87,8,98,9] , (234,6657,6) , {"key1" :"sudh" ,234:[23,45,656]}]))
print(obj1.only_lis(l = [3,4,5,6,7 , [23,456,67,8,78,78] , [345,56,87,8,98,9] , (234,6657,6) , {"key1" :"sudh" ,234:[23,45,656]}]))
print(obj1.sud(l = [3,4,5,6,7 , [23,456,67,8,78,78] , [345,56,87,8,98,9] , (234,6657,6) , {"key1" :"sudh" ,234:[23,45,656]}]))
print(obj1.keysss(l = [3,4,5,6,7 , [23,456,67,8,78,78] , [345,56,87,8,98,9] , (234,6657,6) , {"key1" :"sudh" ,234:[23,45,656]}]))
print(obj1.acces(l = [3,4,5,6,7 , [23,456,67,8,78,78] , [345,56,87,8,98,9] , (234,6657,6) , {"key1" :"sudh" ,234:[23,45,656]}]))

