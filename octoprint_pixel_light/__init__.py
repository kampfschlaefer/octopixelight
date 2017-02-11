# coding=utf-8
from __future__ import absolute_import

# This is a basic skeleton for your plugin's __init__.py. You probably want to
# adjust the class name of your plugin as well as the plugin mixins it's
# subclassing from. This is really just a basic skeleton to get you started,
# defining your plugin as a template plugin, settings and asset plugin. Feel
# free to add or remove mixins as necessary.
#
# Take a look at the documentation on what other plugin mixins are available.

import octoprint.plugin


class OctopixelightPlugin(
    octoprint.plugin.SettingsPlugin,
    octoprint.plugin.ProgressPlugin,
    octoprint.plugin.StartupPlugin,
    octoprint.plugin.ShutdownPlugin,
):

    # SettingsPlugin mixin
    def get_settings_defaults(self):
        return dict(
            # put your plugin's default settings here
            number_of_leds=4,
            bits_per_led=24,
        )

    def on_startup(self, host, port):
        self._logger.warn(
            "Should initialize the spidev here and initialize the digi-dot"
        )

    def on_shutdown(self):
        self._logger.warn("Should close the spidev here")

    def on_print_progress(self, location, path, progress):
        self._logger.warn(
            "Should light up the LEDs for progress of %s" % progress
        )

    # Softwareupdate hook
    def get_update_information(self):
        # Define the configuration for your plugin to use with the Software
        # Update Plugin here. See
        # https://github.com/foosel/OctoPrint/wiki/Plugin:-Software-Update
        # for details.
        return dict(
            octopixelight=dict(
                displayName="Octopixelight Plugin",
                displayVersion=self._plugin_version,

                # version check: github repository
                type="github_release",
                user="kampfschlaefer",
                repo="octopixelight",
                current=self._plugin_version,

                # update method: pip
                pip="https://github.com/kampfschlaefer/octopixelight/archive/"
                    "{target_version}.zip"
            )
        )


# If you want your plugin to be registered within OctoPrint under a different
# name than what you defined in setup.py ("OctoPrint-PluginSkeleton"), you may
# define that here. Same goes for the other metadata derived from setup.py that
# can be overwritten via __plugin_xyz__ control properties. See the
# documentation for that.
__plugin_name__ = "Octopixelight Plugin"
__plugin_implementation__ = OctopixelightPlugin()

# def __plugin_load__():
#     global __plugin_implementation__
#     __plugin_implementation__ = OctopixelightPlugin()
#
#     global __plugin_hooks__
#     __plugin_hooks__ = {
#         "octoprint.plugin.softwareupdate.check_config":
#             __plugin_implementation__.get_update_information
#     }
