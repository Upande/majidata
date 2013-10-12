# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Apopdenavgminmaxcounty'
        db.create_table(u'APopDenAvgMinMaxCounty', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('countyname', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'Countyname')),
            ('countyid', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'CountyID', blank=True)),
            ('avgsqkm', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'AvgSqKm', blank=True)),
            ('avgpopden', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'AvgPopDen', blank=True)),
            ('nareas', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'NAreas', blank=True)),
            ('max', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'Max', blank=True)),
            ('min', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'Min', blank=True)),
        ))
        db.send_create_signal(u'majitables', ['Apopdenavgminmaxcounty'])

        # Adding model 'Apopdenavgminmaxslum'
        db.create_table(u'APopDenAvgMinMaxSlum', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('slumname', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'Slumname')),
            ('slumid', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'SlumID')),
            ('avgsqkm', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'AvgSqKm', blank=True)),
            ('avgpopden', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'AvgPopDen', blank=True)),
            ('nareas', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'NAreas', blank=True)),
            ('max', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'Max', blank=True)),
            ('min', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'Min', blank=True)),
        ))
        db.send_create_signal(u'majitables', ['Apopdenavgminmaxslum'])

        # Adding model 'Apopdenavgminmaxtown'
        db.create_table(u'APopDenAvgMinMaxTown', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('townname', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('townid', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'townID', blank=True)),
            ('avgsqkm', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'AvgSqKm', blank=True)),
            ('avgpopden', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'AvgPopDen', blank=True)),
            ('nareas', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'NAreas', blank=True)),
            ('max', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'Max', blank=True)),
            ('min', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'Min', blank=True)),
        ))
        db.send_create_signal(u'majitables', ['Apopdenavgminmaxtown'])

        # Adding model 'Apopdennareascounty'
        db.create_table(u'APopDenNAreasCounty', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('countyid', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'countyID', blank=True)),
            ('countyname', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('popden', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'PopDen')),
            ('nareas', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'NAreas', blank=True)),
            ('pcntareas', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'PcntAreas', blank=True)),
            ('totareas', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'TotAreas', blank=True)),
        ))
        db.send_create_signal(u'majitables', ['Apopdennareascounty'])

        # Adding model 'Apopdennareasslum'
        db.create_table(u'APopDenNAreasSlum', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('slumid', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'slumID', blank=True)),
            ('slumname', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('popden', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'PopDen')),
            ('nareas', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'NAreas', blank=True)),
            ('pcntareas', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'PcntAreas', blank=True)),
            ('totareas', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'TotAreas', blank=True)),
        ))
        db.send_create_signal(u'majitables', ['Apopdennareasslum'])

        # Adding model 'Apopdennareastowns'
        db.create_table(u'APopDenNAreasTowns', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('townid', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'townID', blank=True)),
            ('townname', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('popden', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'PopDen')),
            ('nareas', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'NAreas', blank=True)),
            ('pcntareas', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'PcntAreas', blank=True)),
            ('totareas', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'TotAreas', blank=True)),
        ))
        db.send_create_signal(u'majitables', ['Apopdennareastowns'])

        # Adding model 'Areadustatuscounty'
        db.create_table(u'AreaDUStatusCounty', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('countyid', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'CountyID', blank=True)),
            ('countyname', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'CountyName')),
            ('dustatus', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'DUStatus')),
            ('nareas', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'Nareas', blank=True)),
            ('smpdus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'SmpDUs', blank=True)),
            ('pcntdus', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'pcntDUs', blank=True)),
            ('dusinarea', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'DusInArea', blank=True)),
            ('totdus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'TotDUs', blank=True)),
        ))
        db.send_create_signal(u'majitables', ['Areadustatuscounty'])

        # Adding model 'Areadustatusslum'
        db.create_table(u'AreaDUStatusSlum', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('slumid', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'SlumID')),
            ('slumname', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'SlumName')),
            ('dustatus', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'DUStatus')),
            ('nareas', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'Nareas', blank=True)),
            ('smpdus', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'SmpDUs')),
            ('pcntdus', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'pcntDUs')),
            ('dusinarea', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'DusInArea')),
            ('totdus', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'TotDUs')),
        ))
        db.send_create_signal(u'majitables', ['Areadustatusslum'])

        # Adding model 'Areadustatustown'
        db.create_table(u'AreaDUStatusTown', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('townid', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'TownID', blank=True)),
            ('townname', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'TownName')),
            ('dustatus', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'DUStatus')),
            ('nareas', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'Nareas', blank=True)),
            ('smpdus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'SmpDUs', blank=True)),
            ('pcntdus', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'pcntDUs', blank=True)),
            ('dusinarea', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'DusInArea', blank=True)),
            ('totdus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'TotDUs', blank=True)),
        ))
        db.send_create_signal(u'majitables', ['Areadustatustown'])

        # Adding model 'Areadustatuswsp'
        db.create_table(u'AreaDUStatusWSP', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('wspid', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'WspID')),
            ('wspname', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'WspName')),
            ('dustatus', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'DUStatus')),
            ('nareas', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'Nareas', blank=True)),
            ('smpdus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'SmpDUs', blank=True)),
            ('pcntdus', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'pcntDUs', blank=True)),
            ('dusinarea', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'DusInArea', blank=True)),
            ('totdus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'TotDUs', blank=True)),
        ))
        db.send_create_signal(u'majitables', ['Areadustatuswsp'])

        # Adding model 'Areadutypecounty'
        db.create_table(u'AreaDUTypeCounty', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('countyid', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'CountyID', blank=True)),
            ('countyname', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'CountyName')),
            ('dutype', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'DUType')),
            ('nareas', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'Nareas', blank=True)),
            ('smpdus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'SmpDUs', blank=True)),
            ('pcntdus', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'pcntDUs', blank=True)),
            ('dusinarea', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'DusInArea', blank=True)),
            ('totdus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'TotDUs', blank=True)),
        ))
        db.send_create_signal(u'majitables', ['Areadutypecounty'])

        # Adding model 'Areadutypeslum'
        db.create_table(u'AreaDUTypeSlum', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('slumid', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'SlumID', blank=True)),
            ('slumname', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'SlumName')),
            ('dutype', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'DUType')),
            ('nareas', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'Nareas', blank=True)),
            ('smpdus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'SmpDUs', blank=True)),
            ('pcntdus', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'pcntDUs', blank=True)),
            ('dusinarea', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'DusInArea', blank=True)),
            ('totdus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'TotDUs', blank=True)),
        ))
        db.send_create_signal(u'majitables', ['Areadutypeslum'])

        # Adding model 'Areadutypestructure'
        db.create_table(u'AreaDUTypeStructure', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('areaid', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'AreaID', blank=True)),
            ('dustatus', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'DUStatus')),
            ('ndus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'NDUs', blank=True)),
            ('pcntdus', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'PcntDUs', blank=True)),
            ('areasmpdus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'AreaSmpDUs', blank=True)),
        ))
        db.send_create_signal(u'majitables', ['Areadutypestructure'])

        # Adding model 'Areadutypetown'
        db.create_table(u'AreaDUTypeTown', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('townid', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'TownID', blank=True)),
            ('townname', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'TownName')),
            ('dutype', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'DUType')),
            ('nareas', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'Nareas', blank=True)),
            ('smpdus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'SmpDUs', blank=True)),
            ('pcntdus', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'pcntDUs', blank=True)),
            ('dusinarea', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'DusInArea', blank=True)),
            ('totdus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'TotDUs', blank=True)),
        ))
        db.send_create_signal(u'majitables', ['Areadutypetown'])

        # Adding model 'Areadutypewsp'
        db.create_table(u'AreaDUTypeWSP', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('wspid', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'WspID')),
            ('wspname', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'WspName')),
            ('dutype', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'DUType')),
            ('nareas', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'Nareas', blank=True)),
            ('smpdus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'SmpDUs', blank=True)),
            ('pcntdus', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'pcntDUs', blank=True)),
            ('dusinarea', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'DusInArea', blank=True)),
            ('totdus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'TotDUs', blank=True)),
        ))
        db.send_create_signal(u'majitables', ['Areadutypewsp'])

        # Adding model 'Areadutypehse'
        db.create_table(u'AreaDUTypehse', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('areaid', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'AreaID', blank=True)),
            ('dutype', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'DUType')),
            ('ndus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'NDUs', blank=True)),
            ('pcntdus', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'PcntDUs', blank=True)),
            ('areasmpdus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'AreaSmpDUs', blank=True)),
        ))
        db.send_create_signal(u'majitables', ['Areadutypehse'])

        # Adding model 'Areahabhsetypecounty'
        db.create_table(u'AreaHabHseTypeCounty', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('countyid', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'CountyID', blank=True)),
            ('countyname', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'CountyName')),
            ('hsngtype', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'HsngType')),
            ('nareas', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'Nareas', blank=True)),
            ('pcntareas', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'PcntAreas', blank=True)),
            ('totareas', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'TotAreas', blank=True)),
        ))
        db.send_create_signal(u'majitables', ['Areahabhsetypecounty'])

        # Adding model 'Areahabhsetypeslum'
        db.create_table(u'AreaHabHseTypeSlum', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('slumid', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'SlumID', blank=True)),
            ('slumname', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'SlumName')),
            ('hsngtype', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'HsngType')),
            ('nareas', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'Nareas', blank=True)),
            ('pcntareas', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'PcntAreas', blank=True)),
            ('totareas', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'TotAreas', blank=True)),
        ))
        db.send_create_signal(u'majitables', ['Areahabhsetypeslum'])

        # Adding model 'Areahabhsetypetown'
        db.create_table(u'AreaHabHseTypeTown', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('townid', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'TownID', blank=True)),
            ('townname', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'TownName')),
            ('hsngtype', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'HsngType')),
            ('nareas', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'Nareas', blank=True)),
            ('pcntareas', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'PcntAreas', blank=True)),
            ('totareas', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'TotAreas', blank=True)),
        ))
        db.send_create_signal(u'majitables', ['Areahabhsetypetown'])

        # Adding model 'Areahabhsetypewsp'
        db.create_table(u'AreaHabHseTypeWSP', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('wspid', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'WspID')),
            ('wspname', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'WspName')),
            ('hsngtype', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'HsngType')),
            ('nareas', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'Nareas', blank=True)),
            ('pcntareas', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'PcntAreas', blank=True)),
            ('totareas', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'TotAreas', blank=True)),
        ))
        db.send_create_signal(u'majitables', ['Areahabhsetypewsp'])

        # Adding model 'Areahabhsgsitcounty'
        db.create_table(u'AreaHabHsgSitCounty', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('countyid', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'CountyID', blank=True)),
            ('countyname', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'CountyName')),
            ('hsgsituation', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'HsgSituation')),
            ('nareas', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'Nareas', blank=True)),
            ('pcntareas', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'PcntAreas', blank=True)),
            ('totareas', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'TotAreas', blank=True)),
        ))
        db.send_create_signal(u'majitables', ['Areahabhsgsitcounty'])

        # Adding model 'Areahabhsgsitslum'
        db.create_table(u'AreaHabHsgSitSlum', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('slumid', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'SlumID')),
            ('slumname', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'SlumName')),
            ('hsgsituation', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'HsgSituation')),
            ('nareas', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'Nareas', blank=True)),
            ('pcntareas', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'PcntAreas')),
            ('totareas', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'TotAreas')),
        ))
        db.send_create_signal(u'majitables', ['Areahabhsgsitslum'])

        # Adding model 'Areahabhsgsittown'
        db.create_table(u'AreaHabHsgSitTown', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('townid', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'TownID', blank=True)),
            ('townname', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'TownName')),
            ('hsgsituation', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'HsgSituation')),
            ('nareas', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'Nareas', blank=True)),
            ('pcntareas', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'PcntAreas', blank=True)),
            ('totareas', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'TotAreas', blank=True)),
        ))
        db.send_create_signal(u'majitables', ['Areahabhsgsittown'])

        # Adding model 'Areahabhsgsitwsp'
        db.create_table(u'AreaHabHsgSitWSP', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('wspid', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'WspID')),
            ('wspname', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'WspName')),
            ('hsgsituation', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'HsgSituation')),
            ('nareas', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'Nareas', blank=True)),
            ('pcntareas', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'PcntAreas', blank=True)),
            ('totareas', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'TotAreas', blank=True)),
        ))
        db.send_create_signal(u'majitables', ['Areahabhsgsitwsp'])

        # Adding model 'Areahabroofcounty'
        db.create_table(u'AreaHabRoofCounty', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('countyid', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'CountyID', blank=True)),
            ('countyname', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'CountyName')),
            ('roof', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'Roof')),
            ('nareas', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'Nareas', blank=True)),
            ('pcntareas', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'PcntAreas', blank=True)),
            ('totareas', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'TotAreas', blank=True)),
        ))
        db.send_create_signal(u'majitables', ['Areahabroofcounty'])

        # Adding model 'Areahabroofslum'
        db.create_table(u'AreaHabRoofSlum', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('slumid', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'SlumID')),
            ('slumname', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'SlumName')),
            ('roof', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'Roof')),
            ('nareas', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'Nareas', blank=True)),
            ('pcntareas', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'PcntAreas')),
            ('totareas', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'TotAreas')),
        ))
        db.send_create_signal(u'majitables', ['Areahabroofslum'])

        # Adding model 'Areahabrooftown'
        db.create_table(u'AreaHabRoofTown', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('townid', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'TownID', blank=True)),
            ('townname', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'TownName')),
            ('roof', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'Roof')),
            ('nareas', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'Nareas', blank=True)),
            ('pcntareas', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'PcntAreas', blank=True)),
            ('totareas', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'TotAreas', blank=True)),
        ))
        db.send_create_signal(u'majitables', ['Areahabrooftown'])

        # Adding model 'Areahabroofwsp'
        db.create_table(u'AreaHabRoofWSP', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('wspid', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'WspID')),
            ('wspname', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'WspName')),
            ('roof', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'Roof')),
            ('nareas', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'Nareas', blank=True)),
            ('pcntareas', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'PcntAreas', blank=True)),
            ('totareas', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'TotAreas', blank=True)),
        ))
        db.send_create_signal(u'majitables', ['Areahabroofwsp'])

        # Adding model 'Areahabwallcounty'
        db.create_table(u'AreaHabWallCounty', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('countyid', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'CountyID', blank=True)),
            ('countyname', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'CountyName')),
            ('wall', self.gf('django.db.models.fields.CharField')(max_length=24, db_column=u'Wall')),
            ('nareas', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'Nareas', blank=True)),
            ('pcntareas', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'PcntAreas', blank=True)),
            ('totareas', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'TotAreas', blank=True)),
        ))
        db.send_create_signal(u'majitables', ['Areahabwallcounty'])

        # Adding model 'Areahabwallslum'
        db.create_table(u'AreaHabWallSlum', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('slumid', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'SlumID')),
            ('slumname', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'SlumName')),
            ('wall', self.gf('django.db.models.fields.CharField')(max_length=24, db_column=u'Wall')),
            ('nareas', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'Nareas', blank=True)),
            ('pcntareas', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'PcntAreas', blank=True)),
            ('totareas', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'TotAreas', blank=True)),
        ))
        db.send_create_signal(u'majitables', ['Areahabwallslum'])

        # Adding model 'Areahabwalltown'
        db.create_table(u'AreaHabWallTown', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('townid', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'TownID', blank=True)),
            ('townname', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'TownName')),
            ('wall', self.gf('django.db.models.fields.CharField')(max_length=24, db_column=u'Wall')),
            ('nareas', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'Nareas', blank=True)),
            ('pcntareas', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'PcntAreas', blank=True)),
            ('totareas', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'TotAreas', blank=True)),
        ))
        db.send_create_signal(u'majitables', ['Areahabwalltown'])

        # Adding model 'Areahabwallwsp'
        db.create_table(u'AreaHabWallWSP', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('wspid', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'WspID')),
            ('wspname', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'WspName')),
            ('wall', self.gf('django.db.models.fields.CharField')(max_length=24, db_column=u'Wall')),
            ('nareas', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'Nareas', blank=True)),
            ('pcntareas', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'PcntAreas', blank=True)),
            ('totareas', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'TotAreas', blank=True)),
        ))
        db.send_create_signal(u'majitables', ['Areahabwallwsp'])

        # Adding model 'Arealist'
        db.create_table(u'AreaList', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('sublocid', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'SublocID', blank=True)),
            ('areaid', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'AreaID', blank=True)),
            ('areaname', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'Areaname')),
            ('townid', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'TownID', blank=True)),
            ('slumid', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'Slumid')),
            ('wsp', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'WSP')),
            ('areatype', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'Areatype')),
            ('numdu', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'numDU', blank=True)),
            ('numplots', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'numPlots', blank=True)),
            ('numflats', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'numFlats', blank=True)),
            ('dusample', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'DUsample', blank=True)),
            ('risk', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'Risk')),
            ('remarks', self.gf('django.db.models.fields.TextField')(db_column=u'Remarks')),
            ('basedate', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'BaseDate', blank=True)),
            ('decode', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'DEcode')),
            ('dedate', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'DeDate', blank=True)),
        ))
        db.send_create_signal(u'majitables', ['Arealist'])

        # Adding model 'Arealist2'
        db.create_table(u'AreaList2', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('provid', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'ProvId', blank=True)),
            ('provname', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('distid', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'DistID', blank=True)),
            ('distname', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'DistName')),
            ('divid', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'DivID', blank=True)),
            ('divname', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'DivName')),
            ('locid', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'locID', blank=True)),
            ('locname', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('sublocid', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'sublocID', blank=True)),
            ('sublocname', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('areaid', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'AreaID', blank=True)),
            ('areaname', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'Areaname')),
            ('townid', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'townID', blank=True)),
            ('townname', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('wspid', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'WSPID')),
            ('wspname', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'WSPName')),
            ('wsbid', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'WSBID', blank=True)),
            ('wsbname', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'WSBName')),
            ('countyid', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'Countyid', blank=True)),
            ('countyname', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'CountyName')),
            ('numdu', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'numDU', blank=True)),
            ('slumid', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'Slumid', blank=True)),
            ('slumname', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'SlumName', blank=True)),
            ('totscore', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'TotScore', blank=True)),
        ))
        db.send_create_signal(u'majitables', ['Arealist2'])

        # Adding model 'Areanospckskcounty'
        db.create_table(u'AreaNoSpcKskCounty', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('countyid', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'CountyID', blank=True)),
            ('countyname', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'CountyName')),
            ('spckiosk', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'SpcKiosk')),
            ('nareas', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'Nareas', blank=True)),
            ('pcntareas', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'PcntAreas', blank=True)),
            ('totareas', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'TotAreas', blank=True)),
        ))
        db.send_create_signal(u'majitables', ['Areanospckskcounty'])

        # Adding model 'Areanospckskslum'
        db.create_table(u'AreaNoSpcKskSlum', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('slumid', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'SlumID')),
            ('slumname', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'SlumName')),
            ('spckiosk', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'SpcKiosk')),
            ('nareas', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'Nareas', blank=True)),
            ('pcntareas', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'PcntAreas')),
            ('totareas', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'TotAreas')),
        ))
        db.send_create_signal(u'majitables', ['Areanospckskslum'])

        # Adding model 'Areanospcksktown'
        db.create_table(u'AreaNoSpcKskTown', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('townid', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'TownID', blank=True)),
            ('townname', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'TownName')),
            ('spckiosk', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'SpcKiosk')),
            ('nareas', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'Nareas', blank=True)),
            ('pcntareas', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'PcntAreas', blank=True)),
            ('totareas', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'TotAreas', blank=True)),
        ))
        db.send_create_signal(u'majitables', ['Areanospcksktown'])

        # Adding model 'Areanospckskwsp'
        db.create_table(u'AreaNoSpcKskWSP', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('wspid', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'WspID')),
            ('wspname', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'WspName')),
            ('spckiosk', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'SpcKiosk')),
            ('nareas', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'Nareas', blank=True)),
            ('pcntareas', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'PcntAreas', blank=True)),
            ('totareas', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'TotAreas', blank=True)),
        ))
        db.send_create_signal(u'majitables', ['Areanospckskwsp'])

        # Adding model 'Areanospcpubsancounty'
        db.create_table(u'AreaNoSpcPubSanCounty', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('countyid', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'CountyID', blank=True)),
            ('countyname', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'CountyName')),
            ('spcpubsan', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'SpcPubSan')),
            ('nareas', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'Nareas', blank=True)),
            ('pcntareas', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'PcntAreas', blank=True)),
            ('totareas', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'TotAreas', blank=True)),
        ))
        db.send_create_signal(u'majitables', ['Areanospcpubsancounty'])

        # Adding model 'Areanospcpubsanslum'
        db.create_table(u'AreaNoSpcPubSanSlum', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('slumid', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'SlumID')),
            ('slumname', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'SlumName')),
            ('spcpubsan', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'SpcPubSan')),
            ('nareas', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'Nareas', blank=True)),
            ('pcntareas', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'PcntAreas')),
            ('totareas', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'TotAreas')),
        ))
        db.send_create_signal(u'majitables', ['Areanospcpubsanslum'])

        # Adding model 'Areanospcpubsantown'
        db.create_table(u'AreaNoSpcPubSanTown', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('townid', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'TownID', blank=True)),
            ('townname', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'TownName')),
            ('spcpubsan', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'SpcPubSan')),
            ('nareas', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'Nareas', blank=True)),
            ('pcntareas', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'PcntAreas', blank=True)),
            ('totareas', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'TotAreas', blank=True)),
        ))
        db.send_create_signal(u'majitables', ['Areanospcpubsantown'])

        # Adding model 'Areanospcpubsanwsp'
        db.create_table(u'AreaNoSpcPubSanWSP', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('wspid', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'WspID')),
            ('wspname', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'WspName')),
            ('spcpubsan', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'SpcPubSan')),
            ('nareas', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'Nareas', blank=True)),
            ('pcntareas', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'PcntAreas', blank=True)),
            ('totareas', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'TotAreas', blank=True)),
        ))
        db.send_create_signal(u'majitables', ['Areanospcpubsanwsp'])

        # Adding model 'Areaownducounty'
        db.create_table(u'AreaOwnDUCounty', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('countyid', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'CountyID', blank=True)),
            ('countyname', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'CountyName')),
            ('owndu', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'OwnDU')),
            ('dusinsmp', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'DUsInSmp', blank=True)),
            ('smpdus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'SmpDUs', blank=True)),
            ('pcntdus', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'pcntDUs', blank=True)),
            ('dusinarea', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'DusInArea', blank=True)),
            ('totdus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'TotDUs', blank=True)),
            ('totalppleinarea', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'TotalPpleinArea', blank=True)),
            ('pcntpop', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'PcntPop', blank=True)),
            ('pop', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'Pop', blank=True)),
        ))
        db.send_create_signal(u'majitables', ['Areaownducounty'])

        # Adding model 'Areaownduslum'
        db.create_table(u'AreaOwnDUSlum', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('slumid', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'SlumID', blank=True)),
            ('slumname', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'SlumName')),
            ('owndu', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'OwnDU')),
            ('dusinsmp', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'DUsInSmp', blank=True)),
            ('smpdus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'SmpDUs', blank=True)),
            ('pcntdus', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'pcntDUs', blank=True)),
            ('dusinarea', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'DusInArea', blank=True)),
            ('totdus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'TotDUs', blank=True)),
            ('totalppleinarea', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'TotalPpleinArea', blank=True)),
            ('pcntpop', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'PcntPop', blank=True)),
            ('pop', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'Pop', blank=True)),
        ))
        db.send_create_signal(u'majitables', ['Areaownduslum'])

        # Adding model 'Areaowndutown'
        db.create_table(u'AreaOwnDUTown', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('townid', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'TownID', blank=True)),
            ('townname', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'TownName')),
            ('owndu', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'OwnDU')),
            ('dusinsmp', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'DUsInSmp', blank=True)),
            ('smpdus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'SmpDUs', blank=True)),
            ('pcntdus', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'pcntDUs', blank=True)),
            ('dusinarea', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'DusInArea', blank=True)),
            ('totdus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'TotDUs', blank=True)),
            ('totalppleinarea', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'TotalPpleinArea', blank=True)),
            ('pcntpop', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'PcntPop', blank=True)),
        ))
        db.send_create_signal(u'majitables', ['Areaowndutown'])

        # Adding model 'Areaownduwsp'
        db.create_table(u'AreaOwnDUWSP', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('wspid', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'WSPID')),
            ('wspname', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'WSPName')),
            ('owndu', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'OwnDU')),
            ('dusinsmp', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'DUsInSmp', blank=True)),
            ('smpdus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'SmpDUs', blank=True)),
            ('pcntdus', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'pcntDUs', blank=True)),
            ('dusinarea', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'DusInArea', blank=True)),
            ('totdus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'TotDUs', blank=True)),
            ('totalppleinarea', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'TotalPpleinArea', blank=True)),
            ('pcntpop', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'PcntPop', blank=True)),
            ('pop', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'Pop', blank=True)),
        ))
        db.send_create_signal(u'majitables', ['Areaownduwsp'])

        # Adding model 'Areaphychar'
        db.create_table(u'AreaPhyChar', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('areaname', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'Areaname')),
            ('areaid', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'AreaID', blank=True)),
            ('townname', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('adist', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'ADist', blank=True)),
            ('areatype', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'AreaType')),
            ('settlement', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'Settlement')),
            ('legalised', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'Legalised')),
            ('yrlegalised', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'YrLegalised')),
            ('watertabledry', self.gf('django.db.models.fields.CharField')(max_length=29, db_column=u'WaterTableDry')),
            ('watertablerainy', self.gf('django.db.models.fields.CharField')(max_length=29, db_column=u'WaterTableRainy')),
            ('flooding', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'Flooding')),
            ('soil', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'Soil')),
            ('soilselfsupporting', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'SoilSelfSupporting')),
            ('arealocation', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'AreaLocation')),
            ('areatopology', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'AreaTopology', blank=True)),
        ))
        db.send_create_signal(u'majitables', ['Areaphychar'])

        # Adding model 'Areapop'
        db.create_table(u'AreaPop', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('area', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'Area', blank=True)),
            ('areaname', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'Areaname')),
            ('basedate', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'BaseDate', blank=True)),
            ('areasmppop', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'AreaSmpPop', blank=True)),
            ('areasmpdus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'AreaSmpDUs', blank=True)),
            ('tothhs', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'TotHHs', blank=True)),
            ('avgdusz', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'AvgDUSz', blank=True)),
            ('maxdusz', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'MaxDUSz', blank=True)),
            ('mindusz', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'MinDUSz', blank=True)),
            ('avghhsz', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'AvgHHSz', blank=True)),
            ('avghhsdu', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'AvgHHsDU', blank=True)),
            ('smpfhhh', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'SmpFHHH', blank=True)),
            ('pcntfhhh', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'PcntFHHH', blank=True)),
            ('avgfhhh', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'AvgFHHH', blank=True)),
            ('numdu', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'NumDU', blank=True)),
            ('popunit', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'PopUnit')),
            ('areapop', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'AreaPop', blank=True)),
            ('sublocpop', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'SubLocPop', blank=True)),
        ))
        db.send_create_signal(u'majitables', ['Areapop'])

        # Adding model 'Areapopdensity'
        db.create_table(u'AreaPopDensity', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('area', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'Area', blank=True)),
            ('areaname', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'Areaname')),
            ('basedate', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'BaseDate', blank=True)),
            ('areapop', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'AreaPop', blank=True)),
            ('sqkm', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'SqKm', blank=True)),
            ('popdensity', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'PopDensity', blank=True)),
            ('popden', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'PopDen')),
        ))
        db.send_create_signal(u'majitables', ['Areapopdensity'])

        # Adding model 'Areaprofiles'
        db.create_table(u'AreaProfiles', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('areaname', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'Areaname')),
            ('areaid', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'AreaID', blank=True)),
            ('townname', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('alocation', self.gf('django.db.models.fields.TextField')(db_column=u'ALocation')),
            ('alayout', self.gf('django.db.models.fields.TextField')(db_column=u'ALayout')),
            ('aurbandev', self.gf('django.db.models.fields.TextField')(db_column=u'AUrbanDev')),
            ('awater', self.gf('django.db.models.fields.TextField')(db_column=u'AWater')),
            ('asanitation', self.gf('django.db.models.fields.TextField')(db_column=u'Asanitation')),
            ('asolidwaste', self.gf('django.db.models.fields.TextField')(db_column=u'Asolidwaste')),
            ('apbhealthrisks', self.gf('django.db.models.fields.TextField')(db_column=u'ApbHealthRisks')),
            ('amainproblems', self.gf('django.db.models.fields.TextField')(db_column=u'AmainProblems')),
        ))
        db.send_create_signal(u'majitables', ['Areaprofiles'])

        # Adding model 'Areasubjfldcounty'
        db.create_table(u'AreaSubjFldCounty', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('countyid', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'CountyID', blank=True)),
            ('countyname', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'CountyName')),
            ('flooding', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'Flooding')),
            ('nareas', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'Nareas', blank=True)),
            ('numareas', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'NumAreas', blank=True)),
            ('pcntareas', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'PcntAreas', blank=True)),
        ))
        db.send_create_signal(u'majitables', ['Areasubjfldcounty'])

        # Adding model 'Areasubjfldslum'
        db.create_table(u'AreaSubjFldSlum', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('slumid', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'SlumID', blank=True)),
            ('slumname', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'SlumName')),
            ('flooding', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'Flooding')),
            ('nareas', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'Nareas', blank=True)),
            ('numareas', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'NumAreas', blank=True)),
            ('pcntareas', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'PcntAreas', blank=True)),
        ))
        db.send_create_signal(u'majitables', ['Areasubjfldslum'])

        # Adding model 'Areasubjfldtown'
        db.create_table(u'AreaSubjFldTown', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('townid', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'TownID', blank=True)),
            ('townname', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'TownName')),
            ('flooding', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'Flooding')),
            ('nareas', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'Nareas', blank=True)),
            ('numareas', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'NumAreas', blank=True)),
            ('pcntareas', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'PcntAreas', blank=True)),
        ))
        db.send_create_signal(u'majitables', ['Areasubjfldtown'])

        # Adding model 'Areasubjfldwsp'
        db.create_table(u'AreaSubjFldWSP', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('wspid', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'WspID')),
            ('wspname', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'WspName')),
            ('flooding', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'Flooding')),
            ('nareas', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'Nareas', blank=True)),
            ('numareas', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'NumAreas', blank=True)),
            ('pcntareas', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'PcntAreas', blank=True)),
        ))
        db.send_create_signal(u'majitables', ['Areasubjfldwsp'])

        # Adding model 'Areasummarysheet'
        db.create_table(u'AreaSummarySheet', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('areaid', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'AreaID', blank=True)),
            ('areaname', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'Areaname')),
            ('sublocname', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('wspname', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'WSPName')),
            ('areatype', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'AreaType')),
            ('areapop', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'AreaPop', blank=True)),
            ('sqkm', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'SqKm', blank=True)),
            ('popdensity', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'PopDensity', blank=True)),
            ('arealinkedwater', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'AreaLinkedWater')),
            ('communityschm', self.gf('django.db.models.fields.TextField')(db_column=u'CommunitySchm')),
            ('wsupplyproj', self.gf('django.db.models.fields.TextField')(db_column=u'WsupplyProj')),
            ('pcntppleusingimpsrcwstf', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'PcntPpleUsingImpSrcWSTF', blank=True)),
            ('nadeqsupplied', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'NAdeqSupplied', blank=True)),
            ('pcntpplereseller', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'PcntPPleReseller', blank=True)),
            ('pcntppleothcon', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'PcntPpleOthCon', blank=True)),
            ('arealinkedsew', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'AreaLinkedSew')),
            ('pcntppleimpsan', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'PcntPpleImpSan', blank=True)),
        ))
        db.send_create_signal(u'majitables', ['Areasummarysheet'])

        # Adding model 'Areassettlocrdrlcounty'
        db.create_table(u'AreasSettLocRdRlCounty', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('countyid', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'Countyid', blank=True)),
            ('countyname', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'CountyName')),
            ('arealocation', self.gf('django.db.models.fields.CharField')(max_length=35, db_column=u'Arealocation')),
            ('nareas', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'Nareas', blank=True)),
            ('pcntareas', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'PcntAreas', blank=True)),
            ('numareas', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'NumAreas', blank=True)),
        ))
        db.send_create_signal(u'majitables', ['Areassettlocrdrlcounty'])

        # Adding model 'Areassettlocrdrlslum'
        db.create_table(u'AreasSettLocRdRlSlum', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('slumid', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'Slumid', blank=True)),
            ('slumname', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'SlumName')),
            ('arealocation', self.gf('django.db.models.fields.CharField')(max_length=35, db_column=u'Arealocation')),
            ('nareas', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'Nareas', blank=True)),
            ('pcntareas', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'PcntAreas', blank=True)),
            ('numareas', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'NumAreas', blank=True)),
        ))
        db.send_create_signal(u'majitables', ['Areassettlocrdrlslum'])

        # Adding model 'Areassettlocrdrltown'
        db.create_table(u'AreasSettLocRdRlTown', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('townid', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'Townid', blank=True)),
            ('townname', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'TownName')),
            ('arealocation', self.gf('django.db.models.fields.CharField')(max_length=35, db_column=u'Arealocation')),
            ('nareas', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'Nareas', blank=True)),
            ('pcntareas', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'PcntAreas', blank=True)),
            ('numareas', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'NumAreas', blank=True)),
        ))
        db.send_create_signal(u'majitables', ['Areassettlocrdrltown'])

        # Adding model 'Areassettlocrdrlwsp'
        db.create_table(u'AreasSettLocRdRlWSP', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('wspid', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'WSPid')),
            ('wspname', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'WSPName')),
            ('arealocation', self.gf('django.db.models.fields.CharField')(max_length=35, db_column=u'Arealocation')),
            ('nareas', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'Nareas', blank=True)),
            ('pcntareas', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'PcntAreas', blank=True)),
            ('numareas', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'NumAreas', blank=True)),
        ))
        db.send_create_signal(u'majitables', ['Areassettlocrdrlwsp'])

        # Adding model 'Demogtrends'
        db.create_table(u'DemogTrends', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('areaid', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'AreaID', blank=True)),
            ('popdensity', self.gf('django.db.models.fields.TextField')(db_column=u'PopDensity')),
            ('demogtrend', self.gf('django.db.models.fields.TextField')(db_column=u'Demogtrend')),
            ('factors', self.gf('django.db.models.fields.TextField')(db_column=u'Factors')),
            ('popgrwth', self.gf('django.db.models.fields.TextField')(db_column=u'PopGrwth')),
            ('demogdev', self.gf('django.db.models.fields.TextField')(db_column=u'DemogDev')),
            ('daypop', self.gf('django.db.models.fields.TextField')(db_column=u'DayPop')),
        ))
        db.send_create_signal(u'majitables', ['Demogtrends'])

        # Adding model 'Devplans'
        db.create_table(u'DevPlans', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('areaid', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'AreaID', blank=True)),
            ('devplan', self.gf('django.db.models.fields.TextField')(db_column=u'DevPlan')),
            ('laplan', self.gf('django.db.models.fields.TextField')(db_column=u'LAPlan')),
            ('devactivities', self.gf('django.db.models.fields.TextField')(db_column=u'DevActivities')),
        ))
        db.send_create_signal(u'majitables', ['Devplans'])

        # Adding model 'Femhhhscounty'
        db.create_table(u'FemHHHsCounty', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('countyid', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'CountyID', blank=True)),
            ('countyname', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'CountyName')),
            ('areasmppop', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'AreaSmpPop', blank=True)),
            ('areasmpdus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'AreaSmpDUs', blank=True)),
            ('tothhs', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'TotHHs', blank=True)),
            ('avgdusz', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'AvgDUSz', blank=True)),
            ('maxdusz', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'MaxDUSz', blank=True)),
            ('mindusz', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'MinDUSz', blank=True)),
            ('avghhsz', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'AvgHHSz', blank=True)),
            ('avghhsdu', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'AvgHHsDU', blank=True)),
            ('smpfhhh', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'SmpFHHH', blank=True)),
            ('pcntfhhh', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'PcntFHHH', blank=True)),
            ('avgfhhh', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'AvgFHHH', blank=True)),
        ))
        db.send_create_signal(u'majitables', ['Femhhhscounty'])

        # Adding model 'Femhhhsslum'
        db.create_table(u'FemHHHsSlum', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('slumid', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'SlumID')),
            ('slumname', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'SlumName')),
            ('areasmppop', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'AreaSmpPop', blank=True)),
            ('areasmpdus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'AreaSmpDUs', blank=True)),
            ('tothhs', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'TotHHs', blank=True)),
            ('avgdusz', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'AvgDUSz', blank=True)),
            ('maxdusz', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'MaxDUSz', blank=True)),
            ('mindusz', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'MinDUSz', blank=True)),
            ('avghhsz', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'AvgHHSz', blank=True)),
            ('avghhsdu', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'AvgHHsDU', blank=True)),
            ('smpfhhh', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'SmpFHHH', blank=True)),
            ('pcntfhhh', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'PcntFHHH', blank=True)),
            ('avgfhhh', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'AvgFHHH', blank=True)),
        ))
        db.send_create_signal(u'majitables', ['Femhhhsslum'])

        # Adding model 'Femhhhstown'
        db.create_table(u'FemHHHsTown', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('townid', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'TownID', blank=True)),
            ('townname', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'TownName')),
            ('areasmppop', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'AreaSmpPop', blank=True)),
            ('areasmpdus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'AreaSmpDUs', blank=True)),
            ('tothhs', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'TotHHs', blank=True)),
            ('avgdusz', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'AvgDUSz', blank=True)),
            ('maxdusz', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'MaxDUSz', blank=True)),
            ('mindusz', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'MinDUSz', blank=True)),
            ('avghhsz', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'AvgHHSz', blank=True)),
            ('avghhsdu', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'AvgHHsDU', blank=True)),
            ('smpfhhh', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'SmpFHHH', blank=True)),
            ('pcntfhhh', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'PcntFHHH', blank=True)),
            ('avgfhhh', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'AvgFHHH', blank=True)),
        ))
        db.send_create_signal(u'majitables', ['Femhhhstown'])

        # Adding model 'Habitationpatterns'
        db.create_table(u'HabitationPatterns', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('areaid', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'AreaID', blank=True)),
            ('areaname', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'Areaname')),
            ('hsetype', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'HseType')),
            ('hsgsituation', self.gf('django.db.models.fields.TextField')(db_column=u'HsgSituation')),
            ('hsngchar', self.gf('django.db.models.fields.TextField')(db_column=u'HsngChar')),
            ('hseroof', self.gf('django.db.models.fields.TextField')(db_column=u'HseRoof')),
            ('hsewall', self.gf('django.db.models.fields.TextField')(db_column=u'HseWall')),
        ))
        db.send_create_signal(u'majitables', ['Habitationpatterns'])

        # Adding model 'Landownuse'
        db.create_table(u'LandOwnUse', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('areaid', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'AreaID', blank=True)),
            ('landownership', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'LandOwnership')),
            ('rdrsrv', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'RdRsrv')),
            ('pubspace', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'PubSpace')),
            ('spcwaterext', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'SpcWaterExt')),
            ('spckiosk', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'SpcKiosk')),
            ('spcpubsan', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'SpcPubSan')),
            ('spcprvsan', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'SpcPrvSan')),
            ('landuse', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'Landuse')),
        ))
        db.send_create_signal(u'majitables', ['Landownuse'])

        # Adding model 'Majidatainfocounty'
        db.create_table(u'MajidataInfoCounty', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('countyid', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'countyID', blank=True)),
            ('countyname', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('nareas', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'NAreas', blank=True)),
            ('ndus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'NDUs', blank=True)),
            ('smpdus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'SmpDUs', blank=True)),
            ('pop', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'Pop', blank=True)),
            ('pcntdusinterv', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'PcntDUsInterv', blank=True)),
            ('smppop', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'SmpPop', blank=True)),
            ('pcntpopinterviewed', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'PcntPopInterviewed', blank=True)),
        ))
        db.send_create_signal(u'majitables', ['Majidatainfocounty'])

        # Adding model 'Majidatainfoslum'
        db.create_table(u'MajidataInfoSlum', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('slumid', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'slumID')),
            ('slumname', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('nareas', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'NAreas', blank=True)),
            ('ndus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'NDUs', blank=True)),
            ('smpdus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'SmpDUs', blank=True)),
            ('pop', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'Pop', blank=True)),
            ('pcntdusinterv', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'PcntDUsInterv', blank=True)),
            ('smppop', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'SmpPop', blank=True)),
            ('pcntpopinterviewed', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'PcntPopInterviewed', blank=True)),
        ))
        db.send_create_signal(u'majitables', ['Majidatainfoslum'])

        # Adding model 'Majidatainfotwn'
        db.create_table(u'MajidataInfoTwn', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('townid', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'townID', blank=True)),
            ('townname', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('nareas', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'NAreas', blank=True)),
            ('ndus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'NDUs', blank=True)),
            ('smpdus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'SmpDUs', blank=True)),
            ('pop', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'Pop', blank=True)),
            ('pcntdusinterv', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'PcntDUsInterv', blank=True)),
            ('smppop', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'SmpPop', blank=True)),
            ('pcntpopinterviewed', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'PcntPopInterviewed', blank=True)),
        ))
        db.send_create_signal(u'majitables', ['Majidatainfotwn'])

        # Adding model 'Majidatainfowsp'
        db.create_table(u'MajidataInfoWSP', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('wspid', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'wspID')),
            ('wspname', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('nareas', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'NAreas', blank=True)),
            ('ndus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'NDUs', blank=True)),
            ('smpdus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'SmpDUs', blank=True)),
            ('pop', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'Pop', blank=True)),
            ('pcntdusinterv', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'PcntDUsInterv', blank=True)),
            ('smppop', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'SmpPop', blank=True)),
            ('pcntpopinterviewed', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'PcntPopInterviewed', blank=True)),
        ))
        db.send_create_signal(u'majitables', ['Majidatainfowsp'])

        # Adding model 'Pavghhduszcounty'
        db.create_table(u'PAvgHHDUSzCounty', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('countyid', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'CountyID', blank=True)),
            ('countyname', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'CountyName')),
            ('areasmppop', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'AreaSmpPop', blank=True)),
            ('areasmpdus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'AreaSmpDUs', blank=True)),
            ('avgdusz', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'AvgDUSz', blank=True)),
            ('maxdusz', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'MaxDUSz', blank=True)),
            ('mindusz', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'MinDUSz', blank=True)),
            ('tothhs', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'TotHHs', blank=True)),
            ('avghhsz', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'AvgHHSz', blank=True)),
            ('avghhsdu', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'AvgHHsDU', blank=True)),
            ('avgfhhh', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'AvgFHHH', blank=True)),
        ))
        db.send_create_signal(u'majitables', ['Pavghhduszcounty'])

        # Adding model 'Pavghhduszslum'
        db.create_table(u'PAvgHHDUSzSlum', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('slumid', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'SlumID')),
            ('slumname', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'SlumName')),
            ('areasmppop', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'AreaSmpPop', blank=True)),
            ('areasmpdus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'AreaSmpDUs', blank=True)),
            ('avgdusz', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'AvgDUSz', blank=True)),
            ('maxdusz', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'MaxDUSz', blank=True)),
            ('mindusz', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'MinDUSz', blank=True)),
            ('tothhs', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'TotHHs', blank=True)),
            ('avghhsz', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'AvgHHSz', blank=True)),
            ('avghhsdu', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'AvgHHsDU', blank=True)),
        ))
        db.send_create_signal(u'majitables', ['Pavghhduszslum'])

        # Adding model 'Pavghhdusztown'
        db.create_table(u'PAvgHHDUSzTown', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('townid', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'TownID', blank=True)),
            ('townname', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'TownName')),
            ('areasmppop', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'AreaSmpPop', blank=True)),
            ('areasmpdus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'AreaSmpDUs', blank=True)),
            ('avgdusz', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'AvgDUSz', blank=True)),
            ('maxdusz', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'MaxDUSz', blank=True)),
            ('mindusz', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'MinDUSz', blank=True)),
            ('tothhs', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'TotHHs', blank=True)),
            ('avghhsz', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'AvgHHSz', blank=True)),
            ('avghhsdu', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'AvgHHsDU', blank=True)),
            ('avgfhhh', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'AvgFHHH', blank=True)),
        ))
        db.send_create_signal(u'majitables', ['Pavghhdusztown'])

        # Adding model 'Phlthwasterds'
        db.create_table(u'PHlthWasteRds', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('areaid', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'AreaID', blank=True)),
            ('areaname', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'Areaname')),
            ('phsit', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'PHSit')),
            ('mnphproblem', self.gf('django.db.models.fields.TextField')(db_column=u'MnPHProblem')),
            ('swsit', self.gf('django.db.models.fields.TextField')(db_column=u'SWSit')),
            ('mnswdisp', self.gf('django.db.models.fields.TextField')(db_column=u'MnSWDisp')),
            ('roadtypes', self.gf('django.db.models.fields.TextField')(db_column=u'RoadTypes')),
            ('rdtechstatus', self.gf('django.db.models.fields.TextField')(db_column=u'RdTechStatus')),
            ('draintypes', self.gf('django.db.models.fields.TextField')(db_column=u'DrainTypes')),
            ('drnstatus', self.gf('django.db.models.fields.TextField')(db_column=u'DrnStatus')),
        ))
        db.send_create_signal(u'majitables', ['Phlthwasterds'])

        # Adding model 'Pownduwsrckskcounty'
        db.create_table(u'POwnDUWSrcKskCounty', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('countyid', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'CountyID', blank=True)),
            ('countyname', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'CountyName')),
            ('owndu', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'OwnDU')),
            ('dusinsmp', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'DUsInSmp', blank=True)),
            ('smpdus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'SmpDUs', blank=True)),
            ('pcntdus', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'pcntDUs', blank=True)),
            ('dusinarea', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'DusInArea', blank=True)),
            ('totdus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'TotDUs', blank=True)),
            ('totalppleinarea', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'TotalPpleinArea', blank=True)),
            ('pcntpop', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'PcntPop', blank=True)),
            ('pop', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'Pop', blank=True)),
        ))
        db.send_create_signal(u'majitables', ['Pownduwsrckskcounty'])

        # Adding model 'Pownduwsrckskslum'
        db.create_table(u'POwnDUWSrcKskSlum', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('slumid', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'SlumID', blank=True)),
            ('slumname', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'SlumName')),
            ('owndu', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'OwnDU')),
            ('dusinsmp', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'DUsInSmp', blank=True)),
            ('smpdus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'SmpDUs', blank=True)),
            ('pcntdus', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'pcntDUs', blank=True)),
            ('dusinarea', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'DusInArea', blank=True)),
            ('totdus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'TotDUs', blank=True)),
            ('totalppleinarea', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'TotalPpleinArea', blank=True)),
            ('pcntpop', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'PcntPop', blank=True)),
            ('pop', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'Pop', blank=True)),
        ))
        db.send_create_signal(u'majitables', ['Pownduwsrckskslum'])

        # Adding model 'Pownduwsrcksktown'
        db.create_table(u'POwnDUWSrcKskTown', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('townid', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'TownID', blank=True)),
            ('townname', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'TownName')),
            ('owndu', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'OwnDU')),
            ('dusinsmp', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'DUsInSmp', blank=True)),
            ('smpdus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'SmpDUs', blank=True)),
            ('pcntdus', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'pcntDUs', blank=True)),
            ('dusinarea', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'DusInArea', blank=True)),
            ('totdus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'TotDUs', blank=True)),
            ('totalppleinarea', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'TotalPpleinArea', blank=True)),
            ('pcntpop', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'PcntPop', blank=True)),
            ('pop', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'Pop', blank=True)),
        ))
        db.send_create_signal(u'majitables', ['Pownduwsrcksktown'])

        # Adding model 'Pownduwsrckskwsp'
        db.create_table(u'POwnDUWSrcKskWSP', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('wspid', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'WspID')),
            ('wspname', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'WspName')),
            ('owndu', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'OwnDU')),
            ('dusinsmp', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'DUsInSmp', blank=True)),
            ('smpdus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'SmpDUs', blank=True)),
            ('pcntdus', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'pcntDUs', blank=True)),
            ('dusinarea', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'DusInArea', blank=True)),
            ('totdus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'TotDUs', blank=True)),
            ('totalppleinarea', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'TotalPpleinArea', blank=True)),
            ('pcntpop', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'PcntPop', blank=True)),
            ('pop', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'Pop', blank=True)),
        ))
        db.send_create_signal(u'majitables', ['Pownduwsrckskwsp'])

        # Adding model 'Pownduwsrcpipedcounty'
        db.create_table(u'POwnDUWSrcPipedCounty', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('countyid', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'CountyID', blank=True)),
            ('countyname', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'CountyName')),
            ('owndu', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'OwnDU')),
            ('dusinsmp', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'DUsInSmp', blank=True)),
            ('smpdus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'SmpDUs', blank=True)),
            ('pcntdus', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'pcntDUs', blank=True)),
            ('dusinarea', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'DusInArea', blank=True)),
            ('totdus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'TotDUs', blank=True)),
            ('totalppleinarea', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'TotalPpleinArea', blank=True)),
            ('pcntpop', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'PcntPop', blank=True)),
            ('pop', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'Pop', blank=True)),
        ))
        db.send_create_signal(u'majitables', ['Pownduwsrcpipedcounty'])

        # Adding model 'Pownduwsrcpipedslum'
        db.create_table(u'POwnDUWSrcPipedSlum', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('slumid', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'SlumID', blank=True)),
            ('slumname', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'SlumName')),
            ('owndu', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'OwnDU')),
            ('dusinsmp', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'DUsInSmp', blank=True)),
            ('smpdus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'SmpDUs', blank=True)),
            ('pcntdus', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'pcntDUs', blank=True)),
            ('dusinarea', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'DusInArea', blank=True)),
            ('totdus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'TotDUs', blank=True)),
            ('totalppleinarea', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'TotalPpleinArea', blank=True)),
            ('pcntpop', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'PcntPop', blank=True)),
            ('pop', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'Pop', blank=True)),
        ))
        db.send_create_signal(u'majitables', ['Pownduwsrcpipedslum'])

        # Adding model 'Pownduwsrcpipedtown'
        db.create_table(u'POwnDUWSrcPipedTown', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('townid', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'TownID', blank=True)),
            ('townname', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'TownName')),
            ('owndu', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'OwnDU')),
            ('dusinsmp', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'DUsInSmp', blank=True)),
            ('smpdus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'SmpDUs', blank=True)),
            ('pcntdus', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'pcntDUs', blank=True)),
            ('dusinarea', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'DusInArea', blank=True)),
            ('totdus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'TotDUs', blank=True)),
            ('totalppleinarea', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'TotalPpleinArea', blank=True)),
            ('pcntpop', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'PcntPop', blank=True)),
            ('pop', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'Pop', blank=True)),
        ))
        db.send_create_signal(u'majitables', ['Pownduwsrcpipedtown'])

        # Adding model 'Pownduwsrcpipedwsp'
        db.create_table(u'POwnDUWSrcPipedWSP', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('wspid', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'wspID')),
            ('wspname', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'wspName')),
            ('owndu', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'OwnDU')),
            ('dusinsmp', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'DUsInSmp', blank=True)),
            ('smpdus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'SmpDUs', blank=True)),
            ('pcntdus', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'pcntDUs', blank=True)),
            ('dusinarea', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'DusInArea', blank=True)),
            ('totdus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'TotDUs', blank=True)),
            ('totalppleinarea', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'TotalPpleinArea', blank=True)),
            ('pcntpop', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'PcntPop', blank=True)),
            ('pop', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'Pop', blank=True)),
        ))
        db.send_create_signal(u'majitables', ['Pownduwsrcpipedwsp'])

        # Adding model 'Preligioncounty'
        db.create_table(u'PReligionCounty', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('countyid', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'CountyID', blank=True)),
            ('countyname', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'CountyName')),
            ('religion', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'Religion')),
            ('ndus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'NDus', blank=True)),
            ('pcntdus', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'PcntDUs', blank=True)),
        ))
        db.send_create_signal(u'majitables', ['Preligioncounty'])

        # Adding model 'Preligionslum'
        db.create_table(u'PReligionSlum', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('slumid', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'SlumID', blank=True)),
            ('slumname', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'SlumName')),
            ('religion', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'Religion')),
            ('ndus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'NDus', blank=True)),
            ('pcntdus', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'PcntDUs', blank=True)),
        ))
        db.send_create_signal(u'majitables', ['Preligionslum'])

        # Adding model 'Preligiontown'
        db.create_table(u'PReligionTown', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('townid', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'TownID', blank=True)),
            ('townname', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'TownName')),
            ('religion', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'Religion')),
            ('ndus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'NDus', blank=True)),
            ('pcntdus', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'PcntDUs', blank=True)),
        ))
        db.send_create_signal(u'majitables', ['Preligiontown'])

        # Adding model 'Preligionwsp'
        db.create_table(u'PReligionWSP', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('wspid', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'wspID')),
            ('wspname', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'wspName')),
            ('religion', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'Religion')),
            ('ndus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'NDus', blank=True)),
            ('pcntdus', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'PcntDUs', blank=True)),
        ))
        db.send_create_signal(u'majitables', ['Preligionwsp'])

        # Adding model 'Popareabysettlementcounty'
        db.create_table(u'PopAreaBySettlementCounty', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('countyid', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'Countyid', blank=True)),
            ('countyname', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'CountyName')),
            ('settlement', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'Settlement')),
            ('nareas', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'NAreas', blank=True)),
            ('totareas', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'TotAreas', blank=True)),
            ('pcntareas', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'PcntAreas', blank=True)),
            ('pop', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'Pop', blank=True)),
            ('totpop', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'TotPop', blank=True)),
            ('pcntpop', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'PcntPop', blank=True)),
        ))
        db.send_create_signal(u'majitables', ['Popareabysettlementcounty'])

        # Adding model 'Popareabysettlementslum'
        db.create_table(u'PopAreaBySettlementSlum', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('slumid', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'Slumid', blank=True)),
            ('slumname', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'SlumName')),
            ('settlement', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'Settlement')),
            ('nareas', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'NAreas', blank=True)),
            ('totareas', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'TotAreas', blank=True)),
            ('pcntareas', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'PcntAreas', blank=True)),
            ('pop', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'Pop', blank=True)),
            ('totpop', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'TotPop', blank=True)),
            ('pcntpop', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'PcntPop', blank=True)),
        ))
        db.send_create_signal(u'majitables', ['Popareabysettlementslum'])

        # Adding model 'Popareabysettlementtown'
        db.create_table(u'PopAreaBySettlementTown', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('townid', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'Townid', blank=True)),
            ('townname', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'TownName')),
            ('settlement', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'Settlement')),
            ('nareas', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'NAreas', blank=True)),
            ('totareas', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'TotAreas', blank=True)),
            ('pcntareas', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'PcntAreas', blank=True)),
            ('pop', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'Pop', blank=True)),
            ('totpop', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'TotPop', blank=True)),
            ('pcntpop', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'PcntPop', blank=True)),
        ))
        db.send_create_signal(u'majitables', ['Popareabysettlementtown'])

        # Adding model 'Popareatypecounty'
        db.create_table(u'PopAreaTypeCounty', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('countyid', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'CountyID', blank=True)),
            ('countyname', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'CountyName')),
            ('areatype', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'AreaType')),
            ('pop', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'Pop', blank=True)),
            ('nareas', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'Nareas', blank=True)),
        ))
        db.send_create_signal(u'majitables', ['Popareatypecounty'])

        # Adding model 'Popareatypeslum'
        db.create_table(u'PopAreaTypeSlum', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('slumid', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'SlumID')),
            ('slumname', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'SlumName')),
            ('areatype', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'AreaType')),
            ('pop', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'Pop', blank=True)),
            ('nareas', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'Nareas', blank=True)),
        ))
        db.send_create_signal(u'majitables', ['Popareatypeslum'])

        # Adding model 'Popareatypetown'
        db.create_table(u'PopAreaTypeTown', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('townid', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'TownID', blank=True)),
            ('townname', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'TownName')),
            ('areatype', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'AreaType')),
            ('pop', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'Pop', blank=True)),
            ('nareas', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'Nareas', blank=True)),
        ))
        db.send_create_signal(u'majitables', ['Popareatypetown'])

        # Adding model 'Popareatypewsp'
        db.create_table(u'PopAreaTypeWSP', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('wspid', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'WspID')),
            ('wspname', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'WspName')),
            ('areatype', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'AreaType')),
            ('pop', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'Pop', blank=True)),
            ('nareas', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'Nareas', blank=True)),
        ))
        db.send_create_signal(u'majitables', ['Popareatypewsp'])

        # Adding model 'Popareasbylegalcounty'
        db.create_table(u'PopAreasByLegalCounty', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('countyid', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'Countyid', blank=True)),
            ('countyname', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'CountyName')),
            ('legalstatus', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'LegalStatus')),
            ('nareas', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'NAreas', blank=True)),
            ('pop', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'Pop', blank=True)),
            ('avgpopperarea', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'AvgPopPerArea', blank=True)),
            ('totareas', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'TotAreas', blank=True)),
            ('pcntareas', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'PcntAreas', blank=True)),
        ))
        db.send_create_signal(u'majitables', ['Popareasbylegalcounty'])

        # Adding model 'Popareasbylegalslum'
        db.create_table(u'PopAreasByLegalSlum', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('slumid', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'Slumid', blank=True)),
            ('slumname', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'SlumName')),
            ('legalstatus', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'LegalStatus')),
            ('nareas', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'NAreas', blank=True)),
            ('pop', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'Pop', blank=True)),
            ('avgpopperarea', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'AvgPopPerArea', blank=True)),
            ('totareas', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'TotAreas', blank=True)),
            ('pcntareas', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'PcntAreas', blank=True)),
        ))
        db.send_create_signal(u'majitables', ['Popareasbylegalslum'])

        # Adding model 'Popareasbylegaltown'
        db.create_table(u'PopAreasByLegalTown', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('townid', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'Townid', blank=True)),
            ('townname', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'TownName')),
            ('legalstatus', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'LegalStatus')),
            ('nareas', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'NAreas', blank=True)),
            ('pop', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'Pop', blank=True)),
            ('avgpopperarea', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'AvgPopPerArea', blank=True)),
            ('totareas', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'TotAreas', blank=True)),
            ('pcntareas', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'PcntAreas', blank=True)),
        ))
        db.send_create_signal(u'majitables', ['Popareasbylegaltown'])

        # Adding model 'Savgdush44County'
        db.create_table(u'SAvgDUSh44County', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('countyid', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'CountyID', blank=True)),
            ('countyname', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'CountyName')),
            ('dusinsmp', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'DUsInSmp', blank=True)),
            ('dussharing', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'DUsSharing')),
            ('smpdus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'SmpDUs', blank=True)),
            ('pcntdus', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'pcntDUs', blank=True)),
            ('dusinarea', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'DusInArea', blank=True)),
            ('totdus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'TotDUs', blank=True)),
            ('totalppleinarea', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'TotalPpleinArea', blank=True)),
            ('pcntpop', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'PcntPop', blank=True)),
            ('pop', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'Pop', blank=True)),
        ))
        db.send_create_signal(u'majitables', ['Savgdush44County'])

        # Adding model 'Savgdush44Slum'
        db.create_table(u'SAvgDUSh44Slum', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('slumid', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'SlumID', blank=True)),
            ('slumname', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'SlumName')),
            ('dusinsmp', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'DUsInSmp', blank=True)),
            ('dussharing', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'DUsSharing')),
            ('smpdus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'SmpDUs', blank=True)),
            ('pcntdus', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'pcntDUs', blank=True)),
            ('dusinarea', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'DusInArea', blank=True)),
            ('totdus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'TotDUs', blank=True)),
            ('totalppleinarea', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'TotalPpleinArea', blank=True)),
            ('pcntpop', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'PcntPop', blank=True)),
            ('pop', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'Pop', blank=True)),
        ))
        db.send_create_signal(u'majitables', ['Savgdush44Slum'])

        # Adding model 'Savgdush44Wsp'
        db.create_table(u'SAvgDUSh44WSP', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('wspid', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'WSPID')),
            ('wspname', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'WSPName')),
            ('dusinsmp', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'DUsInSmp', blank=True)),
            ('dussharing', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'DUsSharing')),
            ('smpdus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'SmpDUs', blank=True)),
            ('pcntdus', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'pcntDUs', blank=True)),
            ('dusinarea', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'DusInArea', blank=True)),
            ('totdus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'TotDUs', blank=True)),
            ('totalppleinarea', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'TotalPpleinArea', blank=True)),
            ('pcntpop', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'PcntPop', blank=True)),
            ('pop', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'Pop', blank=True)),
        ))
        db.send_create_signal(u'majitables', ['Savgdush44Wsp'])

        # Adding model 'Savgdusshfaccounty'
        db.create_table(u'SAvgDUsShFacCounty', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('countyid', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'CountyID', blank=True)),
            ('countyname', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'CountyName')),
            ('dusinsmp', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'DUsInSmp', blank=True)),
            ('dussharing', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'DUsSharing')),
            ('smpdus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'SmpDUs', blank=True)),
            ('pcntdus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'pcntDUs', blank=True)),
            ('dusinarea', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'DusInArea', blank=True)),
            ('totdus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'TotDUs', blank=True)),
            ('avgdusz', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'AvgDUSz', blank=True)),
            ('pop', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'Pop', blank=True)),
        ))
        db.send_create_signal(u'majitables', ['Savgdusshfaccounty'])

        # Adding model 'Savgdusshfacslum'
        db.create_table(u'SAvgDUsShFacSlum', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('slumid', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'SlumID', blank=True)),
            ('slumname', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'SlumName')),
            ('dusinsmp', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'DUsInSmp', blank=True)),
            ('dussharing', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'DUsSharing')),
            ('smpdus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'SmpDUs', blank=True)),
            ('pcntdus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'pcntDUs', blank=True)),
            ('dusinarea', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'DusInArea', blank=True)),
            ('totdus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'TotDUs', blank=True)),
            ('avgdusz', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'AvgDUSz', blank=True)),
            ('pop', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'Pop', blank=True)),
        ))
        db.send_create_signal(u'majitables', ['Savgdusshfacslum'])

        # Adding model 'Savgdusshfacwsp'
        db.create_table(u'SAvgDUsShFacWSP', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('wspid', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'WSPID')),
            ('wspname', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'WSPName')),
            ('dusinsmp', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'DUsInSmp', blank=True)),
            ('dussharing', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'DUsSharing')),
            ('smpdus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'SmpDUs', blank=True)),
            ('pcntdus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'pcntDUs', blank=True)),
            ('dusinarea', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'DusInArea', blank=True)),
            ('totdus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'TotDUs', blank=True)),
            ('avgdusz', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'AvgDUSz', blank=True)),
            ('pop', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'Pop', blank=True)),
        ))
        db.send_create_signal(u'majitables', ['Savgdusshfacwsp'])

        # Adding model 'Savghhshowntlt'
        db.create_table(u'SAvgHHShOwnTlt', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('areaid', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'AreaID', blank=True)),
            ('areaname', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'Areaname')),
            ('avghhsharing', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'AvgHHsharing')),
            ('maxhhsh', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'MaxHHsh')),
            ('minhhsh', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'MinHHsh')),
            ('areasmpdus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'AreaSmpDUs', blank=True)),
            ('numdu', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'NumDU', blank=True)),
        ))
        db.send_create_signal(u'majitables', ['Savghhshowntlt'])

        # Adding model 'Savgtltbath'
        db.create_table(u'SAvgTltBath', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('areaid', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'AreaID', blank=True)),
            ('areaname', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'Areaname')),
            ('avgnfac', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'AvgNFac', blank=True)),
            ('maxfac', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'MaxFac', blank=True)),
            ('minfac', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'MinFac', blank=True)),
            ('avghhsharing', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'AvgHHsharing')),
            ('maxhhsh', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'MaxHHsh')),
            ('minhhsh', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'MinHHsh')),
            ('avgbaths', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'Avgbaths', blank=True)),
            ('maxbath', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'MaxBath', blank=True)),
            ('minbaths', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'MinBaths', blank=True)),
            ('areasmpdus', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'AreaSmpDUs', blank=True)),
            ('dus', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'DUs', blank=True)),
            ('pcntdus', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'pcntDUs', blank=True)),
            ('ndus', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'NDus', blank=True)),
            ('numdu', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'numDU', blank=True)),
        ))
        db.send_create_signal(u'majitables', ['Savgtltbath'])

        # Adding model 'Sduhasownbath'
        db.create_table(u'SDUHasOwnBath', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('areaid', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'AreaID', blank=True)),
            ('areaname', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'Areaname')),
            ('duownbath', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'DuOwnBath')),
            ('areasmpdus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'AreaSmpDUs', blank=True)),
            ('dus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'DUs', blank=True)),
            ('pcntdus', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'pcntDUs', blank=True)),
            ('ndus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'NDus', blank=True)),
            ('numdu', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'NumDU', blank=True)),
        ))
        db.send_create_signal(u'majitables', ['Sduhasownbath'])

        # Adding model 'Sduhasownfacility'
        db.create_table(u'SDUHasOwnFacility', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('areaid', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'AreaID', blank=True)),
            ('areaname', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'Areaname')),
            ('duhasownfac', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'DuHasOwnFac')),
            ('areasmpdus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'AreaSmpDUs', blank=True)),
            ('dus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'DUs', blank=True)),
            ('pcntdus', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'pcntDUs', blank=True)),
            ('ndus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'NDus', blank=True)),
            ('numdu', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'NumDU', blank=True)),
        ))
        db.send_create_signal(u'majitables', ['Sduhasownfacility'])

        # Adding model 'Sduownbath45County'
        db.create_table(u'SDUOwnBath45County', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('countyid', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'CountyID', blank=True)),
            ('countyname', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'CountyName')),
            ('dusinsmp', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'DUsInSmp', blank=True)),
            ('smpdus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'SmpDUs', blank=True)),
            ('pcntdus', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'pcntDUs', blank=True)),
            ('dusinarea', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'DusInArea', blank=True)),
            ('totdus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'TotDUs', blank=True)),
            ('pop', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'Pop', blank=True)),
        ))
        db.send_create_signal(u'majitables', ['Sduownbath45County'])

        # Adding model 'Sduownbath45Slum'
        db.create_table(u'SDUOwnBath45Slum', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('slumid', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'SlumID', blank=True)),
            ('slumname', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'SlumName')),
            ('dusinsmp', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'DUsInSmp', blank=True)),
            ('smpdus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'SmpDUs', blank=True)),
            ('pcntdus', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'pcntDUs', blank=True)),
            ('dusinarea', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'DusInArea', blank=True)),
            ('totdus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'TotDUs', blank=True)),
            ('pop', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'Pop', blank=True)),
        ))
        db.send_create_signal(u'majitables', ['Sduownbath45Slum'])

        # Adding model 'Sduownbath45Wsp'
        db.create_table(u'SDUOwnBath45WSP', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('wspid', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'WSPID')),
            ('wspname', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'WSPName')),
            ('dusinsmp', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'DUsInSmp', blank=True)),
            ('smpdus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'SmpDUs', blank=True)),
            ('pcntdus', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'pcntDUs', blank=True)),
            ('dusinarea', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'DusInArea', blank=True)),
            ('totdus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'TotDUs', blank=True)),
            ('pop', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'Pop', blank=True)),
        ))
        db.send_create_signal(u'majitables', ['Sduownbath45Wsp'])

        # Adding model 'Sduownfac45County'
        db.create_table(u'SDUOwnFac45County', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('countyid', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'CountyID', blank=True)),
            ('countyname', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'CountyName')),
            ('dusinsmp', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'DUsInSmp', blank=True)),
            ('smpdus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'SmpDUs', blank=True)),
            ('pcntdus', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'pcntDUs', blank=True)),
            ('dusinarea', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'DusInArea', blank=True)),
            ('totdus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'TotDUs', blank=True)),
            ('totalppleinarea', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'TotalPpleinArea', blank=True)),
            ('pcntpop', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'PcntPop', blank=True)),
            ('pop', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'Pop', blank=True)),
        ))
        db.send_create_signal(u'majitables', ['Sduownfac45County'])

        # Adding model 'Sduownfac45Slum'
        db.create_table(u'SDUOwnFac45Slum', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('slumid', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'SlumID', blank=True)),
            ('slumname', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'SlumName')),
            ('dusinsmp', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'DUsInSmp', blank=True)),
            ('smpdus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'SmpDUs', blank=True)),
            ('pcntdus', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'pcntDUs', blank=True)),
            ('dusinarea', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'DusInArea', blank=True)),
            ('totdus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'TotDUs', blank=True)),
            ('totalppleinarea', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'TotalPpleinArea', blank=True)),
            ('pcntpop', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'PcntPop', blank=True)),
            ('pop', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'Pop', blank=True)),
        ))
        db.send_create_signal(u'majitables', ['Sduownfac45Slum'])

        # Adding model 'Sduownfac45Wsp'
        db.create_table(u'SDUOwnFac45WSP', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('wspid', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'WSPID')),
            ('wspname', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'WSPName')),
            ('dusinsmp', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'DUsInSmp', blank=True)),
            ('smpdus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'SmpDUs', blank=True)),
            ('pcntdus', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'pcntDUs', blank=True)),
            ('dusinarea', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'DusInArea', blank=True)),
            ('totdus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'TotDUs', blank=True)),
            ('totalppleinarea', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'TotalPpleinArea', blank=True)),
            ('pcntpop', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'PcntPop', blank=True)),
            ('pop', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'Pop', blank=True)),
        ))
        db.send_create_signal(u'majitables', ['Sduownfac45Wsp'])

        # Adding model 'Sduownrpit45County'
        db.create_table(u'SDUOwnRPit45County', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('countyid', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'CountyID', blank=True)),
            ('countyname', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'CountyName')),
            ('dusinsmp', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'DUsInSmp', blank=True)),
            ('smpdus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'SmpDUs', blank=True)),
            ('pcntdus', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'pcntDUs', blank=True)),
            ('dusinarea', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'DusInArea', blank=True)),
            ('totdus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'TotDUs', blank=True)),
            ('pop', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'Pop', blank=True)),
        ))
        db.send_create_signal(u'majitables', ['Sduownrpit45County'])

        # Adding model 'Sduownrpit45Slum'
        db.create_table(u'SDUOwnRPit45Slum', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('slumid', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'SlumID', blank=True)),
            ('slumname', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'SlumName')),
            ('dusinsmp', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'DUsInSmp', blank=True)),
            ('smpdus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'SmpDUs', blank=True)),
            ('pcntdus', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'pcntDUs', blank=True)),
            ('dusinarea', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'DusInArea', blank=True)),
            ('totdus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'TotDUs', blank=True)),
            ('pop', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'Pop', blank=True)),
        ))
        db.send_create_signal(u'majitables', ['Sduownrpit45Slum'])

        # Adding model 'Sduownrpit45Wsp'
        db.create_table(u'SDUOwnRPit45WSP', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('wspid', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'WSPID')),
            ('wspname', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'WSPName')),
            ('dusinsmp', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'DUsInSmp', blank=True)),
            ('smpdus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'SmpDUs', blank=True)),
            ('pcntdus', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'pcntDUs', blank=True)),
            ('dusinarea', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'DusInArea', blank=True)),
            ('totdus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'TotDUs', blank=True)),
            ('pop', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'Pop', blank=True)),
        ))
        db.send_create_signal(u'majitables', ['Sduownrpit45Wsp'])

        # Adding model 'Sdusharestoilet'
        db.create_table(u'SDuSharesToilet', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('areaid', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'AreaID', blank=True)),
            ('areaname', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'Areaname')),
            ('dusharefac', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'DuShareFac')),
            ('areasmpdus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'AreaSmpDUs', blank=True)),
            ('dus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'DUs', blank=True)),
            ('pcntdus', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'pcntDUs', blank=True)),
            ('ndus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'NDus', blank=True)),
            ('numdu', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'NumDU', blank=True)),
        ))
        db.send_create_signal(u'majitables', ['Sdusharestoilet'])

        # Adding model 'Seincomesrcs'
        db.create_table(u'SEIncomeSrcs', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('areaid', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'AreaID', blank=True)),
            ('areaname', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'Areaname')),
            ('maleincsrc', self.gf('django.db.models.fields.TextField')(db_column=u'MaleIncSrc')),
            ('femaleincsrc', self.gf('django.db.models.fields.TextField')(db_column=u'FemaleIncSrc')),
            ('vandlvl', self.gf('django.db.models.fields.TextField')(db_column=u'VandLvl')),
        ))
        db.send_create_signal(u'majitables', ['Seincomesrcs'])

        # Adding model 'Sfacinplotcounty'
        db.create_table(u'SFacInPlotCounty', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('countyid', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'CountyID', blank=True)),
            ('countyname', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'CountyName')),
            ('dusinsmp', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'DUsInSmp', blank=True)),
            ('smpdus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'SmpDUs', blank=True)),
            ('pcntdus', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'pcntDUs', blank=True)),
            ('dusinarea', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'DusInArea', blank=True)),
            ('totdus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'TotDUs', blank=True)),
            ('pop', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'Pop', blank=True)),
        ))
        db.send_create_signal(u'majitables', ['Sfacinplotcounty'])

        # Adding model 'Sfacinplotslum'
        db.create_table(u'SFacInPlotSlum', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('slumid', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'SlumID', blank=True)),
            ('slumname', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'SlumName')),
            ('dusinsmp', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'DUsInSmp', blank=True)),
            ('smpdus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'SmpDUs', blank=True)),
            ('pcntdus', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'pcntDUs', blank=True)),
            ('dusinarea', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'DusInArea', blank=True)),
            ('totdus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'TotDUs', blank=True)),
            ('pop', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'Pop', blank=True)),
        ))
        db.send_create_signal(u'majitables', ['Sfacinplotslum'])

        # Adding model 'Sfacinplotwsp'
        db.create_table(u'SFacInPlotWSP', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('wspid', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'WspID')),
            ('wspname', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'WspName')),
            ('dusinsmp', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'DUsInSmp', blank=True)),
            ('smpdus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'SmpDUs', blank=True)),
            ('pcntdus', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'pcntDUs', blank=True)),
            ('dusinarea', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'DusInArea', blank=True)),
            ('totdus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'TotDUs', blank=True)),
            ('pop', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'Pop', blank=True)),
        ))
        db.send_create_signal(u'majitables', ['Sfacinplotwsp'])

        # Adding model 'Sfacsharedcounty'
        db.create_table(u'SFacSharedCounty', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('countyid', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'CountyID', blank=True)),
            ('countyname', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'CountyName')),
            ('dusinsmp', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'DUsInSmp', blank=True)),
            ('smpdus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'SmpDUs', blank=True)),
            ('pcntdus', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'pcntDUs', blank=True)),
            ('dusinarea', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'DusInArea', blank=True)),
            ('totdus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'TotDUs', blank=True)),
            ('totalppleinarea', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'TotalPpleinArea', blank=True)),
            ('pcntpop', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'PcntPop', blank=True)),
            ('pop', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'Pop', blank=True)),
        ))
        db.send_create_signal(u'majitables', ['Sfacsharedcounty'])

        # Adding model 'Sfacsharedslum'
        db.create_table(u'SFacSharedSlum', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('slumid', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'SlumID', blank=True)),
            ('slumname', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'SlumName')),
            ('dusinsmp', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'DUsInSmp', blank=True)),
            ('smpdus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'SmpDUs', blank=True)),
            ('pcntdus', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'pcntDUs', blank=True)),
            ('dusinarea', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'DusInArea', blank=True)),
            ('totdus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'TotDUs', blank=True)),
            ('totalppleinarea', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'TotalPpleinArea', blank=True)),
            ('pcntpop', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'PcntPop', blank=True)),
            ('pop', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'Pop', blank=True)),
        ))
        db.send_create_signal(u'majitables', ['Sfacsharedslum'])

        # Adding model 'Sfacsharedwsp'
        db.create_table(u'SFacSharedWSP', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('wspid', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'WSPID')),
            ('wspname', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'WSPName')),
            ('dusinsmp', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'DUsInSmp', blank=True)),
            ('smpdus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'SmpDUs', blank=True)),
            ('pcntdus', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'pcntDUs', blank=True)),
            ('dusinarea', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'DusInArea', blank=True)),
            ('totdus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'TotDUs', blank=True)),
            ('totalppleinarea', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'TotalPpleinArea', blank=True)),
            ('pcntpop', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'PcntPop', blank=True)),
            ('pop', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'Pop', blank=True)),
        ))
        db.send_create_signal(u'majitables', ['Sfacsharedwsp'])

        # Adding model 'Sfactypes'
        db.create_table(u'SFacTypes', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('areaid', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'AreaID', blank=True)),
            ('areaname', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'Areaname')),
            ('factype', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'FacType')),
            ('areasmpdus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'AreaSmpDUs', blank=True)),
            ('dus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'DUs', blank=True)),
            ('pcntdus', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'pcntDUs', blank=True)),
            ('ndus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'NDus', blank=True)),
            ('numdu', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'NumDU', blank=True)),
        ))
        db.send_create_signal(u'majitables', ['Sfactypes'])

        # Adding model 'Simpjmp'
        db.create_table(u'SImpJMP', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('areaid', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'AreaID', blank=True)),
            ('areaname', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'Areaname')),
            ('areasmpdus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'AreaSmpDUs', blank=True)),
            ('dusinsmp', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'DUsInSmp', blank=True)),
            ('pcntdus', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'pcntDUs', blank=True)),
            ('dusinarea', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'DusInArea', blank=True)),
            ('smppersons', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'SmpPersons', blank=True)),
            ('totalppleinarea', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'TotalPpleinArea', blank=True)),
            ('pcntpple2', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('totaldusinarea', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'TotalDUsInArea', blank=True)),
        ))
        db.send_create_signal(u'majitables', ['Simpjmp'])

        # Adding model 'Simpjmpcounty'
        db.create_table(u'SImpJMPCounty', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('countyid', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'CountyID', blank=True)),
            ('countyname', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'CountyName')),
            ('dusinsmp', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'DUsInSmp', blank=True)),
            ('smpdus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'SmpDUs', blank=True)),
            ('pcntdus', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'pcntDUs', blank=True)),
            ('dusinarea', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'DusInArea', blank=True)),
            ('totdus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'TotDUs', blank=True)),
            ('totalppleinarea', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'TotalPpleinArea', blank=True)),
            ('pcntpop', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'PcntPop', blank=True)),
            ('pop', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'Pop', blank=True)),
        ))
        db.send_create_signal(u'majitables', ['Simpjmpcounty'])

        # Adding model 'Simpjmpownfac'
        db.create_table(u'SImpJMPOwnFac', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('areaid', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'AreaID', blank=True)),
            ('areaname', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'Areaname')),
            ('areasmpdus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'AreaSmpDUs', blank=True)),
            ('dusinsmp', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'DUsInSmp', blank=True)),
            ('pcntdus', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'pcntDUs', blank=True)),
            ('dusinarea', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'DusInArea', blank=True)),
            ('smppersons', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'SmpPersons', blank=True)),
            ('totalppleinarea', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'TotalPpleinArea', blank=True)),
            ('pcntpple2', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('totaldusinarea', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'TotalDUsInArea', blank=True)),
        ))
        db.send_create_signal(u'majitables', ['Simpjmpownfac'])

        # Adding model 'Simpjmpownplotfac'
        db.create_table(u'SImpJMPOwnPlotFac', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('areaid', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'AreaID', blank=True)),
            ('areaname', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'Areaname')),
            ('areasmpdus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'AreaSmpDUs', blank=True)),
            ('dusinsmp', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'DUsInSmp', blank=True)),
            ('pcntdus', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'pcntDUs', blank=True)),
            ('dusinarea', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'DusInArea', blank=True)),
            ('smppersons', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'SmpPersons', blank=True)),
            ('totalppleinarea', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'TotalPpleinArea', blank=True)),
            ('pcntpple', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('totaldusinarea', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'TotalDUsInArea', blank=True)),
        ))
        db.send_create_signal(u'majitables', ['Simpjmpownplotfac'])

        # Adding model 'Simpjmpshfac'
        db.create_table(u'SImpJMPShFac', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('areaid', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'AreaID', blank=True)),
            ('areaname', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'Areaname')),
            ('areasmpdus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'AreaSmpDUs', blank=True)),
            ('dusinsmp', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'DUsInSmp', blank=True)),
            ('pcntdus', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'pcntDUs', blank=True)),
            ('dusinarea', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'DusInArea', blank=True)),
            ('smppersons', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'SmpPersons', blank=True)),
            ('totalppleinarea', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'TotalPpleinArea', blank=True)),
            ('pcntpple', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('totaldusinarea', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'TotalDUsInArea', blank=True)),
        ))
        db.send_create_signal(u'majitables', ['Simpjmpshfac'])

        # Adding model 'Simpjmpsharedcounty'
        db.create_table(u'SImpJMPSharedCounty', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('countyid', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'CountyID', blank=True)),
            ('countyname', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'CountyName')),
            ('dusinsmp', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'DUsInSmp', blank=True)),
            ('smpdus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'SmpDUs', blank=True)),
            ('pcntdus', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'pcntDUs', blank=True)),
            ('dusinarea', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'DusInArea', blank=True)),
            ('totdus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'TotDUs', blank=True)),
            ('totalppleinarea', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'TotalPpleinArea', blank=True)),
            ('pcntpop', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'PcntPop', blank=True)),
            ('pop', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'Pop', blank=True)),
        ))
        db.send_create_signal(u'majitables', ['Simpjmpsharedcounty'])

        # Adding model 'Simpjmpsharedslum'
        db.create_table(u'SImpJMPSharedSlum', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('slumid', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'SlumID', blank=True)),
            ('slumname', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'SlumName')),
            ('dusinsmp', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'DUsInSmp', blank=True)),
            ('smpdus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'SmpDUs', blank=True)),
            ('pcntdus', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'pcntDUs', blank=True)),
            ('dusinarea', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'DusInArea', blank=True)),
            ('totdus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'TotDUs', blank=True)),
            ('totalppleinarea', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'TotalPpleinArea', blank=True)),
            ('pcntpop', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'PcntPop', blank=True)),
            ('pop', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'Pop', blank=True)),
        ))
        db.send_create_signal(u'majitables', ['Simpjmpsharedslum'])

        # Adding model 'Simpjmpsharedwsp'
        db.create_table(u'SImpJMPSharedWSP', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('wspid', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'WSPID')),
            ('wspname', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'WSPName')),
            ('dusinsmp', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'DUsInSmp', blank=True)),
            ('smpdus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'SmpDUs', blank=True)),
            ('pcntdus', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'pcntDUs', blank=True)),
            ('dusinarea', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'DusInArea', blank=True)),
            ('totdus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'TotDUs', blank=True)),
            ('totalppleinarea', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'TotalPpleinArea', blank=True)),
            ('pcntpop', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'PcntPop', blank=True)),
            ('pop', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'Pop', blank=True)),
        ))
        db.send_create_signal(u'majitables', ['Simpjmpsharedwsp'])

        # Adding model 'Simpjmpslum'
        db.create_table(u'SImpJMPSlum', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('slumid', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'SlumID', blank=True)),
            ('slumname', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'SlumName')),
            ('dusinsmp', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'DUsInSmp', blank=True)),
            ('smpdus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'SmpDUs', blank=True)),
            ('pcntdus', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'pcntDUs', blank=True)),
            ('dusinarea', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'DusInArea', blank=True)),
            ('totdus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'TotDUs', blank=True)),
            ('totalppleinarea', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'TotalPpleinArea', blank=True)),
            ('pcntpop', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'PcntPop', blank=True)),
            ('pop', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'Pop', blank=True)),
        ))
        db.send_create_signal(u'majitables', ['Simpjmpslum'])

        # Adding model 'Simpjmpwsp'
        db.create_table(u'SImpJMPWSP', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('wspid', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'WspID')),
            ('wspname', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'WspName')),
            ('dusinsmp', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'DUsInSmp', blank=True)),
            ('smpdus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'SmpDUs', blank=True)),
            ('pcntdus', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'pcntDUs', blank=True)),
            ('dusinarea', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'DusInArea', blank=True)),
            ('totdus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'TotDUs', blank=True)),
            ('totalppleinarea', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'TotalPpleinArea', blank=True)),
            ('pcntpop', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'PcntPop', blank=True)),
            ('pop', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'Pop', blank=True)),
        ))
        db.send_create_signal(u'majitables', ['Simpjmpwsp'])

        # Adding model 'Snofacused'
        db.create_table(u'SNoFacUsed', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('areaid', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'AreaID', blank=True)),
            ('areaname', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'Areaname')),
            ('areasmpdus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'AreaSmpDUs', blank=True)),
            ('dusinsmp', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'DUsInSmp', blank=True)),
            ('pcntdus', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'pcntDUs', blank=True)),
            ('dusinarea', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'DusInArea', blank=True)),
            ('smppersons', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'SmpPersons', blank=True)),
            ('totalppleinarea', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'TotalPpleinArea', blank=True)),
            ('pcntpple', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('totaldusinarea', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'TotalDUsInArea', blank=True)),
        ))
        db.send_create_signal(u'majitables', ['Snofacused'])

        # Adding model 'Snofacusedcounty'
        db.create_table(u'SNoFacUsedCounty', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('countyid', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'CountyID', blank=True)),
            ('countyname', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'CountyName')),
            ('dusinsmp', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'DUsInSmp', blank=True)),
            ('smpdus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'SmpDUs', blank=True)),
            ('pcntdus', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'pcntDUs', blank=True)),
            ('dusinarea', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'DusInArea', blank=True)),
            ('totdus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'TotDUs', blank=True)),
            ('totalppleinarea', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'TotalPpleinArea', blank=True)),
            ('pcntpop', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'PcntPop', blank=True)),
            ('pop', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'Pop', blank=True)),
        ))
        db.send_create_signal(u'majitables', ['Snofacusedcounty'])

        # Adding model 'Snofacusedslum'
        db.create_table(u'SNoFacUsedSlum', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('slumid', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'SlumID', blank=True)),
            ('slumname', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'SlumName')),
            ('dusinsmp', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'DUsInSmp', blank=True)),
            ('smpdus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'SmpDUs', blank=True)),
            ('pcntdus', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'pcntDUs', blank=True)),
            ('dusinarea', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'DusInArea', blank=True)),
            ('totdus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'TotDUs', blank=True)),
            ('totalppleinarea', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'TotalPpleinArea', blank=True)),
            ('pcntpop', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'PcntPop', blank=True)),
            ('pop', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'Pop', blank=True)),
        ))
        db.send_create_signal(u'majitables', ['Snofacusedslum'])

        # Adding model 'Snofacusedwsp'
        db.create_table(u'SNoFacUsedWSP', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('wspid', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'WSPID')),
            ('wspname', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'WSPName')),
            ('dusinsmp', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'DUsInSmp', blank=True)),
            ('smpdus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'SmpDUs', blank=True)),
            ('pcntdus', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'pcntDUs', blank=True)),
            ('dusinarea', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'DusInArea', blank=True)),
            ('totdus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'TotDUs', blank=True)),
            ('totalppleinarea', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'TotalPpleinArea', blank=True)),
            ('pcntpop', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'PcntPop', blank=True)),
            ('pop', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'Pop', blank=True)),
        ))
        db.send_create_signal(u'majitables', ['Snofacusedwsp'])

        # Adding model 'Snoofbaths'
        db.create_table(u'SNoofBaths', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('areaid', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'AreaID', blank=True)),
            ('areaname', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'Areaname')),
            ('nbaths', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'NBaths')),
            ('areasmpdus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'AreaSmpDUs', blank=True)),
            ('dus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'DUs', blank=True)),
            ('pcntdus', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'pcntDUs', blank=True)),
            ('ndus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'NDus', blank=True)),
            ('numdu', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'NumDU', blank=True)),
        ))
        db.send_create_signal(u'majitables', ['Snoofbaths'])

        # Adding model 'Snoofdushrngtlt'
        db.create_table(u'SNoofDUShrngTlt', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('areaid', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'AreaID', blank=True)),
            ('areaname', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'Areaname')),
            ('nshhhs', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'NshHHs')),
            ('areasmpdus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'AreaSmpDUs', blank=True)),
            ('dus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'DUs', blank=True)),
            ('pcntdus', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'pcntDUs', blank=True)),
            ('ndus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'NDus', blank=True)),
            ('numdu', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'NumDU', blank=True)),
        ))
        db.send_create_signal(u'majitables', ['Snoofdushrngtlt'])

        # Adding model 'Snooffacilities'
        db.create_table(u'SNoofFacilities', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('areaid', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'AreaID', blank=True)),
            ('areaname', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'Areaname')),
            ('nfacilities', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'Nfacilities')),
            ('areasmpdus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'AreaSmpDUs', blank=True)),
            ('dus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'DUs', blank=True)),
            ('pcntdus', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'pcntDUs', blank=True)),
            ('ndus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'NDus', blank=True)),
            ('numdu', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'NumDU', blank=True)),
        ))
        db.send_create_signal(u'majitables', ['Snooffacilities'])

        # Adding model 'Sownimpjmpcounty'
        db.create_table(u'SOwnImpJMPCounty', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('countyid', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'CountyID', blank=True)),
            ('countyname', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'CountyName')),
            ('dusinsmp', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'DUsInSmp', blank=True)),
            ('smpdus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'SmpDUs', blank=True)),
            ('pcntdus', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'pcntDUs', blank=True)),
            ('dusinarea', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'DusInArea', blank=True)),
            ('totdus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'TotDUs', blank=True)),
            ('totalppleinarea', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'TotalPpleinArea', blank=True)),
            ('pcntpop', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'PcntPop', blank=True)),
            ('pop', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'Pop', blank=True)),
        ))
        db.send_create_signal(u'majitables', ['Sownimpjmpcounty'])

        # Adding model 'Sownimpjmpslum'
        db.create_table(u'SOwnImpJMPSlum', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('slumid', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'SlumID', blank=True)),
            ('slumname', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'SlumName')),
            ('dusinsmp', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'DUsInSmp', blank=True)),
            ('smpdus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'SmpDUs', blank=True)),
            ('pcntdus', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'pcntDUs', blank=True)),
            ('dusinarea', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'DusInArea', blank=True)),
            ('totdus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'TotDUs', blank=True)),
            ('totalppleinarea', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'TotalPpleinArea', blank=True)),
            ('pcntpop', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'PcntPop', blank=True)),
            ('pop', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'Pop', blank=True)),
        ))
        db.send_create_signal(u'majitables', ['Sownimpjmpslum'])

        # Adding model 'Sownimpjmpwsp'
        db.create_table(u'SOwnImpJMPWSP', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('wspid', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'WSPID')),
            ('wspname', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'WSPName')),
            ('dusinsmp', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'DUsInSmp', blank=True)),
            ('smpdus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'SmpDUs', blank=True)),
            ('pcntdus', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'pcntDUs', blank=True)),
            ('dusinarea', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'DusInArea', blank=True)),
            ('totdus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'TotDUs', blank=True)),
            ('totalppleinarea', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'TotalPpleinArea', blank=True)),
            ('pcntpop', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'PcntPop', blank=True)),
            ('pop', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'Pop', blank=True)),
        ))
        db.send_create_signal(u'majitables', ['Sownimpjmpwsp'])

        # Adding model 'Spractice'
        db.create_table(u'SPractice', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('areaid', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'AreaID', blank=True)),
            ('areaname', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'Areaname')),
            ('factype', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'FacType')),
            ('areasmpdus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'AreaSmpDUs', blank=True)),
            ('dus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'DUs', blank=True)),
            ('pcntdus', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'pcntDUs', blank=True)),
            ('ndus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'NDus', blank=True)),
            ('numdu', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'NumDU', blank=True)),
        ))
        db.send_create_signal(u'majitables', ['Spractice'])

        # Adding model 'Ssepbaths'
        db.create_table(u'SSepBaths', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('areaid', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'AreaID', blank=True)),
            ('areaname', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'Areaname')),
            ('nsepbaths', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'NSepBaths')),
            ('areasmpdus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'AreaSmpDUs', blank=True)),
            ('dus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'DUs', blank=True)),
            ('pcntdus', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'pcntDUs', blank=True)),
            ('ndus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'NDus', blank=True)),
            ('numdu', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'NumDU', blank=True)),
        ))
        db.send_create_signal(u'majitables', ['Ssepbaths'])

        # Adding model 'Sseptoilets'
        db.create_table(u'SSepToilets', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('areaid', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'AreaID', blank=True)),
            ('areaname', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'Areaname')),
            ('separatefac', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'SeparateFac')),
            ('areasmpdus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'AreaSmpDUs', blank=True)),
            ('dus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'DUs', blank=True)),
            ('pcntdus', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'pcntDUs', blank=True)),
            ('ndus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'NDus', blank=True)),
            ('numdu', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'NumDU', blank=True)),
        ))
        db.send_create_signal(u'majitables', ['Sseptoilets'])

        # Adding model 'Swduhasownrpit'
        db.create_table(u'SWDUHasOwnRpit', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('areaid', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'AreaID', blank=True)),
            ('areaname', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'Areaname')),
            ('duownrpits', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'DuownRpits')),
            ('areasmpdus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'AreaSmpDUs', blank=True)),
            ('dus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'DUs', blank=True)),
            ('pcntdus', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'pcntDUs', blank=True)),
            ('ndus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'NDus', blank=True)),
            ('numdu', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'NumDU', blank=True)),
        ))
        db.send_create_signal(u'majitables', ['Swduhasownrpit'])

        # Adding model 'Swnoofrubpits'
        db.create_table(u'SWNoofRubPits', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('areaid', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'AreaID', blank=True)),
            ('areaname', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'Areaname')),
            ('nrubpits', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'NRubPits')),
            ('areasmpdus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'AreaSmpDUs', blank=True)),
            ('dus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'DUs', blank=True)),
            ('pcntdus', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'pcntDUs', blank=True)),
            ('ndus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'NDus', blank=True)),
            ('numdu', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'NumDU', blank=True)),
        ))
        db.send_create_signal(u'majitables', ['Swnoofrubpits'])

        # Adding model 'Swrpitshared'
        db.create_table(u'SWRPitShared', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('areaid', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'AreaID', blank=True)),
            ('areaname', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'Areaname')),
            ('dusharerpits', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'DuShareRpits')),
            ('areasmpdus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'AreaSmpDUs', blank=True)),
            ('dus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'DUs', blank=True)),
            ('pcntdus', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'pcntDUs', blank=True)),
            ('ndus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'NDus', blank=True)),
            ('numdu', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'NumDU', blank=True)),
        ))
        db.send_create_signal(u'majitables', ['Swrpitshared'])

        # Adding model 'Sanfacpractcounty'
        db.create_table(u'SanFacPractCounty', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('countyid', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'CountyID', blank=True)),
            ('countyname', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'CountyName')),
            ('factype', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'FacType')),
            ('dusinsmp', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'DUsInSmp', blank=True)),
            ('smpdus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'SmpDUs', blank=True)),
            ('pcntdus', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'pcntDUs', blank=True)),
            ('ndus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'NDus', blank=True)),
            ('totdus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'TotDUs', blank=True)),
        ))
        db.send_create_signal(u'majitables', ['Sanfacpractcounty'])

        # Adding model 'Sanfacpractslum'
        db.create_table(u'SanFacPractSlum', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('slumid', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'SlumID', blank=True)),
            ('slumname', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'SlumName')),
            ('factype', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'FacType')),
            ('dusinsmp', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'DUsInSmp', blank=True)),
            ('smpdus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'SmpDUs', blank=True)),
            ('pcntdus', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'pcntDUs', blank=True)),
            ('ndus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'NDus', blank=True)),
            ('totdus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'TotDUs', blank=True)),
        ))
        db.send_create_signal(u'majitables', ['Sanfacpractslum'])

        # Adding model 'Sanfacpractwsp'
        db.create_table(u'SanFacPractWSP', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('wspid', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'WSPID')),
            ('wspname', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'WSPName')),
            ('factype', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'FacType')),
            ('dusinsmp', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'DUsInSmp', blank=True)),
            ('smpdus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'SmpDUs', blank=True)),
            ('pcntdus', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'pcntDUs', blank=True)),
            ('ndus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'NDus', blank=True)),
            ('totdus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'TotDUs', blank=True)),
        ))
        db.send_create_signal(u'majitables', ['Sanfacpractwsp'])

        # Adding model 'Sanitation12B'
        db.create_table(u'Sanitation-12b', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('areaid', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'AreaID', blank=True)),
            ('areaname', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'Areaname')),
            ('facshared', self.gf('django.db.models.fields.TextField')(db_column=u'FacShared')),
            ('cmnmaterials', self.gf('django.db.models.fields.TextField')(db_column=u'CmnMaterials')),
            ('pitscovered', self.gf('django.db.models.fields.TextField')(db_column=u'Pitscovered')),
            ('usedasstore', self.gf('django.db.models.fields.TextField')(db_column=u'UsedasStore')),
            ('usedasbath', self.gf('django.db.models.fields.TextField')(db_column=u'UsedasBath')),
            ('usedfordumping', self.gf('django.db.models.fields.TextField')(db_column=u'UsedforDumping')),
            ('pitsemptied', self.gf('django.db.models.fields.TextField')(db_column=u'PitsEmptied')),
            ('howemptied', self.gf('django.db.models.fields.TextField')(db_column=u'HowEmptied')),
            ('dispmthd', self.gf('django.db.models.fields.TextField')(db_column=u'DispMthd')),
            ('mnsproblem', self.gf('django.db.models.fields.TextField')(db_column=u'MnSProblem')),
            ('anysanproj', self.gf('django.db.models.fields.TextField')(db_column=u'AnySanProj')),
        ))
        db.send_create_signal(u'majitables', ['Sanitation12B'])

        # Adding model 'Sanitationpractice'
        db.create_table(u'SanitationPractice', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('areaid', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'AreaID', blank=True)),
            ('areaname', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'Areaname')),
            ('factype', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'FacType')),
            ('areasmpdus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'AreaSmpDUs', blank=True)),
            ('dus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'DUs', blank=True)),
            ('pcntdus', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'pcntDUs', blank=True)),
            ('ndus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'NDus', blank=True)),
            ('numdu', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'NumDU', blank=True)),
        ))
        db.send_create_signal(u'majitables', ['Sanitationpractice'])

        # Adding model 'Sanitationsewlnk'
        db.create_table(u'SanitationSewLnk', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('areaid', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'AreaID', blank=True)),
            ('areaname', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'Areaname')),
            ('townid', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'TownID', blank=True)),
            ('arealinkedsanitation', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'AreaLinkedSanitation')),
            ('techstat', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'TechStat')),
            ('snwdist', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'Snwdist')),
            ('sactivecons', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'Sactivecons')),
            ('nseptic', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'NSeptic')),
            ('ncomtoilet', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'Ncomtoilet', blank=True)),
            ('npubtoilet', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'NpubToilet')),
            ('mainsfacility', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'MainSFacility')),
            ('cmnpriv', self.gf('django.db.models.fields.TextField')(db_column=u'CmnPriv')),
            ('cmnpublic', self.gf('django.db.models.fields.TextField')(db_column=u'CmnPublic')),
        ))
        db.send_create_signal(u'majitables', ['Sanitationsewlnk'])

        # Adding model 'Socioeconinfr'
        db.create_table(u'SocioEconInfr', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('areaid', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'AreaID', blank=True)),
            ('areaname', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'Areaname')),
            ('seshop', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'SEshop', blank=True)),
            ('prsch', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'PrSch', blank=True)),
            ('secsch', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'SecSch', blank=True)),
            ('hosp', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'Hosp', blank=True)),
            ('hclinic', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'HClinic', blank=True)),
            ('sesport', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'SEsport', blank=True)),
            ('sebusstn', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'SEbusstn', blank=True)),
            ('sehall', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'SEhall', blank=True)),
            ('sepolice', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'SEpolice', blank=True)),
            ('seoth', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'SEoth', blank=True)),
            ('othinfr', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'OthInfr')),
        ))
        db.send_create_signal(u'majitables', ['Socioeconinfr'])

        # Adding model 'Sownimpntshcounty'
        db.create_table(u'SownImpNtShCounty', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('countyid', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'CountyID', blank=True)),
            ('countyname', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'CountyName')),
            ('dusinsmp', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'DUsInSmp', blank=True)),
            ('smpdus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'SmpDUs', blank=True)),
            ('pcntdus', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'pcntDUs', blank=True)),
            ('dusinarea', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'DusInArea', blank=True)),
            ('totdus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'TotDUs', blank=True)),
            ('totalppleinarea', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'TotalPpleinArea', blank=True)),
            ('pcntpop', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'PcntPop', blank=True)),
            ('pop', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'Pop', blank=True)),
        ))
        db.send_create_signal(u'majitables', ['Sownimpntshcounty'])

        # Adding model 'Sownimpntshslum'
        db.create_table(u'SownImpNtShSlum', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('slumid', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'SlumID', blank=True)),
            ('slumname', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'SlumName')),
            ('dusinsmp', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'DUsInSmp', blank=True)),
            ('smpdus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'SmpDUs', blank=True)),
            ('pcntdus', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'pcntDUs', blank=True)),
            ('dusinarea', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'DusInArea', blank=True)),
            ('totdus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'TotDUs', blank=True)),
            ('totalppleinarea', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'TotalPpleinArea', blank=True)),
            ('pcntpop', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'PcntPop', blank=True)),
            ('pop', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'Pop', blank=True)),
        ))
        db.send_create_signal(u'majitables', ['Sownimpntshslum'])

        # Adding model 'Sownimpntshunpcounty'
        db.create_table(u'SownImpNtShUnpCounty', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('countyid', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'CountyID', blank=True)),
            ('countyname', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'CountyName')),
            ('dusinsmp', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'DUsInSmp', blank=True)),
            ('smpdus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'SmpDUs', blank=True)),
            ('pcntdus', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'pcntDUs', blank=True)),
            ('dusinarea', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'DusInArea', blank=True)),
            ('totdus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'TotDUs', blank=True)),
            ('totalppleinarea', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'TotalPpleinArea', blank=True)),
            ('pcntpop', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'PcntPop', blank=True)),
            ('pop', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'Pop', blank=True)),
        ))
        db.send_create_signal(u'majitables', ['Sownimpntshunpcounty'])

        # Adding model 'Sownimpntshunpslum'
        db.create_table(u'SownImpNtShUnpSlum', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('slumid', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'SlumID', blank=True)),
            ('slumname', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'SlumName')),
            ('dusinsmp', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'DUsInSmp', blank=True)),
            ('smpdus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'SmpDUs', blank=True)),
            ('pcntdus', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'pcntDUs', blank=True)),
            ('dusinarea', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'DusInArea', blank=True)),
            ('totdus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'TotDUs', blank=True)),
            ('totalppleinarea', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'TotalPpleinArea', blank=True)),
            ('pcntpop', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'PcntPop', blank=True)),
            ('pop', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'Pop', blank=True)),
        ))
        db.send_create_signal(u'majitables', ['Sownimpntshunpslum'])

        # Adding model 'Sownimpntshunpwsp'
        db.create_table(u'SownImpNtShUnpWSP', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('wspid', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'WSPID')),
            ('wspname', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'WSPName')),
            ('dusinsmp', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'DUsInSmp', blank=True)),
            ('smpdus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'SmpDUs', blank=True)),
            ('pcntdus', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'pcntDUs', blank=True)),
            ('dusinarea', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'DusInArea', blank=True)),
            ('totdus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'TotDUs', blank=True)),
            ('totalppleinarea', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'TotalPpleinArea', blank=True)),
            ('pcntpop', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'PcntPop', blank=True)),
            ('pop', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'Pop', blank=True)),
        ))
        db.send_create_signal(u'majitables', ['Sownimpntshunpwsp'])

        # Adding model 'Sownimpntshwsp'
        db.create_table(u'SownImpNtShWSP', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('wspid', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'WSPID')),
            ('wspname', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'WSPName')),
            ('dusinsmp', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'DUsInSmp', blank=True)),
            ('smpdus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'SmpDUs', blank=True)),
            ('pcntdus', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'pcntDUs', blank=True)),
            ('dusinarea', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'DusInArea', blank=True)),
            ('totdus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'TotDUs', blank=True)),
            ('totalppleinarea', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'TotalPpleinArea', blank=True)),
            ('pcntpop', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'PcntPop', blank=True)),
            ('pop', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'Pop', blank=True)),
        ))
        db.send_create_signal(u'majitables', ['Sownimpntshwsp'])

        # Adding model 'Summaryshtcounty'
        db.create_table(u'SummaryShtCounty', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('countyid', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'CountyID', blank=True)),
            ('countyname', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'CountyName')),
            ('nareas', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'Nareas', blank=True)),
            ('ntowns', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'NTowns', blank=True)),
            ('pop', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'Pop', blank=True)),
            ('avghhsz', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'AvgHHSz', blank=True)),
            ('popplareas', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'PopPlAreas')),
            ('popunplareas', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'PopUnplAreas')),
            ('nareasregfloodg', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'NareasRegFloodg', blank=True)),
            ('mnsrcpcnt', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'MnSrcPcnt')),
            ('drkwatertreated', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'DrkWaterTreated', blank=True)),
            ('payingforwater', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'PayingforWater', blank=True)),
            ('nareaslinked', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'NareasLinked', blank=True)),
            ('plotsconnected', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'PlotsConnected', blank=True)),
            ('dusconnected', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'DUsConnected')),
            ('safewaterpop', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'SafeWaterPop')),
            ('pipedwaterpop', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'PipedWaterPop')),
            ('impsanpop', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'ImpSanPop', blank=True)),
        ))
        db.send_create_signal(u'majitables', ['Summaryshtcounty'])

        # Adding model 'Summaryshtslum'
        db.create_table(u'SummaryShtSlum', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('slumid', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'SlumID', blank=True)),
            ('slumname', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'SlumName')),
            ('nareas', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'Nareas', blank=True)),
            ('ntowns', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'NTowns', blank=True)),
            ('pop', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'Pop', blank=True)),
            ('avghhsz', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'AvgHHSz', blank=True)),
            ('popplareas', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'PopPlAreas')),
            ('popunplareas', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'PopUnplAreas')),
            ('nareasregfloodg', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'NareasRegFloodg', blank=True)),
            ('mnsrcpcnt', self.gf('django.db.models.fields.CharField')(max_length=67, db_column=u'MnSrcPcnt')),
            ('drkwatertreated', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'DrkWaterTreated', blank=True)),
            ('payingforwater', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'PayingforWater')),
            ('nareaslinked', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'NareasLinked', blank=True)),
            ('plotsconnected', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'PlotsConnected')),
            ('dusconnected', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'DUsConnected')),
            ('safewaterpop', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'SafeWaterPop')),
            ('pipedwaterpop', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'PipedWaterPop')),
            ('impsanpop', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'ImpSanPop')),
        ))
        db.send_create_signal(u'majitables', ['Summaryshtslum'])

        # Adding model 'Summaryshttown'
        db.create_table(u'SummaryShtTown', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('townid', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'TownID', blank=True)),
            ('townname', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'TownName')),
            ('nareas', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'Nareas', blank=True)),
            ('ntowns', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'Ntowns', blank=True)),
            ('pop', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'Pop', blank=True)),
            ('avghhsz', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'AvgHHSz', blank=True)),
            ('popplareas', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'PopPlAreas')),
            ('popunplareas', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'PopUnplAreas')),
            ('nareasregfloodg', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'NareasRegFloodg', blank=True)),
            ('mnsrcpcnt', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'MnSrcPcnt')),
            ('drkwatertreated', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'DrkWaterTreated', blank=True)),
            ('payingforwater', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'PayingforWater', blank=True)),
            ('nareaslinked', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'NareasLinked', blank=True)),
            ('plotsconnected', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'PlotsConnected')),
            ('dusconnected', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'DUsConnected')),
            ('safewaterpop', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'SafeWaterPop')),
            ('pipedwaterpop', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'PipedWaterPop')),
            ('impsanpop', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'ImpSanPop', blank=True)),
        ))
        db.send_create_signal(u'majitables', ['Summaryshttown'])

        # Adding model 'TownsareasCounties'
        db.create_table(u'TownsAreas-Counties', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('countyname', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'CountyName')),
            ('countyid', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'Countyid', blank=True)),
            ('nareas', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'NAreas', blank=True)),
            ('ntowns', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'Ntowns', blank=True)),
            ('pop', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'Pop', blank=True)),
            ('avgpopinarea', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'AvgPopinArea', blank=True)),
        ))
        db.send_create_signal(u'majitables', ['TownsareasCounties'])

        # Adding model 'TownsareasSlum'
        db.create_table(u'TownsAreas-Slum', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('slumname', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'SlumName')),
            ('slumid', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'Slumid')),
            ('nareas', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'NAreas', blank=True)),
            ('ntowns', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'Ntowns', blank=True)),
            ('pop', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'Pop', blank=True)),
            ('avgpopinarea', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'AvgPopinArea', blank=True)),
        ))
        db.send_create_signal(u'majitables', ['TownsareasSlum'])

        # Adding model 'TownsareasTowns'
        db.create_table(u'TownsAreas-Towns', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('townname', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('townid', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'townID', blank=True)),
            ('nareas', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'NAreas', blank=True)),
            ('ntowns', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'Ntowns', blank=True)),
            ('pop', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'Pop', blank=True)),
            ('avgpopinarea', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'AvgPopinArea', blank=True)),
            ('knbspop', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'KNBSPop')),
            ('pcntpop', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'PcntPop')),
        ))
        db.send_create_signal(u'majitables', ['TownsareasTowns'])

        # Adding model 'TownsareasWsp'
        db.create_table(u'TownsAreas-WSP', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('wspname', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'WSPName')),
            ('wspid', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'WSPID')),
            ('nareas', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'NAreas', blank=True)),
            ('ntowns', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'Ntowns', blank=True)),
            ('pop', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'Pop', blank=True)),
            ('avgpopinarea', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'AvgPopinArea', blank=True)),
        ))
        db.send_create_signal(u'majitables', ['TownsareasWsp'])

        # Adding model 'Wadeqsupallksk'
        db.create_table(u'WAdeqSupAllKsk', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('areaid', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'AreaID', blank=True)),
            ('areaname', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'Areaname')),
            ('areapop', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'AreaPop', blank=True)),
            ('pubwaterksks', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'PubWaterKsks', blank=True)),
            ('comwaterksks', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'ComWaterKsks', blank=True)),
            ('nadeqsupplied', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'NAdeqSupplied', blank=True)),
        ))
        db.send_create_signal(u'majitables', ['Wadeqsupallksk'])

        # Adding model 'Wadeqsupimpwstfsrcs'
        db.create_table(u'WAdeqSupImpWSTFSrcs', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('areaid', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'AreaID', blank=True)),
            ('areaname', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'Areaname')),
            ('areapop', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'AreaPop', blank=True)),
            ('pubwsptaps', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'PubWSPTaps', blank=True)),
            ('comtaps', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'ComTaps', blank=True)),
            ('pubwaterksks', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'PubWaterKsks', blank=True)),
            ('comwaterksks', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'ComWaterKsks', blank=True)),
            ('nadeqsupplied', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'NAdeqSupplied', blank=True)),
            ('totalcoveredprivcons', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'TotalCoveredPrivCons', blank=True)),
        ))
        db.send_create_signal(u'majitables', ['Wadeqsupimpwstfsrcs'])

        # Adding model 'Wadeqsupprivcons10D'
        db.create_table(u'WAdeqSupPrivCons-10d', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('areaid', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'AreaID', blank=True)),
            ('areaname', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'Areaname')),
            ('areapop', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'AreaPop', blank=True)),
            ('pcoveredownducon', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'PCoveredOwnDuCon')),
            ('pcoveredpcon', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'PCoveredPCon')),
            ('totalcoveredprivcons', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'TotalCoveredPrivCons', blank=True)),
        ))
        db.send_create_signal(u'majitables', ['Wadeqsupprivcons10D'])

        # Adding model 'Wadeqsuppubtap10D'
        db.create_table(u'WAdeqSupPubTap-10d', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('areaid', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'AreaID', blank=True)),
            ('areaname', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'Areaname')),
            ('areapop', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'AreaPop', blank=True)),
            ('nopubcomtaps', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'NoPubComTaps', blank=True)),
            ('noadeqsupplied', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'NoAdeqSupplied', blank=True)),
        ))
        db.send_create_signal(u'majitables', ['Wadeqsuppubtap10D'])

        # Adding model 'Wadeqsupwspksk'
        db.create_table(u'WAdeqSupWSPKsk', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('areaid', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'AreaID', blank=True)),
            ('areaname', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'Areaname')),
            ('areapop', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'AreaPop', blank=True)),
            ('pubwaterksks', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'PubWaterKsks', blank=True)),
            ('nadeqsupplied', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'NAdeqSupplied', blank=True)),
        ))
        db.send_create_signal(u'majitables', ['Wadeqsupwspksk'])

        # Adding model 'Wareasmnprob33County'
        db.create_table(u'WAreasMnProb33County', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('countyid', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'CountyId', blank=True)),
            ('countyname', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'Countyname')),
            ('mainproblem', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'MainProblem')),
            ('nareas', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'NAreas', blank=True)),
            ('totareas', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'TotAreas', blank=True)),
            ('pcntareas', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'PcntAreas', blank=True)),
        ))
        db.send_create_signal(u'majitables', ['Wareasmnprob33County'])

        # Adding model 'Wareasmnprob33Slum'
        db.create_table(u'WAreasMnProb33Slum', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('slumid', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'SlumId', blank=True)),
            ('slumname', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'Slumname')),
            ('mainproblem', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'MainProblem')),
            ('nareas', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'NAreas', blank=True)),
            ('totareas', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'TotAreas', blank=True)),
            ('pcntareas', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'PcntAreas', blank=True)),
        ))
        db.send_create_signal(u'majitables', ['Wareasmnprob33Slum'])

        # Adding model 'Wareasmnprob33Town'
        db.create_table(u'WAreasMnProb33Town', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('townid', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'TownId', blank=True)),
            ('townname', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'Townname')),
            ('mainproblem', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'MainProblem')),
            ('nareas', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'NAreas', blank=True)),
            ('totareas', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'TotAreas', blank=True)),
            ('pcntareas', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'PcntAreas', blank=True)),
        ))
        db.send_create_signal(u'majitables', ['Wareasmnprob33Town'])

        # Adding model 'Wareasmnprob33Wsp'
        db.create_table(u'WAreasMnProb33WSP', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('wspid', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'WSPId')),
            ('wspname', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'WSPname')),
            ('mainproblem', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'MainProblem')),
            ('nareas', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'NAreas', blank=True)),
            ('totareas', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'TotAreas', blank=True)),
            ('pcntareas', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'PcntAreas', blank=True)),
        ))
        db.send_create_signal(u'majitables', ['Wareasmnprob33Wsp'])

        # Adding model 'Wareasnwlinkcounty'
        db.create_table(u'WAreasNWLinkCounty', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('countyid', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'CountyId', blank=True)),
            ('countyname', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'Countyname')),
            ('nareas', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'Nareas', blank=True)),
            ('arealinkedwater', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'AreaLinkedwater')),
            ('totareas', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'TotAreas', blank=True)),
            ('pcntareas', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'PcntAreas', blank=True)),
        ))
        db.send_create_signal(u'majitables', ['Wareasnwlinkcounty'])

        # Adding model 'Wareasnwlinkslum'
        db.create_table(u'WAreasNWLinkSlum', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('slumid', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'SlumId', blank=True)),
            ('slumname', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'Slumname')),
            ('nareas', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'Nareas', blank=True)),
            ('arealinkedwater', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'AreaLinkedwater')),
            ('totareas', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'TotAreas', blank=True)),
            ('pcntareas', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'PcntAreas', blank=True)),
        ))
        db.send_create_signal(u'majitables', ['Wareasnwlinkslum'])

        # Adding model 'Wareasnwlinktown'
        db.create_table(u'WAreasNWLinkTown', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('townid', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'TownId', blank=True)),
            ('townname', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'Townname')),
            ('nareas', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'Nareas', blank=True)),
            ('arealinkedwater', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'AreaLinkedwater')),
            ('totareas', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'TotAreas', blank=True)),
            ('pcntareas', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'PcntAreas', blank=True)),
        ))
        db.send_create_signal(u'majitables', ['Wareasnwlinktown'])

        # Adding model 'Wareasnwlinkwsp'
        db.create_table(u'WAreasNWLinkWSP', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('wspid', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'WSPId')),
            ('wspname', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'WSPname')),
            ('nareas', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'Nareas', blank=True)),
            ('arealinkedwater', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'AreaLinkedwater')),
            ('totareas', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'TotAreas', blank=True)),
            ('pcntareas', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'PcntAreas', blank=True)),
        ))
        db.send_create_signal(u'majitables', ['Wareasnwlinkwsp'])

        # Adding model 'Wareastechstatcounty'
        db.create_table(u'WAreasTechstatCounty', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('countyid', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'CountyId', blank=True)),
            ('countyname', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'Countyname')),
            ('nareas', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'Nareas', blank=True)),
            ('techstat', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'TechStat')),
            ('totareas', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'TotAreas', blank=True)),
            ('pcntareas', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'PcntAreas', blank=True)),
        ))
        db.send_create_signal(u'majitables', ['Wareastechstatcounty'])

        # Adding model 'Wareastechstatslum'
        db.create_table(u'WAreasTechstatSlum', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('slumid', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'SlumId', blank=True)),
            ('slumname', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'Slumname')),
            ('nareas', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'Nareas', blank=True)),
            ('techstat', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'TechStat')),
            ('totareas', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'TotAreas', blank=True)),
            ('pcntareas', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'PcntAreas', blank=True)),
        ))
        db.send_create_signal(u'majitables', ['Wareastechstatslum'])

        # Adding model 'Wareastechstattown'
        db.create_table(u'WAreasTechstatTown', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('townid', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'TownId', blank=True)),
            ('townname', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'Townname')),
            ('nareas', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'Nareas', blank=True)),
            ('techstat', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'TechStat')),
            ('totareas', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'TotAreas', blank=True)),
            ('pcntareas', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'PcntAreas', blank=True)),
        ))
        db.send_create_signal(u'majitables', ['Wareastechstattown'])

        # Adding model 'Wareastechstatwsp'
        db.create_table(u'WAreasTechstatWSP', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('wspid', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'WSPId')),
            ('wspname', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'WSPname')),
            ('nareas', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'Nareas', blank=True)),
            ('techstat', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'TechStat')),
            ('totareas', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'TotAreas', blank=True)),
            ('pcntareas', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'PcntAreas', blank=True)),
        ))
        db.send_create_signal(u'majitables', ['Wareastechstatwsp'])

        # Adding model 'Wckgsrcpipedcounty'
        db.create_table(u'WCkgSrcPipedCounty', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('countyid', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'CountyID', blank=True)),
            ('countyname', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'CountyName')),
            ('dusinsmp', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'DUsInSmp', blank=True)),
            ('smpdus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'SmpDUs', blank=True)),
            ('pcntdus', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'pcntDUs', blank=True)),
            ('dusinarea', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'DusInArea', blank=True)),
            ('totdus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'TotDUs', blank=True)),
            ('totalppleinarea', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'TotalPpleinArea', blank=True)),
            ('pcntpop', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'PcntPop', blank=True)),
            ('pop', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'Pop', blank=True)),
        ))
        db.send_create_signal(u'majitables', ['Wckgsrcpipedcounty'])

        # Adding model 'Wckgsrcpipedslum'
        db.create_table(u'WCkgSrcPipedSlum', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('slumid', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'SlumID', blank=True)),
            ('slumname', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'SlumName')),
            ('dusinsmp', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'DUsInSmp', blank=True)),
            ('smpdus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'SmpDUs', blank=True)),
            ('pcntdus', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'pcntDUs', blank=True)),
            ('dusinarea', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'DusInArea', blank=True)),
            ('totdus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'TotDUs', blank=True)),
            ('totalppleinarea', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'TotalPpleinArea', blank=True)),
            ('pcntpop', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'PcntPop', blank=True)),
            ('pop', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'Pop', blank=True)),
        ))
        db.send_create_signal(u'majitables', ['Wckgsrcpipedslum'])

        # Adding model 'Wckgsrcpipedtown'
        db.create_table(u'WCkgSrcPipedTown', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('townid', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'TownID', blank=True)),
            ('townname', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'TownName')),
            ('dusinsmp', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'DUsInSmp', blank=True)),
            ('smpdus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'SmpDUs', blank=True)),
            ('pcntdus', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'pcntDUs', blank=True)),
            ('dusinarea', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'DusInArea', blank=True)),
            ('totdus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'TotDUs', blank=True)),
            ('totalppleinarea', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'TotalPpleinArea', blank=True)),
            ('pcntpop', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'PcntPop', blank=True)),
            ('pop', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'Pop', blank=True)),
        ))
        db.send_create_signal(u'majitables', ['Wckgsrcpipedtown'])

        # Adding model 'Wckgsrcpipedwsp'
        db.create_table(u'WCkgSrcPipedWSP', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('wspid', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'WSPID')),
            ('wspname', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'WSPName')),
            ('dusinsmp', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'DUsInSmp', blank=True)),
            ('smpdus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'SmpDUs', blank=True)),
            ('pcntdus', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'pcntDUs', blank=True)),
            ('dusinarea', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'DusInArea', blank=True)),
            ('totdus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'TotDUs', blank=True)),
            ('totalppleinarea', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'TotalPpleinArea', blank=True)),
            ('pcntpop', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'PcntPop', blank=True)),
            ('pop', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'Pop', blank=True)),
        ))
        db.send_create_signal(u'majitables', ['Wckgsrcpipedwsp'])

        # Adding model 'WconstatusDu'
        db.create_table(u'WConStatus-DU', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('areaid', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'AreaID', blank=True)),
            ('areaname', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'Areaname')),
            ('constatus', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'ConStatus')),
            ('dusinsmp', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'DUsInSmp', blank=True)),
            ('pcntdus', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'pcntDUs', blank=True)),
            ('dusinarea', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'DUsInArea', blank=True)),
            ('smpduscon', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'SmpDUsCon', blank=True)),
        ))
        db.send_create_signal(u'majitables', ['WconstatusDu'])

        # Adding model 'Wconstatus34County'
        db.create_table(u'WConStatus34County', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('countyid', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'CountyID', blank=True)),
            ('countyname', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'CountyName')),
            ('constatus', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'ConStatus')),
            ('dusinsmp', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'DUsInSmp', blank=True)),
            ('smpdus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'SmpDUs', blank=True)),
            ('pcntdus', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'pcntDUs', blank=True)),
            ('dusinarea', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'DUsInArea', blank=True)),
            ('totdus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'TotDUs', blank=True)),
        ))
        db.send_create_signal(u'majitables', ['Wconstatus34County'])

        # Adding model 'Wconstatus34Slum'
        db.create_table(u'WConStatus34Slum', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('slumid', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'SlumID', blank=True)),
            ('slumname', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'SlumName')),
            ('constatus', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'ConStatus')),
            ('dusinsmp', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'DUsInSmp', blank=True)),
            ('smpdus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'SmpDUs', blank=True)),
            ('pcntdus', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'pcntDUs', blank=True)),
            ('dusinarea', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'DUsInArea', blank=True)),
            ('totdus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'TotDUs', blank=True)),
        ))
        db.send_create_signal(u'majitables', ['Wconstatus34Slum'])

        # Adding model 'Wconstatus34Town'
        db.create_table(u'WConStatus34Town', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('townid', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'TownID', blank=True)),
            ('townname', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'TownName')),
            ('constatus', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'ConStatus')),
            ('dusinsmp', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'DUsInSmp', blank=True)),
            ('smpdus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'SmpDUs', blank=True)),
            ('pcntdus', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'pcntDUs', blank=True)),
            ('dusinarea', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'DUsInArea', blank=True)),
            ('totdus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'TotDUs', blank=True)),
        ))
        db.send_create_signal(u'majitables', ['Wconstatus34Town'])

        # Adding model 'Wconstatus34Wsp'
        db.create_table(u'WConStatus34WSP', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('wspid', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'WSPID')),
            ('wspname', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'WSPName')),
            ('constatus', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'ConStatus')),
            ('dusinsmp', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'DUsInSmp', blank=True)),
            ('smpdus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'SmpDUs', blank=True)),
            ('pcntdus', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'pcntDUs', blank=True)),
            ('dusinarea', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'DUsInArea', blank=True)),
            ('totdus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'TotDUs', blank=True)),
        ))
        db.send_create_signal(u'majitables', ['Wconstatus34Wsp'])

        # Adding model 'Wconsumption'
        db.create_table(u'WConsumption', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('areaid', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'AreaID', blank=True)),
            ('areaname', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'Areaname')),
            ('wmthconsum', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'WMthconsum')),
            ('areasmpdus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'AreaSmpDUs', blank=True)),
            ('dus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'DUs', blank=True)),
            ('pcntdus', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'pcntDUs', blank=True)),
            ('ndus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'NDus', blank=True)),
            ('numdu', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'NumDU', blank=True)),
        ))
        db.send_create_signal(u'majitables', ['Wconsumption'])

        # Adding model 'Wduconcounty'
        db.create_table(u'WDUConCounty', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('countyid', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'CountyID', blank=True)),
            ('countyname', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'CountyName')),
            ('duownconnection', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'DUOwnconnection')),
            ('dusinsmp', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'DUsInSmp', blank=True)),
            ('smpdus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'SmpDUs', blank=True)),
            ('pcntdus', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'pcntDUs', blank=True)),
            ('totdus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'TotDUs', blank=True)),
        ))
        db.send_create_signal(u'majitables', ['Wduconcounty'])

        # Adding model 'Wduconmetcounty'
        db.create_table(u'WDUConMetCounty', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('countyid', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'CountyID', blank=True)),
            ('countyname', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'CountyName')),
            ('duconmet', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'DUconMet')),
            ('dusinsmp', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'DUsInSmp', blank=True)),
            ('smpdus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'SmpDUs', blank=True)),
            ('pcntdus', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'pcntDUs', blank=True)),
            ('ndus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'NDUs', blank=True)),
            ('totdus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'TotDUs', blank=True)),
        ))
        db.send_create_signal(u'majitables', ['Wduconmetcounty'])

        # Adding model 'Wduconmetslum'
        db.create_table(u'WDUConMetSlum', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('slumid', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'SlumID', blank=True)),
            ('slumname', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'SlumName')),
            ('duconmet', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'DUconMet')),
            ('dusinsmp', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'DUsInSmp', blank=True)),
            ('smpdus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'SmpDUs', blank=True)),
            ('pcntdus', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'pcntDUs', blank=True)),
            ('ndus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'NDUs', blank=True)),
            ('totdus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'TotDUs', blank=True)),
        ))
        db.send_create_signal(u'majitables', ['Wduconmetslum'])

        # Adding model 'Wduconmettown'
        db.create_table(u'WDUConMetTown', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('townid', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'TownID', blank=True)),
            ('townname', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'TownName')),
            ('duconmet', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'DUconMet')),
            ('dusinsmp', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'DUsInSmp', blank=True)),
            ('smpdus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'SmpDUs', blank=True)),
            ('pcntdus', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'pcntDUs', blank=True)),
            ('ndus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'NDUs', blank=True)),
            ('totdus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'TotDUs', blank=True)),
        ))
        db.send_create_signal(u'majitables', ['Wduconmettown'])

        # Adding model 'Wduconmetwsp'
        db.create_table(u'WDUConMetWSP', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('wspid', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'WSPID')),
            ('wspname', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'WSPName')),
            ('duconmet', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'DUconMet')),
            ('dusinsmp', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'DUsInSmp', blank=True)),
            ('smpdus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'SmpDUs', blank=True)),
            ('pcntdus', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'pcntDUs', blank=True)),
            ('ndus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'NDUs', blank=True)),
            ('totdus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'TotDUs', blank=True)),
        ))
        db.send_create_signal(u'majitables', ['Wduconmetwsp'])

        # Adding model 'Wduconslum'
        db.create_table(u'WDUConSlum', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('slumid', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'SlumID', blank=True)),
            ('slumname', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'SlumName')),
            ('duownconnection', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'DUOwnconnection')),
            ('dusinsmp', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'DUsInSmp', blank=True)),
            ('smpdus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'SmpDUs', blank=True)),
            ('pcntdus', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'pcntDUs', blank=True)),
            ('totdus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'TotDUs', blank=True)),
        ))
        db.send_create_signal(u'majitables', ['Wduconslum'])

        # Adding model 'Wducontown'
        db.create_table(u'WDUConTown', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('townid', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'TownID', blank=True)),
            ('townname', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'TownName')),
            ('duownconnection', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'DUOwnconnection')),
            ('dusinsmp', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'DUsInSmp', blank=True)),
            ('smpdus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'SmpDUs', blank=True)),
            ('pcntdus', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'pcntDUs', blank=True)),
            ('totdus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'TotDUs', blank=True)),
        ))
        db.send_create_signal(u'majitables', ['Wducontown'])

        # Adding model 'Wduconwsp'
        db.create_table(u'WDUConWSP', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('wspid', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'WSPID')),
            ('wspname', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'WSPName')),
            ('duownconnection', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'DUOwnconnection')),
            ('dusinsmp', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'DUsInSmp', blank=True)),
            ('smpdus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'SmpDUs', blank=True)),
            ('pcntdus', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'pcntDUs', blank=True)),
            ('totdus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'TotDUs', blank=True)),
        ))
        db.send_create_signal(u'majitables', ['Wduconwsp'])

        # Adding model 'Wduowncon'
        db.create_table(u'WDUOwnCon', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('areaid', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'AreaID', blank=True)),
            ('areaname', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'Areaname')),
            ('duownconnection', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'DUOwnconnection')),
            ('areasmpdus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'AreaSmpDUs', blank=True)),
            ('dusinsmp', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'DUsInSmp', blank=True)),
            ('pcntdus', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'pcntDUs', blank=True)),
            ('dusinarea', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'DusInArea', blank=True)),
            ('totaldusinarea', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'TotalDUsInArea', blank=True)),
        ))
        db.send_create_signal(u'majitables', ['Wduowncon'])

        # Adding model 'Wduowncon210D'
        db.create_table(u'WDUOwnCon2-10d', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('areaid', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'AreaID', blank=True)),
            ('areaname', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'Areaname')),
            ('duownconnection', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'DUOwnconnection')),
            ('areasmpdus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'AreaSmpDUs', blank=True)),
            ('dusinsmp', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'DUsInSmp', blank=True)),
            ('pcntdus', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'pcntDUs', blank=True)),
            ('dusinarea', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'DusInArea', blank=True)),
            ('totaldusinarea', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'TotalDUsInArea', blank=True)),
        ))
        db.send_create_signal(u'majitables', ['Wduowncon210D'])

        # Adding model 'Wduownconmet'
        db.create_table(u'WDUOwnConMet', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('areaid', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'AreaID', blank=True)),
            ('areaname', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'Areaname')),
            ('duconmetered', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'DUconmetered')),
            ('dusinsmp', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'DUsInSmp', blank=True)),
            ('pcntdus', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'pcntDUs', blank=True)),
            ('dusinarea', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'DUsInArea', blank=True)),
            ('smpduscon', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'SmpDUsCon', blank=True)),
        ))
        db.send_create_signal(u'majitables', ['Wduownconmet'])

        # Adding model 'Wduownconmet210D'
        db.create_table(u'WDUOwnConMet2-10d', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('areaid', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'AreaID', blank=True)),
            ('areaname', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'Areaname')),
            ('duconmetered', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'DUconmetered')),
            ('dusinsmp', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'DUsInSmp', blank=True)),
            ('pcntdus', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'pcntDUs', blank=True)),
            ('dusinarea', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'DUsInArea', blank=True)),
            ('smpduscon', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'SmpDUsCon', blank=True)),
        ))
        db.send_create_signal(u'majitables', ['Wduownconmet210D'])

        # Adding model 'Wduwaterpaycounty'
        db.create_table(u'WDUWaterPayCounty', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('countyid', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'CountyID', blank=True)),
            ('countyname', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'CountyName')),
            ('waterpaid', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'WaterPaid')),
            ('smpsrc', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'SmpSrc', blank=True)),
            ('smpdus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'SmpDUs', blank=True)),
            ('totdus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'TotDUs', blank=True)),
            ('pcntusingsrc', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'PcntUsingSrc', blank=True)),
            ('nousingsrc', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'NoUsingSrc', blank=True)),
        ))
        db.send_create_signal(u'majitables', ['Wduwaterpaycounty'])

        # Adding model 'Wduwaterpayslum'
        db.create_table(u'WDUWaterPaySlum', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('slumid', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'SlumID', blank=True)),
            ('slumname', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'SlumName')),
            ('waterpaid', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'WaterPaid')),
            ('smpsrc', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'SmpSrc', blank=True)),
            ('smpdus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'SmpDUs', blank=True)),
            ('totdus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'TotDUs', blank=True)),
            ('pcntusingsrc', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'PcntUsingSrc', blank=True)),
            ('nousingsrc', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'NoUsingSrc', blank=True)),
        ))
        db.send_create_signal(u'majitables', ['Wduwaterpayslum'])

        # Adding model 'Wduwaterpaytown'
        db.create_table(u'WDUWaterPayTown', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('townid', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'TownID', blank=True)),
            ('townname', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'TownName')),
            ('waterpaid', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'WaterPaid')),
            ('smpsrc', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'SmpSrc', blank=True)),
            ('smpdus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'SmpDUs', blank=True)),
            ('totdus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'TotDUs', blank=True)),
            ('pcntusingsrc', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'PcntUsingSrc', blank=True)),
            ('nousingsrc', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'NoUsingSrc', blank=True)),
        ))
        db.send_create_signal(u'majitables', ['Wduwaterpaytown'])

        # Adding model 'Wduwaterpaywsp'
        db.create_table(u'WDUWaterPayWSP', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('wspid', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'WSPID')),
            ('wspname', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'WSPName')),
            ('waterpaid', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'WaterPaid')),
            ('smpsrc', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'SmpSrc', blank=True)),
            ('smpdus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'SmpDUs', blank=True)),
            ('totdus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'TotDUs', blank=True)),
            ('pcntusingsrc', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'PcntUsingSrc', blank=True)),
            ('nousingsrc', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'NoUsingSrc', blank=True)),
        ))
        db.send_create_signal(u'majitables', ['Wduwaterpaywsp'])

        # Adding model 'Wdrkqlty33County'
        db.create_table(u'WDrkQlty33County', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('countyid', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'CountyID', blank=True)),
            ('countyname', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'CountyName')),
            ('wqlty', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'WQlty')),
            ('smpsrc', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'SmpSrc', blank=True)),
            ('smpdus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'SmpDUs', blank=True)),
            ('totdus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'TotDUs', blank=True)),
            ('pcntdususingsrc', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'pcntDUsusingsrc', blank=True)),
            ('nousingsrc', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'NoUsingSrc', blank=True)),
        ))
        db.send_create_signal(u'majitables', ['Wdrkqlty33County'])

        # Adding model 'Wdrkqlty33Slum'
        db.create_table(u'WDrkQlty33Slum', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('countyid', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'CountyID', blank=True)),
            ('countyname', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'CountyName')),
            ('wqlty', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'WQlty')),
            ('smpsrc', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'SmpSrc', blank=True)),
            ('smpdus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'SmpDUs', blank=True)),
            ('totdus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'TotDUs', blank=True)),
            ('pcntdususingsrc', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'pcntDUsusingsrc', blank=True)),
            ('nousingsrc', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'NoUsingSrc', blank=True)),
        ))
        db.send_create_signal(u'majitables', ['Wdrkqlty33Slum'])

        # Adding model 'Wdrkqlty33Town'
        db.create_table(u'WDrkQlty33Town', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('townid', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'TownID', blank=True)),
            ('townname', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'TownName')),
            ('wqlty', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'WQlty')),
            ('smpsrc', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'SmpSrc', blank=True)),
            ('smpdus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'SmpDUs', blank=True)),
            ('totdus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'TotDUs', blank=True)),
            ('pcntdususingsrc', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'pcntDUsusingsrc', blank=True)),
            ('nousingsrc', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'NoUsingSrc', blank=True)),
        ))
        db.send_create_signal(u'majitables', ['Wdrkqlty33Town'])

        # Adding model 'Wdrkqlty33Wsp'
        db.create_table(u'WDrkQlty33WSP', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('wspid', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'WSPID')),
            ('wspname', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'WSPName')),
            ('wqlty', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'WQlty')),
            ('smpsrc', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'SmpSrc', blank=True)),
            ('smpdus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'SmpDUs', blank=True)),
            ('totdus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'TotDUs', blank=True)),
            ('pcntdususingsrc', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'pcntDUsusingsrc', blank=True)),
            ('nousingsrc', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'NoUsingSrc', blank=True)),
        ))
        db.send_create_signal(u'majitables', ['Wdrkqlty33Wsp'])

        # Adding model 'Wdrksrc33County'
        db.create_table(u'WDrkSrc33County', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('countyid', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'CountyID', blank=True)),
            ('countyname', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'CountyName')),
            ('wdrksrc', self.gf('django.db.models.fields.CharField')(max_length=61, db_column=u'WDrkSrc')),
            ('smpsrc', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'SmpSrc', blank=True)),
            ('smpdus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'SmpDUs', blank=True)),
            ('totdus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'TotDUs', blank=True)),
            ('pcntdususingsrc', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'pcntDUsusingsrc', blank=True)),
            ('nousingsrc', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'NoUsingSrc', blank=True)),
        ))
        db.send_create_signal(u'majitables', ['Wdrksrc33County'])

        # Adding model 'Wdrksrc33Slum'
        db.create_table(u'WDrkSrc33Slum', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('slumid', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'SlumID', blank=True)),
            ('slumname', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'SlumName')),
            ('wdrksrc', self.gf('django.db.models.fields.CharField')(max_length=61, db_column=u'WDrkSrc')),
            ('smpsrc', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'SmpSrc', blank=True)),
            ('smpdus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'SmpDUs', blank=True)),
            ('totdus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'TotDUs', blank=True)),
            ('pcntdususingsrc', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'pcntDUsusingsrc', blank=True)),
            ('nousingsrc', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'NoUsingSrc', blank=True)),
        ))
        db.send_create_signal(u'majitables', ['Wdrksrc33Slum'])

        # Adding model 'Wdrksrc33Town'
        db.create_table(u'WDrkSrc33Town', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('townid', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'TownID', blank=True)),
            ('townname', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'TownName')),
            ('wdrksrc', self.gf('django.db.models.fields.CharField')(max_length=61, db_column=u'WDrkSrc')),
            ('smpsrc', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'SmpSrc', blank=True)),
            ('smpdus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'SmpDUs', blank=True)),
            ('totdus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'TotDUs', blank=True)),
            ('pcntdususingsrc', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'pcntDUsusingsrc', blank=True)),
            ('nousingsrc', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'NoUsingSrc', blank=True)),
        ))
        db.send_create_signal(u'majitables', ['Wdrksrc33Town'])

        # Adding model 'Wdrksrc33Wsp'
        db.create_table(u'WDrkSrc33WSP', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('wspid', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'WSPID')),
            ('wspname', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'WSPName')),
            ('wdrksrc', self.gf('django.db.models.fields.CharField')(max_length=61, db_column=u'WDrkSrc')),
            ('smpsrc', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'SmpSrc', blank=True)),
            ('smpdus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'SmpDUs', blank=True)),
            ('totdus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'TotDUs', blank=True)),
            ('pcntdususingsrc', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'pcntDUsusingsrc', blank=True)),
            ('nousingsrc', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'NoUsingSrc', blank=True)),
        ))
        db.send_create_signal(u'majitables', ['Wdrksrc33Wsp'])

        # Adding model 'Wdrksrcbyqltycounty37'
        db.create_table(u'WDrkSrcByQltyCounty-37', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('countyid', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'CountyID', blank=True)),
            ('countyname', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'CountyName')),
            ('wdrksrc', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'WDrkSrc')),
            ('wqlty', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'WQlty')),
            ('smpsrc', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'SmpSrc', blank=True)),
            ('smpdus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'SmpDUs', blank=True)),
            ('totdus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'TotDUs', blank=True)),
            ('pcntdususingsrc', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'pcntDUsusingsrc', blank=True)),
            ('nousingsrc', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'NoUsingSrc', blank=True)),
        ))
        db.send_create_signal(u'majitables', ['Wdrksrcbyqltycounty37'])

        # Adding model 'Wdrksrcbyqltyslum37'
        db.create_table(u'WDrkSrcByQltySlum-37', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('slumid', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'SlumID', blank=True)),
            ('slumname', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'SlumName')),
            ('wdrksrc', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'WDrkSrc')),
            ('wqlty', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'WQlty')),
            ('smpsrc', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'SmpSrc', blank=True)),
            ('smpdus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'SmpDUs', blank=True)),
            ('totdus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'TotDUs', blank=True)),
            ('pcntdususingsrc', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'pcntDUsusingsrc', blank=True)),
            ('nousingsrc', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'NoUsingSrc', blank=True)),
        ))
        db.send_create_signal(u'majitables', ['Wdrksrcbyqltyslum37'])

        # Adding model 'Wdrksrcbyqltytown37'
        db.create_table(u'WDrkSrcByQltyTown-37', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('townid', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'TownID', blank=True)),
            ('townname', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'TownName')),
            ('wdrksrc', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'WDrkSrc')),
            ('wqlty', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'WQlty')),
            ('smpsrc', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'SmpSrc', blank=True)),
            ('smpdus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'SmpDUs', blank=True)),
            ('totdus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'TotDUs', blank=True)),
            ('pcntdususingsrc', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'pcntDUsusingsrc', blank=True)),
            ('nousingsrc', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'NoUsingSrc', blank=True)),
        ))
        db.send_create_signal(u'majitables', ['Wdrksrcbyqltytown37'])

        # Adding model 'Wdrksrcbyqltywsp37'
        db.create_table(u'WDrkSrcByQltyWSP-37', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('wspid', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'WSPID')),
            ('wspname', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'WSPName')),
            ('wdrksrc', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'WDrkSrc')),
            ('wqlty', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'WQlty')),
            ('smpsrc', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'SmpSrc', blank=True)),
            ('smpdus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'SmpDUs', blank=True)),
            ('totdus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'TotDUs', blank=True)),
            ('pcntdususingsrc', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'pcntDUsusingsrc', blank=True)),
            ('nousingsrc', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'NoUsingSrc', blank=True)),
        ))
        db.send_create_signal(u'majitables', ['Wdrksrcbyqltywsp37'])

        # Adding model 'Wdrksrcbytrtmthdslum38'
        db.create_table(u'WDrkSrcByTrtMthdSlum-38', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('slumid', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'SlumID', blank=True)),
            ('slumname', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'SlumName')),
            ('wdrksrc', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'WDrkSrc')),
            ('drkwatertrtmthd', self.gf('django.db.models.fields.TextField')(db_column=u'DrkWaterTrtMthd')),
            ('smpsrc', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'SmpSrc', blank=True)),
            ('smpdus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'SmpDUs', blank=True)),
            ('totdus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'TotDUs', blank=True)),
            ('pcntdususingsrc', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'pcntDUsusingsrc', blank=True)),
            ('nousingsrc', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'NoUsingSrc', blank=True)),
        ))
        db.send_create_signal(u'majitables', ['Wdrksrcbytrtmthdslum38'])

        # Adding model 'Wdrksrcbytrtmthdtown38'
        db.create_table(u'WDrkSrcByTrtMthdTown-38', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('townid', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'TownID', blank=True)),
            ('townname', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'TownName')),
            ('wdrksrc', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'WDrkSrc')),
            ('drkwatertrtmthd', self.gf('django.db.models.fields.CharField')(max_length=65, db_column=u'DrkWaterTrtMthd')),
            ('smpsrc', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'SmpSrc', blank=True)),
            ('smpdus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'SmpDUs', blank=True)),
            ('totdus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'TotDUs', blank=True)),
            ('pcntdususingsrc', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'pcntDUsusingsrc', blank=True)),
            ('nousingsrc', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'NoUsingSrc', blank=True)),
        ))
        db.send_create_signal(u'majitables', ['Wdrksrcbytrtmthdtown38'])

        # Adding model 'Wdrksrcbytrtmthdwsp38'
        db.create_table(u'WDrkSrcByTrtMthdWSP-38', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('wspid', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'WSPID')),
            ('wspname', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'WSPName')),
            ('wdrksrc', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'WDrkSrc')),
            ('drkwatertrtmthd', self.gf('django.db.models.fields.CharField')(max_length=65, db_column=u'DrkWaterTrtMthd')),
            ('smpsrc', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'SmpSrc', blank=True)),
            ('smpdus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'SmpDUs', blank=True)),
            ('totdus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'TotDUs', blank=True)),
            ('pcntdususingsrc', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'pcntDUsusingsrc', blank=True)),
            ('nousingsrc', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'NoUsingSrc', blank=True)),
        ))
        db.send_create_signal(u'majitables', ['Wdrksrcbytrtmthdwsp38'])

        # Adding model 'Wdrksrccmtaps10D'
        db.create_table(u'WDrkSrcCmTaps-10d', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('areaid', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'AreaID', blank=True)),
            ('areaname', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'Areaname')),
            ('areasmpdus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'AreaSmpDUs', blank=True)),
            ('dusinsmp', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'DUsInSmp', blank=True)),
            ('pcntdus', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'pcntDUs', blank=True)),
            ('dusinarea', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'DusInArea', blank=True)),
            ('smppersons', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'SmpPersons', blank=True)),
            ('totalppleinarea', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'TotalPpleinArea', blank=True)),
            ('pcntpple', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('totaldusinarea', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'TotalDUsInArea', blank=True)),
        ))
        db.send_create_signal(u'majitables', ['Wdrksrccmtaps10D'])

        # Adding model 'Wdrksrcleak'
        db.create_table(u'WDrkSrcLeak', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('areaid', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'AreaID', blank=True)),
            ('areaname', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'Areaname')),
            ('areasmpdus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'AreaSmpDUs', blank=True)),
            ('dusinsmp', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'DUsInSmp', blank=True)),
            ('pcntdus', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'pcntDUs', blank=True)),
            ('dusinarea', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'DusInArea', blank=True)),
            ('smppersons', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'SmpPersons', blank=True)),
            ('totalppleinarea', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'TotalPpleinArea', blank=True)),
            ('pcntpple', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('totaldusinarea', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'TotalDUsInArea', blank=True)),
        ))
        db.send_create_signal(u'majitables', ['Wdrksrcleak'])

        # Adding model 'Wdrksrcothcon'
        db.create_table(u'WDrkSrcOthCon', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('areaid', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'AreaID', blank=True)),
            ('areaname', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'Areaname')),
            ('areasmpdus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'AreaSmpDUs', blank=True)),
            ('dusinsmp', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'DUsInSmp', blank=True)),
            ('pcntdus', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'pcntDUs', blank=True)),
            ('dusinarea', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'DusInArea', blank=True)),
            ('smppersons', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'SmpPersons', blank=True)),
            ('totalppleinarea', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'TotalPpleinArea', blank=True)),
            ('pcntpple', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('totaldusinarea', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'TotalDUsInArea', blank=True)),
        ))
        db.send_create_signal(u'majitables', ['Wdrksrcothcon'])

        # Adding model 'Wdrksrcpipedcounty'
        db.create_table(u'WDrkSrcPipedCounty', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('countyid', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'CountyID', blank=True)),
            ('countyname', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'CountyName')),
            ('dusinsmp', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'DUsInSmp', blank=True)),
            ('smpdus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'SmpDUs', blank=True)),
            ('pcntdus', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'pcntDUs', blank=True)),
            ('dusinarea', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'DusInArea', blank=True)),
            ('totdus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'TotDUs', blank=True)),
            ('totalppleinarea', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'TotalPpleinArea', blank=True)),
            ('pcntpop', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'PcntPop', blank=True)),
            ('pop', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'Pop', blank=True)),
        ))
        db.send_create_signal(u'majitables', ['Wdrksrcpipedcounty'])

        # Adding model 'Wdrksrcpipedslum'
        db.create_table(u'WDrkSrcPipedSlum', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('slumid', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'SlumID', blank=True)),
            ('slumname', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'SlumName')),
            ('dusinsmp', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'DUsInSmp', blank=True)),
            ('smpdus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'SmpDUs', blank=True)),
            ('pcntdus', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'pcntDUs', blank=True)),
            ('dusinarea', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'DusInArea', blank=True)),
            ('totdus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'TotDUs', blank=True)),
            ('totalppleinarea', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'TotalPpleinArea', blank=True)),
            ('pcntpop', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'PcntPop', blank=True)),
            ('pop', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'Pop', blank=True)),
        ))
        db.send_create_signal(u'majitables', ['Wdrksrcpipedslum'])

        # Adding model 'Wdrksrcpipedtown'
        db.create_table(u'WDrkSrcPipedTown', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('townid', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'TownID', blank=True)),
            ('townname', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'TownName')),
            ('dusinsmp', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'DUsInSmp', blank=True)),
            ('smpdus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'SmpDUs', blank=True)),
            ('pcntdus', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'pcntDUs', blank=True)),
            ('dusinarea', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'DusInArea', blank=True)),
            ('totdus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'TotDUs', blank=True)),
            ('totalppleinarea', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'TotalPpleinArea', blank=True)),
            ('pcntpop', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'PcntPop', blank=True)),
            ('pop', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'Pop', blank=True)),
        ))
        db.send_create_signal(u'majitables', ['Wdrksrcpipedtown'])

        # Adding model 'Wdrksrcpipedwsp'
        db.create_table(u'WDrkSrcPipedWSP', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('wspid', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'WSPID')),
            ('wspname', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'WSPName')),
            ('dusinsmp', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'DUsInSmp', blank=True)),
            ('smpdus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'SmpDUs', blank=True)),
            ('pcntdus', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'pcntDUs', blank=True)),
            ('dusinarea', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'DusInArea', blank=True)),
            ('totdus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'TotDUs', blank=True)),
            ('totalppleinarea', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'TotalPpleinArea', blank=True)),
            ('pcntpop', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'PcntPop', blank=True)),
            ('pop', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'Pop', blank=True)),
        ))
        db.send_create_signal(u'majitables', ['Wdrksrcpipedwsp'])

        # Adding model 'Wdrksrcreseller'
        db.create_table(u'WDrkSrcReseller', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('areaid', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'AreaID', blank=True)),
            ('areaname', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'Areaname')),
            ('areasmpdus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'AreaSmpDUs', blank=True)),
            ('dusinsmp', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'DUsInSmp', blank=True)),
            ('pcntdus', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'pcntDUs', blank=True)),
            ('dusinarea', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'DusInArea', blank=True)),
            ('smppersons', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'SmpPersons', blank=True)),
            ('totalppleinarea', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'TotalPpleinArea', blank=True)),
            ('pcntpple', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('totaldusinarea', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'TotalDUsInArea', blank=True)),
        ))
        db.send_create_signal(u'majitables', ['Wdrksrcreseller'])

        # Adding model 'Wdrksrcywell'
        db.create_table(u'WDrkSrcYWell', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('areaid', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'AreaID', blank=True)),
            ('areaname', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'Areaname')),
            ('areasmpdus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'AreaSmpDUs', blank=True)),
            ('dusinsmp', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'DUsInSmp', blank=True)),
            ('pcntdus', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'pcntDUs', blank=True)),
            ('dusinarea', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'DusInArea', blank=True)),
            ('smppersons', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'SmpPersons', blank=True)),
            ('totalppleinarea', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'TotalPpleinArea', blank=True)),
            ('pcntpple', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('totaldusinarea', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'TotalDUsInArea', blank=True)),
        ))
        db.send_create_signal(u'majitables', ['Wdrksrcywell'])

        # Adding model 'Wfetchdurationdu'
        db.create_table(u'WFetchDurationDU', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('areaid', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'AreaID', blank=True)),
            ('areaname', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'Areaname')),
            ('durationrange', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'DurationRange')),
            ('areasmpdus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'AreaSmpDUs', blank=True)),
            ('smpdus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'SmpDUs', blank=True)),
            ('pcntdus', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'pcntDUs', blank=True)),
            ('ndus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'NDus', blank=True)),
            ('numdu', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'numDU', blank=True)),
        ))
        db.send_create_signal(u'majitables', ['Wfetchdurationdu'])

        # Adding model 'Wimpdrksrcjmp'
        db.create_table(u'WImpDrkSrcJMP', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('areaid', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'AreaID', blank=True)),
            ('areaname', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'Areaname')),
            ('areasmpdus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'AreaSmpDUs', blank=True)),
            ('dusinsmp', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'DUsInSmp', blank=True)),
            ('pcntdus', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'pcntDUs', blank=True)),
            ('dusinarea', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'DusInArea', blank=True)),
            ('smppersons', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'SmpPersons', blank=True)),
            ('totalppleinarea', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'TotalPpleinArea', blank=True)),
            ('pcntpple', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('totaldusinarea', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'TotalDUsInArea', blank=True)),
        ))
        db.send_create_signal(u'majitables', ['Wimpdrksrcjmp'])

        # Adding model 'Wimpdrksrcjmp30Mn'
        db.create_table(u'WImpDrkSrcJMP30mn', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('areaid', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'AreaID', blank=True)),
            ('areaname', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'Areaname')),
            ('areasmpdus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'AreaSmpDUs', blank=True)),
            ('dusinsmp', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'DUsInSmp', blank=True)),
            ('pcntdus', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'pcntDUs', blank=True)),
            ('dusinarea', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'DusInArea', blank=True)),
            ('smppersons', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'SmpPersons', blank=True)),
            ('totalppleinarea', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'TotalPpleinArea', blank=True)),
            ('pcntpple', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('totaldusinarea', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'TotalDUsInArea', blank=True)),
        ))
        db.send_create_signal(u'majitables', ['Wimpdrksrcjmp30Mn'])

        # Adding model 'Wimpdrksrcjmpbyqlty'
        db.create_table(u'WImpDrkSrcJMPByQlty', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('areaid', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'AreaID', blank=True)),
            ('areaname', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'Areaname')),
            ('wqlty', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'WQlty')),
            ('areasmpdus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'AreaSmpDUs', blank=True)),
            ('dusinsmp', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'DUsInSmp', blank=True)),
            ('pcntdus', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'pcntDUs', blank=True)),
            ('dusinarea', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'DusInArea', blank=True)),
            ('smppersons', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'SmpPersons', blank=True)),
            ('totalppleinarea', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'TotalPpleinArea', blank=True)),
            ('pcntpple', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('totaldusinarea', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'TotalDUsInArea', blank=True)),
        ))
        db.send_create_signal(u'majitables', ['Wimpdrksrcjmpbyqlty'])

        # Adding model 'Wimpdrksrcjmpbytrt'
        db.create_table(u'WImpDrkSrcJMPByTrt', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('areaid', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'AreaID', blank=True)),
            ('areaname', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'Areaname')),
            ('wtrtdrk', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'WTrtDrk')),
            ('areasmpdus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'AreaSmpDUs', blank=True)),
            ('dusinsmp', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'DUsInSmp', blank=True)),
            ('pcntdus', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'pcntDUs', blank=True)),
            ('dusinarea', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'DusInArea', blank=True)),
            ('smppersons', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'SmpPersons', blank=True)),
            ('totalppleinarea', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'TotalPpleinArea', blank=True)),
            ('pcntpple', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('totaldusinarea', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'TotalDUsInArea', blank=True)),
        ))
        db.send_create_signal(u'majitables', ['Wimpdrksrcjmpbytrt'])

        # Adding model 'Wimpdrksrcwstf'
        db.create_table(u'WImpDrkSrcWSTF', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('areaid', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'AreaID', blank=True)),
            ('areaname', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'Areaname')),
            ('areasmpdus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'AreaSmpDUs', blank=True)),
            ('dusinsmp', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'DUsInSmp', blank=True)),
            ('pcntdus', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'pcntDUs', blank=True)),
            ('dusinarea', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'DusInArea', blank=True)),
            ('smppersons', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'SmpPersons', blank=True)),
            ('totalppleinarea', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'TotalPpleinArea', blank=True)),
            ('pcntpple', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('totaldusinarea', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'TotalDUsInArea', blank=True)),
        ))
        db.send_create_signal(u'majitables', ['Wimpdrksrcwstf'])

        # Adding model 'Wimpdrksrcwstf30Mn'
        db.create_table(u'WImpDrkSrcWSTF30mn', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('areaid', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'AreaID', blank=True)),
            ('areaname', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'Areaname')),
            ('areasmpdus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'AreaSmpDUs', blank=True)),
            ('dusinsmp', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'DUsInSmp', blank=True)),
            ('pcntdus', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'pcntDUs', blank=True)),
            ('dusinarea', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'DusInArea', blank=True)),
            ('smppersons', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'SmpPersons', blank=True)),
            ('totalppleinarea', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'TotalPpleinArea', blank=True)),
            ('pcntpple', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('totaldusinarea', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'TotalDUsInArea', blank=True)),
        ))
        db.send_create_signal(u'majitables', ['Wimpdrksrcwstf30Mn'])

        # Adding model 'Wimpdrksrcwstfbyqlty'
        db.create_table(u'WImpDrkSrcWSTFByQlty', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('areaid', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'AreaID', blank=True)),
            ('areaname', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'Areaname')),
            ('wqlty', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'WQlty')),
            ('areasmpdus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'AreaSmpDUs', blank=True)),
            ('dusinsmp', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'DUsInSmp', blank=True)),
            ('pcntdus', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'pcntDUs', blank=True)),
            ('dusinarea', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'DusInArea', blank=True)),
            ('smppersons', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'SmpPersons', blank=True)),
            ('totalppleinarea', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'TotalPpleinArea', blank=True)),
            ('pcntpple', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('totaldusinarea', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'TotalDUsInArea', blank=True)),
        ))
        db.send_create_signal(u'majitables', ['Wimpdrksrcwstfbyqlty'])

        # Adding model 'Wimpdrksrcwstfbytrt'
        db.create_table(u'WImpDrkSrcWSTFByTrt', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('areaid', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'AreaID', blank=True)),
            ('areaname', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'Areaname')),
            ('wtrtdrk', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'WTrtDrk')),
            ('areasmpdus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'AreaSmpDUs', blank=True)),
            ('dusinsmp', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'DUsInSmp', blank=True)),
            ('pcntdus', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'pcntDUs', blank=True)),
            ('dusinarea', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'DusInArea', blank=True)),
            ('smppersons', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'SmpPersons', blank=True)),
            ('totalppleinarea', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'TotalPpleinArea', blank=True)),
            ('pcntpple', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('totaldusinarea', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'TotalDUsInArea', blank=True)),
        ))
        db.send_create_signal(u'majitables', ['Wimpdrksrcwstfbytrt'])

        # Adding model 'Wimpsrcbathwstfcounty'
        db.create_table(u'WImpSrcBathWSTFCounty', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('countyid', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'CountyID', blank=True)),
            ('countyname', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'CountyName')),
            ('dusinsmp', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'DUsInSmp', blank=True)),
            ('smpdus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'SmpDUs', blank=True)),
            ('pcntdus', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'pcntDUs', blank=True)),
            ('dusinarea', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'DusInArea', blank=True)),
            ('totdus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'TotDUs', blank=True)),
            ('totalppleinarea', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'TotalPpleinArea', blank=True)),
            ('pcntpop', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'PcntPop', blank=True)),
            ('pop', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'Pop', blank=True)),
        ))
        db.send_create_signal(u'majitables', ['Wimpsrcbathwstfcounty'])

        # Adding model 'Wimpsrcbathwstfslum'
        db.create_table(u'WImpSrcBathWSTFSlum', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('slumid', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'SlumID', blank=True)),
            ('slumname', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'SlumName')),
            ('dusinsmp', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'DUsInSmp', blank=True)),
            ('smpdus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'SmpDUs', blank=True)),
            ('pcntdus', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'pcntDUs', blank=True)),
            ('dusinarea', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'DusInArea', blank=True)),
            ('totdus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'TotDUs', blank=True)),
            ('totalppleinarea', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'TotalPpleinArea', blank=True)),
            ('pcntpop', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'PcntPop', blank=True)),
            ('pop', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'Pop', blank=True)),
        ))
        db.send_create_signal(u'majitables', ['Wimpsrcbathwstfslum'])

        # Adding model 'Wimpsrcbathwstftown'
        db.create_table(u'WImpSrcBathWSTFTown', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('townid', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'TownID', blank=True)),
            ('townname', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'TownName')),
            ('dusinsmp', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'DUsInSmp', blank=True)),
            ('smpdus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'SmpDUs', blank=True)),
            ('pcntdus', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'pcntDUs', blank=True)),
            ('dusinarea', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'DusInArea', blank=True)),
            ('totdus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'TotDUs', blank=True)),
            ('totalppleinarea', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'TotalPpleinArea', blank=True)),
            ('pcntpop', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'PcntPop', blank=True)),
            ('pop', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'Pop', blank=True)),
        ))
        db.send_create_signal(u'majitables', ['Wimpsrcbathwstftown'])

        # Adding model 'Wimpsrcbathwstfwsp'
        db.create_table(u'WImpSrcBathWSTFWSP', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('wspid', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'WSPID')),
            ('wspname', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'WSPName')),
            ('dusinsmp', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'DUsInSmp', blank=True)),
            ('smpdus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'SmpDUs', blank=True)),
            ('pcntdus', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'pcntDUs', blank=True)),
            ('dusinarea', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'DusInArea', blank=True)),
            ('totdus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'TotDUs', blank=True)),
            ('totalppleinarea', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'TotalPpleinArea', blank=True)),
            ('pcntpop', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'PcntPop', blank=True)),
            ('pop', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'Pop', blank=True)),
        ))
        db.send_create_signal(u'majitables', ['Wimpsrcbathwstfwsp'])

        # Adding model 'Wimpsrcckgwstfcounty'
        db.create_table(u'WImpSrcCkgWSTFCounty', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('countyid', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'CountyID', blank=True)),
            ('countyname', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'CountyName')),
            ('dusinsmp', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'DUsInSmp', blank=True)),
            ('smpdus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'SmpDUs', blank=True)),
            ('pcntdus', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'pcntDUs', blank=True)),
            ('dusinarea', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'DusInArea', blank=True)),
            ('totdus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'TotDUs', blank=True)),
            ('totalppleinarea', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'TotalPpleinArea', blank=True)),
            ('pcntpop', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'PcntPop', blank=True)),
            ('pop', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'Pop', blank=True)),
        ))
        db.send_create_signal(u'majitables', ['Wimpsrcckgwstfcounty'])

        # Adding model 'Wimpsrcckgwstfslum'
        db.create_table(u'WImpSrcCkgWSTFSlum', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('slumid', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'SlumID', blank=True)),
            ('slumname', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'SlumName')),
            ('dusinsmp', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'DUsInSmp', blank=True)),
            ('smpdus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'SmpDUs', blank=True)),
            ('pcntdus', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'pcntDUs', blank=True)),
            ('dusinarea', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'DusInArea', blank=True)),
            ('totdus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'TotDUs', blank=True)),
            ('totalppleinarea', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'TotalPpleinArea', blank=True)),
            ('pcntpop', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'PcntPop', blank=True)),
            ('pop', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'Pop', blank=True)),
        ))
        db.send_create_signal(u'majitables', ['Wimpsrcckgwstfslum'])

        # Adding model 'Wimpsrcckgwstftown'
        db.create_table(u'WImpSrcCkgWSTFTown', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('townid', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'TownID', blank=True)),
            ('townname', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'TownName')),
            ('dusinsmp', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'DUsInSmp', blank=True)),
            ('smpdus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'SmpDUs', blank=True)),
            ('pcntdus', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'pcntDUs', blank=True)),
            ('dusinarea', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'DusInArea', blank=True)),
            ('totdus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'TotDUs', blank=True)),
            ('totalppleinarea', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'TotalPpleinArea', blank=True)),
            ('pcntpop', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'PcntPop', blank=True)),
            ('pop', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'Pop', blank=True)),
        ))
        db.send_create_signal(u'majitables', ['Wimpsrcckgwstftown'])

        # Adding model 'Wimpsrcckgwstfwsp'
        db.create_table(u'WImpSrcCkgWSTFWSP', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('wspid', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'WSPID')),
            ('wspname', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'WSPName')),
            ('dusinsmp', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'DUsInSmp', blank=True)),
            ('smpdus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'SmpDUs', blank=True)),
            ('pcntdus', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'pcntDUs', blank=True)),
            ('dusinarea', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'DusInArea', blank=True)),
            ('totdus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'TotDUs', blank=True)),
            ('totalppleinarea', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'TotalPpleinArea', blank=True)),
            ('pcntpop', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'PcntPop', blank=True)),
            ('pop', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'Pop', blank=True)),
        ))
        db.send_create_signal(u'majitables', ['Wimpsrcckgwstfwsp'])

        # Adding model 'Wimpsrcdrkwstfcounty'
        db.create_table(u'WImpSrcDrkWSTFCounty', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('countyid', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'CountyID', blank=True)),
            ('countyname', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'CountyName')),
            ('dusinsmp', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'DUsInSmp', blank=True)),
            ('smpdus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'SmpDUs', blank=True)),
            ('pcntdus', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'pcntDUs', blank=True)),
            ('dusinarea', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'DusInArea', blank=True)),
            ('totdus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'TotDUs', blank=True)),
            ('totalppleinarea', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'TotalPpleinArea', blank=True)),
            ('pcntpop', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'PcntPop', blank=True)),
            ('pop', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'Pop', blank=True)),
        ))
        db.send_create_signal(u'majitables', ['Wimpsrcdrkwstfcounty'])

        # Adding model 'Wimpsrcdrkwstfslum'
        db.create_table(u'WImpSrcDrkWSTFSlum', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('slumid', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'SlumID', blank=True)),
            ('slumname', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'SlumName')),
            ('dusinsmp', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'DUsInSmp', blank=True)),
            ('smpdus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'SmpDUs', blank=True)),
            ('pcntdus', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'pcntDUs', blank=True)),
            ('dusinarea', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'DusInArea', blank=True)),
            ('totdus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'TotDUs', blank=True)),
            ('totalppleinarea', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'TotalPpleinArea', blank=True)),
            ('pcntpop', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'PcntPop', blank=True)),
            ('pop', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'Pop', blank=True)),
        ))
        db.send_create_signal(u'majitables', ['Wimpsrcdrkwstfslum'])

        # Adding model 'Wimpsrcdrkwstfwsp'
        db.create_table(u'WImpSrcDrkWSTFWSP', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('wspid', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'WSPID')),
            ('wspname', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'WSPName')),
            ('dusinsmp', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'DUsInSmp', blank=True)),
            ('smpdus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'SmpDUs', blank=True)),
            ('pcntdus', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'pcntDUs', blank=True)),
            ('dusinarea', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'DusInArea', blank=True)),
            ('totdus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'TotDUs', blank=True)),
            ('totalppleinarea', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'TotalPpleinArea', blank=True)),
            ('pcntpop', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'PcntPop', blank=True)),
            ('pop', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'Pop', blank=True)),
        ))
        db.send_create_signal(u'majitables', ['Wimpsrcdrkwstfwsp'])

        # Adding model 'Wnocompubpsts10D'
        db.create_table(u'WNoComPubPsts-10d', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('areaid', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'AreaID', blank=True)),
            ('areaname', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'AreaName')),
            ('pubwsptaps', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'PubWSPTaps', blank=True)),
            ('comtaps', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'ComTaps', blank=True)),
            ('nopubcomtaps', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'NoPubComTaps', blank=True)),
        ))
        db.send_create_signal(u'majitables', ['Wnocompubpsts10D'])

        # Adding model 'Woutletscounty'
        db.create_table(u'WOutletsCounty', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('countyid', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'CountyID', blank=True)),
            ('countyname', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'CountyName')),
            ('pubwsptaps', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'PubWSPTaps', blank=True)),
            ('comptaps', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'CompTaps', blank=True)),
            ('privtaps', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'PrivTaps', blank=True)),
            ('pubwaterksks', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'PubWaterKsks', blank=True)),
            ('comwaterksks', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'ComWaterKsks', blank=True)),
            ('privwaterksks', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'PrivWaterKsks', blank=True)),
        ))
        db.send_create_signal(u'majitables', ['Woutletscounty'])

        # Adding model 'Woutletsslum'
        db.create_table(u'WOutletsSlum', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('slumid', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'SlumID')),
            ('slumname', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'SlumName')),
            ('pubwsptaps', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'PubWSPTaps', blank=True)),
            ('comptaps', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'CompTaps', blank=True)),
            ('privtaps', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'PrivTaps', blank=True)),
            ('pubwaterksks', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'PubWaterKsks', blank=True)),
            ('comwaterksks', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'ComWaterKsks', blank=True)),
            ('privwaterksks', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'PrivWaterKsks', blank=True)),
        ))
        db.send_create_signal(u'majitables', ['Woutletsslum'])

        # Adding model 'Woutletstown'
        db.create_table(u'WOutletsTown', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('townid', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'TownID', blank=True)),
            ('townname', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'TownName')),
            ('pubwsptaps', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'PubWSPTaps', blank=True)),
            ('comptaps', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'CompTaps', blank=True)),
            ('privtaps', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'PrivTaps', blank=True)),
            ('pubwaterksks', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'PubWaterKsks', blank=True)),
            ('comwaterksks', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'ComWaterKsks', blank=True)),
            ('privwaterksks', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'PrivWaterKsks', blank=True)),
        ))
        db.send_create_signal(u'majitables', ['Woutletstown'])

        # Adding model 'Woutletswsp'
        db.create_table(u'WOutletsWSP', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('wspid', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'WSPID')),
            ('wspname', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'WSPName')),
            ('pubwsptaps', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'PubWSPTaps', blank=True)),
            ('comptaps', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'CompTaps', blank=True)),
            ('privtaps', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'PrivTaps', blank=True)),
            ('pubwaterksks', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'PubWaterKsks', blank=True)),
            ('comwaterksks', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'ComWaterKsks', blank=True)),
            ('privwaterksks', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'PrivWaterKsks', blank=True)),
        ))
        db.send_create_signal(u'majitables', ['Woutletswsp'])

        # Adding model 'Wpconcounty'
        db.create_table(u'WPConCounty', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('countyid', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'CountyID', blank=True)),
            ('countyname', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'CountyName')),
            ('plotconnected', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'Plotconnected')),
            ('dusinsmp', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'DUsInSmp', blank=True)),
            ('smpdus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'SmpDUs', blank=True)),
            ('pcntdus', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'pcntDUs', blank=True)),
            ('dusinarea', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'DusInArea', blank=True)),
            ('totdus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'TotDUs', blank=True)),
        ))
        db.send_create_signal(u'majitables', ['Wpconcounty'])

        # Adding model 'Wpconmetcounty'
        db.create_table(u'WPConMetCounty', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('countyid', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'CountyID', blank=True)),
            ('countyname', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'CountyName')),
            ('plotconmet', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'PlotconMet')),
            ('dusinsmp', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'DUsInSmp', blank=True)),
            ('smpdus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'SmpDUs', blank=True)),
            ('pcntdus', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'pcntDUs', blank=True)),
            ('dusinarea', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'DusInArea', blank=True)),
            ('totdus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'TotDUs', blank=True)),
        ))
        db.send_create_signal(u'majitables', ['Wpconmetcounty'])

        # Adding model 'Wpconmetslum'
        db.create_table(u'WPConMetSlum', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('slumid', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'SlumID', blank=True)),
            ('slumname', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'SlumName')),
            ('plotconmet', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'PlotconMet')),
            ('dusinsmp', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'DUsInSmp', blank=True)),
            ('smpdus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'SmpDUs', blank=True)),
            ('pcntdus', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'pcntDUs', blank=True)),
            ('dusinarea', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'DusInArea', blank=True)),
            ('totdus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'TotDUs', blank=True)),
        ))
        db.send_create_signal(u'majitables', ['Wpconmetslum'])

        # Adding model 'Wpconmettown'
        db.create_table(u'WPConMetTown', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('townid', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'TownID', blank=True)),
            ('townname', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'TownName')),
            ('plotconmet', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'PlotconMet')),
            ('dusinsmp', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'DUsInSmp', blank=True)),
            ('smpdus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'SmpDUs', blank=True)),
            ('pcntdus', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'pcntDUs', blank=True)),
            ('dusinarea', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'DusInArea', blank=True)),
            ('totdus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'TotDUs', blank=True)),
        ))
        db.send_create_signal(u'majitables', ['Wpconmettown'])

        # Adding model 'Wpconmetwsp'
        db.create_table(u'WPConMetWSP', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('wspid', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'WSPID')),
            ('wspname', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'WSPName')),
            ('plotconmet', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'PlotconMet')),
            ('dusinsmp', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'DUsInSmp', blank=True)),
            ('smpdus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'SmpDUs', blank=True)),
            ('pcntdus', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'pcntDUs', blank=True)),
            ('dusinarea', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'DusInArea', blank=True)),
            ('totdus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'TotDUs', blank=True)),
        ))
        db.send_create_signal(u'majitables', ['Wpconmetwsp'])

        # Adding model 'Wpconslum'
        db.create_table(u'WPConSlum', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('slumid', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'SlumID', blank=True)),
            ('slumname', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'SlumName')),
            ('plotconnected', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'Plotconnected')),
            ('dusinsmp', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'DUsInSmp', blank=True)),
            ('smpdus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'SmpDUs', blank=True)),
            ('pcntdus', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'pcntDUs', blank=True)),
            ('dusinarea', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'DusInArea', blank=True)),
            ('totdus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'TotDUs', blank=True)),
        ))
        db.send_create_signal(u'majitables', ['Wpconslum'])

        # Adding model 'Wpcontown'
        db.create_table(u'WPConTown', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('townid', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'TownID', blank=True)),
            ('townname', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'TownName')),
            ('plotconnected', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'Plotconnected')),
            ('dusinsmp', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'DUsInSmp', blank=True)),
            ('smpdus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'SmpDUs', blank=True)),
            ('pcntdus', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'pcntDUs', blank=True)),
            ('dusinarea', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'DusInArea', blank=True)),
            ('totdus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'TotDUs', blank=True)),
        ))
        db.send_create_signal(u'majitables', ['Wpcontown'])

        # Adding model 'Wpconwsp'
        db.create_table(u'WPConWSP', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('wspid', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'wspID')),
            ('wspname', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'wspName')),
            ('plotconnected', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'Plotconnected')),
            ('dusinsmp', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'DUsInSmp', blank=True)),
            ('smpdus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'SmpDUs', blank=True)),
            ('pcntdus', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'pcntDUs', blank=True)),
            ('dusinarea', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'DusInArea', blank=True)),
            ('totdus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'TotDUs', blank=True)),
        ))
        db.send_create_signal(u'majitables', ['Wpconwsp'])

        # Adding model 'Wpducondisconnected'
        db.create_table(u'WPDUConDisconnected', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('areaid', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'AreaID', blank=True)),
            ('areaname', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'Areaname')),
            ('areasmpdus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'AreaSmpDUs', blank=True)),
            ('dusinsmp', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'DUsInSmp', blank=True)),
            ('pcntdus', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'pcntDUs', blank=True)),
            ('dusinarea', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'DUsInArea', blank=True)),
            ('totaldusinarea', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'TotalDUsInArea', blank=True)),
        ))
        db.send_create_signal(u'majitables', ['Wpducondisconnected'])

        # Adding model 'Wpaydrkdu'
        db.create_table(u'WPayDrkDU', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('areaid', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'AreaID', blank=True)),
            ('areaname', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'Areaname')),
            ('wpaydrk', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'WPaydrk')),
            ('areasmpdus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'AreaSmpDUs', blank=True)),
            ('dus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'DUs', blank=True)),
            ('pcntdus', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'pcntDUs', blank=True)),
            ('ndus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'NDus', blank=True)),
            ('numdu', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'numDU', blank=True)),
        ))
        db.send_create_signal(u'majitables', ['Wpaydrkdu'])

        # Adding model 'Wpaynondrkdu'
        db.create_table(u'WPayNonDrkDU', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('areaid', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'AreaID', blank=True)),
            ('areaname', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'Areaname')),
            ('wpaydrk', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'WPaydrk')),
            ('areasmpdus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'AreaSmpDUs', blank=True)),
            ('dus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'DUs', blank=True)),
            ('pcntdus', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'pcntDUs', blank=True)),
            ('ndus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'NDus', blank=True)),
            ('numdu', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'numDU', blank=True)),
        ))
        db.send_create_signal(u'majitables', ['Wpaynondrkdu'])

        # Adding model 'Wpipedsrcbath'
        db.create_table(u'WPipedSrcBath', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('areaid', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'AreaID', blank=True)),
            ('areaname', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'Areaname')),
            ('areasmpdus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'AreaSmpDUs', blank=True)),
            ('dusinsmp', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'DUsInSmp', blank=True)),
            ('pcntdus', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'pcntDUs', blank=True)),
            ('dusinarea', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'DusInArea', blank=True)),
            ('smppersons', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'SmpPersons', blank=True)),
            ('totalppleinarea', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'TotalPpleinArea', blank=True)),
            ('pcntpple', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('totaldusinarea', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'TotalDUsInArea', blank=True)),
        ))
        db.send_create_signal(u'majitables', ['Wpipedsrcbath'])

        # Adding model 'Wpipedsrcdrk'
        db.create_table(u'WPipedSrcDrk', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('areaid', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'AreaID', blank=True)),
            ('areaname', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'Areaname')),
            ('areasmpdus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'AreaSmpDUs', blank=True)),
            ('dusinsmp', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'DUsInSmp', blank=True)),
            ('pcntdus', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'pcntDUs', blank=True)),
            ('dusinarea', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'DusInArea', blank=True)),
            ('smppersons', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'SmpPersons', blank=True)),
            ('totalppleinarea', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'TotalPpleinArea', blank=True)),
            ('pcntpple', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('totaldusinarea', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'TotalDUsInArea', blank=True)),
        ))
        db.send_create_signal(u'majitables', ['Wpipedsrcdrk'])

        # Adding model 'Wpipedsrcdrkavgpay'
        db.create_table(u'WPipedSrcDrkAvgPay', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('areaid', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'AreaID', blank=True)),
            ('areaname', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'Areaname')),
            ('paymthd', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'PayMthd')),
            ('areasmpdus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'AreaSmpDUs', blank=True)),
            ('dusinsmp', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'DUsInSmp', blank=True)),
            ('pcntdus', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'pcntDUs', blank=True)),
            ('dusinarea', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'DusInArea', blank=True)),
            ('smppersons', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'SmpPersons', blank=True)),
            ('totalppleinarea', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'TotalPpleinArea', blank=True)),
            ('pcntpple', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('totaldusinarea', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'TotalDUsInArea', blank=True)),
            ('avgpaydrk', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'AvgPayDrk', blank=True)),
        ))
        db.send_create_signal(u'majitables', ['Wpipedsrcdrkavgpay'])

        # Adding model 'Wpipedsrcdrktrt'
        db.create_table(u'WPipedSrcDrkTrt', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('areaid', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'AreaID', blank=True)),
            ('areaname', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'Areaname')),
            ('areasmpdus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'AreaSmpDUs', blank=True)),
            ('dusinsmp', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'DUsInSmp', blank=True)),
            ('pcntdus', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'pcntDUs', blank=True)),
            ('dusinarea', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'DusInArea', blank=True)),
            ('smppersons', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'SmpPersons', blank=True)),
            ('totalppleinarea', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'TotalPpleinArea', blank=True)),
            ('pcntpple', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('totaldusinarea', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'TotalDUsInArea', blank=True)),
        ))
        db.send_create_signal(u'majitables', ['Wpipedsrcdrktrt'])

        # Adding model 'WplotconmetDu'
        db.create_table(u'WPlotConMet-DU', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('areaid', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'AreaID', blank=True)),
            ('areaname', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'Areaname')),
            ('duconmetered', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'DUconmetered')),
            ('dusinsmp', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'DUsInSmp', blank=True)),
            ('pcntdus', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'pcntDUs', blank=True)),
            ('dusinarea', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'DUsInArea', blank=True)),
            ('smpduscon', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'SmpDUsCon', blank=True)),
        ))
        db.send_create_signal(u'majitables', ['WplotconmetDu'])

        # Adding model 'WplotconnectedDu'
        db.create_table(u'WPlotConnected-DU', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('areaid', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'AreaID', blank=True)),
            ('areaname', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'Areaname')),
            ('plotconnected', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'Plotconnected')),
            ('areasmpdus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'AreaSmpDUs', blank=True)),
            ('dusinsmp', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'DUsInSmp', blank=True)),
            ('pcntdus', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'pcntDUs', blank=True)),
            ('dusinarea', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'DusInArea', blank=True)),
            ('totaldusinarea', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'TotalDUsInArea', blank=True)),
        ))
        db.send_create_signal(u'majitables', ['WplotconnectedDu'])

        # Adding model 'Wrespercomtapcounty'
        db.create_table(u'WResPerComTapCounty', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('countyid', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'CountyID', blank=True)),
            ('countyname', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'CountyName')),
            ('totcomtaps', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'TotComTaps', blank=True)),
            ('pplepercomtap', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'PplePerComTap')),
            ('pop', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'Pop', blank=True)),
        ))
        db.send_create_signal(u'majitables', ['Wrespercomtapcounty'])

        # Adding model 'Wrespercomtapslum'
        db.create_table(u'WResPerComTapSlum', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('slumid', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'SlumID', blank=True)),
            ('slumname', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'SlumName')),
            ('totcomtaps', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'TotComTaps', blank=True)),
            ('pplepercomtap', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'PplePerComTap')),
            ('pop', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'Pop', blank=True)),
        ))
        db.send_create_signal(u'majitables', ['Wrespercomtapslum'])

        # Adding model 'Wrespercomtaptown'
        db.create_table(u'WResPerComTapTown', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('townid', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'TownID', blank=True)),
            ('townname', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'TownName')),
            ('totcomtaps', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'TotComTaps', blank=True)),
            ('pplepercomtap', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'PplePerComTap')),
            ('pop', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'Pop', blank=True)),
        ))
        db.send_create_signal(u'majitables', ['Wrespercomtaptown'])

        # Adding model 'Wrespercomtapwsp'
        db.create_table(u'WResPerComTapWSP', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('wspid', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'WSPID')),
            ('wspname', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'WSPName')),
            ('totcomtaps', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'TotComTaps', blank=True)),
            ('pplepercomtap', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'PplePerComTap')),
            ('pop', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'Pop', blank=True)),
        ))
        db.send_create_signal(u'majitables', ['Wrespercomtapwsp'])

        # Adding model 'Wresperpubcomkskscounty'
        db.create_table(u'WResPerPubComKsksCounty', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('countyid', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'CountyID', blank=True)),
            ('countyname', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'CountyName')),
            ('totpubcomksks', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'TotPubComKsks', blank=True)),
            ('ppleperpubcomtap', self.gf('django.db.models.fields.CharField')(max_length=36, db_column=u'PplePerPubComTap')),
            ('pop', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'Pop', blank=True)),
        ))
        db.send_create_signal(u'majitables', ['Wresperpubcomkskscounty'])

        # Adding model 'Wresperpubcomksksslum'
        db.create_table(u'WResPerPubComKsksSlum', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('slumid', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'SlumID', blank=True)),
            ('slumname', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'SlumName')),
            ('totpubcomksks', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'TotPubComKsks', blank=True)),
            ('ppleperpubcomtap', self.gf('django.db.models.fields.CharField')(max_length=36, db_column=u'PplePerPubComTap')),
            ('pop', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'Pop', blank=True)),
        ))
        db.send_create_signal(u'majitables', ['Wresperpubcomksksslum'])

        # Adding model 'Wresperpubcomkskstown'
        db.create_table(u'WResPerPubComKsksTown', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('townid', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'TownID', blank=True)),
            ('townname', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'TownName')),
            ('totpubcomksks', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'TotPubComKsks', blank=True)),
            ('ppleperpubcomtap', self.gf('django.db.models.fields.CharField')(max_length=36, db_column=u'PplePerPubComTap')),
            ('pop', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'Pop', blank=True)),
        ))
        db.send_create_signal(u'majitables', ['Wresperpubcomkskstown'])

        # Adding model 'Wresperpubcomkskswsp'
        db.create_table(u'WResPerPubComKsksWSP', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('wspid', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'WSPID')),
            ('wspname', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'WSPName')),
            ('totpubcomksks', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'TotPubComKsks', blank=True)),
            ('ppleperpubcomtap', self.gf('django.db.models.fields.CharField')(max_length=36, db_column=u'PplePerPubComTap')),
            ('pop', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'Pop', blank=True)),
        ))
        db.send_create_signal(u'majitables', ['Wresperpubcomkskswsp'])

        # Adding model 'Wresperpubwspcomtapscounty'
        db.create_table(u'WResPerPubWSPComTapsCounty', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('countyid', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'CountyID', blank=True)),
            ('countyname', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'CountyName')),
            ('totpubcomtaps', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'TotPubComTaps', blank=True)),
            ('ppleperpubcomtap', self.gf('django.db.models.fields.CharField')(max_length=34, db_column=u'PplePerPubComTap')),
            ('pop', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'Pop', blank=True)),
        ))
        db.send_create_signal(u'majitables', ['Wresperpubwspcomtapscounty'])

        # Adding model 'Wresperpubwspcomtapsslum'
        db.create_table(u'WResPerPubWSPComTapsSlum', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('slumid', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'SlumID', blank=True)),
            ('slumname', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'SlumName')),
            ('totpubcomtaps', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'TotPubComTaps', blank=True)),
            ('ppleperpubcomtap', self.gf('django.db.models.fields.CharField')(max_length=34, db_column=u'PplePerPubComTap')),
            ('pop', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'Pop', blank=True)),
        ))
        db.send_create_signal(u'majitables', ['Wresperpubwspcomtapsslum'])

        # Adding model 'Wresperpubwspcomtapstown'
        db.create_table(u'WResPerPubWSPComTapsTown', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('townid', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'TownID', blank=True)),
            ('townname', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'TownName')),
            ('totpubcomtaps', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'TotPubComTaps', blank=True)),
            ('ppleperpubcomtap', self.gf('django.db.models.fields.CharField')(max_length=34, db_column=u'PplePerPubComTap')),
            ('pop', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'Pop', blank=True)),
        ))
        db.send_create_signal(u'majitables', ['Wresperpubwspcomtapstown'])

        # Adding model 'Wresperpubwspcomtapswsp'
        db.create_table(u'WResPerPubWSPComTapsWSP', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('wspid', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'WSPID')),
            ('wspname', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'WSPName')),
            ('totpubcomtaps', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'TotPubComTaps', blank=True)),
            ('ppleperpubcomtap', self.gf('django.db.models.fields.CharField')(max_length=34, db_column=u'PplePerPubComTap')),
            ('pop', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'Pop', blank=True)),
        ))
        db.send_create_signal(u'majitables', ['Wresperpubwspcomtapswsp'])

        # Adding model 'Wresperpubwsptapcounty'
        db.create_table(u'WResPerPubWSPTapCounty', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('countyid', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'CountyID', blank=True)),
            ('countyname', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'CountyName')),
            ('tottaps', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'TotTaps', blank=True)),
            ('ppleperpubtap', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'PplePerPubTap')),
            ('pop', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'Pop', blank=True)),
        ))
        db.send_create_signal(u'majitables', ['Wresperpubwsptapcounty'])

        # Adding model 'Wresperpubwsptapslum'
        db.create_table(u'WResPerPubWSPTapSlum', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('slumid', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'SlumID', blank=True)),
            ('slumname', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'SlumName')),
            ('tottaps', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'TotTaps', blank=True)),
            ('ppleperpubtap', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'PplePerPubTap')),
            ('pop', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'Pop', blank=True)),
        ))
        db.send_create_signal(u'majitables', ['Wresperpubwsptapslum'])

        # Adding model 'Wresperpubwsptaptown'
        db.create_table(u'WResPerPubWSPTapTown', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('townid', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'TownID', blank=True)),
            ('townname', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'TownName')),
            ('tottaps', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'TotTaps', blank=True)),
            ('ppleperpubtap', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'PplePerPubTap')),
            ('pop', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'Pop', blank=True)),
        ))
        db.send_create_signal(u'majitables', ['Wresperpubwsptaptown'])

        # Adding model 'Wresperpubwsptapwsp'
        db.create_table(u'WResPerPubWSPTapWSP', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('wspid', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'WSPID')),
            ('wspname', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'WSPName')),
            ('tottaps', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'TotTaps', blank=True)),
            ('ppleperpubtap', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'PplePerPubTap')),
            ('pop', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'Pop', blank=True)),
        ))
        db.send_create_signal(u'majitables', ['Wresperpubwsptapwsp'])

        # Adding model 'Wresperwspkskcounty'
        db.create_table(u'WResPerWSPKskCounty', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('countyid', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'CountyID', blank=True)),
            ('countyname', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'CountyName')),
            ('totksks', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'TotKsks', blank=True)),
            ('ppleperkiosk', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'PplePerKiosk')),
            ('pop', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'Pop', blank=True)),
        ))
        db.send_create_signal(u'majitables', ['Wresperwspkskcounty'])

        # Adding model 'Wresperwspkskslum'
        db.create_table(u'WResPerWSPKskSlum', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('slumid', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'SlumID', blank=True)),
            ('slumname', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'SlumName')),
            ('totksks', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'TotKsks', blank=True)),
            ('ppleperkiosk', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'PplePerKiosk')),
            ('pop', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'Pop', blank=True)),
        ))
        db.send_create_signal(u'majitables', ['Wresperwspkskslum'])

        # Adding model 'Wresperwspksktown'
        db.create_table(u'WResPerWSPKskTown', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('townid', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'TownID', blank=True)),
            ('townname', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'TownName')),
            ('totksks', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'TotKsks', blank=True)),
            ('ppleperkiosk', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'PplePerKiosk')),
            ('pop', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'Pop', blank=True)),
        ))
        db.send_create_signal(u'majitables', ['Wresperwspksktown'])

        # Adding model 'Wresperwspkskwsp'
        db.create_table(u'WResPerWSPKskWSP', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('wspid', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'WSPID')),
            ('wspname', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'WSPName')),
            ('totksks', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'TotKsks', blank=True)),
            ('ppleperkiosk', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'PplePerKiosk')),
            ('pop', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'Pop', blank=True)),
        ))
        db.send_create_signal(u'majitables', ['Wresperwspkskwsp'])

        # Adding model 'Wrespercompubpost10D'
        db.create_table(u'WResperComPubPost-10d', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('area', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'Area', blank=True)),
            ('areaname', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'Areaname')),
            ('areapop', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'AreaPop', blank=True)),
            ('nfacilities', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'NFacilities', blank=True)),
            ('ppleperfacility', self.gf('django.db.models.fields.CharField')(max_length=33, db_column=u'PplePerFacility')),
        ))
        db.send_create_signal(u'majitables', ['Wrespercompubpost10D'])

        # Adding model 'Wsrcbathpipedcounty'
        db.create_table(u'WSrcBathPipedCounty', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('countyid', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'CountyID', blank=True)),
            ('countyname', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'CountyName')),
            ('dusinsmp', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'DUsInSmp', blank=True)),
            ('smpdus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'SmpDUs', blank=True)),
            ('pcntdus', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'pcntDUs', blank=True)),
            ('dusinarea', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'DusInArea', blank=True)),
            ('totdus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'TotDUs', blank=True)),
            ('totalppleinarea', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'TotalPpleinArea', blank=True)),
            ('pcntpop', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'PcntPop', blank=True)),
            ('pop', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'Pop', blank=True)),
        ))
        db.send_create_signal(u'majitables', ['Wsrcbathpipedcounty'])

        # Adding model 'Wsrcbathpipedslum'
        db.create_table(u'WSrcBathPipedSlum', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('slumid', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'SlumID', blank=True)),
            ('slumname', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'SlumName')),
            ('dusinsmp', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'DUsInSmp', blank=True)),
            ('smpdus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'SmpDUs', blank=True)),
            ('pcntdus', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'pcntDUs', blank=True)),
            ('dusinarea', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'DusInArea', blank=True)),
            ('totdus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'TotDUs', blank=True)),
            ('totalppleinarea', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'TotalPpleinArea', blank=True)),
            ('pcntpop', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'PcntPop', blank=True)),
            ('pop', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'Pop', blank=True)),
        ))
        db.send_create_signal(u'majitables', ['Wsrcbathpipedslum'])

        # Adding model 'Wsrcbathpipedtown'
        db.create_table(u'WSrcBathPipedTown', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('townid', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'TownID', blank=True)),
            ('townname', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'TownName')),
            ('dusinsmp', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'DUsInSmp', blank=True)),
            ('smpdus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'SmpDUs', blank=True)),
            ('pcntdus', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'pcntDUs', blank=True)),
            ('dusinarea', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'DusInArea', blank=True)),
            ('totdus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'TotDUs', blank=True)),
            ('totalppleinarea', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'TotalPpleinArea', blank=True)),
            ('pcntpop', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'PcntPop', blank=True)),
            ('pop', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'Pop', blank=True)),
        ))
        db.send_create_signal(u'majitables', ['Wsrcbathpipedtown'])

        # Adding model 'Wsrcbathpipedwsp'
        db.create_table(u'WSrcBathPipedWSP', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('wspid', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'WspID')),
            ('wspname', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'WspName')),
            ('dusinsmp', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'DUsInSmp', blank=True)),
            ('smpdus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'SmpDUs', blank=True)),
            ('pcntdus', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'pcntDUs', blank=True)),
            ('dusinarea', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'DusInArea', blank=True)),
            ('totdus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'TotDUs', blank=True)),
            ('totalppleinarea', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'TotalPpleinArea', blank=True)),
            ('pcntpop', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'PcntPop', blank=True)),
            ('pop', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'Pop', blank=True)),
        ))
        db.send_create_signal(u'majitables', ['Wsrcbathpipedwsp'])

        # Adding model 'Wsrcckg33County'
        db.create_table(u'WSrcCkg33County', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('countyid', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'CountyID', blank=True)),
            ('countyname', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'CountyName')),
            ('ckgwatersrc', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'CkgWaterSrc')),
            ('smpsrc', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'SmpSrc', blank=True)),
            ('smpdus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'SmpDUs', blank=True)),
            ('totdus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'TotDUs', blank=True)),
            ('pcntusingsrc', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'PcntUsingSrc', blank=True)),
            ('nusingsrc', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'NUsingSrc', blank=True)),
        ))
        db.send_create_signal(u'majitables', ['Wsrcckg33County'])

        # Adding model 'Wsrcdrkbhpmpcounty'
        db.create_table(u'WSrcDrkBhPmpCounty', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('countyid', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'CountyID', blank=True)),
            ('countyname', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'CountyName')),
            ('dusinsmp', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'DUsInSmp', blank=True)),
            ('smpdus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'SmpDUs', blank=True)),
            ('pcntdus', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'pcntDUs', blank=True)),
            ('dusinarea', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'DusInArea', blank=True)),
            ('totdus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'TotDUs', blank=True)),
            ('totalppleinarea', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'TotalPpleinArea', blank=True)),
            ('pcntpop', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'PcntPop', blank=True)),
            ('pop', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'Pop', blank=True)),
        ))
        db.send_create_signal(u'majitables', ['Wsrcdrkbhpmpcounty'])

        # Adding model 'Wsrcdrkbhpmpslum'
        db.create_table(u'WSrcDrkBhPmpSlum', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('slumid', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'SlumID', blank=True)),
            ('slumname', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'SlumName')),
            ('dusinsmp', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'DUsInSmp', blank=True)),
            ('smpdus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'SmpDUs', blank=True)),
            ('pcntdus', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'pcntDUs', blank=True)),
            ('dusinarea', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'DusInArea', blank=True)),
            ('totdus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'TotDUs', blank=True)),
            ('totalppleinarea', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'TotalPpleinArea', blank=True)),
            ('pcntpop', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'PcntPop', blank=True)),
            ('pop', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'Pop', blank=True)),
        ))
        db.send_create_signal(u'majitables', ['Wsrcdrkbhpmpslum'])

        # Adding model 'Wsrcdrkbhpmptown'
        db.create_table(u'WSrcDrkBhPmpTown', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('townid', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'TownID', blank=True)),
            ('townname', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'TownName')),
            ('dusinsmp', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'DUsInSmp', blank=True)),
            ('smpdus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'SmpDUs', blank=True)),
            ('pcntdus', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'pcntDUs', blank=True)),
            ('dusinarea', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'DusInArea', blank=True)),
            ('totdus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'TotDUs', blank=True)),
            ('totalppleinarea', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'TotalPpleinArea', blank=True)),
            ('pcntpop', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'PcntPop', blank=True)),
            ('pop', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'Pop', blank=True)),
        ))
        db.send_create_signal(u'majitables', ['Wsrcdrkbhpmptown'])

        # Adding model 'Wsrcdrkbhpmpwsp'
        db.create_table(u'WSrcDrkBhPmpWSP', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('wspid', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'WspID')),
            ('wspname', self.gf('django.db.models.fields.CharField')(max_length=45, db_column=u'WspName')),
            ('dusinsmp', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'DUsInSmp', blank=True)),
            ('smpdus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'SmpDUs', blank=True)),
            ('pcntdus', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'pcntDUs', blank=True)),
            ('dusinarea', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'DusInArea', blank=True)),
            ('totdus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'TotDUs', blank=True)),
            ('totalppleinarea', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'TotalPpleinArea', blank=True)),
            ('pcntpop', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'PcntPop', blank=True)),
            ('pop', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'Pop', blank=True)),
        ))
        db.send_create_signal(u'majitables', ['Wsrcdrkbhpmpwsp'])

        # Adding model 'Wsrcdrkksk'
        db.create_table(u'WSrcDrkKsk', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('areaid', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'AreaID', blank=True)),
            ('areaname', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'Areaname')),
            ('areasmpdus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'AreaSmpDUs', blank=True)),
            ('dusinsmp', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'DUsInSmp', blank=True)),
            ('pcntdus', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'pcntDUs', blank=True)),
            ('dusinarea', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'DusInArea', blank=True)),
            ('smppersons', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'SmpPersons', blank=True)),
            ('totalppleinarea', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'TotalPpleinArea', blank=True)),
            ('pcntpple', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('totaldusinarea', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'TotalDUsInArea', blank=True)),
        ))
        db.send_create_signal(u'majitables', ['Wsrcdrkksk'])

        # Adding model 'Wsrcdrkleakcounty'
        db.create_table(u'WSrcDrkLeakCounty', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('countyid', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'CountyID')),
            ('countyname', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'CountyName')),
            ('dusinsmp', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'DUsInSmp')),
            ('smpdus', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'SmpDUs')),
            ('pcntdus', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'pcntDUs')),
            ('dusinarea', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'DusInArea')),
            ('totdus', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'TotDUs')),
            ('totalppleinarea', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'TotalPpleinArea')),
            ('pcntpop', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'PcntPop')),
            ('pop', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'Pop')),
        ))
        db.send_create_signal(u'majitables', ['Wsrcdrkleakcounty'])

        # Adding model 'Wsrcdrkleakslum'
        db.create_table(u'WSrcDrkLeakSlum', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('slumid', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'SlumID')),
            ('slumname', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'SlumName')),
            ('dusinsmp', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'DUsInSmp')),
            ('smpdus', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'SmpDUs')),
            ('pcntdus', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'pcntDUs')),
            ('dusinarea', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'DusInArea')),
            ('totdus', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'TotDUs')),
            ('totalppleinarea', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'TotalPpleinArea')),
            ('pcntpop', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'PcntPop')),
            ('pop', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'Pop')),
        ))
        db.send_create_signal(u'majitables', ['Wsrcdrkleakslum'])

        # Adding model 'Wsrcdrkleaktown'
        db.create_table(u'WSrcDrkLeakTown', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('townid', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'TownID')),
            ('townname', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'TownName')),
            ('dusinsmp', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'DUsInSmp')),
            ('smpdus', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'SmpDUs')),
            ('pcntdus', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'pcntDUs')),
            ('dusinarea', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'DusInArea')),
            ('totdus', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'TotDUs')),
            ('totalppleinarea', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'TotalPpleinArea')),
            ('pcntpop', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'PcntPop')),
            ('pop', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'Pop')),
        ))
        db.send_create_signal(u'majitables', ['Wsrcdrkleaktown'])

        # Adding model 'Wsrcdrkleakwsp'
        db.create_table(u'WSrcDrkLeakWSP', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('wspid', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'WSPID')),
            ('wspname', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'WSPName')),
            ('dusinsmp', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'DUsInSmp')),
            ('smpdus', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'SmpDUs')),
            ('pcntdus', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'pcntDUs')),
            ('dusinarea', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'DusInArea')),
            ('totdus', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'TotDUs')),
            ('totalppleinarea', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'TotalPpleinArea')),
            ('pcntpop', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'PcntPop')),
            ('pop', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'Pop')),
        ))
        db.send_create_signal(u'majitables', ['Wsrcdrkleakwsp'])

        # Adding model 'Wsrcdrkspringcounty'
        db.create_table(u'WSrcDrkSpringCounty', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('countyid', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'CountyID', blank=True)),
            ('countyname', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'CountyName')),
            ('dusinsmp', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'DUsInSmp', blank=True)),
            ('smpdus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'SmpDUs', blank=True)),
            ('pcntdus', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'pcntDUs', blank=True)),
            ('dusinarea', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'DusInArea', blank=True)),
            ('totdus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'TotDUs', blank=True)),
            ('totalppleinarea', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'TotalPpleinArea', blank=True)),
            ('pcntpop', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'PcntPop', blank=True)),
            ('pop', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'Pop', blank=True)),
        ))
        db.send_create_signal(u'majitables', ['Wsrcdrkspringcounty'])

        # Adding model 'Wsrcdrkspringslum'
        db.create_table(u'WSrcDrkSpringSlum', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('slumid', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'SlumID', blank=True)),
            ('slumname', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'SlumName')),
            ('dusinsmp', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'DUsInSmp', blank=True)),
            ('smpdus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'SmpDUs', blank=True)),
            ('pcntdus', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'pcntDUs', blank=True)),
            ('dusinarea', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'DusInArea', blank=True)),
            ('totdus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'TotDUs', blank=True)),
            ('totalppleinarea', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'TotalPpleinArea', blank=True)),
            ('pcntpop', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'PcntPop', blank=True)),
            ('pop', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'Pop', blank=True)),
        ))
        db.send_create_signal(u'majitables', ['Wsrcdrkspringslum'])

        # Adding model 'Wsrcdrkspringtown'
        db.create_table(u'WSrcDrkSpringTown', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('townid', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'TownID', blank=True)),
            ('townname', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'TownName')),
            ('dusinsmp', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'DUsInSmp', blank=True)),
            ('smpdus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'SmpDUs', blank=True)),
            ('pcntdus', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'pcntDUs', blank=True)),
            ('dusinarea', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'DusInArea', blank=True)),
            ('totdus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'TotDUs', blank=True)),
            ('totalppleinarea', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'TotalPpleinArea', blank=True)),
            ('pcntpop', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'PcntPop', blank=True)),
            ('pop', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'Pop', blank=True)),
        ))
        db.send_create_signal(u'majitables', ['Wsrcdrkspringtown'])

        # Adding model 'Wsrcdrkspringwsp'
        db.create_table(u'WSrcDrkSpringWSP', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('wspid', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'WSPID')),
            ('wspname', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'WSPName')),
            ('dusinsmp', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'DUsInSmp', blank=True)),
            ('smpdus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'SmpDUs', blank=True)),
            ('pcntdus', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'pcntDUs', blank=True)),
            ('dusinarea', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'DusInArea', blank=True)),
            ('totdus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'TotDUs', blank=True)),
            ('totalppleinarea', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'TotalPpleinArea', blank=True)),
            ('pcntpop', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'PcntPop', blank=True)),
            ('pop', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'Pop', blank=True)),
        ))
        db.send_create_signal(u'majitables', ['Wsrcdrkspringwsp'])

        # Adding model 'Wsrcdrkvendorcounty'
        db.create_table(u'WSrcDrkVendorCounty', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('countyid', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'CountyID', blank=True)),
            ('countyname', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'CountyName')),
            ('dusinsmp', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'DUsInSmp', blank=True)),
            ('smpdus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'SmpDUs', blank=True)),
            ('pcntdus', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'pcntDUs', blank=True)),
            ('dusinarea', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'DusInArea', blank=True)),
            ('totdus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'TotDUs', blank=True)),
            ('totalppleinarea', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'TotalPpleinArea', blank=True)),
            ('pcntpop', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'PcntPop', blank=True)),
            ('pop', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'Pop', blank=True)),
        ))
        db.send_create_signal(u'majitables', ['Wsrcdrkvendorcounty'])

        # Adding model 'Wsrcdrkvendorslum'
        db.create_table(u'WSrcDrkVendorSlum', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('slumid', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'SlumID', blank=True)),
            ('slumname', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'SlumName')),
            ('dusinsmp', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'DUsInSmp', blank=True)),
            ('smpdus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'SmpDUs', blank=True)),
            ('pcntdus', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'pcntDUs', blank=True)),
            ('dusinarea', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'DusInArea', blank=True)),
            ('totdus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'TotDUs', blank=True)),
            ('totalppleinarea', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'TotalPpleinArea', blank=True)),
            ('pcntpop', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'PcntPop', blank=True)),
            ('pop', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'Pop', blank=True)),
        ))
        db.send_create_signal(u'majitables', ['Wsrcdrkvendorslum'])

        # Adding model 'Wsrcdrkvendortown'
        db.create_table(u'WSrcDrkVendorTown', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('townid', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'TownID', blank=True)),
            ('townname', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'TownName')),
            ('dusinsmp', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'DUsInSmp', blank=True)),
            ('smpdus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'SmpDUs', blank=True)),
            ('pcntdus', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'pcntDUs', blank=True)),
            ('dusinarea', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'DusInArea', blank=True)),
            ('totdus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'TotDUs', blank=True)),
            ('totalppleinarea', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'TotalPpleinArea', blank=True)),
            ('pcntpop', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'PcntPop', blank=True)),
            ('pop', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'Pop', blank=True)),
        ))
        db.send_create_signal(u'majitables', ['Wsrcdrkvendortown'])

        # Adding model 'Wsrcdrkvendorwsp'
        db.create_table(u'WSrcDrkVendorWSP', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('wspid', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'WSPID')),
            ('wspname', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'WSPName')),
            ('dusinsmp', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'DUsInSmp', blank=True)),
            ('smpdus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'SmpDUs', blank=True)),
            ('pcntdus', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'pcntDUs', blank=True)),
            ('dusinarea', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'DusInArea', blank=True)),
            ('totdus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'TotDUs', blank=True)),
            ('totalppleinarea', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'TotalPpleinArea', blank=True)),
            ('pcntpop', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'PcntPop', blank=True)),
            ('pop', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'Pop', blank=True)),
        ))
        db.send_create_signal(u'majitables', ['Wsrcdrkvendorwsp'])

        # Adding model 'Wsrcdrkwellscounty'
        db.create_table(u'WSrcDrkWellsCounty', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('countyid', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'CountyID', blank=True)),
            ('countyname', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'CountyName')),
            ('dusinsmp', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'DUsInSmp', blank=True)),
            ('smpdus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'SmpDUs', blank=True)),
            ('pcntdus', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'pcntDUs', blank=True)),
            ('dusinarea', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'DusInArea', blank=True)),
            ('totdus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'TotDUs', blank=True)),
            ('totalppleinarea', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'TotalPpleinArea', blank=True)),
            ('pcntpop', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'PcntPop', blank=True)),
            ('pop', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'Pop', blank=True)),
        ))
        db.send_create_signal(u'majitables', ['Wsrcdrkwellscounty'])

        # Adding model 'Wsrcdrkwellsslum'
        db.create_table(u'WSrcDrkWellsSlum', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('slumid', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'SlumID', blank=True)),
            ('slumname', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'SlumName')),
            ('dusinsmp', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'DUsInSmp', blank=True)),
            ('smpdus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'SmpDUs', blank=True)),
            ('pcntdus', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'pcntDUs', blank=True)),
            ('dusinarea', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'DusInArea', blank=True)),
            ('totdus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'TotDUs', blank=True)),
            ('totalppleinarea', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'TotalPpleinArea', blank=True)),
            ('pcntpop', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'PcntPop', blank=True)),
            ('pop', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'Pop', blank=True)),
        ))
        db.send_create_signal(u'majitables', ['Wsrcdrkwellsslum'])

        # Adding model 'Wsrcdrkwellstown'
        db.create_table(u'WSrcDrkWellsTown', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('townid', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'TownID', blank=True)),
            ('townname', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'TownName')),
            ('dusinsmp', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'DUsInSmp', blank=True)),
            ('smpdus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'SmpDUs', blank=True)),
            ('pcntdus', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'pcntDUs', blank=True)),
            ('dusinarea', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'DusInArea', blank=True)),
            ('totdus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'TotDUs', blank=True)),
            ('totalppleinarea', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'TotalPpleinArea', blank=True)),
            ('pcntpop', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'PcntPop', blank=True)),
            ('pop', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'Pop', blank=True)),
        ))
        db.send_create_signal(u'majitables', ['Wsrcdrkwellstown'])

        # Adding model 'Wsrcdrkwellswsp'
        db.create_table(u'WSrcDrkWellsWSP', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('wspid', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'WSPID')),
            ('wspname', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'WSPName')),
            ('dusinsmp', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'DUsInSmp', blank=True)),
            ('smpdus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'SmpDUs', blank=True)),
            ('pcntdus', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'pcntDUs', blank=True)),
            ('dusinarea', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'DusInArea', blank=True)),
            ('totdus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'TotDUs', blank=True)),
            ('totalppleinarea', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'TotalPpleinArea', blank=True)),
            ('pcntpop', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'PcntPop', blank=True)),
            ('pop', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'Pop', blank=True)),
        ))
        db.send_create_signal(u'majitables', ['Wsrcdrkwellswsp'])

        # Adding model 'Wsupsituation8'
        db.create_table(u'WSupSituation-8', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('areaid', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'AreaID', blank=True)),
            ('arealinkedwater', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'AreaLinkedwater')),
            ('techstat', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'TechStat')),
            ('wnwdist', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'WnwDist')),
            ('mainwatersrc', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'MainWaterSrc')),
            ('maindrkgwatersrc', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'MainDrkgWaterSrc')),
            ('mainwaterprob', self.gf('django.db.models.fields.TextField')(db_column=u'MainWaterProb')),
        ))
        db.send_create_signal(u'majitables', ['Wsupsituation8'])

        # Adding model 'Wsupsituation28'
        db.create_table(u'WSupSituation2-8', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('areaid', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'AreaID', blank=True)),
            ('areaname', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'Areaname')),
            ('protectedsrc', self.gf('django.db.models.fields.TextField')(db_column=u'ProtectedSrc')),
            ('unprotectedsrc', self.gf('django.db.models.fields.TextField')(db_column=u'UnProtectedSrc')),
        ))
        db.send_create_signal(u'majitables', ['Wsupsituation28'])

        # Adding model 'Wsupsituation38D'
        db.create_table(u'WSupSituation3-8d', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('areaid', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'AreaID', blank=True)),
            ('illegalcon', self.gf('django.db.models.fields.TextField')(db_column=u'IllegalCon', blank=True)),
            ('supply24hr', self.gf('django.db.models.fields.TextField')(db_column=u'Supply24hr', blank=True)),
            ('supplyinfo', self.gf('django.db.models.fields.TextField')(db_column=u'SupplyInfo', blank=True)),
            ('waterrationing', self.gf('django.db.models.fields.TextField')(db_column=u'Waterrationing', blank=True)),
            ('wdyspwk', self.gf('django.db.models.fields.TextField')(db_column=u'Wdyspwk', blank=True)),
            ('rationrem', self.gf('django.db.models.fields.TextField')(db_column=u'RationRem', blank=True)),
            ('waterpressure', self.gf('django.db.models.fields.TextField')(db_column=u'WaterPressure', blank=True)),
            ('waterqlty', self.gf('django.db.models.fields.TextField')(db_column=u'WaterQlty', blank=True)),
            ('wwsptariffpunit', self.gf('django.db.models.fields.TextField')(db_column=u'Wwsptariffpunit', blank=True)),
            ('wwsptariffp20l', self.gf('django.db.models.fields.TextField')(db_column=u'Wwsptariffp20l', blank=True)),
            ('wwsptariffpmnth', self.gf('django.db.models.fields.TextField')(db_column=u'Wwsptariffpmnth', blank=True)),
            ('tariffrem', self.gf('django.db.models.fields.TextField')(db_column=u'TariffRem', blank=True)),
            ('wsptariffapprvd', self.gf('django.db.models.fields.TextField')(db_column=u'WSPTariffapprvd', blank=True)),
        ))
        db.send_create_signal(u'majitables', ['Wsupsituation38D'])

        # Adding model 'Wsupsituationdu'
        db.create_table(u'WSupSituationDU', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('areaid', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'AreaID', blank=True)),
            ('areaname', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'Areaname')),
            ('wsituation', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'Wsituation')),
            ('areasmpdus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'AreaSmpDUs', blank=True)),
            ('nousingsrc', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'Nousingsrc', blank=True)),
            ('pcntdus', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'pcntDUs', blank=True)),
            ('ndus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'NDus', blank=True)),
            ('persons', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('pcntpple', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('numdu', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'NumDU', blank=True)),
        ))
        db.send_create_signal(u'majitables', ['Wsupsituationdu'])

        # Adding model 'Wsupplyinf8E'
        db.create_table(u'WSupplyInf-8e', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('areaid', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'AreaID', blank=True)),
            ('waterresellers', self.gf('django.db.models.fields.TextField')(db_column=u'Waterresellers', blank=True)),
            ('communityschm', self.gf('django.db.models.fields.TextField')(db_column=u'Communityschm', blank=True)),
            ('ngoscheme', self.gf('django.db.models.fields.TextField')(db_column=u'NGOscheme', blank=True)),
            ('infwaterqlty', self.gf('django.db.models.fields.TextField')(db_column=u'InfWaterqlty', blank=True)),
            ('winftariffp20l1', self.gf('django.db.models.fields.TextField')(db_column=u'Winftariffp20l1', blank=True)),
            ('winftariffp20l2', self.gf('django.db.models.fields.TextField')(db_column=u'Winftariffp20l2', blank=True)),
            ('winftariffp20l3', self.gf('django.db.models.fields.TextField')(db_column=u'Winftariffp20l3', blank=True)),
            ('tariffrem', self.gf('django.db.models.fields.TextField')(db_column=u'TariffRem', blank=True)),
            ('wsupplyproj', self.gf('django.db.models.fields.TextField')(db_column=u'Wsupplyproj')),
        ))
        db.send_create_signal(u'majitables', ['Wsupplyinf8E'])

        # Adding model 'Wunreliablesrcbath'
        db.create_table(u'WUnreliableSrcBath', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('areaid', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'AreaID', blank=True)),
            ('areaname', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'Areaname')),
            ('areasmpdus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'AreaSmpDUs', blank=True)),
            ('dusinsmp', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'DUsInSmp', blank=True)),
            ('pcntdus', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'pcntDUs', blank=True)),
            ('dusinarea', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'DusInArea', blank=True)),
            ('smppersons', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'SmpPersons', blank=True)),
            ('totalppleinarea', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'TotalPpleinArea', blank=True)),
            ('pcntpple', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('totaldusinarea', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'TotalDUsInArea', blank=True)),
            ('areasmppop', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'AreaSmpPop', blank=True)),
        ))
        db.send_create_signal(u'majitables', ['Wunreliablesrcbath'])

        # Adding model 'Wunreliablesrcdrk'
        db.create_table(u'WUnreliableSrcDrk', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('areaid', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'AreaID', blank=True)),
            ('areaname', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'Areaname')),
            ('areasmpdus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'AreaSmpDUs', blank=True)),
            ('dusinsmp', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'DUsInSmp', blank=True)),
            ('pcntdus', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'pcntDUs', blank=True)),
            ('dusinarea', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'DusInArea', blank=True)),
            ('smppersons', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'SmpPersons', blank=True)),
            ('totalppleinarea', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'TotalPpleinArea', blank=True)),
            ('pcntpple', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('totaldusinarea', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'TotalDUsInArea', blank=True)),
            ('areasmppop', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'AreaSmpPop', blank=True)),
        ))
        db.send_create_signal(u'majitables', ['Wunreliablesrcdrk'])

        # Adding model 'Wunreliablesrcdrkavgpay'
        db.create_table(u'WUnreliableSrcDrkAvgPay', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('areaid', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'AreaID', blank=True)),
            ('areaname', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'Areaname')),
            ('paymthd', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'PayMthd')),
            ('areasmpdus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'AreaSmpDUs', blank=True)),
            ('dusinsmp', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'DUsInSmp', blank=True)),
            ('pcntdus', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'pcntDUs', blank=True)),
            ('dusinarea', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'DusInArea', blank=True)),
            ('smppersons', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'SmpPersons', blank=True)),
            ('totalppleinarea', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'TotalPpleinArea', blank=True)),
            ('pcntpple', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('totaldusinarea', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'TotalDUsInArea', blank=True)),
            ('avgpaydrk', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'AvgPayDrk', blank=True)),
        ))
        db.send_create_signal(u'majitables', ['Wunreliablesrcdrkavgpay'])

        # Adding model 'Wunreliablesrcdrktrt'
        db.create_table(u'WUnreliableSrcDrkTrt', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('areaid', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'AreaID', blank=True)),
            ('areaname', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'Areaname')),
            ('areasmpdus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'AreaSmpDUs', blank=True)),
            ('dusinsmp', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'DUsInSmp', blank=True)),
            ('pcntdus', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'pcntDUs', blank=True)),
            ('dusinarea', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'DusInArea', blank=True)),
            ('smppersons', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'SmpPersons', blank=True)),
            ('totalppleinarea', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'TotalPpleinArea', blank=True)),
            ('pcntpple', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('totaldusinarea', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'TotalDUsInArea', blank=True)),
        ))
        db.send_create_signal(u'majitables', ['Wunreliablesrcdrktrt'])

        # Adding model 'Wusersperindcon10D'
        db.create_table(u'WUsersPerIndCon-10d', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('area', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'Area', blank=True)),
            ('areaname', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'Areaname')),
            ('areapop', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'AreaPop', blank=True)),
            ('noofsmpcons', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'NoofSmpCons', blank=True)),
            ('smppersons', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'SmpPersons', blank=True)),
            ('totalppleinarea', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'TotalPpleinArea', blank=True)),
            ('noofconsinarea', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'NoofConsinArea', blank=True)),
            ('userspercon', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'UsersPercon', blank=True)),
        ))
        db.send_create_signal(u'majitables', ['Wusersperindcon10D'])

        # Adding model 'Wusersperksk'
        db.create_table(u'WUsersPerKsk', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('areaid', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'AreaID', blank=True)),
            ('areaname', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'Areaname')),
            ('areapop', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'AreaPop', blank=True)),
            ('totalppleinarea', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'TotalPpleinArea', blank=True)),
            ('pubwaterksks', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'PubWaterKsks', blank=True)),
            ('usersperksk', self.gf('django.db.models.fields.CharField')(max_length=24, db_column=u'UsersPerKsk')),
        ))
        db.send_create_signal(u'majitables', ['Wusersperksk'])

        # Adding model 'Wusersperpubtap10D'
        db.create_table(u'WUsersPerPubTap-10d', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('areaid', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'AreaID', blank=True)),
            ('areaname', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'Areaname')),
            ('nusers', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'NUsers')),
            ('ntaps', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'NTaps', blank=True)),
            ('usersperpubtap', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'UsersPerPubTap')),
        ))
        db.send_create_signal(u'majitables', ['Wusersperpubtap10D'])

        # Adding model 'Wateroutlets'
        db.create_table(u'WaterOutlets', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('areaid', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'AreaID', blank=True)),
            ('areaname', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'AreaName', blank=True)),
            ('pubwsptaps', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'PubWSPTaps', blank=True)),
            ('comtaps', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'ComTaps', blank=True)),
            ('privtaps', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'PrivTaps', blank=True)),
            ('pubwaterksks', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'PubWaterKsks', blank=True)),
            ('comwaterksks', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'ComWaterKsks', blank=True)),
            ('privwaterksks', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'PrivWaterKsks', blank=True)),
        ))
        db.send_create_signal(u'majitables', ['Wateroutlets'])

        # Adding model 'Waterpaiddu'
        db.create_table(u'WaterPaidDU', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('areaid', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'AreaID', blank=True)),
            ('areaname', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'Areaname')),
            ('waterpaid', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'WaterPaid')),
            ('areasmpdus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'AreaSmpDUs', blank=True)),
            ('dusinsmp', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'DUsInSmp', blank=True)),
            ('pcntdus', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'pcntDUs', blank=True)),
            ('dusinarea', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'DusInArea', blank=True)),
            ('totaldusinarea', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'TotalDUsInArea', blank=True)),
        ))
        db.send_create_signal(u'majitables', ['Waterpaiddu'])

        # Adding model 'Waterpaymthddu'
        db.create_table(u'WaterPayMthdDU', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('areaid', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'AreaID', blank=True)),
            ('areaname', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'Areaname')),
            ('wpaymthd', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'WPayMthd')),
            ('dus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'DUs', blank=True)),
            ('dusinsmp', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'DUsInSmp', blank=True)),
            ('pcntdus', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'pcntDUs', blank=True)),
            ('dusinarea', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'DUsInArea', blank=True)),
            ('totaldusinarea', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'TotalDUsInArea', blank=True)),
            ('wpaid', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'Wpaid')),
        ))
        db.send_create_signal(u'majitables', ['Waterpaymthddu'])

        # Adding model 'Waterqlty9'
        db.create_table(u'WaterQlty-9', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('areaid', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'AreaID', blank=True)),
            ('areaname', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'Areaname')),
            ('waterqlty', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'WaterQlty')),
            ('areasmpdus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'AreaSmpDUs', blank=True)),
            ('smpusingsrc', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'Smpusingsrc', blank=True)),
            ('pcntplotsusingsrc', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('ndus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'NDus', blank=True)),
            ('persons', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('pcntppleusingsrc', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('numdu', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'numDU', blank=True)),
        ))
        db.send_create_signal(u'majitables', ['Waterqlty9'])

        # Adding model 'Watersrcbath9'
        db.create_table(u'WaterSrcBath-9', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('areaid', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'AreaID', blank=True)),
            ('areaname', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'Areaname')),
            ('watersrcbath', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'WaterSrcBath')),
            ('areasmpdus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'AreaSmpDUs', blank=True)),
            ('smpusingsrc', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'Smpusingsrc', blank=True)),
            ('pcntplotsusingsrc', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('ndus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'NDus', blank=True)),
            ('persons', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('pcntppleusingsrc', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('numdu', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'NumDU', blank=True)),
        ))
        db.send_create_signal(u'majitables', ['Watersrcbath9'])

        # Adding model 'Watersrcckg9'
        db.create_table(u'WaterSrcCkg-9', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('areaid', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'AreaID', blank=True)),
            ('areaname', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'Areaname')),
            ('ckgwatersrc', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'CkgWaterSrc')),
            ('areasmpdus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'AreaSmpDUs', blank=True)),
            ('nousingsrc', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'Nousingsrc', blank=True)),
            ('pcntplotsusingsrc', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('ndus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'NDus', blank=True)),
            ('persons', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('pcntppleusingsrc', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('numdu', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'NumDU', blank=True)),
        ))
        db.send_create_signal(u'majitables', ['Watersrcckg9'])

        # Adding model 'Watersrcdrk9'
        db.create_table(u'WaterSrcDrk-9', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('areaid', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'AreaID', blank=True)),
            ('areaname', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'Areaname')),
            ('drkgwatersrc', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'DrkgWaterSrc')),
            ('areasmpdus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'AreaSmpDUs', blank=True)),
            ('smpusingsrc', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'Smpusingsrc', blank=True)),
            ('pcntdususingsrc', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'pcntDUsusingsrc', blank=True)),
            ('ndus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'NDus', blank=True)),
            ('nppleusingsrc', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'Nppleusingsrc', blank=True)),
            ('pcntppleusingsrc', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('numdu', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'NumDU', blank=True)),
        ))
        db.send_create_signal(u'majitables', ['Watersrcdrk9'])

        # Adding model 'Watersrclndry9'
        db.create_table(u'WaterSrcLndry-9', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('areaid', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'AreaID', blank=True)),
            ('areaname', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'Areaname')),
            ('watersrclndry', self.gf('django.db.models.fields.TextField')(db_column=u'WaterSrcLndry')),
            ('areasmpdus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'AreaSmpDUs', blank=True)),
            ('smpusingsrc', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'Smpusingsrc', blank=True)),
            ('pcntplotsusingsrc', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('ndus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'NDus', blank=True)),
            ('persons', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('pcntppleusingsrc', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('numdu', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'NumDU', blank=True)),
        ))
        db.send_create_signal(u'majitables', ['Watersrclndry9'])

        # Adding model 'Waterstoragedu'
        db.create_table(u'WaterStorageDU', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('areaid', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'AreaID', blank=True)),
            ('areaname', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'Areaname')),
            ('storagemthd', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'StorageMthd')),
            ('areasmpdus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'AreaSmpDUs', blank=True)),
            ('smpdus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'SmpDUs', blank=True)),
            ('pcntdus', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'pcntDUs', blank=True)),
            ('ndus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'NDus', blank=True)),
            ('persons', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('pcntpple', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('numdu', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'numDU', blank=True)),
        ))
        db.send_create_signal(u'majitables', ['Waterstoragedu'])

        # Adding model 'Watertrt33County'
        db.create_table(u'WaterTrt33County', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('countyid', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'CountyID', blank=True)),
            ('countyname', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'CountyName')),
            ('drkwatertreated', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'DrkWaterTreated')),
            ('smpsrc', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'SmpSrc', blank=True)),
            ('smpdus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'SmpDUs', blank=True)),
            ('totdus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'TotDUs', blank=True)),
            ('pcntdususingsrc', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'pcntDUsusingsrc', blank=True)),
            ('nousingsrc', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'NoUsingSrc', blank=True)),
        ))
        db.send_create_signal(u'majitables', ['Watertrt33County'])

        # Adding model 'Watertrt33Slum'
        db.create_table(u'WaterTrt33Slum', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('slumid', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'SlumID', blank=True)),
            ('slumname', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'SlumName')),
            ('drkwatertreated', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'DrkWaterTreated')),
            ('smpsrc', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'SmpSrc', blank=True)),
            ('smpdus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'SmpDUs', blank=True)),
            ('totdus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'TotDUs', blank=True)),
            ('pcntdususingsrc', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'pcntDUsusingsrc', blank=True)),
            ('nousingsrc', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'NoUsingSrc', blank=True)),
        ))
        db.send_create_signal(u'majitables', ['Watertrt33Slum'])

        # Adding model 'Watertrt33Town'
        db.create_table(u'WaterTrt33Town', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('townid', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'TownID', blank=True)),
            ('townname', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'TownName')),
            ('drkwatertreated', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'DrkWaterTreated')),
            ('smpsrc', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'SmpSrc', blank=True)),
            ('smpdus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'SmpDUs', blank=True)),
            ('totdus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'TotDUs', blank=True)),
            ('pcntdususingsrc', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'pcntDUsusingsrc', blank=True)),
            ('nousingsrc', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'NoUsingSrc', blank=True)),
        ))
        db.send_create_signal(u'majitables', ['Watertrt33Town'])

        # Adding model 'Watertrt33Wsp'
        db.create_table(u'WaterTrt33WSP', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('wspid', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'WSPID')),
            ('wspname', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'WSPName')),
            ('drkwatertreated', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'DrkWaterTreated')),
            ('smpsrc', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'SmpSrc', blank=True)),
            ('smpdus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'SmpDUs', blank=True)),
            ('totdus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'TotDUs', blank=True)),
            ('pcntdususingsrc', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'pcntDUsusingsrc', blank=True)),
            ('nousingsrc', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'NoUsingSrc', blank=True)),
        ))
        db.send_create_signal(u'majitables', ['Watertrt33Wsp'])

        # Adding model 'Watertrtdu9'
        db.create_table(u'WaterTrtDU-9', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('areaid', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'AreaID', blank=True)),
            ('areaname', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'Areaname')),
            ('drkwatertreated', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'DrkWaterTreated')),
            ('areasmpdus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'AreaSmpDUs', blank=True)),
            ('smpusingsrc', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'Smpusingsrc', blank=True)),
            ('pcntdus', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'pcntDUs', blank=True)),
            ('ndus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'NDus', blank=True)),
            ('persons', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('pcntpple', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('numdu', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'numDU', blank=True)),
        ))
        db.send_create_signal(u'majitables', ['Watertrtdu9'])

        # Adding model 'Watertrtmthddu'
        db.create_table(u'WaterTrtMthdDU', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('areaid', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'AreaID', blank=True)),
            ('areaname', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'Areaname')),
            ('drkwatertrtmthd', self.gf('django.db.models.fields.TextField')(db_column=u'DrkWaterTrtMthd', blank=True)),
            ('dus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'DUs', blank=True)),
            ('pcntdus', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'pcntDUs', blank=True)),
            ('ndus', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'NDus', blank=True)),
            ('numdu', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'numDU', blank=True)),
            ('ndu', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'NDU', blank=True)),
        ))
        db.send_create_signal(u'majitables', ['Watertrtmthddu'])

        # Adding model 'Watertrtstorage'
        db.create_table(u'WaterTrtStorage', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('areaid', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'AreaID', blank=True)),
            ('wspwaterqlty', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'WSPWaterQlty')),
            ('infwaterqlty', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'InfWaterQlty')),
            ('watertreated', self.gf('django.db.models.fields.TextField')(db_column=u'WaterTreated', blank=True)),
            ('wtrtmethods', self.gf('django.db.models.fields.TextField')(db_column=u'WtrtMethods', blank=True)),
            ('storagemthd', self.gf('django.db.models.fields.TextField')(db_column=u'StorageMthd', blank=True)),
        ))
        db.send_create_signal(u'majitables', ['Watertrtstorage'])

        # Adding model 'Wresidentsperwspksk'
        db.create_table(u'WresidentsperWSPKsk', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('area', self.gf('django.db.models.fields.FloatField')(null=True, db_column=u'Area', blank=True)),
            ('areaname', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'Areaname')),
            ('areapop', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'AreaPop', blank=True)),
            ('pubwaterksks', self.gf('django.db.models.fields.IntegerField')(null=True, db_column=u'PubWaterKsks', blank=True)),
            ('ppleperkiosk', self.gf('django.db.models.fields.CharField')(max_length=100, db_column=u'PplePerKiosk')),
        ))
        db.send_create_signal(u'majitables', ['Wresidentsperwspksk'])


    def backwards(self, orm):
        # Deleting model 'Apopdenavgminmaxcounty'
        db.delete_table(u'APopDenAvgMinMaxCounty')

        # Deleting model 'Apopdenavgminmaxslum'
        db.delete_table(u'APopDenAvgMinMaxSlum')

        # Deleting model 'Apopdenavgminmaxtown'
        db.delete_table(u'APopDenAvgMinMaxTown')

        # Deleting model 'Apopdennareascounty'
        db.delete_table(u'APopDenNAreasCounty')

        # Deleting model 'Apopdennareasslum'
        db.delete_table(u'APopDenNAreasSlum')

        # Deleting model 'Apopdennareastowns'
        db.delete_table(u'APopDenNAreasTowns')

        # Deleting model 'Areadustatuscounty'
        db.delete_table(u'AreaDUStatusCounty')

        # Deleting model 'Areadustatusslum'
        db.delete_table(u'AreaDUStatusSlum')

        # Deleting model 'Areadustatustown'
        db.delete_table(u'AreaDUStatusTown')

        # Deleting model 'Areadustatuswsp'
        db.delete_table(u'AreaDUStatusWSP')

        # Deleting model 'Areadutypecounty'
        db.delete_table(u'AreaDUTypeCounty')

        # Deleting model 'Areadutypeslum'
        db.delete_table(u'AreaDUTypeSlum')

        # Deleting model 'Areadutypestructure'
        db.delete_table(u'AreaDUTypeStructure')

        # Deleting model 'Areadutypetown'
        db.delete_table(u'AreaDUTypeTown')

        # Deleting model 'Areadutypewsp'
        db.delete_table(u'AreaDUTypeWSP')

        # Deleting model 'Areadutypehse'
        db.delete_table(u'AreaDUTypehse')

        # Deleting model 'Areahabhsetypecounty'
        db.delete_table(u'AreaHabHseTypeCounty')

        # Deleting model 'Areahabhsetypeslum'
        db.delete_table(u'AreaHabHseTypeSlum')

        # Deleting model 'Areahabhsetypetown'
        db.delete_table(u'AreaHabHseTypeTown')

        # Deleting model 'Areahabhsetypewsp'
        db.delete_table(u'AreaHabHseTypeWSP')

        # Deleting model 'Areahabhsgsitcounty'
        db.delete_table(u'AreaHabHsgSitCounty')

        # Deleting model 'Areahabhsgsitslum'
        db.delete_table(u'AreaHabHsgSitSlum')

        # Deleting model 'Areahabhsgsittown'
        db.delete_table(u'AreaHabHsgSitTown')

        # Deleting model 'Areahabhsgsitwsp'
        db.delete_table(u'AreaHabHsgSitWSP')

        # Deleting model 'Areahabroofcounty'
        db.delete_table(u'AreaHabRoofCounty')

        # Deleting model 'Areahabroofslum'
        db.delete_table(u'AreaHabRoofSlum')

        # Deleting model 'Areahabrooftown'
        db.delete_table(u'AreaHabRoofTown')

        # Deleting model 'Areahabroofwsp'
        db.delete_table(u'AreaHabRoofWSP')

        # Deleting model 'Areahabwallcounty'
        db.delete_table(u'AreaHabWallCounty')

        # Deleting model 'Areahabwallslum'
        db.delete_table(u'AreaHabWallSlum')

        # Deleting model 'Areahabwalltown'
        db.delete_table(u'AreaHabWallTown')

        # Deleting model 'Areahabwallwsp'
        db.delete_table(u'AreaHabWallWSP')

        # Deleting model 'Arealist'
        db.delete_table(u'AreaList')

        # Deleting model 'Arealist2'
        db.delete_table(u'AreaList2')

        # Deleting model 'Areanospckskcounty'
        db.delete_table(u'AreaNoSpcKskCounty')

        # Deleting model 'Areanospckskslum'
        db.delete_table(u'AreaNoSpcKskSlum')

        # Deleting model 'Areanospcksktown'
        db.delete_table(u'AreaNoSpcKskTown')

        # Deleting model 'Areanospckskwsp'
        db.delete_table(u'AreaNoSpcKskWSP')

        # Deleting model 'Areanospcpubsancounty'
        db.delete_table(u'AreaNoSpcPubSanCounty')

        # Deleting model 'Areanospcpubsanslum'
        db.delete_table(u'AreaNoSpcPubSanSlum')

        # Deleting model 'Areanospcpubsantown'
        db.delete_table(u'AreaNoSpcPubSanTown')

        # Deleting model 'Areanospcpubsanwsp'
        db.delete_table(u'AreaNoSpcPubSanWSP')

        # Deleting model 'Areaownducounty'
        db.delete_table(u'AreaOwnDUCounty')

        # Deleting model 'Areaownduslum'
        db.delete_table(u'AreaOwnDUSlum')

        # Deleting model 'Areaowndutown'
        db.delete_table(u'AreaOwnDUTown')

        # Deleting model 'Areaownduwsp'
        db.delete_table(u'AreaOwnDUWSP')

        # Deleting model 'Areaphychar'
        db.delete_table(u'AreaPhyChar')

        # Deleting model 'Areapop'
        db.delete_table(u'AreaPop')

        # Deleting model 'Areapopdensity'
        db.delete_table(u'AreaPopDensity')

        # Deleting model 'Areaprofiles'
        db.delete_table(u'AreaProfiles')

        # Deleting model 'Areasubjfldcounty'
        db.delete_table(u'AreaSubjFldCounty')

        # Deleting model 'Areasubjfldslum'
        db.delete_table(u'AreaSubjFldSlum')

        # Deleting model 'Areasubjfldtown'
        db.delete_table(u'AreaSubjFldTown')

        # Deleting model 'Areasubjfldwsp'
        db.delete_table(u'AreaSubjFldWSP')

        # Deleting model 'Areasummarysheet'
        db.delete_table(u'AreaSummarySheet')

        # Deleting model 'Areassettlocrdrlcounty'
        db.delete_table(u'AreasSettLocRdRlCounty')

        # Deleting model 'Areassettlocrdrlslum'
        db.delete_table(u'AreasSettLocRdRlSlum')

        # Deleting model 'Areassettlocrdrltown'
        db.delete_table(u'AreasSettLocRdRlTown')

        # Deleting model 'Areassettlocrdrlwsp'
        db.delete_table(u'AreasSettLocRdRlWSP')

        # Deleting model 'Demogtrends'
        db.delete_table(u'DemogTrends')

        # Deleting model 'Devplans'
        db.delete_table(u'DevPlans')

        # Deleting model 'Femhhhscounty'
        db.delete_table(u'FemHHHsCounty')

        # Deleting model 'Femhhhsslum'
        db.delete_table(u'FemHHHsSlum')

        # Deleting model 'Femhhhstown'
        db.delete_table(u'FemHHHsTown')

        # Deleting model 'Habitationpatterns'
        db.delete_table(u'HabitationPatterns')

        # Deleting model 'Landownuse'
        db.delete_table(u'LandOwnUse')

        # Deleting model 'Majidatainfocounty'
        db.delete_table(u'MajidataInfoCounty')

        # Deleting model 'Majidatainfoslum'
        db.delete_table(u'MajidataInfoSlum')

        # Deleting model 'Majidatainfotwn'
        db.delete_table(u'MajidataInfoTwn')

        # Deleting model 'Majidatainfowsp'
        db.delete_table(u'MajidataInfoWSP')

        # Deleting model 'Pavghhduszcounty'
        db.delete_table(u'PAvgHHDUSzCounty')

        # Deleting model 'Pavghhduszslum'
        db.delete_table(u'PAvgHHDUSzSlum')

        # Deleting model 'Pavghhdusztown'
        db.delete_table(u'PAvgHHDUSzTown')

        # Deleting model 'Phlthwasterds'
        db.delete_table(u'PHlthWasteRds')

        # Deleting model 'Pownduwsrckskcounty'
        db.delete_table(u'POwnDUWSrcKskCounty')

        # Deleting model 'Pownduwsrckskslum'
        db.delete_table(u'POwnDUWSrcKskSlum')

        # Deleting model 'Pownduwsrcksktown'
        db.delete_table(u'POwnDUWSrcKskTown')

        # Deleting model 'Pownduwsrckskwsp'
        db.delete_table(u'POwnDUWSrcKskWSP')

        # Deleting model 'Pownduwsrcpipedcounty'
        db.delete_table(u'POwnDUWSrcPipedCounty')

        # Deleting model 'Pownduwsrcpipedslum'
        db.delete_table(u'POwnDUWSrcPipedSlum')

        # Deleting model 'Pownduwsrcpipedtown'
        db.delete_table(u'POwnDUWSrcPipedTown')

        # Deleting model 'Pownduwsrcpipedwsp'
        db.delete_table(u'POwnDUWSrcPipedWSP')

        # Deleting model 'Preligioncounty'
        db.delete_table(u'PReligionCounty')

        # Deleting model 'Preligionslum'
        db.delete_table(u'PReligionSlum')

        # Deleting model 'Preligiontown'
        db.delete_table(u'PReligionTown')

        # Deleting model 'Preligionwsp'
        db.delete_table(u'PReligionWSP')

        # Deleting model 'Popareabysettlementcounty'
        db.delete_table(u'PopAreaBySettlementCounty')

        # Deleting model 'Popareabysettlementslum'
        db.delete_table(u'PopAreaBySettlementSlum')

        # Deleting model 'Popareabysettlementtown'
        db.delete_table(u'PopAreaBySettlementTown')

        # Deleting model 'Popareatypecounty'
        db.delete_table(u'PopAreaTypeCounty')

        # Deleting model 'Popareatypeslum'
        db.delete_table(u'PopAreaTypeSlum')

        # Deleting model 'Popareatypetown'
        db.delete_table(u'PopAreaTypeTown')

        # Deleting model 'Popareatypewsp'
        db.delete_table(u'PopAreaTypeWSP')

        # Deleting model 'Popareasbylegalcounty'
        db.delete_table(u'PopAreasByLegalCounty')

        # Deleting model 'Popareasbylegalslum'
        db.delete_table(u'PopAreasByLegalSlum')

        # Deleting model 'Popareasbylegaltown'
        db.delete_table(u'PopAreasByLegalTown')

        # Deleting model 'Savgdush44County'
        db.delete_table(u'SAvgDUSh44County')

        # Deleting model 'Savgdush44Slum'
        db.delete_table(u'SAvgDUSh44Slum')

        # Deleting model 'Savgdush44Wsp'
        db.delete_table(u'SAvgDUSh44WSP')

        # Deleting model 'Savgdusshfaccounty'
        db.delete_table(u'SAvgDUsShFacCounty')

        # Deleting model 'Savgdusshfacslum'
        db.delete_table(u'SAvgDUsShFacSlum')

        # Deleting model 'Savgdusshfacwsp'
        db.delete_table(u'SAvgDUsShFacWSP')

        # Deleting model 'Savghhshowntlt'
        db.delete_table(u'SAvgHHShOwnTlt')

        # Deleting model 'Savgtltbath'
        db.delete_table(u'SAvgTltBath')

        # Deleting model 'Sduhasownbath'
        db.delete_table(u'SDUHasOwnBath')

        # Deleting model 'Sduhasownfacility'
        db.delete_table(u'SDUHasOwnFacility')

        # Deleting model 'Sduownbath45County'
        db.delete_table(u'SDUOwnBath45County')

        # Deleting model 'Sduownbath45Slum'
        db.delete_table(u'SDUOwnBath45Slum')

        # Deleting model 'Sduownbath45Wsp'
        db.delete_table(u'SDUOwnBath45WSP')

        # Deleting model 'Sduownfac45County'
        db.delete_table(u'SDUOwnFac45County')

        # Deleting model 'Sduownfac45Slum'
        db.delete_table(u'SDUOwnFac45Slum')

        # Deleting model 'Sduownfac45Wsp'
        db.delete_table(u'SDUOwnFac45WSP')

        # Deleting model 'Sduownrpit45County'
        db.delete_table(u'SDUOwnRPit45County')

        # Deleting model 'Sduownrpit45Slum'
        db.delete_table(u'SDUOwnRPit45Slum')

        # Deleting model 'Sduownrpit45Wsp'
        db.delete_table(u'SDUOwnRPit45WSP')

        # Deleting model 'Sdusharestoilet'
        db.delete_table(u'SDuSharesToilet')

        # Deleting model 'Seincomesrcs'
        db.delete_table(u'SEIncomeSrcs')

        # Deleting model 'Sfacinplotcounty'
        db.delete_table(u'SFacInPlotCounty')

        # Deleting model 'Sfacinplotslum'
        db.delete_table(u'SFacInPlotSlum')

        # Deleting model 'Sfacinplotwsp'
        db.delete_table(u'SFacInPlotWSP')

        # Deleting model 'Sfacsharedcounty'
        db.delete_table(u'SFacSharedCounty')

        # Deleting model 'Sfacsharedslum'
        db.delete_table(u'SFacSharedSlum')

        # Deleting model 'Sfacsharedwsp'
        db.delete_table(u'SFacSharedWSP')

        # Deleting model 'Sfactypes'
        db.delete_table(u'SFacTypes')

        # Deleting model 'Simpjmp'
        db.delete_table(u'SImpJMP')

        # Deleting model 'Simpjmpcounty'
        db.delete_table(u'SImpJMPCounty')

        # Deleting model 'Simpjmpownfac'
        db.delete_table(u'SImpJMPOwnFac')

        # Deleting model 'Simpjmpownplotfac'
        db.delete_table(u'SImpJMPOwnPlotFac')

        # Deleting model 'Simpjmpshfac'
        db.delete_table(u'SImpJMPShFac')

        # Deleting model 'Simpjmpsharedcounty'
        db.delete_table(u'SImpJMPSharedCounty')

        # Deleting model 'Simpjmpsharedslum'
        db.delete_table(u'SImpJMPSharedSlum')

        # Deleting model 'Simpjmpsharedwsp'
        db.delete_table(u'SImpJMPSharedWSP')

        # Deleting model 'Simpjmpslum'
        db.delete_table(u'SImpJMPSlum')

        # Deleting model 'Simpjmpwsp'
        db.delete_table(u'SImpJMPWSP')

        # Deleting model 'Snofacused'
        db.delete_table(u'SNoFacUsed')

        # Deleting model 'Snofacusedcounty'
        db.delete_table(u'SNoFacUsedCounty')

        # Deleting model 'Snofacusedslum'
        db.delete_table(u'SNoFacUsedSlum')

        # Deleting model 'Snofacusedwsp'
        db.delete_table(u'SNoFacUsedWSP')

        # Deleting model 'Snoofbaths'
        db.delete_table(u'SNoofBaths')

        # Deleting model 'Snoofdushrngtlt'
        db.delete_table(u'SNoofDUShrngTlt')

        # Deleting model 'Snooffacilities'
        db.delete_table(u'SNoofFacilities')

        # Deleting model 'Sownimpjmpcounty'
        db.delete_table(u'SOwnImpJMPCounty')

        # Deleting model 'Sownimpjmpslum'
        db.delete_table(u'SOwnImpJMPSlum')

        # Deleting model 'Sownimpjmpwsp'
        db.delete_table(u'SOwnImpJMPWSP')

        # Deleting model 'Spractice'
        db.delete_table(u'SPractice')

        # Deleting model 'Ssepbaths'
        db.delete_table(u'SSepBaths')

        # Deleting model 'Sseptoilets'
        db.delete_table(u'SSepToilets')

        # Deleting model 'Swduhasownrpit'
        db.delete_table(u'SWDUHasOwnRpit')

        # Deleting model 'Swnoofrubpits'
        db.delete_table(u'SWNoofRubPits')

        # Deleting model 'Swrpitshared'
        db.delete_table(u'SWRPitShared')

        # Deleting model 'Sanfacpractcounty'
        db.delete_table(u'SanFacPractCounty')

        # Deleting model 'Sanfacpractslum'
        db.delete_table(u'SanFacPractSlum')

        # Deleting model 'Sanfacpractwsp'
        db.delete_table(u'SanFacPractWSP')

        # Deleting model 'Sanitation12B'
        db.delete_table(u'Sanitation-12b')

        # Deleting model 'Sanitationpractice'
        db.delete_table(u'SanitationPractice')

        # Deleting model 'Sanitationsewlnk'
        db.delete_table(u'SanitationSewLnk')

        # Deleting model 'Socioeconinfr'
        db.delete_table(u'SocioEconInfr')

        # Deleting model 'Sownimpntshcounty'
        db.delete_table(u'SownImpNtShCounty')

        # Deleting model 'Sownimpntshslum'
        db.delete_table(u'SownImpNtShSlum')

        # Deleting model 'Sownimpntshunpcounty'
        db.delete_table(u'SownImpNtShUnpCounty')

        # Deleting model 'Sownimpntshunpslum'
        db.delete_table(u'SownImpNtShUnpSlum')

        # Deleting model 'Sownimpntshunpwsp'
        db.delete_table(u'SownImpNtShUnpWSP')

        # Deleting model 'Sownimpntshwsp'
        db.delete_table(u'SownImpNtShWSP')

        # Deleting model 'Summaryshtcounty'
        db.delete_table(u'SummaryShtCounty')

        # Deleting model 'Summaryshtslum'
        db.delete_table(u'SummaryShtSlum')

        # Deleting model 'Summaryshttown'
        db.delete_table(u'SummaryShtTown')

        # Deleting model 'TownsareasCounties'
        db.delete_table(u'TownsAreas-Counties')

        # Deleting model 'TownsareasSlum'
        db.delete_table(u'TownsAreas-Slum')

        # Deleting model 'TownsareasTowns'
        db.delete_table(u'TownsAreas-Towns')

        # Deleting model 'TownsareasWsp'
        db.delete_table(u'TownsAreas-WSP')

        # Deleting model 'Wadeqsupallksk'
        db.delete_table(u'WAdeqSupAllKsk')

        # Deleting model 'Wadeqsupimpwstfsrcs'
        db.delete_table(u'WAdeqSupImpWSTFSrcs')

        # Deleting model 'Wadeqsupprivcons10D'
        db.delete_table(u'WAdeqSupPrivCons-10d')

        # Deleting model 'Wadeqsuppubtap10D'
        db.delete_table(u'WAdeqSupPubTap-10d')

        # Deleting model 'Wadeqsupwspksk'
        db.delete_table(u'WAdeqSupWSPKsk')

        # Deleting model 'Wareasmnprob33County'
        db.delete_table(u'WAreasMnProb33County')

        # Deleting model 'Wareasmnprob33Slum'
        db.delete_table(u'WAreasMnProb33Slum')

        # Deleting model 'Wareasmnprob33Town'
        db.delete_table(u'WAreasMnProb33Town')

        # Deleting model 'Wareasmnprob33Wsp'
        db.delete_table(u'WAreasMnProb33WSP')

        # Deleting model 'Wareasnwlinkcounty'
        db.delete_table(u'WAreasNWLinkCounty')

        # Deleting model 'Wareasnwlinkslum'
        db.delete_table(u'WAreasNWLinkSlum')

        # Deleting model 'Wareasnwlinktown'
        db.delete_table(u'WAreasNWLinkTown')

        # Deleting model 'Wareasnwlinkwsp'
        db.delete_table(u'WAreasNWLinkWSP')

        # Deleting model 'Wareastechstatcounty'
        db.delete_table(u'WAreasTechstatCounty')

        # Deleting model 'Wareastechstatslum'
        db.delete_table(u'WAreasTechstatSlum')

        # Deleting model 'Wareastechstattown'
        db.delete_table(u'WAreasTechstatTown')

        # Deleting model 'Wareastechstatwsp'
        db.delete_table(u'WAreasTechstatWSP')

        # Deleting model 'Wckgsrcpipedcounty'
        db.delete_table(u'WCkgSrcPipedCounty')

        # Deleting model 'Wckgsrcpipedslum'
        db.delete_table(u'WCkgSrcPipedSlum')

        # Deleting model 'Wckgsrcpipedtown'
        db.delete_table(u'WCkgSrcPipedTown')

        # Deleting model 'Wckgsrcpipedwsp'
        db.delete_table(u'WCkgSrcPipedWSP')

        # Deleting model 'WconstatusDu'
        db.delete_table(u'WConStatus-DU')

        # Deleting model 'Wconstatus34County'
        db.delete_table(u'WConStatus34County')

        # Deleting model 'Wconstatus34Slum'
        db.delete_table(u'WConStatus34Slum')

        # Deleting model 'Wconstatus34Town'
        db.delete_table(u'WConStatus34Town')

        # Deleting model 'Wconstatus34Wsp'
        db.delete_table(u'WConStatus34WSP')

        # Deleting model 'Wconsumption'
        db.delete_table(u'WConsumption')

        # Deleting model 'Wduconcounty'
        db.delete_table(u'WDUConCounty')

        # Deleting model 'Wduconmetcounty'
        db.delete_table(u'WDUConMetCounty')

        # Deleting model 'Wduconmetslum'
        db.delete_table(u'WDUConMetSlum')

        # Deleting model 'Wduconmettown'
        db.delete_table(u'WDUConMetTown')

        # Deleting model 'Wduconmetwsp'
        db.delete_table(u'WDUConMetWSP')

        # Deleting model 'Wduconslum'
        db.delete_table(u'WDUConSlum')

        # Deleting model 'Wducontown'
        db.delete_table(u'WDUConTown')

        # Deleting model 'Wduconwsp'
        db.delete_table(u'WDUConWSP')

        # Deleting model 'Wduowncon'
        db.delete_table(u'WDUOwnCon')

        # Deleting model 'Wduowncon210D'
        db.delete_table(u'WDUOwnCon2-10d')

        # Deleting model 'Wduownconmet'
        db.delete_table(u'WDUOwnConMet')

        # Deleting model 'Wduownconmet210D'
        db.delete_table(u'WDUOwnConMet2-10d')

        # Deleting model 'Wduwaterpaycounty'
        db.delete_table(u'WDUWaterPayCounty')

        # Deleting model 'Wduwaterpayslum'
        db.delete_table(u'WDUWaterPaySlum')

        # Deleting model 'Wduwaterpaytown'
        db.delete_table(u'WDUWaterPayTown')

        # Deleting model 'Wduwaterpaywsp'
        db.delete_table(u'WDUWaterPayWSP')

        # Deleting model 'Wdrkqlty33County'
        db.delete_table(u'WDrkQlty33County')

        # Deleting model 'Wdrkqlty33Slum'
        db.delete_table(u'WDrkQlty33Slum')

        # Deleting model 'Wdrkqlty33Town'
        db.delete_table(u'WDrkQlty33Town')

        # Deleting model 'Wdrkqlty33Wsp'
        db.delete_table(u'WDrkQlty33WSP')

        # Deleting model 'Wdrksrc33County'
        db.delete_table(u'WDrkSrc33County')

        # Deleting model 'Wdrksrc33Slum'
        db.delete_table(u'WDrkSrc33Slum')

        # Deleting model 'Wdrksrc33Town'
        db.delete_table(u'WDrkSrc33Town')

        # Deleting model 'Wdrksrc33Wsp'
        db.delete_table(u'WDrkSrc33WSP')

        # Deleting model 'Wdrksrcbyqltycounty37'
        db.delete_table(u'WDrkSrcByQltyCounty-37')

        # Deleting model 'Wdrksrcbyqltyslum37'
        db.delete_table(u'WDrkSrcByQltySlum-37')

        # Deleting model 'Wdrksrcbyqltytown37'
        db.delete_table(u'WDrkSrcByQltyTown-37')

        # Deleting model 'Wdrksrcbyqltywsp37'
        db.delete_table(u'WDrkSrcByQltyWSP-37')

        # Deleting model 'Wdrksrcbytrtmthdslum38'
        db.delete_table(u'WDrkSrcByTrtMthdSlum-38')

        # Deleting model 'Wdrksrcbytrtmthdtown38'
        db.delete_table(u'WDrkSrcByTrtMthdTown-38')

        # Deleting model 'Wdrksrcbytrtmthdwsp38'
        db.delete_table(u'WDrkSrcByTrtMthdWSP-38')

        # Deleting model 'Wdrksrccmtaps10D'
        db.delete_table(u'WDrkSrcCmTaps-10d')

        # Deleting model 'Wdrksrcleak'
        db.delete_table(u'WDrkSrcLeak')

        # Deleting model 'Wdrksrcothcon'
        db.delete_table(u'WDrkSrcOthCon')

        # Deleting model 'Wdrksrcpipedcounty'
        db.delete_table(u'WDrkSrcPipedCounty')

        # Deleting model 'Wdrksrcpipedslum'
        db.delete_table(u'WDrkSrcPipedSlum')

        # Deleting model 'Wdrksrcpipedtown'
        db.delete_table(u'WDrkSrcPipedTown')

        # Deleting model 'Wdrksrcpipedwsp'
        db.delete_table(u'WDrkSrcPipedWSP')

        # Deleting model 'Wdrksrcreseller'
        db.delete_table(u'WDrkSrcReseller')

        # Deleting model 'Wdrksrcywell'
        db.delete_table(u'WDrkSrcYWell')

        # Deleting model 'Wfetchdurationdu'
        db.delete_table(u'WFetchDurationDU')

        # Deleting model 'Wimpdrksrcjmp'
        db.delete_table(u'WImpDrkSrcJMP')

        # Deleting model 'Wimpdrksrcjmp30Mn'
        db.delete_table(u'WImpDrkSrcJMP30mn')

        # Deleting model 'Wimpdrksrcjmpbyqlty'
        db.delete_table(u'WImpDrkSrcJMPByQlty')

        # Deleting model 'Wimpdrksrcjmpbytrt'
        db.delete_table(u'WImpDrkSrcJMPByTrt')

        # Deleting model 'Wimpdrksrcwstf'
        db.delete_table(u'WImpDrkSrcWSTF')

        # Deleting model 'Wimpdrksrcwstf30Mn'
        db.delete_table(u'WImpDrkSrcWSTF30mn')

        # Deleting model 'Wimpdrksrcwstfbyqlty'
        db.delete_table(u'WImpDrkSrcWSTFByQlty')

        # Deleting model 'Wimpdrksrcwstfbytrt'
        db.delete_table(u'WImpDrkSrcWSTFByTrt')

        # Deleting model 'Wimpsrcbathwstfcounty'
        db.delete_table(u'WImpSrcBathWSTFCounty')

        # Deleting model 'Wimpsrcbathwstfslum'
        db.delete_table(u'WImpSrcBathWSTFSlum')

        # Deleting model 'Wimpsrcbathwstftown'
        db.delete_table(u'WImpSrcBathWSTFTown')

        # Deleting model 'Wimpsrcbathwstfwsp'
        db.delete_table(u'WImpSrcBathWSTFWSP')

        # Deleting model 'Wimpsrcckgwstfcounty'
        db.delete_table(u'WImpSrcCkgWSTFCounty')

        # Deleting model 'Wimpsrcckgwstfslum'
        db.delete_table(u'WImpSrcCkgWSTFSlum')

        # Deleting model 'Wimpsrcckgwstftown'
        db.delete_table(u'WImpSrcCkgWSTFTown')

        # Deleting model 'Wimpsrcckgwstfwsp'
        db.delete_table(u'WImpSrcCkgWSTFWSP')

        # Deleting model 'Wimpsrcdrkwstfcounty'
        db.delete_table(u'WImpSrcDrkWSTFCounty')

        # Deleting model 'Wimpsrcdrkwstfslum'
        db.delete_table(u'WImpSrcDrkWSTFSlum')

        # Deleting model 'Wimpsrcdrkwstfwsp'
        db.delete_table(u'WImpSrcDrkWSTFWSP')

        # Deleting model 'Wnocompubpsts10D'
        db.delete_table(u'WNoComPubPsts-10d')

        # Deleting model 'Woutletscounty'
        db.delete_table(u'WOutletsCounty')

        # Deleting model 'Woutletsslum'
        db.delete_table(u'WOutletsSlum')

        # Deleting model 'Woutletstown'
        db.delete_table(u'WOutletsTown')

        # Deleting model 'Woutletswsp'
        db.delete_table(u'WOutletsWSP')

        # Deleting model 'Wpconcounty'
        db.delete_table(u'WPConCounty')

        # Deleting model 'Wpconmetcounty'
        db.delete_table(u'WPConMetCounty')

        # Deleting model 'Wpconmetslum'
        db.delete_table(u'WPConMetSlum')

        # Deleting model 'Wpconmettown'
        db.delete_table(u'WPConMetTown')

        # Deleting model 'Wpconmetwsp'
        db.delete_table(u'WPConMetWSP')

        # Deleting model 'Wpconslum'
        db.delete_table(u'WPConSlum')

        # Deleting model 'Wpcontown'
        db.delete_table(u'WPConTown')

        # Deleting model 'Wpconwsp'
        db.delete_table(u'WPConWSP')

        # Deleting model 'Wpducondisconnected'
        db.delete_table(u'WPDUConDisconnected')

        # Deleting model 'Wpaydrkdu'
        db.delete_table(u'WPayDrkDU')

        # Deleting model 'Wpaynondrkdu'
        db.delete_table(u'WPayNonDrkDU')

        # Deleting model 'Wpipedsrcbath'
        db.delete_table(u'WPipedSrcBath')

        # Deleting model 'Wpipedsrcdrk'
        db.delete_table(u'WPipedSrcDrk')

        # Deleting model 'Wpipedsrcdrkavgpay'
        db.delete_table(u'WPipedSrcDrkAvgPay')

        # Deleting model 'Wpipedsrcdrktrt'
        db.delete_table(u'WPipedSrcDrkTrt')

        # Deleting model 'WplotconmetDu'
        db.delete_table(u'WPlotConMet-DU')

        # Deleting model 'WplotconnectedDu'
        db.delete_table(u'WPlotConnected-DU')

        # Deleting model 'Wrespercomtapcounty'
        db.delete_table(u'WResPerComTapCounty')

        # Deleting model 'Wrespercomtapslum'
        db.delete_table(u'WResPerComTapSlum')

        # Deleting model 'Wrespercomtaptown'
        db.delete_table(u'WResPerComTapTown')

        # Deleting model 'Wrespercomtapwsp'
        db.delete_table(u'WResPerComTapWSP')

        # Deleting model 'Wresperpubcomkskscounty'
        db.delete_table(u'WResPerPubComKsksCounty')

        # Deleting model 'Wresperpubcomksksslum'
        db.delete_table(u'WResPerPubComKsksSlum')

        # Deleting model 'Wresperpubcomkskstown'
        db.delete_table(u'WResPerPubComKsksTown')

        # Deleting model 'Wresperpubcomkskswsp'
        db.delete_table(u'WResPerPubComKsksWSP')

        # Deleting model 'Wresperpubwspcomtapscounty'
        db.delete_table(u'WResPerPubWSPComTapsCounty')

        # Deleting model 'Wresperpubwspcomtapsslum'
        db.delete_table(u'WResPerPubWSPComTapsSlum')

        # Deleting model 'Wresperpubwspcomtapstown'
        db.delete_table(u'WResPerPubWSPComTapsTown')

        # Deleting model 'Wresperpubwspcomtapswsp'
        db.delete_table(u'WResPerPubWSPComTapsWSP')

        # Deleting model 'Wresperpubwsptapcounty'
        db.delete_table(u'WResPerPubWSPTapCounty')

        # Deleting model 'Wresperpubwsptapslum'
        db.delete_table(u'WResPerPubWSPTapSlum')

        # Deleting model 'Wresperpubwsptaptown'
        db.delete_table(u'WResPerPubWSPTapTown')

        # Deleting model 'Wresperpubwsptapwsp'
        db.delete_table(u'WResPerPubWSPTapWSP')

        # Deleting model 'Wresperwspkskcounty'
        db.delete_table(u'WResPerWSPKskCounty')

        # Deleting model 'Wresperwspkskslum'
        db.delete_table(u'WResPerWSPKskSlum')

        # Deleting model 'Wresperwspksktown'
        db.delete_table(u'WResPerWSPKskTown')

        # Deleting model 'Wresperwspkskwsp'
        db.delete_table(u'WResPerWSPKskWSP')

        # Deleting model 'Wrespercompubpost10D'
        db.delete_table(u'WResperComPubPost-10d')

        # Deleting model 'Wsrcbathpipedcounty'
        db.delete_table(u'WSrcBathPipedCounty')

        # Deleting model 'Wsrcbathpipedslum'
        db.delete_table(u'WSrcBathPipedSlum')

        # Deleting model 'Wsrcbathpipedtown'
        db.delete_table(u'WSrcBathPipedTown')

        # Deleting model 'Wsrcbathpipedwsp'
        db.delete_table(u'WSrcBathPipedWSP')

        # Deleting model 'Wsrcckg33County'
        db.delete_table(u'WSrcCkg33County')

        # Deleting model 'Wsrcdrkbhpmpcounty'
        db.delete_table(u'WSrcDrkBhPmpCounty')

        # Deleting model 'Wsrcdrkbhpmpslum'
        db.delete_table(u'WSrcDrkBhPmpSlum')

        # Deleting model 'Wsrcdrkbhpmptown'
        db.delete_table(u'WSrcDrkBhPmpTown')

        # Deleting model 'Wsrcdrkbhpmpwsp'
        db.delete_table(u'WSrcDrkBhPmpWSP')

        # Deleting model 'Wsrcdrkksk'
        db.delete_table(u'WSrcDrkKsk')

        # Deleting model 'Wsrcdrkleakcounty'
        db.delete_table(u'WSrcDrkLeakCounty')

        # Deleting model 'Wsrcdrkleakslum'
        db.delete_table(u'WSrcDrkLeakSlum')

        # Deleting model 'Wsrcdrkleaktown'
        db.delete_table(u'WSrcDrkLeakTown')

        # Deleting model 'Wsrcdrkleakwsp'
        db.delete_table(u'WSrcDrkLeakWSP')

        # Deleting model 'Wsrcdrkspringcounty'
        db.delete_table(u'WSrcDrkSpringCounty')

        # Deleting model 'Wsrcdrkspringslum'
        db.delete_table(u'WSrcDrkSpringSlum')

        # Deleting model 'Wsrcdrkspringtown'
        db.delete_table(u'WSrcDrkSpringTown')

        # Deleting model 'Wsrcdrkspringwsp'
        db.delete_table(u'WSrcDrkSpringWSP')

        # Deleting model 'Wsrcdrkvendorcounty'
        db.delete_table(u'WSrcDrkVendorCounty')

        # Deleting model 'Wsrcdrkvendorslum'
        db.delete_table(u'WSrcDrkVendorSlum')

        # Deleting model 'Wsrcdrkvendortown'
        db.delete_table(u'WSrcDrkVendorTown')

        # Deleting model 'Wsrcdrkvendorwsp'
        db.delete_table(u'WSrcDrkVendorWSP')

        # Deleting model 'Wsrcdrkwellscounty'
        db.delete_table(u'WSrcDrkWellsCounty')

        # Deleting model 'Wsrcdrkwellsslum'
        db.delete_table(u'WSrcDrkWellsSlum')

        # Deleting model 'Wsrcdrkwellstown'
        db.delete_table(u'WSrcDrkWellsTown')

        # Deleting model 'Wsrcdrkwellswsp'
        db.delete_table(u'WSrcDrkWellsWSP')

        # Deleting model 'Wsupsituation8'
        db.delete_table(u'WSupSituation-8')

        # Deleting model 'Wsupsituation28'
        db.delete_table(u'WSupSituation2-8')

        # Deleting model 'Wsupsituation38D'
        db.delete_table(u'WSupSituation3-8d')

        # Deleting model 'Wsupsituationdu'
        db.delete_table(u'WSupSituationDU')

        # Deleting model 'Wsupplyinf8E'
        db.delete_table(u'WSupplyInf-8e')

        # Deleting model 'Wunreliablesrcbath'
        db.delete_table(u'WUnreliableSrcBath')

        # Deleting model 'Wunreliablesrcdrk'
        db.delete_table(u'WUnreliableSrcDrk')

        # Deleting model 'Wunreliablesrcdrkavgpay'
        db.delete_table(u'WUnreliableSrcDrkAvgPay')

        # Deleting model 'Wunreliablesrcdrktrt'
        db.delete_table(u'WUnreliableSrcDrkTrt')

        # Deleting model 'Wusersperindcon10D'
        db.delete_table(u'WUsersPerIndCon-10d')

        # Deleting model 'Wusersperksk'
        db.delete_table(u'WUsersPerKsk')

        # Deleting model 'Wusersperpubtap10D'
        db.delete_table(u'WUsersPerPubTap-10d')

        # Deleting model 'Wateroutlets'
        db.delete_table(u'WaterOutlets')

        # Deleting model 'Waterpaiddu'
        db.delete_table(u'WaterPaidDU')

        # Deleting model 'Waterpaymthddu'
        db.delete_table(u'WaterPayMthdDU')

        # Deleting model 'Waterqlty9'
        db.delete_table(u'WaterQlty-9')

        # Deleting model 'Watersrcbath9'
        db.delete_table(u'WaterSrcBath-9')

        # Deleting model 'Watersrcckg9'
        db.delete_table(u'WaterSrcCkg-9')

        # Deleting model 'Watersrcdrk9'
        db.delete_table(u'WaterSrcDrk-9')

        # Deleting model 'Watersrclndry9'
        db.delete_table(u'WaterSrcLndry-9')

        # Deleting model 'Waterstoragedu'
        db.delete_table(u'WaterStorageDU')

        # Deleting model 'Watertrt33County'
        db.delete_table(u'WaterTrt33County')

        # Deleting model 'Watertrt33Slum'
        db.delete_table(u'WaterTrt33Slum')

        # Deleting model 'Watertrt33Town'
        db.delete_table(u'WaterTrt33Town')

        # Deleting model 'Watertrt33Wsp'
        db.delete_table(u'WaterTrt33WSP')

        # Deleting model 'Watertrtdu9'
        db.delete_table(u'WaterTrtDU-9')

        # Deleting model 'Watertrtmthddu'
        db.delete_table(u'WaterTrtMthdDU')

        # Deleting model 'Watertrtstorage'
        db.delete_table(u'WaterTrtStorage')

        # Deleting model 'Wresidentsperwspksk'
        db.delete_table(u'WresidentsperWSPKsk')


    models = {
        u'majitables.apopdenavgminmaxcounty': {
            'Meta': {'object_name': 'Apopdenavgminmaxcounty', 'db_table': "u'APopDenAvgMinMaxCounty'"},
            'avgpopden': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'AvgPopDen'", 'blank': 'True'}),
            'avgsqkm': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'AvgSqKm'", 'blank': 'True'}),
            'countyid': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'CountyID'", 'blank': 'True'}),
            'countyname': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'Countyname'"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'max': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'Max'", 'blank': 'True'}),
            'min': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'Min'", 'blank': 'True'}),
            'nareas': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'NAreas'", 'blank': 'True'})
        },
        u'majitables.apopdenavgminmaxslum': {
            'Meta': {'object_name': 'Apopdenavgminmaxslum', 'db_table': "u'APopDenAvgMinMaxSlum'"},
            'avgpopden': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'AvgPopDen'", 'blank': 'True'}),
            'avgsqkm': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'AvgSqKm'", 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'max': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'Max'", 'blank': 'True'}),
            'min': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'Min'", 'blank': 'True'}),
            'nareas': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'NAreas'", 'blank': 'True'}),
            'slumid': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'SlumID'"}),
            'slumname': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'Slumname'"})
        },
        u'majitables.apopdenavgminmaxtown': {
            'Meta': {'object_name': 'Apopdenavgminmaxtown', 'db_table': "u'APopDenAvgMinMaxTown'"},
            'avgpopden': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'AvgPopDen'", 'blank': 'True'}),
            'avgsqkm': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'AvgSqKm'", 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'max': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'Max'", 'blank': 'True'}),
            'min': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'Min'", 'blank': 'True'}),
            'nareas': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'NAreas'", 'blank': 'True'}),
            'townid': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'townID'", 'blank': 'True'}),
            'townname': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'majitables.apopdennareascounty': {
            'Meta': {'object_name': 'Apopdennareascounty', 'db_table': "u'APopDenNAreasCounty'"},
            'countyid': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'countyID'", 'blank': 'True'}),
            'countyname': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nareas': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'NAreas'", 'blank': 'True'}),
            'pcntareas': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'PcntAreas'", 'blank': 'True'}),
            'popden': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'PopDen'"}),
            'totareas': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'TotAreas'", 'blank': 'True'})
        },
        u'majitables.apopdennareasslum': {
            'Meta': {'object_name': 'Apopdennareasslum', 'db_table': "u'APopDenNAreasSlum'"},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nareas': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'NAreas'", 'blank': 'True'}),
            'pcntareas': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'PcntAreas'", 'blank': 'True'}),
            'popden': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'PopDen'"}),
            'slumid': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'slumID'", 'blank': 'True'}),
            'slumname': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'totareas': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'TotAreas'", 'blank': 'True'})
        },
        u'majitables.apopdennareastowns': {
            'Meta': {'object_name': 'Apopdennareastowns', 'db_table': "u'APopDenNAreasTowns'"},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nareas': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'NAreas'", 'blank': 'True'}),
            'pcntareas': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'PcntAreas'", 'blank': 'True'}),
            'popden': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'PopDen'"}),
            'totareas': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'TotAreas'", 'blank': 'True'}),
            'townid': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'townID'", 'blank': 'True'}),
            'townname': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'majitables.areadustatuscounty': {
            'Meta': {'object_name': 'Areadustatuscounty', 'db_table': "u'AreaDUStatusCounty'"},
            'countyid': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'CountyID'", 'blank': 'True'}),
            'countyname': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'CountyName'"}),
            'dusinarea': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'DusInArea'", 'blank': 'True'}),
            'dustatus': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'DUStatus'"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nareas': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'Nareas'", 'blank': 'True'}),
            'pcntdus': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'pcntDUs'", 'blank': 'True'}),
            'smpdus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'SmpDUs'", 'blank': 'True'}),
            'totdus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'TotDUs'", 'blank': 'True'})
        },
        u'majitables.areadustatusslum': {
            'Meta': {'object_name': 'Areadustatusslum', 'db_table': "u'AreaDUStatusSlum'"},
            'dusinarea': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'DusInArea'"}),
            'dustatus': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'DUStatus'"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nareas': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'Nareas'", 'blank': 'True'}),
            'pcntdus': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'pcntDUs'"}),
            'slumid': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'SlumID'"}),
            'slumname': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'SlumName'"}),
            'smpdus': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'SmpDUs'"}),
            'totdus': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'TotDUs'"})
        },
        u'majitables.areadustatustown': {
            'Meta': {'object_name': 'Areadustatustown', 'db_table': "u'AreaDUStatusTown'"},
            'dusinarea': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'DusInArea'", 'blank': 'True'}),
            'dustatus': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'DUStatus'"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nareas': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'Nareas'", 'blank': 'True'}),
            'pcntdus': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'pcntDUs'", 'blank': 'True'}),
            'smpdus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'SmpDUs'", 'blank': 'True'}),
            'totdus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'TotDUs'", 'blank': 'True'}),
            'townid': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'TownID'", 'blank': 'True'}),
            'townname': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'TownName'"})
        },
        u'majitables.areadustatuswsp': {
            'Meta': {'object_name': 'Areadustatuswsp', 'db_table': "u'AreaDUStatusWSP'"},
            'dusinarea': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'DusInArea'", 'blank': 'True'}),
            'dustatus': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'DUStatus'"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nareas': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'Nareas'", 'blank': 'True'}),
            'pcntdus': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'pcntDUs'", 'blank': 'True'}),
            'smpdus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'SmpDUs'", 'blank': 'True'}),
            'totdus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'TotDUs'", 'blank': 'True'}),
            'wspid': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'WspID'"}),
            'wspname': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'WspName'"})
        },
        u'majitables.areadutypecounty': {
            'Meta': {'object_name': 'Areadutypecounty', 'db_table': "u'AreaDUTypeCounty'"},
            'countyid': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'CountyID'", 'blank': 'True'}),
            'countyname': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'CountyName'"}),
            'dusinarea': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'DusInArea'", 'blank': 'True'}),
            'dutype': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'DUType'"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nareas': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'Nareas'", 'blank': 'True'}),
            'pcntdus': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'pcntDUs'", 'blank': 'True'}),
            'smpdus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'SmpDUs'", 'blank': 'True'}),
            'totdus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'TotDUs'", 'blank': 'True'})
        },
        u'majitables.areadutypehse': {
            'Meta': {'object_name': 'Areadutypehse', 'db_table': "u'AreaDUTypehse'"},
            'areaid': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'AreaID'", 'blank': 'True'}),
            'areasmpdus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'AreaSmpDUs'", 'blank': 'True'}),
            'dutype': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'DUType'"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ndus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'NDUs'", 'blank': 'True'}),
            'pcntdus': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'PcntDUs'", 'blank': 'True'})
        },
        u'majitables.areadutypeslum': {
            'Meta': {'object_name': 'Areadutypeslum', 'db_table': "u'AreaDUTypeSlum'"},
            'dusinarea': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'DusInArea'", 'blank': 'True'}),
            'dutype': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'DUType'"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nareas': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'Nareas'", 'blank': 'True'}),
            'pcntdus': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'pcntDUs'", 'blank': 'True'}),
            'slumid': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'SlumID'", 'blank': 'True'}),
            'slumname': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'SlumName'"}),
            'smpdus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'SmpDUs'", 'blank': 'True'}),
            'totdus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'TotDUs'", 'blank': 'True'})
        },
        u'majitables.areadutypestructure': {
            'Meta': {'object_name': 'Areadutypestructure', 'db_table': "u'AreaDUTypeStructure'"},
            'areaid': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'AreaID'", 'blank': 'True'}),
            'areasmpdus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'AreaSmpDUs'", 'blank': 'True'}),
            'dustatus': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'DUStatus'"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ndus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'NDUs'", 'blank': 'True'}),
            'pcntdus': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'PcntDUs'", 'blank': 'True'})
        },
        u'majitables.areadutypetown': {
            'Meta': {'object_name': 'Areadutypetown', 'db_table': "u'AreaDUTypeTown'"},
            'dusinarea': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'DusInArea'", 'blank': 'True'}),
            'dutype': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'DUType'"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nareas': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'Nareas'", 'blank': 'True'}),
            'pcntdus': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'pcntDUs'", 'blank': 'True'}),
            'smpdus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'SmpDUs'", 'blank': 'True'}),
            'totdus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'TotDUs'", 'blank': 'True'}),
            'townid': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'TownID'", 'blank': 'True'}),
            'townname': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'TownName'"})
        },
        u'majitables.areadutypewsp': {
            'Meta': {'object_name': 'Areadutypewsp', 'db_table': "u'AreaDUTypeWSP'"},
            'dusinarea': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'DusInArea'", 'blank': 'True'}),
            'dutype': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'DUType'"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nareas': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'Nareas'", 'blank': 'True'}),
            'pcntdus': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'pcntDUs'", 'blank': 'True'}),
            'smpdus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'SmpDUs'", 'blank': 'True'}),
            'totdus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'TotDUs'", 'blank': 'True'}),
            'wspid': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'WspID'"}),
            'wspname': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'WspName'"})
        },
        u'majitables.areahabhsetypecounty': {
            'Meta': {'object_name': 'Areahabhsetypecounty', 'db_table': "u'AreaHabHseTypeCounty'"},
            'countyid': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'CountyID'", 'blank': 'True'}),
            'countyname': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'CountyName'"}),
            'hsngtype': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'HsngType'"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nareas': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'Nareas'", 'blank': 'True'}),
            'pcntareas': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'PcntAreas'", 'blank': 'True'}),
            'totareas': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'TotAreas'", 'blank': 'True'})
        },
        u'majitables.areahabhsetypeslum': {
            'Meta': {'object_name': 'Areahabhsetypeslum', 'db_table': "u'AreaHabHseTypeSlum'"},
            'hsngtype': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'HsngType'"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nareas': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'Nareas'", 'blank': 'True'}),
            'pcntareas': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'PcntAreas'", 'blank': 'True'}),
            'slumid': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'SlumID'", 'blank': 'True'}),
            'slumname': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'SlumName'"}),
            'totareas': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'TotAreas'", 'blank': 'True'})
        },
        u'majitables.areahabhsetypetown': {
            'Meta': {'object_name': 'Areahabhsetypetown', 'db_table': "u'AreaHabHseTypeTown'"},
            'hsngtype': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'HsngType'"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nareas': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'Nareas'", 'blank': 'True'}),
            'pcntareas': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'PcntAreas'", 'blank': 'True'}),
            'totareas': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'TotAreas'", 'blank': 'True'}),
            'townid': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'TownID'", 'blank': 'True'}),
            'townname': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'TownName'"})
        },
        u'majitables.areahabhsetypewsp': {
            'Meta': {'object_name': 'Areahabhsetypewsp', 'db_table': "u'AreaHabHseTypeWSP'"},
            'hsngtype': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'HsngType'"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nareas': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'Nareas'", 'blank': 'True'}),
            'pcntareas': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'PcntAreas'", 'blank': 'True'}),
            'totareas': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'TotAreas'", 'blank': 'True'}),
            'wspid': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'WspID'"}),
            'wspname': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'WspName'"})
        },
        u'majitables.areahabhsgsitcounty': {
            'Meta': {'object_name': 'Areahabhsgsitcounty', 'db_table': "u'AreaHabHsgSitCounty'"},
            'countyid': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'CountyID'", 'blank': 'True'}),
            'countyname': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'CountyName'"}),
            'hsgsituation': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'HsgSituation'"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nareas': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'Nareas'", 'blank': 'True'}),
            'pcntareas': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'PcntAreas'", 'blank': 'True'}),
            'totareas': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'TotAreas'", 'blank': 'True'})
        },
        u'majitables.areahabhsgsitslum': {
            'Meta': {'object_name': 'Areahabhsgsitslum', 'db_table': "u'AreaHabHsgSitSlum'"},
            'hsgsituation': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'HsgSituation'"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nareas': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'Nareas'", 'blank': 'True'}),
            'pcntareas': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'PcntAreas'"}),
            'slumid': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'SlumID'"}),
            'slumname': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'SlumName'"}),
            'totareas': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'TotAreas'"})
        },
        u'majitables.areahabhsgsittown': {
            'Meta': {'object_name': 'Areahabhsgsittown', 'db_table': "u'AreaHabHsgSitTown'"},
            'hsgsituation': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'HsgSituation'"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nareas': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'Nareas'", 'blank': 'True'}),
            'pcntareas': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'PcntAreas'", 'blank': 'True'}),
            'totareas': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'TotAreas'", 'blank': 'True'}),
            'townid': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'TownID'", 'blank': 'True'}),
            'townname': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'TownName'"})
        },
        u'majitables.areahabhsgsitwsp': {
            'Meta': {'object_name': 'Areahabhsgsitwsp', 'db_table': "u'AreaHabHsgSitWSP'"},
            'hsgsituation': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'HsgSituation'"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nareas': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'Nareas'", 'blank': 'True'}),
            'pcntareas': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'PcntAreas'", 'blank': 'True'}),
            'totareas': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'TotAreas'", 'blank': 'True'}),
            'wspid': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'WspID'"}),
            'wspname': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'WspName'"})
        },
        u'majitables.areahabroofcounty': {
            'Meta': {'object_name': 'Areahabroofcounty', 'db_table': "u'AreaHabRoofCounty'"},
            'countyid': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'CountyID'", 'blank': 'True'}),
            'countyname': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'CountyName'"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nareas': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'Nareas'", 'blank': 'True'}),
            'pcntareas': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'PcntAreas'", 'blank': 'True'}),
            'roof': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'Roof'"}),
            'totareas': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'TotAreas'", 'blank': 'True'})
        },
        u'majitables.areahabroofslum': {
            'Meta': {'object_name': 'Areahabroofslum', 'db_table': "u'AreaHabRoofSlum'"},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nareas': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'Nareas'", 'blank': 'True'}),
            'pcntareas': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'PcntAreas'"}),
            'roof': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'Roof'"}),
            'slumid': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'SlumID'"}),
            'slumname': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'SlumName'"}),
            'totareas': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'TotAreas'"})
        },
        u'majitables.areahabrooftown': {
            'Meta': {'object_name': 'Areahabrooftown', 'db_table': "u'AreaHabRoofTown'"},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nareas': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'Nareas'", 'blank': 'True'}),
            'pcntareas': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'PcntAreas'", 'blank': 'True'}),
            'roof': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'Roof'"}),
            'totareas': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'TotAreas'", 'blank': 'True'}),
            'townid': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'TownID'", 'blank': 'True'}),
            'townname': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'TownName'"})
        },
        u'majitables.areahabroofwsp': {
            'Meta': {'object_name': 'Areahabroofwsp', 'db_table': "u'AreaHabRoofWSP'"},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nareas': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'Nareas'", 'blank': 'True'}),
            'pcntareas': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'PcntAreas'", 'blank': 'True'}),
            'roof': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'Roof'"}),
            'totareas': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'TotAreas'", 'blank': 'True'}),
            'wspid': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'WspID'"}),
            'wspname': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'WspName'"})
        },
        u'majitables.areahabwallcounty': {
            'Meta': {'object_name': 'Areahabwallcounty', 'db_table': "u'AreaHabWallCounty'"},
            'countyid': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'CountyID'", 'blank': 'True'}),
            'countyname': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'CountyName'"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nareas': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'Nareas'", 'blank': 'True'}),
            'pcntareas': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'PcntAreas'", 'blank': 'True'}),
            'totareas': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'TotAreas'", 'blank': 'True'}),
            'wall': ('django.db.models.fields.CharField', [], {'max_length': '24', 'db_column': "u'Wall'"})
        },
        u'majitables.areahabwallslum': {
            'Meta': {'object_name': 'Areahabwallslum', 'db_table': "u'AreaHabWallSlum'"},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nareas': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'Nareas'", 'blank': 'True'}),
            'pcntareas': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'PcntAreas'", 'blank': 'True'}),
            'slumid': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'SlumID'"}),
            'slumname': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'SlumName'"}),
            'totareas': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'TotAreas'", 'blank': 'True'}),
            'wall': ('django.db.models.fields.CharField', [], {'max_length': '24', 'db_column': "u'Wall'"})
        },
        u'majitables.areahabwalltown': {
            'Meta': {'object_name': 'Areahabwalltown', 'db_table': "u'AreaHabWallTown'"},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nareas': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'Nareas'", 'blank': 'True'}),
            'pcntareas': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'PcntAreas'", 'blank': 'True'}),
            'totareas': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'TotAreas'", 'blank': 'True'}),
            'townid': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'TownID'", 'blank': 'True'}),
            'townname': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'TownName'"}),
            'wall': ('django.db.models.fields.CharField', [], {'max_length': '24', 'db_column': "u'Wall'"})
        },
        u'majitables.areahabwallwsp': {
            'Meta': {'object_name': 'Areahabwallwsp', 'db_table': "u'AreaHabWallWSP'"},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nareas': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'Nareas'", 'blank': 'True'}),
            'pcntareas': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'PcntAreas'", 'blank': 'True'}),
            'totareas': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'TotAreas'", 'blank': 'True'}),
            'wall': ('django.db.models.fields.CharField', [], {'max_length': '24', 'db_column': "u'Wall'"}),
            'wspid': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'WspID'"}),
            'wspname': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'WspName'"})
        },
        u'majitables.arealist': {
            'Meta': {'object_name': 'Arealist', 'db_table': "u'AreaList'"},
            'areaid': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'AreaID'", 'blank': 'True'}),
            'areaname': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'Areaname'"}),
            'areatype': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'Areatype'"}),
            'basedate': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'BaseDate'", 'blank': 'True'}),
            'decode': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'DEcode'"}),
            'dedate': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'DeDate'", 'blank': 'True'}),
            'dusample': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'DUsample'", 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'numdu': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'numDU'", 'blank': 'True'}),
            'numflats': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'numFlats'", 'blank': 'True'}),
            'numplots': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'numPlots'", 'blank': 'True'}),
            'remarks': ('django.db.models.fields.TextField', [], {'db_column': "u'Remarks'"}),
            'risk': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'Risk'"}),
            'slumid': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'Slumid'"}),
            'sublocid': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'SublocID'", 'blank': 'True'}),
            'townid': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'TownID'", 'blank': 'True'}),
            'wsp': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'WSP'"})
        },
        u'majitables.arealist2': {
            'Meta': {'object_name': 'Arealist2', 'db_table': "u'AreaList2'"},
            'areaid': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'AreaID'", 'blank': 'True'}),
            'areaname': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'Areaname'"}),
            'countyid': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'Countyid'", 'blank': 'True'}),
            'countyname': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'CountyName'"}),
            'distid': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'DistID'", 'blank': 'True'}),
            'distname': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'DistName'"}),
            'divid': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'DivID'", 'blank': 'True'}),
            'divname': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'DivName'"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'locid': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'locID'", 'blank': 'True'}),
            'locname': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'numdu': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'numDU'", 'blank': 'True'}),
            'provid': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'ProvId'", 'blank': 'True'}),
            'provname': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'slumid': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'Slumid'", 'blank': 'True'}),
            'slumname': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'SlumName'", 'blank': 'True'}),
            'sublocid': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'sublocID'", 'blank': 'True'}),
            'sublocname': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'totscore': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'TotScore'", 'blank': 'True'}),
            'townid': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'townID'", 'blank': 'True'}),
            'townname': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'wsbid': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'WSBID'", 'blank': 'True'}),
            'wsbname': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'WSBName'"}),
            'wspid': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'WSPID'"}),
            'wspname': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'WSPName'"})
        },
        u'majitables.areanospckskcounty': {
            'Meta': {'object_name': 'Areanospckskcounty', 'db_table': "u'AreaNoSpcKskCounty'"},
            'countyid': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'CountyID'", 'blank': 'True'}),
            'countyname': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'CountyName'"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nareas': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'Nareas'", 'blank': 'True'}),
            'pcntareas': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'PcntAreas'", 'blank': 'True'}),
            'spckiosk': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'SpcKiosk'"}),
            'totareas': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'TotAreas'", 'blank': 'True'})
        },
        u'majitables.areanospckskslum': {
            'Meta': {'object_name': 'Areanospckskslum', 'db_table': "u'AreaNoSpcKskSlum'"},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nareas': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'Nareas'", 'blank': 'True'}),
            'pcntareas': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'PcntAreas'"}),
            'slumid': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'SlumID'"}),
            'slumname': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'SlumName'"}),
            'spckiosk': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'SpcKiosk'"}),
            'totareas': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'TotAreas'"})
        },
        u'majitables.areanospcksktown': {
            'Meta': {'object_name': 'Areanospcksktown', 'db_table': "u'AreaNoSpcKskTown'"},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nareas': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'Nareas'", 'blank': 'True'}),
            'pcntareas': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'PcntAreas'", 'blank': 'True'}),
            'spckiosk': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'SpcKiosk'"}),
            'totareas': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'TotAreas'", 'blank': 'True'}),
            'townid': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'TownID'", 'blank': 'True'}),
            'townname': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'TownName'"})
        },
        u'majitables.areanospckskwsp': {
            'Meta': {'object_name': 'Areanospckskwsp', 'db_table': "u'AreaNoSpcKskWSP'"},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nareas': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'Nareas'", 'blank': 'True'}),
            'pcntareas': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'PcntAreas'", 'blank': 'True'}),
            'spckiosk': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'SpcKiosk'"}),
            'totareas': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'TotAreas'", 'blank': 'True'}),
            'wspid': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'WspID'"}),
            'wspname': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'WspName'"})
        },
        u'majitables.areanospcpubsancounty': {
            'Meta': {'object_name': 'Areanospcpubsancounty', 'db_table': "u'AreaNoSpcPubSanCounty'"},
            'countyid': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'CountyID'", 'blank': 'True'}),
            'countyname': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'CountyName'"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nareas': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'Nareas'", 'blank': 'True'}),
            'pcntareas': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'PcntAreas'", 'blank': 'True'}),
            'spcpubsan': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'SpcPubSan'"}),
            'totareas': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'TotAreas'", 'blank': 'True'})
        },
        u'majitables.areanospcpubsanslum': {
            'Meta': {'object_name': 'Areanospcpubsanslum', 'db_table': "u'AreaNoSpcPubSanSlum'"},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nareas': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'Nareas'", 'blank': 'True'}),
            'pcntareas': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'PcntAreas'"}),
            'slumid': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'SlumID'"}),
            'slumname': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'SlumName'"}),
            'spcpubsan': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'SpcPubSan'"}),
            'totareas': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'TotAreas'"})
        },
        u'majitables.areanospcpubsantown': {
            'Meta': {'object_name': 'Areanospcpubsantown', 'db_table': "u'AreaNoSpcPubSanTown'"},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nareas': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'Nareas'", 'blank': 'True'}),
            'pcntareas': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'PcntAreas'", 'blank': 'True'}),
            'spcpubsan': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'SpcPubSan'"}),
            'totareas': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'TotAreas'", 'blank': 'True'}),
            'townid': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'TownID'", 'blank': 'True'}),
            'townname': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'TownName'"})
        },
        u'majitables.areanospcpubsanwsp': {
            'Meta': {'object_name': 'Areanospcpubsanwsp', 'db_table': "u'AreaNoSpcPubSanWSP'"},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nareas': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'Nareas'", 'blank': 'True'}),
            'pcntareas': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'PcntAreas'", 'blank': 'True'}),
            'spcpubsan': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'SpcPubSan'"}),
            'totareas': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'TotAreas'", 'blank': 'True'}),
            'wspid': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'WspID'"}),
            'wspname': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'WspName'"})
        },
        u'majitables.areaownducounty': {
            'Meta': {'object_name': 'Areaownducounty', 'db_table': "u'AreaOwnDUCounty'"},
            'countyid': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'CountyID'", 'blank': 'True'}),
            'countyname': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'CountyName'"}),
            'dusinarea': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'DusInArea'", 'blank': 'True'}),
            'dusinsmp': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'DUsInSmp'", 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'owndu': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'OwnDU'"}),
            'pcntdus': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'pcntDUs'", 'blank': 'True'}),
            'pcntpop': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'PcntPop'", 'blank': 'True'}),
            'pop': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'Pop'", 'blank': 'True'}),
            'smpdus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'SmpDUs'", 'blank': 'True'}),
            'totalppleinarea': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'TotalPpleinArea'", 'blank': 'True'}),
            'totdus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'TotDUs'", 'blank': 'True'})
        },
        u'majitables.areaownduslum': {
            'Meta': {'object_name': 'Areaownduslum', 'db_table': "u'AreaOwnDUSlum'"},
            'dusinarea': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'DusInArea'", 'blank': 'True'}),
            'dusinsmp': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'DUsInSmp'", 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'owndu': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'OwnDU'"}),
            'pcntdus': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'pcntDUs'", 'blank': 'True'}),
            'pcntpop': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'PcntPop'", 'blank': 'True'}),
            'pop': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'Pop'", 'blank': 'True'}),
            'slumid': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'SlumID'", 'blank': 'True'}),
            'slumname': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'SlumName'"}),
            'smpdus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'SmpDUs'", 'blank': 'True'}),
            'totalppleinarea': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'TotalPpleinArea'", 'blank': 'True'}),
            'totdus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'TotDUs'", 'blank': 'True'})
        },
        u'majitables.areaowndutown': {
            'Meta': {'object_name': 'Areaowndutown', 'db_table': "u'AreaOwnDUTown'"},
            'dusinarea': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'DusInArea'", 'blank': 'True'}),
            'dusinsmp': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'DUsInSmp'", 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'owndu': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'OwnDU'"}),
            'pcntdus': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'pcntDUs'", 'blank': 'True'}),
            'pcntpop': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'PcntPop'", 'blank': 'True'}),
            'smpdus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'SmpDUs'", 'blank': 'True'}),
            'totalppleinarea': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'TotalPpleinArea'", 'blank': 'True'}),
            'totdus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'TotDUs'", 'blank': 'True'}),
            'townid': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'TownID'", 'blank': 'True'}),
            'townname': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'TownName'"})
        },
        u'majitables.areaownduwsp': {
            'Meta': {'object_name': 'Areaownduwsp', 'db_table': "u'AreaOwnDUWSP'"},
            'dusinarea': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'DusInArea'", 'blank': 'True'}),
            'dusinsmp': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'DUsInSmp'", 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'owndu': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'OwnDU'"}),
            'pcntdus': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'pcntDUs'", 'blank': 'True'}),
            'pcntpop': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'PcntPop'", 'blank': 'True'}),
            'pop': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'Pop'", 'blank': 'True'}),
            'smpdus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'SmpDUs'", 'blank': 'True'}),
            'totalppleinarea': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'TotalPpleinArea'", 'blank': 'True'}),
            'totdus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'TotDUs'", 'blank': 'True'}),
            'wspid': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'WSPID'"}),
            'wspname': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'WSPName'"})
        },
        u'majitables.areaphychar': {
            'Meta': {'object_name': 'Areaphychar', 'db_table': "u'AreaPhyChar'"},
            'adist': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'ADist'", 'blank': 'True'}),
            'areaid': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'AreaID'", 'blank': 'True'}),
            'arealocation': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'AreaLocation'"}),
            'areaname': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'Areaname'"}),
            'areatopology': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'AreaTopology'", 'blank': 'True'}),
            'areatype': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'AreaType'"}),
            'flooding': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'Flooding'"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'legalised': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'Legalised'"}),
            'settlement': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'Settlement'"}),
            'soil': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'Soil'"}),
            'soilselfsupporting': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'SoilSelfSupporting'"}),
            'townname': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'watertabledry': ('django.db.models.fields.CharField', [], {'max_length': '29', 'db_column': "u'WaterTableDry'"}),
            'watertablerainy': ('django.db.models.fields.CharField', [], {'max_length': '29', 'db_column': "u'WaterTableRainy'"}),
            'yrlegalised': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'YrLegalised'"})
        },
        u'majitables.areapop': {
            'Meta': {'object_name': 'Areapop', 'db_table': "u'AreaPop'"},
            'area': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'Area'", 'blank': 'True'}),
            'areaname': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'Areaname'"}),
            'areapop': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'AreaPop'", 'blank': 'True'}),
            'areasmpdus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'AreaSmpDUs'", 'blank': 'True'}),
            'areasmppop': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'AreaSmpPop'", 'blank': 'True'}),
            'avgdusz': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'AvgDUSz'", 'blank': 'True'}),
            'avgfhhh': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'AvgFHHH'", 'blank': 'True'}),
            'avghhsdu': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'AvgHHsDU'", 'blank': 'True'}),
            'avghhsz': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'AvgHHSz'", 'blank': 'True'}),
            'basedate': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'BaseDate'", 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'maxdusz': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'MaxDUSz'", 'blank': 'True'}),
            'mindusz': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'MinDUSz'", 'blank': 'True'}),
            'numdu': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'NumDU'", 'blank': 'True'}),
            'pcntfhhh': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'PcntFHHH'", 'blank': 'True'}),
            'popunit': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'PopUnit'"}),
            'smpfhhh': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'SmpFHHH'", 'blank': 'True'}),
            'sublocpop': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'SubLocPop'", 'blank': 'True'}),
            'tothhs': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'TotHHs'", 'blank': 'True'})
        },
        u'majitables.areapopdensity': {
            'Meta': {'object_name': 'Areapopdensity', 'db_table': "u'AreaPopDensity'"},
            'area': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'Area'", 'blank': 'True'}),
            'areaname': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'Areaname'"}),
            'areapop': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'AreaPop'", 'blank': 'True'}),
            'basedate': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'BaseDate'", 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'popden': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'PopDen'"}),
            'popdensity': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'PopDensity'", 'blank': 'True'}),
            'sqkm': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'SqKm'", 'blank': 'True'})
        },
        u'majitables.areaprofiles': {
            'Meta': {'object_name': 'Areaprofiles', 'db_table': "u'AreaProfiles'"},
            'alayout': ('django.db.models.fields.TextField', [], {'db_column': "u'ALayout'"}),
            'alocation': ('django.db.models.fields.TextField', [], {'db_column': "u'ALocation'"}),
            'amainproblems': ('django.db.models.fields.TextField', [], {'db_column': "u'AmainProblems'"}),
            'apbhealthrisks': ('django.db.models.fields.TextField', [], {'db_column': "u'ApbHealthRisks'"}),
            'areaid': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'AreaID'", 'blank': 'True'}),
            'areaname': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'Areaname'"}),
            'asanitation': ('django.db.models.fields.TextField', [], {'db_column': "u'Asanitation'"}),
            'asolidwaste': ('django.db.models.fields.TextField', [], {'db_column': "u'Asolidwaste'"}),
            'aurbandev': ('django.db.models.fields.TextField', [], {'db_column': "u'AUrbanDev'"}),
            'awater': ('django.db.models.fields.TextField', [], {'db_column': "u'AWater'"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'townname': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'majitables.areassettlocrdrlcounty': {
            'Meta': {'object_name': 'Areassettlocrdrlcounty', 'db_table': "u'AreasSettLocRdRlCounty'"},
            'arealocation': ('django.db.models.fields.CharField', [], {'max_length': '35', 'db_column': "u'Arealocation'"}),
            'countyid': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'Countyid'", 'blank': 'True'}),
            'countyname': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'CountyName'"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nareas': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'Nareas'", 'blank': 'True'}),
            'numareas': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'NumAreas'", 'blank': 'True'}),
            'pcntareas': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'PcntAreas'", 'blank': 'True'})
        },
        u'majitables.areassettlocrdrlslum': {
            'Meta': {'object_name': 'Areassettlocrdrlslum', 'db_table': "u'AreasSettLocRdRlSlum'"},
            'arealocation': ('django.db.models.fields.CharField', [], {'max_length': '35', 'db_column': "u'Arealocation'"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nareas': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'Nareas'", 'blank': 'True'}),
            'numareas': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'NumAreas'", 'blank': 'True'}),
            'pcntareas': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'PcntAreas'", 'blank': 'True'}),
            'slumid': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'Slumid'", 'blank': 'True'}),
            'slumname': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'SlumName'"})
        },
        u'majitables.areassettlocrdrltown': {
            'Meta': {'object_name': 'Areassettlocrdrltown', 'db_table': "u'AreasSettLocRdRlTown'"},
            'arealocation': ('django.db.models.fields.CharField', [], {'max_length': '35', 'db_column': "u'Arealocation'"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nareas': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'Nareas'", 'blank': 'True'}),
            'numareas': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'NumAreas'", 'blank': 'True'}),
            'pcntareas': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'PcntAreas'", 'blank': 'True'}),
            'townid': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'Townid'", 'blank': 'True'}),
            'townname': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'TownName'"})
        },
        u'majitables.areassettlocrdrlwsp': {
            'Meta': {'object_name': 'Areassettlocrdrlwsp', 'db_table': "u'AreasSettLocRdRlWSP'"},
            'arealocation': ('django.db.models.fields.CharField', [], {'max_length': '35', 'db_column': "u'Arealocation'"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nareas': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'Nareas'", 'blank': 'True'}),
            'numareas': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'NumAreas'", 'blank': 'True'}),
            'pcntareas': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'PcntAreas'", 'blank': 'True'}),
            'wspid': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'WSPid'"}),
            'wspname': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'WSPName'"})
        },
        u'majitables.areasubjfldcounty': {
            'Meta': {'object_name': 'Areasubjfldcounty', 'db_table': "u'AreaSubjFldCounty'"},
            'countyid': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'CountyID'", 'blank': 'True'}),
            'countyname': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'CountyName'"}),
            'flooding': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'Flooding'"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nareas': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'Nareas'", 'blank': 'True'}),
            'numareas': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'NumAreas'", 'blank': 'True'}),
            'pcntareas': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'PcntAreas'", 'blank': 'True'})
        },
        u'majitables.areasubjfldslum': {
            'Meta': {'object_name': 'Areasubjfldslum', 'db_table': "u'AreaSubjFldSlum'"},
            'flooding': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'Flooding'"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nareas': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'Nareas'", 'blank': 'True'}),
            'numareas': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'NumAreas'", 'blank': 'True'}),
            'pcntareas': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'PcntAreas'", 'blank': 'True'}),
            'slumid': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'SlumID'", 'blank': 'True'}),
            'slumname': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'SlumName'"})
        },
        u'majitables.areasubjfldtown': {
            'Meta': {'object_name': 'Areasubjfldtown', 'db_table': "u'AreaSubjFldTown'"},
            'flooding': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'Flooding'"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nareas': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'Nareas'", 'blank': 'True'}),
            'numareas': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'NumAreas'", 'blank': 'True'}),
            'pcntareas': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'PcntAreas'", 'blank': 'True'}),
            'townid': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'TownID'", 'blank': 'True'}),
            'townname': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'TownName'"})
        },
        u'majitables.areasubjfldwsp': {
            'Meta': {'object_name': 'Areasubjfldwsp', 'db_table': "u'AreaSubjFldWSP'"},
            'flooding': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'Flooding'"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nareas': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'Nareas'", 'blank': 'True'}),
            'numareas': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'NumAreas'", 'blank': 'True'}),
            'pcntareas': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'PcntAreas'", 'blank': 'True'}),
            'wspid': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'WspID'"}),
            'wspname': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'WspName'"})
        },
        u'majitables.areasummarysheet': {
            'Meta': {'object_name': 'Areasummarysheet', 'db_table': "u'AreaSummarySheet'"},
            'areaid': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'AreaID'", 'blank': 'True'}),
            'arealinkedsew': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'AreaLinkedSew'"}),
            'arealinkedwater': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'AreaLinkedWater'"}),
            'areaname': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'Areaname'"}),
            'areapop': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'AreaPop'", 'blank': 'True'}),
            'areatype': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'AreaType'"}),
            'communityschm': ('django.db.models.fields.TextField', [], {'db_column': "u'CommunitySchm'"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nadeqsupplied': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'NAdeqSupplied'", 'blank': 'True'}),
            'pcntppleimpsan': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'PcntPpleImpSan'", 'blank': 'True'}),
            'pcntppleothcon': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'PcntPpleOthCon'", 'blank': 'True'}),
            'pcntpplereseller': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'PcntPPleReseller'", 'blank': 'True'}),
            'pcntppleusingimpsrcwstf': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'PcntPpleUsingImpSrcWSTF'", 'blank': 'True'}),
            'popdensity': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'PopDensity'", 'blank': 'True'}),
            'sqkm': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'SqKm'", 'blank': 'True'}),
            'sublocname': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'wspname': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'WSPName'"}),
            'wsupplyproj': ('django.db.models.fields.TextField', [], {'db_column': "u'WsupplyProj'"})
        },
        u'majitables.demogtrends': {
            'Meta': {'object_name': 'Demogtrends', 'db_table': "u'DemogTrends'"},
            'areaid': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'AreaID'", 'blank': 'True'}),
            'daypop': ('django.db.models.fields.TextField', [], {'db_column': "u'DayPop'"}),
            'demogdev': ('django.db.models.fields.TextField', [], {'db_column': "u'DemogDev'"}),
            'demogtrend': ('django.db.models.fields.TextField', [], {'db_column': "u'Demogtrend'"}),
            'factors': ('django.db.models.fields.TextField', [], {'db_column': "u'Factors'"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'popdensity': ('django.db.models.fields.TextField', [], {'db_column': "u'PopDensity'"}),
            'popgrwth': ('django.db.models.fields.TextField', [], {'db_column': "u'PopGrwth'"})
        },
        u'majitables.devplans': {
            'Meta': {'object_name': 'Devplans', 'db_table': "u'DevPlans'"},
            'areaid': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'AreaID'", 'blank': 'True'}),
            'devactivities': ('django.db.models.fields.TextField', [], {'db_column': "u'DevActivities'"}),
            'devplan': ('django.db.models.fields.TextField', [], {'db_column': "u'DevPlan'"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'laplan': ('django.db.models.fields.TextField', [], {'db_column': "u'LAPlan'"})
        },
        u'majitables.femhhhscounty': {
            'Meta': {'object_name': 'Femhhhscounty', 'db_table': "u'FemHHHsCounty'"},
            'areasmpdus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'AreaSmpDUs'", 'blank': 'True'}),
            'areasmppop': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'AreaSmpPop'", 'blank': 'True'}),
            'avgdusz': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'AvgDUSz'", 'blank': 'True'}),
            'avgfhhh': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'AvgFHHH'", 'blank': 'True'}),
            'avghhsdu': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'AvgHHsDU'", 'blank': 'True'}),
            'avghhsz': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'AvgHHSz'", 'blank': 'True'}),
            'countyid': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'CountyID'", 'blank': 'True'}),
            'countyname': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'CountyName'"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'maxdusz': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'MaxDUSz'", 'blank': 'True'}),
            'mindusz': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'MinDUSz'", 'blank': 'True'}),
            'pcntfhhh': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'PcntFHHH'", 'blank': 'True'}),
            'smpfhhh': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'SmpFHHH'", 'blank': 'True'}),
            'tothhs': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'TotHHs'", 'blank': 'True'})
        },
        u'majitables.femhhhsslum': {
            'Meta': {'object_name': 'Femhhhsslum', 'db_table': "u'FemHHHsSlum'"},
            'areasmpdus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'AreaSmpDUs'", 'blank': 'True'}),
            'areasmppop': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'AreaSmpPop'", 'blank': 'True'}),
            'avgdusz': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'AvgDUSz'", 'blank': 'True'}),
            'avgfhhh': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'AvgFHHH'", 'blank': 'True'}),
            'avghhsdu': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'AvgHHsDU'", 'blank': 'True'}),
            'avghhsz': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'AvgHHSz'", 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'maxdusz': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'MaxDUSz'", 'blank': 'True'}),
            'mindusz': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'MinDUSz'", 'blank': 'True'}),
            'pcntfhhh': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'PcntFHHH'", 'blank': 'True'}),
            'slumid': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'SlumID'"}),
            'slumname': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'SlumName'"}),
            'smpfhhh': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'SmpFHHH'", 'blank': 'True'}),
            'tothhs': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'TotHHs'", 'blank': 'True'})
        },
        u'majitables.femhhhstown': {
            'Meta': {'object_name': 'Femhhhstown', 'db_table': "u'FemHHHsTown'"},
            'areasmpdus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'AreaSmpDUs'", 'blank': 'True'}),
            'areasmppop': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'AreaSmpPop'", 'blank': 'True'}),
            'avgdusz': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'AvgDUSz'", 'blank': 'True'}),
            'avgfhhh': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'AvgFHHH'", 'blank': 'True'}),
            'avghhsdu': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'AvgHHsDU'", 'blank': 'True'}),
            'avghhsz': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'AvgHHSz'", 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'maxdusz': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'MaxDUSz'", 'blank': 'True'}),
            'mindusz': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'MinDUSz'", 'blank': 'True'}),
            'pcntfhhh': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'PcntFHHH'", 'blank': 'True'}),
            'smpfhhh': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'SmpFHHH'", 'blank': 'True'}),
            'tothhs': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'TotHHs'", 'blank': 'True'}),
            'townid': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'TownID'", 'blank': 'True'}),
            'townname': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'TownName'"})
        },
        u'majitables.habitationpatterns': {
            'Meta': {'object_name': 'Habitationpatterns', 'db_table': "u'HabitationPatterns'"},
            'areaid': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'AreaID'", 'blank': 'True'}),
            'areaname': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'Areaname'"}),
            'hseroof': ('django.db.models.fields.TextField', [], {'db_column': "u'HseRoof'"}),
            'hsetype': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'HseType'"}),
            'hsewall': ('django.db.models.fields.TextField', [], {'db_column': "u'HseWall'"}),
            'hsgsituation': ('django.db.models.fields.TextField', [], {'db_column': "u'HsgSituation'"}),
            'hsngchar': ('django.db.models.fields.TextField', [], {'db_column': "u'HsngChar'"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'majitables.landownuse': {
            'Meta': {'object_name': 'Landownuse', 'db_table': "u'LandOwnUse'"},
            'areaid': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'AreaID'", 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'landownership': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'LandOwnership'"}),
            'landuse': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'Landuse'"}),
            'pubspace': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'PubSpace'"}),
            'rdrsrv': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'RdRsrv'"}),
            'spckiosk': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'SpcKiosk'"}),
            'spcprvsan': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'SpcPrvSan'"}),
            'spcpubsan': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'SpcPubSan'"}),
            'spcwaterext': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'SpcWaterExt'"})
        },
        u'majitables.majidatainfocounty': {
            'Meta': {'object_name': 'Majidatainfocounty', 'db_table': "u'MajidataInfoCounty'"},
            'countyid': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'countyID'", 'blank': 'True'}),
            'countyname': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nareas': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'NAreas'", 'blank': 'True'}),
            'ndus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'NDUs'", 'blank': 'True'}),
            'pcntdusinterv': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'PcntDUsInterv'", 'blank': 'True'}),
            'pcntpopinterviewed': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'PcntPopInterviewed'", 'blank': 'True'}),
            'pop': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'Pop'", 'blank': 'True'}),
            'smpdus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'SmpDUs'", 'blank': 'True'}),
            'smppop': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'SmpPop'", 'blank': 'True'})
        },
        u'majitables.majidatainfoslum': {
            'Meta': {'object_name': 'Majidatainfoslum', 'db_table': "u'MajidataInfoSlum'"},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nareas': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'NAreas'", 'blank': 'True'}),
            'ndus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'NDUs'", 'blank': 'True'}),
            'pcntdusinterv': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'PcntDUsInterv'", 'blank': 'True'}),
            'pcntpopinterviewed': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'PcntPopInterviewed'", 'blank': 'True'}),
            'pop': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'Pop'", 'blank': 'True'}),
            'slumid': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'slumID'"}),
            'slumname': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'smpdus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'SmpDUs'", 'blank': 'True'}),
            'smppop': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'SmpPop'", 'blank': 'True'})
        },
        u'majitables.majidatainfotwn': {
            'Meta': {'object_name': 'Majidatainfotwn', 'db_table': "u'MajidataInfoTwn'"},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nareas': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'NAreas'", 'blank': 'True'}),
            'ndus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'NDUs'", 'blank': 'True'}),
            'pcntdusinterv': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'PcntDUsInterv'", 'blank': 'True'}),
            'pcntpopinterviewed': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'PcntPopInterviewed'", 'blank': 'True'}),
            'pop': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'Pop'", 'blank': 'True'}),
            'smpdus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'SmpDUs'", 'blank': 'True'}),
            'smppop': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'SmpPop'", 'blank': 'True'}),
            'townid': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'townID'", 'blank': 'True'}),
            'townname': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'majitables.majidatainfowsp': {
            'Meta': {'object_name': 'Majidatainfowsp', 'db_table': "u'MajidataInfoWSP'"},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nareas': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'NAreas'", 'blank': 'True'}),
            'ndus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'NDUs'", 'blank': 'True'}),
            'pcntdusinterv': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'PcntDUsInterv'", 'blank': 'True'}),
            'pcntpopinterviewed': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'PcntPopInterviewed'", 'blank': 'True'}),
            'pop': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'Pop'", 'blank': 'True'}),
            'smpdus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'SmpDUs'", 'blank': 'True'}),
            'smppop': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'SmpPop'", 'blank': 'True'}),
            'wspid': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'wspID'"}),
            'wspname': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'majitables.pavghhduszcounty': {
            'Meta': {'object_name': 'Pavghhduszcounty', 'db_table': "u'PAvgHHDUSzCounty'"},
            'areasmpdus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'AreaSmpDUs'", 'blank': 'True'}),
            'areasmppop': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'AreaSmpPop'", 'blank': 'True'}),
            'avgdusz': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'AvgDUSz'", 'blank': 'True'}),
            'avgfhhh': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'AvgFHHH'", 'blank': 'True'}),
            'avghhsdu': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'AvgHHsDU'", 'blank': 'True'}),
            'avghhsz': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'AvgHHSz'", 'blank': 'True'}),
            'countyid': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'CountyID'", 'blank': 'True'}),
            'countyname': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'CountyName'"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'maxdusz': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'MaxDUSz'", 'blank': 'True'}),
            'mindusz': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'MinDUSz'", 'blank': 'True'}),
            'tothhs': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'TotHHs'", 'blank': 'True'})
        },
        u'majitables.pavghhduszslum': {
            'Meta': {'object_name': 'Pavghhduszslum', 'db_table': "u'PAvgHHDUSzSlum'"},
            'areasmpdus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'AreaSmpDUs'", 'blank': 'True'}),
            'areasmppop': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'AreaSmpPop'", 'blank': 'True'}),
            'avgdusz': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'AvgDUSz'", 'blank': 'True'}),
            'avghhsdu': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'AvgHHsDU'", 'blank': 'True'}),
            'avghhsz': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'AvgHHSz'", 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'maxdusz': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'MaxDUSz'", 'blank': 'True'}),
            'mindusz': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'MinDUSz'", 'blank': 'True'}),
            'slumid': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'SlumID'"}),
            'slumname': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'SlumName'"}),
            'tothhs': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'TotHHs'", 'blank': 'True'})
        },
        u'majitables.pavghhdusztown': {
            'Meta': {'object_name': 'Pavghhdusztown', 'db_table': "u'PAvgHHDUSzTown'"},
            'areasmpdus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'AreaSmpDUs'", 'blank': 'True'}),
            'areasmppop': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'AreaSmpPop'", 'blank': 'True'}),
            'avgdusz': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'AvgDUSz'", 'blank': 'True'}),
            'avgfhhh': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'AvgFHHH'", 'blank': 'True'}),
            'avghhsdu': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'AvgHHsDU'", 'blank': 'True'}),
            'avghhsz': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'AvgHHSz'", 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'maxdusz': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'MaxDUSz'", 'blank': 'True'}),
            'mindusz': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'MinDUSz'", 'blank': 'True'}),
            'tothhs': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'TotHHs'", 'blank': 'True'}),
            'townid': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'TownID'", 'blank': 'True'}),
            'townname': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'TownName'"})
        },
        u'majitables.phlthwasterds': {
            'Meta': {'object_name': 'Phlthwasterds', 'db_table': "u'PHlthWasteRds'"},
            'areaid': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'AreaID'", 'blank': 'True'}),
            'areaname': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'Areaname'"}),
            'draintypes': ('django.db.models.fields.TextField', [], {'db_column': "u'DrainTypes'"}),
            'drnstatus': ('django.db.models.fields.TextField', [], {'db_column': "u'DrnStatus'"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mnphproblem': ('django.db.models.fields.TextField', [], {'db_column': "u'MnPHProblem'"}),
            'mnswdisp': ('django.db.models.fields.TextField', [], {'db_column': "u'MnSWDisp'"}),
            'phsit': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'PHSit'"}),
            'rdtechstatus': ('django.db.models.fields.TextField', [], {'db_column': "u'RdTechStatus'"}),
            'roadtypes': ('django.db.models.fields.TextField', [], {'db_column': "u'RoadTypes'"}),
            'swsit': ('django.db.models.fields.TextField', [], {'db_column': "u'SWSit'"})
        },
        u'majitables.popareabysettlementcounty': {
            'Meta': {'object_name': 'Popareabysettlementcounty', 'db_table': "u'PopAreaBySettlementCounty'"},
            'countyid': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'Countyid'", 'blank': 'True'}),
            'countyname': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'CountyName'"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nareas': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'NAreas'", 'blank': 'True'}),
            'pcntareas': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'PcntAreas'", 'blank': 'True'}),
            'pcntpop': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'PcntPop'", 'blank': 'True'}),
            'pop': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'Pop'", 'blank': 'True'}),
            'settlement': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'Settlement'"}),
            'totareas': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'TotAreas'", 'blank': 'True'}),
            'totpop': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'TotPop'", 'blank': 'True'})
        },
        u'majitables.popareabysettlementslum': {
            'Meta': {'object_name': 'Popareabysettlementslum', 'db_table': "u'PopAreaBySettlementSlum'"},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nareas': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'NAreas'", 'blank': 'True'}),
            'pcntareas': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'PcntAreas'", 'blank': 'True'}),
            'pcntpop': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'PcntPop'", 'blank': 'True'}),
            'pop': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'Pop'", 'blank': 'True'}),
            'settlement': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'Settlement'"}),
            'slumid': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'Slumid'", 'blank': 'True'}),
            'slumname': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'SlumName'"}),
            'totareas': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'TotAreas'", 'blank': 'True'}),
            'totpop': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'TotPop'", 'blank': 'True'})
        },
        u'majitables.popareabysettlementtown': {
            'Meta': {'object_name': 'Popareabysettlementtown', 'db_table': "u'PopAreaBySettlementTown'"},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nareas': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'NAreas'", 'blank': 'True'}),
            'pcntareas': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'PcntAreas'", 'blank': 'True'}),
            'pcntpop': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'PcntPop'", 'blank': 'True'}),
            'pop': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'Pop'", 'blank': 'True'}),
            'settlement': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'Settlement'"}),
            'totareas': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'TotAreas'", 'blank': 'True'}),
            'totpop': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'TotPop'", 'blank': 'True'}),
            'townid': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'Townid'", 'blank': 'True'}),
            'townname': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'TownName'"})
        },
        u'majitables.popareasbylegalcounty': {
            'Meta': {'object_name': 'Popareasbylegalcounty', 'db_table': "u'PopAreasByLegalCounty'"},
            'avgpopperarea': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'AvgPopPerArea'", 'blank': 'True'}),
            'countyid': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'Countyid'", 'blank': 'True'}),
            'countyname': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'CountyName'"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'legalstatus': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'LegalStatus'"}),
            'nareas': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'NAreas'", 'blank': 'True'}),
            'pcntareas': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'PcntAreas'", 'blank': 'True'}),
            'pop': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'Pop'", 'blank': 'True'}),
            'totareas': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'TotAreas'", 'blank': 'True'})
        },
        u'majitables.popareasbylegalslum': {
            'Meta': {'object_name': 'Popareasbylegalslum', 'db_table': "u'PopAreasByLegalSlum'"},
            'avgpopperarea': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'AvgPopPerArea'", 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'legalstatus': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'LegalStatus'"}),
            'nareas': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'NAreas'", 'blank': 'True'}),
            'pcntareas': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'PcntAreas'", 'blank': 'True'}),
            'pop': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'Pop'", 'blank': 'True'}),
            'slumid': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'Slumid'", 'blank': 'True'}),
            'slumname': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'SlumName'"}),
            'totareas': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'TotAreas'", 'blank': 'True'})
        },
        u'majitables.popareasbylegaltown': {
            'Meta': {'object_name': 'Popareasbylegaltown', 'db_table': "u'PopAreasByLegalTown'"},
            'avgpopperarea': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'AvgPopPerArea'", 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'legalstatus': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'LegalStatus'"}),
            'nareas': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'NAreas'", 'blank': 'True'}),
            'pcntareas': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'PcntAreas'", 'blank': 'True'}),
            'pop': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'Pop'", 'blank': 'True'}),
            'totareas': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'TotAreas'", 'blank': 'True'}),
            'townid': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'Townid'", 'blank': 'True'}),
            'townname': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'TownName'"})
        },
        u'majitables.popareatypecounty': {
            'Meta': {'object_name': 'Popareatypecounty', 'db_table': "u'PopAreaTypeCounty'"},
            'areatype': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'AreaType'"}),
            'countyid': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'CountyID'", 'blank': 'True'}),
            'countyname': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'CountyName'"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nareas': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'Nareas'", 'blank': 'True'}),
            'pop': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'Pop'", 'blank': 'True'})
        },
        u'majitables.popareatypeslum': {
            'Meta': {'object_name': 'Popareatypeslum', 'db_table': "u'PopAreaTypeSlum'"},
            'areatype': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'AreaType'"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nareas': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'Nareas'", 'blank': 'True'}),
            'pop': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'Pop'", 'blank': 'True'}),
            'slumid': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'SlumID'"}),
            'slumname': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'SlumName'"})
        },
        u'majitables.popareatypetown': {
            'Meta': {'object_name': 'Popareatypetown', 'db_table': "u'PopAreaTypeTown'"},
            'areatype': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'AreaType'"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nareas': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'Nareas'", 'blank': 'True'}),
            'pop': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'Pop'", 'blank': 'True'}),
            'townid': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'TownID'", 'blank': 'True'}),
            'townname': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'TownName'"})
        },
        u'majitables.popareatypewsp': {
            'Meta': {'object_name': 'Popareatypewsp', 'db_table': "u'PopAreaTypeWSP'"},
            'areatype': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'AreaType'"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nareas': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'Nareas'", 'blank': 'True'}),
            'pop': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'Pop'", 'blank': 'True'}),
            'wspid': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'WspID'"}),
            'wspname': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'WspName'"})
        },
        u'majitables.pownduwsrckskcounty': {
            'Meta': {'object_name': 'Pownduwsrckskcounty', 'db_table': "u'POwnDUWSrcKskCounty'"},
            'countyid': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'CountyID'", 'blank': 'True'}),
            'countyname': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'CountyName'"}),
            'dusinarea': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'DusInArea'", 'blank': 'True'}),
            'dusinsmp': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'DUsInSmp'", 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'owndu': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'OwnDU'"}),
            'pcntdus': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'pcntDUs'", 'blank': 'True'}),
            'pcntpop': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'PcntPop'", 'blank': 'True'}),
            'pop': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'Pop'", 'blank': 'True'}),
            'smpdus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'SmpDUs'", 'blank': 'True'}),
            'totalppleinarea': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'TotalPpleinArea'", 'blank': 'True'}),
            'totdus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'TotDUs'", 'blank': 'True'})
        },
        u'majitables.pownduwsrckskslum': {
            'Meta': {'object_name': 'Pownduwsrckskslum', 'db_table': "u'POwnDUWSrcKskSlum'"},
            'dusinarea': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'DusInArea'", 'blank': 'True'}),
            'dusinsmp': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'DUsInSmp'", 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'owndu': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'OwnDU'"}),
            'pcntdus': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'pcntDUs'", 'blank': 'True'}),
            'pcntpop': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'PcntPop'", 'blank': 'True'}),
            'pop': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'Pop'", 'blank': 'True'}),
            'slumid': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'SlumID'", 'blank': 'True'}),
            'slumname': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'SlumName'"}),
            'smpdus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'SmpDUs'", 'blank': 'True'}),
            'totalppleinarea': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'TotalPpleinArea'", 'blank': 'True'}),
            'totdus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'TotDUs'", 'blank': 'True'})
        },
        u'majitables.pownduwsrcksktown': {
            'Meta': {'object_name': 'Pownduwsrcksktown', 'db_table': "u'POwnDUWSrcKskTown'"},
            'dusinarea': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'DusInArea'", 'blank': 'True'}),
            'dusinsmp': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'DUsInSmp'", 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'owndu': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'OwnDU'"}),
            'pcntdus': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'pcntDUs'", 'blank': 'True'}),
            'pcntpop': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'PcntPop'", 'blank': 'True'}),
            'pop': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'Pop'", 'blank': 'True'}),
            'smpdus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'SmpDUs'", 'blank': 'True'}),
            'totalppleinarea': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'TotalPpleinArea'", 'blank': 'True'}),
            'totdus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'TotDUs'", 'blank': 'True'}),
            'townid': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'TownID'", 'blank': 'True'}),
            'townname': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'TownName'"})
        },
        u'majitables.pownduwsrckskwsp': {
            'Meta': {'object_name': 'Pownduwsrckskwsp', 'db_table': "u'POwnDUWSrcKskWSP'"},
            'dusinarea': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'DusInArea'", 'blank': 'True'}),
            'dusinsmp': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'DUsInSmp'", 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'owndu': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'OwnDU'"}),
            'pcntdus': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'pcntDUs'", 'blank': 'True'}),
            'pcntpop': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'PcntPop'", 'blank': 'True'}),
            'pop': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'Pop'", 'blank': 'True'}),
            'smpdus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'SmpDUs'", 'blank': 'True'}),
            'totalppleinarea': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'TotalPpleinArea'", 'blank': 'True'}),
            'totdus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'TotDUs'", 'blank': 'True'}),
            'wspid': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'WspID'"}),
            'wspname': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'WspName'"})
        },
        u'majitables.pownduwsrcpipedcounty': {
            'Meta': {'object_name': 'Pownduwsrcpipedcounty', 'db_table': "u'POwnDUWSrcPipedCounty'"},
            'countyid': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'CountyID'", 'blank': 'True'}),
            'countyname': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'CountyName'"}),
            'dusinarea': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'DusInArea'", 'blank': 'True'}),
            'dusinsmp': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'DUsInSmp'", 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'owndu': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'OwnDU'"}),
            'pcntdus': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'pcntDUs'", 'blank': 'True'}),
            'pcntpop': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'PcntPop'", 'blank': 'True'}),
            'pop': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'Pop'", 'blank': 'True'}),
            'smpdus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'SmpDUs'", 'blank': 'True'}),
            'totalppleinarea': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'TotalPpleinArea'", 'blank': 'True'}),
            'totdus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'TotDUs'", 'blank': 'True'})
        },
        u'majitables.pownduwsrcpipedslum': {
            'Meta': {'object_name': 'Pownduwsrcpipedslum', 'db_table': "u'POwnDUWSrcPipedSlum'"},
            'dusinarea': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'DusInArea'", 'blank': 'True'}),
            'dusinsmp': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'DUsInSmp'", 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'owndu': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'OwnDU'"}),
            'pcntdus': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'pcntDUs'", 'blank': 'True'}),
            'pcntpop': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'PcntPop'", 'blank': 'True'}),
            'pop': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'Pop'", 'blank': 'True'}),
            'slumid': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'SlumID'", 'blank': 'True'}),
            'slumname': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'SlumName'"}),
            'smpdus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'SmpDUs'", 'blank': 'True'}),
            'totalppleinarea': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'TotalPpleinArea'", 'blank': 'True'}),
            'totdus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'TotDUs'", 'blank': 'True'})
        },
        u'majitables.pownduwsrcpipedtown': {
            'Meta': {'object_name': 'Pownduwsrcpipedtown', 'db_table': "u'POwnDUWSrcPipedTown'"},
            'dusinarea': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'DusInArea'", 'blank': 'True'}),
            'dusinsmp': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'DUsInSmp'", 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'owndu': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'OwnDU'"}),
            'pcntdus': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'pcntDUs'", 'blank': 'True'}),
            'pcntpop': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'PcntPop'", 'blank': 'True'}),
            'pop': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'Pop'", 'blank': 'True'}),
            'smpdus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'SmpDUs'", 'blank': 'True'}),
            'totalppleinarea': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'TotalPpleinArea'", 'blank': 'True'}),
            'totdus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'TotDUs'", 'blank': 'True'}),
            'townid': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'TownID'", 'blank': 'True'}),
            'townname': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'TownName'"})
        },
        u'majitables.pownduwsrcpipedwsp': {
            'Meta': {'object_name': 'Pownduwsrcpipedwsp', 'db_table': "u'POwnDUWSrcPipedWSP'"},
            'dusinarea': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'DusInArea'", 'blank': 'True'}),
            'dusinsmp': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'DUsInSmp'", 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'owndu': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'OwnDU'"}),
            'pcntdus': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'pcntDUs'", 'blank': 'True'}),
            'pcntpop': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'PcntPop'", 'blank': 'True'}),
            'pop': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'Pop'", 'blank': 'True'}),
            'smpdus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'SmpDUs'", 'blank': 'True'}),
            'totalppleinarea': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'TotalPpleinArea'", 'blank': 'True'}),
            'totdus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'TotDUs'", 'blank': 'True'}),
            'wspid': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'wspID'"}),
            'wspname': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'wspName'"})
        },
        u'majitables.preligioncounty': {
            'Meta': {'object_name': 'Preligioncounty', 'db_table': "u'PReligionCounty'"},
            'countyid': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'CountyID'", 'blank': 'True'}),
            'countyname': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'CountyName'"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ndus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'NDus'", 'blank': 'True'}),
            'pcntdus': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'PcntDUs'", 'blank': 'True'}),
            'religion': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'Religion'"})
        },
        u'majitables.preligionslum': {
            'Meta': {'object_name': 'Preligionslum', 'db_table': "u'PReligionSlum'"},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ndus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'NDus'", 'blank': 'True'}),
            'pcntdus': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'PcntDUs'", 'blank': 'True'}),
            'religion': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'Religion'"}),
            'slumid': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'SlumID'", 'blank': 'True'}),
            'slumname': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'SlumName'"})
        },
        u'majitables.preligiontown': {
            'Meta': {'object_name': 'Preligiontown', 'db_table': "u'PReligionTown'"},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ndus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'NDus'", 'blank': 'True'}),
            'pcntdus': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'PcntDUs'", 'blank': 'True'}),
            'religion': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'Religion'"}),
            'townid': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'TownID'", 'blank': 'True'}),
            'townname': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'TownName'"})
        },
        u'majitables.preligionwsp': {
            'Meta': {'object_name': 'Preligionwsp', 'db_table': "u'PReligionWSP'"},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ndus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'NDus'", 'blank': 'True'}),
            'pcntdus': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'PcntDUs'", 'blank': 'True'}),
            'religion': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'Religion'"}),
            'wspid': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'wspID'"}),
            'wspname': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'wspName'"})
        },
        u'majitables.sanfacpractcounty': {
            'Meta': {'object_name': 'Sanfacpractcounty', 'db_table': "u'SanFacPractCounty'"},
            'countyid': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'CountyID'", 'blank': 'True'}),
            'countyname': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'CountyName'"}),
            'dusinsmp': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'DUsInSmp'", 'blank': 'True'}),
            'factype': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'FacType'"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ndus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'NDus'", 'blank': 'True'}),
            'pcntdus': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'pcntDUs'", 'blank': 'True'}),
            'smpdus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'SmpDUs'", 'blank': 'True'}),
            'totdus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'TotDUs'", 'blank': 'True'})
        },
        u'majitables.sanfacpractslum': {
            'Meta': {'object_name': 'Sanfacpractslum', 'db_table': "u'SanFacPractSlum'"},
            'dusinsmp': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'DUsInSmp'", 'blank': 'True'}),
            'factype': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'FacType'"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ndus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'NDus'", 'blank': 'True'}),
            'pcntdus': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'pcntDUs'", 'blank': 'True'}),
            'slumid': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'SlumID'", 'blank': 'True'}),
            'slumname': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'SlumName'"}),
            'smpdus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'SmpDUs'", 'blank': 'True'}),
            'totdus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'TotDUs'", 'blank': 'True'})
        },
        u'majitables.sanfacpractwsp': {
            'Meta': {'object_name': 'Sanfacpractwsp', 'db_table': "u'SanFacPractWSP'"},
            'dusinsmp': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'DUsInSmp'", 'blank': 'True'}),
            'factype': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'FacType'"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ndus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'NDus'", 'blank': 'True'}),
            'pcntdus': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'pcntDUs'", 'blank': 'True'}),
            'smpdus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'SmpDUs'", 'blank': 'True'}),
            'totdus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'TotDUs'", 'blank': 'True'}),
            'wspid': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'WSPID'"}),
            'wspname': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'WSPName'"})
        },
        u'majitables.sanitation12b': {
            'Meta': {'object_name': 'Sanitation12B', 'db_table': "u'Sanitation-12b'"},
            'anysanproj': ('django.db.models.fields.TextField', [], {'db_column': "u'AnySanProj'"}),
            'areaid': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'AreaID'", 'blank': 'True'}),
            'areaname': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'Areaname'"}),
            'cmnmaterials': ('django.db.models.fields.TextField', [], {'db_column': "u'CmnMaterials'"}),
            'dispmthd': ('django.db.models.fields.TextField', [], {'db_column': "u'DispMthd'"}),
            'facshared': ('django.db.models.fields.TextField', [], {'db_column': "u'FacShared'"}),
            'howemptied': ('django.db.models.fields.TextField', [], {'db_column': "u'HowEmptied'"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mnsproblem': ('django.db.models.fields.TextField', [], {'db_column': "u'MnSProblem'"}),
            'pitscovered': ('django.db.models.fields.TextField', [], {'db_column': "u'Pitscovered'"}),
            'pitsemptied': ('django.db.models.fields.TextField', [], {'db_column': "u'PitsEmptied'"}),
            'usedasbath': ('django.db.models.fields.TextField', [], {'db_column': "u'UsedasBath'"}),
            'usedasstore': ('django.db.models.fields.TextField', [], {'db_column': "u'UsedasStore'"}),
            'usedfordumping': ('django.db.models.fields.TextField', [], {'db_column': "u'UsedforDumping'"})
        },
        u'majitables.sanitationpractice': {
            'Meta': {'object_name': 'Sanitationpractice', 'db_table': "u'SanitationPractice'"},
            'areaid': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'AreaID'", 'blank': 'True'}),
            'areaname': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'Areaname'"}),
            'areasmpdus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'AreaSmpDUs'", 'blank': 'True'}),
            'dus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'DUs'", 'blank': 'True'}),
            'factype': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'FacType'"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ndus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'NDus'", 'blank': 'True'}),
            'numdu': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'NumDU'", 'blank': 'True'}),
            'pcntdus': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'pcntDUs'", 'blank': 'True'})
        },
        u'majitables.sanitationsewlnk': {
            'Meta': {'object_name': 'Sanitationsewlnk', 'db_table': "u'SanitationSewLnk'"},
            'areaid': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'AreaID'", 'blank': 'True'}),
            'arealinkedsanitation': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'AreaLinkedSanitation'"}),
            'areaname': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'Areaname'"}),
            'cmnpriv': ('django.db.models.fields.TextField', [], {'db_column': "u'CmnPriv'"}),
            'cmnpublic': ('django.db.models.fields.TextField', [], {'db_column': "u'CmnPublic'"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mainsfacility': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'MainSFacility'"}),
            'ncomtoilet': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'Ncomtoilet'", 'blank': 'True'}),
            'npubtoilet': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'NpubToilet'"}),
            'nseptic': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'NSeptic'"}),
            'sactivecons': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'Sactivecons'"}),
            'snwdist': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'Snwdist'"}),
            'techstat': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'TechStat'"}),
            'townid': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'TownID'", 'blank': 'True'})
        },
        u'majitables.savgdush44county': {
            'Meta': {'object_name': 'Savgdush44County', 'db_table': "u'SAvgDUSh44County'"},
            'countyid': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'CountyID'", 'blank': 'True'}),
            'countyname': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'CountyName'"}),
            'dusinarea': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'DusInArea'", 'blank': 'True'}),
            'dusinsmp': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'DUsInSmp'", 'blank': 'True'}),
            'dussharing': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'DUsSharing'"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pcntdus': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'pcntDUs'", 'blank': 'True'}),
            'pcntpop': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'PcntPop'", 'blank': 'True'}),
            'pop': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'Pop'", 'blank': 'True'}),
            'smpdus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'SmpDUs'", 'blank': 'True'}),
            'totalppleinarea': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'TotalPpleinArea'", 'blank': 'True'}),
            'totdus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'TotDUs'", 'blank': 'True'})
        },
        u'majitables.savgdush44slum': {
            'Meta': {'object_name': 'Savgdush44Slum', 'db_table': "u'SAvgDUSh44Slum'"},
            'dusinarea': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'DusInArea'", 'blank': 'True'}),
            'dusinsmp': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'DUsInSmp'", 'blank': 'True'}),
            'dussharing': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'DUsSharing'"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pcntdus': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'pcntDUs'", 'blank': 'True'}),
            'pcntpop': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'PcntPop'", 'blank': 'True'}),
            'pop': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'Pop'", 'blank': 'True'}),
            'slumid': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'SlumID'", 'blank': 'True'}),
            'slumname': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'SlumName'"}),
            'smpdus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'SmpDUs'", 'blank': 'True'}),
            'totalppleinarea': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'TotalPpleinArea'", 'blank': 'True'}),
            'totdus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'TotDUs'", 'blank': 'True'})
        },
        u'majitables.savgdush44wsp': {
            'Meta': {'object_name': 'Savgdush44Wsp', 'db_table': "u'SAvgDUSh44WSP'"},
            'dusinarea': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'DusInArea'", 'blank': 'True'}),
            'dusinsmp': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'DUsInSmp'", 'blank': 'True'}),
            'dussharing': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'DUsSharing'"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pcntdus': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'pcntDUs'", 'blank': 'True'}),
            'pcntpop': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'PcntPop'", 'blank': 'True'}),
            'pop': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'Pop'", 'blank': 'True'}),
            'smpdus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'SmpDUs'", 'blank': 'True'}),
            'totalppleinarea': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'TotalPpleinArea'", 'blank': 'True'}),
            'totdus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'TotDUs'", 'blank': 'True'}),
            'wspid': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'WSPID'"}),
            'wspname': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'WSPName'"})
        },
        u'majitables.savgdusshfaccounty': {
            'Meta': {'object_name': 'Savgdusshfaccounty', 'db_table': "u'SAvgDUsShFacCounty'"},
            'avgdusz': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'AvgDUSz'", 'blank': 'True'}),
            'countyid': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'CountyID'", 'blank': 'True'}),
            'countyname': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'CountyName'"}),
            'dusinarea': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'DusInArea'", 'blank': 'True'}),
            'dusinsmp': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'DUsInSmp'", 'blank': 'True'}),
            'dussharing': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'DUsSharing'"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pcntdus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'pcntDUs'", 'blank': 'True'}),
            'pop': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'Pop'", 'blank': 'True'}),
            'smpdus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'SmpDUs'", 'blank': 'True'}),
            'totdus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'TotDUs'", 'blank': 'True'})
        },
        u'majitables.savgdusshfacslum': {
            'Meta': {'object_name': 'Savgdusshfacslum', 'db_table': "u'SAvgDUsShFacSlum'"},
            'avgdusz': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'AvgDUSz'", 'blank': 'True'}),
            'dusinarea': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'DusInArea'", 'blank': 'True'}),
            'dusinsmp': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'DUsInSmp'", 'blank': 'True'}),
            'dussharing': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'DUsSharing'"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pcntdus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'pcntDUs'", 'blank': 'True'}),
            'pop': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'Pop'", 'blank': 'True'}),
            'slumid': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'SlumID'", 'blank': 'True'}),
            'slumname': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'SlumName'"}),
            'smpdus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'SmpDUs'", 'blank': 'True'}),
            'totdus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'TotDUs'", 'blank': 'True'})
        },
        u'majitables.savgdusshfacwsp': {
            'Meta': {'object_name': 'Savgdusshfacwsp', 'db_table': "u'SAvgDUsShFacWSP'"},
            'avgdusz': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'AvgDUSz'", 'blank': 'True'}),
            'dusinarea': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'DusInArea'", 'blank': 'True'}),
            'dusinsmp': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'DUsInSmp'", 'blank': 'True'}),
            'dussharing': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'DUsSharing'"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pcntdus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'pcntDUs'", 'blank': 'True'}),
            'pop': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'Pop'", 'blank': 'True'}),
            'smpdus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'SmpDUs'", 'blank': 'True'}),
            'totdus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'TotDUs'", 'blank': 'True'}),
            'wspid': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'WSPID'"}),
            'wspname': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'WSPName'"})
        },
        u'majitables.savghhshowntlt': {
            'Meta': {'object_name': 'Savghhshowntlt', 'db_table': "u'SAvgHHShOwnTlt'"},
            'areaid': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'AreaID'", 'blank': 'True'}),
            'areaname': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'Areaname'"}),
            'areasmpdus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'AreaSmpDUs'", 'blank': 'True'}),
            'avghhsharing': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'AvgHHsharing'"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'maxhhsh': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'MaxHHsh'"}),
            'minhhsh': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'MinHHsh'"}),
            'numdu': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'NumDU'", 'blank': 'True'})
        },
        u'majitables.savgtltbath': {
            'Meta': {'object_name': 'Savgtltbath', 'db_table': "u'SAvgTltBath'"},
            'areaid': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'AreaID'", 'blank': 'True'}),
            'areaname': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'Areaname'"}),
            'areasmpdus': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'AreaSmpDUs'", 'blank': 'True'}),
            'avgbaths': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'Avgbaths'", 'blank': 'True'}),
            'avghhsharing': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'AvgHHsharing'"}),
            'avgnfac': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'AvgNFac'", 'blank': 'True'}),
            'dus': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'DUs'", 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'maxbath': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'MaxBath'", 'blank': 'True'}),
            'maxfac': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'MaxFac'", 'blank': 'True'}),
            'maxhhsh': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'MaxHHsh'"}),
            'minbaths': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'MinBaths'", 'blank': 'True'}),
            'minfac': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'MinFac'", 'blank': 'True'}),
            'minhhsh': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'MinHHsh'"}),
            'ndus': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'NDus'", 'blank': 'True'}),
            'numdu': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'numDU'", 'blank': 'True'}),
            'pcntdus': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'pcntDUs'", 'blank': 'True'})
        },
        u'majitables.sduhasownbath': {
            'Meta': {'object_name': 'Sduhasownbath', 'db_table': "u'SDUHasOwnBath'"},
            'areaid': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'AreaID'", 'blank': 'True'}),
            'areaname': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'Areaname'"}),
            'areasmpdus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'AreaSmpDUs'", 'blank': 'True'}),
            'duownbath': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'DuOwnBath'"}),
            'dus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'DUs'", 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ndus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'NDus'", 'blank': 'True'}),
            'numdu': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'NumDU'", 'blank': 'True'}),
            'pcntdus': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'pcntDUs'", 'blank': 'True'})
        },
        u'majitables.sduhasownfacility': {
            'Meta': {'object_name': 'Sduhasownfacility', 'db_table': "u'SDUHasOwnFacility'"},
            'areaid': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'AreaID'", 'blank': 'True'}),
            'areaname': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'Areaname'"}),
            'areasmpdus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'AreaSmpDUs'", 'blank': 'True'}),
            'duhasownfac': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'DuHasOwnFac'"}),
            'dus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'DUs'", 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ndus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'NDus'", 'blank': 'True'}),
            'numdu': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'NumDU'", 'blank': 'True'}),
            'pcntdus': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'pcntDUs'", 'blank': 'True'})
        },
        u'majitables.sduownbath45county': {
            'Meta': {'object_name': 'Sduownbath45County', 'db_table': "u'SDUOwnBath45County'"},
            'countyid': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'CountyID'", 'blank': 'True'}),
            'countyname': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'CountyName'"}),
            'dusinarea': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'DusInArea'", 'blank': 'True'}),
            'dusinsmp': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'DUsInSmp'", 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pcntdus': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'pcntDUs'", 'blank': 'True'}),
            'pop': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'Pop'", 'blank': 'True'}),
            'smpdus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'SmpDUs'", 'blank': 'True'}),
            'totdus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'TotDUs'", 'blank': 'True'})
        },
        u'majitables.sduownbath45slum': {
            'Meta': {'object_name': 'Sduownbath45Slum', 'db_table': "u'SDUOwnBath45Slum'"},
            'dusinarea': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'DusInArea'", 'blank': 'True'}),
            'dusinsmp': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'DUsInSmp'", 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pcntdus': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'pcntDUs'", 'blank': 'True'}),
            'pop': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'Pop'", 'blank': 'True'}),
            'slumid': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'SlumID'", 'blank': 'True'}),
            'slumname': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'SlumName'"}),
            'smpdus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'SmpDUs'", 'blank': 'True'}),
            'totdus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'TotDUs'", 'blank': 'True'})
        },
        u'majitables.sduownbath45wsp': {
            'Meta': {'object_name': 'Sduownbath45Wsp', 'db_table': "u'SDUOwnBath45WSP'"},
            'dusinarea': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'DusInArea'", 'blank': 'True'}),
            'dusinsmp': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'DUsInSmp'", 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pcntdus': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'pcntDUs'", 'blank': 'True'}),
            'pop': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'Pop'", 'blank': 'True'}),
            'smpdus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'SmpDUs'", 'blank': 'True'}),
            'totdus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'TotDUs'", 'blank': 'True'}),
            'wspid': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'WSPID'"}),
            'wspname': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'WSPName'"})
        },
        u'majitables.sduownfac45county': {
            'Meta': {'object_name': 'Sduownfac45County', 'db_table': "u'SDUOwnFac45County'"},
            'countyid': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'CountyID'", 'blank': 'True'}),
            'countyname': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'CountyName'"}),
            'dusinarea': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'DusInArea'", 'blank': 'True'}),
            'dusinsmp': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'DUsInSmp'", 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pcntdus': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'pcntDUs'", 'blank': 'True'}),
            'pcntpop': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'PcntPop'", 'blank': 'True'}),
            'pop': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'Pop'", 'blank': 'True'}),
            'smpdus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'SmpDUs'", 'blank': 'True'}),
            'totalppleinarea': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'TotalPpleinArea'", 'blank': 'True'}),
            'totdus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'TotDUs'", 'blank': 'True'})
        },
        u'majitables.sduownfac45slum': {
            'Meta': {'object_name': 'Sduownfac45Slum', 'db_table': "u'SDUOwnFac45Slum'"},
            'dusinarea': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'DusInArea'", 'blank': 'True'}),
            'dusinsmp': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'DUsInSmp'", 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pcntdus': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'pcntDUs'", 'blank': 'True'}),
            'pcntpop': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'PcntPop'", 'blank': 'True'}),
            'pop': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'Pop'", 'blank': 'True'}),
            'slumid': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'SlumID'", 'blank': 'True'}),
            'slumname': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'SlumName'"}),
            'smpdus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'SmpDUs'", 'blank': 'True'}),
            'totalppleinarea': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'TotalPpleinArea'", 'blank': 'True'}),
            'totdus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'TotDUs'", 'blank': 'True'})
        },
        u'majitables.sduownfac45wsp': {
            'Meta': {'object_name': 'Sduownfac45Wsp', 'db_table': "u'SDUOwnFac45WSP'"},
            'dusinarea': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'DusInArea'", 'blank': 'True'}),
            'dusinsmp': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'DUsInSmp'", 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pcntdus': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'pcntDUs'", 'blank': 'True'}),
            'pcntpop': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'PcntPop'", 'blank': 'True'}),
            'pop': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'Pop'", 'blank': 'True'}),
            'smpdus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'SmpDUs'", 'blank': 'True'}),
            'totalppleinarea': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'TotalPpleinArea'", 'blank': 'True'}),
            'totdus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'TotDUs'", 'blank': 'True'}),
            'wspid': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'WSPID'"}),
            'wspname': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'WSPName'"})
        },
        u'majitables.sduownrpit45county': {
            'Meta': {'object_name': 'Sduownrpit45County', 'db_table': "u'SDUOwnRPit45County'"},
            'countyid': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'CountyID'", 'blank': 'True'}),
            'countyname': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'CountyName'"}),
            'dusinarea': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'DusInArea'", 'blank': 'True'}),
            'dusinsmp': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'DUsInSmp'", 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pcntdus': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'pcntDUs'", 'blank': 'True'}),
            'pop': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'Pop'", 'blank': 'True'}),
            'smpdus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'SmpDUs'", 'blank': 'True'}),
            'totdus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'TotDUs'", 'blank': 'True'})
        },
        u'majitables.sduownrpit45slum': {
            'Meta': {'object_name': 'Sduownrpit45Slum', 'db_table': "u'SDUOwnRPit45Slum'"},
            'dusinarea': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'DusInArea'", 'blank': 'True'}),
            'dusinsmp': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'DUsInSmp'", 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pcntdus': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'pcntDUs'", 'blank': 'True'}),
            'pop': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'Pop'", 'blank': 'True'}),
            'slumid': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'SlumID'", 'blank': 'True'}),
            'slumname': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'SlumName'"}),
            'smpdus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'SmpDUs'", 'blank': 'True'}),
            'totdus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'TotDUs'", 'blank': 'True'})
        },
        u'majitables.sduownrpit45wsp': {
            'Meta': {'object_name': 'Sduownrpit45Wsp', 'db_table': "u'SDUOwnRPit45WSP'"},
            'dusinarea': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'DusInArea'", 'blank': 'True'}),
            'dusinsmp': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'DUsInSmp'", 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pcntdus': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'pcntDUs'", 'blank': 'True'}),
            'pop': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'Pop'", 'blank': 'True'}),
            'smpdus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'SmpDUs'", 'blank': 'True'}),
            'totdus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'TotDUs'", 'blank': 'True'}),
            'wspid': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'WSPID'"}),
            'wspname': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'WSPName'"})
        },
        u'majitables.sdusharestoilet': {
            'Meta': {'object_name': 'Sdusharestoilet', 'db_table': "u'SDuSharesToilet'"},
            'areaid': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'AreaID'", 'blank': 'True'}),
            'areaname': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'Areaname'"}),
            'areasmpdus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'AreaSmpDUs'", 'blank': 'True'}),
            'dus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'DUs'", 'blank': 'True'}),
            'dusharefac': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'DuShareFac'"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ndus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'NDus'", 'blank': 'True'}),
            'numdu': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'NumDU'", 'blank': 'True'}),
            'pcntdus': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'pcntDUs'", 'blank': 'True'})
        },
        u'majitables.seincomesrcs': {
            'Meta': {'object_name': 'Seincomesrcs', 'db_table': "u'SEIncomeSrcs'"},
            'areaid': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'AreaID'", 'blank': 'True'}),
            'areaname': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'Areaname'"}),
            'femaleincsrc': ('django.db.models.fields.TextField', [], {'db_column': "u'FemaleIncSrc'"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'maleincsrc': ('django.db.models.fields.TextField', [], {'db_column': "u'MaleIncSrc'"}),
            'vandlvl': ('django.db.models.fields.TextField', [], {'db_column': "u'VandLvl'"})
        },
        u'majitables.sfacinplotcounty': {
            'Meta': {'object_name': 'Sfacinplotcounty', 'db_table': "u'SFacInPlotCounty'"},
            'countyid': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'CountyID'", 'blank': 'True'}),
            'countyname': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'CountyName'"}),
            'dusinarea': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'DusInArea'", 'blank': 'True'}),
            'dusinsmp': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'DUsInSmp'", 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pcntdus': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'pcntDUs'", 'blank': 'True'}),
            'pop': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'Pop'", 'blank': 'True'}),
            'smpdus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'SmpDUs'", 'blank': 'True'}),
            'totdus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'TotDUs'", 'blank': 'True'})
        },
        u'majitables.sfacinplotslum': {
            'Meta': {'object_name': 'Sfacinplotslum', 'db_table': "u'SFacInPlotSlum'"},
            'dusinarea': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'DusInArea'", 'blank': 'True'}),
            'dusinsmp': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'DUsInSmp'", 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pcntdus': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'pcntDUs'", 'blank': 'True'}),
            'pop': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'Pop'", 'blank': 'True'}),
            'slumid': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'SlumID'", 'blank': 'True'}),
            'slumname': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'SlumName'"}),
            'smpdus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'SmpDUs'", 'blank': 'True'}),
            'totdus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'TotDUs'", 'blank': 'True'})
        },
        u'majitables.sfacinplotwsp': {
            'Meta': {'object_name': 'Sfacinplotwsp', 'db_table': "u'SFacInPlotWSP'"},
            'dusinarea': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'DusInArea'", 'blank': 'True'}),
            'dusinsmp': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'DUsInSmp'", 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pcntdus': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'pcntDUs'", 'blank': 'True'}),
            'pop': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'Pop'", 'blank': 'True'}),
            'smpdus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'SmpDUs'", 'blank': 'True'}),
            'totdus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'TotDUs'", 'blank': 'True'}),
            'wspid': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'WspID'"}),
            'wspname': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'WspName'"})
        },
        u'majitables.sfacsharedcounty': {
            'Meta': {'object_name': 'Sfacsharedcounty', 'db_table': "u'SFacSharedCounty'"},
            'countyid': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'CountyID'", 'blank': 'True'}),
            'countyname': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'CountyName'"}),
            'dusinarea': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'DusInArea'", 'blank': 'True'}),
            'dusinsmp': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'DUsInSmp'", 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pcntdus': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'pcntDUs'", 'blank': 'True'}),
            'pcntpop': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'PcntPop'", 'blank': 'True'}),
            'pop': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'Pop'", 'blank': 'True'}),
            'smpdus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'SmpDUs'", 'blank': 'True'}),
            'totalppleinarea': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'TotalPpleinArea'", 'blank': 'True'}),
            'totdus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'TotDUs'", 'blank': 'True'})
        },
        u'majitables.sfacsharedslum': {
            'Meta': {'object_name': 'Sfacsharedslum', 'db_table': "u'SFacSharedSlum'"},
            'dusinarea': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'DusInArea'", 'blank': 'True'}),
            'dusinsmp': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'DUsInSmp'", 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pcntdus': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'pcntDUs'", 'blank': 'True'}),
            'pcntpop': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'PcntPop'", 'blank': 'True'}),
            'pop': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'Pop'", 'blank': 'True'}),
            'slumid': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'SlumID'", 'blank': 'True'}),
            'slumname': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'SlumName'"}),
            'smpdus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'SmpDUs'", 'blank': 'True'}),
            'totalppleinarea': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'TotalPpleinArea'", 'blank': 'True'}),
            'totdus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'TotDUs'", 'blank': 'True'})
        },
        u'majitables.sfacsharedwsp': {
            'Meta': {'object_name': 'Sfacsharedwsp', 'db_table': "u'SFacSharedWSP'"},
            'dusinarea': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'DusInArea'", 'blank': 'True'}),
            'dusinsmp': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'DUsInSmp'", 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pcntdus': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'pcntDUs'", 'blank': 'True'}),
            'pcntpop': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'PcntPop'", 'blank': 'True'}),
            'pop': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'Pop'", 'blank': 'True'}),
            'smpdus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'SmpDUs'", 'blank': 'True'}),
            'totalppleinarea': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'TotalPpleinArea'", 'blank': 'True'}),
            'totdus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'TotDUs'", 'blank': 'True'}),
            'wspid': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'WSPID'"}),
            'wspname': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'WSPName'"})
        },
        u'majitables.sfactypes': {
            'Meta': {'object_name': 'Sfactypes', 'db_table': "u'SFacTypes'"},
            'areaid': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'AreaID'", 'blank': 'True'}),
            'areaname': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'Areaname'"}),
            'areasmpdus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'AreaSmpDUs'", 'blank': 'True'}),
            'dus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'DUs'", 'blank': 'True'}),
            'factype': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'FacType'"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ndus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'NDus'", 'blank': 'True'}),
            'numdu': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'NumDU'", 'blank': 'True'}),
            'pcntdus': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'pcntDUs'", 'blank': 'True'})
        },
        u'majitables.simpjmp': {
            'Meta': {'object_name': 'Simpjmp', 'db_table': "u'SImpJMP'"},
            'areaid': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'AreaID'", 'blank': 'True'}),
            'areaname': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'Areaname'"}),
            'areasmpdus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'AreaSmpDUs'", 'blank': 'True'}),
            'dusinarea': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'DusInArea'", 'blank': 'True'}),
            'dusinsmp': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'DUsInSmp'", 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pcntdus': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'pcntDUs'", 'blank': 'True'}),
            'pcntpple2': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'smppersons': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'SmpPersons'", 'blank': 'True'}),
            'totaldusinarea': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'TotalDUsInArea'", 'blank': 'True'}),
            'totalppleinarea': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'TotalPpleinArea'", 'blank': 'True'})
        },
        u'majitables.simpjmpcounty': {
            'Meta': {'object_name': 'Simpjmpcounty', 'db_table': "u'SImpJMPCounty'"},
            'countyid': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'CountyID'", 'blank': 'True'}),
            'countyname': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'CountyName'"}),
            'dusinarea': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'DusInArea'", 'blank': 'True'}),
            'dusinsmp': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'DUsInSmp'", 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pcntdus': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'pcntDUs'", 'blank': 'True'}),
            'pcntpop': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'PcntPop'", 'blank': 'True'}),
            'pop': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'Pop'", 'blank': 'True'}),
            'smpdus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'SmpDUs'", 'blank': 'True'}),
            'totalppleinarea': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'TotalPpleinArea'", 'blank': 'True'}),
            'totdus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'TotDUs'", 'blank': 'True'})
        },
        u'majitables.simpjmpownfac': {
            'Meta': {'object_name': 'Simpjmpownfac', 'db_table': "u'SImpJMPOwnFac'"},
            'areaid': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'AreaID'", 'blank': 'True'}),
            'areaname': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'Areaname'"}),
            'areasmpdus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'AreaSmpDUs'", 'blank': 'True'}),
            'dusinarea': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'DusInArea'", 'blank': 'True'}),
            'dusinsmp': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'DUsInSmp'", 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pcntdus': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'pcntDUs'", 'blank': 'True'}),
            'pcntpple2': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'smppersons': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'SmpPersons'", 'blank': 'True'}),
            'totaldusinarea': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'TotalDUsInArea'", 'blank': 'True'}),
            'totalppleinarea': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'TotalPpleinArea'", 'blank': 'True'})
        },
        u'majitables.simpjmpownplotfac': {
            'Meta': {'object_name': 'Simpjmpownplotfac', 'db_table': "u'SImpJMPOwnPlotFac'"},
            'areaid': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'AreaID'", 'blank': 'True'}),
            'areaname': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'Areaname'"}),
            'areasmpdus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'AreaSmpDUs'", 'blank': 'True'}),
            'dusinarea': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'DusInArea'", 'blank': 'True'}),
            'dusinsmp': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'DUsInSmp'", 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pcntdus': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'pcntDUs'", 'blank': 'True'}),
            'pcntpple': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'smppersons': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'SmpPersons'", 'blank': 'True'}),
            'totaldusinarea': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'TotalDUsInArea'", 'blank': 'True'}),
            'totalppleinarea': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'TotalPpleinArea'", 'blank': 'True'})
        },
        u'majitables.simpjmpsharedcounty': {
            'Meta': {'object_name': 'Simpjmpsharedcounty', 'db_table': "u'SImpJMPSharedCounty'"},
            'countyid': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'CountyID'", 'blank': 'True'}),
            'countyname': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'CountyName'"}),
            'dusinarea': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'DusInArea'", 'blank': 'True'}),
            'dusinsmp': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'DUsInSmp'", 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pcntdus': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'pcntDUs'", 'blank': 'True'}),
            'pcntpop': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'PcntPop'", 'blank': 'True'}),
            'pop': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'Pop'", 'blank': 'True'}),
            'smpdus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'SmpDUs'", 'blank': 'True'}),
            'totalppleinarea': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'TotalPpleinArea'", 'blank': 'True'}),
            'totdus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'TotDUs'", 'blank': 'True'})
        },
        u'majitables.simpjmpsharedslum': {
            'Meta': {'object_name': 'Simpjmpsharedslum', 'db_table': "u'SImpJMPSharedSlum'"},
            'dusinarea': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'DusInArea'", 'blank': 'True'}),
            'dusinsmp': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'DUsInSmp'", 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pcntdus': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'pcntDUs'", 'blank': 'True'}),
            'pcntpop': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'PcntPop'", 'blank': 'True'}),
            'pop': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'Pop'", 'blank': 'True'}),
            'slumid': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'SlumID'", 'blank': 'True'}),
            'slumname': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'SlumName'"}),
            'smpdus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'SmpDUs'", 'blank': 'True'}),
            'totalppleinarea': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'TotalPpleinArea'", 'blank': 'True'}),
            'totdus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'TotDUs'", 'blank': 'True'})
        },
        u'majitables.simpjmpsharedwsp': {
            'Meta': {'object_name': 'Simpjmpsharedwsp', 'db_table': "u'SImpJMPSharedWSP'"},
            'dusinarea': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'DusInArea'", 'blank': 'True'}),
            'dusinsmp': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'DUsInSmp'", 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pcntdus': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'pcntDUs'", 'blank': 'True'}),
            'pcntpop': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'PcntPop'", 'blank': 'True'}),
            'pop': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'Pop'", 'blank': 'True'}),
            'smpdus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'SmpDUs'", 'blank': 'True'}),
            'totalppleinarea': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'TotalPpleinArea'", 'blank': 'True'}),
            'totdus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'TotDUs'", 'blank': 'True'}),
            'wspid': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'WSPID'"}),
            'wspname': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'WSPName'"})
        },
        u'majitables.simpjmpshfac': {
            'Meta': {'object_name': 'Simpjmpshfac', 'db_table': "u'SImpJMPShFac'"},
            'areaid': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'AreaID'", 'blank': 'True'}),
            'areaname': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'Areaname'"}),
            'areasmpdus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'AreaSmpDUs'", 'blank': 'True'}),
            'dusinarea': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'DusInArea'", 'blank': 'True'}),
            'dusinsmp': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'DUsInSmp'", 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pcntdus': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'pcntDUs'", 'blank': 'True'}),
            'pcntpple': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'smppersons': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'SmpPersons'", 'blank': 'True'}),
            'totaldusinarea': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'TotalDUsInArea'", 'blank': 'True'}),
            'totalppleinarea': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'TotalPpleinArea'", 'blank': 'True'})
        },
        u'majitables.simpjmpslum': {
            'Meta': {'object_name': 'Simpjmpslum', 'db_table': "u'SImpJMPSlum'"},
            'dusinarea': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'DusInArea'", 'blank': 'True'}),
            'dusinsmp': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'DUsInSmp'", 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pcntdus': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'pcntDUs'", 'blank': 'True'}),
            'pcntpop': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'PcntPop'", 'blank': 'True'}),
            'pop': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'Pop'", 'blank': 'True'}),
            'slumid': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'SlumID'", 'blank': 'True'}),
            'slumname': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'SlumName'"}),
            'smpdus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'SmpDUs'", 'blank': 'True'}),
            'totalppleinarea': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'TotalPpleinArea'", 'blank': 'True'}),
            'totdus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'TotDUs'", 'blank': 'True'})
        },
        u'majitables.simpjmpwsp': {
            'Meta': {'object_name': 'Simpjmpwsp', 'db_table': "u'SImpJMPWSP'"},
            'dusinarea': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'DusInArea'", 'blank': 'True'}),
            'dusinsmp': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'DUsInSmp'", 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pcntdus': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'pcntDUs'", 'blank': 'True'}),
            'pcntpop': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'PcntPop'", 'blank': 'True'}),
            'pop': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'Pop'", 'blank': 'True'}),
            'smpdus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'SmpDUs'", 'blank': 'True'}),
            'totalppleinarea': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'TotalPpleinArea'", 'blank': 'True'}),
            'totdus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'TotDUs'", 'blank': 'True'}),
            'wspid': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'WspID'"}),
            'wspname': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'WspName'"})
        },
        u'majitables.snofacused': {
            'Meta': {'object_name': 'Snofacused', 'db_table': "u'SNoFacUsed'"},
            'areaid': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'AreaID'", 'blank': 'True'}),
            'areaname': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'Areaname'"}),
            'areasmpdus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'AreaSmpDUs'", 'blank': 'True'}),
            'dusinarea': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'DusInArea'", 'blank': 'True'}),
            'dusinsmp': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'DUsInSmp'", 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pcntdus': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'pcntDUs'", 'blank': 'True'}),
            'pcntpple': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'smppersons': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'SmpPersons'", 'blank': 'True'}),
            'totaldusinarea': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'TotalDUsInArea'", 'blank': 'True'}),
            'totalppleinarea': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'TotalPpleinArea'", 'blank': 'True'})
        },
        u'majitables.snofacusedcounty': {
            'Meta': {'object_name': 'Snofacusedcounty', 'db_table': "u'SNoFacUsedCounty'"},
            'countyid': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'CountyID'", 'blank': 'True'}),
            'countyname': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'CountyName'"}),
            'dusinarea': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'DusInArea'", 'blank': 'True'}),
            'dusinsmp': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'DUsInSmp'", 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pcntdus': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'pcntDUs'", 'blank': 'True'}),
            'pcntpop': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'PcntPop'", 'blank': 'True'}),
            'pop': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'Pop'", 'blank': 'True'}),
            'smpdus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'SmpDUs'", 'blank': 'True'}),
            'totalppleinarea': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'TotalPpleinArea'", 'blank': 'True'}),
            'totdus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'TotDUs'", 'blank': 'True'})
        },
        u'majitables.snofacusedslum': {
            'Meta': {'object_name': 'Snofacusedslum', 'db_table': "u'SNoFacUsedSlum'"},
            'dusinarea': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'DusInArea'", 'blank': 'True'}),
            'dusinsmp': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'DUsInSmp'", 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pcntdus': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'pcntDUs'", 'blank': 'True'}),
            'pcntpop': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'PcntPop'", 'blank': 'True'}),
            'pop': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'Pop'", 'blank': 'True'}),
            'slumid': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'SlumID'", 'blank': 'True'}),
            'slumname': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'SlumName'"}),
            'smpdus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'SmpDUs'", 'blank': 'True'}),
            'totalppleinarea': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'TotalPpleinArea'", 'blank': 'True'}),
            'totdus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'TotDUs'", 'blank': 'True'})
        },
        u'majitables.snofacusedwsp': {
            'Meta': {'object_name': 'Snofacusedwsp', 'db_table': "u'SNoFacUsedWSP'"},
            'dusinarea': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'DusInArea'", 'blank': 'True'}),
            'dusinsmp': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'DUsInSmp'", 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pcntdus': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'pcntDUs'", 'blank': 'True'}),
            'pcntpop': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'PcntPop'", 'blank': 'True'}),
            'pop': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'Pop'", 'blank': 'True'}),
            'smpdus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'SmpDUs'", 'blank': 'True'}),
            'totalppleinarea': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'TotalPpleinArea'", 'blank': 'True'}),
            'totdus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'TotDUs'", 'blank': 'True'}),
            'wspid': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'WSPID'"}),
            'wspname': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'WSPName'"})
        },
        u'majitables.snoofbaths': {
            'Meta': {'object_name': 'Snoofbaths', 'db_table': "u'SNoofBaths'"},
            'areaid': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'AreaID'", 'blank': 'True'}),
            'areaname': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'Areaname'"}),
            'areasmpdus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'AreaSmpDUs'", 'blank': 'True'}),
            'dus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'DUs'", 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nbaths': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'NBaths'"}),
            'ndus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'NDus'", 'blank': 'True'}),
            'numdu': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'NumDU'", 'blank': 'True'}),
            'pcntdus': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'pcntDUs'", 'blank': 'True'})
        },
        u'majitables.snoofdushrngtlt': {
            'Meta': {'object_name': 'Snoofdushrngtlt', 'db_table': "u'SNoofDUShrngTlt'"},
            'areaid': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'AreaID'", 'blank': 'True'}),
            'areaname': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'Areaname'"}),
            'areasmpdus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'AreaSmpDUs'", 'blank': 'True'}),
            'dus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'DUs'", 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ndus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'NDus'", 'blank': 'True'}),
            'nshhhs': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'NshHHs'"}),
            'numdu': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'NumDU'", 'blank': 'True'}),
            'pcntdus': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'pcntDUs'", 'blank': 'True'})
        },
        u'majitables.snooffacilities': {
            'Meta': {'object_name': 'Snooffacilities', 'db_table': "u'SNoofFacilities'"},
            'areaid': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'AreaID'", 'blank': 'True'}),
            'areaname': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'Areaname'"}),
            'areasmpdus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'AreaSmpDUs'", 'blank': 'True'}),
            'dus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'DUs'", 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ndus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'NDus'", 'blank': 'True'}),
            'nfacilities': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'Nfacilities'"}),
            'numdu': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'NumDU'", 'blank': 'True'}),
            'pcntdus': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'pcntDUs'", 'blank': 'True'})
        },
        u'majitables.socioeconinfr': {
            'Meta': {'object_name': 'Socioeconinfr', 'db_table': "u'SocioEconInfr'"},
            'areaid': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'AreaID'", 'blank': 'True'}),
            'areaname': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'Areaname'"}),
            'hclinic': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'HClinic'", 'blank': 'True'}),
            'hosp': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'Hosp'", 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'othinfr': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'OthInfr'"}),
            'prsch': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'PrSch'", 'blank': 'True'}),
            'sebusstn': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'SEbusstn'", 'blank': 'True'}),
            'secsch': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'SecSch'", 'blank': 'True'}),
            'sehall': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'SEhall'", 'blank': 'True'}),
            'seoth': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'SEoth'", 'blank': 'True'}),
            'sepolice': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'SEpolice'", 'blank': 'True'}),
            'seshop': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'SEshop'", 'blank': 'True'}),
            'sesport': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'SEsport'", 'blank': 'True'})
        },
        u'majitables.sownimpjmpcounty': {
            'Meta': {'object_name': 'Sownimpjmpcounty', 'db_table': "u'SOwnImpJMPCounty'"},
            'countyid': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'CountyID'", 'blank': 'True'}),
            'countyname': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'CountyName'"}),
            'dusinarea': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'DusInArea'", 'blank': 'True'}),
            'dusinsmp': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'DUsInSmp'", 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pcntdus': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'pcntDUs'", 'blank': 'True'}),
            'pcntpop': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'PcntPop'", 'blank': 'True'}),
            'pop': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'Pop'", 'blank': 'True'}),
            'smpdus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'SmpDUs'", 'blank': 'True'}),
            'totalppleinarea': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'TotalPpleinArea'", 'blank': 'True'}),
            'totdus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'TotDUs'", 'blank': 'True'})
        },
        u'majitables.sownimpjmpslum': {
            'Meta': {'object_name': 'Sownimpjmpslum', 'db_table': "u'SOwnImpJMPSlum'"},
            'dusinarea': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'DusInArea'", 'blank': 'True'}),
            'dusinsmp': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'DUsInSmp'", 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pcntdus': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'pcntDUs'", 'blank': 'True'}),
            'pcntpop': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'PcntPop'", 'blank': 'True'}),
            'pop': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'Pop'", 'blank': 'True'}),
            'slumid': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'SlumID'", 'blank': 'True'}),
            'slumname': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'SlumName'"}),
            'smpdus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'SmpDUs'", 'blank': 'True'}),
            'totalppleinarea': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'TotalPpleinArea'", 'blank': 'True'}),
            'totdus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'TotDUs'", 'blank': 'True'})
        },
        u'majitables.sownimpjmpwsp': {
            'Meta': {'object_name': 'Sownimpjmpwsp', 'db_table': "u'SOwnImpJMPWSP'"},
            'dusinarea': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'DusInArea'", 'blank': 'True'}),
            'dusinsmp': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'DUsInSmp'", 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pcntdus': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'pcntDUs'", 'blank': 'True'}),
            'pcntpop': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'PcntPop'", 'blank': 'True'}),
            'pop': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'Pop'", 'blank': 'True'}),
            'smpdus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'SmpDUs'", 'blank': 'True'}),
            'totalppleinarea': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'TotalPpleinArea'", 'blank': 'True'}),
            'totdus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'TotDUs'", 'blank': 'True'}),
            'wspid': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'WSPID'"}),
            'wspname': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'WSPName'"})
        },
        u'majitables.sownimpntshcounty': {
            'Meta': {'object_name': 'Sownimpntshcounty', 'db_table': "u'SownImpNtShCounty'"},
            'countyid': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'CountyID'", 'blank': 'True'}),
            'countyname': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'CountyName'"}),
            'dusinarea': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'DusInArea'", 'blank': 'True'}),
            'dusinsmp': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'DUsInSmp'", 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pcntdus': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'pcntDUs'", 'blank': 'True'}),
            'pcntpop': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'PcntPop'", 'blank': 'True'}),
            'pop': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'Pop'", 'blank': 'True'}),
            'smpdus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'SmpDUs'", 'blank': 'True'}),
            'totalppleinarea': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'TotalPpleinArea'", 'blank': 'True'}),
            'totdus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'TotDUs'", 'blank': 'True'})
        },
        u'majitables.sownimpntshslum': {
            'Meta': {'object_name': 'Sownimpntshslum', 'db_table': "u'SownImpNtShSlum'"},
            'dusinarea': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'DusInArea'", 'blank': 'True'}),
            'dusinsmp': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'DUsInSmp'", 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pcntdus': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'pcntDUs'", 'blank': 'True'}),
            'pcntpop': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'PcntPop'", 'blank': 'True'}),
            'pop': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'Pop'", 'blank': 'True'}),
            'slumid': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'SlumID'", 'blank': 'True'}),
            'slumname': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'SlumName'"}),
            'smpdus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'SmpDUs'", 'blank': 'True'}),
            'totalppleinarea': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'TotalPpleinArea'", 'blank': 'True'}),
            'totdus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'TotDUs'", 'blank': 'True'})
        },
        u'majitables.sownimpntshunpcounty': {
            'Meta': {'object_name': 'Sownimpntshunpcounty', 'db_table': "u'SownImpNtShUnpCounty'"},
            'countyid': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'CountyID'", 'blank': 'True'}),
            'countyname': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'CountyName'"}),
            'dusinarea': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'DusInArea'", 'blank': 'True'}),
            'dusinsmp': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'DUsInSmp'", 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pcntdus': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'pcntDUs'", 'blank': 'True'}),
            'pcntpop': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'PcntPop'", 'blank': 'True'}),
            'pop': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'Pop'", 'blank': 'True'}),
            'smpdus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'SmpDUs'", 'blank': 'True'}),
            'totalppleinarea': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'TotalPpleinArea'", 'blank': 'True'}),
            'totdus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'TotDUs'", 'blank': 'True'})
        },
        u'majitables.sownimpntshunpslum': {
            'Meta': {'object_name': 'Sownimpntshunpslum', 'db_table': "u'SownImpNtShUnpSlum'"},
            'dusinarea': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'DusInArea'", 'blank': 'True'}),
            'dusinsmp': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'DUsInSmp'", 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pcntdus': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'pcntDUs'", 'blank': 'True'}),
            'pcntpop': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'PcntPop'", 'blank': 'True'}),
            'pop': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'Pop'", 'blank': 'True'}),
            'slumid': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'SlumID'", 'blank': 'True'}),
            'slumname': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'SlumName'"}),
            'smpdus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'SmpDUs'", 'blank': 'True'}),
            'totalppleinarea': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'TotalPpleinArea'", 'blank': 'True'}),
            'totdus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'TotDUs'", 'blank': 'True'})
        },
        u'majitables.sownimpntshunpwsp': {
            'Meta': {'object_name': 'Sownimpntshunpwsp', 'db_table': "u'SownImpNtShUnpWSP'"},
            'dusinarea': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'DusInArea'", 'blank': 'True'}),
            'dusinsmp': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'DUsInSmp'", 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pcntdus': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'pcntDUs'", 'blank': 'True'}),
            'pcntpop': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'PcntPop'", 'blank': 'True'}),
            'pop': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'Pop'", 'blank': 'True'}),
            'smpdus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'SmpDUs'", 'blank': 'True'}),
            'totalppleinarea': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'TotalPpleinArea'", 'blank': 'True'}),
            'totdus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'TotDUs'", 'blank': 'True'}),
            'wspid': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'WSPID'"}),
            'wspname': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'WSPName'"})
        },
        u'majitables.sownimpntshwsp': {
            'Meta': {'object_name': 'Sownimpntshwsp', 'db_table': "u'SownImpNtShWSP'"},
            'dusinarea': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'DusInArea'", 'blank': 'True'}),
            'dusinsmp': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'DUsInSmp'", 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pcntdus': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'pcntDUs'", 'blank': 'True'}),
            'pcntpop': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'PcntPop'", 'blank': 'True'}),
            'pop': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'Pop'", 'blank': 'True'}),
            'smpdus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'SmpDUs'", 'blank': 'True'}),
            'totalppleinarea': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'TotalPpleinArea'", 'blank': 'True'}),
            'totdus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'TotDUs'", 'blank': 'True'}),
            'wspid': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'WSPID'"}),
            'wspname': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'WSPName'"})
        },
        u'majitables.spractice': {
            'Meta': {'object_name': 'Spractice', 'db_table': "u'SPractice'"},
            'areaid': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'AreaID'", 'blank': 'True'}),
            'areaname': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'Areaname'"}),
            'areasmpdus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'AreaSmpDUs'", 'blank': 'True'}),
            'dus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'DUs'", 'blank': 'True'}),
            'factype': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'FacType'"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ndus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'NDus'", 'blank': 'True'}),
            'numdu': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'NumDU'", 'blank': 'True'}),
            'pcntdus': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'pcntDUs'", 'blank': 'True'})
        },
        u'majitables.ssepbaths': {
            'Meta': {'object_name': 'Ssepbaths', 'db_table': "u'SSepBaths'"},
            'areaid': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'AreaID'", 'blank': 'True'}),
            'areaname': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'Areaname'"}),
            'areasmpdus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'AreaSmpDUs'", 'blank': 'True'}),
            'dus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'DUs'", 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ndus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'NDus'", 'blank': 'True'}),
            'nsepbaths': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'NSepBaths'"}),
            'numdu': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'NumDU'", 'blank': 'True'}),
            'pcntdus': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'pcntDUs'", 'blank': 'True'})
        },
        u'majitables.sseptoilets': {
            'Meta': {'object_name': 'Sseptoilets', 'db_table': "u'SSepToilets'"},
            'areaid': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'AreaID'", 'blank': 'True'}),
            'areaname': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'Areaname'"}),
            'areasmpdus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'AreaSmpDUs'", 'blank': 'True'}),
            'dus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'DUs'", 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ndus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'NDus'", 'blank': 'True'}),
            'numdu': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'NumDU'", 'blank': 'True'}),
            'pcntdus': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'pcntDUs'", 'blank': 'True'}),
            'separatefac': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'SeparateFac'"})
        },
        u'majitables.summaryshtcounty': {
            'Meta': {'object_name': 'Summaryshtcounty', 'db_table': "u'SummaryShtCounty'"},
            'avghhsz': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'AvgHHSz'", 'blank': 'True'}),
            'countyid': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'CountyID'", 'blank': 'True'}),
            'countyname': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'CountyName'"}),
            'drkwatertreated': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'DrkWaterTreated'", 'blank': 'True'}),
            'dusconnected': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'DUsConnected'"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'impsanpop': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'ImpSanPop'", 'blank': 'True'}),
            'mnsrcpcnt': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'MnSrcPcnt'"}),
            'nareas': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'Nareas'", 'blank': 'True'}),
            'nareaslinked': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'NareasLinked'", 'blank': 'True'}),
            'nareasregfloodg': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'NareasRegFloodg'", 'blank': 'True'}),
            'ntowns': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'NTowns'", 'blank': 'True'}),
            'payingforwater': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'PayingforWater'", 'blank': 'True'}),
            'pipedwaterpop': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'PipedWaterPop'"}),
            'plotsconnected': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'PlotsConnected'", 'blank': 'True'}),
            'pop': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'Pop'", 'blank': 'True'}),
            'popplareas': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'PopPlAreas'"}),
            'popunplareas': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'PopUnplAreas'"}),
            'safewaterpop': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'SafeWaterPop'"})
        },
        u'majitables.summaryshtslum': {
            'Meta': {'object_name': 'Summaryshtslum', 'db_table': "u'SummaryShtSlum'"},
            'avghhsz': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'AvgHHSz'", 'blank': 'True'}),
            'drkwatertreated': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'DrkWaterTreated'", 'blank': 'True'}),
            'dusconnected': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'DUsConnected'"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'impsanpop': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'ImpSanPop'"}),
            'mnsrcpcnt': ('django.db.models.fields.CharField', [], {'max_length': '67', 'db_column': "u'MnSrcPcnt'"}),
            'nareas': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'Nareas'", 'blank': 'True'}),
            'nareaslinked': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'NareasLinked'", 'blank': 'True'}),
            'nareasregfloodg': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'NareasRegFloodg'", 'blank': 'True'}),
            'ntowns': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'NTowns'", 'blank': 'True'}),
            'payingforwater': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'PayingforWater'"}),
            'pipedwaterpop': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'PipedWaterPop'"}),
            'plotsconnected': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'PlotsConnected'"}),
            'pop': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'Pop'", 'blank': 'True'}),
            'popplareas': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'PopPlAreas'"}),
            'popunplareas': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'PopUnplAreas'"}),
            'safewaterpop': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'SafeWaterPop'"}),
            'slumid': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'SlumID'", 'blank': 'True'}),
            'slumname': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'SlumName'"})
        },
        u'majitables.summaryshttown': {
            'Meta': {'object_name': 'Summaryshttown', 'db_table': "u'SummaryShtTown'"},
            'avghhsz': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'AvgHHSz'", 'blank': 'True'}),
            'drkwatertreated': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'DrkWaterTreated'", 'blank': 'True'}),
            'dusconnected': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'DUsConnected'"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'impsanpop': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'ImpSanPop'", 'blank': 'True'}),
            'mnsrcpcnt': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'MnSrcPcnt'"}),
            'nareas': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'Nareas'", 'blank': 'True'}),
            'nareaslinked': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'NareasLinked'", 'blank': 'True'}),
            'nareasregfloodg': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'NareasRegFloodg'", 'blank': 'True'}),
            'ntowns': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'Ntowns'", 'blank': 'True'}),
            'payingforwater': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'PayingforWater'", 'blank': 'True'}),
            'pipedwaterpop': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'PipedWaterPop'"}),
            'plotsconnected': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'PlotsConnected'"}),
            'pop': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'Pop'", 'blank': 'True'}),
            'popplareas': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'PopPlAreas'"}),
            'popunplareas': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'PopUnplAreas'"}),
            'safewaterpop': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'SafeWaterPop'"}),
            'townid': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'TownID'", 'blank': 'True'}),
            'townname': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'TownName'"})
        },
        u'majitables.swduhasownrpit': {
            'Meta': {'object_name': 'Swduhasownrpit', 'db_table': "u'SWDUHasOwnRpit'"},
            'areaid': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'AreaID'", 'blank': 'True'}),
            'areaname': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'Areaname'"}),
            'areasmpdus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'AreaSmpDUs'", 'blank': 'True'}),
            'duownrpits': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'DuownRpits'"}),
            'dus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'DUs'", 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ndus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'NDus'", 'blank': 'True'}),
            'numdu': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'NumDU'", 'blank': 'True'}),
            'pcntdus': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'pcntDUs'", 'blank': 'True'})
        },
        u'majitables.swnoofrubpits': {
            'Meta': {'object_name': 'Swnoofrubpits', 'db_table': "u'SWNoofRubPits'"},
            'areaid': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'AreaID'", 'blank': 'True'}),
            'areaname': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'Areaname'"}),
            'areasmpdus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'AreaSmpDUs'", 'blank': 'True'}),
            'dus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'DUs'", 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ndus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'NDus'", 'blank': 'True'}),
            'nrubpits': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'NRubPits'"}),
            'numdu': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'NumDU'", 'blank': 'True'}),
            'pcntdus': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'pcntDUs'", 'blank': 'True'})
        },
        u'majitables.swrpitshared': {
            'Meta': {'object_name': 'Swrpitshared', 'db_table': "u'SWRPitShared'"},
            'areaid': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'AreaID'", 'blank': 'True'}),
            'areaname': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'Areaname'"}),
            'areasmpdus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'AreaSmpDUs'", 'blank': 'True'}),
            'dus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'DUs'", 'blank': 'True'}),
            'dusharerpits': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'DuShareRpits'"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ndus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'NDus'", 'blank': 'True'}),
            'numdu': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'NumDU'", 'blank': 'True'}),
            'pcntdus': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'pcntDUs'", 'blank': 'True'})
        },
        u'majitables.townsareascounties': {
            'Meta': {'object_name': 'TownsareasCounties', 'db_table': "u'TownsAreas-Counties'"},
            'avgpopinarea': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'AvgPopinArea'", 'blank': 'True'}),
            'countyid': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'Countyid'", 'blank': 'True'}),
            'countyname': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'CountyName'"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nareas': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'NAreas'", 'blank': 'True'}),
            'ntowns': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'Ntowns'", 'blank': 'True'}),
            'pop': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'Pop'", 'blank': 'True'})
        },
        u'majitables.townsareasslum': {
            'Meta': {'object_name': 'TownsareasSlum', 'db_table': "u'TownsAreas-Slum'"},
            'avgpopinarea': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'AvgPopinArea'", 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nareas': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'NAreas'", 'blank': 'True'}),
            'ntowns': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'Ntowns'", 'blank': 'True'}),
            'pop': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'Pop'", 'blank': 'True'}),
            'slumid': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'Slumid'"}),
            'slumname': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'SlumName'"})
        },
        u'majitables.townsareastowns': {
            'Meta': {'object_name': 'TownsareasTowns', 'db_table': "u'TownsAreas-Towns'"},
            'avgpopinarea': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'AvgPopinArea'", 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'knbspop': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'KNBSPop'"}),
            'nareas': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'NAreas'", 'blank': 'True'}),
            'ntowns': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'Ntowns'", 'blank': 'True'}),
            'pcntpop': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'PcntPop'"}),
            'pop': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'Pop'", 'blank': 'True'}),
            'townid': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'townID'", 'blank': 'True'}),
            'townname': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'majitables.townsareaswsp': {
            'Meta': {'object_name': 'TownsareasWsp', 'db_table': "u'TownsAreas-WSP'"},
            'avgpopinarea': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'AvgPopinArea'", 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nareas': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'NAreas'", 'blank': 'True'}),
            'ntowns': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'Ntowns'", 'blank': 'True'}),
            'pop': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'Pop'", 'blank': 'True'}),
            'wspid': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'WSPID'"}),
            'wspname': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'WSPName'"})
        },
        u'majitables.wadeqsupallksk': {
            'Meta': {'object_name': 'Wadeqsupallksk', 'db_table': "u'WAdeqSupAllKsk'"},
            'areaid': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'AreaID'", 'blank': 'True'}),
            'areaname': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'Areaname'"}),
            'areapop': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'AreaPop'", 'blank': 'True'}),
            'comwaterksks': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'ComWaterKsks'", 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nadeqsupplied': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'NAdeqSupplied'", 'blank': 'True'}),
            'pubwaterksks': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'PubWaterKsks'", 'blank': 'True'})
        },
        u'majitables.wadeqsupimpwstfsrcs': {
            'Meta': {'object_name': 'Wadeqsupimpwstfsrcs', 'db_table': "u'WAdeqSupImpWSTFSrcs'"},
            'areaid': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'AreaID'", 'blank': 'True'}),
            'areaname': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'Areaname'"}),
            'areapop': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'AreaPop'", 'blank': 'True'}),
            'comtaps': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'ComTaps'", 'blank': 'True'}),
            'comwaterksks': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'ComWaterKsks'", 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nadeqsupplied': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'NAdeqSupplied'", 'blank': 'True'}),
            'pubwaterksks': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'PubWaterKsks'", 'blank': 'True'}),
            'pubwsptaps': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'PubWSPTaps'", 'blank': 'True'}),
            'totalcoveredprivcons': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'TotalCoveredPrivCons'", 'blank': 'True'})
        },
        u'majitables.wadeqsupprivcons10d': {
            'Meta': {'object_name': 'Wadeqsupprivcons10D', 'db_table': "u'WAdeqSupPrivCons-10d'"},
            'areaid': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'AreaID'", 'blank': 'True'}),
            'areaname': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'Areaname'"}),
            'areapop': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'AreaPop'", 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pcoveredownducon': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'PCoveredOwnDuCon'"}),
            'pcoveredpcon': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'PCoveredPCon'"}),
            'totalcoveredprivcons': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'TotalCoveredPrivCons'", 'blank': 'True'})
        },
        u'majitables.wadeqsuppubtap10d': {
            'Meta': {'object_name': 'Wadeqsuppubtap10D', 'db_table': "u'WAdeqSupPubTap-10d'"},
            'areaid': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'AreaID'", 'blank': 'True'}),
            'areaname': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'Areaname'"}),
            'areapop': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'AreaPop'", 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'noadeqsupplied': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'NoAdeqSupplied'", 'blank': 'True'}),
            'nopubcomtaps': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'NoPubComTaps'", 'blank': 'True'})
        },
        u'majitables.wadeqsupwspksk': {
            'Meta': {'object_name': 'Wadeqsupwspksk', 'db_table': "u'WAdeqSupWSPKsk'"},
            'areaid': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'AreaID'", 'blank': 'True'}),
            'areaname': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'Areaname'"}),
            'areapop': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'AreaPop'", 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nadeqsupplied': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'NAdeqSupplied'", 'blank': 'True'}),
            'pubwaterksks': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'PubWaterKsks'", 'blank': 'True'})
        },
        u'majitables.wareasmnprob33county': {
            'Meta': {'object_name': 'Wareasmnprob33County', 'db_table': "u'WAreasMnProb33County'"},
            'countyid': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'CountyId'", 'blank': 'True'}),
            'countyname': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'Countyname'"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mainproblem': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'MainProblem'"}),
            'nareas': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'NAreas'", 'blank': 'True'}),
            'pcntareas': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'PcntAreas'", 'blank': 'True'}),
            'totareas': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'TotAreas'", 'blank': 'True'})
        },
        u'majitables.wareasmnprob33slum': {
            'Meta': {'object_name': 'Wareasmnprob33Slum', 'db_table': "u'WAreasMnProb33Slum'"},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mainproblem': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'MainProblem'"}),
            'nareas': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'NAreas'", 'blank': 'True'}),
            'pcntareas': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'PcntAreas'", 'blank': 'True'}),
            'slumid': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'SlumId'", 'blank': 'True'}),
            'slumname': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'Slumname'"}),
            'totareas': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'TotAreas'", 'blank': 'True'})
        },
        u'majitables.wareasmnprob33town': {
            'Meta': {'object_name': 'Wareasmnprob33Town', 'db_table': "u'WAreasMnProb33Town'"},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mainproblem': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'MainProblem'"}),
            'nareas': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'NAreas'", 'blank': 'True'}),
            'pcntareas': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'PcntAreas'", 'blank': 'True'}),
            'totareas': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'TotAreas'", 'blank': 'True'}),
            'townid': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'TownId'", 'blank': 'True'}),
            'townname': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'Townname'"})
        },
        u'majitables.wareasmnprob33wsp': {
            'Meta': {'object_name': 'Wareasmnprob33Wsp', 'db_table': "u'WAreasMnProb33WSP'"},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mainproblem': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'MainProblem'"}),
            'nareas': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'NAreas'", 'blank': 'True'}),
            'pcntareas': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'PcntAreas'", 'blank': 'True'}),
            'totareas': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'TotAreas'", 'blank': 'True'}),
            'wspid': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'WSPId'"}),
            'wspname': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'WSPname'"})
        },
        u'majitables.wareasnwlinkcounty': {
            'Meta': {'object_name': 'Wareasnwlinkcounty', 'db_table': "u'WAreasNWLinkCounty'"},
            'arealinkedwater': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'AreaLinkedwater'"}),
            'countyid': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'CountyId'", 'blank': 'True'}),
            'countyname': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'Countyname'"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nareas': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'Nareas'", 'blank': 'True'}),
            'pcntareas': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'PcntAreas'", 'blank': 'True'}),
            'totareas': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'TotAreas'", 'blank': 'True'})
        },
        u'majitables.wareasnwlinkslum': {
            'Meta': {'object_name': 'Wareasnwlinkslum', 'db_table': "u'WAreasNWLinkSlum'"},
            'arealinkedwater': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'AreaLinkedwater'"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nareas': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'Nareas'", 'blank': 'True'}),
            'pcntareas': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'PcntAreas'", 'blank': 'True'}),
            'slumid': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'SlumId'", 'blank': 'True'}),
            'slumname': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'Slumname'"}),
            'totareas': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'TotAreas'", 'blank': 'True'})
        },
        u'majitables.wareasnwlinktown': {
            'Meta': {'object_name': 'Wareasnwlinktown', 'db_table': "u'WAreasNWLinkTown'"},
            'arealinkedwater': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'AreaLinkedwater'"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nareas': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'Nareas'", 'blank': 'True'}),
            'pcntareas': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'PcntAreas'", 'blank': 'True'}),
            'totareas': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'TotAreas'", 'blank': 'True'}),
            'townid': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'TownId'", 'blank': 'True'}),
            'townname': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'Townname'"})
        },
        u'majitables.wareasnwlinkwsp': {
            'Meta': {'object_name': 'Wareasnwlinkwsp', 'db_table': "u'WAreasNWLinkWSP'"},
            'arealinkedwater': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'AreaLinkedwater'"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nareas': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'Nareas'", 'blank': 'True'}),
            'pcntareas': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'PcntAreas'", 'blank': 'True'}),
            'totareas': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'TotAreas'", 'blank': 'True'}),
            'wspid': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'WSPId'"}),
            'wspname': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'WSPname'"})
        },
        u'majitables.wareastechstatcounty': {
            'Meta': {'object_name': 'Wareastechstatcounty', 'db_table': "u'WAreasTechstatCounty'"},
            'countyid': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'CountyId'", 'blank': 'True'}),
            'countyname': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'Countyname'"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nareas': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'Nareas'", 'blank': 'True'}),
            'pcntareas': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'PcntAreas'", 'blank': 'True'}),
            'techstat': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'TechStat'"}),
            'totareas': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'TotAreas'", 'blank': 'True'})
        },
        u'majitables.wareastechstatslum': {
            'Meta': {'object_name': 'Wareastechstatslum', 'db_table': "u'WAreasTechstatSlum'"},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nareas': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'Nareas'", 'blank': 'True'}),
            'pcntareas': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'PcntAreas'", 'blank': 'True'}),
            'slumid': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'SlumId'", 'blank': 'True'}),
            'slumname': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'Slumname'"}),
            'techstat': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'TechStat'"}),
            'totareas': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'TotAreas'", 'blank': 'True'})
        },
        u'majitables.wareastechstattown': {
            'Meta': {'object_name': 'Wareastechstattown', 'db_table': "u'WAreasTechstatTown'"},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nareas': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'Nareas'", 'blank': 'True'}),
            'pcntareas': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'PcntAreas'", 'blank': 'True'}),
            'techstat': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'TechStat'"}),
            'totareas': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'TotAreas'", 'blank': 'True'}),
            'townid': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'TownId'", 'blank': 'True'}),
            'townname': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'Townname'"})
        },
        u'majitables.wareastechstatwsp': {
            'Meta': {'object_name': 'Wareastechstatwsp', 'db_table': "u'WAreasTechstatWSP'"},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nareas': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'Nareas'", 'blank': 'True'}),
            'pcntareas': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'PcntAreas'", 'blank': 'True'}),
            'techstat': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'TechStat'"}),
            'totareas': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'TotAreas'", 'blank': 'True'}),
            'wspid': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'WSPId'"}),
            'wspname': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'WSPname'"})
        },
        u'majitables.wateroutlets': {
            'Meta': {'object_name': 'Wateroutlets', 'db_table': "u'WaterOutlets'"},
            'areaid': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'AreaID'", 'blank': 'True'}),
            'areaname': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'AreaName'", 'blank': 'True'}),
            'comtaps': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'ComTaps'", 'blank': 'True'}),
            'comwaterksks': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'ComWaterKsks'", 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'privtaps': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'PrivTaps'", 'blank': 'True'}),
            'privwaterksks': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'PrivWaterKsks'", 'blank': 'True'}),
            'pubwaterksks': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'PubWaterKsks'", 'blank': 'True'}),
            'pubwsptaps': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'PubWSPTaps'", 'blank': 'True'})
        },
        u'majitables.waterpaiddu': {
            'Meta': {'object_name': 'Waterpaiddu', 'db_table': "u'WaterPaidDU'"},
            'areaid': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'AreaID'", 'blank': 'True'}),
            'areaname': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'Areaname'"}),
            'areasmpdus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'AreaSmpDUs'", 'blank': 'True'}),
            'dusinarea': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'DusInArea'", 'blank': 'True'}),
            'dusinsmp': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'DUsInSmp'", 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pcntdus': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'pcntDUs'", 'blank': 'True'}),
            'totaldusinarea': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'TotalDUsInArea'", 'blank': 'True'}),
            'waterpaid': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'WaterPaid'"})
        },
        u'majitables.waterpaymthddu': {
            'Meta': {'object_name': 'Waterpaymthddu', 'db_table': "u'WaterPayMthdDU'"},
            'areaid': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'AreaID'", 'blank': 'True'}),
            'areaname': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'Areaname'"}),
            'dus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'DUs'", 'blank': 'True'}),
            'dusinarea': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'DUsInArea'", 'blank': 'True'}),
            'dusinsmp': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'DUsInSmp'", 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pcntdus': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'pcntDUs'", 'blank': 'True'}),
            'totaldusinarea': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'TotalDUsInArea'", 'blank': 'True'}),
            'wpaid': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'Wpaid'"}),
            'wpaymthd': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'WPayMthd'"})
        },
        u'majitables.waterqlty9': {
            'Meta': {'object_name': 'Waterqlty9', 'db_table': "u'WaterQlty-9'"},
            'areaid': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'AreaID'", 'blank': 'True'}),
            'areaname': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'Areaname'"}),
            'areasmpdus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'AreaSmpDUs'", 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ndus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'NDus'", 'blank': 'True'}),
            'numdu': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'numDU'", 'blank': 'True'}),
            'pcntplotsusingsrc': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'pcntppleusingsrc': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'persons': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'smpusingsrc': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'Smpusingsrc'", 'blank': 'True'}),
            'waterqlty': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'WaterQlty'"})
        },
        u'majitables.watersrcbath9': {
            'Meta': {'object_name': 'Watersrcbath9', 'db_table': "u'WaterSrcBath-9'"},
            'areaid': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'AreaID'", 'blank': 'True'}),
            'areaname': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'Areaname'"}),
            'areasmpdus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'AreaSmpDUs'", 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ndus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'NDus'", 'blank': 'True'}),
            'numdu': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'NumDU'", 'blank': 'True'}),
            'pcntplotsusingsrc': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'pcntppleusingsrc': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'persons': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'smpusingsrc': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'Smpusingsrc'", 'blank': 'True'}),
            'watersrcbath': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'WaterSrcBath'"})
        },
        u'majitables.watersrcckg9': {
            'Meta': {'object_name': 'Watersrcckg9', 'db_table': "u'WaterSrcCkg-9'"},
            'areaid': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'AreaID'", 'blank': 'True'}),
            'areaname': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'Areaname'"}),
            'areasmpdus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'AreaSmpDUs'", 'blank': 'True'}),
            'ckgwatersrc': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'CkgWaterSrc'"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ndus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'NDus'", 'blank': 'True'}),
            'nousingsrc': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'Nousingsrc'", 'blank': 'True'}),
            'numdu': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'NumDU'", 'blank': 'True'}),
            'pcntplotsusingsrc': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'pcntppleusingsrc': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'persons': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'})
        },
        u'majitables.watersrcdrk9': {
            'Meta': {'object_name': 'Watersrcdrk9', 'db_table': "u'WaterSrcDrk-9'"},
            'areaid': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'AreaID'", 'blank': 'True'}),
            'areaname': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'Areaname'"}),
            'areasmpdus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'AreaSmpDUs'", 'blank': 'True'}),
            'drkgwatersrc': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'DrkgWaterSrc'"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ndus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'NDus'", 'blank': 'True'}),
            'nppleusingsrc': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'Nppleusingsrc'", 'blank': 'True'}),
            'numdu': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'NumDU'", 'blank': 'True'}),
            'pcntdususingsrc': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'pcntDUsusingsrc'", 'blank': 'True'}),
            'pcntppleusingsrc': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'smpusingsrc': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'Smpusingsrc'", 'blank': 'True'})
        },
        u'majitables.watersrclndry9': {
            'Meta': {'object_name': 'Watersrclndry9', 'db_table': "u'WaterSrcLndry-9'"},
            'areaid': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'AreaID'", 'blank': 'True'}),
            'areaname': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'Areaname'"}),
            'areasmpdus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'AreaSmpDUs'", 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ndus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'NDus'", 'blank': 'True'}),
            'numdu': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'NumDU'", 'blank': 'True'}),
            'pcntplotsusingsrc': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'pcntppleusingsrc': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'persons': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'smpusingsrc': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'Smpusingsrc'", 'blank': 'True'}),
            'watersrclndry': ('django.db.models.fields.TextField', [], {'db_column': "u'WaterSrcLndry'"})
        },
        u'majitables.waterstoragedu': {
            'Meta': {'object_name': 'Waterstoragedu', 'db_table': "u'WaterStorageDU'"},
            'areaid': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'AreaID'", 'blank': 'True'}),
            'areaname': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'Areaname'"}),
            'areasmpdus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'AreaSmpDUs'", 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ndus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'NDus'", 'blank': 'True'}),
            'numdu': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'numDU'", 'blank': 'True'}),
            'pcntdus': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'pcntDUs'", 'blank': 'True'}),
            'pcntpple': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'persons': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'smpdus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'SmpDUs'", 'blank': 'True'}),
            'storagemthd': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'StorageMthd'"})
        },
        u'majitables.watertrt33county': {
            'Meta': {'object_name': 'Watertrt33County', 'db_table': "u'WaterTrt33County'"},
            'countyid': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'CountyID'", 'blank': 'True'}),
            'countyname': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'CountyName'"}),
            'drkwatertreated': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'DrkWaterTreated'"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nousingsrc': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'NoUsingSrc'", 'blank': 'True'}),
            'pcntdususingsrc': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'pcntDUsusingsrc'", 'blank': 'True'}),
            'smpdus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'SmpDUs'", 'blank': 'True'}),
            'smpsrc': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'SmpSrc'", 'blank': 'True'}),
            'totdus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'TotDUs'", 'blank': 'True'})
        },
        u'majitables.watertrt33slum': {
            'Meta': {'object_name': 'Watertrt33Slum', 'db_table': "u'WaterTrt33Slum'"},
            'drkwatertreated': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'DrkWaterTreated'"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nousingsrc': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'NoUsingSrc'", 'blank': 'True'}),
            'pcntdususingsrc': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'pcntDUsusingsrc'", 'blank': 'True'}),
            'slumid': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'SlumID'", 'blank': 'True'}),
            'slumname': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'SlumName'"}),
            'smpdus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'SmpDUs'", 'blank': 'True'}),
            'smpsrc': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'SmpSrc'", 'blank': 'True'}),
            'totdus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'TotDUs'", 'blank': 'True'})
        },
        u'majitables.watertrt33town': {
            'Meta': {'object_name': 'Watertrt33Town', 'db_table': "u'WaterTrt33Town'"},
            'drkwatertreated': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'DrkWaterTreated'"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nousingsrc': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'NoUsingSrc'", 'blank': 'True'}),
            'pcntdususingsrc': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'pcntDUsusingsrc'", 'blank': 'True'}),
            'smpdus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'SmpDUs'", 'blank': 'True'}),
            'smpsrc': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'SmpSrc'", 'blank': 'True'}),
            'totdus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'TotDUs'", 'blank': 'True'}),
            'townid': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'TownID'", 'blank': 'True'}),
            'townname': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'TownName'"})
        },
        u'majitables.watertrt33wsp': {
            'Meta': {'object_name': 'Watertrt33Wsp', 'db_table': "u'WaterTrt33WSP'"},
            'drkwatertreated': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'DrkWaterTreated'"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nousingsrc': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'NoUsingSrc'", 'blank': 'True'}),
            'pcntdususingsrc': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'pcntDUsusingsrc'", 'blank': 'True'}),
            'smpdus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'SmpDUs'", 'blank': 'True'}),
            'smpsrc': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'SmpSrc'", 'blank': 'True'}),
            'totdus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'TotDUs'", 'blank': 'True'}),
            'wspid': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'WSPID'"}),
            'wspname': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'WSPName'"})
        },
        u'majitables.watertrtdu9': {
            'Meta': {'object_name': 'Watertrtdu9', 'db_table': "u'WaterTrtDU-9'"},
            'areaid': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'AreaID'", 'blank': 'True'}),
            'areaname': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'Areaname'"}),
            'areasmpdus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'AreaSmpDUs'", 'blank': 'True'}),
            'drkwatertreated': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'DrkWaterTreated'"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ndus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'NDus'", 'blank': 'True'}),
            'numdu': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'numDU'", 'blank': 'True'}),
            'pcntdus': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'pcntDUs'", 'blank': 'True'}),
            'pcntpple': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'persons': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'smpusingsrc': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'Smpusingsrc'", 'blank': 'True'})
        },
        u'majitables.watertrtmthddu': {
            'Meta': {'object_name': 'Watertrtmthddu', 'db_table': "u'WaterTrtMthdDU'"},
            'areaid': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'AreaID'", 'blank': 'True'}),
            'areaname': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'Areaname'"}),
            'drkwatertrtmthd': ('django.db.models.fields.TextField', [], {'db_column': "u'DrkWaterTrtMthd'", 'blank': 'True'}),
            'dus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'DUs'", 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ndu': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'NDU'", 'blank': 'True'}),
            'ndus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'NDus'", 'blank': 'True'}),
            'numdu': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'numDU'", 'blank': 'True'}),
            'pcntdus': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'pcntDUs'", 'blank': 'True'})
        },
        u'majitables.watertrtstorage': {
            'Meta': {'object_name': 'Watertrtstorage', 'db_table': "u'WaterTrtStorage'"},
            'areaid': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'AreaID'", 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'infwaterqlty': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'InfWaterQlty'"}),
            'storagemthd': ('django.db.models.fields.TextField', [], {'db_column': "u'StorageMthd'", 'blank': 'True'}),
            'watertreated': ('django.db.models.fields.TextField', [], {'db_column': "u'WaterTreated'", 'blank': 'True'}),
            'wspwaterqlty': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'WSPWaterQlty'"}),
            'wtrtmethods': ('django.db.models.fields.TextField', [], {'db_column': "u'WtrtMethods'", 'blank': 'True'})
        },
        u'majitables.wckgsrcpipedcounty': {
            'Meta': {'object_name': 'Wckgsrcpipedcounty', 'db_table': "u'WCkgSrcPipedCounty'"},
            'countyid': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'CountyID'", 'blank': 'True'}),
            'countyname': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'CountyName'"}),
            'dusinarea': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'DusInArea'", 'blank': 'True'}),
            'dusinsmp': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'DUsInSmp'", 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pcntdus': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'pcntDUs'", 'blank': 'True'}),
            'pcntpop': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'PcntPop'", 'blank': 'True'}),
            'pop': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'Pop'", 'blank': 'True'}),
            'smpdus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'SmpDUs'", 'blank': 'True'}),
            'totalppleinarea': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'TotalPpleinArea'", 'blank': 'True'}),
            'totdus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'TotDUs'", 'blank': 'True'})
        },
        u'majitables.wckgsrcpipedslum': {
            'Meta': {'object_name': 'Wckgsrcpipedslum', 'db_table': "u'WCkgSrcPipedSlum'"},
            'dusinarea': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'DusInArea'", 'blank': 'True'}),
            'dusinsmp': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'DUsInSmp'", 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pcntdus': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'pcntDUs'", 'blank': 'True'}),
            'pcntpop': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'PcntPop'", 'blank': 'True'}),
            'pop': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'Pop'", 'blank': 'True'}),
            'slumid': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'SlumID'", 'blank': 'True'}),
            'slumname': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'SlumName'"}),
            'smpdus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'SmpDUs'", 'blank': 'True'}),
            'totalppleinarea': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'TotalPpleinArea'", 'blank': 'True'}),
            'totdus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'TotDUs'", 'blank': 'True'})
        },
        u'majitables.wckgsrcpipedtown': {
            'Meta': {'object_name': 'Wckgsrcpipedtown', 'db_table': "u'WCkgSrcPipedTown'"},
            'dusinarea': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'DusInArea'", 'blank': 'True'}),
            'dusinsmp': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'DUsInSmp'", 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pcntdus': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'pcntDUs'", 'blank': 'True'}),
            'pcntpop': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'PcntPop'", 'blank': 'True'}),
            'pop': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'Pop'", 'blank': 'True'}),
            'smpdus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'SmpDUs'", 'blank': 'True'}),
            'totalppleinarea': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'TotalPpleinArea'", 'blank': 'True'}),
            'totdus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'TotDUs'", 'blank': 'True'}),
            'townid': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'TownID'", 'blank': 'True'}),
            'townname': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'TownName'"})
        },
        u'majitables.wckgsrcpipedwsp': {
            'Meta': {'object_name': 'Wckgsrcpipedwsp', 'db_table': "u'WCkgSrcPipedWSP'"},
            'dusinarea': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'DusInArea'", 'blank': 'True'}),
            'dusinsmp': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'DUsInSmp'", 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pcntdus': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'pcntDUs'", 'blank': 'True'}),
            'pcntpop': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'PcntPop'", 'blank': 'True'}),
            'pop': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'Pop'", 'blank': 'True'}),
            'smpdus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'SmpDUs'", 'blank': 'True'}),
            'totalppleinarea': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'TotalPpleinArea'", 'blank': 'True'}),
            'totdus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'TotDUs'", 'blank': 'True'}),
            'wspid': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'WSPID'"}),
            'wspname': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'WSPName'"})
        },
        u'majitables.wconstatus34county': {
            'Meta': {'object_name': 'Wconstatus34County', 'db_table': "u'WConStatus34County'"},
            'constatus': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'ConStatus'"}),
            'countyid': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'CountyID'", 'blank': 'True'}),
            'countyname': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'CountyName'"}),
            'dusinarea': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'DUsInArea'", 'blank': 'True'}),
            'dusinsmp': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'DUsInSmp'", 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pcntdus': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'pcntDUs'", 'blank': 'True'}),
            'smpdus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'SmpDUs'", 'blank': 'True'}),
            'totdus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'TotDUs'", 'blank': 'True'})
        },
        u'majitables.wconstatus34slum': {
            'Meta': {'object_name': 'Wconstatus34Slum', 'db_table': "u'WConStatus34Slum'"},
            'constatus': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'ConStatus'"}),
            'dusinarea': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'DUsInArea'", 'blank': 'True'}),
            'dusinsmp': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'DUsInSmp'", 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pcntdus': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'pcntDUs'", 'blank': 'True'}),
            'slumid': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'SlumID'", 'blank': 'True'}),
            'slumname': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'SlumName'"}),
            'smpdus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'SmpDUs'", 'blank': 'True'}),
            'totdus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'TotDUs'", 'blank': 'True'})
        },
        u'majitables.wconstatus34town': {
            'Meta': {'object_name': 'Wconstatus34Town', 'db_table': "u'WConStatus34Town'"},
            'constatus': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'ConStatus'"}),
            'dusinarea': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'DUsInArea'", 'blank': 'True'}),
            'dusinsmp': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'DUsInSmp'", 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pcntdus': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'pcntDUs'", 'blank': 'True'}),
            'smpdus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'SmpDUs'", 'blank': 'True'}),
            'totdus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'TotDUs'", 'blank': 'True'}),
            'townid': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'TownID'", 'blank': 'True'}),
            'townname': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'TownName'"})
        },
        u'majitables.wconstatus34wsp': {
            'Meta': {'object_name': 'Wconstatus34Wsp', 'db_table': "u'WConStatus34WSP'"},
            'constatus': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'ConStatus'"}),
            'dusinarea': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'DUsInArea'", 'blank': 'True'}),
            'dusinsmp': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'DUsInSmp'", 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pcntdus': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'pcntDUs'", 'blank': 'True'}),
            'smpdus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'SmpDUs'", 'blank': 'True'}),
            'totdus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'TotDUs'", 'blank': 'True'}),
            'wspid': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'WSPID'"}),
            'wspname': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'WSPName'"})
        },
        u'majitables.wconstatusdu': {
            'Meta': {'object_name': 'WconstatusDu', 'db_table': "u'WConStatus-DU'"},
            'areaid': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'AreaID'", 'blank': 'True'}),
            'areaname': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'Areaname'"}),
            'constatus': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'ConStatus'"}),
            'dusinarea': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'DUsInArea'", 'blank': 'True'}),
            'dusinsmp': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'DUsInSmp'", 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pcntdus': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'pcntDUs'", 'blank': 'True'}),
            'smpduscon': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'SmpDUsCon'", 'blank': 'True'})
        },
        u'majitables.wconsumption': {
            'Meta': {'object_name': 'Wconsumption', 'db_table': "u'WConsumption'"},
            'areaid': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'AreaID'", 'blank': 'True'}),
            'areaname': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'Areaname'"}),
            'areasmpdus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'AreaSmpDUs'", 'blank': 'True'}),
            'dus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'DUs'", 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ndus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'NDus'", 'blank': 'True'}),
            'numdu': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'NumDU'", 'blank': 'True'}),
            'pcntdus': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'pcntDUs'", 'blank': 'True'}),
            'wmthconsum': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'WMthconsum'"})
        },
        u'majitables.wdrkqlty33county': {
            'Meta': {'object_name': 'Wdrkqlty33County', 'db_table': "u'WDrkQlty33County'"},
            'countyid': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'CountyID'", 'blank': 'True'}),
            'countyname': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'CountyName'"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nousingsrc': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'NoUsingSrc'", 'blank': 'True'}),
            'pcntdususingsrc': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'pcntDUsusingsrc'", 'blank': 'True'}),
            'smpdus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'SmpDUs'", 'blank': 'True'}),
            'smpsrc': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'SmpSrc'", 'blank': 'True'}),
            'totdus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'TotDUs'", 'blank': 'True'}),
            'wqlty': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'WQlty'"})
        },
        u'majitables.wdrkqlty33slum': {
            'Meta': {'object_name': 'Wdrkqlty33Slum', 'db_table': "u'WDrkQlty33Slum'"},
            'countyid': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'CountyID'", 'blank': 'True'}),
            'countyname': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'CountyName'"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nousingsrc': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'NoUsingSrc'", 'blank': 'True'}),
            'pcntdususingsrc': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'pcntDUsusingsrc'", 'blank': 'True'}),
            'smpdus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'SmpDUs'", 'blank': 'True'}),
            'smpsrc': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'SmpSrc'", 'blank': 'True'}),
            'totdus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'TotDUs'", 'blank': 'True'}),
            'wqlty': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'WQlty'"})
        },
        u'majitables.wdrkqlty33town': {
            'Meta': {'object_name': 'Wdrkqlty33Town', 'db_table': "u'WDrkQlty33Town'"},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nousingsrc': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'NoUsingSrc'", 'blank': 'True'}),
            'pcntdususingsrc': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'pcntDUsusingsrc'", 'blank': 'True'}),
            'smpdus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'SmpDUs'", 'blank': 'True'}),
            'smpsrc': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'SmpSrc'", 'blank': 'True'}),
            'totdus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'TotDUs'", 'blank': 'True'}),
            'townid': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'TownID'", 'blank': 'True'}),
            'townname': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'TownName'"}),
            'wqlty': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'WQlty'"})
        },
        u'majitables.wdrkqlty33wsp': {
            'Meta': {'object_name': 'Wdrkqlty33Wsp', 'db_table': "u'WDrkQlty33WSP'"},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nousingsrc': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'NoUsingSrc'", 'blank': 'True'}),
            'pcntdususingsrc': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'pcntDUsusingsrc'", 'blank': 'True'}),
            'smpdus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'SmpDUs'", 'blank': 'True'}),
            'smpsrc': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'SmpSrc'", 'blank': 'True'}),
            'totdus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'TotDUs'", 'blank': 'True'}),
            'wqlty': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'WQlty'"}),
            'wspid': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'WSPID'"}),
            'wspname': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'WSPName'"})
        },
        u'majitables.wdrksrc33county': {
            'Meta': {'object_name': 'Wdrksrc33County', 'db_table': "u'WDrkSrc33County'"},
            'countyid': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'CountyID'", 'blank': 'True'}),
            'countyname': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'CountyName'"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nousingsrc': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'NoUsingSrc'", 'blank': 'True'}),
            'pcntdususingsrc': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'pcntDUsusingsrc'", 'blank': 'True'}),
            'smpdus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'SmpDUs'", 'blank': 'True'}),
            'smpsrc': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'SmpSrc'", 'blank': 'True'}),
            'totdus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'TotDUs'", 'blank': 'True'}),
            'wdrksrc': ('django.db.models.fields.CharField', [], {'max_length': '61', 'db_column': "u'WDrkSrc'"})
        },
        u'majitables.wdrksrc33slum': {
            'Meta': {'object_name': 'Wdrksrc33Slum', 'db_table': "u'WDrkSrc33Slum'"},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nousingsrc': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'NoUsingSrc'", 'blank': 'True'}),
            'pcntdususingsrc': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'pcntDUsusingsrc'", 'blank': 'True'}),
            'slumid': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'SlumID'", 'blank': 'True'}),
            'slumname': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'SlumName'"}),
            'smpdus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'SmpDUs'", 'blank': 'True'}),
            'smpsrc': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'SmpSrc'", 'blank': 'True'}),
            'totdus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'TotDUs'", 'blank': 'True'}),
            'wdrksrc': ('django.db.models.fields.CharField', [], {'max_length': '61', 'db_column': "u'WDrkSrc'"})
        },
        u'majitables.wdrksrc33town': {
            'Meta': {'object_name': 'Wdrksrc33Town', 'db_table': "u'WDrkSrc33Town'"},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nousingsrc': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'NoUsingSrc'", 'blank': 'True'}),
            'pcntdususingsrc': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'pcntDUsusingsrc'", 'blank': 'True'}),
            'smpdus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'SmpDUs'", 'blank': 'True'}),
            'smpsrc': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'SmpSrc'", 'blank': 'True'}),
            'totdus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'TotDUs'", 'blank': 'True'}),
            'townid': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'TownID'", 'blank': 'True'}),
            'townname': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'TownName'"}),
            'wdrksrc': ('django.db.models.fields.CharField', [], {'max_length': '61', 'db_column': "u'WDrkSrc'"})
        },
        u'majitables.wdrksrc33wsp': {
            'Meta': {'object_name': 'Wdrksrc33Wsp', 'db_table': "u'WDrkSrc33WSP'"},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nousingsrc': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'NoUsingSrc'", 'blank': 'True'}),
            'pcntdususingsrc': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'pcntDUsusingsrc'", 'blank': 'True'}),
            'smpdus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'SmpDUs'", 'blank': 'True'}),
            'smpsrc': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'SmpSrc'", 'blank': 'True'}),
            'totdus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'TotDUs'", 'blank': 'True'}),
            'wdrksrc': ('django.db.models.fields.CharField', [], {'max_length': '61', 'db_column': "u'WDrkSrc'"}),
            'wspid': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'WSPID'"}),
            'wspname': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'WSPName'"})
        },
        u'majitables.wdrksrcbyqltycounty37': {
            'Meta': {'object_name': 'Wdrksrcbyqltycounty37', 'db_table': "u'WDrkSrcByQltyCounty-37'"},
            'countyid': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'CountyID'", 'blank': 'True'}),
            'countyname': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'CountyName'"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nousingsrc': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'NoUsingSrc'", 'blank': 'True'}),
            'pcntdususingsrc': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'pcntDUsusingsrc'", 'blank': 'True'}),
            'smpdus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'SmpDUs'", 'blank': 'True'}),
            'smpsrc': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'SmpSrc'", 'blank': 'True'}),
            'totdus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'TotDUs'", 'blank': 'True'}),
            'wdrksrc': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'WDrkSrc'"}),
            'wqlty': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'WQlty'"})
        },
        u'majitables.wdrksrcbyqltyslum37': {
            'Meta': {'object_name': 'Wdrksrcbyqltyslum37', 'db_table': "u'WDrkSrcByQltySlum-37'"},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nousingsrc': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'NoUsingSrc'", 'blank': 'True'}),
            'pcntdususingsrc': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'pcntDUsusingsrc'", 'blank': 'True'}),
            'slumid': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'SlumID'", 'blank': 'True'}),
            'slumname': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'SlumName'"}),
            'smpdus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'SmpDUs'", 'blank': 'True'}),
            'smpsrc': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'SmpSrc'", 'blank': 'True'}),
            'totdus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'TotDUs'", 'blank': 'True'}),
            'wdrksrc': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'WDrkSrc'"}),
            'wqlty': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'WQlty'"})
        },
        u'majitables.wdrksrcbyqltytown37': {
            'Meta': {'object_name': 'Wdrksrcbyqltytown37', 'db_table': "u'WDrkSrcByQltyTown-37'"},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nousingsrc': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'NoUsingSrc'", 'blank': 'True'}),
            'pcntdususingsrc': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'pcntDUsusingsrc'", 'blank': 'True'}),
            'smpdus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'SmpDUs'", 'blank': 'True'}),
            'smpsrc': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'SmpSrc'", 'blank': 'True'}),
            'totdus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'TotDUs'", 'blank': 'True'}),
            'townid': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'TownID'", 'blank': 'True'}),
            'townname': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'TownName'"}),
            'wdrksrc': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'WDrkSrc'"}),
            'wqlty': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'WQlty'"})
        },
        u'majitables.wdrksrcbyqltywsp37': {
            'Meta': {'object_name': 'Wdrksrcbyqltywsp37', 'db_table': "u'WDrkSrcByQltyWSP-37'"},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nousingsrc': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'NoUsingSrc'", 'blank': 'True'}),
            'pcntdususingsrc': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'pcntDUsusingsrc'", 'blank': 'True'}),
            'smpdus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'SmpDUs'", 'blank': 'True'}),
            'smpsrc': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'SmpSrc'", 'blank': 'True'}),
            'totdus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'TotDUs'", 'blank': 'True'}),
            'wdrksrc': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'WDrkSrc'"}),
            'wqlty': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'WQlty'"}),
            'wspid': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'WSPID'"}),
            'wspname': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'WSPName'"})
        },
        u'majitables.wdrksrcbytrtmthdslum38': {
            'Meta': {'object_name': 'Wdrksrcbytrtmthdslum38', 'db_table': "u'WDrkSrcByTrtMthdSlum-38'"},
            'drkwatertrtmthd': ('django.db.models.fields.TextField', [], {'db_column': "u'DrkWaterTrtMthd'"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nousingsrc': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'NoUsingSrc'", 'blank': 'True'}),
            'pcntdususingsrc': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'pcntDUsusingsrc'", 'blank': 'True'}),
            'slumid': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'SlumID'", 'blank': 'True'}),
            'slumname': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'SlumName'"}),
            'smpdus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'SmpDUs'", 'blank': 'True'}),
            'smpsrc': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'SmpSrc'", 'blank': 'True'}),
            'totdus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'TotDUs'", 'blank': 'True'}),
            'wdrksrc': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'WDrkSrc'"})
        },
        u'majitables.wdrksrcbytrtmthdtown38': {
            'Meta': {'object_name': 'Wdrksrcbytrtmthdtown38', 'db_table': "u'WDrkSrcByTrtMthdTown-38'"},
            'drkwatertrtmthd': ('django.db.models.fields.CharField', [], {'max_length': '65', 'db_column': "u'DrkWaterTrtMthd'"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nousingsrc': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'NoUsingSrc'", 'blank': 'True'}),
            'pcntdususingsrc': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'pcntDUsusingsrc'", 'blank': 'True'}),
            'smpdus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'SmpDUs'", 'blank': 'True'}),
            'smpsrc': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'SmpSrc'", 'blank': 'True'}),
            'totdus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'TotDUs'", 'blank': 'True'}),
            'townid': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'TownID'", 'blank': 'True'}),
            'townname': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'TownName'"}),
            'wdrksrc': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'WDrkSrc'"})
        },
        u'majitables.wdrksrcbytrtmthdwsp38': {
            'Meta': {'object_name': 'Wdrksrcbytrtmthdwsp38', 'db_table': "u'WDrkSrcByTrtMthdWSP-38'"},
            'drkwatertrtmthd': ('django.db.models.fields.CharField', [], {'max_length': '65', 'db_column': "u'DrkWaterTrtMthd'"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nousingsrc': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'NoUsingSrc'", 'blank': 'True'}),
            'pcntdususingsrc': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'pcntDUsusingsrc'", 'blank': 'True'}),
            'smpdus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'SmpDUs'", 'blank': 'True'}),
            'smpsrc': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'SmpSrc'", 'blank': 'True'}),
            'totdus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'TotDUs'", 'blank': 'True'}),
            'wdrksrc': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'WDrkSrc'"}),
            'wspid': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'WSPID'"}),
            'wspname': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'WSPName'"})
        },
        u'majitables.wdrksrccmtaps10d': {
            'Meta': {'object_name': 'Wdrksrccmtaps10D', 'db_table': "u'WDrkSrcCmTaps-10d'"},
            'areaid': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'AreaID'", 'blank': 'True'}),
            'areaname': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'Areaname'"}),
            'areasmpdus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'AreaSmpDUs'", 'blank': 'True'}),
            'dusinarea': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'DusInArea'", 'blank': 'True'}),
            'dusinsmp': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'DUsInSmp'", 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pcntdus': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'pcntDUs'", 'blank': 'True'}),
            'pcntpple': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'smppersons': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'SmpPersons'", 'blank': 'True'}),
            'totaldusinarea': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'TotalDUsInArea'", 'blank': 'True'}),
            'totalppleinarea': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'TotalPpleinArea'", 'blank': 'True'})
        },
        u'majitables.wdrksrcleak': {
            'Meta': {'object_name': 'Wdrksrcleak', 'db_table': "u'WDrkSrcLeak'"},
            'areaid': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'AreaID'", 'blank': 'True'}),
            'areaname': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'Areaname'"}),
            'areasmpdus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'AreaSmpDUs'", 'blank': 'True'}),
            'dusinarea': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'DusInArea'", 'blank': 'True'}),
            'dusinsmp': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'DUsInSmp'", 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pcntdus': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'pcntDUs'", 'blank': 'True'}),
            'pcntpple': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'smppersons': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'SmpPersons'", 'blank': 'True'}),
            'totaldusinarea': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'TotalDUsInArea'", 'blank': 'True'}),
            'totalppleinarea': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'TotalPpleinArea'", 'blank': 'True'})
        },
        u'majitables.wdrksrcothcon': {
            'Meta': {'object_name': 'Wdrksrcothcon', 'db_table': "u'WDrkSrcOthCon'"},
            'areaid': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'AreaID'", 'blank': 'True'}),
            'areaname': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'Areaname'"}),
            'areasmpdus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'AreaSmpDUs'", 'blank': 'True'}),
            'dusinarea': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'DusInArea'", 'blank': 'True'}),
            'dusinsmp': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'DUsInSmp'", 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pcntdus': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'pcntDUs'", 'blank': 'True'}),
            'pcntpple': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'smppersons': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'SmpPersons'", 'blank': 'True'}),
            'totaldusinarea': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'TotalDUsInArea'", 'blank': 'True'}),
            'totalppleinarea': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'TotalPpleinArea'", 'blank': 'True'})
        },
        u'majitables.wdrksrcpipedcounty': {
            'Meta': {'object_name': 'Wdrksrcpipedcounty', 'db_table': "u'WDrkSrcPipedCounty'"},
            'countyid': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'CountyID'", 'blank': 'True'}),
            'countyname': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'CountyName'"}),
            'dusinarea': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'DusInArea'", 'blank': 'True'}),
            'dusinsmp': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'DUsInSmp'", 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pcntdus': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'pcntDUs'", 'blank': 'True'}),
            'pcntpop': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'PcntPop'", 'blank': 'True'}),
            'pop': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'Pop'", 'blank': 'True'}),
            'smpdus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'SmpDUs'", 'blank': 'True'}),
            'totalppleinarea': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'TotalPpleinArea'", 'blank': 'True'}),
            'totdus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'TotDUs'", 'blank': 'True'})
        },
        u'majitables.wdrksrcpipedslum': {
            'Meta': {'object_name': 'Wdrksrcpipedslum', 'db_table': "u'WDrkSrcPipedSlum'"},
            'dusinarea': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'DusInArea'", 'blank': 'True'}),
            'dusinsmp': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'DUsInSmp'", 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pcntdus': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'pcntDUs'", 'blank': 'True'}),
            'pcntpop': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'PcntPop'", 'blank': 'True'}),
            'pop': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'Pop'", 'blank': 'True'}),
            'slumid': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'SlumID'", 'blank': 'True'}),
            'slumname': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'SlumName'"}),
            'smpdus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'SmpDUs'", 'blank': 'True'}),
            'totalppleinarea': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'TotalPpleinArea'", 'blank': 'True'}),
            'totdus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'TotDUs'", 'blank': 'True'})
        },
        u'majitables.wdrksrcpipedtown': {
            'Meta': {'object_name': 'Wdrksrcpipedtown', 'db_table': "u'WDrkSrcPipedTown'"},
            'dusinarea': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'DusInArea'", 'blank': 'True'}),
            'dusinsmp': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'DUsInSmp'", 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pcntdus': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'pcntDUs'", 'blank': 'True'}),
            'pcntpop': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'PcntPop'", 'blank': 'True'}),
            'pop': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'Pop'", 'blank': 'True'}),
            'smpdus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'SmpDUs'", 'blank': 'True'}),
            'totalppleinarea': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'TotalPpleinArea'", 'blank': 'True'}),
            'totdus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'TotDUs'", 'blank': 'True'}),
            'townid': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'TownID'", 'blank': 'True'}),
            'townname': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'TownName'"})
        },
        u'majitables.wdrksrcpipedwsp': {
            'Meta': {'object_name': 'Wdrksrcpipedwsp', 'db_table': "u'WDrkSrcPipedWSP'"},
            'dusinarea': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'DusInArea'", 'blank': 'True'}),
            'dusinsmp': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'DUsInSmp'", 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pcntdus': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'pcntDUs'", 'blank': 'True'}),
            'pcntpop': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'PcntPop'", 'blank': 'True'}),
            'pop': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'Pop'", 'blank': 'True'}),
            'smpdus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'SmpDUs'", 'blank': 'True'}),
            'totalppleinarea': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'TotalPpleinArea'", 'blank': 'True'}),
            'totdus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'TotDUs'", 'blank': 'True'}),
            'wspid': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'WSPID'"}),
            'wspname': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'WSPName'"})
        },
        u'majitables.wdrksrcreseller': {
            'Meta': {'object_name': 'Wdrksrcreseller', 'db_table': "u'WDrkSrcReseller'"},
            'areaid': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'AreaID'", 'blank': 'True'}),
            'areaname': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'Areaname'"}),
            'areasmpdus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'AreaSmpDUs'", 'blank': 'True'}),
            'dusinarea': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'DusInArea'", 'blank': 'True'}),
            'dusinsmp': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'DUsInSmp'", 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pcntdus': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'pcntDUs'", 'blank': 'True'}),
            'pcntpple': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'smppersons': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'SmpPersons'", 'blank': 'True'}),
            'totaldusinarea': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'TotalDUsInArea'", 'blank': 'True'}),
            'totalppleinarea': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'TotalPpleinArea'", 'blank': 'True'})
        },
        u'majitables.wdrksrcywell': {
            'Meta': {'object_name': 'Wdrksrcywell', 'db_table': "u'WDrkSrcYWell'"},
            'areaid': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'AreaID'", 'blank': 'True'}),
            'areaname': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'Areaname'"}),
            'areasmpdus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'AreaSmpDUs'", 'blank': 'True'}),
            'dusinarea': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'DusInArea'", 'blank': 'True'}),
            'dusinsmp': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'DUsInSmp'", 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pcntdus': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'pcntDUs'", 'blank': 'True'}),
            'pcntpple': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'smppersons': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'SmpPersons'", 'blank': 'True'}),
            'totaldusinarea': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'TotalDUsInArea'", 'blank': 'True'}),
            'totalppleinarea': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'TotalPpleinArea'", 'blank': 'True'})
        },
        u'majitables.wduconcounty': {
            'Meta': {'object_name': 'Wduconcounty', 'db_table': "u'WDUConCounty'"},
            'countyid': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'CountyID'", 'blank': 'True'}),
            'countyname': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'CountyName'"}),
            'duownconnection': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'DUOwnconnection'"}),
            'dusinsmp': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'DUsInSmp'", 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pcntdus': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'pcntDUs'", 'blank': 'True'}),
            'smpdus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'SmpDUs'", 'blank': 'True'}),
            'totdus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'TotDUs'", 'blank': 'True'})
        },
        u'majitables.wduconmetcounty': {
            'Meta': {'object_name': 'Wduconmetcounty', 'db_table': "u'WDUConMetCounty'"},
            'countyid': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'CountyID'", 'blank': 'True'}),
            'countyname': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'CountyName'"}),
            'duconmet': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'DUconMet'"}),
            'dusinsmp': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'DUsInSmp'", 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ndus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'NDUs'", 'blank': 'True'}),
            'pcntdus': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'pcntDUs'", 'blank': 'True'}),
            'smpdus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'SmpDUs'", 'blank': 'True'}),
            'totdus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'TotDUs'", 'blank': 'True'})
        },
        u'majitables.wduconmetslum': {
            'Meta': {'object_name': 'Wduconmetslum', 'db_table': "u'WDUConMetSlum'"},
            'duconmet': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'DUconMet'"}),
            'dusinsmp': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'DUsInSmp'", 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ndus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'NDUs'", 'blank': 'True'}),
            'pcntdus': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'pcntDUs'", 'blank': 'True'}),
            'slumid': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'SlumID'", 'blank': 'True'}),
            'slumname': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'SlumName'"}),
            'smpdus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'SmpDUs'", 'blank': 'True'}),
            'totdus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'TotDUs'", 'blank': 'True'})
        },
        u'majitables.wduconmettown': {
            'Meta': {'object_name': 'Wduconmettown', 'db_table': "u'WDUConMetTown'"},
            'duconmet': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'DUconMet'"}),
            'dusinsmp': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'DUsInSmp'", 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ndus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'NDUs'", 'blank': 'True'}),
            'pcntdus': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'pcntDUs'", 'blank': 'True'}),
            'smpdus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'SmpDUs'", 'blank': 'True'}),
            'totdus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'TotDUs'", 'blank': 'True'}),
            'townid': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'TownID'", 'blank': 'True'}),
            'townname': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'TownName'"})
        },
        u'majitables.wduconmetwsp': {
            'Meta': {'object_name': 'Wduconmetwsp', 'db_table': "u'WDUConMetWSP'"},
            'duconmet': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'DUconMet'"}),
            'dusinsmp': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'DUsInSmp'", 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ndus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'NDUs'", 'blank': 'True'}),
            'pcntdus': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'pcntDUs'", 'blank': 'True'}),
            'smpdus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'SmpDUs'", 'blank': 'True'}),
            'totdus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'TotDUs'", 'blank': 'True'}),
            'wspid': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'WSPID'"}),
            'wspname': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'WSPName'"})
        },
        u'majitables.wduconslum': {
            'Meta': {'object_name': 'Wduconslum', 'db_table': "u'WDUConSlum'"},
            'duownconnection': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'DUOwnconnection'"}),
            'dusinsmp': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'DUsInSmp'", 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pcntdus': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'pcntDUs'", 'blank': 'True'}),
            'slumid': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'SlumID'", 'blank': 'True'}),
            'slumname': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'SlumName'"}),
            'smpdus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'SmpDUs'", 'blank': 'True'}),
            'totdus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'TotDUs'", 'blank': 'True'})
        },
        u'majitables.wducontown': {
            'Meta': {'object_name': 'Wducontown', 'db_table': "u'WDUConTown'"},
            'duownconnection': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'DUOwnconnection'"}),
            'dusinsmp': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'DUsInSmp'", 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pcntdus': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'pcntDUs'", 'blank': 'True'}),
            'smpdus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'SmpDUs'", 'blank': 'True'}),
            'totdus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'TotDUs'", 'blank': 'True'}),
            'townid': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'TownID'", 'blank': 'True'}),
            'townname': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'TownName'"})
        },
        u'majitables.wduconwsp': {
            'Meta': {'object_name': 'Wduconwsp', 'db_table': "u'WDUConWSP'"},
            'duownconnection': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'DUOwnconnection'"}),
            'dusinsmp': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'DUsInSmp'", 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pcntdus': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'pcntDUs'", 'blank': 'True'}),
            'smpdus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'SmpDUs'", 'blank': 'True'}),
            'totdus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'TotDUs'", 'blank': 'True'}),
            'wspid': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'WSPID'"}),
            'wspname': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'WSPName'"})
        },
        u'majitables.wduowncon': {
            'Meta': {'object_name': 'Wduowncon', 'db_table': "u'WDUOwnCon'"},
            'areaid': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'AreaID'", 'blank': 'True'}),
            'areaname': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'Areaname'"}),
            'areasmpdus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'AreaSmpDUs'", 'blank': 'True'}),
            'duownconnection': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'DUOwnconnection'"}),
            'dusinarea': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'DusInArea'", 'blank': 'True'}),
            'dusinsmp': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'DUsInSmp'", 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pcntdus': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'pcntDUs'", 'blank': 'True'}),
            'totaldusinarea': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'TotalDUsInArea'", 'blank': 'True'})
        },
        u'majitables.wduowncon210d': {
            'Meta': {'object_name': 'Wduowncon210D', 'db_table': "u'WDUOwnCon2-10d'"},
            'areaid': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'AreaID'", 'blank': 'True'}),
            'areaname': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'Areaname'"}),
            'areasmpdus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'AreaSmpDUs'", 'blank': 'True'}),
            'duownconnection': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'DUOwnconnection'"}),
            'dusinarea': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'DusInArea'", 'blank': 'True'}),
            'dusinsmp': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'DUsInSmp'", 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pcntdus': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'pcntDUs'", 'blank': 'True'}),
            'totaldusinarea': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'TotalDUsInArea'", 'blank': 'True'})
        },
        u'majitables.wduownconmet': {
            'Meta': {'object_name': 'Wduownconmet', 'db_table': "u'WDUOwnConMet'"},
            'areaid': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'AreaID'", 'blank': 'True'}),
            'areaname': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'Areaname'"}),
            'duconmetered': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'DUconmetered'"}),
            'dusinarea': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'DUsInArea'", 'blank': 'True'}),
            'dusinsmp': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'DUsInSmp'", 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pcntdus': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'pcntDUs'", 'blank': 'True'}),
            'smpduscon': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'SmpDUsCon'", 'blank': 'True'})
        },
        u'majitables.wduownconmet210d': {
            'Meta': {'object_name': 'Wduownconmet210D', 'db_table': "u'WDUOwnConMet2-10d'"},
            'areaid': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'AreaID'", 'blank': 'True'}),
            'areaname': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'Areaname'"}),
            'duconmetered': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'DUconmetered'"}),
            'dusinarea': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'DUsInArea'", 'blank': 'True'}),
            'dusinsmp': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'DUsInSmp'", 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pcntdus': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'pcntDUs'", 'blank': 'True'}),
            'smpduscon': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'SmpDUsCon'", 'blank': 'True'})
        },
        u'majitables.wduwaterpaycounty': {
            'Meta': {'object_name': 'Wduwaterpaycounty', 'db_table': "u'WDUWaterPayCounty'"},
            'countyid': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'CountyID'", 'blank': 'True'}),
            'countyname': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'CountyName'"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nousingsrc': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'NoUsingSrc'", 'blank': 'True'}),
            'pcntusingsrc': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'PcntUsingSrc'", 'blank': 'True'}),
            'smpdus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'SmpDUs'", 'blank': 'True'}),
            'smpsrc': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'SmpSrc'", 'blank': 'True'}),
            'totdus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'TotDUs'", 'blank': 'True'}),
            'waterpaid': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'WaterPaid'"})
        },
        u'majitables.wduwaterpayslum': {
            'Meta': {'object_name': 'Wduwaterpayslum', 'db_table': "u'WDUWaterPaySlum'"},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nousingsrc': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'NoUsingSrc'", 'blank': 'True'}),
            'pcntusingsrc': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'PcntUsingSrc'", 'blank': 'True'}),
            'slumid': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'SlumID'", 'blank': 'True'}),
            'slumname': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'SlumName'"}),
            'smpdus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'SmpDUs'", 'blank': 'True'}),
            'smpsrc': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'SmpSrc'", 'blank': 'True'}),
            'totdus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'TotDUs'", 'blank': 'True'}),
            'waterpaid': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'WaterPaid'"})
        },
        u'majitables.wduwaterpaytown': {
            'Meta': {'object_name': 'Wduwaterpaytown', 'db_table': "u'WDUWaterPayTown'"},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nousingsrc': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'NoUsingSrc'", 'blank': 'True'}),
            'pcntusingsrc': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'PcntUsingSrc'", 'blank': 'True'}),
            'smpdus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'SmpDUs'", 'blank': 'True'}),
            'smpsrc': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'SmpSrc'", 'blank': 'True'}),
            'totdus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'TotDUs'", 'blank': 'True'}),
            'townid': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'TownID'", 'blank': 'True'}),
            'townname': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'TownName'"}),
            'waterpaid': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'WaterPaid'"})
        },
        u'majitables.wduwaterpaywsp': {
            'Meta': {'object_name': 'Wduwaterpaywsp', 'db_table': "u'WDUWaterPayWSP'"},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nousingsrc': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'NoUsingSrc'", 'blank': 'True'}),
            'pcntusingsrc': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'PcntUsingSrc'", 'blank': 'True'}),
            'smpdus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'SmpDUs'", 'blank': 'True'}),
            'smpsrc': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'SmpSrc'", 'blank': 'True'}),
            'totdus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'TotDUs'", 'blank': 'True'}),
            'waterpaid': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'WaterPaid'"}),
            'wspid': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'WSPID'"}),
            'wspname': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'WSPName'"})
        },
        u'majitables.wfetchdurationdu': {
            'Meta': {'object_name': 'Wfetchdurationdu', 'db_table': "u'WFetchDurationDU'"},
            'areaid': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'AreaID'", 'blank': 'True'}),
            'areaname': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'Areaname'"}),
            'areasmpdus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'AreaSmpDUs'", 'blank': 'True'}),
            'durationrange': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'DurationRange'"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ndus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'NDus'", 'blank': 'True'}),
            'numdu': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'numDU'", 'blank': 'True'}),
            'pcntdus': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'pcntDUs'", 'blank': 'True'}),
            'smpdus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'SmpDUs'", 'blank': 'True'})
        },
        u'majitables.wimpdrksrcjmp': {
            'Meta': {'object_name': 'Wimpdrksrcjmp', 'db_table': "u'WImpDrkSrcJMP'"},
            'areaid': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'AreaID'", 'blank': 'True'}),
            'areaname': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'Areaname'"}),
            'areasmpdus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'AreaSmpDUs'", 'blank': 'True'}),
            'dusinarea': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'DusInArea'", 'blank': 'True'}),
            'dusinsmp': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'DUsInSmp'", 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pcntdus': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'pcntDUs'", 'blank': 'True'}),
            'pcntpple': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'smppersons': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'SmpPersons'", 'blank': 'True'}),
            'totaldusinarea': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'TotalDUsInArea'", 'blank': 'True'}),
            'totalppleinarea': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'TotalPpleinArea'", 'blank': 'True'})
        },
        u'majitables.wimpdrksrcjmp30mn': {
            'Meta': {'object_name': 'Wimpdrksrcjmp30Mn', 'db_table': "u'WImpDrkSrcJMP30mn'"},
            'areaid': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'AreaID'", 'blank': 'True'}),
            'areaname': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'Areaname'"}),
            'areasmpdus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'AreaSmpDUs'", 'blank': 'True'}),
            'dusinarea': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'DusInArea'", 'blank': 'True'}),
            'dusinsmp': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'DUsInSmp'", 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pcntdus': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'pcntDUs'", 'blank': 'True'}),
            'pcntpple': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'smppersons': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'SmpPersons'", 'blank': 'True'}),
            'totaldusinarea': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'TotalDUsInArea'", 'blank': 'True'}),
            'totalppleinarea': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'TotalPpleinArea'", 'blank': 'True'})
        },
        u'majitables.wimpdrksrcjmpbyqlty': {
            'Meta': {'object_name': 'Wimpdrksrcjmpbyqlty', 'db_table': "u'WImpDrkSrcJMPByQlty'"},
            'areaid': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'AreaID'", 'blank': 'True'}),
            'areaname': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'Areaname'"}),
            'areasmpdus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'AreaSmpDUs'", 'blank': 'True'}),
            'dusinarea': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'DusInArea'", 'blank': 'True'}),
            'dusinsmp': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'DUsInSmp'", 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pcntdus': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'pcntDUs'", 'blank': 'True'}),
            'pcntpple': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'smppersons': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'SmpPersons'", 'blank': 'True'}),
            'totaldusinarea': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'TotalDUsInArea'", 'blank': 'True'}),
            'totalppleinarea': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'TotalPpleinArea'", 'blank': 'True'}),
            'wqlty': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'WQlty'"})
        },
        u'majitables.wimpdrksrcjmpbytrt': {
            'Meta': {'object_name': 'Wimpdrksrcjmpbytrt', 'db_table': "u'WImpDrkSrcJMPByTrt'"},
            'areaid': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'AreaID'", 'blank': 'True'}),
            'areaname': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'Areaname'"}),
            'areasmpdus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'AreaSmpDUs'", 'blank': 'True'}),
            'dusinarea': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'DusInArea'", 'blank': 'True'}),
            'dusinsmp': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'DUsInSmp'", 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pcntdus': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'pcntDUs'", 'blank': 'True'}),
            'pcntpple': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'smppersons': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'SmpPersons'", 'blank': 'True'}),
            'totaldusinarea': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'TotalDUsInArea'", 'blank': 'True'}),
            'totalppleinarea': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'TotalPpleinArea'", 'blank': 'True'}),
            'wtrtdrk': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'WTrtDrk'"})
        },
        u'majitables.wimpdrksrcwstf': {
            'Meta': {'object_name': 'Wimpdrksrcwstf', 'db_table': "u'WImpDrkSrcWSTF'"},
            'areaid': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'AreaID'", 'blank': 'True'}),
            'areaname': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'Areaname'"}),
            'areasmpdus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'AreaSmpDUs'", 'blank': 'True'}),
            'dusinarea': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'DusInArea'", 'blank': 'True'}),
            'dusinsmp': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'DUsInSmp'", 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pcntdus': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'pcntDUs'", 'blank': 'True'}),
            'pcntpple': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'smppersons': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'SmpPersons'", 'blank': 'True'}),
            'totaldusinarea': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'TotalDUsInArea'", 'blank': 'True'}),
            'totalppleinarea': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'TotalPpleinArea'", 'blank': 'True'})
        },
        u'majitables.wimpdrksrcwstf30mn': {
            'Meta': {'object_name': 'Wimpdrksrcwstf30Mn', 'db_table': "u'WImpDrkSrcWSTF30mn'"},
            'areaid': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'AreaID'", 'blank': 'True'}),
            'areaname': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'Areaname'"}),
            'areasmpdus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'AreaSmpDUs'", 'blank': 'True'}),
            'dusinarea': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'DusInArea'", 'blank': 'True'}),
            'dusinsmp': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'DUsInSmp'", 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pcntdus': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'pcntDUs'", 'blank': 'True'}),
            'pcntpple': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'smppersons': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'SmpPersons'", 'blank': 'True'}),
            'totaldusinarea': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'TotalDUsInArea'", 'blank': 'True'}),
            'totalppleinarea': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'TotalPpleinArea'", 'blank': 'True'})
        },
        u'majitables.wimpdrksrcwstfbyqlty': {
            'Meta': {'object_name': 'Wimpdrksrcwstfbyqlty', 'db_table': "u'WImpDrkSrcWSTFByQlty'"},
            'areaid': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'AreaID'", 'blank': 'True'}),
            'areaname': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'Areaname'"}),
            'areasmpdus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'AreaSmpDUs'", 'blank': 'True'}),
            'dusinarea': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'DusInArea'", 'blank': 'True'}),
            'dusinsmp': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'DUsInSmp'", 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pcntdus': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'pcntDUs'", 'blank': 'True'}),
            'pcntpple': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'smppersons': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'SmpPersons'", 'blank': 'True'}),
            'totaldusinarea': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'TotalDUsInArea'", 'blank': 'True'}),
            'totalppleinarea': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'TotalPpleinArea'", 'blank': 'True'}),
            'wqlty': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'WQlty'"})
        },
        u'majitables.wimpdrksrcwstfbytrt': {
            'Meta': {'object_name': 'Wimpdrksrcwstfbytrt', 'db_table': "u'WImpDrkSrcWSTFByTrt'"},
            'areaid': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'AreaID'", 'blank': 'True'}),
            'areaname': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'Areaname'"}),
            'areasmpdus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'AreaSmpDUs'", 'blank': 'True'}),
            'dusinarea': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'DusInArea'", 'blank': 'True'}),
            'dusinsmp': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'DUsInSmp'", 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pcntdus': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'pcntDUs'", 'blank': 'True'}),
            'pcntpple': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'smppersons': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'SmpPersons'", 'blank': 'True'}),
            'totaldusinarea': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'TotalDUsInArea'", 'blank': 'True'}),
            'totalppleinarea': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'TotalPpleinArea'", 'blank': 'True'}),
            'wtrtdrk': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'WTrtDrk'"})
        },
        u'majitables.wimpsrcbathwstfcounty': {
            'Meta': {'object_name': 'Wimpsrcbathwstfcounty', 'db_table': "u'WImpSrcBathWSTFCounty'"},
            'countyid': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'CountyID'", 'blank': 'True'}),
            'countyname': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'CountyName'"}),
            'dusinarea': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'DusInArea'", 'blank': 'True'}),
            'dusinsmp': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'DUsInSmp'", 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pcntdus': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'pcntDUs'", 'blank': 'True'}),
            'pcntpop': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'PcntPop'", 'blank': 'True'}),
            'pop': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'Pop'", 'blank': 'True'}),
            'smpdus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'SmpDUs'", 'blank': 'True'}),
            'totalppleinarea': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'TotalPpleinArea'", 'blank': 'True'}),
            'totdus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'TotDUs'", 'blank': 'True'})
        },
        u'majitables.wimpsrcbathwstfslum': {
            'Meta': {'object_name': 'Wimpsrcbathwstfslum', 'db_table': "u'WImpSrcBathWSTFSlum'"},
            'dusinarea': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'DusInArea'", 'blank': 'True'}),
            'dusinsmp': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'DUsInSmp'", 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pcntdus': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'pcntDUs'", 'blank': 'True'}),
            'pcntpop': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'PcntPop'", 'blank': 'True'}),
            'pop': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'Pop'", 'blank': 'True'}),
            'slumid': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'SlumID'", 'blank': 'True'}),
            'slumname': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'SlumName'"}),
            'smpdus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'SmpDUs'", 'blank': 'True'}),
            'totalppleinarea': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'TotalPpleinArea'", 'blank': 'True'}),
            'totdus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'TotDUs'", 'blank': 'True'})
        },
        u'majitables.wimpsrcbathwstftown': {
            'Meta': {'object_name': 'Wimpsrcbathwstftown', 'db_table': "u'WImpSrcBathWSTFTown'"},
            'dusinarea': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'DusInArea'", 'blank': 'True'}),
            'dusinsmp': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'DUsInSmp'", 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pcntdus': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'pcntDUs'", 'blank': 'True'}),
            'pcntpop': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'PcntPop'", 'blank': 'True'}),
            'pop': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'Pop'", 'blank': 'True'}),
            'smpdus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'SmpDUs'", 'blank': 'True'}),
            'totalppleinarea': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'TotalPpleinArea'", 'blank': 'True'}),
            'totdus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'TotDUs'", 'blank': 'True'}),
            'townid': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'TownID'", 'blank': 'True'}),
            'townname': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'TownName'"})
        },
        u'majitables.wimpsrcbathwstfwsp': {
            'Meta': {'object_name': 'Wimpsrcbathwstfwsp', 'db_table': "u'WImpSrcBathWSTFWSP'"},
            'dusinarea': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'DusInArea'", 'blank': 'True'}),
            'dusinsmp': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'DUsInSmp'", 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pcntdus': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'pcntDUs'", 'blank': 'True'}),
            'pcntpop': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'PcntPop'", 'blank': 'True'}),
            'pop': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'Pop'", 'blank': 'True'}),
            'smpdus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'SmpDUs'", 'blank': 'True'}),
            'totalppleinarea': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'TotalPpleinArea'", 'blank': 'True'}),
            'totdus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'TotDUs'", 'blank': 'True'}),
            'wspid': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'WSPID'"}),
            'wspname': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'WSPName'"})
        },
        u'majitables.wimpsrcckgwstfcounty': {
            'Meta': {'object_name': 'Wimpsrcckgwstfcounty', 'db_table': "u'WImpSrcCkgWSTFCounty'"},
            'countyid': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'CountyID'", 'blank': 'True'}),
            'countyname': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'CountyName'"}),
            'dusinarea': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'DusInArea'", 'blank': 'True'}),
            'dusinsmp': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'DUsInSmp'", 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pcntdus': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'pcntDUs'", 'blank': 'True'}),
            'pcntpop': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'PcntPop'", 'blank': 'True'}),
            'pop': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'Pop'", 'blank': 'True'}),
            'smpdus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'SmpDUs'", 'blank': 'True'}),
            'totalppleinarea': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'TotalPpleinArea'", 'blank': 'True'}),
            'totdus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'TotDUs'", 'blank': 'True'})
        },
        u'majitables.wimpsrcckgwstfslum': {
            'Meta': {'object_name': 'Wimpsrcckgwstfslum', 'db_table': "u'WImpSrcCkgWSTFSlum'"},
            'dusinarea': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'DusInArea'", 'blank': 'True'}),
            'dusinsmp': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'DUsInSmp'", 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pcntdus': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'pcntDUs'", 'blank': 'True'}),
            'pcntpop': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'PcntPop'", 'blank': 'True'}),
            'pop': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'Pop'", 'blank': 'True'}),
            'slumid': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'SlumID'", 'blank': 'True'}),
            'slumname': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'SlumName'"}),
            'smpdus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'SmpDUs'", 'blank': 'True'}),
            'totalppleinarea': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'TotalPpleinArea'", 'blank': 'True'}),
            'totdus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'TotDUs'", 'blank': 'True'})
        },
        u'majitables.wimpsrcckgwstftown': {
            'Meta': {'object_name': 'Wimpsrcckgwstftown', 'db_table': "u'WImpSrcCkgWSTFTown'"},
            'dusinarea': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'DusInArea'", 'blank': 'True'}),
            'dusinsmp': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'DUsInSmp'", 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pcntdus': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'pcntDUs'", 'blank': 'True'}),
            'pcntpop': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'PcntPop'", 'blank': 'True'}),
            'pop': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'Pop'", 'blank': 'True'}),
            'smpdus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'SmpDUs'", 'blank': 'True'}),
            'totalppleinarea': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'TotalPpleinArea'", 'blank': 'True'}),
            'totdus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'TotDUs'", 'blank': 'True'}),
            'townid': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'TownID'", 'blank': 'True'}),
            'townname': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'TownName'"})
        },
        u'majitables.wimpsrcckgwstfwsp': {
            'Meta': {'object_name': 'Wimpsrcckgwstfwsp', 'db_table': "u'WImpSrcCkgWSTFWSP'"},
            'dusinarea': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'DusInArea'", 'blank': 'True'}),
            'dusinsmp': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'DUsInSmp'", 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pcntdus': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'pcntDUs'", 'blank': 'True'}),
            'pcntpop': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'PcntPop'", 'blank': 'True'}),
            'pop': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'Pop'", 'blank': 'True'}),
            'smpdus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'SmpDUs'", 'blank': 'True'}),
            'totalppleinarea': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'TotalPpleinArea'", 'blank': 'True'}),
            'totdus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'TotDUs'", 'blank': 'True'}),
            'wspid': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'WSPID'"}),
            'wspname': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'WSPName'"})
        },
        u'majitables.wimpsrcdrkwstfcounty': {
            'Meta': {'object_name': 'Wimpsrcdrkwstfcounty', 'db_table': "u'WImpSrcDrkWSTFCounty'"},
            'countyid': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'CountyID'", 'blank': 'True'}),
            'countyname': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'CountyName'"}),
            'dusinarea': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'DusInArea'", 'blank': 'True'}),
            'dusinsmp': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'DUsInSmp'", 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pcntdus': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'pcntDUs'", 'blank': 'True'}),
            'pcntpop': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'PcntPop'", 'blank': 'True'}),
            'pop': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'Pop'", 'blank': 'True'}),
            'smpdus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'SmpDUs'", 'blank': 'True'}),
            'totalppleinarea': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'TotalPpleinArea'", 'blank': 'True'}),
            'totdus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'TotDUs'", 'blank': 'True'})
        },
        u'majitables.wimpsrcdrkwstfslum': {
            'Meta': {'object_name': 'Wimpsrcdrkwstfslum', 'db_table': "u'WImpSrcDrkWSTFSlum'"},
            'dusinarea': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'DusInArea'", 'blank': 'True'}),
            'dusinsmp': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'DUsInSmp'", 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pcntdus': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'pcntDUs'", 'blank': 'True'}),
            'pcntpop': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'PcntPop'", 'blank': 'True'}),
            'pop': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'Pop'", 'blank': 'True'}),
            'slumid': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'SlumID'", 'blank': 'True'}),
            'slumname': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'SlumName'"}),
            'smpdus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'SmpDUs'", 'blank': 'True'}),
            'totalppleinarea': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'TotalPpleinArea'", 'blank': 'True'}),
            'totdus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'TotDUs'", 'blank': 'True'})
        },
        u'majitables.wimpsrcdrkwstfwsp': {
            'Meta': {'object_name': 'Wimpsrcdrkwstfwsp', 'db_table': "u'WImpSrcDrkWSTFWSP'"},
            'dusinarea': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'DusInArea'", 'blank': 'True'}),
            'dusinsmp': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'DUsInSmp'", 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pcntdus': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'pcntDUs'", 'blank': 'True'}),
            'pcntpop': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'PcntPop'", 'blank': 'True'}),
            'pop': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'Pop'", 'blank': 'True'}),
            'smpdus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'SmpDUs'", 'blank': 'True'}),
            'totalppleinarea': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'TotalPpleinArea'", 'blank': 'True'}),
            'totdus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'TotDUs'", 'blank': 'True'}),
            'wspid': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'WSPID'"}),
            'wspname': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'WSPName'"})
        },
        u'majitables.wnocompubpsts10d': {
            'Meta': {'object_name': 'Wnocompubpsts10D', 'db_table': "u'WNoComPubPsts-10d'"},
            'areaid': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'AreaID'", 'blank': 'True'}),
            'areaname': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'AreaName'"}),
            'comtaps': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'ComTaps'", 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nopubcomtaps': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'NoPubComTaps'", 'blank': 'True'}),
            'pubwsptaps': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'PubWSPTaps'", 'blank': 'True'})
        },
        u'majitables.woutletscounty': {
            'Meta': {'object_name': 'Woutletscounty', 'db_table': "u'WOutletsCounty'"},
            'comptaps': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'CompTaps'", 'blank': 'True'}),
            'comwaterksks': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'ComWaterKsks'", 'blank': 'True'}),
            'countyid': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'CountyID'", 'blank': 'True'}),
            'countyname': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'CountyName'"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'privtaps': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'PrivTaps'", 'blank': 'True'}),
            'privwaterksks': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'PrivWaterKsks'", 'blank': 'True'}),
            'pubwaterksks': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'PubWaterKsks'", 'blank': 'True'}),
            'pubwsptaps': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'PubWSPTaps'", 'blank': 'True'})
        },
        u'majitables.woutletsslum': {
            'Meta': {'object_name': 'Woutletsslum', 'db_table': "u'WOutletsSlum'"},
            'comptaps': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'CompTaps'", 'blank': 'True'}),
            'comwaterksks': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'ComWaterKsks'", 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'privtaps': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'PrivTaps'", 'blank': 'True'}),
            'privwaterksks': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'PrivWaterKsks'", 'blank': 'True'}),
            'pubwaterksks': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'PubWaterKsks'", 'blank': 'True'}),
            'pubwsptaps': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'PubWSPTaps'", 'blank': 'True'}),
            'slumid': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'SlumID'"}),
            'slumname': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'SlumName'"})
        },
        u'majitables.woutletstown': {
            'Meta': {'object_name': 'Woutletstown', 'db_table': "u'WOutletsTown'"},
            'comptaps': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'CompTaps'", 'blank': 'True'}),
            'comwaterksks': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'ComWaterKsks'", 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'privtaps': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'PrivTaps'", 'blank': 'True'}),
            'privwaterksks': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'PrivWaterKsks'", 'blank': 'True'}),
            'pubwaterksks': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'PubWaterKsks'", 'blank': 'True'}),
            'pubwsptaps': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'PubWSPTaps'", 'blank': 'True'}),
            'townid': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'TownID'", 'blank': 'True'}),
            'townname': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'TownName'"})
        },
        u'majitables.woutletswsp': {
            'Meta': {'object_name': 'Woutletswsp', 'db_table': "u'WOutletsWSP'"},
            'comptaps': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'CompTaps'", 'blank': 'True'}),
            'comwaterksks': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'ComWaterKsks'", 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'privtaps': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'PrivTaps'", 'blank': 'True'}),
            'privwaterksks': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'PrivWaterKsks'", 'blank': 'True'}),
            'pubwaterksks': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'PubWaterKsks'", 'blank': 'True'}),
            'pubwsptaps': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'PubWSPTaps'", 'blank': 'True'}),
            'wspid': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'WSPID'"}),
            'wspname': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'WSPName'"})
        },
        u'majitables.wpaydrkdu': {
            'Meta': {'object_name': 'Wpaydrkdu', 'db_table': "u'WPayDrkDU'"},
            'areaid': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'AreaID'", 'blank': 'True'}),
            'areaname': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'Areaname'"}),
            'areasmpdus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'AreaSmpDUs'", 'blank': 'True'}),
            'dus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'DUs'", 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ndus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'NDus'", 'blank': 'True'}),
            'numdu': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'numDU'", 'blank': 'True'}),
            'pcntdus': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'pcntDUs'", 'blank': 'True'}),
            'wpaydrk': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'WPaydrk'"})
        },
        u'majitables.wpaynondrkdu': {
            'Meta': {'object_name': 'Wpaynondrkdu', 'db_table': "u'WPayNonDrkDU'"},
            'areaid': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'AreaID'", 'blank': 'True'}),
            'areaname': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'Areaname'"}),
            'areasmpdus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'AreaSmpDUs'", 'blank': 'True'}),
            'dus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'DUs'", 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ndus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'NDus'", 'blank': 'True'}),
            'numdu': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'numDU'", 'blank': 'True'}),
            'pcntdus': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'pcntDUs'", 'blank': 'True'}),
            'wpaydrk': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'WPaydrk'"})
        },
        u'majitables.wpconcounty': {
            'Meta': {'object_name': 'Wpconcounty', 'db_table': "u'WPConCounty'"},
            'countyid': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'CountyID'", 'blank': 'True'}),
            'countyname': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'CountyName'"}),
            'dusinarea': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'DusInArea'", 'blank': 'True'}),
            'dusinsmp': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'DUsInSmp'", 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pcntdus': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'pcntDUs'", 'blank': 'True'}),
            'plotconnected': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'Plotconnected'"}),
            'smpdus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'SmpDUs'", 'blank': 'True'}),
            'totdus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'TotDUs'", 'blank': 'True'})
        },
        u'majitables.wpconmetcounty': {
            'Meta': {'object_name': 'Wpconmetcounty', 'db_table': "u'WPConMetCounty'"},
            'countyid': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'CountyID'", 'blank': 'True'}),
            'countyname': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'CountyName'"}),
            'dusinarea': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'DusInArea'", 'blank': 'True'}),
            'dusinsmp': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'DUsInSmp'", 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pcntdus': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'pcntDUs'", 'blank': 'True'}),
            'plotconmet': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'PlotconMet'"}),
            'smpdus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'SmpDUs'", 'blank': 'True'}),
            'totdus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'TotDUs'", 'blank': 'True'})
        },
        u'majitables.wpconmetslum': {
            'Meta': {'object_name': 'Wpconmetslum', 'db_table': "u'WPConMetSlum'"},
            'dusinarea': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'DusInArea'", 'blank': 'True'}),
            'dusinsmp': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'DUsInSmp'", 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pcntdus': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'pcntDUs'", 'blank': 'True'}),
            'plotconmet': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'PlotconMet'"}),
            'slumid': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'SlumID'", 'blank': 'True'}),
            'slumname': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'SlumName'"}),
            'smpdus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'SmpDUs'", 'blank': 'True'}),
            'totdus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'TotDUs'", 'blank': 'True'})
        },
        u'majitables.wpconmettown': {
            'Meta': {'object_name': 'Wpconmettown', 'db_table': "u'WPConMetTown'"},
            'dusinarea': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'DusInArea'", 'blank': 'True'}),
            'dusinsmp': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'DUsInSmp'", 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pcntdus': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'pcntDUs'", 'blank': 'True'}),
            'plotconmet': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'PlotconMet'"}),
            'smpdus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'SmpDUs'", 'blank': 'True'}),
            'totdus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'TotDUs'", 'blank': 'True'}),
            'townid': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'TownID'", 'blank': 'True'}),
            'townname': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'TownName'"})
        },
        u'majitables.wpconmetwsp': {
            'Meta': {'object_name': 'Wpconmetwsp', 'db_table': "u'WPConMetWSP'"},
            'dusinarea': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'DusInArea'", 'blank': 'True'}),
            'dusinsmp': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'DUsInSmp'", 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pcntdus': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'pcntDUs'", 'blank': 'True'}),
            'plotconmet': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'PlotconMet'"}),
            'smpdus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'SmpDUs'", 'blank': 'True'}),
            'totdus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'TotDUs'", 'blank': 'True'}),
            'wspid': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'WSPID'"}),
            'wspname': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'WSPName'"})
        },
        u'majitables.wpconslum': {
            'Meta': {'object_name': 'Wpconslum', 'db_table': "u'WPConSlum'"},
            'dusinarea': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'DusInArea'", 'blank': 'True'}),
            'dusinsmp': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'DUsInSmp'", 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pcntdus': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'pcntDUs'", 'blank': 'True'}),
            'plotconnected': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'Plotconnected'"}),
            'slumid': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'SlumID'", 'blank': 'True'}),
            'slumname': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'SlumName'"}),
            'smpdus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'SmpDUs'", 'blank': 'True'}),
            'totdus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'TotDUs'", 'blank': 'True'})
        },
        u'majitables.wpcontown': {
            'Meta': {'object_name': 'Wpcontown', 'db_table': "u'WPConTown'"},
            'dusinarea': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'DusInArea'", 'blank': 'True'}),
            'dusinsmp': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'DUsInSmp'", 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pcntdus': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'pcntDUs'", 'blank': 'True'}),
            'plotconnected': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'Plotconnected'"}),
            'smpdus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'SmpDUs'", 'blank': 'True'}),
            'totdus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'TotDUs'", 'blank': 'True'}),
            'townid': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'TownID'", 'blank': 'True'}),
            'townname': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'TownName'"})
        },
        u'majitables.wpconwsp': {
            'Meta': {'object_name': 'Wpconwsp', 'db_table': "u'WPConWSP'"},
            'dusinarea': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'DusInArea'", 'blank': 'True'}),
            'dusinsmp': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'DUsInSmp'", 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pcntdus': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'pcntDUs'", 'blank': 'True'}),
            'plotconnected': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'Plotconnected'"}),
            'smpdus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'SmpDUs'", 'blank': 'True'}),
            'totdus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'TotDUs'", 'blank': 'True'}),
            'wspid': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'wspID'"}),
            'wspname': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'wspName'"})
        },
        u'majitables.wpducondisconnected': {
            'Meta': {'object_name': 'Wpducondisconnected', 'db_table': "u'WPDUConDisconnected'"},
            'areaid': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'AreaID'", 'blank': 'True'}),
            'areaname': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'Areaname'"}),
            'areasmpdus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'AreaSmpDUs'", 'blank': 'True'}),
            'dusinarea': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'DUsInArea'", 'blank': 'True'}),
            'dusinsmp': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'DUsInSmp'", 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pcntdus': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'pcntDUs'", 'blank': 'True'}),
            'totaldusinarea': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'TotalDUsInArea'", 'blank': 'True'})
        },
        u'majitables.wpipedsrcbath': {
            'Meta': {'object_name': 'Wpipedsrcbath', 'db_table': "u'WPipedSrcBath'"},
            'areaid': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'AreaID'", 'blank': 'True'}),
            'areaname': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'Areaname'"}),
            'areasmpdus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'AreaSmpDUs'", 'blank': 'True'}),
            'dusinarea': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'DusInArea'", 'blank': 'True'}),
            'dusinsmp': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'DUsInSmp'", 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pcntdus': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'pcntDUs'", 'blank': 'True'}),
            'pcntpple': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'smppersons': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'SmpPersons'", 'blank': 'True'}),
            'totaldusinarea': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'TotalDUsInArea'", 'blank': 'True'}),
            'totalppleinarea': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'TotalPpleinArea'", 'blank': 'True'})
        },
        u'majitables.wpipedsrcdrk': {
            'Meta': {'object_name': 'Wpipedsrcdrk', 'db_table': "u'WPipedSrcDrk'"},
            'areaid': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'AreaID'", 'blank': 'True'}),
            'areaname': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'Areaname'"}),
            'areasmpdus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'AreaSmpDUs'", 'blank': 'True'}),
            'dusinarea': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'DusInArea'", 'blank': 'True'}),
            'dusinsmp': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'DUsInSmp'", 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pcntdus': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'pcntDUs'", 'blank': 'True'}),
            'pcntpple': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'smppersons': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'SmpPersons'", 'blank': 'True'}),
            'totaldusinarea': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'TotalDUsInArea'", 'blank': 'True'}),
            'totalppleinarea': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'TotalPpleinArea'", 'blank': 'True'})
        },
        u'majitables.wpipedsrcdrkavgpay': {
            'Meta': {'object_name': 'Wpipedsrcdrkavgpay', 'db_table': "u'WPipedSrcDrkAvgPay'"},
            'areaid': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'AreaID'", 'blank': 'True'}),
            'areaname': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'Areaname'"}),
            'areasmpdus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'AreaSmpDUs'", 'blank': 'True'}),
            'avgpaydrk': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'AvgPayDrk'", 'blank': 'True'}),
            'dusinarea': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'DusInArea'", 'blank': 'True'}),
            'dusinsmp': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'DUsInSmp'", 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'paymthd': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'PayMthd'"}),
            'pcntdus': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'pcntDUs'", 'blank': 'True'}),
            'pcntpple': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'smppersons': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'SmpPersons'", 'blank': 'True'}),
            'totaldusinarea': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'TotalDUsInArea'", 'blank': 'True'}),
            'totalppleinarea': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'TotalPpleinArea'", 'blank': 'True'})
        },
        u'majitables.wpipedsrcdrktrt': {
            'Meta': {'object_name': 'Wpipedsrcdrktrt', 'db_table': "u'WPipedSrcDrkTrt'"},
            'areaid': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'AreaID'", 'blank': 'True'}),
            'areaname': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'Areaname'"}),
            'areasmpdus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'AreaSmpDUs'", 'blank': 'True'}),
            'dusinarea': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'DusInArea'", 'blank': 'True'}),
            'dusinsmp': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'DUsInSmp'", 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pcntdus': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'pcntDUs'", 'blank': 'True'}),
            'pcntpple': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'smppersons': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'SmpPersons'", 'blank': 'True'}),
            'totaldusinarea': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'TotalDUsInArea'", 'blank': 'True'}),
            'totalppleinarea': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'TotalPpleinArea'", 'blank': 'True'})
        },
        u'majitables.wplotconmetdu': {
            'Meta': {'object_name': 'WplotconmetDu', 'db_table': "u'WPlotConMet-DU'"},
            'areaid': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'AreaID'", 'blank': 'True'}),
            'areaname': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'Areaname'"}),
            'duconmetered': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'DUconmetered'"}),
            'dusinarea': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'DUsInArea'", 'blank': 'True'}),
            'dusinsmp': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'DUsInSmp'", 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pcntdus': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'pcntDUs'", 'blank': 'True'}),
            'smpduscon': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'SmpDUsCon'", 'blank': 'True'})
        },
        u'majitables.wplotconnecteddu': {
            'Meta': {'object_name': 'WplotconnectedDu', 'db_table': "u'WPlotConnected-DU'"},
            'areaid': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'AreaID'", 'blank': 'True'}),
            'areaname': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'Areaname'"}),
            'areasmpdus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'AreaSmpDUs'", 'blank': 'True'}),
            'dusinarea': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'DusInArea'", 'blank': 'True'}),
            'dusinsmp': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'DUsInSmp'", 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pcntdus': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'pcntDUs'", 'blank': 'True'}),
            'plotconnected': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'Plotconnected'"}),
            'totaldusinarea': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'TotalDUsInArea'", 'blank': 'True'})
        },
        u'majitables.wresidentsperwspksk': {
            'Meta': {'object_name': 'Wresidentsperwspksk', 'db_table': "u'WresidentsperWSPKsk'"},
            'area': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'Area'", 'blank': 'True'}),
            'areaname': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'Areaname'"}),
            'areapop': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'AreaPop'", 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ppleperkiosk': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'PplePerKiosk'"}),
            'pubwaterksks': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'PubWaterKsks'", 'blank': 'True'})
        },
        u'majitables.wrespercompubpost10d': {
            'Meta': {'object_name': 'Wrespercompubpost10D', 'db_table': "u'WResperComPubPost-10d'"},
            'area': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'Area'", 'blank': 'True'}),
            'areaname': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'Areaname'"}),
            'areapop': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'AreaPop'", 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nfacilities': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'NFacilities'", 'blank': 'True'}),
            'ppleperfacility': ('django.db.models.fields.CharField', [], {'max_length': '33', 'db_column': "u'PplePerFacility'"})
        },
        u'majitables.wrespercomtapcounty': {
            'Meta': {'object_name': 'Wrespercomtapcounty', 'db_table': "u'WResPerComTapCounty'"},
            'countyid': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'CountyID'", 'blank': 'True'}),
            'countyname': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'CountyName'"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pop': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'Pop'", 'blank': 'True'}),
            'pplepercomtap': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'PplePerComTap'"}),
            'totcomtaps': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'TotComTaps'", 'blank': 'True'})
        },
        u'majitables.wrespercomtapslum': {
            'Meta': {'object_name': 'Wrespercomtapslum', 'db_table': "u'WResPerComTapSlum'"},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pop': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'Pop'", 'blank': 'True'}),
            'pplepercomtap': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'PplePerComTap'"}),
            'slumid': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'SlumID'", 'blank': 'True'}),
            'slumname': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'SlumName'"}),
            'totcomtaps': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'TotComTaps'", 'blank': 'True'})
        },
        u'majitables.wrespercomtaptown': {
            'Meta': {'object_name': 'Wrespercomtaptown', 'db_table': "u'WResPerComTapTown'"},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pop': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'Pop'", 'blank': 'True'}),
            'pplepercomtap': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'PplePerComTap'"}),
            'totcomtaps': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'TotComTaps'", 'blank': 'True'}),
            'townid': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'TownID'", 'blank': 'True'}),
            'townname': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'TownName'"})
        },
        u'majitables.wrespercomtapwsp': {
            'Meta': {'object_name': 'Wrespercomtapwsp', 'db_table': "u'WResPerComTapWSP'"},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pop': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'Pop'", 'blank': 'True'}),
            'pplepercomtap': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'PplePerComTap'"}),
            'totcomtaps': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'TotComTaps'", 'blank': 'True'}),
            'wspid': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'WSPID'"}),
            'wspname': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'WSPName'"})
        },
        u'majitables.wresperpubcomkskscounty': {
            'Meta': {'object_name': 'Wresperpubcomkskscounty', 'db_table': "u'WResPerPubComKsksCounty'"},
            'countyid': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'CountyID'", 'blank': 'True'}),
            'countyname': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'CountyName'"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pop': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'Pop'", 'blank': 'True'}),
            'ppleperpubcomtap': ('django.db.models.fields.CharField', [], {'max_length': '36', 'db_column': "u'PplePerPubComTap'"}),
            'totpubcomksks': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'TotPubComKsks'", 'blank': 'True'})
        },
        u'majitables.wresperpubcomksksslum': {
            'Meta': {'object_name': 'Wresperpubcomksksslum', 'db_table': "u'WResPerPubComKsksSlum'"},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pop': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'Pop'", 'blank': 'True'}),
            'ppleperpubcomtap': ('django.db.models.fields.CharField', [], {'max_length': '36', 'db_column': "u'PplePerPubComTap'"}),
            'slumid': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'SlumID'", 'blank': 'True'}),
            'slumname': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'SlumName'"}),
            'totpubcomksks': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'TotPubComKsks'", 'blank': 'True'})
        },
        u'majitables.wresperpubcomkskstown': {
            'Meta': {'object_name': 'Wresperpubcomkskstown', 'db_table': "u'WResPerPubComKsksTown'"},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pop': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'Pop'", 'blank': 'True'}),
            'ppleperpubcomtap': ('django.db.models.fields.CharField', [], {'max_length': '36', 'db_column': "u'PplePerPubComTap'"}),
            'totpubcomksks': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'TotPubComKsks'", 'blank': 'True'}),
            'townid': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'TownID'", 'blank': 'True'}),
            'townname': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'TownName'"})
        },
        u'majitables.wresperpubcomkskswsp': {
            'Meta': {'object_name': 'Wresperpubcomkskswsp', 'db_table': "u'WResPerPubComKsksWSP'"},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pop': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'Pop'", 'blank': 'True'}),
            'ppleperpubcomtap': ('django.db.models.fields.CharField', [], {'max_length': '36', 'db_column': "u'PplePerPubComTap'"}),
            'totpubcomksks': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'TotPubComKsks'", 'blank': 'True'}),
            'wspid': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'WSPID'"}),
            'wspname': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'WSPName'"})
        },
        u'majitables.wresperpubwspcomtapscounty': {
            'Meta': {'object_name': 'Wresperpubwspcomtapscounty', 'db_table': "u'WResPerPubWSPComTapsCounty'"},
            'countyid': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'CountyID'", 'blank': 'True'}),
            'countyname': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'CountyName'"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pop': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'Pop'", 'blank': 'True'}),
            'ppleperpubcomtap': ('django.db.models.fields.CharField', [], {'max_length': '34', 'db_column': "u'PplePerPubComTap'"}),
            'totpubcomtaps': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'TotPubComTaps'", 'blank': 'True'})
        },
        u'majitables.wresperpubwspcomtapsslum': {
            'Meta': {'object_name': 'Wresperpubwspcomtapsslum', 'db_table': "u'WResPerPubWSPComTapsSlum'"},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pop': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'Pop'", 'blank': 'True'}),
            'ppleperpubcomtap': ('django.db.models.fields.CharField', [], {'max_length': '34', 'db_column': "u'PplePerPubComTap'"}),
            'slumid': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'SlumID'", 'blank': 'True'}),
            'slumname': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'SlumName'"}),
            'totpubcomtaps': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'TotPubComTaps'", 'blank': 'True'})
        },
        u'majitables.wresperpubwspcomtapstown': {
            'Meta': {'object_name': 'Wresperpubwspcomtapstown', 'db_table': "u'WResPerPubWSPComTapsTown'"},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pop': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'Pop'", 'blank': 'True'}),
            'ppleperpubcomtap': ('django.db.models.fields.CharField', [], {'max_length': '34', 'db_column': "u'PplePerPubComTap'"}),
            'totpubcomtaps': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'TotPubComTaps'", 'blank': 'True'}),
            'townid': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'TownID'", 'blank': 'True'}),
            'townname': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'TownName'"})
        },
        u'majitables.wresperpubwspcomtapswsp': {
            'Meta': {'object_name': 'Wresperpubwspcomtapswsp', 'db_table': "u'WResPerPubWSPComTapsWSP'"},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pop': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'Pop'", 'blank': 'True'}),
            'ppleperpubcomtap': ('django.db.models.fields.CharField', [], {'max_length': '34', 'db_column': "u'PplePerPubComTap'"}),
            'totpubcomtaps': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'TotPubComTaps'", 'blank': 'True'}),
            'wspid': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'WSPID'"}),
            'wspname': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'WSPName'"})
        },
        u'majitables.wresperpubwsptapcounty': {
            'Meta': {'object_name': 'Wresperpubwsptapcounty', 'db_table': "u'WResPerPubWSPTapCounty'"},
            'countyid': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'CountyID'", 'blank': 'True'}),
            'countyname': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'CountyName'"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pop': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'Pop'", 'blank': 'True'}),
            'ppleperpubtap': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'PplePerPubTap'"}),
            'tottaps': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'TotTaps'", 'blank': 'True'})
        },
        u'majitables.wresperpubwsptapslum': {
            'Meta': {'object_name': 'Wresperpubwsptapslum', 'db_table': "u'WResPerPubWSPTapSlum'"},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pop': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'Pop'", 'blank': 'True'}),
            'ppleperpubtap': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'PplePerPubTap'"}),
            'slumid': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'SlumID'", 'blank': 'True'}),
            'slumname': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'SlumName'"}),
            'tottaps': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'TotTaps'", 'blank': 'True'})
        },
        u'majitables.wresperpubwsptaptown': {
            'Meta': {'object_name': 'Wresperpubwsptaptown', 'db_table': "u'WResPerPubWSPTapTown'"},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pop': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'Pop'", 'blank': 'True'}),
            'ppleperpubtap': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'PplePerPubTap'"}),
            'tottaps': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'TotTaps'", 'blank': 'True'}),
            'townid': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'TownID'", 'blank': 'True'}),
            'townname': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'TownName'"})
        },
        u'majitables.wresperpubwsptapwsp': {
            'Meta': {'object_name': 'Wresperpubwsptapwsp', 'db_table': "u'WResPerPubWSPTapWSP'"},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pop': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'Pop'", 'blank': 'True'}),
            'ppleperpubtap': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'PplePerPubTap'"}),
            'tottaps': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'TotTaps'", 'blank': 'True'}),
            'wspid': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'WSPID'"}),
            'wspname': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'WSPName'"})
        },
        u'majitables.wresperwspkskcounty': {
            'Meta': {'object_name': 'Wresperwspkskcounty', 'db_table': "u'WResPerWSPKskCounty'"},
            'countyid': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'CountyID'", 'blank': 'True'}),
            'countyname': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'CountyName'"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pop': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'Pop'", 'blank': 'True'}),
            'ppleperkiosk': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'PplePerKiosk'"}),
            'totksks': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'TotKsks'", 'blank': 'True'})
        },
        u'majitables.wresperwspkskslum': {
            'Meta': {'object_name': 'Wresperwspkskslum', 'db_table': "u'WResPerWSPKskSlum'"},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pop': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'Pop'", 'blank': 'True'}),
            'ppleperkiosk': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'PplePerKiosk'"}),
            'slumid': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'SlumID'", 'blank': 'True'}),
            'slumname': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'SlumName'"}),
            'totksks': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'TotKsks'", 'blank': 'True'})
        },
        u'majitables.wresperwspksktown': {
            'Meta': {'object_name': 'Wresperwspksktown', 'db_table': "u'WResPerWSPKskTown'"},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pop': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'Pop'", 'blank': 'True'}),
            'ppleperkiosk': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'PplePerKiosk'"}),
            'totksks': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'TotKsks'", 'blank': 'True'}),
            'townid': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'TownID'", 'blank': 'True'}),
            'townname': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'TownName'"})
        },
        u'majitables.wresperwspkskwsp': {
            'Meta': {'object_name': 'Wresperwspkskwsp', 'db_table': "u'WResPerWSPKskWSP'"},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pop': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'Pop'", 'blank': 'True'}),
            'ppleperkiosk': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'PplePerKiosk'"}),
            'totksks': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'TotKsks'", 'blank': 'True'}),
            'wspid': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'WSPID'"}),
            'wspname': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'WSPName'"})
        },
        u'majitables.wsrcbathpipedcounty': {
            'Meta': {'object_name': 'Wsrcbathpipedcounty', 'db_table': "u'WSrcBathPipedCounty'"},
            'countyid': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'CountyID'", 'blank': 'True'}),
            'countyname': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'CountyName'"}),
            'dusinarea': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'DusInArea'", 'blank': 'True'}),
            'dusinsmp': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'DUsInSmp'", 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pcntdus': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'pcntDUs'", 'blank': 'True'}),
            'pcntpop': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'PcntPop'", 'blank': 'True'}),
            'pop': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'Pop'", 'blank': 'True'}),
            'smpdus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'SmpDUs'", 'blank': 'True'}),
            'totalppleinarea': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'TotalPpleinArea'", 'blank': 'True'}),
            'totdus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'TotDUs'", 'blank': 'True'})
        },
        u'majitables.wsrcbathpipedslum': {
            'Meta': {'object_name': 'Wsrcbathpipedslum', 'db_table': "u'WSrcBathPipedSlum'"},
            'dusinarea': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'DusInArea'", 'blank': 'True'}),
            'dusinsmp': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'DUsInSmp'", 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pcntdus': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'pcntDUs'", 'blank': 'True'}),
            'pcntpop': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'PcntPop'", 'blank': 'True'}),
            'pop': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'Pop'", 'blank': 'True'}),
            'slumid': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'SlumID'", 'blank': 'True'}),
            'slumname': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'SlumName'"}),
            'smpdus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'SmpDUs'", 'blank': 'True'}),
            'totalppleinarea': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'TotalPpleinArea'", 'blank': 'True'}),
            'totdus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'TotDUs'", 'blank': 'True'})
        },
        u'majitables.wsrcbathpipedtown': {
            'Meta': {'object_name': 'Wsrcbathpipedtown', 'db_table': "u'WSrcBathPipedTown'"},
            'dusinarea': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'DusInArea'", 'blank': 'True'}),
            'dusinsmp': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'DUsInSmp'", 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pcntdus': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'pcntDUs'", 'blank': 'True'}),
            'pcntpop': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'PcntPop'", 'blank': 'True'}),
            'pop': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'Pop'", 'blank': 'True'}),
            'smpdus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'SmpDUs'", 'blank': 'True'}),
            'totalppleinarea': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'TotalPpleinArea'", 'blank': 'True'}),
            'totdus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'TotDUs'", 'blank': 'True'}),
            'townid': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'TownID'", 'blank': 'True'}),
            'townname': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'TownName'"})
        },
        u'majitables.wsrcbathpipedwsp': {
            'Meta': {'object_name': 'Wsrcbathpipedwsp', 'db_table': "u'WSrcBathPipedWSP'"},
            'dusinarea': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'DusInArea'", 'blank': 'True'}),
            'dusinsmp': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'DUsInSmp'", 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pcntdus': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'pcntDUs'", 'blank': 'True'}),
            'pcntpop': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'PcntPop'", 'blank': 'True'}),
            'pop': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'Pop'", 'blank': 'True'}),
            'smpdus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'SmpDUs'", 'blank': 'True'}),
            'totalppleinarea': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'TotalPpleinArea'", 'blank': 'True'}),
            'totdus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'TotDUs'", 'blank': 'True'}),
            'wspid': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'WspID'"}),
            'wspname': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'WspName'"})
        },
        u'majitables.wsrcckg33county': {
            'Meta': {'object_name': 'Wsrcckg33County', 'db_table': "u'WSrcCkg33County'"},
            'ckgwatersrc': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'CkgWaterSrc'"}),
            'countyid': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'CountyID'", 'blank': 'True'}),
            'countyname': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'CountyName'"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nusingsrc': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'NUsingSrc'", 'blank': 'True'}),
            'pcntusingsrc': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'PcntUsingSrc'", 'blank': 'True'}),
            'smpdus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'SmpDUs'", 'blank': 'True'}),
            'smpsrc': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'SmpSrc'", 'blank': 'True'}),
            'totdus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'TotDUs'", 'blank': 'True'})
        },
        u'majitables.wsrcdrkbhpmpcounty': {
            'Meta': {'object_name': 'Wsrcdrkbhpmpcounty', 'db_table': "u'WSrcDrkBhPmpCounty'"},
            'countyid': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'CountyID'", 'blank': 'True'}),
            'countyname': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'CountyName'"}),
            'dusinarea': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'DusInArea'", 'blank': 'True'}),
            'dusinsmp': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'DUsInSmp'", 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pcntdus': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'pcntDUs'", 'blank': 'True'}),
            'pcntpop': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'PcntPop'", 'blank': 'True'}),
            'pop': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'Pop'", 'blank': 'True'}),
            'smpdus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'SmpDUs'", 'blank': 'True'}),
            'totalppleinarea': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'TotalPpleinArea'", 'blank': 'True'}),
            'totdus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'TotDUs'", 'blank': 'True'})
        },
        u'majitables.wsrcdrkbhpmpslum': {
            'Meta': {'object_name': 'Wsrcdrkbhpmpslum', 'db_table': "u'WSrcDrkBhPmpSlum'"},
            'dusinarea': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'DusInArea'", 'blank': 'True'}),
            'dusinsmp': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'DUsInSmp'", 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pcntdus': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'pcntDUs'", 'blank': 'True'}),
            'pcntpop': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'PcntPop'", 'blank': 'True'}),
            'pop': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'Pop'", 'blank': 'True'}),
            'slumid': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'SlumID'", 'blank': 'True'}),
            'slumname': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'SlumName'"}),
            'smpdus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'SmpDUs'", 'blank': 'True'}),
            'totalppleinarea': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'TotalPpleinArea'", 'blank': 'True'}),
            'totdus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'TotDUs'", 'blank': 'True'})
        },
        u'majitables.wsrcdrkbhpmptown': {
            'Meta': {'object_name': 'Wsrcdrkbhpmptown', 'db_table': "u'WSrcDrkBhPmpTown'"},
            'dusinarea': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'DusInArea'", 'blank': 'True'}),
            'dusinsmp': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'DUsInSmp'", 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pcntdus': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'pcntDUs'", 'blank': 'True'}),
            'pcntpop': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'PcntPop'", 'blank': 'True'}),
            'pop': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'Pop'", 'blank': 'True'}),
            'smpdus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'SmpDUs'", 'blank': 'True'}),
            'totalppleinarea': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'TotalPpleinArea'", 'blank': 'True'}),
            'totdus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'TotDUs'", 'blank': 'True'}),
            'townid': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'TownID'", 'blank': 'True'}),
            'townname': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'TownName'"})
        },
        u'majitables.wsrcdrkbhpmpwsp': {
            'Meta': {'object_name': 'Wsrcdrkbhpmpwsp', 'db_table': "u'WSrcDrkBhPmpWSP'"},
            'dusinarea': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'DusInArea'", 'blank': 'True'}),
            'dusinsmp': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'DUsInSmp'", 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pcntdus': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'pcntDUs'", 'blank': 'True'}),
            'pcntpop': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'PcntPop'", 'blank': 'True'}),
            'pop': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'Pop'", 'blank': 'True'}),
            'smpdus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'SmpDUs'", 'blank': 'True'}),
            'totalppleinarea': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'TotalPpleinArea'", 'blank': 'True'}),
            'totdus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'TotDUs'", 'blank': 'True'}),
            'wspid': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'WspID'"}),
            'wspname': ('django.db.models.fields.CharField', [], {'max_length': '45', 'db_column': "u'WspName'"})
        },
        u'majitables.wsrcdrkksk': {
            'Meta': {'object_name': 'Wsrcdrkksk', 'db_table': "u'WSrcDrkKsk'"},
            'areaid': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'AreaID'", 'blank': 'True'}),
            'areaname': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'Areaname'"}),
            'areasmpdus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'AreaSmpDUs'", 'blank': 'True'}),
            'dusinarea': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'DusInArea'", 'blank': 'True'}),
            'dusinsmp': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'DUsInSmp'", 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pcntdus': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'pcntDUs'", 'blank': 'True'}),
            'pcntpple': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'smppersons': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'SmpPersons'", 'blank': 'True'}),
            'totaldusinarea': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'TotalDUsInArea'", 'blank': 'True'}),
            'totalppleinarea': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'TotalPpleinArea'", 'blank': 'True'})
        },
        u'majitables.wsrcdrkleakcounty': {
            'Meta': {'object_name': 'Wsrcdrkleakcounty', 'db_table': "u'WSrcDrkLeakCounty'"},
            'countyid': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'CountyID'"}),
            'countyname': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'CountyName'"}),
            'dusinarea': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'DusInArea'"}),
            'dusinsmp': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'DUsInSmp'"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pcntdus': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'pcntDUs'"}),
            'pcntpop': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'PcntPop'"}),
            'pop': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'Pop'"}),
            'smpdus': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'SmpDUs'"}),
            'totalppleinarea': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'TotalPpleinArea'"}),
            'totdus': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'TotDUs'"})
        },
        u'majitables.wsrcdrkleakslum': {
            'Meta': {'object_name': 'Wsrcdrkleakslum', 'db_table': "u'WSrcDrkLeakSlum'"},
            'dusinarea': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'DusInArea'"}),
            'dusinsmp': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'DUsInSmp'"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pcntdus': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'pcntDUs'"}),
            'pcntpop': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'PcntPop'"}),
            'pop': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'Pop'"}),
            'slumid': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'SlumID'"}),
            'slumname': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'SlumName'"}),
            'smpdus': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'SmpDUs'"}),
            'totalppleinarea': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'TotalPpleinArea'"}),
            'totdus': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'TotDUs'"})
        },
        u'majitables.wsrcdrkleaktown': {
            'Meta': {'object_name': 'Wsrcdrkleaktown', 'db_table': "u'WSrcDrkLeakTown'"},
            'dusinarea': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'DusInArea'"}),
            'dusinsmp': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'DUsInSmp'"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pcntdus': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'pcntDUs'"}),
            'pcntpop': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'PcntPop'"}),
            'pop': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'Pop'"}),
            'smpdus': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'SmpDUs'"}),
            'totalppleinarea': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'TotalPpleinArea'"}),
            'totdus': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'TotDUs'"}),
            'townid': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'TownID'"}),
            'townname': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'TownName'"})
        },
        u'majitables.wsrcdrkleakwsp': {
            'Meta': {'object_name': 'Wsrcdrkleakwsp', 'db_table': "u'WSrcDrkLeakWSP'"},
            'dusinarea': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'DusInArea'"}),
            'dusinsmp': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'DUsInSmp'"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pcntdus': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'pcntDUs'"}),
            'pcntpop': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'PcntPop'"}),
            'pop': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'Pop'"}),
            'smpdus': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'SmpDUs'"}),
            'totalppleinarea': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'TotalPpleinArea'"}),
            'totdus': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'TotDUs'"}),
            'wspid': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'WSPID'"}),
            'wspname': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'WSPName'"})
        },
        u'majitables.wsrcdrkspringcounty': {
            'Meta': {'object_name': 'Wsrcdrkspringcounty', 'db_table': "u'WSrcDrkSpringCounty'"},
            'countyid': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'CountyID'", 'blank': 'True'}),
            'countyname': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'CountyName'"}),
            'dusinarea': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'DusInArea'", 'blank': 'True'}),
            'dusinsmp': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'DUsInSmp'", 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pcntdus': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'pcntDUs'", 'blank': 'True'}),
            'pcntpop': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'PcntPop'", 'blank': 'True'}),
            'pop': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'Pop'", 'blank': 'True'}),
            'smpdus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'SmpDUs'", 'blank': 'True'}),
            'totalppleinarea': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'TotalPpleinArea'", 'blank': 'True'}),
            'totdus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'TotDUs'", 'blank': 'True'})
        },
        u'majitables.wsrcdrkspringslum': {
            'Meta': {'object_name': 'Wsrcdrkspringslum', 'db_table': "u'WSrcDrkSpringSlum'"},
            'dusinarea': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'DusInArea'", 'blank': 'True'}),
            'dusinsmp': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'DUsInSmp'", 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pcntdus': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'pcntDUs'", 'blank': 'True'}),
            'pcntpop': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'PcntPop'", 'blank': 'True'}),
            'pop': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'Pop'", 'blank': 'True'}),
            'slumid': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'SlumID'", 'blank': 'True'}),
            'slumname': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'SlumName'"}),
            'smpdus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'SmpDUs'", 'blank': 'True'}),
            'totalppleinarea': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'TotalPpleinArea'", 'blank': 'True'}),
            'totdus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'TotDUs'", 'blank': 'True'})
        },
        u'majitables.wsrcdrkspringtown': {
            'Meta': {'object_name': 'Wsrcdrkspringtown', 'db_table': "u'WSrcDrkSpringTown'"},
            'dusinarea': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'DusInArea'", 'blank': 'True'}),
            'dusinsmp': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'DUsInSmp'", 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pcntdus': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'pcntDUs'", 'blank': 'True'}),
            'pcntpop': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'PcntPop'", 'blank': 'True'}),
            'pop': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'Pop'", 'blank': 'True'}),
            'smpdus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'SmpDUs'", 'blank': 'True'}),
            'totalppleinarea': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'TotalPpleinArea'", 'blank': 'True'}),
            'totdus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'TotDUs'", 'blank': 'True'}),
            'townid': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'TownID'", 'blank': 'True'}),
            'townname': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'TownName'"})
        },
        u'majitables.wsrcdrkspringwsp': {
            'Meta': {'object_name': 'Wsrcdrkspringwsp', 'db_table': "u'WSrcDrkSpringWSP'"},
            'dusinarea': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'DusInArea'", 'blank': 'True'}),
            'dusinsmp': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'DUsInSmp'", 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pcntdus': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'pcntDUs'", 'blank': 'True'}),
            'pcntpop': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'PcntPop'", 'blank': 'True'}),
            'pop': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'Pop'", 'blank': 'True'}),
            'smpdus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'SmpDUs'", 'blank': 'True'}),
            'totalppleinarea': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'TotalPpleinArea'", 'blank': 'True'}),
            'totdus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'TotDUs'", 'blank': 'True'}),
            'wspid': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'WSPID'"}),
            'wspname': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'WSPName'"})
        },
        u'majitables.wsrcdrkvendorcounty': {
            'Meta': {'object_name': 'Wsrcdrkvendorcounty', 'db_table': "u'WSrcDrkVendorCounty'"},
            'countyid': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'CountyID'", 'blank': 'True'}),
            'countyname': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'CountyName'"}),
            'dusinarea': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'DusInArea'", 'blank': 'True'}),
            'dusinsmp': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'DUsInSmp'", 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pcntdus': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'pcntDUs'", 'blank': 'True'}),
            'pcntpop': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'PcntPop'", 'blank': 'True'}),
            'pop': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'Pop'", 'blank': 'True'}),
            'smpdus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'SmpDUs'", 'blank': 'True'}),
            'totalppleinarea': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'TotalPpleinArea'", 'blank': 'True'}),
            'totdus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'TotDUs'", 'blank': 'True'})
        },
        u'majitables.wsrcdrkvendorslum': {
            'Meta': {'object_name': 'Wsrcdrkvendorslum', 'db_table': "u'WSrcDrkVendorSlum'"},
            'dusinarea': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'DusInArea'", 'blank': 'True'}),
            'dusinsmp': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'DUsInSmp'", 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pcntdus': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'pcntDUs'", 'blank': 'True'}),
            'pcntpop': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'PcntPop'", 'blank': 'True'}),
            'pop': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'Pop'", 'blank': 'True'}),
            'slumid': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'SlumID'", 'blank': 'True'}),
            'slumname': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'SlumName'"}),
            'smpdus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'SmpDUs'", 'blank': 'True'}),
            'totalppleinarea': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'TotalPpleinArea'", 'blank': 'True'}),
            'totdus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'TotDUs'", 'blank': 'True'})
        },
        u'majitables.wsrcdrkvendortown': {
            'Meta': {'object_name': 'Wsrcdrkvendortown', 'db_table': "u'WSrcDrkVendorTown'"},
            'dusinarea': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'DusInArea'", 'blank': 'True'}),
            'dusinsmp': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'DUsInSmp'", 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pcntdus': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'pcntDUs'", 'blank': 'True'}),
            'pcntpop': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'PcntPop'", 'blank': 'True'}),
            'pop': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'Pop'", 'blank': 'True'}),
            'smpdus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'SmpDUs'", 'blank': 'True'}),
            'totalppleinarea': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'TotalPpleinArea'", 'blank': 'True'}),
            'totdus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'TotDUs'", 'blank': 'True'}),
            'townid': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'TownID'", 'blank': 'True'}),
            'townname': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'TownName'"})
        },
        u'majitables.wsrcdrkvendorwsp': {
            'Meta': {'object_name': 'Wsrcdrkvendorwsp', 'db_table': "u'WSrcDrkVendorWSP'"},
            'dusinarea': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'DusInArea'", 'blank': 'True'}),
            'dusinsmp': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'DUsInSmp'", 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pcntdus': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'pcntDUs'", 'blank': 'True'}),
            'pcntpop': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'PcntPop'", 'blank': 'True'}),
            'pop': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'Pop'", 'blank': 'True'}),
            'smpdus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'SmpDUs'", 'blank': 'True'}),
            'totalppleinarea': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'TotalPpleinArea'", 'blank': 'True'}),
            'totdus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'TotDUs'", 'blank': 'True'}),
            'wspid': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'WSPID'"}),
            'wspname': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'WSPName'"})
        },
        u'majitables.wsrcdrkwellscounty': {
            'Meta': {'object_name': 'Wsrcdrkwellscounty', 'db_table': "u'WSrcDrkWellsCounty'"},
            'countyid': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'CountyID'", 'blank': 'True'}),
            'countyname': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'CountyName'"}),
            'dusinarea': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'DusInArea'", 'blank': 'True'}),
            'dusinsmp': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'DUsInSmp'", 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pcntdus': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'pcntDUs'", 'blank': 'True'}),
            'pcntpop': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'PcntPop'", 'blank': 'True'}),
            'pop': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'Pop'", 'blank': 'True'}),
            'smpdus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'SmpDUs'", 'blank': 'True'}),
            'totalppleinarea': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'TotalPpleinArea'", 'blank': 'True'}),
            'totdus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'TotDUs'", 'blank': 'True'})
        },
        u'majitables.wsrcdrkwellsslum': {
            'Meta': {'object_name': 'Wsrcdrkwellsslum', 'db_table': "u'WSrcDrkWellsSlum'"},
            'dusinarea': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'DusInArea'", 'blank': 'True'}),
            'dusinsmp': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'DUsInSmp'", 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pcntdus': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'pcntDUs'", 'blank': 'True'}),
            'pcntpop': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'PcntPop'", 'blank': 'True'}),
            'pop': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'Pop'", 'blank': 'True'}),
            'slumid': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'SlumID'", 'blank': 'True'}),
            'slumname': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'SlumName'"}),
            'smpdus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'SmpDUs'", 'blank': 'True'}),
            'totalppleinarea': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'TotalPpleinArea'", 'blank': 'True'}),
            'totdus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'TotDUs'", 'blank': 'True'})
        },
        u'majitables.wsrcdrkwellstown': {
            'Meta': {'object_name': 'Wsrcdrkwellstown', 'db_table': "u'WSrcDrkWellsTown'"},
            'dusinarea': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'DusInArea'", 'blank': 'True'}),
            'dusinsmp': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'DUsInSmp'", 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pcntdus': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'pcntDUs'", 'blank': 'True'}),
            'pcntpop': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'PcntPop'", 'blank': 'True'}),
            'pop': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'Pop'", 'blank': 'True'}),
            'smpdus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'SmpDUs'", 'blank': 'True'}),
            'totalppleinarea': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'TotalPpleinArea'", 'blank': 'True'}),
            'totdus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'TotDUs'", 'blank': 'True'}),
            'townid': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'TownID'", 'blank': 'True'}),
            'townname': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'TownName'"})
        },
        u'majitables.wsrcdrkwellswsp': {
            'Meta': {'object_name': 'Wsrcdrkwellswsp', 'db_table': "u'WSrcDrkWellsWSP'"},
            'dusinarea': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'DusInArea'", 'blank': 'True'}),
            'dusinsmp': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'DUsInSmp'", 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pcntdus': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'pcntDUs'", 'blank': 'True'}),
            'pcntpop': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'PcntPop'", 'blank': 'True'}),
            'pop': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'Pop'", 'blank': 'True'}),
            'smpdus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'SmpDUs'", 'blank': 'True'}),
            'totalppleinarea': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'TotalPpleinArea'", 'blank': 'True'}),
            'totdus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'TotDUs'", 'blank': 'True'}),
            'wspid': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'WSPID'"}),
            'wspname': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'WSPName'"})
        },
        u'majitables.wsupplyinf8e': {
            'Meta': {'object_name': 'Wsupplyinf8E', 'db_table': "u'WSupplyInf-8e'"},
            'areaid': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'AreaID'", 'blank': 'True'}),
            'communityschm': ('django.db.models.fields.TextField', [], {'db_column': "u'Communityschm'", 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'infwaterqlty': ('django.db.models.fields.TextField', [], {'db_column': "u'InfWaterqlty'", 'blank': 'True'}),
            'ngoscheme': ('django.db.models.fields.TextField', [], {'db_column': "u'NGOscheme'", 'blank': 'True'}),
            'tariffrem': ('django.db.models.fields.TextField', [], {'db_column': "u'TariffRem'", 'blank': 'True'}),
            'waterresellers': ('django.db.models.fields.TextField', [], {'db_column': "u'Waterresellers'", 'blank': 'True'}),
            'winftariffp20l1': ('django.db.models.fields.TextField', [], {'db_column': "u'Winftariffp20l1'", 'blank': 'True'}),
            'winftariffp20l2': ('django.db.models.fields.TextField', [], {'db_column': "u'Winftariffp20l2'", 'blank': 'True'}),
            'winftariffp20l3': ('django.db.models.fields.TextField', [], {'db_column': "u'Winftariffp20l3'", 'blank': 'True'}),
            'wsupplyproj': ('django.db.models.fields.TextField', [], {'db_column': "u'Wsupplyproj'"})
        },
        u'majitables.wsupsituation28': {
            'Meta': {'object_name': 'Wsupsituation28', 'db_table': "u'WSupSituation2-8'"},
            'areaid': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'AreaID'", 'blank': 'True'}),
            'areaname': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'Areaname'"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'protectedsrc': ('django.db.models.fields.TextField', [], {'db_column': "u'ProtectedSrc'"}),
            'unprotectedsrc': ('django.db.models.fields.TextField', [], {'db_column': "u'UnProtectedSrc'"})
        },
        u'majitables.wsupsituation38d': {
            'Meta': {'object_name': 'Wsupsituation38D', 'db_table': "u'WSupSituation3-8d'"},
            'areaid': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'AreaID'", 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'illegalcon': ('django.db.models.fields.TextField', [], {'db_column': "u'IllegalCon'", 'blank': 'True'}),
            'rationrem': ('django.db.models.fields.TextField', [], {'db_column': "u'RationRem'", 'blank': 'True'}),
            'supply24hr': ('django.db.models.fields.TextField', [], {'db_column': "u'Supply24hr'", 'blank': 'True'}),
            'supplyinfo': ('django.db.models.fields.TextField', [], {'db_column': "u'SupplyInfo'", 'blank': 'True'}),
            'tariffrem': ('django.db.models.fields.TextField', [], {'db_column': "u'TariffRem'", 'blank': 'True'}),
            'waterpressure': ('django.db.models.fields.TextField', [], {'db_column': "u'WaterPressure'", 'blank': 'True'}),
            'waterqlty': ('django.db.models.fields.TextField', [], {'db_column': "u'WaterQlty'", 'blank': 'True'}),
            'waterrationing': ('django.db.models.fields.TextField', [], {'db_column': "u'Waterrationing'", 'blank': 'True'}),
            'wdyspwk': ('django.db.models.fields.TextField', [], {'db_column': "u'Wdyspwk'", 'blank': 'True'}),
            'wsptariffapprvd': ('django.db.models.fields.TextField', [], {'db_column': "u'WSPTariffapprvd'", 'blank': 'True'}),
            'wwsptariffp20l': ('django.db.models.fields.TextField', [], {'db_column': "u'Wwsptariffp20l'", 'blank': 'True'}),
            'wwsptariffpmnth': ('django.db.models.fields.TextField', [], {'db_column': "u'Wwsptariffpmnth'", 'blank': 'True'}),
            'wwsptariffpunit': ('django.db.models.fields.TextField', [], {'db_column': "u'Wwsptariffpunit'", 'blank': 'True'})
        },
        u'majitables.wsupsituation8': {
            'Meta': {'object_name': 'Wsupsituation8', 'db_table': "u'WSupSituation-8'"},
            'areaid': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'AreaID'", 'blank': 'True'}),
            'arealinkedwater': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'AreaLinkedwater'"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'maindrkgwatersrc': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'MainDrkgWaterSrc'"}),
            'mainwaterprob': ('django.db.models.fields.TextField', [], {'db_column': "u'MainWaterProb'"}),
            'mainwatersrc': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'MainWaterSrc'"}),
            'techstat': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'TechStat'"}),
            'wnwdist': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'WnwDist'"})
        },
        u'majitables.wsupsituationdu': {
            'Meta': {'object_name': 'Wsupsituationdu', 'db_table': "u'WSupSituationDU'"},
            'areaid': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'AreaID'", 'blank': 'True'}),
            'areaname': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'Areaname'"}),
            'areasmpdus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'AreaSmpDUs'", 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ndus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'NDus'", 'blank': 'True'}),
            'nousingsrc': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'Nousingsrc'", 'blank': 'True'}),
            'numdu': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'NumDU'", 'blank': 'True'}),
            'pcntdus': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'pcntDUs'", 'blank': 'True'}),
            'pcntpple': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'persons': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'wsituation': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'Wsituation'"})
        },
        u'majitables.wunreliablesrcbath': {
            'Meta': {'object_name': 'Wunreliablesrcbath', 'db_table': "u'WUnreliableSrcBath'"},
            'areaid': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'AreaID'", 'blank': 'True'}),
            'areaname': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'Areaname'"}),
            'areasmpdus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'AreaSmpDUs'", 'blank': 'True'}),
            'areasmppop': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'AreaSmpPop'", 'blank': 'True'}),
            'dusinarea': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'DusInArea'", 'blank': 'True'}),
            'dusinsmp': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'DUsInSmp'", 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pcntdus': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'pcntDUs'", 'blank': 'True'}),
            'pcntpple': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'smppersons': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'SmpPersons'", 'blank': 'True'}),
            'totaldusinarea': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'TotalDUsInArea'", 'blank': 'True'}),
            'totalppleinarea': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'TotalPpleinArea'", 'blank': 'True'})
        },
        u'majitables.wunreliablesrcdrk': {
            'Meta': {'object_name': 'Wunreliablesrcdrk', 'db_table': "u'WUnreliableSrcDrk'"},
            'areaid': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'AreaID'", 'blank': 'True'}),
            'areaname': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'Areaname'"}),
            'areasmpdus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'AreaSmpDUs'", 'blank': 'True'}),
            'areasmppop': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'AreaSmpPop'", 'blank': 'True'}),
            'dusinarea': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'DusInArea'", 'blank': 'True'}),
            'dusinsmp': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'DUsInSmp'", 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pcntdus': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'pcntDUs'", 'blank': 'True'}),
            'pcntpple': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'smppersons': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'SmpPersons'", 'blank': 'True'}),
            'totaldusinarea': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'TotalDUsInArea'", 'blank': 'True'}),
            'totalppleinarea': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'TotalPpleinArea'", 'blank': 'True'})
        },
        u'majitables.wunreliablesrcdrkavgpay': {
            'Meta': {'object_name': 'Wunreliablesrcdrkavgpay', 'db_table': "u'WUnreliableSrcDrkAvgPay'"},
            'areaid': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'AreaID'", 'blank': 'True'}),
            'areaname': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'Areaname'"}),
            'areasmpdus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'AreaSmpDUs'", 'blank': 'True'}),
            'avgpaydrk': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'AvgPayDrk'", 'blank': 'True'}),
            'dusinarea': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'DusInArea'", 'blank': 'True'}),
            'dusinsmp': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'DUsInSmp'", 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'paymthd': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'PayMthd'"}),
            'pcntdus': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'pcntDUs'", 'blank': 'True'}),
            'pcntpple': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'smppersons': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'SmpPersons'", 'blank': 'True'}),
            'totaldusinarea': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'TotalDUsInArea'", 'blank': 'True'}),
            'totalppleinarea': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'TotalPpleinArea'", 'blank': 'True'})
        },
        u'majitables.wunreliablesrcdrktrt': {
            'Meta': {'object_name': 'Wunreliablesrcdrktrt', 'db_table': "u'WUnreliableSrcDrkTrt'"},
            'areaid': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'AreaID'", 'blank': 'True'}),
            'areaname': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'Areaname'"}),
            'areasmpdus': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'AreaSmpDUs'", 'blank': 'True'}),
            'dusinarea': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'DusInArea'", 'blank': 'True'}),
            'dusinsmp': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'DUsInSmp'", 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pcntdus': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'pcntDUs'", 'blank': 'True'}),
            'pcntpple': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'smppersons': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'SmpPersons'", 'blank': 'True'}),
            'totaldusinarea': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'TotalDUsInArea'", 'blank': 'True'}),
            'totalppleinarea': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'TotalPpleinArea'", 'blank': 'True'})
        },
        u'majitables.wusersperindcon10d': {
            'Meta': {'object_name': 'Wusersperindcon10D', 'db_table': "u'WUsersPerIndCon-10d'"},
            'area': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'Area'", 'blank': 'True'}),
            'areaname': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'Areaname'"}),
            'areapop': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'AreaPop'", 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'noofconsinarea': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'NoofConsinArea'", 'blank': 'True'}),
            'noofsmpcons': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'NoofSmpCons'", 'blank': 'True'}),
            'smppersons': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'SmpPersons'", 'blank': 'True'}),
            'totalppleinarea': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'TotalPpleinArea'", 'blank': 'True'}),
            'userspercon': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'UsersPercon'", 'blank': 'True'})
        },
        u'majitables.wusersperksk': {
            'Meta': {'object_name': 'Wusersperksk', 'db_table': "u'WUsersPerKsk'"},
            'areaid': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'AreaID'", 'blank': 'True'}),
            'areaname': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'Areaname'"}),
            'areapop': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'AreaPop'", 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pubwaterksks': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'PubWaterKsks'", 'blank': 'True'}),
            'totalppleinarea': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'TotalPpleinArea'", 'blank': 'True'}),
            'usersperksk': ('django.db.models.fields.CharField', [], {'max_length': '24', 'db_column': "u'UsersPerKsk'"})
        },
        u'majitables.wusersperpubtap10d': {
            'Meta': {'object_name': 'Wusersperpubtap10D', 'db_table': "u'WUsersPerPubTap-10d'"},
            'areaid': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "u'AreaID'", 'blank': 'True'}),
            'areaname': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'Areaname'"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ntaps': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "u'NTaps'", 'blank': 'True'}),
            'nusers': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'NUsers'"}),
            'usersperpubtap': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "u'UsersPerPubTap'"})
        }
    }

    complete_apps = ['majitables']