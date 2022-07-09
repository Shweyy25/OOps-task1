import logging
logging.basicConfig(filename="task2.log",level=logging.DEBUG, format='%(asctime)s %(name)s %(levelname)s %(message)s')
#q.3) Try to extract all the list entity. #L
#q.4) Try to extract all the dict entity.
#q.5) Try to extract all the Tuples entity.
#q.6) Try to extract all the Numeric data it may be a part of dict key and values.
#q.7) Try to give summation of all the numeric data.
#q.8) Try to filter out all the odd values out all numeric datawhich is a part of a list.
#q.9) Try to extract "ineuron" out of this dataset.
#q.10) Try to find out a number of occurance of all the data.
#q.11) Try to find out a number of keys in dict element.
#q.12) Try to filter out all the string data.
#q.13) Try to find out alphanum in data.
#q.14) Try to find out multiplication of all numeric value in the individual collection inside dataset.
#q.15) Try to unwrape all the collection inside collection and create a flat list.

#l =[[1,2,3,4], (2,3,4,5,6), (3,4,5,6,7), set([23,4,5,45,4,4,5,45,45,4,5]),{'k1' : "sudh" , 'k2' :
# "ineuron", 'k3' : "kumar", 3:6, 7:8}, ["ineuron", "data science"]]
class lis2 :
    logging.info("entering into class lis2")
    def __init__(self,l):
        self.l=l
    try:

        def extract_lis(self):
            logging.info("we are here for extraction of list from a list")
            l1=[]
            for i in self.l:
                if type(i)==list :
                        l1.append(i)
            logging.info("The new list with only list items %s",l1)
            return l1

    except Exception as e:
        logging.exception(e)

    try:
        def extract_dic(self):
            logging.info("we are here for extraction of dictionary from a list")
            l2=[]
            for i in self.l:
                if type(i)==dict:
                    l2.append(i)
            logging.info("The new list with only dict items %s", l2)
            return l2

    except Exception as e:
        logging.exception(e)

    try:

        def extract_tuples(self):
            logging.info("we are here for extraction of tuples from a list")
            l3=[]
            for i in self.l:
                if type(i)==tuple:
                    l3.append(i)
            logging.info("The new list with only tuples  %s", l3)
            return l3

    except Exception as e:
        logging.exception(e)

    try:

        def num_data(self):
            logging.info("we are here for extraction of all numeric data from a list")
            l4=[]
            for i in self.l:
                if type(i)==list or type(i)==tuple or type(i)==set:
                    for j in i:
                        if type(j)==int:
                            l4.append(j)

                elif type(i)==dict:
                    for k,v in i.items():
                        if type(k)==int or type(v)==int:
                            l4.append(k)
                            l4.append(v)
            logging.info("All the extracted numeric data %s",l4)
            return l4

    except Exception as e:
        logging.exception(e)

    try:
        def sum_num(self):
            logging.info("we are here for extraction and summation of all numeric data from a list")
            l4 = []
            sum=0
            for i in self.l:

                if type(i) == list or type(i) == tuple or type(i) == set:
                    for j in i:
                        if type(j) == int:
                            l4.append(j)
                elif type(i) == dict:
                    for k, v in i.items():
                        if type(k) == int or type(v) == int:
                            l4.append(k)
                            l4.append(v)

            for s in range(0, len(l4)):
                sum = sum + l4[s]
            logging.info("sum of All the extracted numeric data %s", sum)
            return sum

    except Exception as e:
        logging.exception(e)

    try:

        def odd_val(self):
            logging.info("we are here to filter out all odd data from a list")
            l5=[]
            l4 = []
            sum = 0
            for i in self.l:

                if type(i) == list or type(i) == tuple or type(i) == set:
                    for j in i:
                        if type(j) == int:
                            l4.append(j)
                elif type(i) == dict:
                    for k, v in i.items():
                        if type(k) == int or type(v) == int:
                            l4.append(k)
                            l4.append(v)

            for s in range(0, len(l4)):
               if s%2==0:
                   l5.append(s)
            logging.info("Here is your filtered data %s", l5)
            return l5

    except Exception as e:
        logging.exception(e)
    try:

        def ex_ineuron(self):
            logging.info("We are going to extract ineuron from the given list")
            l5=[]
            for i in self.l:
                if type(i) == list or type(i) == tuple or type(i) == set:
                    for j in i:
                        if j == 'ineuron':
                           l5.append(j)
                elif type(i) == dict:
                    for k, v in i.items():
                        if k == 'ineuron':
                            l5.append(k)
                        elif v=='ineuron':
                            l5.append(v)
            logging.info("list after extracting ineuron %s", l5)
            return l5

    except Exception as e:
        logging.exception(e)

    try:

        def occur(self):
            logging.info("We are going count the occurance of each data in a list")
            l5=[]
            for i in self.l:

                if type(i) == list or type(i) == tuple or type(i) == set:
                    for j in i:
                        if type(j) == int or type(j)==str:
                            l5.append(j)
                elif type(i) == dict:
                    for k, v in i.items():
                        if type(k) == int or type(v) == int or type(k)==str or type(v)==str:
                            l5.append(k)
                            l5.append(v)
            c=0
            for c in l5:
                ct=l5.count(c)
                logging.info("elements is  %s", c)
                logging.info("count is %s",ct )

    except Exception as e:
        logging.exception(e)

    try:

        def unwrape(self):
            logging.info("We are going to unwrape all data in a list")
            l5 = []
            for i in self.l:

                if type(i) == list or type(i) == tuple or type(i) == set:
                    for j in i:
                        if type(j) == int or type(j) == str:
                            l5.append(j)
                elif type(i) == dict:
                    for k, v in i.items():
                        if type(k) == int or type(v) == int or type(k) == str or type(v) == str:
                            l5.append(k)
                            l5.append(v)

            logging.info("Unwraped data %s",l5)
    except Exception as e:
        logging.exception(e)
    try:
        def num_keys(self):
            c=0
            logging.info("WE are here to find out the number of keys in dictionary")
            l6=[]
            for i in self.l:
                if type(i) == dict:
                    for k in i.keys():
                        c=c+1
            logging.info("total count of keys %s",c)
            return c

    except Exception as e:
        logging.exception(e)

    try:
        def filtr_strg(self):
            logging.info("WE are here to filter  out string data ")
            l6 = []
            for i in self.l:
                if type(i) == list or type(i) == tuple or type(i) == set:
                    for j in i:
                        if type(j) == int:
                            l6.append(j)
                elif type(i) == dict:
                    for k, v in i.items():
                        if type(k) == int or type(v) == int:
                            l6.append(k)
                            l6.append(v)
            logging.info("filtered list %s", l6)
            return l6

    except Exception as e:
        logging.exception(e)

    try:
        def al_num(self):
            logging.info("WE are here to find out alnum data ")
            l6=[]
            for i in self.l:
                for k in i:
                    k = str(k)
                    if not k.isnumeric() and not k.isalpha():
                        l6.append(k)
            logging.info("Alpha numeric data %s", l6)
            return l6

    except Exception as e:
        logging.exception(e)
    try:
        def mul(self):
            for i in self.l:
                mul = 1
                if type(i) != dict:
                    logging.info("the type is %s",type(i))
                    for j in i:
                        j = str(j)
                        if j.isnumeric():
                            j = int(j)
                            mul = mul * j
                    if mul != 1:
                        logging.info("data %s",i)
                        logging.info("mutiplication %s",mul)
                elif type(i) == dict:
                    mul = 1
                    for k, v in i.items():
                        v = str(v)
                        if v.isnumeric():
                            v = int(v)
                            mul *= v
                    logging.info("data %s",taski)
                    logging.info("mutiplication %s", mul)
    except Exception as e:
        logging.exception(e)

obj=lis2(l =[[1,2,3,4], (2,3,4,5,6), (3,4,5,6,7), set([23,4,5,45,4,4,5,45,45,4,5]),{'k1' : "sudh" , 'k2' :"ineuron", 'k3' : "kumar", 3:6, 7:8},
             ["ineuron", "datascience"]])
print(obj.mul())