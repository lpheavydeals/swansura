import sys,pathlib,numpy as np
from PIL import Image,ImageDraw,ImageFilter
# re-place a cleaned cut-out like cutout_photos.py: product <=80% wide / 74% tall, 3% below centre, fresh floor shadow
d=pathlib.Path(sys.argv[1]); W,H=1200,1500
for n in sys.argv[2:]:
    im=Image.open(d/n).convert('RGBA'); a=np.array(im); al=a[...,3]
    m=al>110; ys,xs=np.where(m); box=(xs.min(),ys.min(),xs.max()+1,ys.max()+1)
    a[...,3]=np.where(m|(al>0)&False,al,0)  # drop old shadow
    keep=np.zeros_like(al); x0,y0,x1,y1=box
    sub=al[y0:y1,x0:x1].copy(); sub[sub<=110]=0  # product only
    from scipy import ndimage
    soft=ndimage.binary_dilation(sub>0,iterations=2); sub2=np.where(soft,al[y0:y1,x0:x1],0)
    c=Image.fromarray(np.dstack([np.array(im)[y0:y1,x0:x1,:3],sub2]).astype('uint8'),'RGBA')
    sc=min(W*0.80/c.width,H*0.74/c.height); c=c.resize((max(1,int(c.width*sc)),max(1,int(c.height*sc))),Image.LANCZOS)
    x,y=(W-c.width)//2,(H-c.height)//2+int(H*0.03)
    sh=Image.new('L',(W,H),0); ImageDraw.Draw(sh).ellipse((x+int(c.width*.05),y+c.height-18,x+int(c.width*.95),y+c.height+22),fill=70)
    shadow=Image.new('RGBA',(W,H),(60,50,40,0)); shadow.putalpha(sh.filter(ImageFilter.GaussianBlur(18)))
    layer=Image.new('RGBA',(W,H),(0,0,0,0)); layer.paste(c,(x,y),c)
    Image.alpha_composite(Image.alpha_composite(Image.new('RGBA',(W,H),(0,0,0,0)),shadow),layer).save(d/n,'WEBP',quality=90,method=6); print(n,round(sc,2))
