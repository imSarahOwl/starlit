import os, platform, subprocess
from xdg import DesktopEntry
from xdg.BaseDirectory import xdg_data_dirs


def _run_powershell_command(command):
    """Runs a PowerShell command and returns the output as a list of lines."""
    result = subprocess.run(
        ['powershell', '-Command', command],
        capture_output=True,
        text=True
    )
    return [line.strip() for line in result.stdout.splitlines() if line.strip()]

def get_apps():
    if platform.system() == "Linux":
        apps = []
        for data_dir in xdg_data_dirs:
            apps_dir = os.path.join(data_dir, "applications")
            if os.path.exists(apps_dir):
                for root, _, files in os.walk(apps_dir):
                    for file in files:
                        if file.endswith(".desktop"):
                            try:
                                entry = DesktopEntry.DesktopEntry(os.path.join(root, file))
                                if entry.getNoDisplay():
                                    continue
                                apps.append(entry)
                            except Exception:
                                pass
        return apps
                
    elif platform.system() == "Windows":
        class owl_app:
            def __init__(self, name, appID):
                self.name = name
                self.appID = appID
            
            def getName(self):
                return self.name

            def getExec(self):
                return self.appID

            
        names = _run_powershell_command('Get-StartApps | Select-Object -ExpandProperty Name')
        appids = _run_powershell_command('Get-StartApps | Select-Object -ExpandProperty AppID')

        apps = [owl_app(name, appid) for name, appid in zip(names, appids)]
        return apps
    


