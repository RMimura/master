#coding:utf-8
from __future__ import division
from __future__ import unicode_literals
from psychopy import visual, event, core, sound, gui
import random
import codecs

### 実験によって異なる部分 ###

##概念対A-B
# 概念A
A_concept="攻撃的"
A_words=["罵倒","陰口","排斥","脅迫"]
# 概念B
B_concept="非攻撃的"
B_words=["介抱","賛美","談笑","握手"]

# 概念X
X_concept="自己"
X_words=["自己","自分","私達","学生"]
# 概念Y
Y_concept="他者"
Y_words=["他者","他人","彼等","教師"]


# 参加者情報
param_dict={"subj_num":"","gender":["female","male"],"age":"","counter_balance":["CB1","CB2"]}
dlg=gui.DlgFromDict(param_dict,title=".. + * * INFORMATION * * + ..")
if dlg.OK==False:
    core.quit()

# 画面情報・時間情報
win=visual.Window(fullscr=True, monitor="testMonitor", units="deg",color="gray")
clock=core.Clock()
clock=clock

# カーソルを消す
event.Mouse(visible=False)

# サウンド
sound=sound.Sound("A",secs=0.5)

# データファイル
fn_IAT=param_dict["subj_num"] +"_"+ param_dict["gender"] +"_"+ param_dict["age"] +"_"+ param_dict["counter_balance"]+"_IAT"+ ".csv"
datafile=codecs.open(fn_IAT,"w","shift-JIS")
#左の列から、ブロック番号、一つの刺激に対する誤答回数、反応時間、そのブロックでは左右のどちらに分類したか、刺激単語がどの概念に含まれるか、刺激単語は何かをデータファイルに出力
datafile.write("block,error_num,RT,L_R,word_concept,word\n")


#設計(CB1: CB2はABが逆転)
#1 A-B
#2 X-Y
#3 AX-BY(practice) -> #4 AX-BY
#5 B-A
#6 X-Y
#7 BX-AY(practice) -> #8 BX-AY
#9 A-B
#10 Y-X
#11 AY-BX(practice) -> #12 AY-BX
#13 B-A
#14 Y-X
#15 BY-AX(practice) -> #16 BY-AX

#刺激単語
##group A
#A_words
##group B
#B_words
### group A&B
AB_words=A_words+B_words

##group X
X_words
##group Y
Y_words
##group X&Y
XY_words=X_words+Y_words

## all words for association
All_words_practice=AB_words+XY_words
All_words=AB_words+XY_words

#repetition & shuffle
AB_words *=3
random.shuffle(AB_words)
XY_words *=3
random.shuffle(XY_words)

#連合ブロックの練習繰り返し数を2回とする
All_words_practice *=2
random.shuffle(All_words_practice)

#連合ブロックの繰り返し数は3回
All_words *=3
random.shuffle(All_words)


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

stim01=visual.TextStim(win,font="ipagothic",color="skyblue",pos=(0,0),height=3.0)
stim02=visual.TextStim(win,font="ipagothic",color="lightgreen",pos=(0,0),height=3.0)

fix=visual.TextStim(win,text="+",font="ipagothic",color="white",pos=(0,0),height=3.0)
false=visual.TextStim(win,text="×",font="ipagothic",color="red",pos=(0,0),height=3.0)
#--------------------------------

#------------------------------------------------------------------------
                     #実験開始
#------------------------------------------------------------------------

IAT.draw()
press.draw()
win.flip()
event.waitKeys()


for block in range(1,17):
    if block in [1,3,4,9,11,12]:
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
        elif block in [11,12]:
            concept_X.setPos(underRight)
            concept_Y.setPos(underLeft)
            if block==11:
                words=All_words_practice
            elif block==12:
                words=All_words
    elif block in [5,7,8,13,15,16]:
        concept_A.setPos(upRight)
        concept_B.setPos(upLeft)
        words=AB_words
        if block in [7,8]:
            concept_X.setPos(underLeft)
            concept_Y.setPos(underRight)
            if block==7:
                words=All_words_practice
            elif block== 8:
                words=All_words
        elif block in [15,16]:
            concept_X.setPos(underRight)
            concept_Y.setPos(underLeft)
            if block==15:
                words=All_words_practice
            elif block==16:
                words=All_words
    elif block in [2,6]:
        words=XY_words
        concept_X.setPos(underLeft)
        concept_Y.setPos(underRight)
    elif block in [10,14]:
        words=XY_words
        concept_X.setPos(underRight)
        concept_Y.setPos(underLeft)
    
    
    if block in [1,5,9,13]:
        concept_A.draw()
        concept_B.draw()
    elif block in [2,6,10,14]:
        concept_X.draw()
        concept_Y.draw()
    else:
        concept_A.draw()
        concept_B.draw()
        concept_X.draw()
        concept_Y.draw()
        if block in [3,7,11,15]:
            prac.draw()
        elif block in [4,8,12,16]:
            crucial.draw()
    ready.draw()
    press.draw()
    win.flip()
    event.waitKeys(keyList=["space"])
    
    
    if block in [1,5,9,13]:
        concept_A.draw()
        concept_B.draw()
    elif block in [2,6,10,14]:
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
            stim01.setText(word)
        elif word in XY_words:
            stim02.setText(word)
        error_num=0
        
        waiting_keypress=True
        event.getKeys()
        clock.reset()
        while waiting_keypress:
            if block in [1,2,3,4]:
                if word in A_words:
                    stim_kind, correct_key,way="A_words",E,L
                elif word in B_words:
                    stim_kind, correct_key,way="B_words",I,R
                elif word in X_words:
                    stim_kind, correct_key,way="X_words","e","left"
                elif word in Y_words:
                    stim_kind, correct_key,way="Y_words","i","right"
            elif block in [5,6,7,8]:
                if word in A_words:
                    stim_kind, correct_key,way="A_words",I,R
                elif word in B_words:
                    stim_kind, correct_key,way="B_words",E,L
                elif word in X_words:
                    stim_kind, correct_key,way="X_words","e","left"
                elif word in Y_words:
                    stim_kind, correct_key,way="Y_words","i","right"
            elif block in [9,10,11,12]:
                if word in A_words:
                    stim_kind, correct_key,way="A_words",E,L
                elif word in B_words:
                    stim_kind, correct_key,way="B_words",I,R
                elif word in X_words:
                    stim_kind, correct_key,way="X_words","i","right"
                elif word in Y_words:
                    stim_kind, correct_key,way="Y_words","e","left"
            elif block in [13,14,15,16]:
                if word in A_words:
                    stim_kind, correct_key,way="A_words",I,R
                elif word in B_words:
                    stim_kind, correct_key,way="B_words",E,L
                elif word in X_words:
                    stim_kind, correct_key,way="X_words","i","right"
                elif word in Y_words:
                    stim_kind, correct_key,way="Y_words","e","left"
                
            keys=event.getKeys(keyList=["e","i","escape"])  
            
            for key in keys:
                if "escape" in keys:
                    datafile.close()
                    core.quit()
                elif correct_key in keys:
                    datafile.write("block{},{},{:.5f},{},{},{}\n".format(block,error_num,clock.getTime()*1000,way,stim_kind,word))
                    datafile.flush()
                    waiting_keypress=False
                    break
                else:
                    error_num +=1
                    if block in [1,5,9,13]:
                        concept_A.draw()
                        concept_B.draw()
                    elif block in [2,6,10,14]:
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
                    waiting_keypress=True
                    
            if block in [1,5,9,13]:
                concept_A.draw()
                concept_B.draw()
                stim01.draw()
            elif block in [2,6,10,14]:
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
            
        if block in [1,5,9,13]:
            concept_A.draw()
            concept_B.draw()
        elif block in [2,6,10,14]:
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

#----------IAT----------
sound.play()
thankyou.draw()
win.flip()
event.waitKeys(keyList=["space"])
print("Done Experiment")
