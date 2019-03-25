import sys
import os
from PySide2 import QtCore, QtGui
from PySide2.QtWidgets import QLineEdit, QStylePainter
from PySide2.QtGui import QPaintEvent, QPainter, QPalette, QPen, QColor
from PySide2.QtCore import QPoint, QObject, Property, Qt


class MDLineEdit(QLineEdit):

    def __init__(self, *args, **kwargs):
        QLineEdit.__init__(self, *args, **kwargs)
        self._labelX = int()
        self._labelY = int()
        self._labelTextWidth = int()
        self._labelColor = QColor()
        self._labelFocusColor = QColor()
        self._label = str()
        self.setAttribute(Qt.WA_StyledBackground)

    def paintEvent(self, arg__1:QPaintEvent):
        QLineEdit.paintEvent(self, arg__1)

        p = QStylePainter(self)
        p.setRenderHint(QPainter.Antialiasing)

        pal = self.palette()
        # QPen pen;
        # QColor labelColor;
        if (self.hasFocus() and (not self.isReadOnly())):
            labelColor = self._labelFocusColor
        else:
            labelColor = pal.text().color()

        pen = QPen()
        pen.setColor(labelColor)
        p.setPen(pen)
        font = self.font()
        font.setPixelSize(self.readLabelTextWidth())
        p.setFont(font)
        p.drawText(QPoint(self._labelX, self._labelY), str(self._label))

    # @property
    def readLabelX(self):
        return self._labelX

    # @labelX.setter
    def writeLabelX(self, val: int):
        if val != self._labelX:
            self._labelX = val

    # @property
    def readLabelY(self):
        return self._labelY

    # @labelY.setter
    def writeLabelY(self, val: int):
        if val != self._labelY:
            self._labelY = val

    # @property
    def readLabelTextWidth(self):
        return self._labelTextWidth

    # @labelTextWidth.setter
    def writeLabelTextWidth(self, val):
        self._labelTextWidth = val

    # @property
    def readLabelColor(self):
        return self._labelColor

    # @labelColor.setter
    def writeLabelColor(self, val):
        self._labelColor = val

    # @property
    def readLabelFocusColor(self):
        return self._labelFocusColor

    # @labelFocusColor.setter
    def writeLabelFocusColor(self, val):
        self._labelFocusColor = val

    # @property
    def readLabel(self):
        return self._label

    # @label.setter
    def writeLabel(self, val: str):
        self._label = val

    # Q_PROPERTY(labelX READ readLabelX WRITE writeLabelX)
    labelX = Property(int, readLabelX, writeLabelX)
    labelY = Property(int, readLabelY, writeLabelY)
    labelTextWidth = Property(int, readLabelTextWidth, writeLabelTextWidth)
    labelColor = Property(QColor, readLabelColor, writeLabelColor)
    labelFocusColor = Property(QColor, readLabelFocusColor, writeLabelFocusColor)
    label = Property(str, readLabel, writeLabel)
