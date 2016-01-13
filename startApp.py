import sys, modlistAPI
from PyQt4 import QtGui
from modlistGUI import Ui_mdlst
from modlistAPI import getInfo
gi = getInfo()
iterator = 0
app = QtGui.QApplication(sys.argv)
ui = Ui_mdlst()
ui.setupUi()
ui.show()
ui.iterator.setText(str(iterator+1)+'/'+str(modlistAPI.maxpages+1))
ui.name.setText(str(gi.getName(iterator)))
ui.other.setText(str(gi.getOther(iterator)))
ui.link.setText(str(gi.getLink(iterator)))
ui.desc.setText(str(gi.getDesc(iterator)))
ui.author.setText(str(gi.getAuthor(iterator)))
ui.type.setText(str(gi.getType(iterator)))
ui.dependencies.setText(str(gi.getDependencies(iterator)))
ui.versions.setText(str(gi.getVersions(iterator)))
ui.source.setText(str(gi.getSource(iterator)))
if iterator == 0:
    ui.backward.setVisible(False)
else:
    ui.backward.setVisible(True)
if iterator == modlistAPI.maxpages:
    ui.nextward.setVisible(False)
else:
    ui.nextward.setVisible(True)
sys.exit(app.exec_())
