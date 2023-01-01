N, K = map(int, input().split())
MAX = 100001  # 점 위치 최대
array = [0] * MAX  # 해당 점에 도착했을 때 초를 표시하는 리스트


def bfs(V):
    need_visit = list()
    need_visit.append(V)  # 수빈이 출발점 삽입
    while need_visit:
        node = need_visit.pop(0)
        if node == K:  # 수빈이의 위치와 동생의 위치가 일치할때 함수 종료
            return array[node]
        for next in (node-1, node+1, node*2):
            # 점 위치가 최대.최소 범위 안에 있고 아직 방문하지 않았다면
            if 0 <= next < MAX and not array[next]:
                array[next] = array[node]+1
                need_visit.append(next)


print(bfs(N))
