# Py68FaceZones

[English](README.md)

## 專案介紹

Py68FaceZones 使用 `dlib` 與 `OpenCV`（`cv2`）處理人臉影像，偵測 68 個臉部特徵點，繪製自訂臉頰區域的 Bezier 曲線，並輸出左右臉頰的裁切結果。

<img src="res/result/test_landmarks.jpg" height="300">
<img src="res/result/test_full.jpg" height="300">

## 功能特色

- 自動偵測圖片中的人臉。
- 繪製 68 個 dlib 臉部特徵點與索引編號。
- 依照特徵點建立左右臉頰的 Bezier 曲線區域。
- 輸出左右臉頰區域的裁切結果。

## 環境需求

- Python 3.12
- `numpy<2`
- `opencv-python==4.8.1.78`
- `dlib-bin==19.24.2.post1`
- `imutils==0.5.4`

安裝指令：

```bash
python -m pip install -r requirements.txt
```

## 檔案結構

- `shape_predictor_68_face_landmarks.dat`：dlib 的 68 點臉部特徵模型檔。
- `res/`：放置輸入圖片的資料夾。
- `res/result/`：存放輸出結果圖片的資料夾。

## 使用方式

1. 確認已安裝所有相依套件，並將 `shape_predictor_68_face_landmarks.dat` 放在專案根目錄。
2. 將欲處理的圖片放入 `res/` 資料夾。
3. 編輯 `main.py` 中的 `file_name` 變數，指定圖片檔名（不含副檔名）。例如 `file_name = "test"` 會讀取 `res/test.jpg`。
4. 執行程式：

```bash
python main.py
```

5. 結果會輸出到 `res/result/`。

## 輸出圖片說明

執行完成後，`res/result/` 會產生以下圖片：

- `test_landmarks.jpg`：原始臉部圖片上疊加 68 個 landmark 點與編號，可用來確認臉部偵測與特徵點定位是否正確。
- `test_full.jpg`：原始圖片上繪製左右臉頰的綠色 Bezier 曲線輪廓。
- `test_left_zone.jpg`：依左臉頰路徑裁切出的區域圖，保留區域內的像素，其餘部分以白色填滿。
- `test_right_zone.jpg`：依右臉頰路徑裁切出的區域圖，輸出方式與左臉頰相同。

## 範例結果

### 68 點標記結果

<img src="res/result/test_landmarks.jpg" height="320">

### 左右臉頰輪廓

<img src="res/result/test_full.jpg" height="320">

### 左臉頰裁切

<img src="res/result/test_left_zone.jpg" height="220">

### 右臉頰裁切

<img src="res/result/test_right_zone.jpg" height="220">

## 錯誤處理

- 若 `shape_predictor_68_face_landmarks.dat` 不存在，或 `res/` 中缺少指定圖片，程式會拋出錯誤。
- 若圖片中沒有偵測到人臉，程式會回報錯誤。
