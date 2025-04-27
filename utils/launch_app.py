import os, platform, subprocess

def launch_app(exec):
    if platform.system() == "Linux":
        to_remove = ["%F", "%f", "%U", "%u", "@@u", "@@"]
        for word in to_remove:
            exec = exec.replace(word, "")

        execie = exec.strip().split()
        subprocess.Popen(execie)
    
    if platform.system() == "Windows":
        subprocess.Popen(rf"explorer shell:appsFolder\{exec}")


