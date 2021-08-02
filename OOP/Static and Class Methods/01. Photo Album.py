from math import floor


class PhotoAlbum:
    def __init__(self, pages):
        self.pages = pages
        self.photos = [[] for _ in range(pages)]

    @classmethod
    def from_photos_count(cls, photos_count):
        current_pages = floor(photos_count / 4)
        return cls(current_pages)

    def add_photo(self, label):
        for row in range(len(self.photos)):
            if len(self.photos[row]) < 4:
                self.photos[row].append(label)
                return f"{label} photo added successfully on page {row + 1} slot {len(self.photos[row])}"
        return "No more free slots"

    def display(self):
        photos_mapper = {0:"", 1: "[]", 2: "[] []", 3: "[] [] []", 4: "[] [] [] []", 5: "-----------"}
        pages_str_repr_list = []
        for page in range(self.pages):
            pages_str_repr_list.append(photos_mapper[5])
            pages_str_repr_list.append(photos_mapper[len(self.photos[page])])
        pages_str_repr_list.append(photos_mapper[5])
        return "\n".join(pages_str_repr_list)

album = PhotoAlbum(2)

print(album.add_photo("baby"))
print(album.add_photo("first grade"))
print(album.add_photo("eight grade"))
print(album.add_photo("party with friends"))
print(album.photos)
print(album.add_photo("prom"))
print(album.add_photo("wedding"))

print(album.display())