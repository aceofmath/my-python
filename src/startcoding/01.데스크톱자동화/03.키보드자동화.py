import pyautogui
import pyperclip

# 1. 키보드 입력(문자)
# pyautogui.write('Hello, World!', interval=0.2)  # 문자 입력, 글자 사이 0.2초 대기
# pyautogui.write('스타트코딩') <=== 한글은 입력되지 않는다.

# 2. 키보드 입력(키)
# pyautogui.press('enter')  # 엔터 키 입력
# pyautogui.press('up')     # 방향키 위 입력
# pyautogui.press('down')   # 방향키 아래 입력
# pyautogui.press('left')   # 방향키 왼쪽 입력
# pyautogui.press('right')  # 방향키 오른쪽 입력

# 3. 키보드 입력(여러개 동시에)
# pyautogui.hotkey('ctrl', 'c')  # Ctrl + C 입력 (저장 단축키)

# 4. 한글 입력 방법
pyperclip.copy('스타트코딩')  # 클립보드에 한글 복사
pyautogui.hotkey('ctrl', 'v')

