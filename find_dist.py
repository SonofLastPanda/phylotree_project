from ete3 import Tree, TreeStyle,TextFace, NodeStyle
from scipy import stats
import statistics

t = Tree("((6669.DappuP312785:1.24473,(((7739.JGI126010:4.02e-06,7739.JGI126021:0.168081)0.99985:0.848895,((45351.NEMVEDRAFT_v1g217973-PA:1.49614,(6085.XP_002167371:1.08059,10228.TriadP54105:1.08509)0.457684:0.128729)0.99985:0.321915,(7668.SPU_016633tr:0.00222941,7668.SPU_013365tr:0.093091)0.99985:0.642533)0.888302:0.101463)0.998565:0.12537,((51511.ENSCSAVP00000011400:0.259936,7719.ENSCINP00000035803:0.209259)0.99985:1.762,(7757.ENSPMAP00000006833:0.945887,((7955.ENSDARP00000103018:0.187989,(8049.ENSGMOP00000003903:0.283082,((8128.ENSONIP00000009923:0.172432,(69293.ENSGACP00000005927:0.11289,(99883.ENSTNIP00000008530:0.0637802,31033.ENSTRUP00000029741:0.0851327)0.99985:0.111539)0.750558:0.0140823)0.99985:0.0210439,(8083.ENSXMAP00000007211:0.156672,8090.ENSORLP00000021771:0.242897)0.99985:0.0332475)0.99985:0.0502247)0.99985:0.097906)0.99985:0.204816,(7897.ENSLACP00000021045:0.20103,(8364.ENSXETP00000053091:0.389689,((9258.ENSOANP00000015194:0.652603,((13616.ENSMODP00000032296:0.0669026,(9315.ENSMEUP00000005072:0.0368095,9305.ENSSHAP00000018667:0.0280404)0.997706:0.0140274)0.99985:0.109803,((9361.ENSDNOP00000011178:0.093465,(9371.ENSETEP00000005953:0.276816,(9813.ENSPCAP00000009886:0.0800451,9785.ENSLAFP00000023898:0.0550027)0.99697:0.0294647)0.99985:0.0375967)0.608183:0.00574174,((((30608.ENSMICP00000006810:0.0353003,30611.ENSOGAP00000013460:0.0515798)0.99985:0.034051,(9478.ENSTSYP00000011163:0.0656837,(9483.ENSCJAP00000037059:0.0556713,(9544.ENSMMUP00000001688:0.00821597,(61853.ENSNLEP00000001585:0.00543935,(9601.ENSPPYP00000009641:0.00544861,(9593.ENSGGOP00000014253:0.00241737,(9606.ENSP00000299886:0.00108745,9598.ENSPTRP00000016297:0.00216932)0.993995:0.00108247)0.99985:0.00217395)0.99985:0.00216928)0.99985:0.00380297)0.99985:0.00880979)0.99985:0.0259329)0.993631:0.00725957)0.99985:0.00775695,((((10141.ENSCPOP00000018381:0.0312261,10141.ENSCPOP00000003239:0.0560276)0.99985:0.131426,(10090.ENSMUSP00000018805:0.0326181,10116.ENSRNOP00000003804:0.0330137)0.99985:0.081468)0.995671:0.0105266,(43179.ENSSTOP00000001636:0.0584822,10020.ENSDORP00000002346:0.148367)0.976029:0.00712029)0.99985:0.020967,(9986.ENSOCUP00000010215:0.342444,37347.ENSTBEP00000010812:0.0710806)0.981559:0.0148504)0.99985:0.0111655)0.99985:0.0141806,((9823.ENSSSCP00000018275:0.0497089,(9739.ENSTTRP00000004916:0.0624029,9913.ENSBTAP00000007999:0.0933538)0.99985:0.0153799)0.99985:0.0353429,((9796.ENSECAP00000006507:0.0593149,(9685.ENSFCAP00000004377:0.0895056,(9615.ENSCAFP00000006718:0.0344248,(9646.ENSAMEP00000002816:0.0246918,9669.ENSMPUP00000014182:0.157245)0.979337:0.0106908)0.990824:0.00781435)0.99985:0.0209773)0.99291:0.00461526,(59463.ENSMLUP00000015199:0.175449,132908.ENSPVAP00000006353:0.0636063)0.828177:0.00861023)0.805512:0.00313751)0.99985:0.0138134)0.99985:0.0180555)0.99985:0.0925821)0.99985:0.0504324)0.99985:0.0408666,(28377.ENSACAP00000014302:0.2972,(13735.ENSPSIP00000020553:0.125656,(59729.ENSTGUP00000002997:0.21101,(9103.ENSMGAP00000006649:0.034221,9031.ENSGALP00000007041:0.0301602)0.99985:0.14558)0.99985:0.0950631)0.912514:0.0193477)0.99985:0.0543705)0.99985:0.0558399)0.99985:0.0851946)0.996306:0.0767894)0.99985:0.242292)0.99843:0.214734)0.760404:0.170331)0.99985:0.889243)0.99985:0.309174,((7070.TC009561-PA:1.414,(7029.ACYPI001869-PA:2.67503,((34740.HMEL012959-PA:0.216556,(13037.EHJ66433:0.30242,7091.BGIBMGA012450-TA:0.234676)0.691542:0.0356537)0.99985:1.06833,(7425.NV10250-PA:0.448078,(7460.GB18353-PA:0.265179,12957.ACEP_00009457-PA:0.219522)0.99985:0.223062)0.99985:0.715703)0.950323:0.0960579)0.630765:0.0828761)0.868488:0.104171,(121225.PHUM413450-PA:1.38201,(((43151.ADAR004533-PA:0.286189,7165.AGAP001322-PA:0.216522)0.99985:0.404262,(7176.CPIJ007948-PA:0.310705,7159.AAEL007141-PA:0.261808)0.99985:0.238196)0.99985:0.352684,(7260.FBpp0240708:0.24283,((7222.FBpp0149372:0.191481,7244.FBpp0224481:0.114954)0.99985:0.156407,(7237.FBpp0281462:0.118908,(7217.FBpp0120932:0.132407,(7245.FBpp0269552:0.0320153,7227.FBpp0082093:0.0340969)0.99985:0.0854297)0.99985:0.0800303)0.99985:0.0655239)0.825983:0.0710402)0.99985:1.14395)0.99985:0.708932)0.628915:0.0819834)0.99985:0.309174);",format=1)
#t=Tree("((A,B),C);",format=1)
#t=Tree("(GOOSE Guangdong 96,(GOOSE Guangdong 97,((((CHICKEN Hubei 2002,CHICKEN Hubei 1997),CHICKEN Hubei 1997),((((((((((((((((((((((((((((((DUCK Guangxi 2005,GOOSE Guangxi 2005),(DUCK Guangxi 2005,GOOSE Guangxi 2005)),DUCK Guangxi 2005),DUCK Guangxi 2005),CHICKEN Guangxi 2005),DUCK Guangxi 2006),(GOOSE Guangxi 2006,CHICKEN Thailand 172)),(DUCK Hunan 2005,DUCK Hunan 2005)),((DUCK Guangxi 2005,DUCK Guangxi 2006),(CHICKEN Hong Kong 2006,CHICKEN Hong Kong 2006))),((((CHICKEN Guangxi 2006,GOOSE Guangxi 2006),GOOSE Guangxi 2006),((((CHICKEN Guangxi 2006,(DUCK Guangxi 2006,GOOSE Guangxi 2006)),DUCK Guangxi 2006),((DUCK Guangxi 2006,GOOSE Guangxi 2006),DUCK Guangxi 2006)),DUCK Guangxi 2006)),CHICKEN Guiyang 2006)),((((((CHICKEN Guiyang 2005,(CHICKEN Guiyang 2005,(DUCK Guiyang 2006,DUCK Guiyang 2006))),(DUCK Guiyang 2005,DUCK Guiyang 2005)),(DUCK Fujian 2006,DUCK Fujian 2006)),COMMON magpie 645),(DUCK Hunan 2006,DUCK Hunan 2006)),(GOOSE Guangxi 2006,(GOOSE Shantou 2006,GOOSE Shantou 2006)))),(((CHICKEN Fujian 2005,((DUCK Fujian 2005,(DUCK Fujian 2005,(DUCK Fujian 2005,DUCK Fujian 2005))),((CHICKEN Fujian 2005,DUCK Fujian 2005),DUCK Fujian 2005))),((CHICKEN Fujian 2005,(CHICKEN Fujian 2005,CHICKEN Fujian 2006)),(CHICKEN Shantou 2006,CHICKEN Shantou 2006))),(DUCK Shantou 2005,CHICKEN Shantou 2006))),(((DUCK Hunan 2006,DUCK Hunan 2006),CRESTED myna 540),((((JAPANESE white Hong Kong,LITTLE egret 718),(((COMMON magpie 2125,MUNIA Hong Kong 2006),COMMON magpie 3033),WHITE backed Hong Kong)),COMMON magpie 2256),LARGE billed Hong Kong))),GOOSE Guangxi 2005),(CHICKEN Guiyang 2005,((CHICKEN Guiyang 2005,GOOSE Guiyang 2005),DUCK Guiyang 2005))),((DUCK China 2,((CHICKEN Guangdong 04,((CHICKEN Guangxi 2005,QUAIL Guangxi 2005),DUCK Guangxi 2005)),((((((((((CHICKEN Guangxi 2005,((CHICKEN Guangxi 2005,(DUCK Guangxi 2005,(DUCK Guangxi 2005,DUCK Guangxi 2005))),GOOSE Yunnan 2005)),GOOSE Yunnan 2005),((((((CHICKEN Guiyang 2005,CHICKEN Guiyang 2005),GOOSE Yunnan 2005),DUCK Yunnan 2005),DUCK Yunnan 2005),GOOSE Yunnan 2005),DUCK Yunnan 2005)),GOOSE Guangxi 2005),((DUCK Guangxi 2005,(DUCK Guangxi 2005,DUCK Guangxi 2005)),(DUCK Guangxi 2005,DUCK Guangxi 2006))),DUCK Guangxi 2005),GOOSE Guangxi 2005),DUCK Guangxi 2005),((GOOSE Guangxi 2005,((QUAIL Viet 15,CHICKEN Viet 17),DUCK Viet 12)),CHICKEN Viet 10)),(DUCK Guangxi 2005,((DUCK Hunan 2005,(DUCK Hunan 2005,DUCK Hunan 2005)),PHEASANT Shantou 2006))))),(CHICKEN Guangdong 04,CHICKEN Hunan 2005))),((((((((((CHICKEN Afghanistan 2006,CHICKEN Afghanistan 92),CHICKEN Afghanistan 47),CHICKEN Afghanistan 7),(COMMON goldeneye 12,WHOOPER swan 2)),CHICKEN Afghanistan 65),CYGNUS cygnus 754),((((((((((BAR headed Qinghai,BROWN headed Qinghai),BAR headed Qinghai),BAR headed Qinghai),BAR headed Qinghai),((BAR headed Qinghai,BAR headed Qinghai),BAR headed Qinghai)),BAR headed Qinghai),BAR headed Qinghai),(MIGRATORY duck 2300,(GUINEA fowl 1341,((BAR headed Mongolia,(TURKEY Turkey 2005,TURKEY Turkey 2005)),WHOOPER swan 3)))),BAR headed Qinghai),BAR headed Qinghai)),GREAT Black Gull),((((DUCK Hubei 2003,DUCK Hubei 2003),CHICKEN Guangdong 04),((((CHICKEN Kyoto 2004,CROW Kyoto 2004),CHICKEN Yamaguchi 2004),CROW Osaka 2004),(CHICKEN Oita 2004,(CHICKEN Korea 03,DUCK Korea 03)))),(GOOSE Jilin 2003,(GOOSE Shantou 2006,GOOSE Shantou 2006)))),((CHICKEN Guangxi 2004,DUCK Guangxi 2004),(((CK Indonesia 2003,DK Indonesia 2004),CK Indonesia 2003),(((CHICKEN Dairi 2005,CHICKEN Simalanggang 2005),(CHICKEN Deli BPPVI,(CHICKEN Tarutung 2005,CHICKEN Tebing BPPVI))),((((CHICKEN Gunung BBVW,CHICKEN Magetan 2005),DUCK Parepare 2005),CHICKEN Indonesia 2005),CHICKEN Purworejo 2005)))))),DUCK Guangdong 04),(EGRET Hong Kong 2,((((((((CHICKEN Ayutthaya CU,(CHICKEN Nakorn Thailand,(CHICKEN Thailand 168,(CK Viet C57,CHICKEN Vietnam 04)))),LITTLE grebe Phichit),(CK Thailand 1,QA Thailand 2004)),BIRD Thailand 1),OPEN billed Nakhonsawan),(((OPEN billed Nakhonsawan,OPEN billed Suphanburi),((CHICKEN Thailand CK,CHICKEN Thailand CK),(QUAIL Thailand Pathom,CHICKEN Thailand 170))),((((DUCK Viet 1,CHICKEN Viet 11),(DUCK Viet 20,DUCK Viet 19)),(CHICKEN Viet 2,((CHICKEN Viet 6,CHICKEN Viet 8),CHICKEN Viet 9))),DUCK Viet 18))),((OPEN billed Nakhonsawan,OPEN billed Nakhonsawan),OPEN billed Nakhonsawan)),(((((CK Viet 35,CHICKEN Viet TN),(CK Viet 36,QUAIL Vietnam 04)),CK Viet 38),(CK Viet 37,CHICKEN Viet TG)),(CHICKEN Viet 33,CHICKEN Viet LD))))),(((DUCK Shanghai 2002,DUCK Shantou 2003),(((CHICKEN Henan 2004,(CHICKEN Henan 2004,CHICKEN Henan 2004)),CHICKEN Henan 2004),(((CHICKEN Henan 2004,CHICKEN Henan 2004),((CHICKEN Hubei 2004,CHICKEN Hubei 2004),SWAN Guangxi 2004)),(MALLARD Guangxi 2004,WILDDUCK Guangdong 2004)))),((((CHICKEN Fujian 2005,DUCK Fujian 2005),GOOSE Shantou 2005),(DUCK Guangxi 2005,DUCK Guangzhou 2005)),PEREGRINE falcon D0028))),(CHICKEN Jilin 2002,CHICKEN Jilin 2004)),(((((((CHICKEN Hebei 2001,DUCK Guangxi 2001),(GOOSE Fujian 2003,(((CHICKEN Guiyang 2006,GOOSE Guiyang 2006),DUCK Guiyang 2005),CK HK 4))),GOOSE Hong Kong 8),((DUCK Hong Kong 1,(CHICKEN HongKong 01,(CHICKEN HongKong 2,CHICKEN HongKong 2))),((((CHICKEN HongKong 01,CHICKEN HongKong 01),PHEASANT HongKong 01),PHEASANT HongKong 01),(CHICKEN HongKong 3,CHICKEN HongKong 3)))),DUCK Zhejiang 2002),(CHICKEN Jiangsu 2002,(CHICKEN Jilin 2002,(CHICKEN Hubei 2003,((CHICKEN Hebei 2005,CHICKEN Shanxi 2006),(DUCK Yunnan 2005,GOOSE Yunnan 2005)))))),(((DUCK Guangxi 2004,GOOSE Guangxi 2004),DUCK Guangxi 2004),DUCK Yokohama 2003))),CHICKEN Jilin 2002),(DUCK Hokkaido 1,DUCK Mongolia 01)),CHICKEN Jilin 2003),(GOOSE Hong Kong 2000,GOOSE Hong Kong 2000)),((((DUCK Anyang 1,GOOSE Guangdong 2001),CHICKEN Hebei 02),DUCK Shandong 2004),CHICKEN Jilin 2002)),(((ENVIRONMENT Hong Kong 10,ENVIRONMENT Hong Kong 8),ENVIRONMENT Hong Kong 4),ENVIRONMENT Hong Kong 6)),CHICKEN Jilin 2003),CHICKEN Hubei 1997)),(((CHICKEN Hong Kong 97,CHICKEN Hong Kong 97),((CHICKEN Hong Kong 97,(DUCK Vietnam 2005,DUCK Vietnam 05)),GOOSE Vietnam 05)),(DUCK Hong Kong 97,GOOSE Hong Kong 97)))));")


#to-do:
# p-value ile beraber difference setlerin mean ve medianlarını alalım
#leaflerin ortak ataya olan uzaklıkları, iki ayrı subtree için, ayrı bir fonksiyon olabilir en sonunda t-test yaparız
#FINAL STEP: bunları GUIye dökmek
edge = 0
for node in t.traverse():
   if not node.is_leaf():
      node.name = "NODE_%d" %edge
      edge += 1

print(str(edge))

'''
t.write(format=1)
ts = TreeStyle()
ts.show_leaf_name = True
ts.show_branch_length = True
t.show(tree_style=ts)


'''
def get_ancestor_subtree(tree,node1,node2):
    anc=tree.get_common_ancestor(node1, node2)
    return anc

def node_take(tree,num):
        e=0
        for node in tree.traverse():
                if not node.is_leaf() and e==num:
                        n=node
                        break
                else:
                        e=e+1
        return n
        


'''
ts = TreeStyle()
ts.show_leaf_name = True
ts.show_branch_length = True
ts.title.add_face(TextFace("Our first tree", fsize=10), column=0)
t.show(tree_style=ts)
'''


#leaf1=input("Enter a leaf name: ")
#leaf2=input("Enter another leaf name: ")
num1=int(input("Enter a node number: "))
num2=int(input("Enter another node number: "))
node1=node_take(t,num1)
node2=node_take(t,num2)
#newtree=get_ancestor_subtree(t,node1,node2)
node1.write(outfile="node1.nwk")
node2.write(outfile="node2.nwk")

new1=Tree("node1.nwk")
new2=Tree("node2.nwk")


'''
ts = TreeStyle()
ts.show_leaf_name = True
ts.show_branch_length = True
ts.title.add_face(TextFace("Our first tree", fsize=10), column=0)
neww.show(tree_style=ts)
'''
'''
leaves=neww.get_leaves()
#print(leaves)
leavess=neww.get_leaf_names()

print(str(node1))
print(str(node2))
for i in range(len(leaves)):
    if node1==leavess[i]:
        first=leaves[i]

for i in range(len(leaves)):
    if  node2==leavess[i]:
        second=leaves[i]

while first.is_root()==False:
    previous1=first
    first=first.up
#print (previous1)

while second.is_root()==False:
    previous2=second
    second=second.up
#print (previous2)
'''
subtree1=new1.get_leaves()
subtree2=new2.get_leaves()

diff_1=[]
diff_2=[]

for i in range(len(subtree1)):
    x=new1.get_distance(subtree1[i])
    #s.write(str(subtree1[i])+"\t"+str(x)+"\t"+"1")
    diff_1.append(x)

for i in range(len(subtree2)):
    y=new2.get_distance(subtree2[i])
    #s.write(str(subtree2[i])+"\t"+str(y)+"\t"+"2")
    diff_2.append(y)


'''
for i in range(len(subtree1)):
    for j in range(i+1,len(subtree1)):
        x=node1.get_distance(subtree1[i],subtree1[j])
        diff_1.append(x)

for i in range(len(subtree2)):
    for j in range(i+1,len(subtree2)):
        x=neww.get_distance(subtree2[i],subtree2[j])
        diff_2.append(x)
'''
stat=stats.ttest_ind(diff_1,diff_2)

print(stat.pvalue) #mean ve median ekle
print("Median of first set is: "+ str(statistics.median(diff_1)) +" " + "Median of second set is: " + str(statistics.median(diff_2)) )
print("Mean of first set is: "+ str(statistics.mean(diff_1)) + " " + "Mean of second set is: " + str(statistics.mean(diff_2)) )
#print(stat.statistic)

