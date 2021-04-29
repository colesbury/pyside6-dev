#!/usr/bin/env python

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

'''Using self.connect(signal, method)'''

import os
import sys
import unittest

from pathlib import Path
sys.path.append(os.fspath(Path(__file__).resolve().parents[1]))
from init_paths import init_test_paths
init_test_paths(False)

from PySide6.QtCore import QObject, SIGNAL, SLOT
from PySide6.QtWidgets import QPushButton, QWidget

from helper.usesqapplication import UsesQApplication


class SelfConnect(UsesQApplication):

    def testButtonClickClose(self):
        button = QPushButton()
        button.connect(button, SIGNAL('clicked()'), SLOT('close()'))

        button.show()
        self.assertTrue(button.isVisible())
        button.click()
        self.assertTrue(not button.isVisible())

    def testWindowButtonClickClose(self):
        button = QPushButton()
        window = QWidget()
        window.connect(button, SIGNAL('clicked()'), SLOT('close()'))

        window.show()
        self.assertTrue(window.isVisible())
        button.click()
        self.assertTrue(not window.isVisible())


if __name__ == '__main__':
    unittest.main()
