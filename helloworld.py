'''
목록(list, [])은 정렬되고 변경 가능한 컬렉션입니다. 중복된 멤버를 허용합니다.
튜플(tuple, ())은 정렬되고 변경할 수 없는 컬렉션입니다. 중복된 멤버를 허용합니다.
셋(Set, {key}) 은 순서가 없고, 변경 불가능하며, 인덱싱되지 않은 컬렉션입니다. 중복된 멤버가 없습니다.
사전(Dic, {key, val})은 정렬되고** 변경 가능한 컬렉션입니다. 중복된 멤버가 없습니다.
'''

x = range(1,10)
y = range(1,10)
result = ""
for i in x:
    print(f"{i}dan")
    for j in y:
        #result = f"{i} X {j} = {i*j}"
        #print(result)
        print(i, "X", j, "=", i*j)

day = 4
match day:
  case 1:
    print("Monday")
  case 2:
    print("Tuesday")
  case 3:
    print("Wednesday")
  case 4:
    print("Thursday")
  case 5:
    print("Friday")
  case 6:
    print("Saturday")
  case 7:
    print("Sunday")        