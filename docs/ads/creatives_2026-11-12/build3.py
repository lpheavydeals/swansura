import sys,os
from build2 import build,E,OVD
MD='../vv/Milk_Drops_Serum__Milk_Drops_-_Product_1080x1920.mp4';A='../vv/AM_PM_Combo__AM_PM_Combo_1080X1920.mp4'
H1='../dv/Deyga_Organics_V42_Hair_Growth_Oil.mp4';H2='../dv/Deyga_Organics_V39_Rice_water_shampoo.mp4';H3='../dv/Deyga_Organics_V40_Conditioner.mp4'
LB='../dv/Deyga_Organics_V15_Beetroot_Lipbalm.mp4'
W=sys.argv[1:]
if 'r' in W:
    build('Vilvah_MilkDropsSerum_9x16.mp4',[(MD,6.6,8.3,0.5,'','fade'),(MD,10.5,11.95,0.6,'','smoothup'),(MD,15.0,16.45,0.65,'','dissolve'),(A,8.0,9.4,0.7,'','fade'),(MD,18.5,19.45,0.42)],
      [('r1',0,0),('r2',1,1),('r2b',1,1),('r3',2,2),('r4',3,3),('r5',4,4)],f'{OVD}/rend.png',E,MD,'fade')
if 'g' in W:
    build('Deyga_HairCareKit_9x16.mp4',[(H1,2.5,4.9,0.9,'','fade'),(H1,5.0,6.9,0.85,'','slideleft'),(H2,3.0,4.4,1,'','fade'),(H2,4.5,5.4,1,'','dissolve'),(H2,5.5,7.9,1,'','fade'),(H3,3.0,3.9,1,'','fade'),(H3,4.0,5.4,1,'','dissolve'),(H3,7.0,8.9,1,'','fade'),(H3,16.0,18.5,1)],
      [('g1',0,0),('g2',1,1),('g2b',1,1),('g3',2,4),('g3b',3,4),('g4',5,7),('g4b',6,7),('g5',8,8)],f'{OVD}/gend.png',E,H2,'fade')
if 'p' in W:
    build('Deyga_BeetrootLipBalmClassic_9x16.mp4',[(LB,0.0,1.9,0.8,'','fade'),(LB,2.0,3.4,0.8,'','zoomin'),(LB,3.5,5.4,0.85,'','fade'),(LB,5.5,7.4,0.85,'','dissolve'),(LB,11.0,13.9,0.9,'','fade'),(LB,14.0,16.4,0.9)],
      [('p1',0,0),('p2',1,2),('p2b',1,2),('p3',3,3),('p4',4,4),('p5',5,5)],f'{OVD}/pend.png',E,LB,'fade')
