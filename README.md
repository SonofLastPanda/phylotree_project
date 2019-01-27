# phylotree_project

## 1)Get two leaves from user, find common ancestor. For all leaves from two subtree (as going up until common ancestor) find distances from root. Apply t-test for all points.

1)In deneme.py, 
    >leaf names are taken, subtrees are found and distance table created.
  In analysis_ETE.py,
    >t-test is applied.

## 2)Find all leaves' pair distances between two subtrees.For this data apply t-test for all distance points.
    In find_dist.py, first pair-wise distances of leaves of two subtrees of common ancestor of user-given two leafes are found, then t-test is applied to two resulting arrays that contains pair-wise distances of subtrees. In order to see whether the code works, the algorithm is applied to two different trees.
