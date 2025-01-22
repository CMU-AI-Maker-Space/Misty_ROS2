# Misty-ROS2
ROS2 Packages for Misty Robot

Install Misty Python [library](https://github.com/MistyCommunity/Wrapper-Python):
```
pip install mistyPy
```

Some functionalities on the Wrapper are outdated:
Replace the file at .local/lib/python3.8/site-packages/mistyPy/\__init__.py with this [updated version](https://github.com/CMU-AI-Maker-Space/Misty_ROS2/blob/main/__init__.py). In case some functionality is not working, use this [documentation](https://docs.mistyrobotics.com/misty-ii/web-api/overview/) as a reference to update any of the functionalities inside the Wrapper.


Clone the repository:
```
mkdir misty_ws
cd misty_ws
git clone --recursive https://github.com/CMU-AI-Maker-Space/Misty_ROS2.git
```


