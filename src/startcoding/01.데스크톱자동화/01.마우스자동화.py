import pyautogui
import time

# 1.화면 크기 출력
print(pyautogui.size())  # 화면 해상도 출력

# 2.마우스 위치 출력
# time.sleep(2)  # 2초 대기
# print(pyautogui.position())  # 현재 마우스 커서 위치 출력

# 3.마우스 이동
pyautogui.moveTo(32, 284, duration=1)

# 4.마우스 클릭
# pyautogui.click()
# pyautogui.click(button='right')  # 오른쪽 클릭  
# pyautogui.doubleClick()
# pyautogui.click(clicks=3, interval=1)  # 3번 클릭, 클릭 사이 1초 대기

# 5. 마우스 드래그
# 582,49 -> 411,52
pyautogui.moveTo(582, 49, duration=1)
pyautogui.dragTo(411, 52, duration=1)  # 절대 좌표로 드래그
