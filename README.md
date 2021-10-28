# ESLab_hw3 : BLE Programming - Central
### 實作目標

在Raspberry Pi 3執行BLE Central程式，與iOS系統的light blue App溝通，(以Blood Pressure Service為例)，實現Read、Write、Notify 與 Indicate功能。

#### Step 1

下載 light blue app (iOS)，並開啟藍芽功能

#### Step 2

在RPi上執行 "rpi_cccd.py"，等待掃描裝置

#### Step 3

輸入裝置編號 (最後印出的裝置編號)

#### Step 4

確認 terminal 與 App 的溝通結果

### 彈性調整

- 在rpi_cccd.py中，將有關變數 "flag" 的程式碼刪掉，便會印出所有裝置資訊及編號，可依照需求輸入不同裝置編號，以及修改BPService中的UUID
- 在 "WRITE" 時，可修改rpi_cccd.py中的內容以傳送不同資訊(default: "QAQ")
- 在 "READ" 時，可在app中修改想要讓RPi讀取的文字內容
- Light blue app中，可以任意新增service、characteristics及其property，和相關內容，四種property (READ、WRITE、NOTIFY、INDICATE) 都能和RPi進行互動



