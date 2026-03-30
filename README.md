# JdeRobot-GSoC-2026
My Google Summer of Code 2026 application repository for JdeRobot. Includes the Follow Line exercise solution with adaptive PID control and my complete project proposal.

# JdeRobot GSoC 2026 - Follow Line Exercise

This repository contains my solution for the **Follow Line** exercise in JdeRobot's RoboticsAcademy, developed as part of my Google Summer of Code (GSoC) 2026 application.

## 🚀 Key Features of My Solution
Instead of a basic P or PD controller, I implemented several advanced mechanics to ensure smooth and robust navigation:
* **Adaptive PID Control:** The `Kp` value is dynamically adjusted based on the cross-track error. It becomes more aggressive in sharp turns and smoother on straight paths.
* **Asymmetric Braking & Acceleration:** The robot applies hard brakes (`0.8` factor) when entering curves but accelerates smoothly (`0.1` factor) to prevent slipping.
* **Real-time HUD Visualization:** Critical telemetry data (Speed, Error, Active Kp) is overlaid on the camera feed in real-time using OpenCV.

## 🎥 Demo Video
You can watch the robot successfully completing the track here: 
[Watch the Demo on YouTube](https://youtu.be/aZTyB_sHlaI)

## 📄 GSoC Proposal
My complete proposal for **Project #3: New Power Tower Inspection Using Deep Learning** can be found in this repository as a PDF file: `GSoC_2026_Proposal_Mustafa_Kerem_Guclu.pdf`.
