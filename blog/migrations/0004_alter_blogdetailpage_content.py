# Generated by Django 4.0.2 on 2022-03-08 21:39

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_alter_blogpagegalleryimage_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogdetailpage',
            name='content',
            field=wagtail.core.fields.StreamField([('heading', wagtail.core.blocks.CharBlock(form_classname='full title')), ('paragraph', wagtail.core.blocks.RichTextBlock()), ('image', wagtail.images.blocks.ImageChooserBlock())], blank=True, null=True),
        ),
    ]
