#!/usr/bin/python3


class AnalysisResult:
    def __init__(self):
        self._is_directory = False
        self._name = None
        self._extension = None
        self._content_type = None
        self._size = None
        self._content_specific_info = None

    @property
    def is_directory(self):
        return self._is_directory

    @is_directory.setter
    def is_directory(self, value):
        self._is_directory = value

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def extension(self):
        return self._extension

    @extension.setter
    def extension(self, value):
        self._extension = value

    @property
    def content_type(self):
        return self._content_type

    @content_type.setter
    def content_type(self, value):
        self._content_type = value

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        self._size = value

    @property
    def content_specific_info(self):
        return self._content_specific_info

    @content_specific_info.setter
    def content_specific_info(self, value):
        self._content_specific_info = value
