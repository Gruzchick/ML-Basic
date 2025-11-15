from datetime import datetime
from media_files import ImageFile, VideoFile, AudioFile
from storages import LocalStorage, S3Storage

now = datetime.now().strftime("%Y-%m-%d")

# Создаем фото
my_photo = ImageFile(
    name="cat.jpg",
    size=2.5,
    created_at=now,
    owner="John Doe",
    resolution="4032x3024",
    format_="JPEG"
)

# Создаем видео
my_video = VideoFile(
    name="vacation.mp4",
    size=150.0,
    created_at=now,
    owner="John Doe",
    duration=92,
    resolution="1920x1080",
    format_="mp4",
)

# Создаем аудио
my_audio = AudioFile(
    name="song.mp3",
    size=4.1,
    created_at=now,
    owner="Alice",
    duration=185,
    artist="The Pythonistas"
)

my_photo.display_info()
my_photo.resize("800x600")

my_video.convert(to_format="avi")

features = my_audio.extract_features()

local_storage = LocalStorage()
cloud_storage = S3Storage(bucket_name="my-media-bucket")

local_storage.save(my_photo)

cloud_storage.save(my_video)

my_audio.delete()
