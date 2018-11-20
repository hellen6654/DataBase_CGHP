# DataBase_CGHP 資料庫系統課程實做練習

## 0.請先Download或Clone此repo
![](https://i.imgur.com/emwIaXN.png)

## 1.請先開啟InstallEnv資料夾 並依照"環境安裝說明"的步驟執行
環境安裝說明：https://hackmd.io/s/rJV-Itb07
![](https://i.imgur.com/HJBORSH.png)
![](https://i.imgur.com/Qm2yFVv.png)

## 2.開啟RunServer.bat
![](https://i.imgur.com/DyDVpUA.png)
![](https://i.imgur.com/Luer8oS.png)

## 3.開啟任意瀏覽器 並輸入 127.0.0.1:8000 或 localhost:8000 出現此畫面即建置環境完成
![](https://i.imgur.com/R5kwQsp.png)
- 如果要中止 切回cmd視窗 按下ctrl+c 就會中止了
- 中止之後網頁連不上是正常現象
- 要開啟只須在打開RunServer.bat即可
## 4.開始亂玩Django吧！
- 官方教學：https://docs.djangoproject.com/en/2.1/intro/tutorial01/
- 我把 "py manage.py runserver" 這句指令包進RunServer.bat裡面了，這樣就不用一直打指令了。
- 儘管試，如果不小心試出問題，想要重來，把CGHP資料夾刪除，解壓縮CGHP_init，並把CGHP_init資料夾裡面的CGHP資料夾放到manage.py和RunServer.bat相同資料夾裡就可以了
- 如果有修改程式碼，建議先關閉RunServer.bat，再進行修改。修改完，在開啟RunServer.bat
