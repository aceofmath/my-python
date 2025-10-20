import pyautogui

pyautogui.alert('메세지 박스입니다.')  # 확인 버튼만 있는 메세지 박스
response = pyautogui.confirm('계속 진행할까요?')  # 확인 / 취소 버튼이 있는 메세지 박스
print('사용자 응답:', response)
response = pyautogui.prompt('당신의 이름은 무엇입니까?')  # 사용자 입력을 받는 메세지 박스
print('사용자 이름:', response)
