import sys,pathlib,numpy as np
from PIL import Image,ImageDraw,ImageFilter
from scipy import ndimage
# remove thin stray pieces (wall cracks) from cut-outs; put the floor shadow back under them
src=pathlib.Path(sys.argv[1]); out=pathlib.Path(sys.argv[2]); W,H=1200,1500
for n in sys.argv[3:]:
    a=np.array(Image.open(src/n).convert('RGBA')); al=a[...,3]
    solid=al>110; lab,k=ndimage.label(solid)
    sizes=ndimage.sum(solid,lab,range(1,k+1)); sl=ndimage.find_objects(lab); big=sizes.max()
    drop=[i+1 for i,(s,q) in enumerate(zip(sizes,sl)) if s<0.05*big and s/((q[0].stop-q[0].start)*(q[1].stop-q[1].start))<0.18]
    if not drop: print(n,'none'); continue
    keep=solid & ~np.isin(lab,drop)
    ys,xs=np.where(keep); x0,x1,y0,y1=xs.min(),xs.max()+1,ys.min(),ys.max()+1
    cw,chh=x1-x0,y1-y0
    sh=Image.new('L',(W,H),0); ImageDraw.Draw(sh).ellipse((x0+int(cw*.05),y1-18,x0+int(cw*.95),y1+22),fill=70)
    sa=np.array(sh.filter(ImageFilter.GaussianBlur(18)))
    bad=ndimage.binary_dilation(np.isin(lab,drop),iterations=4) & ~ndimage.binary_dilation(keep,iterations=2)
    a[bad,0:3]=(60,50,40); a[bad,3]=sa[bad]
    # faint leftovers outside product+shadow
    far=~ndimage.binary_dilation(keep,iterations=6) & (sa<3) & (al<=110)
    a[far,3]=0
    Image.fromarray(a).save(out/n,'WEBP',quality=90,method=6); print(n,len(drop))
