# 05장. 그래프 알고리즘

# 1. 그래프 표현 이해하기

- 버텍스(Vertex) : 네트워크를 구성하는 개체, `|V|`
- 엣지(Edge) : 두 버텍스를 잇는 선, `|E|`
    
    ```python
    import networkx as nx
    
    G = nx.Graph()
    
    G.add_node("Mike")
    G.add_nodes_from(["Amine", "Wasim", "Nick"])
    G.add_edge("Mike", "Amine")
    
    list(G.nodes)
    list(G.edges)
    
    G.add_edge("Amine", "Imran")
    
    list(G.edges)
    ```
    

## 1. 그래프 유형

### 1. 무방향 그래프(Undirected Graph)

- 무방향 엣지 : 서로 연결된 노드 사이에는 어떠한 상하 관계나 순서가 존재하지 않음

### 2. 방향 그래프(Directed Graph)

- 노드 사이의 관계가 어떠한 방향성을 갖는 경우

### 3. 무방향 멀티그래프(Undirected Multigraph)

- 두 노드를 잇는 여러 엣지는 서로 다른 유형의 관계를 표현

### 4. 방향 멀티그래프(Directed Multigraph)

- 멀티그래프에 있는 노드 사이에 방향 관계 존재

## 2. 특수한 유형의 엣지

- 셀프 엣지(Self-Edge) : 어떤 버텍스는 자기 자신과 관계를 형성
- 하이퍼 엣지(Hyperedge) : 엣지 하나가 셋 이상의 버텍스에 연결된 형태

## 3. 에고 중심 네트워크

- 특정한 버텍스에 대한 중요한 정보는 그와 연결된 다른 버텍스에서 얻을 수 있음

## 4. 소셜 네트워크 분석(Social Network Analysis, SNA)

- 그래프를 구성하는 버텍스가 사람을 의미
- 버텍스를 연결하는 엣지는 친구, 친족, 연인 등 다양한 사회적 관계 표현
- 그래프 분석을 통해 도출한 결과는 강력한 사회적 파급 효과를 불러올 수 있음
- 네트워크 분석 이론(Network Analysis Theory) : 네트워크로 설정하고 네트워크 분석을 위해 고안된 알고리즘 적용

# 2. 네트워크 분석 이론 살펴보기

## 1. 최단 경로

- 경로 : 시작 버텍스와 끝 버텍스 사이에 있는 일련의 연속적인 버텍스
- 최단 경로 : 모든 가능한 경로 중에서 가장 거리가 짧은 경로
- 다익스트라 알고리즘(Dijkstra’s Algorithm) : 단일 출발지로부터의 최단 경로 계산
- 너비 우선 검색(Breadth-First Search, BFS) : 그래프상에 있는 모든 엣지의 이동 비용은 동일하다는 가정 사용
- 플로이드-워셜(Floyd-Warshall) : 모든 출발지-도착지 쌍의 최단 경로 탐색

## 2. 삼각형

- 세 개의 버텍스가 세 개의 엣지로 연결된 형태

## 3. 밀도

- 완전 연결 네트워크(Fully Connected Network) : 모든 버텍스들이 서로 연결된 네트워크

$$
Edges_{total} = \frac{N(N-1)}{2}
$$

$$
density = \frac{Edges_{observed}}{Edges_{total}}
$$

## 4. 중심성 지표 이해하기

- 해당 버텍스가 그래프 내에서 얼마나 중요한지 나타내는 지표

### 1. 도수 중심성(Degree Centrality)

- 도수(Degree) : 특정 버텕스에 연결된 엣지의 수
- 해당 버텍스가 다른 버텍스와 얼마나 잘 연결되어 있는지, 네트워크 내에서 메시지를 얼마나 빠르게 전파할 수 있는지 표현

$$
C_{DC_a} = \frac{deg(a)}{|V| - 1}
$$

### 2. 매개 중심성(Betweenness Centrality)

- 그래프 내에서 버텍스가 다른 버텍스들 사이에 위치하는 정도를 표현

$$
C_{betweenness_a} = \frac{n_{shortest_a}}{n_{shortest_{Total}}}
$$

### 3. 공정성(Fairness)과 근접 중심성(Closeness Centrality)

- 공정성 : 자기 자신과 그래프 내 다른 버텍스와의 거리를 모두 더한 것
- 근접 중심성 : 공정성에 역수를 취한 것

### 4. 고유벡터 중심성(Eigenvector Centrality)

- 다른 버텍스의 중심성을 가중치로 반영

## 5. 파이썬으로 중심성 지표 계산하기

```python
import networkx as nx
import matplotlib.pyplot as plt

vertices = range(1, 10)
edges = [(7, 2), (2, 3), (7, 4), (4, 5), (7, 3), (7, 5), (1, 6), (1, 7), (2, 8), (2, 9)]
G = nx.Graph()
G.add_nodes_from(vertices)
G.add_edges_From(edges)
nx.draw(G, with_labels=True, node_color='y', node_size=800)

nx.degree_centrality(G)
nx.betweenness_centrality(G)
nx.closeness_centrality(G)

centrality = nx.eigenvector_centrality(G)
sorted((v, '{:0.2f}'.format(c)) for v, c in centrality.items())
```

# 3. 그래프 순회(Graph Traversal) 이해하기

- 특정한 방식을 따라 그래프에 있는 모든 버텍스와 엣지를 확인하는 과정
- 모든 버텍스와 엣지를 단 한 번만 방문

## 1. 너비 우선 검색(Breadth-First Search, BFS)

- 그래프 내에 레이어 또는 레벨로 구성된 이웃 그룹들이 있을 때 적용할 수 있는 가장 효율적인 그래프 순회 전략
- 루트 버텍스에서 시작하여 그 인근 레이어에 있는 이웃 버텍스들을 탐색 → 이웃들에 대한 확인이 끝나면 다음 레이어로 이동하여 검색 과정 반복

### 1. 초기 설정

- `visited`  : 방문한 버텍스 저장
- `queue`  : 다음 번 검색에서 방문할 버텍스 저장

### 2. 메인 루프

- `queue`  에서 첫 번째 버텍스를 꺼내옴
- 해당 버텍스가 `visited` 리스트에 없다면 이를 `visited` 에 추가 → 이 버텍스의 이웃 버텍스 목록을 그래프에서 불러옴
- 불러온 이웃들을 `queue` 에 추가
- 메인 루프 종료 → 그동안 방몬한 모든 버텍스가 담긴 `visited` 반환
    
    ```python
    def bfs(graph, start):
        visited = []
        queue = [start]
    
        while queue:
            node = queue.pop(0)
            if node not in visited:
                visited.append(node)
                neighbours = graph[node]
                for neighbour in neighbours:
                    queue.append(neighbour)
        return visited
    ```
    

## 2. 깊이 우선 검색(Depth-First Search, DFS)

- 개별 경로를 하나씩 끝까지 탐색 → 선택한 경로의 끝에 도달하면 DFS는 그 과정에서 방문한 모든 버텍스들을 방문 완료 처리