# Generated by Django 2.2.4 on 2021-07-19 22:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300, verbose_name='nombre')),
                ('primaryCategory', models.BooleanField(default=False, verbose_name='Categoria primaria')),
            ],
        ),
        migrations.CreateModel(
            name='Ecommerce',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, verbose_name='Nombre de Tienda')),
                ('logo', models.ImageField(upload_to='ecommerce_logo/', verbose_name='Logo de Empresa')),
                ('phone', models.CharField(max_length=250, verbose_name='Telefono')),
                ('email', models.EmailField(max_length=254)),
                ('descripcion', models.TextField(max_length=500, verbose_name='Descripción')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='owner', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300, verbose_name='Nombre de Producto')),
                ('slug', models.SlugField()),
                ('price', models.FloatField(verbose_name='Precio')),
                ('discount_price', models.FloatField(blank=True, null=True, verbose_name='Precio con Descuento')),
                ('preview_text', models.TextField(max_length=250, verbose_name='Texto Previo')),
                ('detail_text', models.TextField(max_length=1000, verbose_name='Detalle de Producto')),
                ('image_product', models.ImageField(blank=True, upload_to='products/', verbose_name='Imagen de producto')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.Category', verbose_name='Categoria')),
                ('ecommerce', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.Ecommerce', verbose_name='Nombre de Tienda')),
            ],
        ),
        migrations.CreateModel(
            name='ImagesCover',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cover', models.ImageField(upload_to='covers/', verbose_name='cover')),
                ('ecommerce', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.Ecommerce')),
            ],
        ),
        migrations.CreateModel(
            name='AttributeProduct',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attribute', models.CharField(max_length=250, verbose_name='Atributo')),
                ('value', models.CharField(max_length=250, verbose_name='valor')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.Product', verbose_name='Producto')),
            ],
        ),
    ]
