# -*- coding: utf-8 -*-
"""
Created on Thu Jan 28 22:32:29 2016

@author: 洪浚皓＆陳博允
"""
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

from PIL import Image
img = Image.open("image1.png")

obs=[]
for colory in range (0,300,1):
    for colorx in range (0,400,1):
        rgb = img.getpixel((colorx,colory))
        #if rgb != (255,255,255):
        if rgb == (0,0,0):
            a = colorx*1000 + colory
            obs = obs + [a]

#print(obstacle)
ob = []

u=0
v=0
w=0
x=0
#-----------找障礙物頂點座標--------------------------------------------------------
for i in range (0, len(obs),1):
    u=obs[i]+1000
    v=obs[i]-1000
    w=obs[i]+1
    x=obs[i]-1
    b=obs[i]
    
    if ((((u not in obs) or (v not in obs)) and ((w not in obs) or (x not in obs))) == 1):
        ob = ob + [b]
#-----------找障礙物頂點座標--------------------------------------------------------
        
#------------------判斷有幾個障礙物--------------------------------------------------        
obstacle = {}
for ii in range (0, len(ob)/4,1):
    obstacle.update({ii:[]})
#------------------判斷有幾個障礙物-------------------------------------------------- 


#---------------判斷打幾個點屬於同一個障礙物------------------------------------------
def CanMakeRact(i_1,i_2,i_3,i_4):
    if (i_1 + i_2 == i_3 +i_4) or(i_1 +i_3 == i_2 +i_4) or (i_1 + i_4 == i_2 + i_3):
        return 0
jj = 0
for j_1 in range (0, len(ob), 1):
    for j_2 in range (j_1+1, len(ob), 1):
        for j_3 in range (j_2+1, len(ob), 1):
            for j_4 in range (j_3+1, len(ob), 1):
                if (CanMakeRact(ob[j_1],ob[j_2],ob[j_3],ob[j_4]) == 0):
                    obstacle[jj] = obstacle[jj]+[ob[j_1],ob[j_2],ob[j_3],ob[j_4]]
                    jj+=1
#---------------判斷哪幾個點屬於同一個障礙物------------------------------------------
                    

#----------------找出路徑點----------------------------------
               

for t_1 in range (0,len(ob)/4,1):
    obstacle[t_1].append(obstacle[t_1].pop(2))   #左上→右上→右下→左下→左上
    obstacle[t_1].append(obstacle[t_1][0])
    
    obstacle[t_1][0] = obstacle[t_1][0] - 10*1000 - 10
    obstacle[t_1][1] = obstacle[t_1][1] + 10*1000 - 10
    obstacle[t_1][2] = obstacle[t_1][2] + 10*1000 + 10
    obstacle[t_1][3] = obstacle[t_1][3] - 10*1000 + 10
    obstacle[t_1][4] = obstacle[t_1][4] - 10*1000 - 10


#----------------找出路徑點----------------------------------



for q_1 in range (0, len(ob)/4, 1):
    for q_2 in range (0, 100, 1):
        if (obstacle[q_1][q_2] - obstacle[q_1][q_2 + 1]) > 20:
            if ((obstacle[q_1][q_2] - obstacle[q_1][q_2 + 1])/1000) > 20:
                obstacle[q_1].insert(q_2 + 1, obstacle[q_1][q_2] - (20*1000))
            if ((obstacle[q_1][q_2] - obstacle[q_1][q_2 + 1])%1000) != 0:
                obstacle[q_1].insert(q_2 + 1, obstacle[q_1][q_2] -20)
        if (obstacle[q_1][q_2] - obstacle[q_1][q_2 + 1]) < -20:
            if ((obstacle[q_1][q_2] - obstacle[q_1][q_2 + 1])/1000) < -20:
                obstacle[q_1].insert(q_2 + 1, obstacle[q_1][q_2] + (20*1000))
            if ((obstacle[q_1][q_2] - obstacle[q_1][q_2 + 1])%1000) != 0:
                obstacle[q_1].insert(q_2 + 1, obstacle[q_1][q_2] + 20)
        if obstacle[q_1][q_2 +1 ] in obstacle[q_1]:
            q_2 += 1
        if obstacle[q_1][q_2]-obstacle[q_1][0] < 20:
            break
        
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

ver = {
        0:[],	1:[],	      2:[],	      3:[], 	4:[],  	5:[],  	6:[],  	7:[],  	8:[],  	9:[],  	10:[],	11:[],	12:[],	13:[],	14:[],	15:[],	16:[],	17:[],	18:[],	19:[],
        100:[],	101:[],	102:[],	103:[],	104:[],	105:[],	106:[],	107:[],	108:[],	109:[],	110:[],	111:[],	112:[],	113:[],	114:[],	115:[],	116:[],	117:[],	118:[],	119:[],
        200:[],	201:[],	202:[],	203:[],	204:[],	205:[],	206:[],	207:[],	208:[],	209:[],	210:[],	211:[],	212:[],	213:[],	214:[],	215:[],	216:[],	217:[],	218:[],	219:[],
        300:[],	301:[],	302:[],	303:[],	304:[],	305:[],	306:[],	307:[],	308:[],	309:[],	310:[],	311:[],	312:[],	313:[],	314:[],	315:[],	316:[],	317:[],	318:[],	319:[],
        400:[],	401:[],	402:[],	403:[],	404:[],	405:[],	406:[],	407:[],	408:[],	409:[],	410:[],	411:[],	412:[],	413:[],	414:[],	415:[],	416:[],	417:[],	418:[],	419:[],
        500:[],	501:[],	502:[],	503:[],	504:[],	505:[],	506:[],	507:[],	508:[],	509:[],	510:[],	511:[],	512:[],	513:[],	514:[],	515:[],	516:[],	517:[],	518:[],	519:[],
        600:[],	601:[],	602:[],	603:[],	604:[],	605:[],	606:[],	607:[],	608:[],	609:[],	610:[],	611:[],	612:[],	613:[],	614:[],	615:[],	616:[],	617:[],	618:[],	619:[],
        700:[],	701:[],	702:[],	703:[],	704:[],	705:[],	706:[],	707:[],	708:[],	709:[],	710:[],	711:[],	712:[],	713:[],	714:[],	715:[],	716:[],	717:[],	718:[],	719:[],
        800:[],	801:[],	802:[],	803:[],	804:[],	805:[],	806:[],	807:[],	808:[],	809:[],	810:[],	811:[],	812:[],	813:[],	814:[],	815:[],	816:[],	817:[],	818:[],	819:[],
        900:[],	901:[],	902:[],	903:[],	904:[],	905:[],	906:[],	907:[],	908:[],	909:[],	910:[],	911:[],	912:[],	913:[],	914:[],	915:[],	916:[],	917:[],	918:[],	919:[],
        1000:[],	1001:[],	1002:[],	1003:[],	1004:[],	1005:[],	1006:[],	1007:[],	1008:[],	1009:[],	1010:[],	1011:[],	1012:[],	1013:[],	1014:[],	1015:[],	1016:[],	1017:[],	1018:[],	1019:[],
        1100:[],	1101:[],	1102:[],	1103:[],	1104:[],	1105:[],	1106:[],	1107:[],	1108:[],	1109:[],	1110:[],	1111:[],	1112:[],	1113:[],	1114:[],	1115:[],	1116:[],	1117:[],	1118:[],	1119:[],
        1200:[],	1201:[],	1202:[],	1203:[],	1204:[],	1205:[],	1206:[],	1207:[],	1208:[],	1209:[],	1210:[],	1211:[],	1212:[],	1213:[],	1214:[],	1215:[],	1216:[],	1217:[],	1218:[],	1219:[],
        1300:[],	1301:[],	1302:[],	1303:[],	1304:[],	1305:[],	1306:[],	1307:[],	1308:[],	1309:[],	1310:[],	1311:[],	1312:[],	1313:[],	1314:[],	1315:[],	1316:[],	1317:[],	1318:[],	1319:[],
        1400:[],	1401:[],	1402:[],	1403:[],	1404:[],	1405:[],	1406:[],	1407:[],	1408:[],	1409:[],	1410:[],	1411:[],	1412:[],	1413:[],	1414:[],	1415:[],	1416:[],	1417:[],	1418:[],	1419:[],

        }



i = 0
j = 0


#陣列裡面的順序是會影響支撐樹的喔
for i in range (0, 1500, 100):                             # Y方向灑格點
    for j in range (0, 20, 1):                             # X方向灑格點
        if i+j < 20:
            ver[i+j] = ver[i+j] + [i+j-1, i+j+1, i+j+100]
        elif i == 1400:
            ver[i+j] = ver[i+j] + [i+j-100, i+j-1, i+j+1]
        elif (i+j)%100 == 0:
            ver[i+j] = ver[i+j] + [i+j-100, i+j+1, i+j+100]
        elif (i+j)%100 == 19:
            ver[i+j] = ver[i+j] + [i+j-100, i+j-1, i+j+100]
        else:
            ver[i+j] = ver[i+j] + [i+j-100, i+j-1, i+j+1, i+j+100]

ver.update({0 :[1, 100],
            19 :[18, 119],
            1400 :[1300, 1401],
            1419 :[1319, 1418]})
print(ver)



from PIL import Image
img = Image.open("image1.png")           # 400X300 px

def remove_value(graph, vertex, edge):        #定義一個函式把邊去掉
    if edge in graph[vertex]:
        graph[vertex].remove(edge)
    return graph

is_it_white = 0
i = -9
no_obstacles = []
obstacles = []
mixed = []
a = 0

for colory in range(29, 309, 20):
    for colorx in range(29, 409, 20):
        is_it_white = 0
        for i in range(-9, 11, 1):                   #判斷網格是哪種類型
            rgb = img.getpixel((colorx-i,colory-i))  #檢查對角線就好(第一條對角線)
            if rgb != (255, 255, 255):
                is_it_white += 0
            else:
                is_it_white += 1

            rgb = img.getpixel((colorx-i,colory+i))  #檢查對角線就好(第二條對角線)
            if rgb != (255, 255, 255):
                is_it_white += 0
            else:
                is_it_white += 1

        if is_it_white == 40:                               #把網格類型分類
            a = ((colory-9)/20)*100 + (colorx-9)/20
            no_obstacles = no_obstacles + [a]
        elif (is_it_white > 0) and (is_it_white < 40) :
            a = ((colory-9)/20)*100 + (colorx-9)/20
            mixed = mixed + [a]
        elif is_it_white == 0:
            a = ((colory-9)/20)*100 + (colorx-9)/20
            obstacles = obstacles + [a]



i = 0
j = 0
u = 0
v = 0

for i in range (0, 1500, 100):                             
    for j in range (0, 20, 1):                                
        if (i + j) in obstacles :               #有障礙物的點︰                                        
            ver.update({(i + j):[]})            #把有障礙物中的點裡面的邊清空            
            for u in range (0, 1500, 100):      #把其他所有的點去掉有障礙物的邊                             
                for v in range (0, 20, 1):
                    remove_value(ver,(u+v), (i+j))
        elif (i + j) in mixed :                 #混和部份的點︰
            ver.update({(i + j):[]})            #把有障礙物中的點裡面的邊清空            
            for u in range (0, 1500, 100):      #把其他所有的點去掉有障礙物的邊                             
                for v in range (0, 20, 1):
                    remove_value(ver,(u+v), (i+j))

graph = ver
print(graph)

#---深度優先搜尋法---
def iterative_dfs(graph, start, path=[]):
  '''iterative depth first search from start'''
  q=[start]
  while q:
    v=q.pop(0)
    if v not in path:
      path=path+[v]
      q=graph[v]+q
  return path
#---深度優先搜尋法---

"""↓↓↓↓↓ 2016/02/14的時候這部份只有我跟上帝看得懂，今天只有上帝看的懂了QQ"""
dfs = iterative_dfs(graph, 00) #做出回樹幹的路
path = dfs
last = path[len(path)-1]

def dis(x_1, x_2):
    x = 0
    y = 0
    x = (x_1/100) - (x_2/100)
    y = (x_1%100) - (x_2%100)
    return x*x + y*y
    
r = 0    
for i in range (0, 1000, 1):
    check = 0
    if dfs[i] == last:
        break
    if ((((dfs[i] - dfs[i+1] == 100) or (dfs[i] - dfs[i+1] == -100)) or ((dfs[i] - dfs[i+1] == 1) or (dfs[i] - dfs[i+1] == -1))) == 0) :
        r = dis(dfs[i],dfs[i+1])
        if (dfs[i]+1 in dfs) and dis(dfs[i]+1,dfs[i+1])< r and (check == 0) and (dfs[i] + 1 != dfs[i-1]):
            dfs.insert(i+1,dfs[i]+1)
            i += 1
            check=1
        if (dfs[i]+100 in dfs) and dis(dfs[i]+100,dfs[i+1])< r and (check == 0) and (dfs[i] + 100 != dfs[i-1]):
            dfs.insert(i+1,dfs[i]+100)
            i += 1
            check=1
        if (dfs[i]-1 in dfs) and dis(dfs[i]-1,dfs[i+1])< r and (check == 0) and (dfs[i] - 1 != dfs[i-1]):
            dfs.insert(i+1,dfs[i]-1)
            i += 1
            check=1
        if (dfs[i]-100 in dfs) and dis(dfs[i]-100,dfs[i+1])< r and (check == 0) and (dfs[i] - 100 != dfs[i-1]):
            dfs.insert(i+1,dfs[i]-100)
            i += 1
            check=1
        if (dfs[i]+1 in dfs) and check == 0:
            dfs.insert(i+1,dfs[i]+1)
            i += 1
            check=1
        if (dfs[i]+100 in dfs) and check == 0:
            dfs.insert(i+1,dfs[i]+100)
            i += 1
            check=1
        if (dfs[i]-1 in dfs) and check == 0:
            dfs.insert(i+1,dfs[i]-1)
            i += 1
            check=1
        if (dfs[i]-100 in dfs) and check == 0:
            dfs.insert(i+1,dfs[i]-100)
            i += 1
            check=1
        

for uu in range (0, len(dfs),1):
    ch_x = ((dfs[uu]%100)*20) +10 
    ch_y = ((dfs[uu]/100)*20) +10
    dfs[uu] = ch_x*1000 + ch_y       
    
    
check=[]
for lock in range (0, len(ob)/4, 1):
    check = check + [0]
    
    
def Distance(point_1,point_2):
    point_1_x = point_1/1000
    point_1_y = point_1%1000
    point_2_x = point_2/1000
    point_2_y = point_2%1000
    
    if ((((point_1_x - point_2_x)*(point_1_x - point_2_x)) + ((point_1_y - point_2_y)*(point_1_y - point_2_y))) <= 400):
        return 0
    else:
        return 1
        

   
#check_1=[]
#k= len(dfs)
#dis =[]
for iii in range (0, len(dfs), 1):
    for jjj in range (0,len(ob)/4, 1):
        #dis = dis + [Distance(dfs[iii], obstacle[jjj][0])]
        if ((Distance(dfs[iii],obstacle[jjj][0]) == 0) and (check[jjj] == 0)):
           for kkk in range (0, len(obstacle[jjj]), 1):
                dfs.insert(iii+kkk+1, obstacle[jjj][kkk])
                #ckeck_1 = check_1 + [1]
                check[jjj] = 1        
    
#===============把原本一次走一格改成一次走1 pixel========================
    
i = 0
j = 0
k = 0
m = len(dfs) - 2

while i <= m:
#for i in range (0, len(dfs), 1):
    if abs(dfs[i+1] - dfs[i]) == 20000 :    #這裡要先知道哪個格子是走在X座標。
        if dfs[i+1] - dfs[i] == 20000:      #判斷這是往上面走。
            while k < 19:                   #在一格內，把要往上面走一個像素的座標
                j = dfs[i] + 1000           #全部收集起來     
                dfs.insert(i+1, j)
                k = k + 1
                i = i + 1
        else:                               #其他的就是往下面走
            while k < 19:
                j = dfs[i] - 1000                
                dfs.insert(i+1, j)          #在一格內，把要往上面走一個像素的座標
                k = k + 1                   #全部收集起來
                i = i + 1
        i = 0
        j = 0
        k = 0
    else:
        pass
    
    m = len(dfs)
    
    if i == m-2:                            #做一個if，不然會超出LIST的長度
        break
    else:
        m = len(dfs)
        i = i + 1


i = 0
m = len(dfs) - 2

while i <= m:                               
#for i in range (0, len(dfs), 1):       
    if abs(dfs[i+1] - dfs[i]) == 20:        #這裡要先知道哪個格子是走在Y座標。
        if dfs[i+1] - dfs[i] == 20:         #判斷這是往上面走。        
            while k < 19:                   #在一格內，把要往上面走一個像素的座標
                j = dfs[i] + 1              #全部收集起來   
                dfs.insert(i+1, j)
                k = k + 1
                i = i + 1
        else:                               #其他的就是往下面走
            while k < 19:
                j = dfs[i] - 1                
                dfs.insert(i+1, j)          #在一格內，把要往上面走一個像素的座標
                k = k + 1                   #全部收集起來
                i = i + 1
        i = 0
        j = 0
        k = 0
    else:
        pass
    m = len(dfs)
    
    if i == m-2:                            #做一個if，不然會超出LIST的長度
        break
    else:
        m = len(dfs)
        i = i + 1

        

#===============把原本一次走一格改成一次走1 pixel========================

import matplotlib.pyplot as plt
from PIL import Image

#img = Image.open("image1.png")
for rr in range (0, len(dfs),1):
    img = Image.open("image1.png")
    for color_x in range ((dfs[rr]/1000)-10, (dfs[rr]/1000)+10, 1):
        for color_y in range ((dfs[rr]%1000)-10,(dfs[rr]%1000)+10, 1):
            
            if (((color_x-(dfs[rr]/1000))*(color_x-(dfs[rr]/1000))+ (color_y-(dfs[rr]%1000))*(color_y-(dfs[rr]%1000))) <= 100):
                img.putpixel((color_x, color_y), (78, 128, 210))

    a = str(rr)
    name = "image_" + a + ".png"
    img.save(name)        
