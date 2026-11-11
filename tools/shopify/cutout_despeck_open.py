# pass 2: morphological opening for cracks touching the product
import sys,pathlib,numpy as np
from PIL import Image,ImageDraw,ImageFilter
from scipy import ndimage
# cut thin lines that touch the product (morphological opening), restore shadow under them
src=pathlib.Path(sys.argv[1]); out=pathlib.Path(sys.argv[2]); it=int(sys.argv[3]); W,H=1200,1500
for n in sys.argv[4:]:
    a=np.array(Image.open(src/n).convert('RGBA')); al=a[...,3]
    solid=al>110
    op=ndimage.binary_opening(solid,iterations=it)
    lab,k=ndimage.label(op); sizes=ndimage.sum(op,lab,range(1,k+1))
    main=np.isin(lab,[i+1 for i,s in enumerate(sizes) if s>=0.05*sizes.max()])
    keep=solid & ndimage.binary_dilation(main,iterations=it+2)
    ys,xs=np.where(keep); x0,x1,y1=xs.min(),xs.max()+1,ys.max()+1; cw=x1-x0
    sh=Image.new('L',(W,H),0); ImageDraw.Draw(sh).ellipse((x0+int(cw*.05),y1-18,x0+int(cw*.95),y1+22),fill=70)
    sa=np.array(sh.filter(ImageFilter.GaussianBlur(18)))
    bad=(al>0) & ~ndimage.binary_dilation(keep,iterations=2)
    a[bad,0:3]=(60,50,40); a[bad,3]=np.minimum(sa[bad],al[bad])
    Image.fromarray(a).save(out/n,'WEBP',quality=90,method=6); print(n,int(bad.sum()))
