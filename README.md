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

# 🚀 Revolt

✨ **Revolt: Open-Source Mobile Robotic Kit** ✨  

**Revolt** is a cutting-edge, open-source mobile robot Kit built for high-performance autonomous systems. Designed as a learning kit for robotics beginners, it provides a hands-on introduction to **ROS 2** and real-world hardware integration.  

🔧 **Key Features:**  
- Runs on **ROS 2**, enabling seamless robotics development.  
- Fully customizable—users can modify features, add new capabilities, and experiment with different configurations.  
- Includes **pre-designed 3D meshes** and CAD models, available in the `/meshes` directory, for easy customization.  
- Supports both **simulation and real-world deployment**, making it perfect for learning and prototyping.  

💡 Whether you're a beginner exploring **ROS 2** or an advanced user building autonomous systems, **Revolt** provides the perfect foundation for your robotics journey! 🚀

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
| **revolt_control 🎮** | Motor control, and movement algorithms. |
| **revolt_description 📐** | URDF and meshes for Revolt's 3D model and simulation. |
| **revolt_firmware 🖥️** | Low-level firmware managing hardware interactions. |
| **revolt_gz_classic 🏗️** | Integration with Gazebo Classic for simulation. |

<p align="center">
  <img src="docs/Revolt 1.2 Circuit Diagram_page-0001.jpg" style="height:800px; transform: rotate(90deg);" />
</p>

*Revolt's electronic system in action.*


## 🛠️ Installation

### Build from Source

#### Dependencies

1. Install [ROS 2](https://docs.ros.org/en/humble/Installation/Ubuntu-Install-Debians.html)
2. Install [colcon](https://colcon.readthedocs.io/en/released/user/installation.html)

#### colcon workspace

Packages here provided are colcon packages. As such a colcon workspace is expected:

1. Create colcon workspace

```
mkdir -p ~/ws/src
```

2. Clone this repository in the `src` folder

```
cd ~/ws/src
```

```
git clone https://github.com/KeneUkwueze/revolt_v2.git
```

3. Install dependencies via `rosdep`

```
cd ~/ws
```

```
rosdep install --from-paths src --ignore-src -i -y
```

4. Build the packages

```
colcon build
```

5. Finally, source the built packages
   If using `bash`:

```
source install/setup.bash
```

`Note`: Whether your are installing the packages in your dev machine or in your robot the procedure is the same. Remember to go over the assembly instructions first.



## 🎥 Demonstration

Watch Revolt in action on YouTube:
📺 [Revolt Demonstration Playlist](https://www.youtube.com/playlist?list=PLCbmpDw8dFjcA3yO1rBD3gkzvP6GnQTbm)
<iframe width="560" height="315" src="https://www.youtube.com/embed/tcmcyrkjlWY?si=aFnVfgFRzQszALwp" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

💡 *Revolt Robotics - Powering the Future of Autonomous Systems!*