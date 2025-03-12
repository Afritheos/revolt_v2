<div align="center">
  <picture>
    <source srcset="./docs/white_and_blue_logo.svg" media="(prefers-color-scheme: dark)" width="300">
    <source srcset="./docs/black_and_blue_logo.svg" media="(prefers-color-scheme: light)" width="300">
    <img src="./docs/white_and_blue_logo.svg" alt="Logo" width="300">
  </picture>
</div>

<br>

<p align="center">
<strong>ReVolt</strong> is a test differential drive robot designed for research and development.
It is fully integrated with ROS 2 and it is a great base platform for our continuous learning and development in the field of mobile robotics.
</p>

<p align="center">
  <img src="docs/revolt_cad.png" width=1000 />
</p>
# 🚀 Revolt Robotics

An advanced open-source robotics framework designed for high-performance autonomous systems. This repository contains the core packages needed to bring up, control, and simulate the **Revolt** robot.

![Revolt Electronics](path/to/your/image.png)  
*Revolt's electronic system in action.*

## 📌 Features

- **Seamless Bringup ⚡** - Easily initialize and configure Revolt.
- **Intelligent Control 🎮** - Advanced motion planning and control mechanisms.
- **Lifelike Simulation 🏗️** - Test and refine in a physics-based simulator.
- **High-Performance Firmware 🔧** - Optimized for real-time robotics applications.
- **Modular Design 🏗️** - Flexible architecture for easy expansion.

## 📦 Package Overview

| Package Name | Description |
|-------------|-------------|
| **revolt_base 🚀** | Core functionalities for the Revolt platform. |
| **revolt_bringup 🔧** | Scripts and launch files for booting up the system. |
| **revolt_control 🎮** | Motor control, PID tuning, and movement algorithms. |
| **revolt_description 📐** | URDF and meshes for Revolt's 3D model and simulation. |
| **revolt_firmware 🖥️** | Low-level firmware managing hardware interactions. |
| **revolt_gz_classic 🏗️** | Integration with Gazebo Classic for simulation. |

## 🛠️ Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/revolt.git
   cd revolt
   ```
2. Install dependencies:
   ```bash
   sudo apt update && sudo apt install -y ros-noetic-desktop-full
   ```
3. Build the workspace:
   ```bash
   catkin_make
   source devel/setup.bash
   ```

## 🎥 Demonstration

Watch Revolt in action on YouTube:
📺 [Revolt Demonstration Playlist](https://www.youtube.com/playlist?list=PLCbmpDw8dFjcA3yO1rBD3gkzvP6GnQTbm)

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

💡 *Revolt Robotics - Powering the Future of Autonomous Systems!*