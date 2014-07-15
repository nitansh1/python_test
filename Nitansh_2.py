import os
import sys
from csv import reader

class CompanyInfo(object):
    """ The company info is stored in it """  
  
    def __init__(self, company_name):
      self.__company_price__list = []
      self.__company_time_list   = []
      self.__name = company_name

    def add_info(self, year, month, price):
      self.__company_time_list.append(year + ' ' + month) 
      self.__company_price__list.append(price)  

    def find_peak_share_time(self):
       indices = [i for i, x in enumerate(self.__company_price__list) if x == max(self.__company_price__list)]
       time_string = ''
       for index in indices:
          time_string += self.__company_time_list[index] + ' '

       return time_string, self.__company_price__list[indices[0]] 

    def share_info(self):
      return self.__name + ' ---> the peak time is %s and Share at that time is %s '%  self.find_peak_share_time()  

class MainHandler(object):
  """ Triggers the main process """

  def __init__(self):
    self.company_list = []

  def final_info(self):
    for company in self.company_list:
      print company.share_info()
      
  def add_company(self, company):
    self.company_list.append(company)

  def process_row(self,row):
    """ Process each row of the csv file and write it to dictornary """
    year  = row[0]
    month = row[1]
    share_prices = row[2:]
    for x in range(0, len(self.company_list)):
      self.company_list[x].add_info(year, month, share_prices[x])

  def read_from_file(self,filename):
    """ Read the given csv file """
    count = 0  
    with open(filename, 'rb') as file_object:
      csv_reader = reader(file_object)
      companies_name = next(csv_reader)
      for company_name in companies_name[2:]:
        self.add_company(CompanyInfo(company_name)) 
      try :
        while(True):
          self.process_row(next(csv_reader))
      except:
        pass # stoping the iteration
      file_object.close()
  

if __name__ == "__main__":
  
  if not sys.argv[1]:
    print 'Please enter the filename'
  
  if os.path.exists(sys.argv[1]):
    my_main_handler = MainHandler()
    my_main_handler.read_from_file(sys.argv[1])
    my_main_handler.final_info()
  else :
    print 'Please check the file is present or not'
