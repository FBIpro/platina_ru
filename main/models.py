from django.db import models

# Create your models here.
class News(models.Model):
    name = models.CharField(max_length=30, verbose_name="Заголовок Новости")
    description = models.TextField(verbose_name="Описание")
    rating = models.FloatField(default=0, verbose_name="Рейтинг")
    url = models.URLField(verbose_name="Интернет-адрес", blank=True)
    photo = models.ImageField("Фото", upload_to="main/photos", default="", blank=True)
    date = models.DateTimeField(auto_now=False, verbose_name="Дата")


    class Meta:
        verbose_name="Новость"
        verbose_name_plural="Новости"

    def __str__(self):
        return self.name
