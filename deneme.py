import PyQt5
from ete3 import Tree, TreeStyle, TextFace
import pandas as pd
import numpy as np
t = Tree("(((A:6, B:7):2, C:2):1.0,(((((D:1,I:3):5,F:10):7,G:2):0,H:2):8,E:0.1):1):2.0;" )
#print (t)
t.show()
leaf_list=t.get_leaves()
a_node=leaf_list[0]
another_node=a_node.get_farthest_node(topology_only=True)
other_node=another_node[0]
#print (other_node)

while a_node.is_root()==False:
    previous=a_node
    a_node=a_node.up

print (previous)

while other_node.is_root()==False:
    previous2=other_node
    other_node=other_node.up

#print (previous2)

leaff1=previous.get_leaves()
sum1=0
for i in range(len(leaff1)):
    #print (t.get_distance(leaff1[i]))
    sum1=sum1+t.get_distance(leaff1[i])

average1=sum1/len(leaff1)

print("sum1= " +str(sum1))
print("average1= " + str(average1))

leaff2=previous2.get_leaves()
sum2=0
for i in range(len(leaff2)):
    #print (t.get_distance(leaff2[i]))
    sum2=sum2+t.get_distance(leaff2[i])

average2=sum2/len(leaff2)

print("sum2= " +str(sum2))
print("average2= " + str(average2))

statistic=open("statistic3.csv", "w")
statistic.write("left subtree"+"\t"+"right subtree"+"\n"+str(sum1)+"\t"+str(sum2)+"\n"+str(average1)+"\t"+str(average2))


