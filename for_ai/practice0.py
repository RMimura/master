"""
この実験での流れ
1．＋の注視点が画面上に1秒間提示される。
2．HかSが提示される。
3．キーを押すと試行が終了する。
4．条件が全て提示されたら実験を終了する。
"""
from psychopy import core, visual, event, sound # "core"は時間。"visual"は視覚刺激。"event"はキーやマウスの反応。"sound"は音刺激。
import random # ランダムな順序に並びかえる
import codecs # 記録する

# 画面の定義。
win = visual.Window(fullscr = True,size = [1920, 1080],units="pix",color="gray") # sizeはPCのピクセル数に合わせる
clock = core.Clock() # 時計の定義

fix = visual.TextStim(win, text = "+", height = 50.0, color = "white") # 注視点の定義
stim = visual.TextStim(win, height = 50.0) # 刺激の共通情報

# 条件として，提示する文字と着色を変える。2*3の6条件ある
condition = []
for word in ["H", "S"]:
    for col in ["red","green","blue"]:
        condition.append([word, col]) # wordとcolの各組み合わせをconditionに代入

# 条件の組み合わせを3倍に増やす（繰り返し回数が3回）
condition *= 3
random.shuffle(condition) # ランダムな順序に並びかえる

# データファイルの作成
filename = "dataFile.csv"
datafile=codecs.open(filename,"w","shift-JIS")

# データファイルに書き込み。\nは改行を意味する
datafile.write("word,color,key,RT\n")

# ここから提示開始
for cond in condition:
    w = cond[0] # condの0番目、つまりwordについての条件をwとする
    c = cond[1] # condの1番目、つまりcolについての条件をcとする
    stim.setText(w) # stimにwをTextとして代入
    stim.setColor(c) # stimにcをColorとして代入
    
    fix.draw() # fixをウィンドウに描画。
    win.flip() # ウィンドウを更新。
    core.wait(1.0) # 1.0秒間待機。
    
    wait=True # キー押しの待ちであることを宣言する
    clock.reset() # 時間情報をリセット
    event.getKeys() # 刺激提示前のキー押しを無効にする
    while wait: # キー押しを待っている間
        keys=event.getKeys(keyList=["escape","s","h"]) # "escape", "h", "s"のキーを取得対象とする
        for key in keys: # 取得対象のキーにおいて
            if "escape" in keys: # もしキーの中の"escape"ならば
                core.quit() # 時間の計測を終了する
                datafile.close() # データファイルの書き込みを終了する
            else: # そうでなければ
                datafile.write("{},{},{},{:.5f}\n".format(w,c,key,clock.getTime())) # データファイルに書込み。{}の中身を.format(中身)で指定できる
                wait = False # 待ち状態を解除
                break # forから抜け出す
        stim.draw() # waitの間stimをウィンドウに描画。
        win.flip() # waitの間ウィンドウを更新。


win.close() # ウィンドウを閉じる。
core.quit() # 時間の計測を終了する。