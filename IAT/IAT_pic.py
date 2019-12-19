#coding:utf-8
from __future__ import division
from __future__ import unicode_literals
from psychopy import visual, event, core, sound, gui
import random
import codecs

### 実験によって異なる部分 ###

##概念対A-B
# 概念A(写真を使用)
A_concept="概念1"
A_words=["写真.png","写真.png","写真.png","写真.png","写真.png"]# "xxx.png"と書く（変更点）
# 概念B
B_concept="概念2"
B_words=["写真.png","写真.png","写真.png","写真.png","写真.png"]

# 概念対ABの繰り返し数（変更点）
repeat_AB = 1 #整数

# 概念X
X_concept="概念3"
X_words=["言葉","","",""]
# 概念Y
Y_concept="概念4"
Y_words=["言葉","","",""]

# 概念対XYの繰り返し数（変更点）
repeat_XY = 1 #整数
repeat_all_practice = 1 # 連合ブロック練習の繰り返し数
repeat_all = 1 #連合ブロック本番の繰り返し数



# 参加者情報
param_dict={"subj_num":"","gender":["female","male"],"age":"","counter_balance":["CB1","CB2"]}
dlg=gui.DlgFromDict(param_dict,title=".. + * * INFORMATION * * + ..")
if dlg.OK==False:
    core.quit()


# 画面情報・時間情報
win=visual.Window(fullscr=True, monitor="testMonitor", units="deg",color="gray")
clock=core.Clock()

# カーソルを消す
event.Mouse(visible=False)

# サウンド
sound=sound.Sound("A",secs=0.5)

# データファイル
fn_IAT=param_dict["subj_num"] +"_"+ param_dict["gender"] +"_"+ param_dict["age"] +"_"+ param_dict["counter_balance"]+"_IAT"+ ".csv"
datafile=codecs.open(fn_IAT,"w","shift-JIS")
# 左の列から、ブロック番号、一つの刺激に対する誤答回数、反応時間、そのブロックでは左右のどちらに分類したか、刺激単語がどの概念に含まれるか、刺激単語は何かをデータファイルに出力
datafile.write("block,error_num,RT,L_R,word_concept,stim\n")


#設計(CB1: CB2はABが逆転)
#1 A-B
#2 X-Y
#3 AX-BY(practice) -> #4 AX-BY
#5 B-A
#6 BX-AY(practice) -> #7 BX-AY
#
#刺激単語
#group A
#A_words
#group B
#B_words
## group A&B
AB_words=A_words+B_words

#group X
#X_words
#group Y
#Y_words
#group X&Y
XY_words=X_words+Y_words

# all words for association
All_words_practice=AB_words+XY_words
All_words=AB_words+XY_words

#repetition
AB_words *=repeat_AB
XY_words *=repeat_XY

#連合ブロックの練習繰り返し数を2回とする
All_words_practice *=repeat_all_practice

#連合ブロックの繰り返し数は4回
All_words *=repeat_all


#教示文
IAT=visual.TextStim(win,"単語分類課題",font="ipagothic",pos=(0,0),height=3.0)
ready=visual.TextStim(win,text="READY?",font="Alial",color="white",pos=(0,0),height=2.7)
press=visual.TextStim(win,text="press 'SPACE' key",font="Alial",color="white",pos=(0,-5),height=2.0)
prac=visual.TextStim(win,text="練習",font="ipagothic",color="yellow",pos=(0,5),height=2.7)
crucial=visual.TextStim(win,text="本番",font="ipagothic",color="yellow",pos=(0,5),height=2.7)
thankyou=visual.TextStim(win,text="Thank you!\n Please call the experimenter:)",color="yellow",font="Alial",pos=(0,0),height=2.0)

#刺激 及び 対概念
#------------------------------

if param_dict["counter_balance"]=="CB1":
    upLeft=(-15,10)
    upRight=(15,10)
    E="e"
    I="i"
    R="right"
    L="left"
elif param_dict["counter_balance"]=="CB2":
    upLeft=(15,10)
    upRight=(-15,10)
    E="i"
    I="e"
    R="left"
    L="right"

underLeft=(-15,6)
underRight=(15,6)

concept_A=visual.TextStim(win,text=A_concept,font="ipagothic",color="skyblue",height=2.7) #pos=(-10,10) or (10,10)
concept_B=visual.TextStim(win,text=B_concept,font="ipagothic",color="skyblue",height=2.7)  #pos=(10,10) or (-10,10)
concept_X=visual.TextStim(win,text=X_concept,font="ipagothic",color="lightgreen",height=2.7)  #pos=(-10, 6) or (10, 6)
concept_Y=visual.TextStim(win,text=Y_concept, font="ipagothic",color="lightgreen",height=2.7)#pos=(10, 6) or (-10, 6)

stim01=visual.ImageStim(win,size=(8,8),pos=(0,0))
stim02=visual.TextStim(win,font="ipagothic",color="lightgreen",pos=(0,0),height=3.0)

fix=visual.TextStim(win,text="+",font="ipagothic",color="white",pos=(0,0),height=3.0)
false=visual.TextStim(win,text="×",font="ipagothic",color="red",pos=(0,0),height=3.0)
#--------------------------------

#------------------------------------------------------------------------
#                     #実験開始
#------------------------------------------------------------------------

IAT.draw()
press.draw()
win.flip()
event.waitKeys()


for block in range(1,8):
    # shuffle
    random.shuffle(AB_words)
    random.shuffle(XY_words)
    random.shuffle(All_words_practice)
    random.shuffle(All_words)
    
    if block in [1,3,4]:
        concept_A.setPos(upLeft)
        concept_B.setPos(upRight)
        words=AB_words
        if block in [3,4]:
            concept_X.setPos(underLeft)
            concept_Y.setPos(underRight)
            if block==3:
                words=All_words_practice
            elif block==4:
                words=All_words
    elif block in [5,6,7]:
        concept_A.setPos(upRight)
        concept_B.setPos(upLeft)
        words=AB_words
        if block in [6,7]:
            concept_X.setPos(underLeft)
            concept_Y.setPos(underRight)
            if block ==6:
                words=All_words_practice
            elif block == 7:
                words=All_words
    elif block == 2:
        words=XY_words
        concept_X.setPos(underLeft)
        concept_Y.setPos(underRight)    
    
    if block in [1,5]:
        concept_A.draw()
        concept_B.draw()
    elif block in [2]:
        concept_X.draw()
        concept_Y.draw()
    else:
        concept_A.draw()
        concept_B.draw()
        concept_X.draw()
        concept_Y.draw()
        if block in [3,6]:
            prac.draw()
        elif block in [4,7]:
            crucial.draw()
    ready.draw()
    press.draw()
    win.flip()
    event.waitKeys(keyList=["space"])
    
    
    if block in [1,5]:
        concept_A.draw()
        concept_B.draw()
    elif block in [2]:
        concept_X.draw()
        concept_Y.draw()
    else:
        concept_A.draw()
        concept_B.draw()
        concept_X.draw()
        concept_Y.draw()
    fix.draw()
    win.flip()
    core.wait(1.0)
    
    for word in words:
        
        if word in AB_words:
            stim01.setImage(word)
        elif word in XY_words:
            stim02.setText(word)
        
        waiting_keypress=True
        event.getKeys()
        clock.reset()
        while waiting_keypress:
            if block in [1,5]:
                concept_A.draw()
                concept_B.draw()
                stim01.draw()
            elif block in [2]:
                concept_X.draw()
                concept_Y.draw()
                stim02.draw()
            else:
                concept_A.draw()
                concept_B.draw()
                concept_X.draw()
                concept_Y.draw()
                if word in AB_words:
                    stim01.draw()
                elif word in XY_words:
                    stim02.draw()
            win.flip()
            
            if block in [1,2,3,4]:
                if word in A_words:
                    stim_kind, correct_key,way="A_words",E,L
                elif word in B_words:
                    stim_kind, correct_key,way="B_words",I,R
                elif word in X_words:
                    stim_kind, correct_key,way="X_words","e","left"
                elif word in Y_words:
                    stim_kind, correct_key,way="Y_words","i","right"
            elif block in [5,6,7]:
                if word in A_words:
                    stim_kind, correct_key,way="A_words",I,R
                elif word in B_words:
                    stim_kind, correct_key,way="B_words",E,L
                elif word in X_words:
                    stim_kind, correct_key,way="X_words","e","left"
                elif word in Y_words:
                    stim_kind, correct_key,way="Y_words","i","right"
                
            keys=event.getKeys(keyList=["e","i","escape"])  
            
            for key in keys:
                if "escape" in keys:
                    datafile.close()
                    core.quit()
                elif correct_key in keys:
                    datafile.write("block{},0,{:.5f},{},{},{}\n".format(block,clock.getTime()*1000,way,stim_kind,word))
                    datafile.flush()
                    waiting_keypress=False
                    break
                else:
                    if block in [1,5]:
                        concept_A.draw()
                        concept_B.draw()
                    elif block in [2]:
                        concept_X.draw()
                        concept_Y.draw()
                    else:
                        concept_A.draw()
                        concept_B.draw()
                        concept_X.draw()
                        concept_Y.draw()
                    false.draw()
                    win.flip()
                    core.wait(0.3)
                    datafile.write("block{},1,{:.5f},{},{},{}\n".format(block,clock.getTime()*1000,way,stim_kind,word))
                    datafile.flush()
                    waiting_keypress=False # 間違えたら終わり（変更点）
                    break
                    
            
        if block in [1,5]:
            concept_A.draw()
            concept_B.draw()
        elif block in [2]:
            concept_X.draw()
            concept_Y.draw()
        else:
            concept_A.draw()
            concept_B.draw()
            concept_X.draw()
            concept_Y.draw()
        fix.draw()
        win.flip()
        core.wait(0.25)

datafile.close()

#----------IAT終了----------
sound.play()
thankyou.draw()
win.flip()
event.waitKeys(keyList=["space"])
print("Done Experiment")


#----------D_score----------
import pandas as pd
import numpy as np
import glob

file = glob.glob(fn_IAT)


# データファイルを選択
file_mat=pd.read_csv(file[0],encoding="Shift-JIS")

## 使用するデータの形成
# 使用するブロックだけ抽出するための型
matA=np.zeros([len(file_mat),3])
matA[:,:]=np.nan
matA=pd.DataFrame(matA,columns=["block", "error","rt"])

# 使用するブロックのみのブロック番号、正誤、反応時間を抽出
for row in range(0,len(file_mat)):
    if file_mat.iloc[row,0] in ["block3","block4","block6","block7"]:
        for col in range(0,3):
            matA.iloc[row,col]=file_mat.iloc[row,col]

# 使用しないブロックを削除
matA=matA.dropna()
print("Datafile was selected.")

## 反応時間が300 ms未満の試行が10%以上ある参加者を排除
n=0
for i in range(0,len(matA)):
    if matA.iloc[i,2] < 300:
        n +=1
        matA.iloc[i,2]=np.nan
    elif matA.iloc[i,2] < 400: #400 ms未満の試行を削除
        matA.iloc[i,2] =np.nan
    elif matA.iloc[i,2] >= 10000: #10 s以上の試行を削除
        matA.iloc[i,2]=np.nan

under_300_sec= n/len(matA)*100
if under_300_sec >= 10:
    print("His/Her RT were too fast to use!!")
    print("Under 300 ms was "+str(round(under_300_sec,2)) + "%")
    D_score=np.nan
else: # 300 ms未満の反応時間が10 %未満だった場合は以下へ進む
    print("Calculating D-score...")
    print("Under 300 ms was only "+str(round(under_300_sec,2)) + "%")
    
    # D得点の計算
    # 平均や標準偏差を記入する表を作成
    matB=np.zeros([6,5])
    matB[:,:]=np.nan
    matB=pd.DataFrame(matB)
    matB.iloc[:,0]=["block3","block4","block6","block7","block3_6","block4_7"]
    
    # 計算対象をリストに挿入
    correct_b=[[],[],[],[],[],[]]
    for rowB in range(0,6):
        for rowA in range(0,len(matA)):
            if matA.iloc[rowA,0]==matB.iloc[rowB,0] and matA.iloc[rowA,1]==0.0:
                correct_b[rowB].append(matA.iloc[rowA,2])
    for rowB2 in range(0,2):
        correct_b[rowB2+4]=correct_b[rowB2]+correct_b[rowB2+2]
    
    # 対象ブロックそれぞれの平均値と標準偏差を算出
    for c_b_len in range(0,len(correct_b)):
        matB.iloc[c_b_len,1]=np.nanmean(correct_b[c_b_len])
        matB.iloc[c_b_len,2]=np.nanstd(correct_b[c_b_len])
    
    # 対ブロックの平均値+2*SDを算出
    for rowB in range(0,6):
        matB.iloc[rowB,3]=matB.iloc[rowB,1]+2*matB.iloc[rowB,2]
    
    # 誤答をそのブロックの平均値＋2SDに置換
    for rowA in range(0,len(matA)):
        for rowB in range(0,6):
            if matA.iloc[rowA,1] != 0.0 and matA.iloc[rowA,0]==matB.iloc[rowB,0]:
                matA.iloc[rowA,2]=matB.iloc[rowB,3]
    
    #置換した後の数値も含んでブロックごとに平均化
    b=[[],[],[],[],[],[]]
    for rowB in range(0,6):
        for rowA in range(0,len(matA)):
            if matA.iloc[rowA,0]==matB.iloc[rowB,0]:
                b[rowB].append(matA.iloc[rowA,2])
    
    # 置換も含めた平均を表に代入
    for len_b in range(0,len(b)):
        matB.iloc[len_b,4]=np.nanmean(b[len_b])
    
    #対ブロックの平均の差を対ブロックの標準偏差で割る
    # (BXAY - AXBY)/SD
    #2対の平均を D得点とする
    if param_dict["counter_balance"]=="CB1":
        D_score=np.mean([
        (matB.iloc[2,4]-matB.iloc[0,4])/matB.iloc[4,2],
        (matB.iloc[3,4]-matB.iloc[1,4])/matB.iloc[5,2]])
    else:
        D_score=np.mean([
        (matB.iloc[0,4]-matB.iloc[2,4])/matB.iloc[4,2],
        (matB.iloc[1,4]-matB.iloc[3,4])/matB.iloc[5,2]])

matC=np.zeros([1,6])
matC[:,:]=np.nan
matC=pd.DataFrame(matC,columns=["subj_num","sex","age","CB","under 300 ms(%)","D_score"])

matC.iloc[0,0]=param_dict["subj_num"]
matC.iloc[0,1]=param_dict["gender"]
matC.iloc[0,2]=param_dict["age"]
matC.iloc[0,3]=param_dict["counter_balance"]
matC.iloc[0,4]=under_300_sec
matC.iloc[0,5]=D_score
fn_IAT_D=param_dict["subj_num"] +"_"+ param_dict["gender"] +"_"+ param_dict["age"] +"_"+ param_dict["counter_balance"]+"_IAT_Dscore"+ ".csv"

# D得点のcsvファイルも作成
matC.to_csv(fn_IAT_D)
print("---D_score (Greenwald, Nosek, & Banaji, 2003)---")
print(round(D_score,3))

print("This script was made by R. Mimura @ Chiba University")