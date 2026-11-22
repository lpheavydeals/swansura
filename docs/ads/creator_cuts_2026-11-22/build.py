# Creator cuts (22 Nov 2026; permission from the brands/creators confirmed by the user 21 Nov).
# python3 build.py <src dir with d01.mp4 …> <music mp4>  ->  <name>_9x16.mp4 (1080x1920, 30 fps)
# Each video: kept segments (claim / 'comment link' / 'US launch' lines cut), optional blurs (burned-in claim captions,
# 'India's most searched' badge), Swansura pill on top, 4 s end card (VD10, next-day, T&Cs). music=True replaces the audio.
import subprocess,sys
SRC,MUSIC=sys.argv[1],sys.argv[2]
V={
 'Deyga_LipBalmStick_Creator':dict(src='d04',seg=[(0,13.0),(19.22,27.95)],blur=[],music=False),
 'Deyga_RiceWaterDuo_Creator':dict(src='d08',seg=[(0,29.55)],blur=[],music=False),
 'Vilvah_FaceBrightening_Creator':dict(src='v10',seg=[(0,20.4)],blur=[],music=True,moff=0),
 'Deyga_Unboxing_Creator':dict(src='d01',seg=[(0,28.9)],blur=[],music=False),
 'Deyga_LipBalmMaking_Creator':dict(src='d09',seg=[(0,17.6)],blur=[(470,0,250,170,0,99)],music=True,moff=6),
}
END=4.0
ONLY=sys.argv[3:] or list(V)
for name,c in V.items():
    if name not in ONLY: continue
    f=f"{SRC}/{c['src']}.mp4";fc=[];segs=c['seg'];n=len(segs)
    base='[0:v]'
    for i,(x,y,w,h,a,b) in enumerate(c['blur']):
        fc.append(f"{base}split[bb{i}][bs{i}];[bs{i}]crop={w}:{h}:{x}:{y},boxblur=18:2[bl{i}];[bb{i}][bl{i}]overlay={x}:{y}:enable='between(t,{a},{b})'[vb{i}]");base=f'[vb{i}]'
    fc.append(f"{base}split={n}"+''.join(f'[vs{i}]' for i in range(n)))
    for i,(a,b) in enumerate(segs):
        fc.append(f"[vs{i}]trim={a}:{b},setpts=PTS-STARTPTS,scale=1080:1920,fps=30,setsar=1[v{i}]")
        if not c['music']: fc.append(f"[0:a]atrim={a}:{b},asetpts=PTS-STARTPTS,afade=t=in:d=0.04,afade=t=out:st={b-a-0.06:.2f}:d=0.06[a{i}]")
    total=sum(b-a for a,b in segs)
    fc.append(''.join(f'[v{i}]' for i in range(n))+f"concat=n={n}:v=1:a=0[vc]")
    fc.append(f"[vc][2:v]overlay=0:240[vp]")
    fc.append(f"[1:v]scale=1080:1920,fps=30,setsar=1,trim=0:{END},setpts=PTS-STARTPTS,fade=t=in:d=0.35[ve]")
    fc.append("[vp][ve]concat=n=2:v=1:a=0[vout]")
    if c['music']:
        fc.append(f"[3:a]atrim={c['moff']}:{c['moff']+total+END},asetpts=PTS-STARTPTS,afade=t=in:d=0.3,afade=t=out:st={total+END-1.2:.2f}:d=1.2[aout]")
    else:
        fc.append(''.join(f'[a{i}]' for i in range(n))+f"concat=n={n}:v=0:a=1[ac]")
        fc.append(f"[3:a]atrim=20:{20+END},asetpts=PTS-STARTPTS,volume=0.35,afade=t=in:d=0.4,afade=t=out:st={END-1:.2f}:d=1[ae]")
        fc.append("[ac][ae]concat=n=2:v=0:a=1[aout]")
    fc[-1]=fc[-1].replace('[aout]','[araw]');fc.append('[araw]loudnorm=I=-14:TP=-1.5:LRA=11[aout]')
    cmd=['ffmpeg','-v','error','-y','-i',f,'-loop','1','-t',str(END),'-i','end.png','-i','pill.png','-i',MUSIC,'-filter_complex',';'.join(fc),
         '-map','[vout]','-map','[aout]','-c:v','libx264','-preset','slow','-crf','19','-pix_fmt','yuv420p','-c:a','aac','-b:a','160k','-ar','48000','-movflags','+faststart',f'{name}_9x16.mp4']
    r=subprocess.run(cmd,capture_output=True,text=True);print(name,'ERR '+r.stderr[-600:] if r.returncode else 'ok',flush=True)
