import sys,numpy as np
from PIL import Image,ImageFilter
from scipy import ndimage
from rembg import remove,new_session
s=new_session('birefnet-general-lite')
for f in sys.argv[1:]:
    im=Image.open(f).convert('RGB');a=np.array(remove(im,session=s).split()[-1]).astype(float)
    solid=ndimage.binary_fill_holes(a>25);lab,n=ndimage.label(solid)
    if n>1:
        sz=ndimage.sum(solid,lab,range(1,n+1));solid=np.isin(lab,[i+1 for i,v in enumerate(sz) if v>=sz.max()*0.02])
    core=ndimage.binary_erosion(solid,iterations=3)
    al=np.where(core,255,np.where(solid,np.maximum(a,128),0)).astype('uint8')
    r=im.copy();r.putalpha(Image.fromarray(al).filter(ImageFilter.GaussianBlur(0.8)));r=r.crop(r.getbbox())
    out=f.rsplit('.',1)[0]+'_cut.png';r.save(out);print(out,r.size)
