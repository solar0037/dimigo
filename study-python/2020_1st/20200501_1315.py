# 딕셔너리
testd = dict()  # 빈딕셔너리를 만들어요

testd['name'] = '사호준'  # 추가
testd[('a',)] = '사호준'  # 추가 튜플이 키로 가능
testd[[1]] = '사호준'  # ERROR 키는 중복될 수 없고 리스트가 올 수 없다.
testd[1301] = '사호준'  # 추가 숫자는 키로 가능
testd[(5)] = '사호준'  # 추가 숫자