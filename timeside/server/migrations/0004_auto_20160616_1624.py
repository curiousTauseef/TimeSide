# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-16 14:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0003_auto_20160616_1244'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='analysistrack',
            options={'verbose_name': 'Analysis Track'},
        ),
        migrations.AlterModelOptions(
            name='subprocessor',
            options={'verbose_name': 'Subprocessor'},
        ),
        migrations.RenameField(
            model_name='analysistrack',
            old_name='sub_processor_id',
            new_name='sub_processor',
        ),
        migrations.AlterField(
            model_name='processor',
            name='pid',
            field=models.CharField(choices=[(b'Analyzers', [(b'vamp_simple_host', b'vamp_simple_host'), (b'aubio_melenergy', b'aubio_melenergy'), (b'aubio_mfcc', b'aubio_mfcc'), (b'aubio_pitch', b'aubio_pitch'), (b'aubio_specdesc', b'aubio_specdesc'), (b'aubio_temporal', b'aubio_temporal'), (b'yaafe', b'yaafe'), (b'spectrogram_analyzer', b'spectrogram_analyzer'), (b'onset_detection_function', b'onset_detection_function'), (b'spectrogram_analyzer_buffer', b'spectrogram_analyzer_buffer'), (b'waveform_analyzer', b'waveform_analyzer'), (b'mean_dc_shift', b'mean_dc_shift'), (b'level', b'level')]), (b'Graphers', [(b'grapher_aubio_pitch', b'grapher_aubio_pitch'), (b'grapher_onset_detection_function', b'grapher_onset_detection_function'), (b'grapher_waveform', b'grapher_waveform'), (b'spectrogram_log', b'spectrogram_log'), (b'spectrogram_lin', b'spectrogram_lin'), (b'waveform_simple', b'waveform_simple'), (b'waveform_centroid', b'waveform_centroid'), (b'waveform_contour_black', b'waveform_contour_black'), (b'waveform_contour_white', b'waveform_contour_white'), (b'waveform_transparent', b'waveform_transparent')]), (b'Encoders', [(b'live_encoder', b'live_encoder'), (b'flac_encoder', b'flac_encoder'), (b'aac_encoder', b'aac_encoder'), (b'mp3_encoder', b'mp3_encoder'), (b'vorbis_encoder', b'vorbis_encoder'), (b'opus_encoder', b'opus_encoder'), (b'wav_encoder', b'wav_encoder'), (b'webm_encoder', b'webm_encoder')])], max_length=128, unique=True, verbose_name='pid'),
        ),
        migrations.AlterModelTable(
            name='analysistrack',
            table='timeside_analysistracks',
        ),
        migrations.AlterModelTable(
            name='subprocessor',
            table='timeside_subprocessors',
        ),
    ]