from ete3 import Tree, TreeStyle,TextFace, NodeStyle
from scipy import stats
import statistics

#to-do:
#FINAL STEP: PYTHON GUI

def get_ancestor_subtree(tree,node1,node2):
    anc=tree.get_common_ancestor(node1, node2)
    return anc

def node_take(tree,num):
        e=0
        n=tree.get_tree_root()
        for node in tree.traverse():
                if e==num:
                        n=node
                        break
                else:
                        e=e+1
        return n

def pair_wise_diff(tree,node):
        diff=[]
        for i in range(len(tree)):
                for j in range(i+1,len(tree)):
                        x=node.get_distance(tree[i],tree[j])
                        diff.append(x)

        return diff

def diff_to_root(tree,node):
        dist=[]
        for i in range(len(tree)):
                x=node.get_distance(tree[i])
                dist.append(x)
        #print(str(len(tree)) + "    " + str(i))
        return dist
t = Tree("((6669.DappuP312785:1.24473,(((7739.JGI126010:4.02e-06,7739.JGI126021:0.168081)0.99985:0.848895,((45351.NEMVEDRAFT_v1g217973-PA:1.49614,(6085.XP_002167371:1.08059,10228.TriadP54105:1.08509)0.457684:0.128729)0.99985:0.321915,(7668.SPU_016633tr:0.00222941,7668.SPU_013365tr:0.093091)0.99985:0.642533)0.888302:0.101463)0.998565:0.12537,((51511.ENSCSAVP00000011400:0.259936,7719.ENSCINP00000035803:0.209259)0.99985:1.762,(7757.ENSPMAP00000006833:0.945887,((7955.ENSDARP00000103018:0.187989,(8049.ENSGMOP00000003903:0.283082,((8128.ENSONIP00000009923:0.172432,(69293.ENSGACP00000005927:0.11289,(99883.ENSTNIP00000008530:0.0637802,31033.ENSTRUP00000029741:0.0851327)0.99985:0.111539)0.750558:0.0140823)0.99985:0.0210439,(8083.ENSXMAP00000007211:0.156672,8090.ENSORLP00000021771:0.242897)0.99985:0.0332475)0.99985:0.0502247)0.99985:0.097906)0.99985:0.204816,(7897.ENSLACP00000021045:0.20103,(8364.ENSXETP00000053091:0.389689,((9258.ENSOANP00000015194:0.652603,((13616.ENSMODP00000032296:0.0669026,(9315.ENSMEUP00000005072:0.0368095,9305.ENSSHAP00000018667:0.0280404)0.997706:0.0140274)0.99985:0.109803,((9361.ENSDNOP00000011178:0.093465,(9371.ENSETEP00000005953:0.276816,(9813.ENSPCAP00000009886:0.0800451,9785.ENSLAFP00000023898:0.0550027)0.99697:0.0294647)0.99985:0.0375967)0.608183:0.00574174,((((30608.ENSMICP00000006810:0.0353003,30611.ENSOGAP00000013460:0.0515798)0.99985:0.034051,(9478.ENSTSYP00000011163:0.0656837,(9483.ENSCJAP00000037059:0.0556713,(9544.ENSMMUP00000001688:0.00821597,(61853.ENSNLEP00000001585:0.00543935,(9601.ENSPPYP00000009641:0.00544861,(9593.ENSGGOP00000014253:0.00241737,(9606.ENSP00000299886:0.00108745,9598.ENSPTRP00000016297:0.00216932)0.993995:0.00108247)0.99985:0.00217395)0.99985:0.00216928)0.99985:0.00380297)0.99985:0.00880979)0.99985:0.0259329)0.993631:0.00725957)0.99985:0.00775695,((((10141.ENSCPOP00000018381:0.0312261,10141.ENSCPOP00000003239:0.0560276)0.99985:0.131426,(10090.ENSMUSP00000018805:0.0326181,10116.ENSRNOP00000003804:0.0330137)0.99985:0.081468)0.995671:0.0105266,(43179.ENSSTOP00000001636:0.0584822,10020.ENSDORP00000002346:0.148367)0.976029:0.00712029)0.99985:0.020967,(9986.ENSOCUP00000010215:0.342444,37347.ENSTBEP00000010812:0.0710806)0.981559:0.0148504)0.99985:0.0111655)0.99985:0.0141806,((9823.ENSSSCP00000018275:0.0497089,(9739.ENSTTRP00000004916:0.0624029,9913.ENSBTAP00000007999:0.0933538)0.99985:0.0153799)0.99985:0.0353429,((9796.ENSECAP00000006507:0.0593149,(9685.ENSFCAP00000004377:0.0895056,(9615.ENSCAFP00000006718:0.0344248,(9646.ENSAMEP00000002816:0.0246918,9669.ENSMPUP00000014182:0.157245)0.979337:0.0106908)0.990824:0.00781435)0.99985:0.0209773)0.99291:0.00461526,(59463.ENSMLUP00000015199:0.175449,132908.ENSPVAP00000006353:0.0636063)0.828177:0.00861023)0.805512:0.00313751)0.99985:0.0138134)0.99985:0.0180555)0.99985:0.0925821)0.99985:0.0504324)0.99985:0.0408666,(28377.ENSACAP00000014302:0.2972,(13735.ENSPSIP00000020553:0.125656,(59729.ENSTGUP00000002997:0.21101,(9103.ENSMGAP00000006649:0.034221,9031.ENSGALP00000007041:0.0301602)0.99985:0.14558)0.99985:0.0950631)0.912514:0.0193477)0.99985:0.0543705)0.99985:0.0558399)0.99985:0.0851946)0.996306:0.0767894)0.99985:0.242292)0.99843:0.214734)0.760404:0.170331)0.99985:0.889243)0.99985:0.309174,((7070.TC009561-PA:1.414,(7029.ACYPI001869-PA:2.67503,((34740.HMEL012959-PA:0.216556,(13037.EHJ66433:0.30242,7091.BGIBMGA012450-TA:0.234676)0.691542:0.0356537)0.99985:1.06833,(7425.NV10250-PA:0.448078,(7460.GB18353-PA:0.265179,12957.ACEP_00009457-PA:0.219522)0.99985:0.223062)0.99985:0.715703)0.950323:0.0960579)0.630765:0.0828761)0.868488:0.104171,(121225.PHUM413450-PA:1.38201,(((43151.ADAR004533-PA:0.286189,7165.AGAP001322-PA:0.216522)0.99985:0.404262,(7176.CPIJ007948-PA:0.310705,7159.AAEL007141-PA:0.261808)0.99985:0.238196)0.99985:0.352684,(7260.FBpp0240708:0.24283,((7222.FBpp0149372:0.191481,7244.FBpp0224481:0.114954)0.99985:0.156407,(7237.FBpp0281462:0.118908,(7217.FBpp0120932:0.132407,(7245.FBpp0269552:0.0320153,7227.FBpp0082093:0.0340969)0.99985:0.0854297)0.99985:0.0800303)0.99985:0.0655239)0.825983:0.0710402)0.99985:1.14395)0.99985:0.708932)0.628915:0.0819834)0.99985:0.309174);",format=1)
num_nodes=0
for node in t.traverse():
   num_nodes+=1

print(str(num_nodes))



num1=int(input("Enter a node number: "))
num2=int(input("Enter another node number: "))

selection=int(input("1: Pair wise distances of leaves or 2: Distances of leaves to root: "))
node1=node_take(t,num1)
node2=node_take(t,num2)

print(node1.get_ascii(show_internal=True))
print(node2.get_ascii(show_internal=True))

diff_1=[]
diff_2=[]
if(node1.is_leaf() and node2.is_leaf() ):   #if both are leaves
        newtree=t.get_common_ancestor(node1, node2)
        child=newtree.get_children()
        subtree1=child[0].get_leaves()
        subtree2=child[1].get_leaves()
        if(selection==1):
                diff_1=pair_wise_diff(subtree1,newtree)
                diff_2=pair_wise_diff(subtree2,newtree)
        elif(selection==2):
                diff_1=diff_to_root(subtree1,newtree)
                diff_2=diff_to_root(subtree2,newtree)
        #leavess=neww.get_leaf_names()

elif (not node1.is_leaf() and  not node2.is_leaf()):
        node1.write(outfile="node1.nwk")
        node2.write(outfile="node2.nwk")
        new1=Tree("node1.nwk")
        new2=Tree("node2.nwk")

        subtree1=node1.get_leaves()
        subtree2=node2.get_leaves()
        #print(str(len(subtree1)) + "    " + str(len(subtree2)))
        if(selection==1):
                diff_1=pair_wise_diff(subtree1,new1)
                diff_2=pair_wise_diff(subtree2,new2)
        elif(selection==2):
                diff_1=diff_to_root(subtree1,new1)
                diff_2=diff_to_root(subtree2,new2)


stat=stats.ttest_ind(diff_1,diff_2)

print(stat.pvalue) #mean ve median ekle
print("Median of first set is: "+ str(statistics.median(diff_1)) +" " + "Median of second set is: " + str(statistics.median(diff_2)) )
print("Mean of first set is: "+ str(statistics.mean(diff_1)) + " " + "Mean of second set is: " + str(statistics.mean(diff_2)) )
#print(stat.statistic)

