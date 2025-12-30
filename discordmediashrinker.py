import sys, os, subprocess
if len(sys.argv) < 2:
    print("Usage: discordmediashrinker.py <input> [output]")
    sys.exit(0)
inp=sys.argv[1]
out=sys.argv[2] if len(sys.argv)>2 else "output.mp4"
if not os.path.isfile(inp):
    raise SystemExit("Input not found")
cmd=["ffmpeg","-y","-i",inp,"-vf","scale=1280:-2","-c:v","libx264","-crf","32","-pix_fmt","yuv420p","-an",out]
subprocess.run(cmd,check=True)
