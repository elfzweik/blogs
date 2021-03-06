# Generated by Django 4.0.2 on 2022-03-08 21:54

from django.db import migrations
import wagtail.contrib.table_block.blocks
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.documents.blocks
import wagtail.embeds.blocks
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_alter_blogdetailpage_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogdetailpage',
            name='content',
            field=wagtail.core.fields.StreamField([('heading', wagtail.core.blocks.CharBlock(form_classname='full title')), ('paragraph', wagtail.core.blocks.RichTextBlock()), ('image', wagtail.images.blocks.ImageChooserBlock()), ('blockquote', wagtail.core.blocks.BlockQuoteBlock(label='Block Quote')), ('documentchooser', wagtail.documents.blocks.DocumentChooserBlock(label='Document Chooser')), ('url', wagtail.core.blocks.URLBlock(label='URL')), ('embed', wagtail.embeds.blocks.EmbedBlock(label='Embed')), ('rawhtml', wagtail.core.blocks.RawHTMLBlock(label='Raw HTML')), ('table', wagtail.contrib.table_block.blocks.TableBlock(label='Table'))], blank=True, null=True),
        ),
    ]
