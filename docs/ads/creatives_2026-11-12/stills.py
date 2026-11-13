# square product photo -> 1080x1920 clip: photo full width in the middle, bands filled with its own edge colours (blurred), slow zoom
import subprocess,numpy as np
from PIL import Image,ImageFilter
def canvas(src,box=None):
    im=Image.open(src).convert('RGB')
    if box: im=im.crop(box)
    w=1080;h=round(im.height*w/im.width);im=im.resize((w,h),Image.LANCZOS)
    s=max(1080/im.width,1920/im.height)*1.15
    bg=im.resize((round(im.width*s),round(im.height*s)),Image.LANCZOS)
    l=(bg.width-1080)//2;t=(bg.height-1920)//2;bg=bg.crop((l,t,l+1080,t+1920)).filter(ImageFilter.GaussianBlur(70))
    B=np.asarray(bg).astype(float);B=B*0.85+255*0.15
    a=np.asarray(im).astype(float);y0=(1920-h)//2
    m=np.ones(1920);m[y0:y0+h]=0;r=np.linspace(1,0,90);m[y0:y0+90]=r;m[y0+h-90:y0+h]=r[::-1]
    full=B.copy();full[y0:y0+h]=a
    out=full*(1-m[:,None,None])+B*m[:,None,None]
    return Image.fromarray(np.uint8(out.clip(0,255)))
def clip(src,out,dur,box=None,z0=1.0,z1=1.06):
    canvas(src,box).save(out+'.png');n=int(dur*30)
    subprocess.run(['ffmpeg','-v','error','-y','-loop','1','-i',out+'.png','-vf',
      f"scale=2160:3840,zoompan=z='{z0}+({z1}-{z0})*on/{n}':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d={n}:s=1080x1920:fps=30,format=yuv420p",
      '-frames:v',str(n),'-c:v','libx264','-crf','16','-preset','medium',out],check=True)
J=[('lift_1.jpg','st/lift_wide.mp4',3.2,None),('lift_1.jpg','st/lift_ultra.mp4',3.2,(0,300,620,945)),
   ('mbody_1.jpg','st/body_wide.mp4',3.2,None),('mbody_1.jpg','st/body_wash.mp4',3.2,(75,100,650,950)),
   ('mface_1.jpg','st/face_wide.mp4',3.2,None),('mface_1.jpg','st/face_mask.mp4',3.2,(25,300,550,850))]
for s,o,d,b in J: clip(s,o,d,b);print(o)
