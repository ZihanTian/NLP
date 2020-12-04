import csv 
import json
#d = json.load(open("results.txt"))['1']
filename = "recipes.csv"
fields = ['recipe']    
# writing to csv file  
with open(filename, 'w') as csvfile:  
    # creating a csv writer object  
    csvwriter = csv.writer(csvfile)  
        
    # writing the fields  
    csvwriter.writerow(fields) 
    csvwriter.writerow(['context1'])
    #csvwriter.writerows(d) 
