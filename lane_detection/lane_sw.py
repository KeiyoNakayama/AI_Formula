import cv2
import numpy as np

# 画像を読み込み
img = cv2.imread("test_images/lane.png")

if img is None:
    print("画像が読み込めませんでした")
    exit()

# グレースケール変換
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Cannyエッジ検出
edges = cv2.Canny(gray, 50, 150)

# 結果を表示
cv2.imshow("Edges", edges)
cv2.waitKey(0)
cv2.destroyAllWindows()
