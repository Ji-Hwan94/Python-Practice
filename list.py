s = [1, 'four', 9, 16, 28]
print(s) 
print(s[0]) #list의 index를 통해 원소를 얻는 방법
print(len(s)) #list의 길이를 아는 방법
#index의 값을 바꾸는 방법
s[1] = 4
print(s)

#삭제방법
del s[3]
print(s)

#추가방법
s.append(5)      #끝에
s.insert(3,5656) #원하는 곳에