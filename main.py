mport csv           
import random               
import copy          
                 
f=open("question2.csv","r",encoding="utf-8")
                                
reader=csv.reader(f)
qarray=[]
count1=0

for row in reader:
    qarray.append(row)   
    count1+=1

del qarray[0]
count1=count1-1   #CSVの第一行を削除

f.close()

countlist=[]
alist=[]
                                                                 
while True:

    try:                                                                                                                                                                                                                           
        a=random.randint(0,count1-1)   #第何問を選ぶか選択
#    alist.append(str(qarray[a][0]))

        if len(qarray[a][3])==1:            #一択問題であったら

            try:

                print(qarray[a][1])         
                x=int(input(qarray[a][2]+" >>"))
                
            except ValueError:
                print("正しい値を入力してください")
                print("")
                continue
                                      
            if x==int(qarray[a][3]):
                print("正解です！")
                print("")
                count1=count1-1
                del qarray[a]

                if len(qarray)<=0:       #問題が無くなったら終了
                    break


            else:
                print("不正解です")
                print("")
                continue

        elif len(qarray[a][3])==3:       #2択問題であったら

            try:
                print(qarray[a][1])
                x=str(input(qarray[a][2]+">>"))

            except ValueError:
                print("正しい数値を入力してください。")
                print("")
                continue
                                                        #入力値からコンマ除去
            ar=x.split(",")
            x_nocomma="".join(ar)
            if len(x_nocomma) > 2:  #解答した番号が3個以上なら無効
                print("正しい数値を入力してください")

            for c in x_nocomma:
                if x_nocomma.count(c)!=1 :  #同じ番号が２つ以上あったら無効
                    continue

            count_match = 0
            for c in x_nocomma:
                if c in qarray[a][3]:
                    count_match+=1

            if count_match==2:

                print("正解です！")
                print("")
                count1=count1-1
                del qarray[a]

                if len(qarray)<=0:
                    break

            else:
                print("不正解です")
                print("")
                continue

        elif len(qarray[a][3])==5:     #3択問題であったら
                             
            try:
                print(qarray[a][1])
                x=str(input(qarray[a][2]+" >>"))
                                                                                                            
            except ValueError:
                print("正しい数値を入力してください。")
                print("")
                continue

            ar = x.split(",")
            x_nocomma = "".join(ar)
            if len(x_nocomma) > 3:  # 解答した番号が4個以上なら無効
                print("正しい数値を入力してください")

            for c in x_nocomma:
                if x_nocomma.count(c) != 1:  # 同じ番号が２つ以上あったら無効
                    continue

            count_match = 0
            for c in x_nocomma:
                if c in qarray[a][3]:
                    count_match += 1

            if count_match==3:
                print("正解です！")
                print("")
                count1=count1-1
                del qarray[a]

                if len(qarray)<=0:    #問題がなくなったら終了
                    break
            else:
                print("不正解です")
                print("")
                continue

    except:
        continue

print("お疲れ様でした！")
