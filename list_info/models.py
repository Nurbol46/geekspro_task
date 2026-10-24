from django.db import models


class Category(models.Model):
    name = models.CharField("Категории задач", max_length=100, unique=True, null=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class Tag(models.Model):
    name = models.CharField("Теги/Метки", max_length=100, unique=True, null=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Тег/Метка"
        verbose_name_plural = "Теги/Метки"


class Task(models.Model):
    title = models.CharField("Заголовок", max_length=100, null=False)
    description = models.TextField("Описание", null=True, blank=True)
    status = models.BooleanField("Статус выполнения", default=False)
    created_date = models.DateField("Дата создания", auto_now_add=True)

    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="tasks",
        verbose_name="Категория",
    )

    tags = models.ManyToManyField(
        Tag,
        blank=True,
        related_name="tasks",
        verbose_name="Теги/Метки",
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Задача"
        verbose_name_plural = "Задачи"
