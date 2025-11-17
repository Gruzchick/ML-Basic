# Базовый класс, для всех медиа-файлов
class MediaFile:
    def __init__(self, name, size, created_at, owner):
        self.name = name
        self.size = size
        self.created_at = created_at
        self.owner = owner

    def display_info(self):
        # Выводит в консоль информацию о файле
        print(f"File: {self.name}, Size: {self.size}MB, Created: {self.created_at}, Owner: {self.owner}")

    # Общие действия, которые можно делать с любым файлом
    def delete(self):
        # Удаляет файл
        print(f"File '{self.name}' deleted.")

class ImageFile(MediaFile):
    def __init__(self, name, size, created_at, owner, resolution, format_):
        super().__init__(name, size, created_at, owner)
        self.resolution = resolution
        self.format = format_

    def resize(self, new_resolution):
        # Изменяет размер изображения.
        print(f"Resizing image '{self.name}' to {new_resolution}")
        self.resolution = new_resolution
        print("Image resized.")


class VideoFile(MediaFile):
    def __init__(self, name, size, created_at, owner, duration, resolution, format_):
        super().__init__(name, size, created_at, owner)
        self.duration = duration
        self.resolution = resolution
        self.format = format_

    def convert(self, to_format):
        # Конвертирует видео в другой формат.
        print(f"Converting video '{self.name}' to {to_format}...")
        self.format = to_format
        print("Video converted.")


class AudioFile(MediaFile):
    def __init__(self, name, size, created_at, owner, duration, artist):
        super().__init__(name, size, created_at, owner)
        self.duration = duration
        self.artist = artist

    def extract_features(self):
        # Извлекает фичи из аудио, например.
        print(f"Extracting features from audio '{self.name}' by {self.artist}...")