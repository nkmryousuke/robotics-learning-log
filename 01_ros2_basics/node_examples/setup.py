from setuptools import find_packages, setup

package_name = 'node_examples'

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
    maintainer='naka',
    maintainer_email='nkmr.yousuke70351@gmail.com',
    description='TODO: Package description',
    license='Apache-2.0',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
    'console_scripts': [
        'circle_publisher = node_examples.circle_publisher:main',
        'pose_subscriber = node_examples.pose_subscriber:main',
        'wall_avoider = node_examples.wall_avoider:main',
        'param_circle = node_examples.param_circle:main',
        'speed_limiter = node_examples.speed_limiter:main',
        'pausable_driver = node_examples.pausable_driver:main',
        'turtle_spawner = node_examples.turtle_spawner:main',
        'fibonacci_server = node_examples.fibonacci_server:main',
        'rotate_client = node_examples.rotate_client:main',
        'square_patrol = node_examples.square_patrol:main',
    ],
    },
)
