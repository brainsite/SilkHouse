# -*- coding: utf-8 -*-

from django.db import models

# Create your models here.


class Colors(models.Model):
    title = models.CharField(u'Название', max_length=128)
    alias = models.CharField(u'Алиас', max_length=128, blank=True)
    translate = models.CharField(u'Цвет', max_length=128)
    code = models.CharField(u'Hex code', max_length=8)

    def __str__(self):
            return u'{}'.format(self.translate)

    class Meta:
        ordering = ['title']
        verbose_name = u'Цвет'
        verbose_name_plural = u'Цвета'

    def color_box(self):
        return '<div class="color_box" style="background-color:{};"></div>'.format(self.code)
    color_box.short_description = 'Demo'
    color_box.allow_tags = True

COLORS_HELP_TABLE = """
<table>
  <tr>
    <td>aqua</td>
    <td>black</td>
    <td>blue</td>
    <td>fuchsia</td>
    <td>gray</td>
    <td>green</td>
    <td>lime</td>
    <td>maroon</td>
    <td>navy</td>
    <td>olive</td>
    <td>purple</td>
    <td>red</td>
    <td>silver</td>
    <td>teal</td>
    <td>white</td>
    <td>yellow</td>
  </tr>
  <tr>
    <td>cyan</td>
    <td></td>
    <td></td>
    <td>magenta</td>
    <td></td>
    <td></td>
    <td>lightgreen</td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td style="background-color:#00ffff"></td>
    <td style="background-color:#000000"></td>
    <td style="background-color:#0000ff"></td>
    <td style="background-color:#ff00ff"></td>
    <td style="background-color:#808080"></td>
    <td style="background-color:#008000"></td>
    <td style="background-color:#00ff00"></td>
    <td style="background-color:#800000"></td>
    <td style="background-color:#000080"></td>
    <td style="background-color:#808000"></td>
    <td style="background-color:#800080"></td>
    <td style="background-color:#ff0000"></td>
    <td style="background-color:#c0c0c0"></td>
    <td style="background-color:#008080"></td>
    <td style="background-color:#ffffff"></td>
    <td style="background-color:#ffff00"></td>
  </tr>

  <tr>
    <td>морская волна</td>
    <td>чёрный</td>
    <td>синий</td>
    <td>фуксия</td>
    <td>серый</td>
    <td>зелёный</td>
    <td>лайм</td>
    <td>тёмно-бордовый</td>
    <td>тёмно-синий</td>
    <td>оливковый</td>
    <td>пурпурный</td>
    <td>красный</td>
    <td>серебряный</td>
    <td>сине-зелёный</td>
    <td>белый</td>
    <td>жёлтый</td>
  </tr>
</table>
"""