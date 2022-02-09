from django.core.exceptions import ValidationError


def validate_letters_only(value):
    for ch in value:
        if not ch.isalpha():
            raise ValidationError('value must contain letters only')


def validate_file_max_mb_size(max_size):
    def validate(value):
        filesize = value.file.size
        if filesize > max_size * 1024 * 1024:
            raise ValidationError(f"Max file size is {max_size}MB")
        return validate
