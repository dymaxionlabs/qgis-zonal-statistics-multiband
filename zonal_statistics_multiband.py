# -*- coding: utf-8 -*-

"""
/***************************************************************************
 ZonalStatisticsMultiband
                                 A QGIS plugin
 Extends Zonal Statistics official plugin with multiband raster support
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                              -------------------
        begin                : 2019-01-30
        copyright            : (C) 2019 by Dymaxion Labs
        email                : damian@dymaxionlabs.com
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""

__author__ = 'Dymaxion Labs'
__date__ = '2019-01-30'
__copyright__ = '(C) 2019 by Dymaxion Labs'

# This will get replaced with a git SHA1 when you do a git archive

__revision__ = '$Format:%H$'

import os
import sys
import inspect

from qgis.core import QgsProcessingAlgorithm, QgsApplication
from .ZonalStatisticsMultiband_provider import ZonalStatisticsMultibandProvider

cmd_folder = os.path.split(inspect.getfile(inspect.currentframe()))[0]

if cmd_folder not in sys.path:
    sys.path.insert(0, cmd_folder)


class ZonalStatisticsMultibandPlugin(object):

    def __init__(self):
        self.provider = ZonalStatisticsMultibandProvider()

    def initGui(self):
        QgsApplication.processingRegistry().addProvider(self.provider)

    def unload(self):
        QgsApplication.processingRegistry().removeProvider(self.provider)