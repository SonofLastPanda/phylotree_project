from ete3 import Tree, TreeStyle,TextFace, NodeStyle
t = Tree("(((A:5, B:7):0.001, C:2):1.0,(((((D:0.1,I:3):10,F:10):6,G:2):1,H:2):0,E:0.1):5):2.0;" )
#print (t)

def minimum_distance_pair(t):
    leaf_names = t.get_leaf_names()
    min_dist=32768
    index1=0
    index2=0
    pair_list=[]
    for i in range(len(leaf_names)):
        for j in range(len(leaf_names)):
            if i != j:
                dist=t.get_distance(leaf_names[i], leaf_names[j])
                if min_dist > dist:
                    min_dist = dist
                    index1=i
                    index2=j

    pair_list.append(leaf_names[index1])
    pair_list.append(leaf_names[index2])
    print("min distance: "+ str(min_dist))
    print("min dist pair: " + leaf_names[index1] + " " + leaf_names[index2])
    return pair_list



def print_ancestor_subtree(tree):
    node1=str(input("Enter a leaf to search: "))
    node2=str(input("Enter second leaf to search: "))
    anc=tree.get_common_ancestor(node1, node2)
    print(anc)
    
print_ancestor_subtree(t)
#minimum_distance_pair(t)

ts = TreeStyle()
ts.show_leaf_name = True
ts.show_branch_length = True
ts.title.add_face(TextFace("Our first tree", fsize=10), column=0)
t.add_face(TextFace("min distance pair:" + str(minimum_distance_pair(t)), ftype="Courier"), column=1, position="float-behind")
t.show(tree_style=ts)
