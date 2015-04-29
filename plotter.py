#!/usr/bin/env python3
import matplotlib
import matplotlib.pyplot as plt
import pathlib
import csv

files = pathlib.Path(".").glob("LOG*.csv")

for p in files:
    with p.open() as f:
        reader = csv.DictReader(f)
        Acc_X = []
        Acc_Y = []
        Acc_Z = []
        Gyro_X = []
        Gyro_Y = []
        Gyro_Z = []
        Compass_X = []
        Compass_Y = []
        Compass_Z = []
        Lidar = []
        Temperature = []
        Time = []
        for row in reader:
            Acc_X.append(float(row["Acc X"]))
            Acc_Y.append(float(row["Acc Y"]))
            Acc_Z.append(float(row["Acc Z"]))
            Gyro_X.append(float(row["Gyro X"]))
            Gyro_Y.append(float(row["Gyro Y"]))
            Gyro_Z.append(float(row["Gyro Z"]))
            Compass_X.append(float(row["Compass X"]))
            Compass_Y.append(float(row["Compass Y"]))
            Compass_Z.append(float(row["Compass Z"]))
            Lidar.append(float(row["Lidar"]))
            Temperature.append(float(row["Temperature"]))
            Time.append(float(row["Time"])/1000)
        name = p.name[:-4]
        plt.clf()
        plt.plot(Time,Acc_X,label="X")
        plt.plot(Time,Acc_Y,label="Y")
        plt.plot(Time,Acc_Z,label="Z")
        plt.ylabel("Acceleration (Raw Accelerometer Value)")
        plt.xlabel("Time (Seconds)")
        plt.legend()
        plt.savefig(name+"-acceleration.png")

        plt.clf()
        plt.plot(Time,Gyro_X,label="X")
        plt.plot(Time,Gyro_Y,label="Y")
        plt.plot(Time,Gyro_Z,label="Z")
        plt.ylabel("Rotation (Raw Gyro Value)")
        plt.xlabel("Time (Seconds)")
        plt.legend()
        plt.savefig(name+"-gyro.png")

        plt.clf()
        plt.plot(Time,Compass_X,label="X")
        plt.plot(Time,Compass_Y,label="Y")
        plt.plot(Time,Compass_Z,label="Z")
        plt.ylabel("Rotation (Raw Compass Value)")
        plt.xlabel("Time (Seconds)")
        plt.legend()
        plt.savefig(name+"-compass.png")

        plt.clf()
        plt.plot(Time,Temperature)
        plt.ylabel("Temperature (Degrees Celcius)")
        plt.xlabel("Time (Seconds)")
        plt.savefig(name+"-temperature.png")

        plt.clf()
        plt.plot(Time,Lidar)
        plt.ylabel("Distance (cm)")
        plt.xlabel("Time (Seconds)")
        plt.savefig(name+"-lidar.png")
