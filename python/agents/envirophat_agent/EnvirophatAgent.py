# -*- coding: utf-8 -*-
"""

This file is part of **opensense** project https://github.com/opensense-network/.
    :platform: Unix, Windows, MacOS X
    :sinopsis: opensense

.. moduleauthor:: Max-R. Ulbricht (@maroulb)

License : GPL(v3)

**opensense** is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

**opensense** is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU General Public License for more details.
You should have received a copy of the GNU General Public License
along with opensense. If not, see http://www.gnu.org/licenses.

"""


from ...core.abstract_agent import *
import time
from envirophat import light, weather


class EnvirophatAgent(AbstractAgent):
    """
    A opensense donation agent for sending environmental data measured by an "Enviro_pHat" sensing board from pimoroni.
    """

    def __init__(self, configDir, osnInstance):
        AbstractAgent.__init__(self, configDir, osnInstance)

    def getPreferenceInfo(self):
        # TODO: check how to add PreferenceInfos into the right configFile
        return 4490
        pass

    def run(self):
        self.isRunning = True
        while True:
            self.sendValue(temp, ((weather.temperature()) - 4))
            self.sendValue(pressure, weather.pressure())
            self.sendValue(lumi, light.light())
            time.sleep(60)

    def discoverSensors(self):
        prefId = self.getPreferenceInfo()
        prefURL = 'http://consentcentral.org/' + str(prefId)
        self.addDefaultSensor(temp, "temperature", "celsius", {"usagePreferenceLink": str(prefURL)})
        self.addDefaultSensor(lumi, "luminance", "lux", {"usagePreferenceLink": str(prefURL)})
        self.addDefaultSensor(pressure, "air_pressure", "hPa", {"usagePreferenceLink": str(prefURL)})
        self.serializeConfig()

    def stop(self):
        self.isRunning = False
