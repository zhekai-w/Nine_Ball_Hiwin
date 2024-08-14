from setuptools import find_packages, setup

package_name = 'hiwin_control'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='zack',
    maintainer_email='zack@todo.todo',
    description='TODO: Package description',
    license='Apache-2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'arm_controller = hiwin_control.arm_controller:main',
            'team_selection = hiwin_control.team_selection:main',
            'testbeat_arm_controller = hiwin_control.testbeat_arm_controller:main',
            'pool_arm_controller = hiwin_control.pool_arm_controller:main',
            'nine_arm_controller = hiwin_control.nine_arm_controller:main',
            'rush_arm_controller = hiwin_control.rush_arm_controller:main',
            'yyy_arm_controller = hiwin_control.yyy_arm_controller:main',
            'stream_rs = hiwin_control.stream_rs:main',
            'pool_arm_controller = hiwin_control.pool_arm_controller:main',
        ],
    },
)
