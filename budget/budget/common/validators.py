from django.core.exceptions import ValidationError


def validate_only_letters(value):
    for c in value:
        if not c.isalpha():
            raise ValidationError('Value must contain only letters')


def validate_file_max_size_in_mb(max_size):
    def validate(value):
        filesize = value.file.size
        if filesize > max_size * 1024 * 1024:
            raise ValidationError(f'Max file size is {max_size}MB')

    return validate
