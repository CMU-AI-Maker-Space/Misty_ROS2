from setuptools import find_packages, setup

import os
from glob import glob

package_name = 'misty_core'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        # ADDED
        (os.path.join('share', package_name), glob('launch/*launch.[pxy][yma]*')),
         # END ADDED
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='rlc',
    maintainer_email='rlc@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
                'misty_low_level = misty_core.misty_low_level:main',
        ],
    },
)
