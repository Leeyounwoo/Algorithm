# Tree 정리

[TOC]

## Tree 정의

- 트리는 그래프 자료구조 중 하나
- **그래프와 트리의 차이점?**
  - 싸이클이 없어야 함
  - 루트 노드가 반드시 하나
  - 부모 노드가 반드시 하나
- 트리는 일반적인 경우, 암묵적으로 방향 표기 X (단방향이므로)



## Tree 용어 정리

- 노드, 간선
- 높이(height)
  - 루프부터 리프까지 간선의 개수
- 레벨(level)
  - 루트부터 현재 노드까지 간선의 개수
  - 루트를 0이 아닌 1투저 시작하는 경우가 있으므로 주의
- 차수(degree)
  - 어떤 노드의 자식 수
- 부모노드, 자식노드, 형제노드
- 루트노드, 리프노트
- 서브트리



## 트리의 종류

> 다진트리보다 이진트리의 구조가 간결해서
> 여러가지 알고리즘을 구현할 때 편하기 때문에 많이 활용됨.
> (이진트리 또는 BST 등)

- 다진트리 (n-ary)
- 이진트리 (binary tree)
  - 완전 이진 트리
    - 마지막 레벨을 제외하고는 모든 노드가 
      "왼쪽부터 순서대로" 채워져있는 트리
  - 포화 이진 트리
    - 모든 노드가 두개의 자식을 가지고
      리프 노드가 동일한 레벨을 갖는 트리
- 이진 탐색 트리 (Binary Search Tree, BST)



## 트리 순회 방법

- 전위 (preorder) 순회
- 중위 (inorder) 순회
- 후위 (postorder) 순회



## 트리 표현 방식

- 배열 (ex. 파이썬의 리스트)
- 연결 리스트 (ex. 파이썬의 클래스로 표현 가능)
