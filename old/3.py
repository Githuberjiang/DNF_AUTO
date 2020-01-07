# import cv2
# # 生成图片
# img = cv2.imread("1.jpg")
# # 生成灰色图片
# imgGrey = cv2.imread("1.jpg", 0)
# #  展示原图
# cv2.imshow("img", img)
# #  展示灰色图片
# cv2.imshow("imgGrey", imgGrey)
# #  等待图片的关闭
# cv2.waitKey()
# # 保存灰色图片
# cv2.imwrite("Copy.jpg", imgGrey)



# import cv2
#
# img = cv2.imread("1.jpg")
#
# cv2.namedWindow("img", cv2.WINDOW_NORMAL)
# cv2.imshow("img", img)
# cv2.waitKey()
# cv2.destroyAllWindows()


import cv2
#
# img = cv2.imread("1.jpg")
#
# numb = img[50, 100]
# print(numb)
#
# img[50, 100] = (0, 0, 255)
# cv2.imshow("img", img)
# cv2.waitKey()

#
# import pyautogui
# #判定目标截图在系统上的位置
# location=pyautogui.locateOnScreen(image='2.png')
# #输出坐标
# print(location)



imgsr = cv2.imread("2.png")
imgtm = cv2.imread("3.png")
# 获取模板图片的高和宽
imgtmh1 = imgtm.shape[0]

imgtmw1 = imgtm.shape[1]

print(imgtmh1, imgtmw1)
# 与模版比对
res = cv2.matchTemplate(imgsr, imgtm, cv2.TM_CCOEFF_NORMED)
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
img = cv2.rectangle(imgsr, max_loc, (max_loc[0] + imgtmw1, max_loc[1] + imgtmh1), (0, 0, 255), 2)

cv2.imshow('Image', img)
print(max_loc[0] + imgtmw1, max_loc[1] + imgtmh1)
cv2.waitKey(0)
cv2.destroyAllWindows()




