from launch import LaunchDescription

from launch.actions import (
    IncludeLaunchDescription,
    DeclareLaunchArgument,
    OpaqueFunction,
)

from launch.substitutions import LaunchConfiguration
from launch.launch_description_sources import PythonLaunchDescriptionSource
from ament_index_python.packages import get_package_share_directory


def launch_setup(context, *args, **kwargs):

    mode = LaunchConfiguration("mode").perform(context)
    record = LaunchConfiguration("record").perform(context)

    configuration_directory = LaunchConfiguration("configuration_directory").perform(
        context
    )

    robot = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            get_package_share_directory("tirrex_demo") + "/launch/demo.launch.py"
        ),
        launch_arguments={
            "mode": mode,
            "configuration_directory": configuration_directory,
            "record" : record,
        }.items(),
    )

    return [robot]


def generate_launch_description():

    declared_arguments = []

    declared_arguments.append(DeclareLaunchArgument("mode", default_value="simulation"))

    declared_arguments.append(
        DeclareLaunchArgument(
            "configuration_directory",
            default_value=get_package_share_directory("tirrex_adap2e") + "/config",
        )
    )

    declared_arguments.append(DeclareLaunchArgument("record", default_value="false"))

    return LaunchDescription(
        declared_arguments + [OpaqueFunction(function=launch_setup)]
    )
