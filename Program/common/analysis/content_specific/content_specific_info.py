#!/usr/bin/python3
from common.analysis.content_specific import specific_area_types


class ContentSpecificInfo:
    def __init__(self, specific_area):
        self._specific_area = specific_area

    @property
    def specific_area(self):
        return self._specific_area


class MusicSpecificInfo(ContentSpecificInfo):
    def __init__(self, band, genre, album):
        super().__init__(specific_area_types.MUSIC)
        self._band = band
        self._genre = genre
        self._album = album

    @property
    def band(self):
        return self._band

    @property
    def genre(self):
        return self._genre

    @property
    def album(self):
        return self._album


class TextSpecificInfo(ContentSpecificInfo):
    def __init__(self, specific_area, subject, language):
        super().__init__(specific_area)
        self._subject = subject
        self._language = language

    @property
    def subject(self):
        return self._subject

    @property
    def language(self):
        return self._language


class DocumentSpecificInfo(TextSpecificInfo):
    def __init__(self, subject, language):
        super().__init__(specific_area_types.DOCS, subject, language)


class BookSpecificInfo(TextSpecificInfo):
    def __init__(self, subject, language, genre, author):
        super().__init__(specific_area_types.BOOKS, subject, language)
        self._genre = genre
        self._author = author

    @property
    def genre(self):
        return self._genre

    @property
    def author(self):
        return self._author
