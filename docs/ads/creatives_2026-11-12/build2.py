# xfade-based builder: segs=(src,ss,to,speed,precrop,transition_into_next)
import subprocess,sys,os
OVD=os.environ.get('OVD','ov916');PFX=os.environ.get('PFX','')
V='scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,fps=30,setsar=1,format=yuv420p,settb=1/30'
XD=0.3
def build(name,segs,ovs,endpng,endlen,audio,endtr='fade'):
    inputs=[];fc=[];n=[0]
    def add(*a): inputs.extend(a);n[0]+=1;return n[0]-1
    srcs=[];[srcs.append(s[0]) for s in segs if s[0] not in srcs]
    sidx={s:add('-i',s) for s in srcs};uses={s:sum(1 for x in segs if x[0]==s) for s in srcs}
    for s in srcs: fc.append(f"[{sidx[s]}:v]split={uses[s]}"+''.join(f'[u{sidx[s]}_{k}]' for k in range(uses[s])))
    cnt={s:0 for s in srcs};durs=[]
    for i,s in enumerate(segs):
        src,ss,to,sp=s[:4];pre=s[4] if len(s)>4 and s[4] else ''
        lab=f'u{sidx[src]}_{cnt[src]}';cnt[src]+=1
        fc.append(f"[{lab}]trim={ss}:{to},setpts=(PTS-STARTPTS)/{sp},{pre+',' if pre else ''}{V}[s{i}]");durs.append((to-ss)/sp)
    # chain xfades; start time of seg i on the output timeline
    starts=[0];cur='s0';off=durs[0]
    for i in range(1,len(segs)):
        tr=segs[i-1][5] if len(segs[i-1])>5 else 'fade'
        o=off-XD;starts.append(o)
        fc.append(f"[{cur}][s{i}]xfade=transition={tr}:duration={XD}:offset={o:.3f}[x{i}]");cur=f'x{i}';off=o+durs[i]
    body=off
    ei=add('-loop','1','-t',str(endlen+0.5),'-i',endpng)
    fc.append(f"[{ei}:v]scale=1080:1920,fps=30,format=yuv420p,setsar=1,settb=1/30[end]")
    fc.append(f"[{cur}][end]xfade=transition={endtr}:duration=0.4:offset={body-0.4:.3f}[base]")
    total=body-0.4+endlen+0.5;cur='base'
    ends=[starts[i]+durs[i] for i in range(len(segs))]
    for k,ov in enumerate(ovs):
        png,i0,i1=ov[:3];fin,fout=(ov[3],ov[4]) if len(ov)>3 else (1,1)
        a=starts[i0]+(0.1 if i0==0 else XD*0.5);b=ends[i1]-(XD*0.5 if i1<len(segs)-1 else 0.35)
        oi=add('-loop','1','-t',str(total),'-i',f'{OVD}/{png}.png')
        fl=['format=rgba']+([f"fade=in:st={a:.3f}:d=0.3:alpha=1"] if fin else [])+([f"fade=out:st={b-0.2:.3f}:d=0.2:alpha=1"] if fout else [])
        fc.append(f"[{oi}:v]{','.join(fl)}[o{k}]")
        y=f"'if(lt(t,{a:.3f}),36,if(lt(t,{a+0.35:.3f}),36*(1-(t-{a:.3f})/0.35)^2,0))'" if fin else "0"
        fc.append(f"[{cur}][o{k}]overlay=x=0:y={y}:enable='between(t,{a:.3f},{b:.3f})':eval=frame[c{k}]");cur=f"c{k}"
    ai=add('-i',audio)
    fc.append(f"[{ai}:a]atrim=0:{total:.3f},asetpts=PTS-STARTPTS,afade=t=in:d=0.15,afade=t=out:st={total-1.2:.3f}:d=1.2,loudnorm=I=-14:TP=-1.5:LRA=11[aud]")
    cmd=['ffmpeg','-v','error','-y',*inputs,'-filter_complex',';'.join(fc),'-map',f'[{cur}]','-map','[aud]','-t',f'{total:.3f}',
         '-c:v','libx264','-preset','slow','-crf','18','-profile:v','high','-pix_fmt','yuv420p','-movflags','+faststart','-c:a','aac','-b:a','192k','-ar','48000',PFX+name]
    subprocess.run(cmd,check=True);print(PFX+name,round(total,2),[round(s,2) for s in starts])
A='../vv/AM_PM_Combo__AM_PM_Combo_1080X1920.mp4'
G='../vv/Goatmilk_shampoo_250ml__GMS_Brand_video_Marketplace.mp4'
AL='../dv/Deyga_Organics_V02_Aloe_Gel.mp4';ST='../dv/Deyga_Organics_V01_Beetroot_lip_balm_stick.mp4';CH='../dv/Deyga_Organics_V20_Charcoal_Bath_Bar.mp4'
CU='crop=740:1316:170:604';CL='crop=650:1156:215:764'
W=sys.argv[1:]
E=4.0
if 'a' in W:
    build('Vilvah_AMPMSerumKit_9x16.mp4',[(A,4.0,4.6,0.4,CU,'dissolve'),(A,4.8,6.0,0.6,CL,'smoothup'),(A,8.0,9.4,0.6,'','fadeblack'),(A,9.6,11.3,0.75,'crop=843:1500:118:420','smoothup'),(A,11.6,13.6,0.8,CU,'dissolve'),(A,14.0,15.9,0.8,CU,'circleopen'),(A,16.0,16.9,0.45)],
      [('a1',0,1),('a2',2,2),('a2b',2,2),('a3',3,4),('a3b',3,4),('a4',5,5),('a5',6,6)],f'{OVD}/aend.png',E,A,'fadewhite')
if 'b' in W:
    build('Vilvah_BestsellerHairKit_9x16.mp4',[(G,0.0,0.35,0.5,'','fade'),(G,1.0,3.8,0.85,'crop=1116:1984:594:740','slideleft'),(G,11.2,15.9,1,'crop=1244:2212:530:1244','wipeleft'),(G,7.0,9.5,1,'crop=540:960:882:0','slideleft'),(G,16.3,18.9,0.8,'crop=1361:2419:943:1037')],
      [('b1',0,1),('b2',2,2),('b2b',2,2),('b3',3,3),('b4',4,4),('b4b',4,4)],f'{OVD}/bend.png',E,G,'slideup')
if 'c' in W:
    build('Deyga_ABCKit_9x16.mp4',[(AL,0.0,2.6,1,'','circleopen'),(AL,3.0,4.4,1,'','zoomin'),(AL,4.5,6.4,1,'','slideleft'),(ST,5.2,6.9,1,'','zoomin'),(ST,8.5,10.2,1,'','slideleft'),(CH,2.4,4.0,1,'','zoomin'),(CH,5.0,7.4,1,'','circleopen'),(ST,12.4,14.4,1)],
      [('c1',0,0),('c2',1,2),('c2b',1,2),('c3',3,4),('c3b',3,4),('c4',5,6),('c4b',5,6),('c5',7,7)],f'{OVD}/cend.png',E,AL,'circleclose')
if 'k' in W:
    build('Deyga_ClearSkinKit_9x16.mp4',[(CH,0.0,1.0,0.6,'','hblur'),(CH,4.0,5.9,1,'','fade'),(CH,7.5,9.9,1,'','hblur'),(CH,12.5,14.0,1,'','fadewhite'),(AL,2.0,3.4,1,'','fade'),(AL,8.5,10.6,1,'','hblur'),(AL,14.0,17.0,1)],
      [('k1',0,0),('k2',1,3),('k2b',1,3),('k3',4,5),('k3b',4,5),('k4',6,6)],f'{OVD}/kend.png',E,CH,'fadeblack')

FB='../vv/Face_Brightening_Combo__FBC_Vertical.mp4';PW='../vv/Milk_Powder_Facewash__MPFW_Product_Video_1080x1920.mp4';MD='../vv/Milk_Drops_Serum__Milk_Drops_-_Product_1080x1920.mp4'
if 'f' in W:
    build('Vilvah_FaceBrighteningKitLarge_9x16.mp4',[(PW,2.5,3.9,0.8,'','dissolve'),(PW,7.0,8.7,0.85,'','slideup'),(FB,16.0,17.9,0.8,'crop=742:1320:169:600','dissolve'),(FB,18.0,19.4,0.8,'crop=686:1220:197:700','fadewhite'),(MD,7.0,8.4,0.75,'','dissolve'),(FB,20.5,21.9,0.8,'crop=675:1200:200:720','smoothup'),(FB,26.0,27.9,0.8,'crop=720:1280:60:640')],
      [('f1',0,0),('f2',1,1),('f2b',1,1),('f3',2,3),('f4',4,5),('f4b',4,5),('f5',6,6)],f'{OVD}/fend.png',E,PW,'fade')
LB='../dv/Deyga_Organics_V15_Beetroot_Lipbalm.mp4';LS='../dv/Deyga_Organics_V19_Strawberry_lip_scrub.mp4'
if 'n' in W:
    build('Deyga_NourishedLipsKit_9x16.mp4',[(LS,0.0,1.4,1,'','slideleft'),(LB,0.0,1.6,1,'','fade'),(LS,1.5,3.8,1,'','zoomin'),(LS,4.0,5.6,1,'','fade'),(LB,2.0,4.6,1,'','zoomin'),(LB,5.5,7.0,1,'','dissolve'),(LB,11.5,13.6,1,'','dissolve'),(LS,14.3,15.9,1)],
      [('n1',0,1),('n2',2,2),('n2b',2,2),('n3',3,3),('n4',4,5),('n4b',4,5),('n5',6,6),('n6',7,7)],f'{OVD}/nend.png',E,LS,'fade')
ST='../dv/Deyga_Organics_V01_Beetroot_lip_balm_stick.mp4';MR='../vv/MILK_RANGE__Milk_Range.mp4'
LO='../../nk/src/milkbodylotion.mp4';UE='../../nk/src/undereye.mp4';SQ='crop=608:1080:236:0'
if 's' in W:
    build('Deyga_LipBalmStick_9x16.mp4',[(ST,0.0,1.8,0.8,'','dissolve'),(ST,2.0,3.6,0.8,'','slideleft'),(ST,5.0,6.9,0.8,'','zoomin'),(ST,8.4,10.4,0.85,'','dissolve'),(ST,12.0,13.8,0.85,'','fade'),(ST,14.2,16.2,0.85)],
      [('s1',0,1),('s2',2,2),('s2b',2,2),('s3',3,4),('s4',5,5)],f'{OVD}/send.png',E,ST,'fade')
if 'm' in W:
    build('Vilvah_MilkFaceKit_9x16.mp4',[('st/face_wide.mp4',0,2.6,1,'','fade'),('st/face_mask.mp4',0,2.6,1,'','fade'),(MR,29.0,30.4,0.7,'crop=378:672:1144:0','smoothup'),(MD,2.6,3.7,0.6,'','fade'),(MD,7.0,8.9,0.85,'','fade'),(MD,15.0,15.95,0.6,'','dissolve'),(MD,19.0,19.9,0.6)],
      [('m1',0,0),('m2',1,2),('m2b',1,2),('m3',3,4),('m3b',3,4),('m4',5,5),('m5',6,6)],f'{OVD}/mend.png',E,MD,'fade')
if 'y' in W:
    build('Vilvah_MilkBodyKit_9x16.mp4',[('st/body_wide.mp4',0,2.6,1,'','fade'),('st/body_wash.mp4',0,2.6,1,'','smoothup'),(LO,12.0,13.6,0.8,'crop=450:800:315:0','fade'),(LO,16.0,17.6,0.8,'crop=484:860:298:0','dissolve'),(LO,17.8,19.6,0.85,'crop=484:860:298:0','fade'),(LO,27.0,28.9,0.85,SQ)],
      [('y1',0,0),('y2',1,1),('y2b',1,1),('y3',2,3),('y3b',2,3),('y4',4,4),('y5',5,5)],f'{OVD}/yend.png',E,LO,'fade')
if 'l' in W:
    build('Vilvah_FaceLiftKit_9x16.mp4',[('st/lift_wide.mp4',0,2.6,1,'','fade'),(UE,4.0,5.0,0.6,SQ,'fade'),(UE,5.0,7.0,0.85,SQ,'dissolve'),(UE,8.0,9.8,0.85,SQ,'fade'),('st/lift_ultra.mp4',0,2.6,1,'','dissolve'),(UE,10.0,12.6,0.85,SQ)],
      [('l1',0,0),('l2',1,2),('l2b',1,2),('l3',3,3),('l4',4,4),('l4b',4,4),('l5',5,5)],f'{OVD}/lend.png',E,MD,'fade')
