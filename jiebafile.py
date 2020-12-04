import jieba
import csv
with open('processed.csv', 'w') as csvfile:
    csvwriter = csv.writer(csvfile)
    with open('recipes.csv', 'r') as original:
        csvreader = csv.reader(original)
        for row in csvreader:
            #print(row)
            
            seg_list = jieba.cut_for_search(row[0])
            csvwriter.writerow([' '.join(seg_list)])


