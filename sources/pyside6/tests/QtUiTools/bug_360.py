#############################################################################
##
## Copyright (C) 2016 The Qt Company Ltd.
## Contact: https://www.qt.io/licensing/
##
## This file is part of the test suite of Qt for Python.
##
## $QT_BEGIN_LICENSE:GPL-EXCEPT$
## Commercial License Usage
## Licensees holding valid commercial Qt licenses may use this file in
## accordance with the commercial license agreement provided with the
## Software or, alternatively, in accordance with the terms contained in
## a written agreement between you and The Qt Company. For licensing terms
## and conditions see https://www.qt.io/terms-conditions. For further
## information use the contact form at https://www.qt.io/contact-us.
##
## GNU General Public License Usage
## Alternatively, this file may be used under the terms of the GNU
## General Public License version 3 as published by the Free Software
## Foundation with exceptions as appearing in the file LICENSE.GPL3-EXCEPT
## included in the packaging of this file. Please review the following
## information to ensure the GNU General Public License requirements will
## be met: https://www.gnu.org/licenses/gpl-3.0.html.
##
## $QT_END_LICENSE$
##
#############################################################################

import os
import sys
import unittest

from pathlib import Path
sys.path.append(os.fspath(Path(__file__).resolve().parents[1]))
from init_paths import init_test_paths
init_test_paths(False)

from helper.usesqapplication import UsesQApplication
from PySide6.QtWidgets import QFrame, QWidget
from PySide6.QtUiTools import QUiLoader


class MyQUiLoader(QUiLoader):
    def __init__(self, baseinstance):
        super().__init__()
        self.baseinstance = baseinstance
        self._widgets = []

    def createWidget(self, className, parent=None, name=""):
        widget = QUiLoader.createWidget(self, className, parent, name)
        self._widgets.append(widget)
        if parent is None:
            return self.baseinstance
        else:
            setattr(self.baseinstance, name, widget)
            return widget


class ButTest(UsesQApplication):
    def testCase(self):
        w = QWidget()
        loader = MyQUiLoader(w)

        filePath = os.path.join(os.path.dirname(__file__), 'minimal.ui')
        ui = loader.load(filePath)

        self.assertEqual(len(loader._widgets), 1)
        self.assertEqual(type(loader._widgets[0]), QFrame)


if __name__ == '__main__':
    unittest.main()

