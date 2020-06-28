#carregando modulos do script
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from qgis.core import *
from qgis.gui import *
import processing
import sys

#carregando layers para a interface
lim_est_TO = "/home/gabriel/qgis/LimiteEstado/LimiteEstado.shp"
hid_est_TO = "/home/gabriel/qgis/Hidrografia/Hidrografia.shp"
iface.addVectorLayer(lim_est_TO, "Limite Estado", "ogr")
iface.addVectorLayer(hid_est_TO, "Hidrografia Estado", "ogr")

#selecionando aspectos unicos
#shapefile Hidrografia.shp (NM_IDENTIF)
hid_select = "/home/gabriel/qgis/rio_to.shp"
processing.runalg("qgis:extractbyattribute", hid_est_TO, "NM_IDENTIF", 0, "Rio Tocantins", hid_select)

#selecionando shape unico
hid_SIRGAS = "/home/gabriel/qgis/hid_SIRGAS.shp"
processing.runalg("qgis:reprojectlayer", hid_est_TO, "epsg:4618", hid_SIRGAS)
hid_TO     = "/home/gabriel/qgis/hid_TO.shp"
processing.runalg("qgis:clip", hid_SIRGAS, hid_select, hid_TO)
iface.addVectorLayer(hid_TO, "Rio Tocantins e Estado", "ogr")
