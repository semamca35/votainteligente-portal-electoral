# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-10-05 22:16
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import picklefield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('popular_proposal', '0027_auto_20170914_1841'),
        ('backend_candidate', '0004_candidacycontact_initial_password'),
    ]

    operations = [
        migrations.CreateModel(
            name='IncrementalsCandidateFilter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=12288, null=True)),
                ('text', models.TextField()),
                ('filter_qs', picklefield.fields.PickledObjectField(editable=False)),
                ('exclude_qs', picklefield.fields.PickledObjectField(editable=False)),
            ],
            options={
                'verbose_name': 'Filtro de propuestas para candidatos',
                'verbose_name_plural': 'Filtros de propuestas para candidatos',
            },
        ),
        migrations.CreateModel(
            name='ProposalSuggestionForIncremental',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sent', models.BooleanField(default=False)),
                ('incremental', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='suggestions', to='backend_candidate.IncrementalsCandidateFilter')),
                ('proposal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='suggested_proposals', to='popular_proposal.PopularProposal')),
            ],
        ),
        migrations.AddField(
            model_name='incrementalscandidatefilter',
            name='suggested_proposals',
            field=models.ManyToManyField(through='backend_candidate.ProposalSuggestionForIncremental', to='popular_proposal.PopularProposal'),
        ),
    ]
