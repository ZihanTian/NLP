query1 = {1:0, 4:0,31:1, 45:0, 48:0, 113:1, 123:1, 124:0, 165:0, 164:0, 163:0, 206:0, 218:0, 225:0, 244:0, 272:0, 282:0, 284:0, 336:1, 390:1, 412:0, 511:1, 516:1, 577:0, 579:1, 605:0, 626:0, 707:1, 776:1, 848:0, 922:0, 939:0}
query2 = {1:0, 33:0, 74:0, 79:0, 238:0, 282:0, 293:0, 401:0, 423:0, 498:0, 493:0, 577:0, 588:0, 596:0, 605:0, 741:0, 760:0, 864:0, 890:0, 9:1, 19:1, 58:1, 76:1, 265:1, 294:1, 312:1 ,353:1, 509:0, 541:1, 568:1, 584:1,  598:1, 608:1, 693:1, 761:1, 818:1}
query3 = {1:0, 116:0, 130:0,172:0, 191:0, 256:0, 282:0, 185:0, 298:0, 478:0, 553:0, 571:0, 577:0, 605:0, 638:0, 678:0, 736:0, 768:0, 842:0, 868:0, 885:0, 94:1, 361:1, 406:1, 436:1, 642:1, 699:1, 722:1}
query4 = {1:0, 24:1, 43:0, 56:0, 63:1, 128:1, 152:1, 160:0, 186:1, 237:1, 264:1, 266:1, 282:0, 298:0, 307:0, 346:1, 351:1, 356:1, 447:1, 458:1, 464:1, 469:1, 476:1, 525:1, 535:1, 538:1, 577:0, 581:1, 605:0, 614:0, 670:0, 686:0, 708:0, 754:1, 785:1, 805:0, 848:0}
query5 = {8:0, 1:0, 19:0, 14:0, 16:0, 21:0, 77:0, 84:0, 109:0, 146:0, 180:0, 204:0, 205:0, 143:0, 282:0, 290:0, 296:0, 305:0, 318:0, 438:0, 457:0, 508:0, 568:0, 577:0, 587:0, 605:0, 631:0, 641:0, 665:0, 677:0, 709:0, 728:0, 759:0, 800:0, 848:0, 900:0, 96:1, 125:1, 181:1, 259:1, 360:1, 366:1, 411:1, 420:1, 478:1,547:1, 561:1, 560:1, 617:1, 766:1, 790:1, 835:1}
query6 = {52:1, 75:1, 3:0, 83:0, 93:0, 95:0, 246:1, 272:0, 879:1, 922:0}
query7 = {33:1, 81:1, 4:0, 31:0, 45:0, 48:0, 113:0, 123:0, 124:0,163:1,2206:1,284:0, 290:1, 339:1, 457:1, 589:1, 626:1, 638:1, 654:1, 734:1, 769:1, 796:1, 825:1, 833:1, 848:0}
query8 = {17:1, 32:1, 51:0, 84:1, 89:1, 133:1, 199:1, 201:1, 240:1, 267:1, 323:1, 331:1, 382:1, 407:1, 536:1, 601:1, 620:1, 663:1, 715:1, 750:1, 833:1, 838:1, 605:0, 653:0, 885:0}
query9 = {8:0, 40:0, 44:0, 182:1, 592:0, 605:0, 689:1}
query10 = {121:1, 956:1, 129:1, 141:1, 860:1, 929:1, 939:0, 956:1}
'''# b= 0.5
result1 = [243, 411, 578, 112, 335, 515, 775, 122, 706, 104]
result2 = [595, 760, 759, 497, 817, 540, 8, 607, 293, 508]
result3 = [360, 698, 735, 284, 115, 637, 93, 641, 867, 677]
result4 = [524, 784, 185, 580, 350, 151, 463, 753, 537, 263]

result5 = [616, 560, 359, 124, 765, 13, 676, 95, 834, 727]
result6 = [513, 416, 880, 461, 245, 914, 931, 879, 854, 920]
result7 = [465, 163, 625, 385, 164, 768, 80, 588, 578, 411]
result8 = [547, 390, 879, 513, 461, 549, 792, 332, 472, 79]
result9 = [321, 229, 590, 288, 60, 39, 430, 360, 698, 104]
result10 = [140, 120, 859, 928, 128, 955, 938, -1, -1, -1]
import math 
finaldcg = []
finalidcg = []
finalndcg = []
def cal(result, query):
    dcg = 0
    idcg = 0 
    idea = []
    for idx, docId in enumerate(result):
        docId+=1
        idx += 1
        score = query.get(docId, -1)
        if score == 0:
            score = 0.5
        idea.append((score, idx))
        if score != -1:
            dcg+=score/math.log(idx+1, 2)
    idea.sort(reverse=True)
    for i, (score, idx) in enumerate(idea):
        i+=1
        if score>0:
            idcg += score/math.log(i+1, 2)
    #print(dcg, idcg)
    if idcg == 0:
        return float(format(dcg, '.3f')), float(format(idcg, '.3f')), 0
    return float(format(dcg, '.3f')), float(format(idcg, '.3f')), float(format(dcg/idcg, '.3f'))
#result1 = [321, 229, 590, 288, 60, 39, 430, 360, 698, 104]
#result2 = [688, 181, 604]
#result3 = [649, 500, 803, 556, 452, 632, 187, 248, 368, 688]
#result4 = [803, 366, 694, 649, 7, 304, 586, 604, 78, 456]
#result5 = [649, 803, 694, 366, 304, 586, 7, 591, 8, 607]
#result6 = [304, 7, 586, 201, 772, 229, 321, 590, 288, 60]
num1, num2, num3 = cal(result1, query1)
finaldcg.append(num1)
finalidcg.append(num2)
finalndcg.append(num3)
num1, num2, num3 = cal(result2, query2)
finaldcg.append(num1)
finalidcg.append(num2)
finalndcg.append(num3)
num1, num2, num3 = cal(result3, query3)
finaldcg.append(num1)
finalidcg.append(num2)
finalndcg.append(num3)
num1, num2, num3 = cal(result4, query4)
finaldcg.append(num1)
finalidcg.append(num2)
finalndcg.append(num3)
num1, num2, num3 = cal(result5, query5)
finaldcg.append(num1)
finalidcg.append(num2)
finalndcg.append(num3)
num1, num2, num3 = cal(result6, query6)
finaldcg.append(num1)
finalidcg.append(num2)
finalndcg.append(num3)
num1, num2, num3 = cal(result7, query7)
finaldcg.append(num1)
finalidcg.append(num2)
finalndcg.append(num3)
num1, num2, num3 = cal(result8, query8)
finaldcg.append(num1)
finalidcg.append(num2)
finalndcg.append(num3)
num1, num2, num3 = cal(result9, query9)
finaldcg.append(num1)
finalidcg.append(num2)
finalndcg.append(num3)
num1, num2, num3 = cal(result10, query10)
finaldcg.append(num1)
finalidcg.append(num2)
finalndcg.append(num3)
print(finaldcg)
print(finalidcg)
print(finalndcg)
# b = 0.55
result1 = [243, 411, 578, 112, 335, 775, 122, 515, 706, 372]
result2 = [595, 760, 540, 817, 497, 759, 508, 8, 607, 293]
result3 = [698, 360, 735, 93, 641, 284, 115, 637, 867, 677]
result4 = [524, 185, 784, 580, 350, 151, 463, 753, 537, 263]

result5 = [616, 560, 359, 124, 765, 13, 676, 95, 834, 727]
result6 = [880, 914, 416, 245, 920, 668, 274, 931, 734, 883]
result7 = [465, 163, 625, 385, 164, 768, 411, 243, 80, 588]
result8 = [749, 239, 381, 651, 809, 590, 288, 60, 840, 496]
result9 = [229, 321, 590, 288, 60, 39, 430, 698, 360, 104]
result10 = [140, 120, 859, 928, 128, 955, 938, -1, -1, -1]
finaldcg = []
finalidcg = []
finalndcg = []        
num1, num2, num3 = cal(result1, query1)
finaldcg.append(num1)
finalidcg.append(num2)
finalndcg.append(num3)
num1, num2, num3 = cal(result2, query2)
finaldcg.append(num1)
finalidcg.append(num2)
finalndcg.append(num3)
num1, num2, num3 = cal(result3, query3)
finaldcg.append(num1)
finalidcg.append(num2)
finalndcg.append(num3)
num1, num2, num3 = cal(result4, query4)
finaldcg.append(num1)
finalidcg.append(num2)
finalndcg.append(num3)
num1, num2, num3 = cal(result5, query5)
finaldcg.append(num1)
finalidcg.append(num2)
finalndcg.append(num3)
num1, num2, num3 = cal(result6, query6)
finaldcg.append(num1)
finalidcg.append(num2)
finalndcg.append(num3)
num1, num2, num3 = cal(result7, query7)
finaldcg.append(num1)
finalidcg.append(num2)
finalndcg.append(num3)
num1, num2, num3 = cal(result8, query8)
finaldcg.append(num1)
finalidcg.append(num2)
finalndcg.append(num3)
num1, num2, num3 = cal(result9, query9)
finaldcg.append(num1)
finalidcg.append(num2)
finalndcg.append(num3)
num1, num2, num3 = cal(result10, query10)
finaldcg.append(num1)
finalidcg.append(num2)
finalndcg.append(num3)
print(finaldcg)
print(finalidcg)
print(finalndcg)
# b = 0.6
result1 = [411, 243, 578, 112, 335, 515, 775, 122, 706, 104]
result2 = [595, 760, 817, 540, 497, 759, 508, 8, 607, 293]
result3 = [698, 360, 735, 93, 641, 284, 115, 637, 677, 190]
result4 = [524, 185, 784, 580, 350, 151, 463, 753, 537, 263]

result5 = [616, 560, 359, 124, 765, 13, 676, 95, 834, 727]
result6 = [880, 914, 416, 245, 920, 668, 274, 931, 734, 883]
result7 = [465, 163, 625, 385, 164, 768, 80, 588, 243, 411]
result8 = [239, 381, 749, 651, 809, 288, 590, 60, 132, 600]
result9 = [321, 229, 39, 430, 288, 590, 60, 104, 698, 360]
result10 = [140, 120, 859, 928, 128, 955, 938]
finaldcg = []
finalidcg = []
finalndcg = []        
num1, num2, num3 = cal(result1, query1)
finaldcg.append(num1)
finalidcg.append(num2)
finalndcg.append(num3)
num1, num2, num3 = cal(result2, query2)
finaldcg.append(num1)
finalidcg.append(num2)
finalndcg.append(num3)
num1, num2, num3 = cal(result3, query3)
finaldcg.append(num1)
finalidcg.append(num2)
finalndcg.append(num3)
num1, num2, num3 = cal(result4, query4)
finaldcg.append(num1)
finalidcg.append(num2)
finalndcg.append(num3)
num1, num2, num3 = cal(result5, query5)
finaldcg.append(num1)
finalidcg.append(num2)
finalndcg.append(num3)
num1, num2, num3 = cal(result6, query6)
finaldcg.append(num1)
finalidcg.append(num2)
finalndcg.append(num3)
num1, num2, num3 = cal(result7, query7)
finaldcg.append(num1)
finalidcg.append(num2)
finalndcg.append(num3)
num1, num2, num3 = cal(result8, query8)
finaldcg.append(num1)
finalidcg.append(num2)
finalndcg.append(num3)
num1, num2, num3 = cal(result9, query9)
finaldcg.append(num1)
finalidcg.append(num2)
finalndcg.append(num3)
num1, num2, num3 = cal(result10, query10)
finaldcg.append(num1)
finalidcg.append(num2)
finalndcg.append(num3)
print(finaldcg)
print(finalidcg)
print(finalndcg)

# b = 0.65
result1 = [243, 411, 578, 335, 112, 515, 775, 122, 706, 104]
result2 = [595, 760, 540, 817, 508, 497, 759, 8, 607, 293]
result3 = [360, 698, 641, 93, 735, 284, 115, 637, 841, 677]
result4 = [524, 185, 580, 350, 151, 784, 463, 753, 537, 263]

result5 = [616, 560, 359, 124, 765, 13, 676, 95, 834, 727]
result6 = [880, 914, 416, 245, 920, 668, 274, 931, 734, 54]
result7 = [465, 163, 625, 385, 80, 588, 768, 733, 164, 411]
result8 = [239, 381, 749, 651, 590, 60, 288, 809, 330, 132]
result9 = [229, 321, 430, 39, 288, 590, 60, 104, 698, 360]
result10 = [140, 120, 859, 928, 128, 955, 938]
finaldcg = []
finalidcg = []
finalndcg = []        
num1, num2, num3 = cal(result1, query1)
finaldcg.append(num1)
finalidcg.append(num2)
finalndcg.append(num3)
num1, num2, num3 = cal(result2, query2)
finaldcg.append(num1)
finalidcg.append(num2)
finalndcg.append(num3)
num1, num2, num3 = cal(result3, query3)
finaldcg.append(num1)
finalidcg.append(num2)
finalndcg.append(num3)
num1, num2, num3 = cal(result4, query4)
finaldcg.append(num1)
finalidcg.append(num2)
finalndcg.append(num3)
num1, num2, num3 = cal(result5, query5)
finaldcg.append(num1)
finalidcg.append(num2)
finalndcg.append(num3)
num1, num2, num3 = cal(result6, query6)
finaldcg.append(num1)
finalidcg.append(num2)
finalndcg.append(num3)
num1, num2, num3 = cal(result7, query7)
finaldcg.append(num1)
finalidcg.append(num2)
finalndcg.append(num3)
num1, num2, num3 = cal(result8, query8)
finaldcg.append(num1)
finalidcg.append(num2)
finalndcg.append(num3)
num1, num2, num3 = cal(result9, query9)
finaldcg.append(num1)
finalidcg.append(num2)
finalndcg.append(num3)
num1, num2, num3 = cal(result10, query10)
finaldcg.append(num1)
finalidcg.append(num2)
finalndcg.append(num3)
print(finaldcg)
print(finalidcg)
print(finalndcg)

# b = 0.7
result1 = [243, 411, 578, 335, 112, 515, 775, 122, 104, 706]
result2 = [595, 760, 817, 540, 508, 759, 497, 8, 607, 293]
result3 = [360, 698, 641, 93, 735, 841, 284, 115, 677, 190]
result4 = [524, 185, 580, 350, 151, 463, 753, 784, 537, 263]

result5 = [616, 560, 124, 359, 13, 765, 676, 95, 834, 727]
result6 = [880, 914, 416, 245, 920, 274, 668, 734, 931, 54]
result7 = [465, 163, 625, 385, 733, 80, 588, 768, 164, 411]
result8 = [239, 381, 749, 651, 132, 330, 600, 590, 60, 288]
result9 = [229, 321, 39, 430, 104, 590, 288, 60, 698, 360]
result10 = [140, 120, 859, 928, 128, 955, 938]
finaldcg = []
finalidcg = []
finalndcg = []        
num1, num2, num3 = cal(result1, query1)
finaldcg.append(num1)
finalidcg.append(num2)
finalndcg.append(num3)
num1, num2, num3 = cal(result2, query2)
finaldcg.append(num1)
finalidcg.append(num2)
finalndcg.append(num3)
num1, num2, num3 = cal(result3, query3)
finaldcg.append(num1)
finalidcg.append(num2)
finalndcg.append(num3)
num1, num2, num3 = cal(result4, query4)
finaldcg.append(num1)
finalidcg.append(num2)
finalndcg.append(num3)
num1, num2, num3 = cal(result5, query5)
finaldcg.append(num1)
finalidcg.append(num2)
finalndcg.append(num3)
num1, num2, num3 = cal(result6, query6)
finaldcg.append(num1)
finalidcg.append(num2)
finalndcg.append(num3)
num1, num2, num3 = cal(result7, query7)
finaldcg.append(num1)
finalidcg.append(num2)
finalndcg.append(num3)
num1, num2, num3 = cal(result8, query8)
finaldcg.append(num1)
finalidcg.append(num2)
finalndcg.append(num3)
num1, num2, num3 = cal(result9, query9)
finaldcg.append(num1)
finalidcg.append(num2)
finalndcg.append(num3)
num1, num2, num3 = cal(result10, query10)
finaldcg.append(num1)
finalidcg.append(num2)
finalndcg.append(num3)
print(finaldcg)
print(finalidcg)
print(finalndcg)
# b = 0.75

result1 = [243, 411, 578, 335, 112, 515, 775, 122, 104, 372]
result2 = [595, 760, 817, 540, 508, 759, 497, 8, 607, 293]
result3 = [360, 698, 641, 93, 735, 841, 284, 115, 677, 190]
result4 = [524, 185, 580, 350, 151, 753, 463, 784, 457, 537]

result5 = [616, 560, 124, 13, 765, 359, 676, 95, 834, 727]
result6 = [880, 914, 416, 245, 920, 274, 668, 734, 931, 54]
result7 = [465, 163, 385, 625, 733, 588, 80, 768, 243, 411]
result8 = [749, 239, 381, 651, 600, 330, 132, 590, 288, 60]
result9 = [321, 229, 39, 430, 104, 590, 288, 60, 698, 360]
result10 = [140, 120, 859, 928, 128, 955, 938]
finaldcg = []
finalidcg = []
finalndcg = []        
num1, num2, num3 = cal(result1, query1)
finaldcg.append(num1)
finalidcg.append(num2)
finalndcg.append(num3)
num1, num2, num3 = cal(result2, query2)
finaldcg.append(num1)
finalidcg.append(num2)
finalndcg.append(num3)
num1, num2, num3 = cal(result3, query3)
finaldcg.append(num1)
finalidcg.append(num2)
finalndcg.append(num3)
num1, num2, num3 = cal(result4, query4)
finaldcg.append(num1)
finalidcg.append(num2)
finalndcg.append(num3)
num1, num2, num3 = cal(result5, query5)
finaldcg.append(num1)
finalidcg.append(num2)
finalndcg.append(num3)
num1, num2, num3 = cal(result6, query6)
finaldcg.append(num1)
finalidcg.append(num2)
finalndcg.append(num3)
num1, num2, num3 = cal(result7, query7)
finaldcg.append(num1)
finalidcg.append(num2)
finalndcg.append(num3)
num1, num2, num3 = cal(result8, query8)
finaldcg.append(num1)
finalidcg.append(num2)
finalndcg.append(num3)
num1, num2, num3 = cal(result9, query9)
finaldcg.append(num1)
finalidcg.append(num2)
finalndcg.append(num3)
num1, num2, num3 = cal(result10, query10)
finaldcg.append(num1)
finalidcg.append(num2)
finalndcg.append(num3)
print(finaldcg)
print(finalidcg)
print(finalndcg)
'''

result1 = [243, 411, 578, 335, 112, 515, 775, 122, 104, 372]
result2 = [595, 760, 817, 540, 508, 759, 497, 8, 607, 293]
result3 = [360, 698, 641, 93, 735, 841, 284, 115, 677, 190]
result4 = [524, 185, 580, 350, 151, 753, 463, 784, 457, 537]

result5 = [616, 560, 124, 13, 765, 359, 676, 95, 834, 727]
result6 = [880, 914, 416, 245, 920, 274, 668, 734, 931, 54]
result7 = [465, 163, 385, 625, 733, 588, 80, 768, 243, 411]
result8 = [749, 239, 381, 651, 600, 330, 132, 590, 288, 60]
result9 = [321, 229, 39, 430, 104, 590, 288, 60, 698, 360]
result10 = [140, 120, 859, 928, 128, 955, 938]
finaldcg = []
finalidcg = []
finalndcg = []        
num1, num2, num3 = cal(result1, query1)
finaldcg.append(num1)
finalidcg.append(num2)
finalndcg.append(num3)
num1, num2, num3 = cal(result2, query2)
finaldcg.append(num1)
finalidcg.append(num2)
finalndcg.append(num3)
num1, num2, num3 = cal(result3, query3)
finaldcg.append(num1)
finalidcg.append(num2)
finalndcg.append(num3)
num1, num2, num3 = cal(result4, query4)
finaldcg.append(num1)
finalidcg.append(num2)
finalndcg.append(num3)
num1, num2, num3 = cal(result5, query5)
finaldcg.append(num1)
finalidcg.append(num2)
finalndcg.append(num3)
num1, num2, num3 = cal(result6, query6)
finaldcg.append(num1)
finalidcg.append(num2)
finalndcg.append(num3)
num1, num2, num3 = cal(result7, query7)
finaldcg.append(num1)
finalidcg.append(num2)
finalndcg.append(num3)
num1, num2, num3 = cal(result8, query8)
finaldcg.append(num1)
finalidcg.append(num2)
finalndcg.append(num3)
num1, num2, num3 = cal(result9, query9)
finaldcg.append(num1)
finalidcg.append(num2)
finalndcg.append(num3)
num1, num2, num3 = cal(result10, query10)
finaldcg.append(num1)
finalidcg.append(num2)
finalndcg.append(num3)
print(finaldcg)
print(finalidcg)
print(finalndcg)


