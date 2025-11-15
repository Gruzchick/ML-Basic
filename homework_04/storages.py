class Storage:
    def save(self, file):
        raise NotImplementedError("Метод 'save' не реализован!")

    def load(self, file_name):
        raise NotImplementedError("Метод 'load' не реализован!")


class LocalStorage(Storage):
    def __init__(self, path="/var/data/"):
        self.path = path
        print(f"Initialized Local Storage at: {self.path}")

    def save(self, file):
        # Сохраняет файл на локальный диск.
        print(f"Saving '{file.name}' to local disk at '{self.path}'")
        print("Saved.")

    def load(self, file_name):
        # Загружает файл с локального диска.
        print(f"Loading '{file_name}' from local disk")
        return f"Content of {file_name}"


class S3Storage(Storage):
    def __init__(self, bucket_name):
        self.bucket = bucket_name
        print(f"Initialized S3 Storage for bucket: '{self.bucket}'")

    def save(self, file):
        # Сохраняет файл в облако S3.
        print(f"Uploading '{file.name}' to S3 bucket '{self.bucket}'")
        print("Uploaded.")

    def load(self, file_name):
        # Загружает файл из S3.
        print(f"Downloading '{file_name}' from S3 bucket '{self.bucket}'")
        return f"Content of {file_name} from S3"