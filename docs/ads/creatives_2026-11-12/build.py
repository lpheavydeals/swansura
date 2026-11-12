import subprocess,sys,os
OVD=os.environ.get('OVD','ov')
V='scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,fps=30,setsar=1,format=yuv420p'
def seg(src,ss,to,speed=1.0,extra=''):
    f=f"trim={ss}:{to},setpts=(PTS-STARTPTS)/{speed},{extra+',' if extra else ''}{V}"
    return f
def build(name,segs,ovs,endpng,endlen,audio,a_ss=0):
    inputs=[];fc=[];labels=[];n=[0]
    def add(*a):
        inputs.extend(a);n[0]+=1;return n[0]-1
    srcs=[]
    for s in segs:
        if s[0] not in srcs: srcs.append(s[0])
    sidx={s:add('-i',s) for s in srcs}
    uses={s:sum(1 for x in segs if x[0]==s) for s in srcs}
    for s in srcs: fc.append(f"[{sidx[s]}:v]split={uses[s]}"+''.join(f'[u{sidx[s]}_{k}]' for k in range(uses[s])))
    cnt={s:0 for s in srcs}
    t=0;parts=[]
    for i,s in enumerate(segs):
        src,ss,to,sp=s[:4];blur=len(s)>4 and s[4];pre=s[5] if len(s)>5 else ''
        lab=f'u{sidx[src]}_{cnt[src]}';cnt[src]+=1
        fc.append(f"[{lab}]{seg(src,ss,to,sp,pre)}[s{i}]")
        dur=(to-ss)/sp
        if blur:
            mi=add('-loop','1','-i',f'{OVD}/mask.png')
            fc.append(f"[{mi}:v]crop=860:440:110:850,format=gray,trim=duration={dur}[m{i}]")
            fc.append(f"[s{i}]split[a{i}][b{i}];[b{i}]crop=860:440:110:850,boxblur=40:4,format=rgba[bl{i}];[bl{i}][m{i}]alphamerge[bm{i}];[a{i}][bm{i}]overlay=110:850[sb{i}]")
            parts.append(f"[sb{i}]")
        else: parts.append(f"[s{i}]")
        t+=dur
    body=t
    fc.append(f"{''.join(parts)}concat=n={len(parts)}:v=1:a=0,fps=30,settb=1/30[body]")
    # end card
    ei=add('-loop','1','-t',str(endlen+0.5),'-i',endpng)
    fc.append(f"[{ei}:v]scale=1080:1920,fps=30,format=yuv420p,setsar=1,settb=1/30[end]")
    fc.append(f"[body][end]xfade=transition=fade:duration=0.4:offset={body-0.4:.3f}[base]")
    total=body-0.4+endlen+0.5
    cur='base'
    for k,ov in enumerate(ovs):
        png,a,b=ov[:3];fin,fout=(ov[3],ov[4]) if len(ov)>3 else (1,1)
        oi=add('-loop','1','-t',str(total),'-i',f'{OVD}/{png}.png')
        fl=['format=rgba']+([f"fade=in:st={a}:d=0.22:alpha=1"] if fin else [])+([f"fade=out:st={b-0.2}:d=0.2:alpha=1"] if fout else [])
        fc.append(f"[{oi}:v]{','.join(fl)}[o{k}]")
        y=f"'if(lt(t,{a}),36,if(lt(t,{a+0.35}),36*(1-(t-{a})/0.35)^2,0))'" if fin else "0"
        fc.append(f"[{cur}][o{k}]overlay=x=0:y={y}:enable='between(t,{a},{b})':eval=frame[c{k}]")
        cur=f"c{k}"
    ai=add('-ss',str(a_ss),'-i',audio)
    fc.append(f"[{ai}:a]atrim=0:{total:.3f},asetpts=PTS-STARTPTS,afade=t=in:d=0.15,afade=t=out:st={total-1.2:.3f}:d=1.2,loudnorm=I=-14:TP=-1.5:LRA=11[aud]")
    cmd=['ffmpeg','-v','error','-y',*inputs,'-filter_complex',';'.join(fc),'-map',f'[{cur}]','-map','[aud]','-t',f'{total:.3f}',
         '-c:v','libx264','-preset','slow','-crf','18','-profile:v','high','-pix_fmt','yuv420p','-movflags','+faststart','-c:a','aac','-b:a','192k','-ar','48000',name]
    subprocess.run(cmd,check=True);print(name,round(total,2))
D='../dv/Deyga_Organics_V15_Beetroot_Lipbalm.mp4'
M='../vv/Milk_Drops_Serum__Milk_Drops_-_Product_1080x1920.mp4'
S='../vv/MDS_20ml__milk_drop.mp4'
if 'd' in sys.argv[1:]:
    build(os.environ.get('PFX','')+'Deyga_Beetroot_LipBalm_9x16.mp4',[(D,0,10.6,1),(D,11.6,14.6,1)],
      [('d1',0.15,2.3),('d2a',2.5,3.3,1,0),('d2b',3.3,4.1,0,0),('d2c',4.1,6.0,0,1),('d3a',6.3,8.3),('d3b',8.35,10.5),('d4',10.8,13.1)],
      f'{OVD}/dend.png',3.2,D)
F='../vv/Face_Brightening_Combo__FBC_Vertical.mp4'
A='../vv/AM_PM_Combo__AM_PM_Combo_1080X1920.mp4'
if 'v' in sys.argv[1:]:
    build(os.environ.get('PFX','')+'Vilvah_MilkDrops_9x16.mp4',[(M,7.0,8.4,0.75),(M,11.0,11.9,0.75),(F,7.5,8.9,0.8,False,'crop=828:1472:126:448'),(A,8.0,9.4,0.8),(M,15.0,15.9,0.8),(M,19.0,19.9,0.55)],
      [('v1',0.1,1.8),('v2',1.95,3.07,1,0),('v3',3.07,4.75,0,1),('vs1',4.85,6.5),('vs2',6.6,7.62),('vs3',7.72,9.2),('v5',7.72,9.2)],
      f'{OVD}/vend.png',3.2,M)
