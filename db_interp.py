import os
import statistics as st

axial = []
normal = []

# Collect data.
cfd_directory = "<INSERT CFD DIRECTORY>"
for file in os.listdir(cfd_directory):
    path = os.path.join(cfd_directory, file)
    angle_of_actuation = float(file.split("_")[1][:-7])
    angle_of_attack = float(file.split("_")[2])
    mach_number= float(file.split("_")[3])

    forces = None
    with open(path, "r") as fp:
        forces = fp.readlines()
    qforces = [float(forces[-i].strip().split(" ")[1]) for i in range(10, 0, -1)]
    forces = qforces

    if st.stdev(qforces) < 1
      if file.endswith("axial"):
        axial.append([angle_of_actuation, angle_of_attack, mach_number, forces])
      elif file.endswith("normal"):
        normal.append([angle_of_actuation, angle_of_attack, mach_number, forces])
