# 문제 출처: 
# https://www.acmicpc.net/problem/1002

# 원의 방정식
# 1. 두 원의 중심 사이의 거리를 계산합니다.
# 2. 두 원의 반지름을 차이를 계산합니다.
# 3. 두 원의 반지름을 합한 값과 중심 사이의 거리를 비교합니다.
# - 만약 두 원의 반지름을 합한 값이 중심 사이의 거리보다 크다면 교점이 두 개 있습니다.
# - 만약 두 원의 반지름을 합한 값이 중심 사이의 거리와 같다면 교점이 하나 있습니다.
# - 만약 두 원의 반지름을 합한 값이 중심 사이의 거리보다 작다면 교점이 없습니다.
# 4. 특별한 경우로, 두 원이 완전히 겹쳐진 경우 무한히 많은 교점이 있습니다.

def intersection_points(x1, y1, r1, x2, y2, r2):
    # 두 원의 중심 사이의 거리 계산
    distance = ((x2 - x1)**2 + (y2 - y1)**2)**(1/2)
    
    # 두 원의 반지름 합
    radius_sum = r1 + r2

    # 두 원의 반지름 차이
    radius_diff = abs(r1 - r2)
    
    # 교점 개수 계산
    if distance == 0 and r1 == r2:  # 두 원이 동심원일 때
        return -1  # 무한히 많은 교점
    elif distance < radius_diff:  # 두 원이 내접하거나 한 원이 다른 원 안에 있는 경우
        return 0
    elif distance == radius_sum:  # 두 원이 외접할 때
        return 1
    elif distance < radius_sum:  # 두 원이 교차할 때
        return 2
    else:  # 두 원이 완전히 겹치지 않을 때
        return 0

for i in range(int(input())):
    question = list(map(int, input().split()))
    print(intersection_points(question[0], question[1], question[2], question[3], question[4], question[5]))


# 위 코드는 틀림.
# 외접하는 경우는 생각하였으나 내접하는 경우를 생각하지 않음.

# 답: 
def intersection_points(x1, y1, r1, x2, y2, r2):
    # 두 원의 중심 사이의 거리 계산
    distance = ((x2 - x1)**2 + (y2 - y1)**2)**(1/2)
    
    # 두 원의 반지름 합
    radius_sum = r1 + r2

    # 두 원의 반지름 차이
    radius_diff = abs(r1 - r2)
    
    # 두 원이 동심원일 때
    if distance == 0:
        if r1 == r2:
            return -1  # 무한히 많은 교점
        else:
            return 0  # 교점 없음
    
    # 두 원의 외접, 내접, 겹치지 않는 경우 처리
    if distance == radius_sum or distance == radius_diff: # 앞에는 외접, 뒤에는 내접
        return 1  # 한 점에서 만남
    elif distance < radius_sum and distance > radius_diff: # 교점과 두 원의 중심을 기준으로 삼각형을 만들 수 있어야 함.(두 선분의 길이의 합은 남은 한 선분보다 크다)
        return 2  # 두 점에서 만남
    else:
        return 0  # 교점 없음

for i in range(int(input())):
    question = list(map(int, input().split()))
    print(intersection_points(question[0], question[1], question[2], question[3], question[4], question[5]))


# 답 최적화: 
for i in range(int(input())):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    distance = ((x2 - x1)**2 + (y2 - y1)**2)**(1/2)
    radius_sum = r1 + r2
    radius_diff = abs(r1 - r2)
    if distance == 0 and r1 == r2:
        print(-1)
    elif distance == radius_sum or distance == radius_diff:
        print(1)
    elif distance < radius_sum and distance > radius_diff:
        print(2)
    else:
        print(0)