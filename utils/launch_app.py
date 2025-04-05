import os, platform, subprocess

def launch_app(exec):
    if platform.system() == "Linux":
        subprocess.Popen(exec.replace("%F", "").replace("%f", "").replace("%U", "").replace("%u", "").strip())
    
    if platform.system() == "Windows":
        subprocess.Popen(rf"explorer shell:appsFolder\{exec}")


