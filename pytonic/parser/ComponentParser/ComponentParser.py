from pathlib import Path
import subprocess


component_identifier = Path(__file__).parent.absolute() / 'component_identifier.sh'
component_identifier = str(component_identifier)

def component_parser(file : str):
    return subprocess.run([component_identifier, file], stdout=subprocess.PIPE).stdout.decode('utf-8').strip().split()

if __name__ == "__main__":
    file="/home/caioaamaral/Workspace/mccr_ws/src/attraction_force_surface_gazebo"
    component_name, component_path, component_type = component_parser(file)
    print(component_name, component_path, component_type)
