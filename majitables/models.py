# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#     * Rearrange models' order
#     * Make sure each model has one field with primary_key=True
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [appname]'
# into your database.
from __future__ import unicode_literals

from django.db import models

class Apopdenavgminmaxcounty(models.Model): 
    countyname = models.CharField(max_length=100, db_column='Countyname') # Field name made lowercase.
    countyid = models.IntegerField(null=True, db_column='CountyID', blank=True) # Field name made lowercase.
    avgsqkm = models.FloatField(null=True, db_column='AvgSqKm', blank=True) # Field name made lowercase.
    avgpopden = models.IntegerField(null=True, db_column='AvgPopDen', blank=True) # Field name made lowercase.
    nareas = models.IntegerField(null=True, db_column='NAreas', blank=True) # Field name made lowercase.
    max = models.IntegerField(null=True, db_column='Max', blank=True) # Field name made lowercase.
    min = models.IntegerField(null=True, db_column='Min', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'APopDenAvgMinMaxCounty'

class Apopdenavgminmaxslum(models.Model): 
    slumname = models.CharField(max_length=100, db_column='Slumname') # Field name made lowercase.
    slumid = models.CharField(max_length=100, db_column='SlumID') # Field name made lowercase.
    avgsqkm = models.FloatField(null=True, db_column='AvgSqKm', blank=True) # Field name made lowercase.
    avgpopden = models.IntegerField(null=True, db_column='AvgPopDen', blank=True) # Field name made lowercase.
    nareas = models.IntegerField(null=True, db_column='NAreas', blank=True) # Field name made lowercase.
    max = models.IntegerField(null=True, db_column='Max', blank=True) # Field name made lowercase.
    min = models.IntegerField(null=True, db_column='Min', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'APopDenAvgMinMaxSlum'

class Apopdenavgminmaxtown(models.Model): 
    townname = models.CharField(max_length=100)
    townid = models.IntegerField(null=True, db_column='townID', blank=True) # Field name made lowercase.
    avgsqkm = models.FloatField(null=True, db_column='AvgSqKm', blank=True) # Field name made lowercase.
    avgpopden = models.IntegerField(null=True, db_column='AvgPopDen', blank=True) # Field name made lowercase.
    nareas = models.IntegerField(null=True, db_column='NAreas', blank=True) # Field name made lowercase.
    max = models.IntegerField(null=True, db_column='Max', blank=True) # Field name made lowercase.
    min = models.IntegerField(null=True, db_column='Min', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'APopDenAvgMinMaxTown'

class Apopdenavgminmaxwsp(models.Model): 
    wspname = models.CharField(max_length=100, blank=True)
    wspid = models.CharField(max_length=20, db_column='wspID', blank=True) # Field name made lowercase.
    avgsqkm = models.FloatField(null=True, db_column='AvgSqKm', blank=True) # Field name made lowercase.
    avgpopden = models.IntegerField(null=True, db_column='AvgPopDen', blank=True) # Field name made lowercase.
    nareas = models.IntegerField(null=True, db_column='NAreas', blank=True) # Field name made lowercase.
    max = models.IntegerField(null=True, db_column='Max', blank=True) # Field name made lowercase.
    min = models.IntegerField(null=True, db_column='Min', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'APopDenAvgMinMaxWSP'

class Apopdennareascounty(models.Model): 
    countyid = models.IntegerField(null=True, db_column='countyID', blank=True) # Field name made lowercase.
    countyname = models.CharField(max_length=100)
    popden = models.CharField(max_length=100, db_column='PopDen') # Field name made lowercase.
    nareas = models.IntegerField(null=True, db_column='NAreas', blank=True) # Field name made lowercase.
    pcntareas = models.FloatField(null=True, db_column='PcntAreas', blank=True) # Field name made lowercase.
    totareas = models.IntegerField(null=True, db_column='TotAreas', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'APopDenNAreasCounty'

class Apopdennareasslum(models.Model): 
    slumid = models.IntegerField(null=True, db_column='slumID', blank=True) # Field name made lowercase.
    slumname = models.CharField(max_length=100)
    popden = models.CharField(max_length=100, db_column='PopDen') # Field name made lowercase.
    nareas = models.IntegerField(null=True, db_column='NAreas', blank=True) # Field name made lowercase.
    pcntareas = models.IntegerField(null=True, db_column='PcntAreas', blank=True) # Field name made lowercase.
    totareas = models.IntegerField(null=True, db_column='TotAreas', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'APopDenNAreasSlum'

class Apopdennareastowns(models.Model): 
    townid = models.IntegerField(null=True, db_column='townID', blank=True) # Field name made lowercase.
    townname = models.CharField(max_length=100)
    popden = models.CharField(max_length=100, db_column='PopDen') # Field name made lowercase.
    nareas = models.IntegerField(null=True, db_column='NAreas', blank=True) # Field name made lowercase.
    pcntareas = models.FloatField(null=True, db_column='PcntAreas', blank=True) # Field name made lowercase.
    totareas = models.IntegerField(null=True, db_column='TotAreas', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'APopDenNAreasTowns'

class Apopdennareaswsp(models.Model): 
    wspid = models.CharField(max_length=20, db_column='wspID', blank=True) # Field name made lowercase.
    wspname = models.CharField(max_length=100, blank=True)
    popden = models.CharField(max_length=20, db_column='PopDen', blank=True) # Field name made lowercase.
    nareas = models.IntegerField(null=True, db_column='NAreas', blank=True) # Field name made lowercase.
    pcntareas = models.FloatField(null=True, db_column='PcntAreas', blank=True) # Field name made lowercase.
    totareas = models.IntegerField(null=True, db_column='TotAreas', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'APopDenNAreasWSP'

class Areadustatuscounty(models.Model): 
    countyid = models.IntegerField(null=True, db_column='CountyID', blank=True) # Field name made lowercase.
    countyname = models.CharField(max_length=100, db_column='CountyName') # Field name made lowercase.
    dustatus = models.CharField(max_length=100, db_column='DUStatus') # Field name made lowercase.
    nareas = models.IntegerField(null=True, db_column='Nareas', blank=True) # Field name made lowercase.
    smpdus = models.IntegerField(null=True, db_column='SmpDUs', blank=True) # Field name made lowercase.
    pcntdus = models.FloatField(null=True, db_column='pcntDUs', blank=True) # Field name made lowercase.
    dusinarea = models.IntegerField(null=True, db_column='DusInArea', blank=True) # Field name made lowercase.
    totdus = models.IntegerField(null=True, db_column='TotDUs', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'AreaDUStatusCounty'

class Areadustatusslum(models.Model): 
    slumid = models.CharField(max_length=100, db_column='SlumID') # Field name made lowercase.
    slumname = models.CharField(max_length=100, db_column='SlumName') # Field name made lowercase.
    dustatus = models.CharField(max_length=100, db_column='DUStatus') # Field name made lowercase.
    nareas = models.IntegerField(null=True, db_column='Nareas', blank=True) # Field name made lowercase.
    smpdus = models.CharField(max_length=100, db_column='SmpDUs') # Field name made lowercase.
    pcntdus = models.CharField(max_length=100, db_column='pcntDUs') # Field name made lowercase.
    dusinarea = models.CharField(max_length=100, db_column='DusInArea') # Field name made lowercase.
    totdus = models.CharField(max_length=100, db_column='TotDUs') # Field name made lowercase.
    class Meta:
        db_table = 'AreaDUStatusSlum'

class Areadustatustown(models.Model): 
    townid = models.IntegerField(null=True, db_column='TownID', blank=True) # Field name made lowercase.
    townname = models.CharField(max_length=100, db_column='TownName') # Field name made lowercase.
    dustatus = models.CharField(max_length=100, db_column='DUStatus') # Field name made lowercase.
    nareas = models.IntegerField(null=True, db_column='Nareas', blank=True) # Field name made lowercase.
    smpdus = models.IntegerField(null=True, db_column='SmpDUs', blank=True) # Field name made lowercase.
    pcntdus = models.FloatField(null=True, db_column='pcntDUs', blank=True) # Field name made lowercase.
    dusinarea = models.IntegerField(null=True, db_column='DusInArea', blank=True) # Field name made lowercase.
    totdus = models.IntegerField(null=True, db_column='TotDUs', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'AreaDUStatusTown'

class Areadustatuswsp(models.Model): 
    wspid = models.CharField(max_length=100, db_column='WspID') # Field name made lowercase.
    wspname = models.CharField(max_length=100, db_column='WspName') # Field name made lowercase.
    dustatus = models.CharField(max_length=100, db_column='DUStatus') # Field name made lowercase.
    nareas = models.IntegerField(null=True, db_column='Nareas', blank=True) # Field name made lowercase.
    smpdus = models.IntegerField(null=True, db_column='SmpDUs', blank=True) # Field name made lowercase.
    pcntdus = models.FloatField(null=True, db_column='pcntDUs', blank=True) # Field name made lowercase.
    dusinarea = models.IntegerField(null=True, db_column='DusInArea', blank=True) # Field name made lowercase.
    totdus = models.IntegerField(null=True, db_column='TotDUs', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'AreaDUStatusWSP'

class Areadutypecounty(models.Model): 
    countyid = models.IntegerField(null=True, db_column='CountyID', blank=True) # Field name made lowercase.
    countyname = models.CharField(max_length=100, db_column='CountyName') # Field name made lowercase.
    dutype = models.CharField(max_length=100, db_column='DUType') # Field name made lowercase.
    nareas = models.IntegerField(null=True, db_column='Nareas', blank=True) # Field name made lowercase.
    smpdus = models.IntegerField(null=True, db_column='SmpDUs', blank=True) # Field name made lowercase.
    pcntdus = models.FloatField(null=True, db_column='pcntDUs', blank=True) # Field name made lowercase.
    dusinarea = models.IntegerField(null=True, db_column='DusInArea', blank=True) # Field name made lowercase.
    totdus = models.IntegerField(null=True, db_column='TotDUs', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'AreaDUTypeCounty'

class Areadutypeslum(models.Model): 
    slumid = models.IntegerField(null=True, db_column='SlumID', blank=True) # Field name made lowercase.
    slumname = models.CharField(max_length=100, db_column='SlumName') # Field name made lowercase.
    dutype = models.CharField(max_length=100, db_column='DUType') # Field name made lowercase.
    nareas = models.IntegerField(null=True, db_column='Nareas', blank=True) # Field name made lowercase.
    smpdus = models.IntegerField(null=True, db_column='SmpDUs', blank=True) # Field name made lowercase.
    pcntdus = models.FloatField(null=True, db_column='pcntDUs', blank=True) # Field name made lowercase.
    dusinarea = models.IntegerField(null=True, db_column='DusInArea', blank=True) # Field name made lowercase.
    totdus = models.IntegerField(null=True, db_column='TotDUs', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'AreaDUTypeSlum'

class Areadutypestructure(models.Model): 
    areaid = models.FloatField(null=True, db_column='AreaID', blank=True) # Field name made lowercase.
    dustatus = models.CharField(max_length=100, db_column='DUStatus') # Field name made lowercase.
    ndus = models.IntegerField(null=True, db_column='NDUs', blank=True) # Field name made lowercase.
    pcntdus = models.FloatField(null=True, db_column='PcntDUs', blank=True) # Field name made lowercase.
    areasmpdus = models.IntegerField(null=True, db_column='AreaSmpDUs', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'AreaDUTypeStructure'

class Areadutypetown(models.Model): 
    townid = models.IntegerField(null=True, db_column='TownID', blank=True) # Field name made lowercase.
    townname = models.CharField(max_length=100, db_column='TownName') # Field name made lowercase.
    dutype = models.CharField(max_length=100, db_column='DUType') # Field name made lowercase.
    nareas = models.IntegerField(null=True, db_column='Nareas', blank=True) # Field name made lowercase.
    smpdus = models.IntegerField(null=True, db_column='SmpDUs', blank=True) # Field name made lowercase.
    pcntdus = models.FloatField(null=True, db_column='pcntDUs', blank=True) # Field name made lowercase.
    dusinarea = models.IntegerField(null=True, db_column='DusInArea', blank=True) # Field name made lowercase.
    totdus = models.IntegerField(null=True, db_column='TotDUs', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'AreaDUTypeTown'

class Areadutypewsp(models.Model): 
    wspid = models.CharField(max_length=100, db_column='WspID') # Field name made lowercase.
    wspname = models.CharField(max_length=100, db_column='WspName') # Field name made lowercase.
    dutype = models.CharField(max_length=100, db_column='DUType') # Field name made lowercase.
    nareas = models.IntegerField(null=True, db_column='Nareas', blank=True) # Field name made lowercase.
    smpdus = models.IntegerField(null=True, db_column='SmpDUs', blank=True) # Field name made lowercase.
    pcntdus = models.FloatField(null=True, db_column='pcntDUs', blank=True) # Field name made lowercase.
    dusinarea = models.IntegerField(null=True, db_column='DusInArea', blank=True) # Field name made lowercase.
    totdus = models.IntegerField(null=True, db_column='TotDUs', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'AreaDUTypeWSP'

class Areadutypehse(models.Model): 
    areaid = models.FloatField(null=True, db_column='AreaID', blank=True) # Field name made lowercase.
    dutype = models.CharField(max_length=100, db_column='DUType') # Field name made lowercase.
    ndus = models.IntegerField(null=True, db_column='NDUs', blank=True) # Field name made lowercase.
    pcntdus = models.FloatField(null=True, db_column='PcntDUs', blank=True) # Field name made lowercase.
    areasmpdus = models.IntegerField(null=True, db_column='AreaSmpDUs', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'AreaDUTypehse'

class Areahabhsetypecounty(models.Model): 
    countyid = models.IntegerField(null=True, db_column='CountyID', blank=True) # Field name made lowercase.
    countyname = models.CharField(max_length=100, db_column='CountyName') # Field name made lowercase.
    hsngtype = models.CharField(max_length=100, db_column='HsngType') # Field name made lowercase.
    nareas = models.IntegerField(null=True, db_column='Nareas', blank=True) # Field name made lowercase.
    pcntareas = models.FloatField(null=True, db_column='PcntAreas', blank=True) # Field name made lowercase.
    totareas = models.IntegerField(null=True, db_column='TotAreas', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'AreaHabHseTypeCounty'

class Areahabhsetypeslum(models.Model): 
    slumid = models.IntegerField(null=True, db_column='SlumID', blank=True) # Field name made lowercase.
    slumname = models.CharField(max_length=100, db_column='SlumName') # Field name made lowercase.
    hsngtype = models.CharField(max_length=100, db_column='HsngType') # Field name made lowercase.
    nareas = models.IntegerField(null=True, db_column='Nareas', blank=True) # Field name made lowercase.
    pcntareas = models.IntegerField(null=True, db_column='PcntAreas', blank=True) # Field name made lowercase.
    totareas = models.IntegerField(null=True, db_column='TotAreas', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'AreaHabHseTypeSlum'

class Areahabhsetypetown(models.Model): 
    townid = models.IntegerField(null=True, db_column='TownID', blank=True) # Field name made lowercase.
    townname = models.CharField(max_length=100, db_column='TownName') # Field name made lowercase.
    hsngtype = models.CharField(max_length=100, db_column='HsngType') # Field name made lowercase.
    nareas = models.IntegerField(null=True, db_column='Nareas', blank=True) # Field name made lowercase.
    pcntareas = models.FloatField(null=True, db_column='PcntAreas', blank=True) # Field name made lowercase.
    totareas = models.IntegerField(null=True, db_column='TotAreas', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'AreaHabHseTypeTown'

class Areahabhsetypewsp(models.Model): 
    wspid = models.CharField(max_length=100, db_column='WspID') # Field name made lowercase.
    wspname = models.CharField(max_length=100, db_column='WspName') # Field name made lowercase.
    hsngtype = models.CharField(max_length=100, db_column='HsngType') # Field name made lowercase.
    nareas = models.IntegerField(null=True, db_column='Nareas', blank=True) # Field name made lowercase.
    pcntareas = models.FloatField(null=True, db_column='PcntAreas', blank=True) # Field name made lowercase.
    totareas = models.IntegerField(null=True, db_column='TotAreas', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'AreaHabHseTypeWSP'

class Areahabhsgsitcounty(models.Model): 
    countyid = models.IntegerField(null=True, db_column='CountyID', blank=True) # Field name made lowercase.
    countyname = models.CharField(max_length=100, db_column='CountyName') # Field name made lowercase.
    hsgsituation = models.CharField(max_length=100, db_column='HsgSituation') # Field name made lowercase.
    nareas = models.IntegerField(null=True, db_column='Nareas', blank=True) # Field name made lowercase.
    pcntareas = models.FloatField(null=True, db_column='PcntAreas', blank=True) # Field name made lowercase.
    totareas = models.IntegerField(null=True, db_column='TotAreas', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'AreaHabHsgSitCounty'

class Areahabhsgsitslum(models.Model): 
    slumid = models.CharField(max_length=100, db_column='SlumID') # Field name made lowercase.
    slumname = models.CharField(max_length=100, db_column='SlumName') # Field name made lowercase.
    hsgsituation = models.CharField(max_length=100, db_column='HsgSituation') # Field name made lowercase.
    nareas = models.IntegerField(null=True, db_column='Nareas', blank=True) # Field name made lowercase.
    pcntareas = models.CharField(max_length=100, db_column='PcntAreas') # Field name made lowercase.
    totareas = models.CharField(max_length=100, db_column='TotAreas') # Field name made lowercase.
    class Meta:
        db_table = 'AreaHabHsgSitSlum'

class Areahabhsgsittown(models.Model): 
    townid = models.IntegerField(null=True, db_column='TownID', blank=True) # Field name made lowercase.
    townname = models.CharField(max_length=100, db_column='TownName') # Field name made lowercase.
    hsgsituation = models.CharField(max_length=100, db_column='HsgSituation') # Field name made lowercase.
    nareas = models.IntegerField(null=True, db_column='Nareas', blank=True) # Field name made lowercase.
    pcntareas = models.FloatField(null=True, db_column='PcntAreas', blank=True) # Field name made lowercase.
    totareas = models.IntegerField(null=True, db_column='TotAreas', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'AreaHabHsgSitTown'

class Areahabhsgsitwsp(models.Model): 
    wspid = models.CharField(max_length=100, db_column='WspID') # Field name made lowercase.
    wspname = models.CharField(max_length=100, db_column='WspName') # Field name made lowercase.
    hsgsituation = models.CharField(max_length=100, db_column='HsgSituation') # Field name made lowercase.
    nareas = models.IntegerField(null=True, db_column='Nareas', blank=True) # Field name made lowercase.
    pcntareas = models.FloatField(null=True, db_column='PcntAreas', blank=True) # Field name made lowercase.
    totareas = models.IntegerField(null=True, db_column='TotAreas', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'AreaHabHsgSitWSP'

class Areahabroofcounty(models.Model): 
    countyid = models.IntegerField(null=True, db_column='CountyID', blank=True) # Field name made lowercase.
    countyname = models.CharField(max_length=100, db_column='CountyName') # Field name made lowercase.
    roof = models.CharField(max_length=100, db_column='Roof') # Field name made lowercase.
    nareas = models.IntegerField(null=True, db_column='Nareas', blank=True) # Field name made lowercase.
    pcntareas = models.FloatField(null=True, db_column='PcntAreas', blank=True) # Field name made lowercase.
    totareas = models.IntegerField(null=True, db_column='TotAreas', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'AreaHabRoofCounty'

class Areahabroofslum(models.Model): 
    slumid = models.CharField(max_length=100, db_column='SlumID') # Field name made lowercase.
    slumname = models.CharField(max_length=100, db_column='SlumName') # Field name made lowercase.
    roof = models.CharField(max_length=100, db_column='Roof') # Field name made lowercase.
    nareas = models.IntegerField(null=True, db_column='Nareas', blank=True) # Field name made lowercase.
    pcntareas = models.CharField(max_length=100, db_column='PcntAreas') # Field name made lowercase.
    totareas = models.CharField(max_length=100, db_column='TotAreas') # Field name made lowercase.
    class Meta:
        db_table = 'AreaHabRoofSlum'

class Areahabrooftown(models.Model): 
    townid = models.IntegerField(null=True, db_column='TownID', blank=True) # Field name made lowercase.
    townname = models.CharField(max_length=100, db_column='TownName') # Field name made lowercase.
    roof = models.CharField(max_length=100, db_column='Roof') # Field name made lowercase.
    nareas = models.IntegerField(null=True, db_column='Nareas', blank=True) # Field name made lowercase.
    pcntareas = models.FloatField(null=True, db_column='PcntAreas', blank=True) # Field name made lowercase.
    totareas = models.IntegerField(null=True, db_column='TotAreas', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'AreaHabRoofTown'

class Areahabroofwsp(models.Model): 
    wspid = models.CharField(max_length=100, db_column='WspID') # Field name made lowercase.
    wspname = models.CharField(max_length=100, db_column='WspName') # Field name made lowercase.
    roof = models.CharField(max_length=100, db_column='Roof') # Field name made lowercase.
    nareas = models.IntegerField(null=True, db_column='Nareas', blank=True) # Field name made lowercase.
    pcntareas = models.FloatField(null=True, db_column='PcntAreas', blank=True) # Field name made lowercase.
    totareas = models.IntegerField(null=True, db_column='TotAreas', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'AreaHabRoofWSP'

class Areahabwallcounty(models.Model): 
    countyid = models.IntegerField(null=True, db_column='CountyID', blank=True) # Field name made lowercase.
    countyname = models.CharField(max_length=100, db_column='CountyName') # Field name made lowercase.
    wall = models.CharField(max_length=24, db_column='Wall') # Field name made lowercase.
    nareas = models.IntegerField(null=True, db_column='Nareas', blank=True) # Field name made lowercase.
    pcntareas = models.FloatField(null=True, db_column='PcntAreas', blank=True) # Field name made lowercase.
    totareas = models.IntegerField(null=True, db_column='TotAreas', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'AreaHabWallCounty'

class Areahabwallslum(models.Model): 
    slumid = models.CharField(max_length=100, db_column='SlumID') # Field name made lowercase.
    slumname = models.CharField(max_length=100, db_column='SlumName') # Field name made lowercase.
    wall = models.CharField(max_length=24, db_column='Wall') # Field name made lowercase.
    nareas = models.IntegerField(null=True, db_column='Nareas', blank=True) # Field name made lowercase.
    pcntareas = models.FloatField(null=True, db_column='PcntAreas', blank=True) # Field name made lowercase.
    totareas = models.IntegerField(null=True, db_column='TotAreas', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'AreaHabWallSlum'

class Areahabwalltown(models.Model): 
    townid = models.IntegerField(null=True, db_column='TownID', blank=True) # Field name made lowercase.
    townname = models.CharField(max_length=100, db_column='TownName') # Field name made lowercase.
    wall = models.CharField(max_length=24, db_column='Wall') # Field name made lowercase.
    nareas = models.IntegerField(null=True, db_column='Nareas', blank=True) # Field name made lowercase.
    pcntareas = models.FloatField(null=True, db_column='PcntAreas', blank=True) # Field name made lowercase.
    totareas = models.IntegerField(null=True, db_column='TotAreas', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'AreaHabWallTown'

class Areahabwallwsp(models.Model): 
    wspid = models.CharField(max_length=100, db_column='WspID') # Field name made lowercase.
    wspname = models.CharField(max_length=100, db_column='WspName') # Field name made lowercase.
    wall = models.CharField(max_length=24, db_column='Wall') # Field name made lowercase.
    nareas = models.IntegerField(null=True, db_column='Nareas', blank=True) # Field name made lowercase.
    pcntareas = models.FloatField(null=True, db_column='PcntAreas', blank=True) # Field name made lowercase.
    totareas = models.IntegerField(null=True, db_column='TotAreas', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'AreaHabWallWSP'

class Arealist(models.Model): 
    sublocid = models.IntegerField(null=True, db_column='SublocID', blank=True) # Field name made lowercase.
    areaid = models.FloatField(null=True, db_column='AreaID', blank=True) # Field name made lowercase.
    areaname = models.CharField(max_length=100, db_column='Areaname') # Field name made lowercase.
    townid = models.IntegerField(null=True, db_column='TownID', blank=True) # Field name made lowercase.
    slumid = models.CharField(max_length=100, db_column='Slumid') # Field name made lowercase.
    wsp = models.CharField(max_length=100, db_column='WSP') # Field name made lowercase.
    areatype = models.CharField(max_length=100, db_column='Areatype') # Field name made lowercase.
    numdu = models.CharField(max_length=100, db_column='numDU', blank=True) # Field name made lowercase.
    numplots = models.CharField(max_length=100, db_column='numPlots', blank=True) # Field name made lowercase.
    numflats = models.CharField(max_length=100, db_column='numFlats', blank=True) # Field name made lowercase.
    dusample = models.IntegerField(null=True, db_column='DUsample', blank=True) # Field name made lowercase.
    risk = models.CharField(max_length=100, db_column='Risk') # Field name made lowercase.
    remarks = models.TextField(db_column='Remarks') # Field name made lowercase.
    basedate = models.FloatField(null=True, db_column='BaseDate', blank=True) # Field name made lowercase.
    decode = models.CharField(max_length=100, db_column='DEcode') # Field name made lowercase.
    dedate = models.FloatField(null=True, db_column='DeDate', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'AreaList'

class Arealist2(models.Model): 
    provid = models.IntegerField(null=True, db_column='ProvId', blank=True) # Field name made lowercase.
    provname = models.CharField(max_length=100)
    distid = models.IntegerField(null=True, db_column='DistID', blank=True) # Field name made lowercase.
    distname = models.CharField(max_length=100, db_column='DistName') # Field name made lowercase.
    divid = models.IntegerField(null=True, db_column='DivID', blank=True) # Field name made lowercase.
    divname = models.CharField(max_length=100, db_column='DivName') # Field name made lowercase.
    locid = models.IntegerField(null=True, db_column='locID', blank=True) # Field name made lowercase.
    locname = models.CharField(max_length=100)
    sublocid = models.IntegerField(null=True, db_column='sublocID', blank=True) # Field name made lowercase.
    sublocname = models.CharField(max_length=100)
    areaid = models.FloatField(null=True, db_column='AreaID', blank=True) # Field name made lowercase.
    areaname = models.CharField(max_length=100, db_column='Areaname') # Field name made lowercase.
    townid = models.IntegerField(null=True, db_column='townID', blank=True) # Field name made lowercase.
    townname = models.CharField(max_length=100)
    wspid = models.CharField(max_length=100, db_column='WSPID') # Field name made lowercase.
    wspname = models.CharField(max_length=100, db_column='WSPName') # Field name made lowercase.
    wsbid = models.IntegerField(null=True, db_column='WSBID', blank=True) # Field name made lowercase.
    wsbname = models.CharField(max_length=100, db_column='WSBName') # Field name made lowercase.
    countyid = models.IntegerField(null=True, db_column='Countyid', blank=True) # Field name made lowercase.
    countyname = models.CharField(max_length=100, db_column='CountyName') # Field name made lowercase.
    numdu = models.CharField(max_length=100, db_column='numDU', blank=True) # Field name made lowercase.
    slumid = models.CharField(max_length=100, db_column='Slumid', blank=True) # Field name made lowercase.
    slumname = models.CharField(max_length=100, db_column='SlumName', blank=True) # Field name made lowercase.
    totscore = models.IntegerField(null=True, db_column='TotScore', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'AreaList2'

class Areanospckskcounty(models.Model): 
    countyid = models.IntegerField(null=True, db_column='CountyID', blank=True) # Field name made lowercase.
    countyname = models.CharField(max_length=100, db_column='CountyName') # Field name made lowercase.
    spckiosk = models.CharField(max_length=100, db_column='SpcKiosk') # Field name made lowercase.
    nareas = models.IntegerField(null=True, db_column='Nareas', blank=True) # Field name made lowercase.
    pcntareas = models.FloatField(null=True, db_column='PcntAreas', blank=True) # Field name made lowercase.
    totareas = models.IntegerField(null=True, db_column='TotAreas', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'AreaNoSpcKskCounty'

class Areanospckskslum(models.Model): 
    slumid = models.CharField(max_length=100, db_column='SlumID') # Field name made lowercase.
    slumname = models.CharField(max_length=100, db_column='SlumName') # Field name made lowercase.
    spckiosk = models.CharField(max_length=100, db_column='SpcKiosk') # Field name made lowercase.
    nareas = models.IntegerField(null=True, db_column='Nareas', blank=True) # Field name made lowercase.
    pcntareas = models.CharField(max_length=100, db_column='PcntAreas') # Field name made lowercase.
    totareas = models.CharField(max_length=100, db_column='TotAreas') # Field name made lowercase.
    class Meta:
        db_table = 'AreaNoSpcKskSlum'

class Areanospcksktown(models.Model): 
    townid = models.IntegerField(null=True, db_column='TownID', blank=True) # Field name made lowercase.
    townname = models.CharField(max_length=100, db_column='TownName') # Field name made lowercase.
    spckiosk = models.CharField(max_length=100, db_column='SpcKiosk') # Field name made lowercase.
    nareas = models.IntegerField(null=True, db_column='Nareas', blank=True) # Field name made lowercase.
    pcntareas = models.FloatField(null=True, db_column='PcntAreas', blank=True) # Field name made lowercase.
    totareas = models.IntegerField(null=True, db_column='TotAreas', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'AreaNoSpcKskTown'

class Areanospckskwsp(models.Model): 
    wspid = models.CharField(max_length=100, db_column='WspID') # Field name made lowercase.
    wspname = models.CharField(max_length=100, db_column='WspName') # Field name made lowercase.
    spckiosk = models.CharField(max_length=100, db_column='SpcKiosk') # Field name made lowercase.
    nareas = models.IntegerField(null=True, db_column='Nareas', blank=True) # Field name made lowercase.
    pcntareas = models.FloatField(null=True, db_column='PcntAreas', blank=True) # Field name made lowercase.
    totareas = models.IntegerField(null=True, db_column='TotAreas', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'AreaNoSpcKskWSP'

class Areanospcpubsancounty(models.Model): 
    countyid = models.IntegerField(null=True, db_column='CountyID', blank=True) # Field name made lowercase.
    countyname = models.CharField(max_length=100, db_column='CountyName') # Field name made lowercase.
    spcpubsan = models.CharField(max_length=100, db_column='SpcPubSan') # Field name made lowercase.
    nareas = models.IntegerField(null=True, db_column='Nareas', blank=True) # Field name made lowercase.
    pcntareas = models.FloatField(null=True, db_column='PcntAreas', blank=True) # Field name made lowercase.
    totareas = models.IntegerField(null=True, db_column='TotAreas', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'AreaNoSpcPubSanCounty'

class Areanospcpubsanslum(models.Model): 
    slumid = models.CharField(max_length=100, db_column='SlumID') # Field name made lowercase.
    slumname = models.CharField(max_length=100, db_column='SlumName') # Field name made lowercase.
    spcpubsan = models.CharField(max_length=100, db_column='SpcPubSan') # Field name made lowercase.
    nareas = models.IntegerField(null=True, db_column='Nareas', blank=True) # Field name made lowercase.
    pcntareas = models.CharField(max_length=100, db_column='PcntAreas') # Field name made lowercase.
    totareas = models.CharField(max_length=100, db_column='TotAreas') # Field name made lowercase.
    class Meta:
        db_table = 'AreaNoSpcPubSanSlum'

class Areanospcpubsantown(models.Model): 
    townid = models.IntegerField(null=True, db_column='TownID', blank=True) # Field name made lowercase.
    townname = models.CharField(max_length=100, db_column='TownName') # Field name made lowercase.
    spcpubsan = models.CharField(max_length=100, db_column='SpcPubSan') # Field name made lowercase.
    nareas = models.IntegerField(null=True, db_column='Nareas', blank=True) # Field name made lowercase.
    pcntareas = models.FloatField(null=True, db_column='PcntAreas', blank=True) # Field name made lowercase.
    totareas = models.IntegerField(null=True, db_column='TotAreas', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'AreaNoSpcPubSanTown'

class Areanospcpubsanwsp(models.Model): 
    wspid = models.CharField(max_length=100, db_column='WspID') # Field name made lowercase.
    wspname = models.CharField(max_length=100, db_column='WspName') # Field name made lowercase.
    spcpubsan = models.CharField(max_length=100, db_column='SpcPubSan') # Field name made lowercase.
    nareas = models.IntegerField(null=True, db_column='Nareas', blank=True) # Field name made lowercase.
    pcntareas = models.FloatField(null=True, db_column='PcntAreas', blank=True) # Field name made lowercase.
    totareas = models.IntegerField(null=True, db_column='TotAreas', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'AreaNoSpcPubSanWSP'

class Areaownducounty(models.Model): 
    countyid = models.IntegerField(null=True, db_column='CountyID', blank=True) # Field name made lowercase.
    countyname = models.CharField(max_length=100, db_column='CountyName') # Field name made lowercase.
    owndu = models.CharField(max_length=100, db_column='OwnDU') # Field name made lowercase.
    dusinsmp = models.IntegerField(null=True, db_column='DUsInSmp', blank=True) # Field name made lowercase.
    smpdus = models.IntegerField(null=True, db_column='SmpDUs', blank=True) # Field name made lowercase.
    pcntdus = models.FloatField(null=True, db_column='pcntDUs', blank=True) # Field name made lowercase.
    dusinarea = models.IntegerField(null=True, db_column='DusInArea', blank=True) # Field name made lowercase.
    totdus = models.IntegerField(null=True, db_column='TotDUs', blank=True) # Field name made lowercase.
    totalppleinarea = models.IntegerField(null=True, db_column='TotalPpleinArea', blank=True) # Field name made lowercase.
    pcntpop = models.FloatField(null=True, db_column='PcntPop', blank=True) # Field name made lowercase.
    pop = models.IntegerField(null=True, db_column='Pop', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'AreaOwnDUCounty'

class Areaownduslum(models.Model): 
    slumid = models.IntegerField(null=True, db_column='SlumID', blank=True) # Field name made lowercase.
    slumname = models.CharField(max_length=100, db_column='SlumName') # Field name made lowercase.
    owndu = models.CharField(max_length=100, db_column='OwnDU') # Field name made lowercase.
    dusinsmp = models.IntegerField(null=True, db_column='DUsInSmp', blank=True) # Field name made lowercase.
    smpdus = models.IntegerField(null=True, db_column='SmpDUs', blank=True) # Field name made lowercase.
    pcntdus = models.FloatField(null=True, db_column='pcntDUs', blank=True) # Field name made lowercase.
    dusinarea = models.IntegerField(null=True, db_column='DusInArea', blank=True) # Field name made lowercase.
    totdus = models.IntegerField(null=True, db_column='TotDUs', blank=True) # Field name made lowercase.
    totalppleinarea = models.IntegerField(null=True, db_column='TotalPpleinArea', blank=True) # Field name made lowercase.
    pcntpop = models.FloatField(null=True, db_column='PcntPop', blank=True) # Field name made lowercase.
    pop = models.IntegerField(null=True, db_column='Pop', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'AreaOwnDUSlum'

class Areaowndutown(models.Model): 
    townid = models.IntegerField(null=True, db_column='TownID', blank=True) # Field name made lowercase.
    townname = models.CharField(max_length=100, db_column='TownName') # Field name made lowercase.
    owndu = models.CharField(max_length=100, db_column='OwnDU') # Field name made lowercase.
    dusinsmp = models.IntegerField(null=True, db_column='DUsInSmp', blank=True) # Field name made lowercase.
    smpdus = models.IntegerField(null=True, db_column='SmpDUs', blank=True) # Field name made lowercase.
    pcntdus = models.FloatField(null=True, db_column='pcntDUs', blank=True) # Field name made lowercase.
    dusinarea = models.IntegerField(null=True, db_column='DusInArea', blank=True) # Field name made lowercase.
    totdus = models.IntegerField(null=True, db_column='TotDUs', blank=True) # Field name made lowercase.
    totalppleinarea = models.IntegerField(null=True, db_column='TotalPpleinArea', blank=True) # Field name made lowercase.
    pcntpop = models.FloatField(null=True, db_column='PcntPop', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'AreaOwnDUTown'

class Areaownduwsp(models.Model): 
    wspid = models.CharField(max_length=100, db_column='WSPID') # Field name made lowercase.
    wspname = models.CharField(max_length=100, db_column='WSPName') # Field name made lowercase.
    owndu = models.CharField(max_length=100, db_column='OwnDU') # Field name made lowercase.
    dusinsmp = models.IntegerField(null=True, db_column='DUsInSmp', blank=True) # Field name made lowercase.
    smpdus = models.IntegerField(null=True, db_column='SmpDUs', blank=True) # Field name made lowercase.
    pcntdus = models.FloatField(null=True, db_column='pcntDUs', blank=True) # Field name made lowercase.
    dusinarea = models.IntegerField(null=True, db_column='DusInArea', blank=True) # Field name made lowercase.
    totdus = models.IntegerField(null=True, db_column='TotDUs', blank=True) # Field name made lowercase.
    totalppleinarea = models.IntegerField(null=True, db_column='TotalPpleinArea', blank=True) # Field name made lowercase.
    pcntpop = models.FloatField(null=True, db_column='PcntPop', blank=True) # Field name made lowercase.
    pop = models.IntegerField(null=True, db_column='Pop', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'AreaOwnDUWSP'

class Areaphychar(models.Model): 
    areaname = models.CharField(max_length=100, db_column='Areaname') # Field name made lowercase.
    areaid = models.FloatField(null=True, db_column='AreaID', blank=True) # Field name made lowercase.
    townname = models.CharField(max_length=100)
    adist = models.FloatField(null=True, db_column='ADist', blank=True) # Field name made lowercase.
    areatype = models.CharField(max_length=100, db_column='AreaType') # Field name made lowercase.
    settlement = models.CharField(max_length=100, db_column='Settlement') # Field name made lowercase.
    legalised = models.CharField(max_length=100, db_column='Legalised') # Field name made lowercase.
    yrlegalised = models.CharField(max_length=100, db_column='YrLegalised') # Field name made lowercase.
    watertabledry = models.CharField(max_length=29, db_column='WaterTableDry') # Field name made lowercase.
    watertablerainy = models.CharField(max_length=29, db_column='WaterTableRainy') # Field name made lowercase.
    flooding = models.CharField(max_length=100, db_column='Flooding') # Field name made lowercase.
    soil = models.CharField(max_length=100, db_column='Soil') # Field name made lowercase.
    soilselfsupporting = models.CharField(max_length=100, db_column='SoilSelfSupporting') # Field name made lowercase.
    arealocation = models.CharField(max_length=100, db_column='AreaLocation') # Field name made lowercase.
    areatopology = models.CharField(max_length=100, db_column='AreaTopology', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'AreaPhyChar'

class Areapop(models.Model): 
    area = models.FloatField(null=True, db_column='Area', blank=True) # Field name made lowercase.
    areaname = models.CharField(max_length=100, db_column='Areaname') # Field name made lowercase.
    basedate = models.FloatField(null=True, db_column='BaseDate', blank=True) # Field name made lowercase.
    areasmppop = models.IntegerField(null=True, db_column='AreaSmpPop', blank=True) # Field name made lowercase.
    areasmpdus = models.IntegerField(null=True, db_column='AreaSmpDUs', blank=True) # Field name made lowercase.
    tothhs = models.IntegerField(null=True, db_column='TotHHs', blank=True) # Field name made lowercase.
    avgdusz = models.FloatField(null=True, db_column='AvgDUSz', blank=True) # Field name made lowercase.
    maxdusz = models.IntegerField(null=True, db_column='MaxDUSz', blank=True) # Field name made lowercase.
    mindusz = models.IntegerField(null=True, db_column='MinDUSz', blank=True) # Field name made lowercase.
    avghhsz = models.FloatField(null=True, db_column='AvgHHSz', blank=True) # Field name made lowercase.
    avghhsdu = models.IntegerField(null=True, db_column='AvgHHsDU', blank=True) # Field name made lowercase.
    smpfhhh = models.IntegerField(null=True, db_column='SmpFHHH', blank=True) # Field name made lowercase.
    pcntfhhh = models.FloatField(null=True, db_column='PcntFHHH', blank=True) # Field name made lowercase.
    avgfhhh = models.IntegerField(null=True, db_column='AvgFHHH', blank=True) # Field name made lowercase.
    numdu = models.IntegerField(null=True, db_column='NumDU', blank=True) # Field name made lowercase.
    popunit = models.CharField(max_length=100, db_column='PopUnit') # Field name made lowercase.
    areapop = models.IntegerField(null=True, db_column='AreaPop', blank=True) # Field name made lowercase.
    sublocpop = models.IntegerField(null=True, db_column='SubLocPop', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'AreaPop'

class Areapopdensity(models.Model): 
    area = models.FloatField(null=True, db_column='Area', blank=True) # Field name made lowercase.
    areaname = models.CharField(max_length=100, db_column='Areaname') # Field name made lowercase.
    basedate = models.FloatField(null=True, db_column='BaseDate', blank=True) # Field name made lowercase.
    areapop = models.IntegerField(null=True, db_column='AreaPop', blank=True) # Field name made lowercase.
    sqkm = models.CharField(max_length=100, db_column='SqKm', blank=True) # Field name made lowercase.
    popdensity = models.CharField(max_length=100, db_column='PopDensity', blank=True) # Field name made lowercase.
    popden = models.CharField(max_length=100, db_column='PopDen') # Field name made lowercase.
    class Meta:
        db_table = 'AreaPopDensity'

class Areaprofiles(models.Model): 
    areaname = models.CharField(max_length=100, db_column='Areaname') # Field name made lowercase.
    areaid = models.FloatField(null=True, db_column='AreaID', blank=True) # Field name made lowercase.
    townname = models.CharField(max_length=100)
    alocation = models.TextField(db_column='ALocation') # Field name made lowercase.
    alayout = models.TextField(db_column='ALayout') # Field name made lowercase.
    aurbandev = models.TextField(db_column='AUrbanDev') # Field name made lowercase.
    awater = models.TextField(db_column='AWater') # Field name made lowercase.
    asanitation = models.TextField(db_column='Asanitation') # Field name made lowercase.
    asolidwaste = models.TextField(db_column='Asolidwaste') # Field name made lowercase.
    apbhealthrisks = models.TextField(db_column='ApbHealthRisks') # Field name made lowercase.
    amainproblems = models.TextField(db_column='AmainProblems') # Field name made lowercase.
    class Meta:
        db_table = 'AreaProfiles'

class Areasubjfldcounty(models.Model): 
    countyid = models.IntegerField(null=True, db_column='CountyID', blank=True) # Field name made lowercase.
    countyname = models.CharField(max_length=100, db_column='CountyName') # Field name made lowercase.
    flooding = models.CharField(max_length=100, db_column='Flooding') # Field name made lowercase.
    nareas = models.IntegerField(null=True, db_column='Nareas', blank=True) # Field name made lowercase.
    numareas = models.IntegerField(null=True, db_column='NumAreas', blank=True) # Field name made lowercase.
    pcntareas = models.FloatField(null=True, db_column='PcntAreas', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'AreaSubjFldCounty'

class Areasubjfldslum(models.Model): 
    slumid = models.IntegerField(null=True, db_column='SlumID', blank=True) # Field name made lowercase.
    slumname = models.CharField(max_length=100, db_column='SlumName') # Field name made lowercase.
    flooding = models.CharField(max_length=100, db_column='Flooding') # Field name made lowercase.
    nareas = models.IntegerField(null=True, db_column='Nareas', blank=True) # Field name made lowercase.
    numareas = models.IntegerField(null=True, db_column='NumAreas', blank=True) # Field name made lowercase.
    pcntareas = models.FloatField(null=True, db_column='PcntAreas', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'AreaSubjFldSlum'

class Areasubjfldtown(models.Model): 
    townid = models.IntegerField(null=True, db_column='TownID', blank=True) # Field name made lowercase.
    townname = models.CharField(max_length=100, db_column='TownName') # Field name made lowercase.
    flooding = models.CharField(max_length=100, db_column='Flooding') # Field name made lowercase.
    nareas = models.IntegerField(null=True, db_column='Nareas', blank=True) # Field name made lowercase.
    numareas = models.IntegerField(null=True, db_column='NumAreas', blank=True) # Field name made lowercase.
    pcntareas = models.FloatField(null=True, db_column='PcntAreas', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'AreaSubjFldTown'

class Areasubjfldwsp(models.Model): 
    wspid = models.CharField(max_length=100, db_column='WspID') # Field name made lowercase.
    wspname = models.CharField(max_length=100, db_column='WspName') # Field name made lowercase.
    flooding = models.CharField(max_length=100, db_column='Flooding') # Field name made lowercase.
    nareas = models.IntegerField(null=True, db_column='Nareas', blank=True) # Field name made lowercase.
    numareas = models.IntegerField(null=True, db_column='NumAreas', blank=True) # Field name made lowercase.
    pcntareas = models.FloatField(null=True, db_column='PcntAreas', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'AreaSubjFldWSP'

class Areasummarysheet(models.Model): 
    areaid = models.FloatField(null=True, db_column='AreaID', blank=True) # Field name made lowercase.
    areaname = models.CharField(max_length=100, db_column='Areaname') # Field name made lowercase.
    sublocname = models.CharField(max_length=100)
    wspname = models.CharField(max_length=100, db_column='WSPName') # Field name made lowercase.
    areatype = models.CharField(max_length=100, db_column='AreaType') # Field name made lowercase.
    areapop = models.IntegerField(null=True, db_column='AreaPop', blank=True) # Field name made lowercase.
    sqkm = models.FloatField(null=True, db_column='SqKm', blank=True) # Field name made lowercase.
    popdensity = models.IntegerField(null=True, db_column='PopDensity', blank=True) # Field name made lowercase.
    arealinkedwater = models.CharField(max_length=100, db_column='AreaLinkedWater') # Field name made lowercase.
    communityschm = models.TextField(db_column='CommunitySchm') # Field name made lowercase.
    wsupplyproj = models.TextField(db_column='WsupplyProj') # Field name made lowercase.
    pcntppleusingimpsrcwstf = models.FloatField(null=True, db_column='PcntPpleUsingImpSrcWSTF', blank=True) # Field name made lowercase.
    nadeqsupplied = models.IntegerField(null=True, db_column='NAdeqSupplied', blank=True) # Field name made lowercase.
    pcntpplereseller = models.FloatField(null=True, db_column='PcntPPleReseller', blank=True) # Field name made lowercase.
    pcntppleothcon = models.FloatField(null=True, db_column='PcntPpleOthCon', blank=True) # Field name made lowercase.
    arealinkedsew = models.CharField(max_length=100, db_column='AreaLinkedSew') # Field name made lowercase.
    pcntppleimpsan = models.FloatField(null=True, db_column='PcntPpleImpSan', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'AreaSummarySheet'

class Areassettlocrdrlcounty(models.Model): 
    countyid = models.IntegerField(null=True, db_column='Countyid', blank=True) # Field name made lowercase.
    countyname = models.CharField(max_length=100, db_column='CountyName') # Field name made lowercase.
    arealocation = models.CharField(max_length=35, db_column='Arealocation') # Field name made lowercase.
    nareas = models.IntegerField(null=True, db_column='Nareas', blank=True) # Field name made lowercase.
    pcntareas = models.FloatField(null=True, db_column='PcntAreas', blank=True) # Field name made lowercase.
    numareas = models.IntegerField(null=True, db_column='NumAreas', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'AreasSettLocRdRlCounty'

class Areassettlocrdrlslum(models.Model): 
    slumid = models.IntegerField(null=True, db_column='Slumid', blank=True) # Field name made lowercase.
    slumname = models.CharField(max_length=100, db_column='SlumName') # Field name made lowercase.
    arealocation = models.CharField(max_length=35, db_column='Arealocation') # Field name made lowercase.
    nareas = models.IntegerField(null=True, db_column='Nareas', blank=True) # Field name made lowercase.
    pcntareas = models.FloatField(null=True, db_column='PcntAreas', blank=True) # Field name made lowercase.
    numareas = models.IntegerField(null=True, db_column='NumAreas', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'AreasSettLocRdRlSlum'

class Areassettlocrdrltown(models.Model): 
    townid = models.IntegerField(null=True, db_column='Townid', blank=True) # Field name made lowercase.
    townname = models.CharField(max_length=100, db_column='TownName') # Field name made lowercase.
    arealocation = models.CharField(max_length=35, db_column='Arealocation') # Field name made lowercase.
    nareas = models.IntegerField(null=True, db_column='Nareas', blank=True) # Field name made lowercase.
    pcntareas = models.FloatField(null=True, db_column='PcntAreas', blank=True) # Field name made lowercase.
    numareas = models.IntegerField(null=True, db_column='NumAreas', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'AreasSettLocRdRlTown'

class Areassettlocrdrlwsp(models.Model): 
    wspid = models.CharField(max_length=100, db_column='WSPid') # Field name made lowercase.
    wspname = models.CharField(max_length=100, db_column='WSPName') # Field name made lowercase.
    arealocation = models.CharField(max_length=35, db_column='Arealocation') # Field name made lowercase.
    nareas = models.IntegerField(null=True, db_column='Nareas', blank=True) # Field name made lowercase.
    pcntareas = models.FloatField(null=True, db_column='PcntAreas', blank=True) # Field name made lowercase.
    numareas = models.IntegerField(null=True, db_column='NumAreas', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'AreasSettLocRdRlWSP'

class Demogtrends(models.Model): 
    areaid = models.FloatField(null=True, db_column='AreaID', blank=True) # Field name made lowercase.
    popdensity = models.TextField(db_column='PopDensity') # Field name made lowercase.
    demogtrend = models.TextField(db_column='Demogtrend') # Field name made lowercase.
    factors = models.TextField(db_column='Factors') # Field name made lowercase.
    popgrwth = models.TextField(db_column='PopGrwth') # Field name made lowercase.
    demogdev = models.TextField(db_column='DemogDev') # Field name made lowercase.
    daypop = models.TextField(db_column='DayPop') # Field name made lowercase.
    class Meta:
        db_table = 'DemogTrends'

class Devplans(models.Model): 
    areaid = models.FloatField(null=True, db_column='AreaID', blank=True) # Field name made lowercase.
    devplan = models.TextField(db_column='DevPlan') # Field name made lowercase.
    laplan = models.TextField(db_column='LAPlan') # Field name made lowercase.
    devactivities = models.TextField(db_column='DevActivities') # Field name made lowercase.
    class Meta:
        db_table = 'DevPlans'

class Femhhhscounty(models.Model): 
    countyid = models.IntegerField(null=True, db_column='CountyID', blank=True) # Field name made lowercase.
    countyname = models.CharField(max_length=100, db_column='CountyName') # Field name made lowercase.
    areasmppop = models.IntegerField(null=True, db_column='AreaSmpPop', blank=True) # Field name made lowercase.
    areasmpdus = models.IntegerField(null=True, db_column='AreaSmpDUs', blank=True) # Field name made lowercase.
    tothhs = models.IntegerField(null=True, db_column='TotHHs', blank=True) # Field name made lowercase.
    avgdusz = models.FloatField(null=True, db_column='AvgDUSz', blank=True) # Field name made lowercase.
    maxdusz = models.IntegerField(null=True, db_column='MaxDUSz', blank=True) # Field name made lowercase.
    mindusz = models.IntegerField(null=True, db_column='MinDUSz', blank=True) # Field name made lowercase.
    avghhsz = models.FloatField(null=True, db_column='AvgHHSz', blank=True) # Field name made lowercase.
    avghhsdu = models.IntegerField(null=True, db_column='AvgHHsDU', blank=True) # Field name made lowercase.
    smpfhhh = models.IntegerField(null=True, db_column='SmpFHHH', blank=True) # Field name made lowercase.
    pcntfhhh = models.FloatField(null=True, db_column='PcntFHHH', blank=True) # Field name made lowercase.
    avgfhhh = models.IntegerField(null=True, db_column='AvgFHHH', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'FemHHHsCounty'

class Femhhhsslum(models.Model): 
    slumid = models.CharField(max_length=100, db_column='SlumID') # Field name made lowercase.
    slumname = models.CharField(max_length=100, db_column='SlumName') # Field name made lowercase.
    areasmppop = models.IntegerField(null=True, db_column='AreaSmpPop', blank=True) # Field name made lowercase.
    areasmpdus = models.IntegerField(null=True, db_column='AreaSmpDUs', blank=True) # Field name made lowercase.
    tothhs = models.IntegerField(null=True, db_column='TotHHs', blank=True) # Field name made lowercase.
    avgdusz = models.FloatField(null=True, db_column='AvgDUSz', blank=True) # Field name made lowercase.
    maxdusz = models.IntegerField(null=True, db_column='MaxDUSz', blank=True) # Field name made lowercase.
    mindusz = models.IntegerField(null=True, db_column='MinDUSz', blank=True) # Field name made lowercase.
    avghhsz = models.FloatField(null=True, db_column='AvgHHSz', blank=True) # Field name made lowercase.
    avghhsdu = models.IntegerField(null=True, db_column='AvgHHsDU', blank=True) # Field name made lowercase.
    smpfhhh = models.IntegerField(null=True, db_column='SmpFHHH', blank=True) # Field name made lowercase.
    pcntfhhh = models.FloatField(null=True, db_column='PcntFHHH', blank=True) # Field name made lowercase.
    avgfhhh = models.IntegerField(null=True, db_column='AvgFHHH', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'FemHHHsSlum'

class Femhhhstown(models.Model): 
    townid = models.IntegerField(null=True, db_column='TownID', blank=True) # Field name made lowercase.
    townname = models.CharField(max_length=100, db_column='TownName') # Field name made lowercase.
    areasmppop = models.IntegerField(null=True, db_column='AreaSmpPop', blank=True) # Field name made lowercase.
    areasmpdus = models.IntegerField(null=True, db_column='AreaSmpDUs', blank=True) # Field name made lowercase.
    tothhs = models.IntegerField(null=True, db_column='TotHHs', blank=True) # Field name made lowercase.
    avgdusz = models.FloatField(null=True, db_column='AvgDUSz', blank=True) # Field name made lowercase.
    maxdusz = models.IntegerField(null=True, db_column='MaxDUSz', blank=True) # Field name made lowercase.
    mindusz = models.IntegerField(null=True, db_column='MinDUSz', blank=True) # Field name made lowercase.
    avghhsz = models.FloatField(null=True, db_column='AvgHHSz', blank=True) # Field name made lowercase.
    avghhsdu = models.IntegerField(null=True, db_column='AvgHHsDU', blank=True) # Field name made lowercase.
    smpfhhh = models.IntegerField(null=True, db_column='SmpFHHH', blank=True) # Field name made lowercase.
    pcntfhhh = models.FloatField(null=True, db_column='PcntFHHH', blank=True) # Field name made lowercase.
    avgfhhh = models.IntegerField(null=True, db_column='AvgFHHH', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'FemHHHsTown'

class Femhhhswsp(models.Model): 
    wspid = models.CharField(max_length=20, db_column='WspID', blank=True) # Field name made lowercase.
    wspname = models.CharField(max_length=100, db_column='WspName', blank=True) # Field name made lowercase.
    areasmppop = models.IntegerField(null=True, db_column='AreaSmpPop', blank=True) # Field name made lowercase.
    areasmpdus = models.IntegerField(null=True, db_column='AreaSmpDUs', blank=True) # Field name made lowercase.
    tothhs = models.IntegerField(null=True, db_column='TotHHs', blank=True) # Field name made lowercase.
    avgdusz = models.FloatField(null=True, db_column='AvgDUSz', blank=True) # Field name made lowercase.
    maxdusz = models.IntegerField(null=True, db_column='MaxDUSz', blank=True) # Field name made lowercase.
    mindusz = models.IntegerField(null=True, db_column='MinDUSz', blank=True) # Field name made lowercase.
    avghhsz = models.FloatField(null=True, db_column='AvgHHSz', blank=True) # Field name made lowercase.
    avghhsdu = models.IntegerField(null=True, db_column='AvgHHsDU', blank=True) # Field name made lowercase.
    smpfhhh = models.IntegerField(null=True, db_column='SmpFHHH', blank=True) # Field name made lowercase.
    pcntfhhh = models.FloatField(null=True, db_column='PcntFHHH', blank=True) # Field name made lowercase.
    avgfhhh = models.IntegerField(null=True, db_column='AvgFHHH', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'FemHHHsWSP'

class Habitationpatterns(models.Model): 
    areaid = models.FloatField(null=True, db_column='AreaID', blank=True) # Field name made lowercase.
    areaname = models.CharField(max_length=100, db_column='Areaname') # Field name made lowercase.
    hsetype = models.CharField(max_length=100, db_column='HseType') # Field name made lowercase.
    hsgsituation = models.TextField(db_column='HsgSituation') # Field name made lowercase.
    hsngchar = models.TextField(db_column='HsngChar') # Field name made lowercase.
    hseroof = models.TextField(db_column='HseRoof') # Field name made lowercase.
    hsewall = models.TextField(db_column='HseWall') # Field name made lowercase.
    class Meta:
        db_table = 'HabitationPatterns'

class Landownuse(models.Model): 
    areaid = models.FloatField(null=True, db_column='AreaID', blank=True) # Field name made lowercase.
    landownership = models.CharField(max_length=100, db_column='LandOwnership') # Field name made lowercase.
    rdrsrv = models.CharField(max_length=100, db_column='RdRsrv') # Field name made lowercase.
    pubspace = models.CharField(max_length=100, db_column='PubSpace') # Field name made lowercase.
    spcwaterext = models.CharField(max_length=100, db_column='SpcWaterExt') # Field name made lowercase.
    spckiosk = models.CharField(max_length=100, db_column='SpcKiosk') # Field name made lowercase.
    spcpubsan = models.CharField(max_length=100, db_column='SpcPubSan') # Field name made lowercase.
    spcprvsan = models.CharField(max_length=100, db_column='SpcPrvSan') # Field name made lowercase.
    landuse = models.CharField(max_length=100, db_column='Landuse') # Field name made lowercase.
    class Meta:
        db_table = 'LandOwnUse'

class Majidatainfocounty(models.Model): 
    countyid = models.IntegerField(null=True, db_column='countyID', blank=True) # Field name made lowercase.
    countyname = models.CharField(max_length=100)
    nareas = models.IntegerField(null=True, db_column='NAreas', blank=True) # Field name made lowercase.
    ndus = models.IntegerField(null=True, db_column='NDUs', blank=True) # Field name made lowercase.
    smpdus = models.IntegerField(null=True, db_column='SmpDUs', blank=True) # Field name made lowercase.
    pop = models.IntegerField(null=True, db_column='Pop', blank=True) # Field name made lowercase.
    pcntdusinterv = models.FloatField(null=True, db_column='PcntDUsInterv', blank=True) # Field name made lowercase.
    smppop = models.IntegerField(null=True, db_column='SmpPop', blank=True) # Field name made lowercase.
    pcntpopinterviewed = models.FloatField(null=True, db_column='PcntPopInterviewed', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'MajidataInfoCounty'

class Majidatainfoslum(models.Model): 
    slumid = models.CharField(max_length=100, db_column='slumID') # Field name made lowercase.
    slumname = models.CharField(max_length=100)
    nareas = models.IntegerField(null=True, db_column='NAreas', blank=True) # Field name made lowercase.
    ndus = models.IntegerField(null=True, db_column='NDUs', blank=True) # Field name made lowercase.
    smpdus = models.IntegerField(null=True, db_column='SmpDUs', blank=True) # Field name made lowercase.
    pop = models.IntegerField(null=True, db_column='Pop', blank=True) # Field name made lowercase.
    pcntdusinterv = models.FloatField(null=True, db_column='PcntDUsInterv', blank=True) # Field name made lowercase.
    smppop = models.IntegerField(null=True, db_column='SmpPop', blank=True) # Field name made lowercase.
    pcntpopinterviewed = models.FloatField(null=True, db_column='PcntPopInterviewed', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'MajidataInfoSlum'

class Majidatainfotwn(models.Model): 
    townid = models.IntegerField(null=True, db_column='townID', blank=True) # Field name made lowercase.
    townname = models.CharField(max_length=100)
    nareas = models.IntegerField(null=True, db_column='NAreas', blank=True) # Field name made lowercase.
    ndus = models.IntegerField(null=True, db_column='NDUs', blank=True) # Field name made lowercase.
    smpdus = models.IntegerField(null=True, db_column='SmpDUs', blank=True) # Field name made lowercase.
    pop = models.IntegerField(null=True, db_column='Pop', blank=True) # Field name made lowercase.
    pcntdusinterv = models.FloatField(null=True, db_column='PcntDUsInterv', blank=True) # Field name made lowercase.
    smppop = models.IntegerField(null=True, db_column='SmpPop', blank=True) # Field name made lowercase.
    pcntpopinterviewed = models.FloatField(null=True, db_column='PcntPopInterviewed', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'MajidataInfoTwn'

class Majidatainfowsp(models.Model): 
    wspid = models.CharField(max_length=100, db_column='wspID') # Field name made lowercase.
    wspname = models.CharField(max_length=100)
    nareas = models.IntegerField(null=True, db_column='NAreas', blank=True) # Field name made lowercase.
    ndus = models.IntegerField(null=True, db_column='NDUs', blank=True) # Field name made lowercase.
    smpdus = models.IntegerField(null=True, db_column='SmpDUs', blank=True) # Field name made lowercase.
    pop = models.IntegerField(null=True, db_column='Pop', blank=True) # Field name made lowercase.
    pcntdusinterv = models.FloatField(null=True, db_column='PcntDUsInterv', blank=True) # Field name made lowercase.
    smppop = models.IntegerField(null=True, db_column='SmpPop', blank=True) # Field name made lowercase.
    pcntpopinterviewed = models.FloatField(null=True, db_column='PcntPopInterviewed', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'MajidataInfoWSP'

class Pavghhduszcounty(models.Model): 
    countyid = models.IntegerField(null=True, db_column='CountyID', blank=True) # Field name made lowercase.
    countyname = models.CharField(max_length=100, db_column='CountyName') # Field name made lowercase.
    areasmppop = models.IntegerField(null=True, db_column='AreaSmpPop', blank=True) # Field name made lowercase.
    areasmpdus = models.IntegerField(null=True, db_column='AreaSmpDUs', blank=True) # Field name made lowercase.
    avgdusz = models.FloatField(null=True, db_column='AvgDUSz', blank=True) # Field name made lowercase.
    maxdusz = models.IntegerField(null=True, db_column='MaxDUSz', blank=True) # Field name made lowercase.
    mindusz = models.IntegerField(null=True, db_column='MinDUSz', blank=True) # Field name made lowercase.
    tothhs = models.IntegerField(null=True, db_column='TotHHs', blank=True) # Field name made lowercase.
    avghhsz = models.FloatField(null=True, db_column='AvgHHSz', blank=True) # Field name made lowercase.
    avghhsdu = models.IntegerField(null=True, db_column='AvgHHsDU', blank=True) # Field name made lowercase.
    avgfhhh = models.IntegerField(null=True, db_column='AvgFHHH', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'PAvgHHDUSzCounty'

class Pavghhduszslum(models.Model): 
    slumid = models.CharField(max_length=100, db_column='SlumID') # Field name made lowercase.
    slumname = models.CharField(max_length=100, db_column='SlumName') # Field name made lowercase.
    areasmppop = models.IntegerField(null=True, db_column='AreaSmpPop', blank=True) # Field name made lowercase.
    areasmpdus = models.IntegerField(null=True, db_column='AreaSmpDUs', blank=True) # Field name made lowercase.
    avgdusz = models.FloatField(null=True, db_column='AvgDUSz', blank=True) # Field name made lowercase.
    maxdusz = models.IntegerField(null=True, db_column='MaxDUSz', blank=True) # Field name made lowercase.
    mindusz = models.IntegerField(null=True, db_column='MinDUSz', blank=True) # Field name made lowercase.
    tothhs = models.IntegerField(null=True, db_column='TotHHs', blank=True) # Field name made lowercase.
    avghhsz = models.FloatField(null=True, db_column='AvgHHSz', blank=True) # Field name made lowercase.
    avghhsdu = models.IntegerField(null=True, db_column='AvgHHsDU', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'PAvgHHDUSzSlum'

class Pavghhdusztown(models.Model): 
    townid = models.IntegerField(null=True, db_column='TownID', blank=True) # Field name made lowercase.
    townname = models.CharField(max_length=100, db_column='TownName') # Field name made lowercase.
    areasmppop = models.IntegerField(null=True, db_column='AreaSmpPop', blank=True) # Field name made lowercase.
    areasmpdus = models.IntegerField(null=True, db_column='AreaSmpDUs', blank=True) # Field name made lowercase.
    avgdusz = models.FloatField(null=True, db_column='AvgDUSz', blank=True) # Field name made lowercase.
    maxdusz = models.IntegerField(null=True, db_column='MaxDUSz', blank=True) # Field name made lowercase.
    mindusz = models.IntegerField(null=True, db_column='MinDUSz', blank=True) # Field name made lowercase.
    tothhs = models.IntegerField(null=True, db_column='TotHHs', blank=True) # Field name made lowercase.
    avghhsz = models.FloatField(null=True, db_column='AvgHHSz', blank=True) # Field name made lowercase.
    avghhsdu = models.IntegerField(null=True, db_column='AvgHHsDU', blank=True) # Field name made lowercase.
    avgfhhh = models.IntegerField(null=True, db_column='AvgFHHH', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'PAvgHHDUSzTown'

class Pavghhduszwsp(models.Model): 
    wspid = models.CharField(max_length=20, db_column='WSPID', blank=True) # Field name made lowercase.
    wspname = models.CharField(max_length=49, db_column='WSPName', blank=True) # Field name made lowercase.
    areasmppop = models.IntegerField(null=True, db_column='AreaSmpPop', blank=True) # Field name made lowercase.
    areasmpdus = models.IntegerField(null=True, db_column='AreaSmpDUs', blank=True) # Field name made lowercase.
    avgdusz = models.FloatField(null=True, db_column='AvgDUSz', blank=True) # Field name made lowercase.
    maxdusz = models.IntegerField(null=True, db_column='MaxDUSz', blank=True) # Field name made lowercase.
    mindusz = models.IntegerField(null=True, db_column='MinDUSz', blank=True) # Field name made lowercase.
    tothhs = models.IntegerField(null=True, db_column='TotHHs', blank=True) # Field name made lowercase.
    avghhsz = models.FloatField(null=True, db_column='AvgHHSz', blank=True) # Field name made lowercase.
    avghhsdu = models.IntegerField(null=True, db_column='AvgHHsDU', blank=True) # Field name made lowercase.
    avgfhhh = models.IntegerField(null=True, db_column='AvgFHHH', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'PAvgHHDUSzWSP'

class Phlthwasterds(models.Model): 
    areaid = models.FloatField(null=True, db_column='AreaID', blank=True) # Field name made lowercase.
    areaname = models.CharField(max_length=100, db_column='Areaname') # Field name made lowercase.
    phsit = models.CharField(max_length=100, db_column='PHSit') # Field name made lowercase.
    mnphproblem = models.TextField(db_column='MnPHProblem') # Field name made lowercase.
    swsit = models.TextField(db_column='SWSit') # Field name made lowercase.
    mnswdisp = models.TextField(db_column='MnSWDisp') # Field name made lowercase.
    roadtypes = models.TextField(db_column='RoadTypes') # Field name made lowercase.
    rdtechstatus = models.TextField(db_column='RdTechStatus') # Field name made lowercase.
    draintypes = models.TextField(db_column='DrainTypes') # Field name made lowercase.
    drnstatus = models.TextField(db_column='DrnStatus') # Field name made lowercase.
    class Meta:
        db_table = 'PHlthWasteRds'

class Pownduwsrckskcounty(models.Model): 
    countyid = models.IntegerField(null=True, db_column='CountyID', blank=True) # Field name made lowercase.
    countyname = models.CharField(max_length=100, db_column='CountyName') # Field name made lowercase.
    owndu = models.CharField(max_length=100, db_column='OwnDU') # Field name made lowercase.
    dusinsmp = models.IntegerField(null=True, db_column='DUsInSmp', blank=True) # Field name made lowercase.
    smpdus = models.IntegerField(null=True, db_column='SmpDUs', blank=True) # Field name made lowercase.
    pcntdus = models.FloatField(null=True, db_column='pcntDUs', blank=True) # Field name made lowercase.
    dusinarea = models.IntegerField(null=True, db_column='DusInArea', blank=True) # Field name made lowercase.
    totdus = models.IntegerField(null=True, db_column='TotDUs', blank=True) # Field name made lowercase.
    totalppleinarea = models.IntegerField(null=True, db_column='TotalPpleinArea', blank=True) # Field name made lowercase.
    pcntpop = models.FloatField(null=True, db_column='PcntPop', blank=True) # Field name made lowercase.
    pop = models.IntegerField(null=True, db_column='Pop', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'POwnDUWSrcKskCounty'

class Pownduwsrckskslum(models.Model): 
    slumid = models.IntegerField(null=True, db_column='SlumID', blank=True) # Field name made lowercase.
    slumname = models.CharField(max_length=100, db_column='SlumName') # Field name made lowercase.
    owndu = models.CharField(max_length=100, db_column='OwnDU') # Field name made lowercase.
    dusinsmp = models.IntegerField(null=True, db_column='DUsInSmp', blank=True) # Field name made lowercase.
    smpdus = models.IntegerField(null=True, db_column='SmpDUs', blank=True) # Field name made lowercase.
    pcntdus = models.FloatField(null=True, db_column='pcntDUs', blank=True) # Field name made lowercase.
    dusinarea = models.IntegerField(null=True, db_column='DusInArea', blank=True) # Field name made lowercase.
    totdus = models.IntegerField(null=True, db_column='TotDUs', blank=True) # Field name made lowercase.
    totalppleinarea = models.IntegerField(null=True, db_column='TotalPpleinArea', blank=True) # Field name made lowercase.
    pcntpop = models.FloatField(null=True, db_column='PcntPop', blank=True) # Field name made lowercase.
    pop = models.IntegerField(null=True, db_column='Pop', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'POwnDUWSrcKskSlum'

class Pownduwsrcksktown(models.Model): 
    townid = models.IntegerField(null=True, db_column='TownID', blank=True) # Field name made lowercase.
    townname = models.CharField(max_length=100, db_column='TownName') # Field name made lowercase.
    owndu = models.CharField(max_length=100, db_column='OwnDU') # Field name made lowercase.
    dusinsmp = models.IntegerField(null=True, db_column='DUsInSmp', blank=True) # Field name made lowercase.
    smpdus = models.IntegerField(null=True, db_column='SmpDUs', blank=True) # Field name made lowercase.
    pcntdus = models.FloatField(null=True, db_column='pcntDUs', blank=True) # Field name made lowercase.
    dusinarea = models.IntegerField(null=True, db_column='DusInArea', blank=True) # Field name made lowercase.
    totdus = models.IntegerField(null=True, db_column='TotDUs', blank=True) # Field name made lowercase.
    totalppleinarea = models.IntegerField(null=True, db_column='TotalPpleinArea', blank=True) # Field name made lowercase.
    pcntpop = models.FloatField(null=True, db_column='PcntPop', blank=True) # Field name made lowercase.
    pop = models.IntegerField(null=True, db_column='Pop', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'POwnDUWSrcKskTown'

class Pownduwsrckskwsp(models.Model): 
    wspid = models.CharField(max_length=100, db_column='WspID') # Field name made lowercase.
    wspname = models.CharField(max_length=100, db_column='WspName') # Field name made lowercase.
    owndu = models.CharField(max_length=100, db_column='OwnDU') # Field name made lowercase.
    dusinsmp = models.IntegerField(null=True, db_column='DUsInSmp', blank=True) # Field name made lowercase.
    smpdus = models.IntegerField(null=True, db_column='SmpDUs', blank=True) # Field name made lowercase.
    pcntdus = models.FloatField(null=True, db_column='pcntDUs', blank=True) # Field name made lowercase.
    dusinarea = models.IntegerField(null=True, db_column='DusInArea', blank=True) # Field name made lowercase.
    totdus = models.IntegerField(null=True, db_column='TotDUs', blank=True) # Field name made lowercase.
    totalppleinarea = models.IntegerField(null=True, db_column='TotalPpleinArea', blank=True) # Field name made lowercase.
    pcntpop = models.FloatField(null=True, db_column='PcntPop', blank=True) # Field name made lowercase.
    pop = models.IntegerField(null=True, db_column='Pop', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'POwnDUWSrcKskWSP'

class Pownduwsrcpipedcounty(models.Model): 
    countyid = models.IntegerField(null=True, db_column='CountyID', blank=True) # Field name made lowercase.
    countyname = models.CharField(max_length=100, db_column='CountyName') # Field name made lowercase.
    owndu = models.CharField(max_length=100, db_column='OwnDU') # Field name made lowercase.
    dusinsmp = models.IntegerField(null=True, db_column='DUsInSmp', blank=True) # Field name made lowercase.
    smpdus = models.IntegerField(null=True, db_column='SmpDUs', blank=True) # Field name made lowercase.
    pcntdus = models.FloatField(null=True, db_column='pcntDUs', blank=True) # Field name made lowercase.
    dusinarea = models.IntegerField(null=True, db_column='DusInArea', blank=True) # Field name made lowercase.
    totdus = models.IntegerField(null=True, db_column='TotDUs', blank=True) # Field name made lowercase.
    totalppleinarea = models.IntegerField(null=True, db_column='TotalPpleinArea', blank=True) # Field name made lowercase.
    pcntpop = models.FloatField(null=True, db_column='PcntPop', blank=True) # Field name made lowercase.
    pop = models.IntegerField(null=True, db_column='Pop', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'POwnDUWSrcPipedCounty'

class Pownduwsrcpipedslum(models.Model): 
    slumid = models.IntegerField(null=True, db_column='SlumID', blank=True) # Field name made lowercase.
    slumname = models.CharField(max_length=100, db_column='SlumName') # Field name made lowercase.
    owndu = models.CharField(max_length=100, db_column='OwnDU') # Field name made lowercase.
    dusinsmp = models.IntegerField(null=True, db_column='DUsInSmp', blank=True) # Field name made lowercase.
    smpdus = models.IntegerField(null=True, db_column='SmpDUs', blank=True) # Field name made lowercase.
    pcntdus = models.FloatField(null=True, db_column='pcntDUs', blank=True) # Field name made lowercase.
    dusinarea = models.IntegerField(null=True, db_column='DusInArea', blank=True) # Field name made lowercase.
    totdus = models.IntegerField(null=True, db_column='TotDUs', blank=True) # Field name made lowercase.
    totalppleinarea = models.IntegerField(null=True, db_column='TotalPpleinArea', blank=True) # Field name made lowercase.
    pcntpop = models.FloatField(null=True, db_column='PcntPop', blank=True) # Field name made lowercase.
    pop = models.IntegerField(null=True, db_column='Pop', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'POwnDUWSrcPipedSlum'

class Pownduwsrcpipedtown(models.Model): 
    townid = models.IntegerField(null=True, db_column='TownID', blank=True) # Field name made lowercase.
    townname = models.CharField(max_length=100, db_column='TownName') # Field name made lowercase.
    owndu = models.CharField(max_length=100, db_column='OwnDU') # Field name made lowercase.
    dusinsmp = models.IntegerField(null=True, db_column='DUsInSmp', blank=True) # Field name made lowercase.
    smpdus = models.IntegerField(null=True, db_column='SmpDUs', blank=True) # Field name made lowercase.
    pcntdus = models.FloatField(null=True, db_column='pcntDUs', blank=True) # Field name made lowercase.
    dusinarea = models.IntegerField(null=True, db_column='DusInArea', blank=True) # Field name made lowercase.
    totdus = models.IntegerField(null=True, db_column='TotDUs', blank=True) # Field name made lowercase.
    totalppleinarea = models.IntegerField(null=True, db_column='TotalPpleinArea', blank=True) # Field name made lowercase.
    pcntpop = models.FloatField(null=True, db_column='PcntPop', blank=True) # Field name made lowercase.
    pop = models.IntegerField(null=True, db_column='Pop', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'POwnDUWSrcPipedTown'

class Pownduwsrcpipedwsp(models.Model): 
    wspid = models.CharField(max_length=100, db_column='wspID') # Field name made lowercase.
    wspname = models.CharField(max_length=100, db_column='wspName') # Field name made lowercase.
    owndu = models.CharField(max_length=100, db_column='OwnDU') # Field name made lowercase.
    dusinsmp = models.IntegerField(null=True, db_column='DUsInSmp', blank=True) # Field name made lowercase.
    smpdus = models.IntegerField(null=True, db_column='SmpDUs', blank=True) # Field name made lowercase.
    pcntdus = models.FloatField(null=True, db_column='pcntDUs', blank=True) # Field name made lowercase.
    dusinarea = models.IntegerField(null=True, db_column='DusInArea', blank=True) # Field name made lowercase.
    totdus = models.IntegerField(null=True, db_column='TotDUs', blank=True) # Field name made lowercase.
    totalppleinarea = models.IntegerField(null=True, db_column='TotalPpleinArea', blank=True) # Field name made lowercase.
    pcntpop = models.FloatField(null=True, db_column='PcntPop', blank=True) # Field name made lowercase.
    pop = models.IntegerField(null=True, db_column='Pop', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'POwnDUWSrcPipedWSP'

class Preligioncounty(models.Model): 
    countyid = models.IntegerField(null=True, db_column='CountyID', blank=True) # Field name made lowercase.
    countyname = models.CharField(max_length=100, db_column='CountyName') # Field name made lowercase.
    religion = models.CharField(max_length=100, db_column='Religion') # Field name made lowercase.
    ndus = models.IntegerField(null=True, db_column='NDus', blank=True) # Field name made lowercase.
    pcntdus = models.FloatField(null=True, db_column='PcntDUs', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'PReligionCounty'

class Preligionslum(models.Model): 
    slumid = models.IntegerField(null=True, db_column='SlumID', blank=True) # Field name made lowercase.
    slumname = models.CharField(max_length=100, db_column='SlumName') # Field name made lowercase.
    religion = models.CharField(max_length=100, db_column='Religion') # Field name made lowercase.
    ndus = models.IntegerField(null=True, db_column='NDus', blank=True) # Field name made lowercase.
    pcntdus = models.FloatField(null=True, db_column='PcntDUs', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'PReligionSlum'

class Preligiontown(models.Model): 
    townid = models.IntegerField(null=True, db_column='TownID', blank=True) # Field name made lowercase.
    townname = models.CharField(max_length=100, db_column='TownName') # Field name made lowercase.
    religion = models.CharField(max_length=100, db_column='Religion') # Field name made lowercase.
    ndus = models.IntegerField(null=True, db_column='NDus', blank=True) # Field name made lowercase.
    pcntdus = models.FloatField(null=True, db_column='PcntDUs', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'PReligionTown'

class Preligionwsp(models.Model): 
    wspid = models.CharField(max_length=100, db_column='wspID') # Field name made lowercase.
    wspname = models.CharField(max_length=100, db_column='wspName') # Field name made lowercase.
    religion = models.CharField(max_length=100, db_column='Religion') # Field name made lowercase.
    ndus = models.IntegerField(null=True, db_column='NDus', blank=True) # Field name made lowercase.
    pcntdus = models.FloatField(null=True, db_column='PcntDUs', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'PReligionWSP'

class Popareabysettlementcounty(models.Model): 
    countyid = models.IntegerField(null=True, db_column='Countyid', blank=True) # Field name made lowercase.
    countyname = models.CharField(max_length=100, db_column='CountyName') # Field name made lowercase.
    settlement = models.CharField(max_length=100, db_column='Settlement') # Field name made lowercase.
    nareas = models.IntegerField(null=True, db_column='NAreas', blank=True) # Field name made lowercase.
    totareas = models.IntegerField(null=True, db_column='TotAreas', blank=True) # Field name made lowercase.
    pcntareas = models.FloatField(null=True, db_column='PcntAreas', blank=True) # Field name made lowercase.
    pop = models.IntegerField(null=True, db_column='Pop', blank=True) # Field name made lowercase.
    totpop = models.IntegerField(null=True, db_column='TotPop', blank=True) # Field name made lowercase.
    pcntpop = models.FloatField(null=True, db_column='PcntPop', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'PopAreaBySettlementCounty'

class Popareabysettlementslum(models.Model): 
    slumid = models.IntegerField(null=True, db_column='Slumid', blank=True) # Field name made lowercase.
    slumname = models.CharField(max_length=100, db_column='SlumName') # Field name made lowercase.
    settlement = models.CharField(max_length=100, db_column='Settlement') # Field name made lowercase.
    nareas = models.IntegerField(null=True, db_column='NAreas', blank=True) # Field name made lowercase.
    totareas = models.IntegerField(null=True, db_column='TotAreas', blank=True) # Field name made lowercase.
    pcntareas = models.FloatField(null=True, db_column='PcntAreas', blank=True) # Field name made lowercase.
    pop = models.IntegerField(null=True, db_column='Pop', blank=True) # Field name made lowercase.
    totpop = models.IntegerField(null=True, db_column='TotPop', blank=True) # Field name made lowercase.
    pcntpop = models.FloatField(null=True, db_column='PcntPop', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'PopAreaBySettlementSlum'

class Popareabysettlementtown(models.Model): 
    townid = models.IntegerField(null=True, db_column='Townid', blank=True) # Field name made lowercase.
    townname = models.CharField(max_length=100, db_column='TownName') # Field name made lowercase.
    settlement = models.CharField(max_length=100, db_column='Settlement') # Field name made lowercase.
    nareas = models.IntegerField(null=True, db_column='NAreas', blank=True) # Field name made lowercase.
    totareas = models.IntegerField(null=True, db_column='TotAreas', blank=True) # Field name made lowercase.
    pcntareas = models.FloatField(null=True, db_column='PcntAreas', blank=True) # Field name made lowercase.
    pop = models.IntegerField(null=True, db_column='Pop', blank=True) # Field name made lowercase.
    totpop = models.IntegerField(null=True, db_column='TotPop', blank=True) # Field name made lowercase.
    pcntpop = models.FloatField(null=True, db_column='PcntPop', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'PopAreaBySettlementTown'

class Popareabysettlementwsp(models.Model): 
    wspid = models.CharField(max_length=20, db_column='Wspid', blank=True) # Field name made lowercase.
    wspname = models.CharField(max_length=100, db_column='WspName', blank=True) # Field name made lowercase.
    settlement = models.CharField(max_length=50, db_column='Settlement', blank=True) # Field name made lowercase.
    nareas = models.IntegerField(null=True, db_column='NAreas', blank=True) # Field name made lowercase.
    totareas = models.IntegerField(null=True, db_column='TotAreas', blank=True) # Field name made lowercase.
    pcntareas = models.FloatField(null=True, db_column='PcntAreas', blank=True) # Field name made lowercase.
    pop = models.IntegerField(null=True, db_column='Pop', blank=True) # Field name made lowercase.
    totpop = models.IntegerField(null=True, db_column='TotPop', blank=True) # Field name made lowercase.
    pcntpop = models.FloatField(null=True, db_column='PcntPop', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'PopAreaBySettlementWSP'

class Popareatypecounty(models.Model): 
    countyid = models.IntegerField(null=True, db_column='CountyID', blank=True) # Field name made lowercase.
    countyname = models.CharField(max_length=100, db_column='CountyName') # Field name made lowercase.
    areatype = models.CharField(max_length=100, db_column='AreaType') # Field name made lowercase.
    pop = models.IntegerField(null=True, db_column='Pop', blank=True) # Field name made lowercase.
    nareas = models.IntegerField(null=True, db_column='Nareas', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'PopAreaTypeCounty'

class Popareatypeslum(models.Model): 
    slumid = models.CharField(max_length=100, db_column='SlumID') # Field name made lowercase.
    slumname = models.CharField(max_length=100, db_column='SlumName') # Field name made lowercase.
    areatype = models.CharField(max_length=100, db_column='AreaType') # Field name made lowercase.
    pop = models.IntegerField(null=True, db_column='Pop', blank=True) # Field name made lowercase.
    nareas = models.IntegerField(null=True, db_column='Nareas', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'PopAreaTypeSlum'

class Popareatypetown(models.Model): 
    townid = models.IntegerField(null=True, db_column='TownID', blank=True) # Field name made lowercase.
    townname = models.CharField(max_length=100, db_column='TownName') # Field name made lowercase.
    areatype = models.CharField(max_length=100, db_column='AreaType') # Field name made lowercase.
    pop = models.IntegerField(null=True, db_column='Pop', blank=True) # Field name made lowercase.
    nareas = models.IntegerField(null=True, db_column='Nareas', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'PopAreaTypeTown'

class Popareatypewsp(models.Model): 
    wspid = models.CharField(max_length=100, db_column='WspID') # Field name made lowercase.
    wspname = models.CharField(max_length=100, db_column='WspName') # Field name made lowercase.
    areatype = models.CharField(max_length=100, db_column='AreaType') # Field name made lowercase.
    pop = models.IntegerField(null=True, db_column='Pop', blank=True) # Field name made lowercase.
    nareas = models.IntegerField(null=True, db_column='Nareas', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'PopAreaTypeWSP'

class Popareasbylegalcounty(models.Model): 
    countyid = models.IntegerField(null=True, db_column='Countyid', blank=True) # Field name made lowercase.
    countyname = models.CharField(max_length=100, db_column='CountyName') # Field name made lowercase.
    legalstatus = models.CharField(max_length=100, db_column='LegalStatus') # Field name made lowercase.
    nareas = models.IntegerField(null=True, db_column='NAreas', blank=True) # Field name made lowercase.
    pop = models.IntegerField(null=True, db_column='Pop', blank=True) # Field name made lowercase.
    avgpopperarea = models.IntegerField(null=True, db_column='AvgPopPerArea', blank=True) # Field name made lowercase.
    totareas = models.IntegerField(null=True, db_column='TotAreas', blank=True) # Field name made lowercase.
    pcntareas = models.FloatField(null=True, db_column='PcntAreas', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'PopAreasByLegalCounty'

class Popareasbylegalslum(models.Model): 
    slumid = models.IntegerField(null=True, db_column='Slumid', blank=True) # Field name made lowercase.
    slumname = models.CharField(max_length=100, db_column='SlumName') # Field name made lowercase.
    legalstatus = models.CharField(max_length=100, db_column='LegalStatus') # Field name made lowercase.
    nareas = models.IntegerField(null=True, db_column='NAreas', blank=True) # Field name made lowercase.
    pop = models.IntegerField(null=True, db_column='Pop', blank=True) # Field name made lowercase.
    avgpopperarea = models.IntegerField(null=True, db_column='AvgPopPerArea', blank=True) # Field name made lowercase.
    totareas = models.IntegerField(null=True, db_column='TotAreas', blank=True) # Field name made lowercase.
    pcntareas = models.FloatField(null=True, db_column='PcntAreas', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'PopAreasByLegalSlum'

class Popareasbylegaltown(models.Model): 
    townid = models.IntegerField(null=True, db_column='Townid', blank=True) # Field name made lowercase.
    townname = models.CharField(max_length=100, db_column='TownName') # Field name made lowercase.
    legalstatus = models.CharField(max_length=100, db_column='LegalStatus') # Field name made lowercase.
    nareas = models.IntegerField(null=True, db_column='NAreas', blank=True) # Field name made lowercase.
    pop = models.IntegerField(null=True, db_column='Pop', blank=True) # Field name made lowercase.
    avgpopperarea = models.IntegerField(null=True, db_column='AvgPopPerArea', blank=True) # Field name made lowercase.
    totareas = models.IntegerField(null=True, db_column='TotAreas', blank=True) # Field name made lowercase.
    pcntareas = models.FloatField(null=True, db_column='PcntAreas', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'PopAreasByLegalTown'

class Popareasbylegalwsp(models.Model): 
    wspid = models.CharField(max_length=20, db_column='Wspid', blank=True) # Field name made lowercase.
    wspname = models.CharField(max_length=100, db_column='WspName', blank=True) # Field name made lowercase.
    legalstatus = models.CharField(max_length=20, db_column='LegalStatus', blank=True) # Field name made lowercase.
    nareas = models.IntegerField(null=True, db_column='NAreas', blank=True) # Field name made lowercase.
    pop = models.IntegerField(null=True, db_column='Pop', blank=True) # Field name made lowercase.
    avgpopperarea = models.IntegerField(null=True, db_column='AvgPopPerArea', blank=True) # Field name made lowercase.
    totareas = models.IntegerField(null=True, db_column='TotAreas', blank=True) # Field name made lowercase.
    pcntareas = models.FloatField(null=True, db_column='PcntAreas', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'PopAreasByLegalWSP'

class Savgdush44County(models.Model): 
    countyid = models.IntegerField(null=True, db_column='CountyID', blank=True) # Field name made lowercase.
    countyname = models.CharField(max_length=100, db_column='CountyName') # Field name made lowercase.
    dusinsmp = models.IntegerField(null=True, db_column='DUsInSmp', blank=True) # Field name made lowercase.
    dussharing = models.CharField(max_length=100, db_column='DUsSharing') # Field name made lowercase.
    smpdus = models.IntegerField(null=True, db_column='SmpDUs', blank=True) # Field name made lowercase.
    pcntdus = models.FloatField(null=True, db_column='pcntDUs', blank=True) # Field name made lowercase.
    dusinarea = models.IntegerField(null=True, db_column='DusInArea', blank=True) # Field name made lowercase.
    totdus = models.IntegerField(null=True, db_column='TotDUs', blank=True) # Field name made lowercase.
    totalppleinarea = models.IntegerField(null=True, db_column='TotalPpleinArea', blank=True) # Field name made lowercase.
    pcntpop = models.FloatField(null=True, db_column='PcntPop', blank=True) # Field name made lowercase.
    pop = models.IntegerField(null=True, db_column='Pop', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'SAvgDUSh44County'

class Savgdush44Slum(models.Model): 
    slumid = models.IntegerField(null=True, db_column='SlumID', blank=True) # Field name made lowercase.
    slumname = models.CharField(max_length=100, db_column='SlumName') # Field name made lowercase.
    dusinsmp = models.IntegerField(null=True, db_column='DUsInSmp', blank=True) # Field name made lowercase.
    dussharing = models.CharField(max_length=100, db_column='DUsSharing') # Field name made lowercase.
    smpdus = models.IntegerField(null=True, db_column='SmpDUs', blank=True) # Field name made lowercase.
    pcntdus = models.FloatField(null=True, db_column='pcntDUs', blank=True) # Field name made lowercase.
    dusinarea = models.IntegerField(null=True, db_column='DusInArea', blank=True) # Field name made lowercase.
    totdus = models.IntegerField(null=True, db_column='TotDUs', blank=True) # Field name made lowercase.
    totalppleinarea = models.IntegerField(null=True, db_column='TotalPpleinArea', blank=True) # Field name made lowercase.
    pcntpop = models.FloatField(null=True, db_column='PcntPop', blank=True) # Field name made lowercase.
    pop = models.IntegerField(null=True, db_column='Pop', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'SAvgDUSh44Slum'

class Savgdush44Wsp(models.Model): 
    wspid = models.CharField(max_length=100, db_column='WSPID') # Field name made lowercase.
    wspname = models.CharField(max_length=100, db_column='WSPName') # Field name made lowercase.
    dusinsmp = models.IntegerField(null=True, db_column='DUsInSmp', blank=True) # Field name made lowercase.
    dussharing = models.CharField(max_length=100, db_column='DUsSharing') # Field name made lowercase.
    smpdus = models.IntegerField(null=True, db_column='SmpDUs', blank=True) # Field name made lowercase.
    pcntdus = models.FloatField(null=True, db_column='pcntDUs', blank=True) # Field name made lowercase.
    dusinarea = models.IntegerField(null=True, db_column='DusInArea', blank=True) # Field name made lowercase.
    totdus = models.IntegerField(null=True, db_column='TotDUs', blank=True) # Field name made lowercase.
    totalppleinarea = models.IntegerField(null=True, db_column='TotalPpleinArea', blank=True) # Field name made lowercase.
    pcntpop = models.FloatField(null=True, db_column='PcntPop', blank=True) # Field name made lowercase.
    pop = models.IntegerField(null=True, db_column='Pop', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'SAvgDUSh44WSP'

class Savgdusshfaccounty(models.Model): 
    countyid = models.IntegerField(null=True, db_column='CountyID', blank=True) # Field name made lowercase.
    countyname = models.CharField(max_length=100, db_column='CountyName') # Field name made lowercase.
    dusinsmp = models.IntegerField(null=True, db_column='DUsInSmp', blank=True) # Field name made lowercase.
    dussharing = models.CharField(max_length=100, db_column='DUsSharing') # Field name made lowercase.
    smpdus = models.IntegerField(null=True, db_column='SmpDUs', blank=True) # Field name made lowercase.
    pcntdus = models.IntegerField(null=True, db_column='pcntDUs', blank=True) # Field name made lowercase.
    dusinarea = models.IntegerField(null=True, db_column='DusInArea', blank=True) # Field name made lowercase.
    totdus = models.IntegerField(null=True, db_column='TotDUs', blank=True) # Field name made lowercase.
    avgdusz = models.FloatField(null=True, db_column='AvgDUSz', blank=True) # Field name made lowercase.
    pop = models.IntegerField(null=True, db_column='Pop', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'SAvgDUsShFacCounty'

class Savgdusshfacslum(models.Model): 
    slumid = models.IntegerField(null=True, db_column='SlumID', blank=True) # Field name made lowercase.
    slumname = models.CharField(max_length=100, db_column='SlumName') # Field name made lowercase.
    dusinsmp = models.IntegerField(null=True, db_column='DUsInSmp', blank=True) # Field name made lowercase.
    dussharing = models.CharField(max_length=100, db_column='DUsSharing') # Field name made lowercase.
    smpdus = models.IntegerField(null=True, db_column='SmpDUs', blank=True) # Field name made lowercase.
    pcntdus = models.IntegerField(null=True, db_column='pcntDUs', blank=True) # Field name made lowercase.
    dusinarea = models.IntegerField(null=True, db_column='DusInArea', blank=True) # Field name made lowercase.
    totdus = models.IntegerField(null=True, db_column='TotDUs', blank=True) # Field name made lowercase.
    avgdusz = models.FloatField(null=True, db_column='AvgDUSz', blank=True) # Field name made lowercase.
    pop = models.IntegerField(null=True, db_column='Pop', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'SAvgDUsShFacSlum'

class Savgdusshfacwsp(models.Model): 
    wspid = models.CharField(max_length=100, db_column='WSPID') # Field name made lowercase.
    wspname = models.CharField(max_length=100, db_column='WSPName') # Field name made lowercase.
    dusinsmp = models.IntegerField(null=True, db_column='DUsInSmp', blank=True) # Field name made lowercase.
    dussharing = models.CharField(max_length=100, db_column='DUsSharing') # Field name made lowercase.
    smpdus = models.IntegerField(null=True, db_column='SmpDUs', blank=True) # Field name made lowercase.
    pcntdus = models.IntegerField(null=True, db_column='pcntDUs', blank=True) # Field name made lowercase.
    dusinarea = models.IntegerField(null=True, db_column='DusInArea', blank=True) # Field name made lowercase.
    totdus = models.IntegerField(null=True, db_column='TotDUs', blank=True) # Field name made lowercase.
    avgdusz = models.FloatField(null=True, db_column='AvgDUSz', blank=True) # Field name made lowercase.
    pop = models.IntegerField(null=True, db_column='Pop', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'SAvgDUsShFacWSP'

class Savghhshowntlt(models.Model): 
    areaid = models.FloatField(null=True, db_column='AreaID', blank=True) # Field name made lowercase.
    areaname = models.CharField(max_length=100, db_column='Areaname') # Field name made lowercase.
    avghhsharing = models.CharField(max_length=100, db_column='AvgHHsharing') # Field name made lowercase.
    maxhhsh = models.CharField(max_length=100, db_column='MaxHHsh') # Field name made lowercase.
    minhhsh = models.CharField(max_length=100, db_column='MinHHsh') # Field name made lowercase.
    areasmpdus = models.IntegerField(null=True, db_column='AreaSmpDUs', blank=True) # Field name made lowercase.
    numdu = models.IntegerField(null=True, db_column='NumDU', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'SAvgHHShOwnTlt'

class Savgtltbath(models.Model): 
    areaid = models.FloatField(null=True, db_column='AreaID', blank=True) # Field name made lowercase.
    areaname = models.CharField(max_length=100, db_column='Areaname') # Field name made lowercase.
    avgnfac = models.IntegerField(null=True, db_column='AvgNFac', blank=True) # Field name made lowercase.
    maxfac = models.IntegerField(null=True, db_column='MaxFac', blank=True) # Field name made lowercase.
    minfac = models.IntegerField(null=True, db_column='MinFac', blank=True) # Field name made lowercase.
    avghhsharing = models.CharField(max_length=100, db_column='AvgHHsharing') # Field name made lowercase.
    maxhhsh = models.CharField(max_length=100, db_column='MaxHHsh') # Field name made lowercase.
    minhhsh = models.CharField(max_length=100, db_column='MinHHsh') # Field name made lowercase.
    avgbaths = models.CharField(max_length=100, db_column='Avgbaths', blank=True) # Field name made lowercase.
    maxbath = models.IntegerField(null=True, db_column='MaxBath', blank=True) # Field name made lowercase.
    minbaths = models.IntegerField(null=True, db_column='MinBaths', blank=True) # Field name made lowercase.
    areasmpdus = models.CharField(max_length=100, db_column='AreaSmpDUs', blank=True) # Field name made lowercase.
    dus = models.CharField(max_length=100, db_column='DUs', blank=True) # Field name made lowercase.
    pcntdus = models.CharField(max_length=100, db_column='pcntDUs', blank=True) # Field name made lowercase.
    ndus = models.CharField(max_length=100, db_column='NDus', blank=True) # Field name made lowercase.
    numdu = models.CharField(max_length=100, db_column='numDU', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'SAvgTltBath'

class Sduhasownbath(models.Model): 
    areaid = models.FloatField(null=True, db_column='AreaID', blank=True) # Field name made lowercase.
    areaname = models.CharField(max_length=100, db_column='Areaname') # Field name made lowercase.
    duownbath = models.CharField(max_length=100, db_column='DuOwnBath') # Field name made lowercase.
    areasmpdus = models.IntegerField(null=True, db_column='AreaSmpDUs', blank=True) # Field name made lowercase.
    dus = models.IntegerField(null=True, db_column='DUs', blank=True) # Field name made lowercase.
    pcntdus = models.FloatField(null=True, db_column='pcntDUs', blank=True) # Field name made lowercase.
    ndus = models.IntegerField(null=True, db_column='NDus', blank=True) # Field name made lowercase.
    numdu = models.IntegerField(null=True, db_column='NumDU', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'SDUHasOwnBath'

class Sduhasownfacility(models.Model): 
    areaid = models.FloatField(null=True, db_column='AreaID', blank=True) # Field name made lowercase.
    areaname = models.CharField(max_length=100, db_column='Areaname') # Field name made lowercase.
    duhasownfac = models.CharField(max_length=100, db_column='DuHasOwnFac') # Field name made lowercase.
    areasmpdus = models.IntegerField(null=True, db_column='AreaSmpDUs', blank=True) # Field name made lowercase.
    dus = models.IntegerField(null=True, db_column='DUs', blank=True) # Field name made lowercase.
    pcntdus = models.FloatField(null=True, db_column='pcntDUs', blank=True) # Field name made lowercase.
    ndus = models.IntegerField(null=True, db_column='NDus', blank=True) # Field name made lowercase.
    numdu = models.IntegerField(null=True, db_column='NumDU', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'SDUHasOwnFacility'

class Sduownbath45County(models.Model): 
    countyid = models.IntegerField(null=True, db_column='CountyID', blank=True) # Field name made lowercase.
    countyname = models.CharField(max_length=100, db_column='CountyName') # Field name made lowercase.
    dusinsmp = models.IntegerField(null=True, db_column='DUsInSmp', blank=True) # Field name made lowercase.
    smpdus = models.IntegerField(null=True, db_column='SmpDUs', blank=True) # Field name made lowercase.
    pcntdus = models.FloatField(null=True, db_column='pcntDUs', blank=True) # Field name made lowercase.
    dusinarea = models.IntegerField(null=True, db_column='DusInArea', blank=True) # Field name made lowercase.
    totdus = models.IntegerField(null=True, db_column='TotDUs', blank=True) # Field name made lowercase.
    pop = models.IntegerField(null=True, db_column='Pop', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'SDUOwnBath45County'

class Sduownbath45Slum(models.Model): 
    slumid = models.IntegerField(null=True, db_column='SlumID', blank=True) # Field name made lowercase.
    slumname = models.CharField(max_length=100, db_column='SlumName') # Field name made lowercase.
    dusinsmp = models.IntegerField(null=True, db_column='DUsInSmp', blank=True) # Field name made lowercase.
    smpdus = models.IntegerField(null=True, db_column='SmpDUs', blank=True) # Field name made lowercase.
    pcntdus = models.FloatField(null=True, db_column='pcntDUs', blank=True) # Field name made lowercase.
    dusinarea = models.IntegerField(null=True, db_column='DusInArea', blank=True) # Field name made lowercase.
    totdus = models.IntegerField(null=True, db_column='TotDUs', blank=True) # Field name made lowercase.
    pop = models.IntegerField(null=True, db_column='Pop', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'SDUOwnBath45Slum'

class Sduownbath45Wsp(models.Model): 
    wspid = models.CharField(max_length=100, db_column='WSPID') # Field name made lowercase.
    wspname = models.CharField(max_length=100, db_column='WSPName') # Field name made lowercase.
    dusinsmp = models.IntegerField(null=True, db_column='DUsInSmp', blank=True) # Field name made lowercase.
    smpdus = models.IntegerField(null=True, db_column='SmpDUs', blank=True) # Field name made lowercase.
    pcntdus = models.FloatField(null=True, db_column='pcntDUs', blank=True) # Field name made lowercase.
    dusinarea = models.IntegerField(null=True, db_column='DusInArea', blank=True) # Field name made lowercase.
    totdus = models.IntegerField(null=True, db_column='TotDUs', blank=True) # Field name made lowercase.
    pop = models.IntegerField(null=True, db_column='Pop', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'SDUOwnBath45WSP'

class Sduownfac45County(models.Model): 
    countyid = models.IntegerField(null=True, db_column='CountyID', blank=True) # Field name made lowercase.
    countyname = models.CharField(max_length=100, db_column='CountyName') # Field name made lowercase.
    dusinsmp = models.IntegerField(null=True, db_column='DUsInSmp', blank=True) # Field name made lowercase.
    smpdus = models.IntegerField(null=True, db_column='SmpDUs', blank=True) # Field name made lowercase.
    pcntdus = models.FloatField(null=True, db_column='pcntDUs', blank=True) # Field name made lowercase.
    dusinarea = models.IntegerField(null=True, db_column='DusInArea', blank=True) # Field name made lowercase.
    totdus = models.IntegerField(null=True, db_column='TotDUs', blank=True) # Field name made lowercase.
    totalppleinarea = models.IntegerField(null=True, db_column='TotalPpleinArea', blank=True) # Field name made lowercase.
    pcntpop = models.FloatField(null=True, db_column='PcntPop', blank=True) # Field name made lowercase.
    pop = models.IntegerField(null=True, db_column='Pop', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'SDUOwnFac45County'

class Sduownfac45Slum(models.Model): 
    slumid = models.IntegerField(null=True, db_column='SlumID', blank=True) # Field name made lowercase.
    slumname = models.CharField(max_length=100, db_column='SlumName') # Field name made lowercase.
    dusinsmp = models.IntegerField(null=True, db_column='DUsInSmp', blank=True) # Field name made lowercase.
    smpdus = models.IntegerField(null=True, db_column='SmpDUs', blank=True) # Field name made lowercase.
    pcntdus = models.FloatField(null=True, db_column='pcntDUs', blank=True) # Field name made lowercase.
    dusinarea = models.IntegerField(null=True, db_column='DusInArea', blank=True) # Field name made lowercase.
    totdus = models.IntegerField(null=True, db_column='TotDUs', blank=True) # Field name made lowercase.
    totalppleinarea = models.IntegerField(null=True, db_column='TotalPpleinArea', blank=True) # Field name made lowercase.
    pcntpop = models.FloatField(null=True, db_column='PcntPop', blank=True) # Field name made lowercase.
    pop = models.IntegerField(null=True, db_column='Pop', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'SDUOwnFac45Slum'

class Sduownfac45Wsp(models.Model): 
    wspid = models.CharField(max_length=100, db_column='WSPID') # Field name made lowercase.
    wspname = models.CharField(max_length=100, db_column='WSPName') # Field name made lowercase.
    dusinsmp = models.IntegerField(null=True, db_column='DUsInSmp', blank=True) # Field name made lowercase.
    smpdus = models.IntegerField(null=True, db_column='SmpDUs', blank=True) # Field name made lowercase.
    pcntdus = models.FloatField(null=True, db_column='pcntDUs', blank=True) # Field name made lowercase.
    dusinarea = models.IntegerField(null=True, db_column='DusInArea', blank=True) # Field name made lowercase.
    totdus = models.IntegerField(null=True, db_column='TotDUs', blank=True) # Field name made lowercase.
    totalppleinarea = models.IntegerField(null=True, db_column='TotalPpleinArea', blank=True) # Field name made lowercase.
    pcntpop = models.FloatField(null=True, db_column='PcntPop', blank=True) # Field name made lowercase.
    pop = models.IntegerField(null=True, db_column='Pop', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'SDUOwnFac45WSP'

class Sduownrpit45County(models.Model): 
    countyid = models.IntegerField(null=True, db_column='CountyID', blank=True) # Field name made lowercase.
    countyname = models.CharField(max_length=100, db_column='CountyName') # Field name made lowercase.
    dusinsmp = models.IntegerField(null=True, db_column='DUsInSmp', blank=True) # Field name made lowercase.
    smpdus = models.IntegerField(null=True, db_column='SmpDUs', blank=True) # Field name made lowercase.
    pcntdus = models.FloatField(null=True, db_column='pcntDUs', blank=True) # Field name made lowercase.
    dusinarea = models.IntegerField(null=True, db_column='DusInArea', blank=True) # Field name made lowercase.
    totdus = models.IntegerField(null=True, db_column='TotDUs', blank=True) # Field name made lowercase.
    pop = models.IntegerField(null=True, db_column='Pop', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'SDUOwnRPit45County'

class Sduownrpit45Slum(models.Model): 
    slumid = models.IntegerField(null=True, db_column='SlumID', blank=True) # Field name made lowercase.
    slumname = models.CharField(max_length=100, db_column='SlumName') # Field name made lowercase.
    dusinsmp = models.IntegerField(null=True, db_column='DUsInSmp', blank=True) # Field name made lowercase.
    smpdus = models.IntegerField(null=True, db_column='SmpDUs', blank=True) # Field name made lowercase.
    pcntdus = models.FloatField(null=True, db_column='pcntDUs', blank=True) # Field name made lowercase.
    dusinarea = models.IntegerField(null=True, db_column='DusInArea', blank=True) # Field name made lowercase.
    totdus = models.IntegerField(null=True, db_column='TotDUs', blank=True) # Field name made lowercase.
    pop = models.IntegerField(null=True, db_column='Pop', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'SDUOwnRPit45Slum'

class Sduownrpit45Wsp(models.Model): 
    wspid = models.CharField(max_length=100, db_column='WSPID') # Field name made lowercase.
    wspname = models.CharField(max_length=100, db_column='WSPName') # Field name made lowercase.
    dusinsmp = models.IntegerField(null=True, db_column='DUsInSmp', blank=True) # Field name made lowercase.
    smpdus = models.IntegerField(null=True, db_column='SmpDUs', blank=True) # Field name made lowercase.
    pcntdus = models.FloatField(null=True, db_column='pcntDUs', blank=True) # Field name made lowercase.
    dusinarea = models.IntegerField(null=True, db_column='DusInArea', blank=True) # Field name made lowercase.
    totdus = models.IntegerField(null=True, db_column='TotDUs', blank=True) # Field name made lowercase.
    pop = models.IntegerField(null=True, db_column='Pop', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'SDUOwnRPit45WSP'

class Sdusharestoilet(models.Model): 
    areaid = models.FloatField(null=True, db_column='AreaID', blank=True) # Field name made lowercase.
    areaname = models.CharField(max_length=100, db_column='Areaname') # Field name made lowercase.
    dusharefac = models.CharField(max_length=100, db_column='DuShareFac') # Field name made lowercase.
    areasmpdus = models.IntegerField(null=True, db_column='AreaSmpDUs', blank=True) # Field name made lowercase.
    dus = models.IntegerField(null=True, db_column='DUs', blank=True) # Field name made lowercase.
    pcntdus = models.FloatField(null=True, db_column='pcntDUs', blank=True) # Field name made lowercase.
    ndus = models.IntegerField(null=True, db_column='NDus', blank=True) # Field name made lowercase.
    numdu = models.IntegerField(null=True, db_column='NumDU', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'SDuSharesToilet'

class Seincomesrcs(models.Model): 
    areaid = models.FloatField(null=True, db_column='AreaID', blank=True) # Field name made lowercase.
    areaname = models.CharField(max_length=100, db_column='Areaname') # Field name made lowercase.
    maleincsrc = models.TextField(db_column='MaleIncSrc') # Field name made lowercase.
    femaleincsrc = models.TextField(db_column='FemaleIncSrc') # Field name made lowercase.
    vandlvl = models.TextField(db_column='VandLvl') # Field name made lowercase.
    class Meta:
        db_table = 'SEIncomeSrcs'

class Sfacinplotcounty(models.Model): 
    countyid = models.IntegerField(null=True, db_column='CountyID', blank=True) # Field name made lowercase.
    countyname = models.CharField(max_length=100, db_column='CountyName') # Field name made lowercase.
    dusinsmp = models.IntegerField(null=True, db_column='DUsInSmp', blank=True) # Field name made lowercase.
    smpdus = models.IntegerField(null=True, db_column='SmpDUs', blank=True) # Field name made lowercase.
    pcntdus = models.FloatField(null=True, db_column='pcntDUs', blank=True) # Field name made lowercase.
    dusinarea = models.IntegerField(null=True, db_column='DusInArea', blank=True) # Field name made lowercase.
    totdus = models.IntegerField(null=True, db_column='TotDUs', blank=True) # Field name made lowercase.
    pop = models.IntegerField(null=True, db_column='Pop', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'SFacInPlotCounty'

class Sfacinplotslum(models.Model): 
    slumid = models.IntegerField(null=True, db_column='SlumID', blank=True) # Field name made lowercase.
    slumname = models.CharField(max_length=100, db_column='SlumName') # Field name made lowercase.
    dusinsmp = models.IntegerField(null=True, db_column='DUsInSmp', blank=True) # Field name made lowercase.
    smpdus = models.IntegerField(null=True, db_column='SmpDUs', blank=True) # Field name made lowercase.
    pcntdus = models.FloatField(null=True, db_column='pcntDUs', blank=True) # Field name made lowercase.
    dusinarea = models.IntegerField(null=True, db_column='DusInArea', blank=True) # Field name made lowercase.
    totdus = models.IntegerField(null=True, db_column='TotDUs', blank=True) # Field name made lowercase.
    pop = models.IntegerField(null=True, db_column='Pop', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'SFacInPlotSlum'

class Sfacinplotwsp(models.Model): 
    wspid = models.CharField(max_length=100, db_column='WspID') # Field name made lowercase.
    wspname = models.CharField(max_length=100, db_column='WspName') # Field name made lowercase.
    dusinsmp = models.IntegerField(null=True, db_column='DUsInSmp', blank=True) # Field name made lowercase.
    smpdus = models.IntegerField(null=True, db_column='SmpDUs', blank=True) # Field name made lowercase.
    pcntdus = models.FloatField(null=True, db_column='pcntDUs', blank=True) # Field name made lowercase.
    dusinarea = models.IntegerField(null=True, db_column='DusInArea', blank=True) # Field name made lowercase.
    totdus = models.IntegerField(null=True, db_column='TotDUs', blank=True) # Field name made lowercase.
    pop = models.IntegerField(null=True, db_column='Pop', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'SFacInPlotWSP'

class Sfacsharedcounty(models.Model): 
    countyid = models.IntegerField(null=True, db_column='CountyID', blank=True) # Field name made lowercase.
    countyname = models.CharField(max_length=100, db_column='CountyName') # Field name made lowercase.
    dusinsmp = models.IntegerField(null=True, db_column='DUsInSmp', blank=True) # Field name made lowercase.
    smpdus = models.IntegerField(null=True, db_column='SmpDUs', blank=True) # Field name made lowercase.
    pcntdus = models.FloatField(null=True, db_column='pcntDUs', blank=True) # Field name made lowercase.
    dusinarea = models.IntegerField(null=True, db_column='DusInArea', blank=True) # Field name made lowercase.
    totdus = models.IntegerField(null=True, db_column='TotDUs', blank=True) # Field name made lowercase.
    totalppleinarea = models.IntegerField(null=True, db_column='TotalPpleinArea', blank=True) # Field name made lowercase.
    pcntpop = models.FloatField(null=True, db_column='PcntPop', blank=True) # Field name made lowercase.
    pop = models.IntegerField(null=True, db_column='Pop', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'SFacSharedCounty'

class Sfacsharedslum(models.Model): 
    slumid = models.IntegerField(null=True, db_column='SlumID', blank=True) # Field name made lowercase.
    slumname = models.CharField(max_length=100, db_column='SlumName') # Field name made lowercase.
    dusinsmp = models.IntegerField(null=True, db_column='DUsInSmp', blank=True) # Field name made lowercase.
    smpdus = models.IntegerField(null=True, db_column='SmpDUs', blank=True) # Field name made lowercase.
    pcntdus = models.FloatField(null=True, db_column='pcntDUs', blank=True) # Field name made lowercase.
    dusinarea = models.IntegerField(null=True, db_column='DusInArea', blank=True) # Field name made lowercase.
    totdus = models.IntegerField(null=True, db_column='TotDUs', blank=True) # Field name made lowercase.
    totalppleinarea = models.IntegerField(null=True, db_column='TotalPpleinArea', blank=True) # Field name made lowercase.
    pcntpop = models.FloatField(null=True, db_column='PcntPop', blank=True) # Field name made lowercase.
    pop = models.IntegerField(null=True, db_column='Pop', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'SFacSharedSlum'

class Sfacsharedwsp(models.Model): 
    wspid = models.CharField(max_length=100, db_column='WSPID') # Field name made lowercase.
    wspname = models.CharField(max_length=100, db_column='WSPName') # Field name made lowercase.
    dusinsmp = models.IntegerField(null=True, db_column='DUsInSmp', blank=True) # Field name made lowercase.
    smpdus = models.IntegerField(null=True, db_column='SmpDUs', blank=True) # Field name made lowercase.
    pcntdus = models.FloatField(null=True, db_column='pcntDUs', blank=True) # Field name made lowercase.
    dusinarea = models.IntegerField(null=True, db_column='DusInArea', blank=True) # Field name made lowercase.
    totdus = models.IntegerField(null=True, db_column='TotDUs', blank=True) # Field name made lowercase.
    totalppleinarea = models.IntegerField(null=True, db_column='TotalPpleinArea', blank=True) # Field name made lowercase.
    pcntpop = models.FloatField(null=True, db_column='PcntPop', blank=True) # Field name made lowercase.
    pop = models.IntegerField(null=True, db_column='Pop', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'SFacSharedWSP'

class Sfactypes(models.Model): 
    areaid = models.FloatField(null=True, db_column='AreaID', blank=True) # Field name made lowercase.
    areaname = models.CharField(max_length=100, db_column='Areaname') # Field name made lowercase.
    factype = models.CharField(max_length=100, db_column='FacType') # Field name made lowercase.
    areasmpdus = models.IntegerField(null=True, db_column='AreaSmpDUs', blank=True) # Field name made lowercase.
    dus = models.IntegerField(null=True, db_column='DUs', blank=True) # Field name made lowercase.
    pcntdus = models.FloatField(null=True, db_column='pcntDUs', blank=True) # Field name made lowercase.
    ndus = models.IntegerField(null=True, db_column='NDus', blank=True) # Field name made lowercase.
    numdu = models.IntegerField(null=True, db_column='NumDU', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'SFacTypes'

class Simpjmp(models.Model): 
    areaid = models.FloatField(null=True, db_column='AreaID', blank=True) # Field name made lowercase.
    areaname = models.CharField(max_length=100, db_column='Areaname') # Field name made lowercase.
    areasmpdus = models.IntegerField(null=True, db_column='AreaSmpDUs', blank=True) # Field name made lowercase.
    dusinsmp = models.IntegerField(null=True, db_column='DUsInSmp', blank=True) # Field name made lowercase.
    pcntdus = models.FloatField(null=True, db_column='pcntDUs', blank=True) # Field name made lowercase.
    dusinarea = models.IntegerField(null=True, db_column='DusInArea', blank=True) # Field name made lowercase.
    smppersons = models.IntegerField(null=True, db_column='SmpPersons', blank=True) # Field name made lowercase.
    totalppleinarea = models.IntegerField(null=True, db_column='TotalPpleinArea', blank=True) # Field name made lowercase.
    pcntpple2 = models.FloatField(null=True, blank=True)
    totaldusinarea = models.IntegerField(null=True, db_column='TotalDUsInArea', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'SImpJMP'

class Simpjmpcounty(models.Model): 
    countyid = models.IntegerField(null=True, db_column='CountyID', blank=True) # Field name made lowercase.
    countyname = models.CharField(max_length=100, db_column='CountyName') # Field name made lowercase.
    dusinsmp = models.IntegerField(null=True, db_column='DUsInSmp', blank=True) # Field name made lowercase.
    smpdus = models.IntegerField(null=True, db_column='SmpDUs', blank=True) # Field name made lowercase.
    pcntdus = models.FloatField(null=True, db_column='pcntDUs', blank=True) # Field name made lowercase.
    dusinarea = models.IntegerField(null=True, db_column='DusInArea', blank=True) # Field name made lowercase.
    totdus = models.IntegerField(null=True, db_column='TotDUs', blank=True) # Field name made lowercase.
    totalppleinarea = models.IntegerField(null=True, db_column='TotalPpleinArea', blank=True) # Field name made lowercase.
    pcntpop = models.FloatField(null=True, db_column='PcntPop', blank=True) # Field name made lowercase.
    pop = models.IntegerField(null=True, db_column='Pop', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'SImpJMPCounty'

class Simpjmpownfac(models.Model): 
    areaid = models.FloatField(null=True, db_column='AreaID', blank=True) # Field name made lowercase.
    areaname = models.CharField(max_length=100, db_column='Areaname') # Field name made lowercase.
    areasmpdus = models.IntegerField(null=True, db_column='AreaSmpDUs', blank=True) # Field name made lowercase.
    dusinsmp = models.IntegerField(null=True, db_column='DUsInSmp', blank=True) # Field name made lowercase.
    pcntdus = models.FloatField(null=True, db_column='pcntDUs', blank=True) # Field name made lowercase.
    dusinarea = models.IntegerField(null=True, db_column='DusInArea', blank=True) # Field name made lowercase.
    smppersons = models.IntegerField(null=True, db_column='SmpPersons', blank=True) # Field name made lowercase.
    totalppleinarea = models.IntegerField(null=True, db_column='TotalPpleinArea', blank=True) # Field name made lowercase.
    pcntpple2 = models.FloatField(null=True, blank=True)
    totaldusinarea = models.IntegerField(null=True, db_column='TotalDUsInArea', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'SImpJMPOwnFac'

class Simpjmpownplotfac(models.Model): 
    areaid = models.FloatField(null=True, db_column='AreaID', blank=True) # Field name made lowercase.
    areaname = models.CharField(max_length=100, db_column='Areaname') # Field name made lowercase.
    areasmpdus = models.IntegerField(null=True, db_column='AreaSmpDUs', blank=True) # Field name made lowercase.
    dusinsmp = models.IntegerField(null=True, db_column='DUsInSmp', blank=True) # Field name made lowercase.
    pcntdus = models.FloatField(null=True, db_column='pcntDUs', blank=True) # Field name made lowercase.
    dusinarea = models.IntegerField(null=True, db_column='DusInArea', blank=True) # Field name made lowercase.
    smppersons = models.IntegerField(null=True, db_column='SmpPersons', blank=True) # Field name made lowercase.
    totalppleinarea = models.IntegerField(null=True, db_column='TotalPpleinArea', blank=True) # Field name made lowercase.
    pcntpple = models.FloatField(null=True, blank=True)
    totaldusinarea = models.IntegerField(null=True, db_column='TotalDUsInArea', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'SImpJMPOwnPlotFac'

class Simpjmpshfac(models.Model): 
    areaid = models.FloatField(null=True, db_column='AreaID', blank=True) # Field name made lowercase.
    areaname = models.CharField(max_length=100, db_column='Areaname') # Field name made lowercase.
    areasmpdus = models.IntegerField(null=True, db_column='AreaSmpDUs', blank=True) # Field name made lowercase.
    dusinsmp = models.IntegerField(null=True, db_column='DUsInSmp', blank=True) # Field name made lowercase.
    pcntdus = models.FloatField(null=True, db_column='pcntDUs', blank=True) # Field name made lowercase.
    dusinarea = models.IntegerField(null=True, db_column='DusInArea', blank=True) # Field name made lowercase.
    smppersons = models.IntegerField(null=True, db_column='SmpPersons', blank=True) # Field name made lowercase.
    totalppleinarea = models.IntegerField(null=True, db_column='TotalPpleinArea', blank=True) # Field name made lowercase.
    pcntpple = models.FloatField(null=True, blank=True)
    totaldusinarea = models.IntegerField(null=True, db_column='TotalDUsInArea', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'SImpJMPShFac'

class Simpjmpsharedcounty(models.Model): 
    countyid = models.IntegerField(null=True, db_column='CountyID', blank=True) # Field name made lowercase.
    countyname = models.CharField(max_length=100, db_column='CountyName') # Field name made lowercase.
    dusinsmp = models.IntegerField(null=True, db_column='DUsInSmp', blank=True) # Field name made lowercase.
    smpdus = models.IntegerField(null=True, db_column='SmpDUs', blank=True) # Field name made lowercase.
    pcntdus = models.FloatField(null=True, db_column='pcntDUs', blank=True) # Field name made lowercase.
    dusinarea = models.IntegerField(null=True, db_column='DusInArea', blank=True) # Field name made lowercase.
    totdus = models.IntegerField(null=True, db_column='TotDUs', blank=True) # Field name made lowercase.
    totalppleinarea = models.IntegerField(null=True, db_column='TotalPpleinArea', blank=True) # Field name made lowercase.
    pcntpop = models.FloatField(null=True, db_column='PcntPop', blank=True) # Field name made lowercase.
    pop = models.IntegerField(null=True, db_column='Pop', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'SImpJMPSharedCounty'

class Simpjmpsharedslum(models.Model): 
    slumid = models.IntegerField(null=True, db_column='SlumID', blank=True) # Field name made lowercase.
    slumname = models.CharField(max_length=100, db_column='SlumName') # Field name made lowercase.
    dusinsmp = models.IntegerField(null=True, db_column='DUsInSmp', blank=True) # Field name made lowercase.
    smpdus = models.IntegerField(null=True, db_column='SmpDUs', blank=True) # Field name made lowercase.
    pcntdus = models.FloatField(null=True, db_column='pcntDUs', blank=True) # Field name made lowercase.
    dusinarea = models.IntegerField(null=True, db_column='DusInArea', blank=True) # Field name made lowercase.
    totdus = models.IntegerField(null=True, db_column='TotDUs', blank=True) # Field name made lowercase.
    totalppleinarea = models.IntegerField(null=True, db_column='TotalPpleinArea', blank=True) # Field name made lowercase.
    pcntpop = models.FloatField(null=True, db_column='PcntPop', blank=True) # Field name made lowercase.
    pop = models.IntegerField(null=True, db_column='Pop', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'SImpJMPSharedSlum'

class Simpjmpsharedwsp(models.Model): 
    wspid = models.CharField(max_length=100, db_column='WSPID') # Field name made lowercase.
    wspname = models.CharField(max_length=100, db_column='WSPName') # Field name made lowercase.
    dusinsmp = models.IntegerField(null=True, db_column='DUsInSmp', blank=True) # Field name made lowercase.
    smpdus = models.IntegerField(null=True, db_column='SmpDUs', blank=True) # Field name made lowercase.
    pcntdus = models.FloatField(null=True, db_column='pcntDUs', blank=True) # Field name made lowercase.
    dusinarea = models.IntegerField(null=True, db_column='DusInArea', blank=True) # Field name made lowercase.
    totdus = models.IntegerField(null=True, db_column='TotDUs', blank=True) # Field name made lowercase.
    totalppleinarea = models.IntegerField(null=True, db_column='TotalPpleinArea', blank=True) # Field name made lowercase.
    pcntpop = models.FloatField(null=True, db_column='PcntPop', blank=True) # Field name made lowercase.
    pop = models.IntegerField(null=True, db_column='Pop', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'SImpJMPSharedWSP'

class Simpjmpslum(models.Model): 
    slumid = models.IntegerField(null=True, db_column='SlumID', blank=True) # Field name made lowercase.
    slumname = models.CharField(max_length=100, db_column='SlumName') # Field name made lowercase.
    dusinsmp = models.IntegerField(null=True, db_column='DUsInSmp', blank=True) # Field name made lowercase.
    smpdus = models.IntegerField(null=True, db_column='SmpDUs', blank=True) # Field name made lowercase.
    pcntdus = models.FloatField(null=True, db_column='pcntDUs', blank=True) # Field name made lowercase.
    dusinarea = models.IntegerField(null=True, db_column='DusInArea', blank=True) # Field name made lowercase.
    totdus = models.IntegerField(null=True, db_column='TotDUs', blank=True) # Field name made lowercase.
    totalppleinarea = models.IntegerField(null=True, db_column='TotalPpleinArea', blank=True) # Field name made lowercase.
    pcntpop = models.FloatField(null=True, db_column='PcntPop', blank=True) # Field name made lowercase.
    pop = models.IntegerField(null=True, db_column='Pop', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'SImpJMPSlum'

class Simpjmpwsp(models.Model): 
    wspid = models.CharField(max_length=100, db_column='WspID') # Field name made lowercase.
    wspname = models.CharField(max_length=100, db_column='WspName') # Field name made lowercase.
    dusinsmp = models.IntegerField(null=True, db_column='DUsInSmp', blank=True) # Field name made lowercase.
    smpdus = models.IntegerField(null=True, db_column='SmpDUs', blank=True) # Field name made lowercase.
    pcntdus = models.FloatField(null=True, db_column='pcntDUs', blank=True) # Field name made lowercase.
    dusinarea = models.IntegerField(null=True, db_column='DusInArea', blank=True) # Field name made lowercase.
    totdus = models.IntegerField(null=True, db_column='TotDUs', blank=True) # Field name made lowercase.
    totalppleinarea = models.IntegerField(null=True, db_column='TotalPpleinArea', blank=True) # Field name made lowercase.
    pcntpop = models.FloatField(null=True, db_column='PcntPop', blank=True) # Field name made lowercase.
    pop = models.IntegerField(null=True, db_column='Pop', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'SImpJMPWSP'

class Snofacused(models.Model): 
    areaid = models.FloatField(null=True, db_column='AreaID', blank=True) # Field name made lowercase.
    areaname = models.CharField(max_length=100, db_column='Areaname') # Field name made lowercase.
    areasmpdus = models.IntegerField(null=True, db_column='AreaSmpDUs', blank=True) # Field name made lowercase.
    dusinsmp = models.IntegerField(null=True, db_column='DUsInSmp', blank=True) # Field name made lowercase.
    pcntdus = models.FloatField(null=True, db_column='pcntDUs', blank=True) # Field name made lowercase.
    dusinarea = models.IntegerField(null=True, db_column='DusInArea', blank=True) # Field name made lowercase.
    smppersons = models.IntegerField(null=True, db_column='SmpPersons', blank=True) # Field name made lowercase.
    totalppleinarea = models.IntegerField(null=True, db_column='TotalPpleinArea', blank=True) # Field name made lowercase.
    pcntpple = models.FloatField(null=True, blank=True)
    totaldusinarea = models.IntegerField(null=True, db_column='TotalDUsInArea', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'SNoFacUsed'

class Snofacusedcounty(models.Model): 
    countyid = models.IntegerField(null=True, db_column='CountyID', blank=True) # Field name made lowercase.
    countyname = models.CharField(max_length=100, db_column='CountyName') # Field name made lowercase.
    dusinsmp = models.IntegerField(null=True, db_column='DUsInSmp', blank=True) # Field name made lowercase.
    smpdus = models.IntegerField(null=True, db_column='SmpDUs', blank=True) # Field name made lowercase.
    pcntdus = models.FloatField(null=True, db_column='pcntDUs', blank=True) # Field name made lowercase.
    dusinarea = models.IntegerField(null=True, db_column='DusInArea', blank=True) # Field name made lowercase.
    totdus = models.IntegerField(null=True, db_column='TotDUs', blank=True) # Field name made lowercase.
    totalppleinarea = models.IntegerField(null=True, db_column='TotalPpleinArea', blank=True) # Field name made lowercase.
    pcntpop = models.FloatField(null=True, db_column='PcntPop', blank=True) # Field name made lowercase.
    pop = models.IntegerField(null=True, db_column='Pop', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'SNoFacUsedCounty'

class Snofacusedslum(models.Model): 
    slumid = models.IntegerField(null=True, db_column='SlumID', blank=True) # Field name made lowercase.
    slumname = models.CharField(max_length=100, db_column='SlumName') # Field name made lowercase.
    dusinsmp = models.IntegerField(null=True, db_column='DUsInSmp', blank=True) # Field name made lowercase.
    smpdus = models.IntegerField(null=True, db_column='SmpDUs', blank=True) # Field name made lowercase.
    pcntdus = models.FloatField(null=True, db_column='pcntDUs', blank=True) # Field name made lowercase.
    dusinarea = models.IntegerField(null=True, db_column='DusInArea', blank=True) # Field name made lowercase.
    totdus = models.IntegerField(null=True, db_column='TotDUs', blank=True) # Field name made lowercase.
    totalppleinarea = models.IntegerField(null=True, db_column='TotalPpleinArea', blank=True) # Field name made lowercase.
    pcntpop = models.FloatField(null=True, db_column='PcntPop', blank=True) # Field name made lowercase.
    pop = models.IntegerField(null=True, db_column='Pop', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'SNoFacUsedSlum'

class Snofacusedwsp(models.Model): 
    wspid = models.CharField(max_length=100, db_column='WSPID') # Field name made lowercase.
    wspname = models.CharField(max_length=100, db_column='WSPName') # Field name made lowercase.
    dusinsmp = models.IntegerField(null=True, db_column='DUsInSmp', blank=True) # Field name made lowercase.
    smpdus = models.IntegerField(null=True, db_column='SmpDUs', blank=True) # Field name made lowercase.
    pcntdus = models.FloatField(null=True, db_column='pcntDUs', blank=True) # Field name made lowercase.
    dusinarea = models.IntegerField(null=True, db_column='DusInArea', blank=True) # Field name made lowercase.
    totdus = models.IntegerField(null=True, db_column='TotDUs', blank=True) # Field name made lowercase.
    totalppleinarea = models.IntegerField(null=True, db_column='TotalPpleinArea', blank=True) # Field name made lowercase.
    pcntpop = models.FloatField(null=True, db_column='PcntPop', blank=True) # Field name made lowercase.
    pop = models.IntegerField(null=True, db_column='Pop', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'SNoFacUsedWSP'

class Snoofbaths(models.Model): 
    areaid = models.FloatField(null=True, db_column='AreaID', blank=True) # Field name made lowercase.
    areaname = models.CharField(max_length=100, db_column='Areaname') # Field name made lowercase.
    nbaths = models.CharField(max_length=100, db_column='NBaths') # Field name made lowercase.
    areasmpdus = models.IntegerField(null=True, db_column='AreaSmpDUs', blank=True) # Field name made lowercase.
    dus = models.IntegerField(null=True, db_column='DUs', blank=True) # Field name made lowercase.
    pcntdus = models.FloatField(null=True, db_column='pcntDUs', blank=True) # Field name made lowercase.
    ndus = models.IntegerField(null=True, db_column='NDus', blank=True) # Field name made lowercase.
    numdu = models.IntegerField(null=True, db_column='NumDU', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'SNoofBaths'

class Snoofdushrngtlt(models.Model): 
    areaid = models.FloatField(null=True, db_column='AreaID', blank=True) # Field name made lowercase.
    areaname = models.CharField(max_length=100, db_column='Areaname') # Field name made lowercase.
    nshhhs = models.CharField(max_length=100, db_column='NshHHs') # Field name made lowercase.
    areasmpdus = models.IntegerField(null=True, db_column='AreaSmpDUs', blank=True) # Field name made lowercase.
    dus = models.IntegerField(null=True, db_column='DUs', blank=True) # Field name made lowercase.
    pcntdus = models.FloatField(null=True, db_column='pcntDUs', blank=True) # Field name made lowercase.
    ndus = models.IntegerField(null=True, db_column='NDus', blank=True) # Field name made lowercase.
    numdu = models.IntegerField(null=True, db_column='NumDU', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'SNoofDUShrngTlt'

class Snooffacilities(models.Model): 
    areaid = models.FloatField(null=True, db_column='AreaID', blank=True) # Field name made lowercase.
    areaname = models.CharField(max_length=100, db_column='Areaname') # Field name made lowercase.
    nfacilities = models.CharField(max_length=100, db_column='Nfacilities') # Field name made lowercase.
    areasmpdus = models.IntegerField(null=True, db_column='AreaSmpDUs', blank=True) # Field name made lowercase.
    dus = models.IntegerField(null=True, db_column='DUs', blank=True) # Field name made lowercase.
    pcntdus = models.FloatField(null=True, db_column='pcntDUs', blank=True) # Field name made lowercase.
    ndus = models.IntegerField(null=True, db_column='NDus', blank=True) # Field name made lowercase.
    numdu = models.IntegerField(null=True, db_column='NumDU', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'SNoofFacilities'

class Sownimpjmpcounty(models.Model): 
    countyid = models.IntegerField(null=True, db_column='CountyID', blank=True) # Field name made lowercase.
    countyname = models.CharField(max_length=100, db_column='CountyName') # Field name made lowercase.
    dusinsmp = models.IntegerField(null=True, db_column='DUsInSmp', blank=True) # Field name made lowercase.
    smpdus = models.IntegerField(null=True, db_column='SmpDUs', blank=True) # Field name made lowercase.
    pcntdus = models.FloatField(null=True, db_column='pcntDUs', blank=True) # Field name made lowercase.
    dusinarea = models.IntegerField(null=True, db_column='DusInArea', blank=True) # Field name made lowercase.
    totdus = models.IntegerField(null=True, db_column='TotDUs', blank=True) # Field name made lowercase.
    totalppleinarea = models.IntegerField(null=True, db_column='TotalPpleinArea', blank=True) # Field name made lowercase.
    pcntpop = models.FloatField(null=True, db_column='PcntPop', blank=True) # Field name made lowercase.
    pop = models.IntegerField(null=True, db_column='Pop', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'SOwnImpJMPCounty'

class Sownimpjmpslum(models.Model): 
    slumid = models.IntegerField(null=True, db_column='SlumID', blank=True) # Field name made lowercase.
    slumname = models.CharField(max_length=100, db_column='SlumName') # Field name made lowercase.
    dusinsmp = models.IntegerField(null=True, db_column='DUsInSmp', blank=True) # Field name made lowercase.
    smpdus = models.IntegerField(null=True, db_column='SmpDUs', blank=True) # Field name made lowercase.
    pcntdus = models.FloatField(null=True, db_column='pcntDUs', blank=True) # Field name made lowercase.
    dusinarea = models.IntegerField(null=True, db_column='DusInArea', blank=True) # Field name made lowercase.
    totdus = models.IntegerField(null=True, db_column='TotDUs', blank=True) # Field name made lowercase.
    totalppleinarea = models.IntegerField(null=True, db_column='TotalPpleinArea', blank=True) # Field name made lowercase.
    pcntpop = models.FloatField(null=True, db_column='PcntPop', blank=True) # Field name made lowercase.
    pop = models.IntegerField(null=True, db_column='Pop', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'SOwnImpJMPSlum'

class Sownimpjmpwsp(models.Model): 
    wspid = models.CharField(max_length=100, db_column='WSPID') # Field name made lowercase.
    wspname = models.CharField(max_length=100, db_column='WSPName') # Field name made lowercase.
    dusinsmp = models.IntegerField(null=True, db_column='DUsInSmp', blank=True) # Field name made lowercase.
    smpdus = models.IntegerField(null=True, db_column='SmpDUs', blank=True) # Field name made lowercase.
    pcntdus = models.FloatField(null=True, db_column='pcntDUs', blank=True) # Field name made lowercase.
    dusinarea = models.IntegerField(null=True, db_column='DusInArea', blank=True) # Field name made lowercase.
    totdus = models.IntegerField(null=True, db_column='TotDUs', blank=True) # Field name made lowercase.
    totalppleinarea = models.IntegerField(null=True, db_column='TotalPpleinArea', blank=True) # Field name made lowercase.
    pcntpop = models.FloatField(null=True, db_column='PcntPop', blank=True) # Field name made lowercase.
    pop = models.IntegerField(null=True, db_column='Pop', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'SOwnImpJMPWSP'

class Spractice(models.Model): 
    areaid = models.FloatField(null=True, db_column='AreaID', blank=True) # Field name made lowercase.
    areaname = models.CharField(max_length=100, db_column='Areaname') # Field name made lowercase.
    factype = models.CharField(max_length=100, db_column='FacType') # Field name made lowercase.
    areasmpdus = models.IntegerField(null=True, db_column='AreaSmpDUs', blank=True) # Field name made lowercase.
    dus = models.IntegerField(null=True, db_column='DUs', blank=True) # Field name made lowercase.
    pcntdus = models.FloatField(null=True, db_column='pcntDUs', blank=True) # Field name made lowercase.
    ndus = models.IntegerField(null=True, db_column='NDus', blank=True) # Field name made lowercase.
    numdu = models.IntegerField(null=True, db_column='NumDU', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'SPractice'

class Ssepbaths(models.Model): 
    areaid = models.FloatField(null=True, db_column='AreaID', blank=True) # Field name made lowercase.
    areaname = models.CharField(max_length=100, db_column='Areaname') # Field name made lowercase.
    nsepbaths = models.CharField(max_length=100, db_column='NSepBaths') # Field name made lowercase.
    areasmpdus = models.IntegerField(null=True, db_column='AreaSmpDUs', blank=True) # Field name made lowercase.
    dus = models.IntegerField(null=True, db_column='DUs', blank=True) # Field name made lowercase.
    pcntdus = models.FloatField(null=True, db_column='pcntDUs', blank=True) # Field name made lowercase.
    ndus = models.IntegerField(null=True, db_column='NDus', blank=True) # Field name made lowercase.
    numdu = models.IntegerField(null=True, db_column='NumDU', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'SSepBaths'

class Sseptoilets(models.Model): 
    areaid = models.FloatField(null=True, db_column='AreaID', blank=True) # Field name made lowercase.
    areaname = models.CharField(max_length=100, db_column='Areaname') # Field name made lowercase.
    separatefac = models.CharField(max_length=100, db_column='SeparateFac') # Field name made lowercase.
    areasmpdus = models.IntegerField(null=True, db_column='AreaSmpDUs', blank=True) # Field name made lowercase.
    dus = models.IntegerField(null=True, db_column='DUs', blank=True) # Field name made lowercase.
    pcntdus = models.FloatField(null=True, db_column='pcntDUs', blank=True) # Field name made lowercase.
    ndus = models.IntegerField(null=True, db_column='NDus', blank=True) # Field name made lowercase.
    numdu = models.IntegerField(null=True, db_column='NumDU', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'SSepToilets'

class Swduhasownrpit(models.Model): 
    areaid = models.FloatField(null=True, db_column='AreaID', blank=True) # Field name made lowercase.
    areaname = models.CharField(max_length=100, db_column='Areaname') # Field name made lowercase.
    duownrpits = models.CharField(max_length=100, db_column='DuownRpits') # Field name made lowercase.
    areasmpdus = models.IntegerField(null=True, db_column='AreaSmpDUs', blank=True) # Field name made lowercase.
    dus = models.IntegerField(null=True, db_column='DUs', blank=True) # Field name made lowercase.
    pcntdus = models.FloatField(null=True, db_column='pcntDUs', blank=True) # Field name made lowercase.
    ndus = models.IntegerField(null=True, db_column='NDus', blank=True) # Field name made lowercase.
    numdu = models.IntegerField(null=True, db_column='NumDU', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'SWDUHasOwnRpit'

class Swnoofrubpits(models.Model): 
    areaid = models.FloatField(null=True, db_column='AreaID', blank=True) # Field name made lowercase.
    areaname = models.CharField(max_length=100, db_column='Areaname') # Field name made lowercase.
    nrubpits = models.CharField(max_length=100, db_column='NRubPits') # Field name made lowercase.
    areasmpdus = models.IntegerField(null=True, db_column='AreaSmpDUs', blank=True) # Field name made lowercase.
    dus = models.IntegerField(null=True, db_column='DUs', blank=True) # Field name made lowercase.
    pcntdus = models.FloatField(null=True, db_column='pcntDUs', blank=True) # Field name made lowercase.
    ndus = models.IntegerField(null=True, db_column='NDus', blank=True) # Field name made lowercase.
    numdu = models.IntegerField(null=True, db_column='NumDU', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'SWNoofRubPits'

class Swrpitshared(models.Model): 
    areaid = models.FloatField(null=True, db_column='AreaID', blank=True) # Field name made lowercase.
    areaname = models.CharField(max_length=100, db_column='Areaname') # Field name made lowercase.
    dusharerpits = models.CharField(max_length=100, db_column='DuShareRpits') # Field name made lowercase.
    areasmpdus = models.IntegerField(null=True, db_column='AreaSmpDUs', blank=True) # Field name made lowercase.
    dus = models.IntegerField(null=True, db_column='DUs', blank=True) # Field name made lowercase.
    pcntdus = models.FloatField(null=True, db_column='pcntDUs', blank=True) # Field name made lowercase.
    ndus = models.IntegerField(null=True, db_column='NDus', blank=True) # Field name made lowercase.
    numdu = models.IntegerField(null=True, db_column='NumDU', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'SWRPitShared'

class Sanfacpractcounty(models.Model): 
    countyid = models.IntegerField(null=True, db_column='CountyID', blank=True) # Field name made lowercase.
    countyname = models.CharField(max_length=100, db_column='CountyName') # Field name made lowercase.
    factype = models.CharField(max_length=100, db_column='FacType') # Field name made lowercase.
    dusinsmp = models.IntegerField(null=True, db_column='DUsInSmp', blank=True) # Field name made lowercase.
    smpdus = models.IntegerField(null=True, db_column='SmpDUs', blank=True) # Field name made lowercase.
    pcntdus = models.FloatField(null=True, db_column='pcntDUs', blank=True) # Field name made lowercase.
    ndus = models.IntegerField(null=True, db_column='NDus', blank=True) # Field name made lowercase.
    totdus = models.IntegerField(null=True, db_column='TotDUs', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'SanFacPractCounty'

class Sanfacpractslum(models.Model): 
    slumid = models.IntegerField(null=True, db_column='SlumID', blank=True) # Field name made lowercase.
    slumname = models.CharField(max_length=100, db_column='SlumName') # Field name made lowercase.
    factype = models.CharField(max_length=100, db_column='FacType') # Field name made lowercase.
    dusinsmp = models.IntegerField(null=True, db_column='DUsInSmp', blank=True) # Field name made lowercase.
    smpdus = models.IntegerField(null=True, db_column='SmpDUs', blank=True) # Field name made lowercase.
    pcntdus = models.FloatField(null=True, db_column='pcntDUs', blank=True) # Field name made lowercase.
    ndus = models.IntegerField(null=True, db_column='NDus', blank=True) # Field name made lowercase.
    totdus = models.IntegerField(null=True, db_column='TotDUs', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'SanFacPractSlum'

class Sanfacpractwsp(models.Model): 
    wspid = models.CharField(max_length=100, db_column='WSPID') # Field name made lowercase.
    wspname = models.CharField(max_length=100, db_column='WSPName') # Field name made lowercase.
    factype = models.CharField(max_length=100, db_column='FacType') # Field name made lowercase.
    dusinsmp = models.IntegerField(null=True, db_column='DUsInSmp', blank=True) # Field name made lowercase.
    smpdus = models.IntegerField(null=True, db_column='SmpDUs', blank=True) # Field name made lowercase.
    pcntdus = models.FloatField(null=True, db_column='pcntDUs', blank=True) # Field name made lowercase.
    ndus = models.IntegerField(null=True, db_column='NDus', blank=True) # Field name made lowercase.
    totdus = models.IntegerField(null=True, db_column='TotDUs', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'SanFacPractWSP'

class Sanitation12B(models.Model): 
    areaid = models.FloatField(null=True, db_column='AreaID', blank=True) # Field name made lowercase.
    areaname = models.CharField(max_length=100, db_column='Areaname') # Field name made lowercase.
    facshared = models.TextField(db_column='FacShared') # Field name made lowercase.
    cmnmaterials = models.TextField(db_column='CmnMaterials') # Field name made lowercase.
    pitscovered = models.TextField(db_column='Pitscovered') # Field name made lowercase.
    usedasstore = models.TextField(db_column='UsedasStore') # Field name made lowercase.
    usedasbath = models.TextField(db_column='UsedasBath') # Field name made lowercase.
    usedfordumping = models.TextField(db_column='UsedforDumping') # Field name made lowercase.
    pitsemptied = models.TextField(db_column='PitsEmptied') # Field name made lowercase.
    howemptied = models.TextField(db_column='HowEmptied') # Field name made lowercase.
    dispmthd = models.TextField(db_column='DispMthd') # Field name made lowercase.
    mnsproblem = models.TextField(db_column='MnSProblem') # Field name made lowercase.
    anysanproj = models.TextField(db_column='AnySanProj') # Field name made lowercase.
    class Meta:
        db_table = 'Sanitation-12b'

class Sanitationpractice(models.Model): 
    areaid = models.FloatField(null=True, db_column='AreaID', blank=True) # Field name made lowercase.
    areaname = models.CharField(max_length=100, db_column='Areaname') # Field name made lowercase.
    factype = models.CharField(max_length=100, db_column='FacType') # Field name made lowercase.
    areasmpdus = models.IntegerField(null=True, db_column='AreaSmpDUs', blank=True) # Field name made lowercase.
    dus = models.IntegerField(null=True, db_column='DUs', blank=True) # Field name made lowercase.
    pcntdus = models.FloatField(null=True, db_column='pcntDUs', blank=True) # Field name made lowercase.
    ndus = models.IntegerField(null=True, db_column='NDus', blank=True) # Field name made lowercase.
    numdu = models.IntegerField(null=True, db_column='NumDU', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'SanitationPractice'

class Sanitationsewlnk(models.Model): 
    areaid = models.FloatField(null=True, db_column='AreaID', blank=True) # Field name made lowercase.
    areaname = models.CharField(max_length=100, db_column='Areaname') # Field name made lowercase.
    townid = models.IntegerField(null=True, db_column='TownID', blank=True) # Field name made lowercase.
    arealinkedsanitation = models.CharField(max_length=100, db_column='AreaLinkedSanitation') # Field name made lowercase.
    techstat = models.CharField(max_length=100, db_column='TechStat') # Field name made lowercase.
    snwdist = models.CharField(max_length=100, db_column='Snwdist') # Field name made lowercase.
    sactivecons = models.CharField(max_length=100, db_column='Sactivecons') # Field name made lowercase.
    nseptic = models.CharField(max_length=100, db_column='NSeptic') # Field name made lowercase.
    ncomtoilet = models.CharField(max_length=100, db_column='Ncomtoilet', blank=True) # Field name made lowercase.
    npubtoilet = models.CharField(max_length=100, db_column='NpubToilet') # Field name made lowercase.
    mainsfacility = models.CharField(max_length=100, db_column='MainSFacility') # Field name made lowercase.
    cmnpriv = models.TextField(db_column='CmnPriv') # Field name made lowercase.
    cmnpublic = models.TextField(db_column='CmnPublic') # Field name made lowercase.
    class Meta:
        db_table = 'SanitationSewLnk'

class Socioeconinfr(models.Model): 
    areaid = models.FloatField(null=True, db_column='AreaID', blank=True) # Field name made lowercase.
    areaname = models.CharField(max_length=100, db_column='Areaname') # Field name made lowercase.
    seshop = models.IntegerField(null=True, db_column='SEshop', blank=True) # Field name made lowercase.
    prsch = models.IntegerField(null=True, db_column='PrSch', blank=True) # Field name made lowercase.
    secsch = models.IntegerField(null=True, db_column='SecSch', blank=True) # Field name made lowercase.
    hosp = models.IntegerField(null=True, db_column='Hosp', blank=True) # Field name made lowercase.
    hclinic = models.IntegerField(null=True, db_column='HClinic', blank=True) # Field name made lowercase.
    sesport = models.IntegerField(null=True, db_column='SEsport', blank=True) # Field name made lowercase.
    sebusstn = models.IntegerField(null=True, db_column='SEbusstn', blank=True) # Field name made lowercase.
    sehall = models.IntegerField(null=True, db_column='SEhall', blank=True) # Field name made lowercase.
    sepolice = models.IntegerField(null=True, db_column='SEpolice', blank=True) # Field name made lowercase.
    seoth = models.IntegerField(null=True, db_column='SEoth', blank=True) # Field name made lowercase.
    othinfr = models.CharField(max_length=100, db_column='OthInfr') # Field name made lowercase.
    class Meta:
        db_table = 'SocioEconInfr'

class Sownimpntshcounty(models.Model): 
    countyid = models.IntegerField(null=True, db_column='CountyID', blank=True) # Field name made lowercase.
    countyname = models.CharField(max_length=100, db_column='CountyName') # Field name made lowercase.
    dusinsmp = models.IntegerField(null=True, db_column='DUsInSmp', blank=True) # Field name made lowercase.
    smpdus = models.IntegerField(null=True, db_column='SmpDUs', blank=True) # Field name made lowercase.
    pcntdus = models.FloatField(null=True, db_column='pcntDUs', blank=True) # Field name made lowercase.
    dusinarea = models.IntegerField(null=True, db_column='DusInArea', blank=True) # Field name made lowercase.
    totdus = models.IntegerField(null=True, db_column='TotDUs', blank=True) # Field name made lowercase.
    totalppleinarea = models.IntegerField(null=True, db_column='TotalPpleinArea', blank=True) # Field name made lowercase.
    pcntpop = models.FloatField(null=True, db_column='PcntPop', blank=True) # Field name made lowercase.
    pop = models.IntegerField(null=True, db_column='Pop', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'SownImpNtShCounty'

class Sownimpntshslum(models.Model): 
    slumid = models.IntegerField(null=True, db_column='SlumID', blank=True) # Field name made lowercase.
    slumname = models.CharField(max_length=100, db_column='SlumName') # Field name made lowercase.
    dusinsmp = models.IntegerField(null=True, db_column='DUsInSmp', blank=True) # Field name made lowercase.
    smpdus = models.IntegerField(null=True, db_column='SmpDUs', blank=True) # Field name made lowercase.
    pcntdus = models.FloatField(null=True, db_column='pcntDUs', blank=True) # Field name made lowercase.
    dusinarea = models.IntegerField(null=True, db_column='DusInArea', blank=True) # Field name made lowercase.
    totdus = models.IntegerField(null=True, db_column='TotDUs', blank=True) # Field name made lowercase.
    totalppleinarea = models.IntegerField(null=True, db_column='TotalPpleinArea', blank=True) # Field name made lowercase.
    pcntpop = models.FloatField(null=True, db_column='PcntPop', blank=True) # Field name made lowercase.
    pop = models.IntegerField(null=True, db_column='Pop', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'SownImpNtShSlum'

class Sownimpntshunpcounty(models.Model): 
    countyid = models.IntegerField(null=True, db_column='CountyID', blank=True) # Field name made lowercase.
    countyname = models.CharField(max_length=100, db_column='CountyName') # Field name made lowercase.
    dusinsmp = models.IntegerField(null=True, db_column='DUsInSmp', blank=True) # Field name made lowercase.
    smpdus = models.IntegerField(null=True, db_column='SmpDUs', blank=True) # Field name made lowercase.
    pcntdus = models.FloatField(null=True, db_column='pcntDUs', blank=True) # Field name made lowercase.
    dusinarea = models.IntegerField(null=True, db_column='DusInArea', blank=True) # Field name made lowercase.
    totdus = models.IntegerField(null=True, db_column='TotDUs', blank=True) # Field name made lowercase.
    totalppleinarea = models.IntegerField(null=True, db_column='TotalPpleinArea', blank=True) # Field name made lowercase.
    pcntpop = models.FloatField(null=True, db_column='PcntPop', blank=True) # Field name made lowercase.
    pop = models.IntegerField(null=True, db_column='Pop', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'SownImpNtShUnpCounty'

class Sownimpntshunpslum(models.Model): 
    slumid = models.IntegerField(null=True, db_column='SlumID', blank=True) # Field name made lowercase.
    slumname = models.CharField(max_length=100, db_column='SlumName') # Field name made lowercase.
    dusinsmp = models.IntegerField(null=True, db_column='DUsInSmp', blank=True) # Field name made lowercase.
    smpdus = models.IntegerField(null=True, db_column='SmpDUs', blank=True) # Field name made lowercase.
    pcntdus = models.FloatField(null=True, db_column='pcntDUs', blank=True) # Field name made lowercase.
    dusinarea = models.IntegerField(null=True, db_column='DusInArea', blank=True) # Field name made lowercase.
    totdus = models.IntegerField(null=True, db_column='TotDUs', blank=True) # Field name made lowercase.
    totalppleinarea = models.IntegerField(null=True, db_column='TotalPpleinArea', blank=True) # Field name made lowercase.
    pcntpop = models.FloatField(null=True, db_column='PcntPop', blank=True) # Field name made lowercase.
    pop = models.IntegerField(null=True, db_column='Pop', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'SownImpNtShUnpSlum'

class Sownimpntshunpwsp(models.Model): 
    wspid = models.CharField(max_length=100, db_column='WSPID') # Field name made lowercase.
    wspname = models.CharField(max_length=100, db_column='WSPName') # Field name made lowercase.
    dusinsmp = models.IntegerField(null=True, db_column='DUsInSmp', blank=True) # Field name made lowercase.
    smpdus = models.IntegerField(null=True, db_column='SmpDUs', blank=True) # Field name made lowercase.
    pcntdus = models.FloatField(null=True, db_column='pcntDUs', blank=True) # Field name made lowercase.
    dusinarea = models.IntegerField(null=True, db_column='DusInArea', blank=True) # Field name made lowercase.
    totdus = models.IntegerField(null=True, db_column='TotDUs', blank=True) # Field name made lowercase.
    totalppleinarea = models.IntegerField(null=True, db_column='TotalPpleinArea', blank=True) # Field name made lowercase.
    pcntpop = models.FloatField(null=True, db_column='PcntPop', blank=True) # Field name made lowercase.
    pop = models.IntegerField(null=True, db_column='Pop', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'SownImpNtShUnpWSP'

class Sownimpntshwsp(models.Model): 
    wspid = models.CharField(max_length=100, db_column='WSPID') # Field name made lowercase.
    wspname = models.CharField(max_length=100, db_column='WSPName') # Field name made lowercase.
    dusinsmp = models.IntegerField(null=True, db_column='DUsInSmp', blank=True) # Field name made lowercase.
    smpdus = models.IntegerField(null=True, db_column='SmpDUs', blank=True) # Field name made lowercase.
    pcntdus = models.FloatField(null=True, db_column='pcntDUs', blank=True) # Field name made lowercase.
    dusinarea = models.IntegerField(null=True, db_column='DusInArea', blank=True) # Field name made lowercase.
    totdus = models.IntegerField(null=True, db_column='TotDUs', blank=True) # Field name made lowercase.
    totalppleinarea = models.IntegerField(null=True, db_column='TotalPpleinArea', blank=True) # Field name made lowercase.
    pcntpop = models.FloatField(null=True, db_column='PcntPop', blank=True) # Field name made lowercase.
    pop = models.IntegerField(null=True, db_column='Pop', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'SownImpNtShWSP'

class Summaryshtcounty(models.Model): 
    countyid = models.IntegerField(null=True, db_column='CountyID', blank=True) # Field name made lowercase.
    countyname = models.CharField(max_length=100, db_column='CountyName') # Field name made lowercase.
    nareas = models.IntegerField(null=True, db_column='Nareas', blank=True) # Field name made lowercase.
    ntowns = models.IntegerField(null=True, db_column='NTowns', blank=True) # Field name made lowercase.
    pop = models.IntegerField(null=True, db_column='Pop', blank=True) # Field name made lowercase.
    avghhsz = models.FloatField(null=True, db_column='AvgHHSz', blank=True) # Field name made lowercase.
    popplareas = models.CharField(max_length=100, db_column='PopPlAreas') # Field name made lowercase.
    popunplareas = models.CharField(max_length=100, db_column='PopUnplAreas') # Field name made lowercase.
    nareasregfloodg = models.IntegerField(null=True, db_column='NareasRegFloodg', blank=True) # Field name made lowercase.
    mnsrcpcnt = models.CharField(max_length=100, db_column='MnSrcPcnt') # Field name made lowercase.
    drkwatertreated = models.FloatField(null=True, db_column='DrkWaterTreated', blank=True) # Field name made lowercase.
    payingforwater = models.FloatField(null=True, db_column='PayingforWater', blank=True) # Field name made lowercase.
    nareaslinked = models.IntegerField(null=True, db_column='NareasLinked', blank=True) # Field name made lowercase.
    plotsconnected = models.FloatField(null=True, db_column='PlotsConnected', blank=True) # Field name made lowercase.
    dusconnected = models.CharField(max_length=100, db_column='DUsConnected') # Field name made lowercase.
    safewaterpop = models.CharField(max_length=100, db_column='SafeWaterPop') # Field name made lowercase.
    pipedwaterpop = models.CharField(max_length=100, db_column='PipedWaterPop') # Field name made lowercase.
    impsanpop = models.FloatField(null=True, db_column='ImpSanPop', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'SummaryShtCounty'

class Summaryshtslum(models.Model): 
    slumid = models.IntegerField(null=True, db_column='SlumID', blank=True) # Field name made lowercase.
    slumname = models.CharField(max_length=100, db_column='SlumName') # Field name made lowercase.
    nareas = models.IntegerField(null=True, db_column='Nareas', blank=True) # Field name made lowercase.
    ntowns = models.IntegerField(null=True, db_column='NTowns', blank=True) # Field name made lowercase.
    pop = models.IntegerField(null=True, db_column='Pop', blank=True) # Field name made lowercase.
    avghhsz = models.FloatField(null=True, db_column='AvgHHSz', blank=True) # Field name made lowercase.
    popplareas = models.CharField(max_length=100, db_column='PopPlAreas') # Field name made lowercase.
    popunplareas = models.CharField(max_length=100, db_column='PopUnplAreas') # Field name made lowercase.
    nareasregfloodg = models.IntegerField(null=True, db_column='NareasRegFloodg', blank=True) # Field name made lowercase.
    mnsrcpcnt = models.CharField(max_length=67, db_column='MnSrcPcnt') # Field name made lowercase.
    drkwatertreated = models.FloatField(null=True, db_column='DrkWaterTreated', blank=True) # Field name made lowercase.
    payingforwater = models.CharField(max_length=100, db_column='PayingforWater') # Field name made lowercase.
    nareaslinked = models.IntegerField(null=True, db_column='NareasLinked', blank=True) # Field name made lowercase.
    plotsconnected = models.CharField(max_length=100, db_column='PlotsConnected') # Field name made lowercase.
    dusconnected = models.CharField(max_length=100, db_column='DUsConnected') # Field name made lowercase.
    safewaterpop = models.CharField(max_length=100, db_column='SafeWaterPop') # Field name made lowercase.
    pipedwaterpop = models.CharField(max_length=100, db_column='PipedWaterPop') # Field name made lowercase.
    impsanpop = models.CharField(max_length=100, db_column='ImpSanPop') # Field name made lowercase.
    class Meta:
        db_table = 'SummaryShtSlum'

class Summaryshttown(models.Model): 
    townid = models.IntegerField(null=True, db_column='TownID', blank=True) # Field name made lowercase.
    townname = models.CharField(max_length=100, db_column='TownName') # Field name made lowercase.
    nareas = models.IntegerField(null=True, db_column='Nareas', blank=True) # Field name made lowercase.
    ntowns = models.IntegerField(null=True, db_column='Ntowns', blank=True) # Field name made lowercase.
    pop = models.IntegerField(null=True, db_column='Pop', blank=True) # Field name made lowercase.
    avghhsz = models.FloatField(null=True, db_column='AvgHHSz', blank=True) # Field name made lowercase.
    popplareas = models.CharField(max_length=100, db_column='PopPlAreas') # Field name made lowercase.
    popunplareas = models.CharField(max_length=100, db_column='PopUnplAreas') # Field name made lowercase.
    nareasregfloodg = models.IntegerField(null=True, db_column='NareasRegFloodg', blank=True) # Field name made lowercase.
    mnsrcpcnt = models.CharField(max_length=100, db_column='MnSrcPcnt') # Field name made lowercase.
    drkwatertreated = models.CharField(max_length=100, db_column='DrkWaterTreated', blank=True) # Field name made lowercase.
    payingforwater = models.CharField(max_length=100, db_column='PayingforWater', blank=True) # Field name made lowercase.
    nareaslinked = models.CharField(max_length=100, db_column='NareasLinked', blank=True) # Field name made lowercase.
    plotsconnected = models.CharField(max_length=100, db_column='PlotsConnected') # Field name made lowercase.
    dusconnected = models.CharField(max_length=100, db_column='DUsConnected') # Field name made lowercase.
    safewaterpop = models.CharField(max_length=100, db_column='SafeWaterPop') # Field name made lowercase.
    pipedwaterpop = models.CharField(max_length=100, db_column='PipedWaterPop') # Field name made lowercase.
    impsanpop = models.CharField(max_length=100, db_column='ImpSanPop', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'SummaryShtTown'

class Summaryshtwsp(models.Model): 
    wspid = models.CharField(max_length=20, db_column='WSPID', blank=True) # Field name made lowercase.
    wspname = models.CharField(max_length=100, db_column='WSPName', blank=True) # Field name made lowercase.
    nareas = models.IntegerField(null=True, db_column='Nareas', blank=True) # Field name made lowercase.
    ntowns = models.IntegerField(null=True, db_column='Ntowns', blank=True) # Field name made lowercase.
    pop = models.IntegerField(null=True, db_column='Pop', blank=True) # Field name made lowercase.
    avghhsz = models.FloatField(null=True, db_column='AvgHHSz', blank=True) # Field name made lowercase.
    popplareas = models.CharField(max_length=20, db_column='PopPlAreas', blank=True) # Field name made lowercase.
    popunplareas = models.CharField(max_length=20, db_column='PopUnplAreas', blank=True) # Field name made lowercase.
    nareasregfloodg = models.IntegerField(null=True, db_column='NareasRegFloodg', blank=True) # Field name made lowercase.
    mnsrcpcnt = models.TextField(db_column='MnSrcPcnt', blank=True) # Field name made lowercase.
    drkwatertreated = models.FloatField(null=True, db_column='DrkWaterTreated', blank=True) # Field name made lowercase.
    payingforwater = models.FloatField(null=True, db_column='PayingforWater', blank=True) # Field name made lowercase.
    nareaslinked = models.IntegerField(null=True, db_column='NareasLinked', blank=True) # Field name made lowercase.
    plotsconnected = models.CharField(max_length=20, db_column='PlotsConnected', blank=True) # Field name made lowercase.
    dusconnected = models.CharField(max_length=20, db_column='DUsConnected', blank=True) # Field name made lowercase.
    safewaterpop = models.FloatField(null=True, db_column='SafeWaterPop', blank=True) # Field name made lowercase.
    pipedwaterpop = models.FloatField(null=True, db_column='PipedWaterPop', blank=True) # Field name made lowercase.
    impsanpop = models.FloatField(null=True, db_column='ImpSanPop', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'SummaryShtWSP'

class TownsareasCounties(models.Model): 
    countyname = models.CharField(max_length=100, db_column='CountyName') # Field name made lowercase.
    countyid = models.IntegerField(null=True, db_column='Countyid', blank=True) # Field name made lowercase.
    nareas = models.IntegerField(null=True, db_column='NAreas', blank=True) # Field name made lowercase.
    ntowns = models.IntegerField(null=True, db_column='Ntowns', blank=True) # Field name made lowercase.
    pop = models.IntegerField(null=True, db_column='Pop', blank=True) # Field name made lowercase.
    avgpopinarea = models.IntegerField(null=True, db_column='AvgPopinArea', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'TownsAreas-Counties'

class TownsareasSlum(models.Model): 
    slumname = models.CharField(max_length=100, db_column='SlumName') # Field name made lowercase.
    slumid = models.CharField(max_length=100, db_column='Slumid') # Field name made lowercase.
    nareas = models.IntegerField(null=True, db_column='NAreas', blank=True) # Field name made lowercase.
    ntowns = models.IntegerField(null=True, db_column='Ntowns', blank=True) # Field name made lowercase.
    pop = models.IntegerField(null=True, db_column='Pop', blank=True) # Field name made lowercase.
    avgpopinarea = models.IntegerField(null=True, db_column='AvgPopinArea', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'TownsAreas-Slum'

class TownsareasTowns(models.Model): 
    townname = models.CharField(max_length=100)
    townid = models.IntegerField(null=True, db_column='townID', blank=True) # Field name made lowercase.
    nareas = models.IntegerField(null=True, db_column='NAreas', blank=True) # Field name made lowercase.
    ntowns = models.IntegerField(null=True, db_column='Ntowns', blank=True) # Field name made lowercase.
    pop = models.IntegerField(null=True, db_column='Pop', blank=True) # Field name made lowercase.
    avgpopinarea = models.IntegerField(null=True, db_column='AvgPopinArea', blank=True) # Field name made lowercase.
    knbspop = models.CharField(max_length=100, db_column='KNBSPop') # Field name made lowercase.
    pcntpop = models.CharField(max_length=100, db_column='PcntPop') # Field name made lowercase.
    class Meta:
        db_table = 'TownsAreas-Towns'

class TownsareasWsp(models.Model): 
    wspname = models.CharField(max_length=100, db_column='WSPName') # Field name made lowercase.
    wspid = models.CharField(max_length=100, db_column='WSPID') # Field name made lowercase.
    nareas = models.IntegerField(null=True, db_column='NAreas', blank=True) # Field name made lowercase.
    ntowns = models.IntegerField(null=True, db_column='Ntowns', blank=True) # Field name made lowercase.
    pop = models.IntegerField(null=True, db_column='Pop', blank=True) # Field name made lowercase.
    avgpopinarea = models.FloatField(null=True, db_column='AvgPopinArea', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'TownsAreas-WSP'

class Wadeqsupallksk(models.Model): 
    areaid = models.FloatField(null=True, db_column='AreaID', blank=True) # Field name made lowercase.
    areaname = models.CharField(max_length=100, db_column='Areaname') # Field name made lowercase.
    areapop = models.IntegerField(null=True, db_column='AreaPop', blank=True) # Field name made lowercase.
    pubwaterksks = models.IntegerField(null=True, db_column='PubWaterKsks', blank=True) # Field name made lowercase.
    comwaterksks = models.IntegerField(null=True, db_column='ComWaterKsks', blank=True) # Field name made lowercase.
    nadeqsupplied = models.IntegerField(null=True, db_column='NAdeqSupplied', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'WAdeqSupAllKsk'

class Wadeqsupimpwstfsrcs(models.Model): 
    areaid = models.FloatField(null=True, db_column='AreaID', blank=True) # Field name made lowercase.
    areaname = models.CharField(max_length=100, db_column='Areaname') # Field name made lowercase.
    areapop = models.IntegerField(null=True, db_column='AreaPop', blank=True) # Field name made lowercase.
    pubwsptaps = models.IntegerField(null=True, db_column='PubWSPTaps', blank=True) # Field name made lowercase.
    comtaps = models.IntegerField(null=True, db_column='ComTaps', blank=True) # Field name made lowercase.
    pubwaterksks = models.IntegerField(null=True, db_column='PubWaterKsks', blank=True) # Field name made lowercase.
    comwaterksks = models.IntegerField(null=True, db_column='ComWaterKsks', blank=True) # Field name made lowercase.
    nadeqsupplied = models.IntegerField(null=True, db_column='NAdeqSupplied', blank=True) # Field name made lowercase.
    totalcoveredprivcons = models.IntegerField(null=True, db_column='TotalCoveredPrivCons', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'WAdeqSupImpWSTFSrcs'

class Wadeqsupprivcons10D(models.Model): 
    areaid = models.FloatField(null=True, db_column='AreaID', blank=True) # Field name made lowercase.
    areaname = models.CharField(max_length=100, db_column='Areaname') # Field name made lowercase.
    areapop = models.IntegerField(null=True, db_column='AreaPop', blank=True) # Field name made lowercase.
    pcoveredownducon = models.CharField(max_length=100, db_column='PCoveredOwnDuCon') # Field name made lowercase.
    pcoveredpcon = models.CharField(max_length=100, db_column='PCoveredPCon') # Field name made lowercase.
    totalcoveredprivcons = models.IntegerField(null=True, db_column='TotalCoveredPrivCons', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'WAdeqSupPrivCons-10d'

class Wadeqsuppubtap10D(models.Model): 
    areaid = models.FloatField(null=True, db_column='AreaID', blank=True) # Field name made lowercase.
    areaname = models.CharField(max_length=100, db_column='Areaname') # Field name made lowercase.
    areapop = models.IntegerField(null=True, db_column='AreaPop', blank=True) # Field name made lowercase.
    nopubcomtaps = models.IntegerField(null=True, db_column='NoPubComTaps', blank=True) # Field name made lowercase.
    noadeqsupplied = models.IntegerField(null=True, db_column='NoAdeqSupplied', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'WAdeqSupPubTap-10d'

class Wadeqsupwspksk(models.Model): 
    areaid = models.FloatField(null=True, db_column='AreaID', blank=True) # Field name made lowercase.
    areaname = models.CharField(max_length=100, db_column='Areaname') # Field name made lowercase.
    areapop = models.IntegerField(null=True, db_column='AreaPop', blank=True) # Field name made lowercase.
    pubwaterksks = models.IntegerField(null=True, db_column='PubWaterKsks', blank=True) # Field name made lowercase.
    nadeqsupplied = models.IntegerField(null=True, db_column='NAdeqSupplied', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'WAdeqSupWSPKsk'

class Wareasmnprob33County(models.Model): 
    countyid = models.IntegerField(null=True, db_column='CountyId', blank=True) # Field name made lowercase.
    countyname = models.CharField(max_length=100, db_column='Countyname') # Field name made lowercase.
    mainproblem = models.CharField(max_length=100, db_column='MainProblem') # Field name made lowercase.
    nareas = models.IntegerField(null=True, db_column='NAreas', blank=True) # Field name made lowercase.
    totareas = models.IntegerField(null=True, db_column='TotAreas', blank=True) # Field name made lowercase.
    pcntareas = models.FloatField(null=True, db_column='PcntAreas', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'WAreasMnProb33County'

class Wareasmnprob33Slum(models.Model): 
    slumid = models.IntegerField(null=True, db_column='SlumId', blank=True) # Field name made lowercase.
    slumname = models.CharField(max_length=100, db_column='Slumname') # Field name made lowercase.
    mainproblem = models.CharField(max_length=100, db_column='MainProblem') # Field name made lowercase.
    nareas = models.IntegerField(null=True, db_column='NAreas', blank=True) # Field name made lowercase.
    totareas = models.IntegerField(null=True, db_column='TotAreas', blank=True) # Field name made lowercase.
    pcntareas = models.FloatField(null=True, db_column='PcntAreas', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'WAreasMnProb33Slum'

class Wareasmnprob33Town(models.Model): 
    townid = models.IntegerField(null=True, db_column='TownId', blank=True) # Field name made lowercase.
    townname = models.CharField(max_length=100, db_column='Townname') # Field name made lowercase.
    mainproblem = models.CharField(max_length=100, db_column='MainProblem') # Field name made lowercase.
    nareas = models.IntegerField(null=True, db_column='NAreas', blank=True) # Field name made lowercase.
    totareas = models.IntegerField(null=True, db_column='TotAreas', blank=True) # Field name made lowercase.
    pcntareas = models.FloatField(null=True, db_column='PcntAreas', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'WAreasMnProb33Town'

class Wareasmnprob33Wsp(models.Model): 
    wspid = models.CharField(max_length=100, db_column='WSPId') # Field name made lowercase.
    wspname = models.CharField(max_length=100, db_column='WSPname') # Field name made lowercase.
    mainproblem = models.CharField(max_length=100, db_column='MainProblem') # Field name made lowercase.
    nareas = models.IntegerField(null=True, db_column='NAreas', blank=True) # Field name made lowercase.
    totareas = models.IntegerField(null=True, db_column='TotAreas', blank=True) # Field name made lowercase.
    pcntareas = models.FloatField(null=True, db_column='PcntAreas', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'WAreasMnProb33WSP'

class Wareasnwlinkcounty(models.Model): 
    countyid = models.IntegerField(null=True, db_column='CountyId', blank=True) # Field name made lowercase.
    countyname = models.CharField(max_length=100, db_column='Countyname') # Field name made lowercase.
    nareas = models.IntegerField(null=True, db_column='Nareas', blank=True) # Field name made lowercase.
    arealinkedwater = models.CharField(max_length=100, db_column='AreaLinkedwater') # Field name made lowercase.
    totareas = models.IntegerField(null=True, db_column='TotAreas', blank=True) # Field name made lowercase.
    pcntareas = models.FloatField(null=True, db_column='PcntAreas', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'WAreasNWLinkCounty'

class Wareasnwlinkslum(models.Model): 
    slumid = models.IntegerField(null=True, db_column='SlumId', blank=True) # Field name made lowercase.
    slumname = models.CharField(max_length=100, db_column='Slumname') # Field name made lowercase.
    nareas = models.IntegerField(null=True, db_column='Nareas', blank=True) # Field name made lowercase.
    arealinkedwater = models.CharField(max_length=100, db_column='AreaLinkedwater') # Field name made lowercase.
    totareas = models.IntegerField(null=True, db_column='TotAreas', blank=True) # Field name made lowercase.
    pcntareas = models.FloatField(null=True, db_column='PcntAreas', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'WAreasNWLinkSlum'

class Wareasnwlinktown(models.Model): 
    townid = models.IntegerField(null=True, db_column='TownId', blank=True) # Field name made lowercase.
    townname = models.CharField(max_length=100, db_column='Townname') # Field name made lowercase.
    nareas = models.IntegerField(null=True, db_column='Nareas', blank=True) # Field name made lowercase.
    arealinkedwater = models.CharField(max_length=100, db_column='AreaLinkedwater') # Field name made lowercase.
    totareas = models.IntegerField(null=True, db_column='TotAreas', blank=True) # Field name made lowercase.
    pcntareas = models.FloatField(null=True, db_column='PcntAreas', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'WAreasNWLinkTown'

class Wareasnwlinkwsp(models.Model): 
    wspid = models.CharField(max_length=100, db_column='WSPId') # Field name made lowercase.
    wspname = models.CharField(max_length=100, db_column='WSPname') # Field name made lowercase.
    nareas = models.IntegerField(null=True, db_column='Nareas', blank=True) # Field name made lowercase.
    arealinkedwater = models.CharField(max_length=100, db_column='AreaLinkedwater') # Field name made lowercase.
    totareas = models.IntegerField(null=True, db_column='TotAreas', blank=True) # Field name made lowercase.
    pcntareas = models.FloatField(null=True, db_column='PcntAreas', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'WAreasNWLinkWSP'

class Wareastechstatcounty(models.Model): 
    countyid = models.IntegerField(null=True, db_column='CountyId', blank=True) # Field name made lowercase.
    countyname = models.CharField(max_length=100, db_column='Countyname') # Field name made lowercase.
    nareas = models.IntegerField(null=True, db_column='Nareas', blank=True) # Field name made lowercase.
    techstat = models.CharField(max_length=100, db_column='TechStat') # Field name made lowercase.
    totareas = models.IntegerField(null=True, db_column='TotAreas', blank=True) # Field name made lowercase.
    pcntareas = models.FloatField(null=True, db_column='PcntAreas', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'WAreasTechstatCounty'

class Wareastechstatslum(models.Model): 
    slumid = models.IntegerField(null=True, db_column='SlumId', blank=True) # Field name made lowercase.
    slumname = models.CharField(max_length=100, db_column='Slumname') # Field name made lowercase.
    nareas = models.IntegerField(null=True, db_column='Nareas', blank=True) # Field name made lowercase.
    techstat = models.CharField(max_length=100, db_column='TechStat') # Field name made lowercase.
    totareas = models.IntegerField(null=True, db_column='TotAreas', blank=True) # Field name made lowercase.
    pcntareas = models.FloatField(null=True, db_column='PcntAreas', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'WAreasTechstatSlum'

class Wareastechstattown(models.Model): 
    townid = models.IntegerField(null=True, db_column='TownId', blank=True) # Field name made lowercase.
    townname = models.CharField(max_length=100, db_column='Townname') # Field name made lowercase.
    nareas = models.IntegerField(null=True, db_column='Nareas', blank=True) # Field name made lowercase.
    techstat = models.CharField(max_length=100, db_column='TechStat') # Field name made lowercase.
    totareas = models.IntegerField(null=True, db_column='TotAreas', blank=True) # Field name made lowercase.
    pcntareas = models.FloatField(null=True, db_column='PcntAreas', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'WAreasTechstatTown'

class Wareastechstatwsp(models.Model): 
    wspid = models.CharField(max_length=100, db_column='WSPId') # Field name made lowercase.
    wspname = models.CharField(max_length=100, db_column='WSPname') # Field name made lowercase.
    nareas = models.IntegerField(null=True, db_column='Nareas', blank=True) # Field name made lowercase.
    techstat = models.CharField(max_length=100, db_column='TechStat') # Field name made lowercase.
    totareas = models.IntegerField(null=True, db_column='TotAreas', blank=True) # Field name made lowercase.
    pcntareas = models.FloatField(null=True, db_column='PcntAreas', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'WAreasTechstatWSP'

class Wckgsrcpipedcounty(models.Model): 
    countyid = models.IntegerField(null=True, db_column='CountyID', blank=True) # Field name made lowercase.
    countyname = models.CharField(max_length=100, db_column='CountyName') # Field name made lowercase.
    dusinsmp = models.IntegerField(null=True, db_column='DUsInSmp', blank=True) # Field name made lowercase.
    smpdus = models.IntegerField(null=True, db_column='SmpDUs', blank=True) # Field name made lowercase.
    pcntdus = models.FloatField(null=True, db_column='pcntDUs', blank=True) # Field name made lowercase.
    dusinarea = models.IntegerField(null=True, db_column='DusInArea', blank=True) # Field name made lowercase.
    totdus = models.IntegerField(null=True, db_column='TotDUs', blank=True) # Field name made lowercase.
    totalppleinarea = models.IntegerField(null=True, db_column='TotalPpleinArea', blank=True) # Field name made lowercase.
    pcntpop = models.FloatField(null=True, db_column='PcntPop', blank=True) # Field name made lowercase.
    pop = models.IntegerField(null=True, db_column='Pop', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'WCkgSrcPipedCounty'

class Wckgsrcpipedslum(models.Model): 
    slumid = models.IntegerField(null=True, db_column='SlumID', blank=True) # Field name made lowercase.
    slumname = models.CharField(max_length=100, db_column='SlumName') # Field name made lowercase.
    dusinsmp = models.IntegerField(null=True, db_column='DUsInSmp', blank=True) # Field name made lowercase.
    smpdus = models.IntegerField(null=True, db_column='SmpDUs', blank=True) # Field name made lowercase.
    pcntdus = models.FloatField(null=True, db_column='pcntDUs', blank=True) # Field name made lowercase.
    dusinarea = models.IntegerField(null=True, db_column='DusInArea', blank=True) # Field name made lowercase.
    totdus = models.IntegerField(null=True, db_column='TotDUs', blank=True) # Field name made lowercase.
    totalppleinarea = models.IntegerField(null=True, db_column='TotalPpleinArea', blank=True) # Field name made lowercase.
    pcntpop = models.FloatField(null=True, db_column='PcntPop', blank=True) # Field name made lowercase.
    pop = models.IntegerField(null=True, db_column='Pop', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'WCkgSrcPipedSlum'

class Wckgsrcpipedtown(models.Model): 
    townid = models.IntegerField(null=True, db_column='TownID', blank=True) # Field name made lowercase.
    townname = models.CharField(max_length=100, db_column='TownName') # Field name made lowercase.
    dusinsmp = models.IntegerField(null=True, db_column='DUsInSmp', blank=True) # Field name made lowercase.
    smpdus = models.IntegerField(null=True, db_column='SmpDUs', blank=True) # Field name made lowercase.
    pcntdus = models.FloatField(null=True, db_column='pcntDUs', blank=True) # Field name made lowercase.
    dusinarea = models.IntegerField(null=True, db_column='DusInArea', blank=True) # Field name made lowercase.
    totdus = models.IntegerField(null=True, db_column='TotDUs', blank=True) # Field name made lowercase.
    totalppleinarea = models.IntegerField(null=True, db_column='TotalPpleinArea', blank=True) # Field name made lowercase.
    pcntpop = models.FloatField(null=True, db_column='PcntPop', blank=True) # Field name made lowercase.
    pop = models.IntegerField(null=True, db_column='Pop', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'WCkgSrcPipedTown'

class Wckgsrcpipedwsp(models.Model): 
    wspid = models.CharField(max_length=100, db_column='WSPID') # Field name made lowercase.
    wspname = models.CharField(max_length=100, db_column='WSPName') # Field name made lowercase.
    dusinsmp = models.IntegerField(null=True, db_column='DUsInSmp', blank=True) # Field name made lowercase.
    smpdus = models.IntegerField(null=True, db_column='SmpDUs', blank=True) # Field name made lowercase.
    pcntdus = models.FloatField(null=True, db_column='pcntDUs', blank=True) # Field name made lowercase.
    dusinarea = models.IntegerField(null=True, db_column='DusInArea', blank=True) # Field name made lowercase.
    totdus = models.IntegerField(null=True, db_column='TotDUs', blank=True) # Field name made lowercase.
    totalppleinarea = models.IntegerField(null=True, db_column='TotalPpleinArea', blank=True) # Field name made lowercase.
    pcntpop = models.FloatField(null=True, db_column='PcntPop', blank=True) # Field name made lowercase.
    pop = models.IntegerField(null=True, db_column='Pop', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'WCkgSrcPipedWSP'

class WconstatusDu(models.Model): 
    areaid = models.FloatField(null=True, db_column='AreaID', blank=True) # Field name made lowercase.
    areaname = models.CharField(max_length=100, db_column='Areaname') # Field name made lowercase.
    constatus = models.CharField(max_length=100, db_column='ConStatus') # Field name made lowercase.
    dusinsmp = models.IntegerField(null=True, db_column='DUsInSmp', blank=True) # Field name made lowercase.
    pcntdus = models.FloatField(null=True, db_column='pcntDUs', blank=True) # Field name made lowercase.
    dusinarea = models.IntegerField(null=True, db_column='DUsInArea', blank=True) # Field name made lowercase.
    smpduscon = models.IntegerField(null=True, db_column='SmpDUsCon', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'WConStatus-DU'

class Wconstatus34County(models.Model): 
    countyid = models.IntegerField(null=True, db_column='CountyID', blank=True) # Field name made lowercase.
    countyname = models.CharField(max_length=100, db_column='CountyName') # Field name made lowercase.
    constatus = models.CharField(max_length=100, db_column='ConStatus') # Field name made lowercase.
    dusinsmp = models.IntegerField(null=True, db_column='DUsInSmp', blank=True) # Field name made lowercase.
    smpdus = models.IntegerField(null=True, db_column='SmpDUs', blank=True) # Field name made lowercase.
    pcntdus = models.FloatField(null=True, db_column='pcntDUs', blank=True) # Field name made lowercase.
    dusinarea = models.FloatField(null=True, db_column='DUsInArea', blank=True) # Field name made lowercase.
    totdus = models.IntegerField(null=True, db_column='TotDUs', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'WConStatus34County'

class Wconstatus34Slum(models.Model): 
    slumid = models.IntegerField(null=True, db_column='SlumID', blank=True) # Field name made lowercase.
    slumname = models.CharField(max_length=100, db_column='SlumName') # Field name made lowercase.
    constatus = models.CharField(max_length=100, db_column='ConStatus') # Field name made lowercase.
    dusinsmp = models.IntegerField(null=True, db_column='DUsInSmp', blank=True) # Field name made lowercase.
    smpdus = models.IntegerField(null=True, db_column='SmpDUs', blank=True) # Field name made lowercase.
    pcntdus = models.FloatField(null=True, db_column='pcntDUs', blank=True) # Field name made lowercase.
    dusinarea = models.FloatField(null=True, db_column='DUsInArea', blank=True) # Field name made lowercase.
    totdus = models.IntegerField(null=True, db_column='TotDUs', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'WConStatus34Slum'

class Wconstatus34Town(models.Model): 
    townid = models.IntegerField(null=True, db_column='TownID', blank=True) # Field name made lowercase.
    townname = models.CharField(max_length=100, db_column='TownName') # Field name made lowercase.
    constatus = models.CharField(max_length=100, db_column='ConStatus') # Field name made lowercase.
    dusinsmp = models.IntegerField(null=True, db_column='DUsInSmp', blank=True) # Field name made lowercase.
    smpdus = models.IntegerField(null=True, db_column='SmpDUs', blank=True) # Field name made lowercase.
    pcntdus = models.FloatField(null=True, db_column='pcntDUs', blank=True) # Field name made lowercase.
    dusinarea = models.FloatField(null=True, db_column='DUsInArea', blank=True) # Field name made lowercase.
    totdus = models.IntegerField(null=True, db_column='TotDUs', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'WConStatus34Town'

class Wconstatus34Wsp(models.Model): 
    wspid = models.CharField(max_length=100, db_column='WSPID') # Field name made lowercase.
    wspname = models.CharField(max_length=100, db_column='WSPName') # Field name made lowercase.
    constatus = models.CharField(max_length=100, db_column='ConStatus') # Field name made lowercase.
    dusinsmp = models.IntegerField(null=True, db_column='DUsInSmp', blank=True) # Field name made lowercase.
    smpdus = models.IntegerField(null=True, db_column='SmpDUs', blank=True) # Field name made lowercase.
    pcntdus = models.FloatField(null=True, db_column='pcntDUs', blank=True) # Field name made lowercase.
    dusinarea = models.FloatField(null=True, db_column='DUsInArea', blank=True) # Field name made lowercase.
    totdus = models.IntegerField(null=True, db_column='TotDUs', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'WConStatus34WSP'

class Wconsumption(models.Model): 
    areaid = models.FloatField(null=True, db_column='AreaID', blank=True) # Field name made lowercase.
    areaname = models.CharField(max_length=100, db_column='Areaname') # Field name made lowercase.
    wmthconsum = models.CharField(max_length=100, db_column='WMthconsum') # Field name made lowercase.
    areasmpdus = models.IntegerField(null=True, db_column='AreaSmpDUs', blank=True) # Field name made lowercase.
    dus = models.IntegerField(null=True, db_column='DUs', blank=True) # Field name made lowercase.
    pcntdus = models.FloatField(null=True, db_column='pcntDUs', blank=True) # Field name made lowercase.
    ndus = models.IntegerField(null=True, db_column='NDus', blank=True) # Field name made lowercase.
    numdu = models.IntegerField(null=True, db_column='NumDU', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'WConsumption'

class Wduconcounty(models.Model): 
    countyid = models.IntegerField(null=True, db_column='CountyID', blank=True) # Field name made lowercase.
    countyname = models.CharField(max_length=100, db_column='CountyName') # Field name made lowercase.
    duownconnection = models.CharField(max_length=100, db_column='DUOwnconnection') # Field name made lowercase.
    dusinsmp = models.IntegerField(null=True, db_column='DUsInSmp', blank=True) # Field name made lowercase.
    smpdus = models.IntegerField(null=True, db_column='SmpDUs', blank=True) # Field name made lowercase.
    pcntdus = models.FloatField(null=True, db_column='pcntDUs', blank=True) # Field name made lowercase.
    totdus = models.IntegerField(null=True, db_column='TotDUs', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'WDUConCounty'

class Wduconmetcounty(models.Model): 
    countyid = models.IntegerField(null=True, db_column='CountyID', blank=True) # Field name made lowercase.
    countyname = models.CharField(max_length=100, db_column='CountyName') # Field name made lowercase.
    duconmet = models.CharField(max_length=100, db_column='DUconMet') # Field name made lowercase.
    dusinsmp = models.IntegerField(null=True, db_column='DUsInSmp', blank=True) # Field name made lowercase.
    smpdus = models.IntegerField(null=True, db_column='SmpDUs', blank=True) # Field name made lowercase.
    pcntdus = models.FloatField(null=True, db_column='pcntDUs', blank=True) # Field name made lowercase.
    ndus = models.IntegerField(null=True, db_column='NDUs', blank=True) # Field name made lowercase.
    totdus = models.IntegerField(null=True, db_column='TotDUs', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'WDUConMetCounty'

class Wduconmetslum(models.Model): 
    slumid = models.IntegerField(null=True, db_column='SlumID', blank=True) # Field name made lowercase.
    slumname = models.CharField(max_length=100, db_column='SlumName') # Field name made lowercase.
    duconmet = models.CharField(max_length=100, db_column='DUconMet') # Field name made lowercase.
    dusinsmp = models.IntegerField(null=True, db_column='DUsInSmp', blank=True) # Field name made lowercase.
    smpdus = models.IntegerField(null=True, db_column='SmpDUs', blank=True) # Field name made lowercase.
    pcntdus = models.FloatField(null=True, db_column='pcntDUs', blank=True) # Field name made lowercase.
    ndus = models.IntegerField(null=True, db_column='NDUs', blank=True) # Field name made lowercase.
    totdus = models.IntegerField(null=True, db_column='TotDUs', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'WDUConMetSlum'

class Wduconmettown(models.Model): 
    townid = models.IntegerField(null=True, db_column='TownID', blank=True) # Field name made lowercase.
    townname = models.CharField(max_length=100, db_column='TownName') # Field name made lowercase.
    duconmet = models.CharField(max_length=100, db_column='DUconMet') # Field name made lowercase.
    dusinsmp = models.IntegerField(null=True, db_column='DUsInSmp', blank=True) # Field name made lowercase.
    smpdus = models.IntegerField(null=True, db_column='SmpDUs', blank=True) # Field name made lowercase.
    pcntdus = models.FloatField(null=True, db_column='pcntDUs', blank=True) # Field name made lowercase.
    ndus = models.IntegerField(null=True, db_column='NDUs', blank=True) # Field name made lowercase.
    totdus = models.IntegerField(null=True, db_column='TotDUs', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'WDUConMetTown'

class Wduconmetwsp(models.Model): 
    wspid = models.CharField(max_length=100, db_column='WSPID') # Field name made lowercase.
    wspname = models.CharField(max_length=100, db_column='WSPName') # Field name made lowercase.
    duconmet = models.CharField(max_length=100, db_column='DUconMet') # Field name made lowercase.
    dusinsmp = models.IntegerField(null=True, db_column='DUsInSmp', blank=True) # Field name made lowercase.
    smpdus = models.IntegerField(null=True, db_column='SmpDUs', blank=True) # Field name made lowercase.
    pcntdus = models.FloatField(null=True, db_column='pcntDUs', blank=True) # Field name made lowercase.
    ndus = models.IntegerField(null=True, db_column='NDUs', blank=True) # Field name made lowercase.
    totdus = models.IntegerField(null=True, db_column='TotDUs', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'WDUConMetWSP'

class Wduconslum(models.Model): 
    slumid = models.IntegerField(null=True, db_column='SlumID', blank=True) # Field name made lowercase.
    slumname = models.CharField(max_length=100, db_column='SlumName') # Field name made lowercase.
    duownconnection = models.CharField(max_length=100, db_column='DUOwnconnection') # Field name made lowercase.
    dusinsmp = models.IntegerField(null=True, db_column='DUsInSmp', blank=True) # Field name made lowercase.
    smpdus = models.IntegerField(null=True, db_column='SmpDUs', blank=True) # Field name made lowercase.
    pcntdus = models.FloatField(null=True, db_column='pcntDUs', blank=True) # Field name made lowercase.
    totdus = models.IntegerField(null=True, db_column='TotDUs', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'WDUConSlum'

class Wducontown(models.Model): 
    townid = models.IntegerField(null=True, db_column='TownID', blank=True) # Field name made lowercase.
    townname = models.CharField(max_length=100, db_column='TownName') # Field name made lowercase.
    duownconnection = models.CharField(max_length=100, db_column='DUOwnconnection') # Field name made lowercase.
    dusinsmp = models.IntegerField(null=True, db_column='DUsInSmp', blank=True) # Field name made lowercase.
    smpdus = models.IntegerField(null=True, db_column='SmpDUs', blank=True) # Field name made lowercase.
    pcntdus = models.FloatField(null=True, db_column='pcntDUs', blank=True) # Field name made lowercase.
    totdus = models.IntegerField(null=True, db_column='TotDUs', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'WDUConTown'

class Wduconwsp(models.Model): 
    wspid = models.CharField(max_length=100, db_column='WSPID') # Field name made lowercase.
    wspname = models.CharField(max_length=100, db_column='WSPName') # Field name made lowercase.
    duownconnection = models.CharField(max_length=100, db_column='DUOwnconnection') # Field name made lowercase.
    dusinsmp = models.IntegerField(null=True, db_column='DUsInSmp', blank=True) # Field name made lowercase.
    smpdus = models.IntegerField(null=True, db_column='SmpDUs', blank=True) # Field name made lowercase.
    pcntdus = models.FloatField(null=True, db_column='pcntDUs', blank=True) # Field name made lowercase.
    totdus = models.IntegerField(null=True, db_column='TotDUs', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'WDUConWSP'

class Wduowncon(models.Model): 
    areaid = models.FloatField(null=True, db_column='AreaID', blank=True) # Field name made lowercase.
    areaname = models.CharField(max_length=100, db_column='Areaname') # Field name made lowercase.
    duownconnection = models.CharField(max_length=100, db_column='DUOwnconnection') # Field name made lowercase.
    areasmpdus = models.IntegerField(null=True, db_column='AreaSmpDUs', blank=True) # Field name made lowercase.
    dusinsmp = models.IntegerField(null=True, db_column='DUsInSmp', blank=True) # Field name made lowercase.
    pcntdus = models.FloatField(null=True, db_column='pcntDUs', blank=True) # Field name made lowercase.
    dusinarea = models.IntegerField(null=True, db_column='DusInArea', blank=True) # Field name made lowercase.
    totaldusinarea = models.IntegerField(null=True, db_column='TotalDUsInArea', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'WDUOwnCon'

class Wduowncon210D(models.Model): 
    areaid = models.FloatField(null=True, db_column='AreaID', blank=True) # Field name made lowercase.
    areaname = models.CharField(max_length=100, db_column='Areaname') # Field name made lowercase.
    duownconnection = models.CharField(max_length=100, db_column='DUOwnconnection') # Field name made lowercase.
    areasmpdus = models.IntegerField(null=True, db_column='AreaSmpDUs', blank=True) # Field name made lowercase.
    dusinsmp = models.IntegerField(null=True, db_column='DUsInSmp', blank=True) # Field name made lowercase.
    pcntdus = models.FloatField(null=True, db_column='pcntDUs', blank=True) # Field name made lowercase.
    dusinarea = models.IntegerField(null=True, db_column='DusInArea', blank=True) # Field name made lowercase.
    totaldusinarea = models.IntegerField(null=True, db_column='TotalDUsInArea', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'WDUOwnCon2-10d'

class Wduownconmet(models.Model): 
    areaid = models.FloatField(null=True, db_column='AreaID', blank=True) # Field name made lowercase.
    areaname = models.CharField(max_length=100, db_column='Areaname') # Field name made lowercase.
    duconmetered = models.CharField(max_length=100, db_column='DUconmetered') # Field name made lowercase.
    dusinsmp = models.IntegerField(null=True, db_column='DUsInSmp', blank=True) # Field name made lowercase.
    pcntdus = models.FloatField(null=True, db_column='pcntDUs', blank=True) # Field name made lowercase.
    dusinarea = models.IntegerField(null=True, db_column='DUsInArea', blank=True) # Field name made lowercase.
    smpduscon = models.IntegerField(null=True, db_column='SmpDUsCon', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'WDUOwnConMet'

class Wduownconmet210D(models.Model): 
    areaid = models.FloatField(null=True, db_column='AreaID', blank=True) # Field name made lowercase.
    areaname = models.CharField(max_length=100, db_column='Areaname') # Field name made lowercase.
    duconmetered = models.CharField(max_length=100, db_column='DUconmetered') # Field name made lowercase.
    dusinsmp = models.IntegerField(null=True, db_column='DUsInSmp', blank=True) # Field name made lowercase.
    pcntdus = models.FloatField(null=True, db_column='pcntDUs', blank=True) # Field name made lowercase.
    dusinarea = models.IntegerField(null=True, db_column='DUsInArea', blank=True) # Field name made lowercase.
    smpduscon = models.IntegerField(null=True, db_column='SmpDUsCon', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'WDUOwnConMet2-10d'

class Wduwaterpaycounty(models.Model): 
    countyid = models.IntegerField(null=True, db_column='CountyID', blank=True) # Field name made lowercase.
    countyname = models.CharField(max_length=100, db_column='CountyName') # Field name made lowercase.
    waterpaid = models.CharField(max_length=100, db_column='WaterPaid') # Field name made lowercase.
    smpsrc = models.IntegerField(null=True, db_column='SmpSrc', blank=True) # Field name made lowercase.
    smpdus = models.IntegerField(null=True, db_column='SmpDUs', blank=True) # Field name made lowercase.
    totdus = models.IntegerField(null=True, db_column='TotDUs', blank=True) # Field name made lowercase.
    pcntusingsrc = models.FloatField(null=True, db_column='PcntUsingSrc', blank=True) # Field name made lowercase.
    nousingsrc = models.IntegerField(null=True, db_column='NoUsingSrc', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'WDUWaterPayCounty'

class Wduwaterpayslum(models.Model): 
    slumid = models.IntegerField(null=True, db_column='SlumID', blank=True) # Field name made lowercase.
    slumname = models.CharField(max_length=100, db_column='SlumName') # Field name made lowercase.
    waterpaid = models.CharField(max_length=100, db_column='WaterPaid') # Field name made lowercase.
    smpsrc = models.IntegerField(null=True, db_column='SmpSrc', blank=True) # Field name made lowercase.
    smpdus = models.IntegerField(null=True, db_column='SmpDUs', blank=True) # Field name made lowercase.
    totdus = models.IntegerField(null=True, db_column='TotDUs', blank=True) # Field name made lowercase.
    pcntusingsrc = models.FloatField(null=True, db_column='PcntUsingSrc', blank=True) # Field name made lowercase.
    nousingsrc = models.IntegerField(null=True, db_column='NoUsingSrc', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'WDUWaterPaySlum'

class Wduwaterpaytown(models.Model): 
    townid = models.IntegerField(null=True, db_column='TownID', blank=True) # Field name made lowercase.
    townname = models.CharField(max_length=100, db_column='TownName') # Field name made lowercase.
    waterpaid = models.CharField(max_length=100, db_column='WaterPaid') # Field name made lowercase.
    smpsrc = models.IntegerField(null=True, db_column='SmpSrc', blank=True) # Field name made lowercase.
    smpdus = models.IntegerField(null=True, db_column='SmpDUs', blank=True) # Field name made lowercase.
    totdus = models.IntegerField(null=True, db_column='TotDUs', blank=True) # Field name made lowercase.
    pcntusingsrc = models.FloatField(null=True, db_column='PcntUsingSrc', blank=True) # Field name made lowercase.
    nousingsrc = models.IntegerField(null=True, db_column='NoUsingSrc', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'WDUWaterPayTown'

class Wduwaterpaywsp(models.Model): 
    wspid = models.CharField(max_length=100, db_column='WSPID') # Field name made lowercase.
    wspname = models.CharField(max_length=100, db_column='WSPName') # Field name made lowercase.
    waterpaid = models.CharField(max_length=100, db_column='WaterPaid') # Field name made lowercase.
    smpsrc = models.IntegerField(null=True, db_column='SmpSrc', blank=True) # Field name made lowercase.
    smpdus = models.IntegerField(null=True, db_column='SmpDUs', blank=True) # Field name made lowercase.
    totdus = models.IntegerField(null=True, db_column='TotDUs', blank=True) # Field name made lowercase.
    pcntusingsrc = models.FloatField(null=True, db_column='PcntUsingSrc', blank=True) # Field name made lowercase.
    nousingsrc = models.IntegerField(null=True, db_column='NoUsingSrc', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'WDUWaterPayWSP'

class Wdrkqlty33County(models.Model): 
    countyid = models.IntegerField(null=True, db_column='CountyID', blank=True) # Field name made lowercase.
    countyname = models.CharField(max_length=100, db_column='CountyName') # Field name made lowercase.
    wqlty = models.CharField(max_length=100, db_column='WQlty') # Field name made lowercase.
    smpsrc = models.IntegerField(null=True, db_column='SmpSrc', blank=True) # Field name made lowercase.
    smpdus = models.IntegerField(null=True, db_column='SmpDUs', blank=True) # Field name made lowercase.
    totdus = models.IntegerField(null=True, db_column='TotDUs', blank=True) # Field name made lowercase.
    pcntdususingsrc = models.FloatField(null=True, db_column='pcntDUsusingsrc', blank=True) # Field name made lowercase.
    nousingsrc = models.IntegerField(null=True, db_column='NoUsingSrc', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'WDrkQlty33County'

class Wdrkqlty33Slum(models.Model): 
    countyid = models.IntegerField(null=True, db_column='CountyID', blank=True) # Field name made lowercase.
    countyname = models.CharField(max_length=100, db_column='CountyName') # Field name made lowercase.
    wqlty = models.CharField(max_length=100, db_column='WQlty') # Field name made lowercase.
    smpsrc = models.IntegerField(null=True, db_column='SmpSrc', blank=True) # Field name made lowercase.
    smpdus = models.IntegerField(null=True, db_column='SmpDUs', blank=True) # Field name made lowercase.
    totdus = models.IntegerField(null=True, db_column='TotDUs', blank=True) # Field name made lowercase.
    pcntdususingsrc = models.FloatField(null=True, db_column='pcntDUsusingsrc', blank=True) # Field name made lowercase.
    nousingsrc = models.IntegerField(null=True, db_column='NoUsingSrc', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'WDrkQlty33Slum'

class Wdrkqlty33Town(models.Model): 
    townid = models.IntegerField(null=True, db_column='TownID', blank=True) # Field name made lowercase.
    townname = models.CharField(max_length=100, db_column='TownName') # Field name made lowercase.
    wqlty = models.CharField(max_length=100, db_column='WQlty') # Field name made lowercase.
    smpsrc = models.IntegerField(null=True, db_column='SmpSrc', blank=True) # Field name made lowercase.
    smpdus = models.IntegerField(null=True, db_column='SmpDUs', blank=True) # Field name made lowercase.
    totdus = models.IntegerField(null=True, db_column='TotDUs', blank=True) # Field name made lowercase.
    pcntdususingsrc = models.FloatField(null=True, db_column='pcntDUsusingsrc', blank=True) # Field name made lowercase.
    nousingsrc = models.IntegerField(null=True, db_column='NoUsingSrc', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'WDrkQlty33Town'

class Wdrkqlty33Wsp(models.Model): 
    wspid = models.CharField(max_length=100, db_column='WSPID') # Field name made lowercase.
    wspname = models.CharField(max_length=100, db_column='WSPName') # Field name made lowercase.
    wqlty = models.CharField(max_length=100, db_column='WQlty') # Field name made lowercase.
    smpsrc = models.IntegerField(null=True, db_column='SmpSrc', blank=True) # Field name made lowercase.
    smpdus = models.IntegerField(null=True, db_column='SmpDUs', blank=True) # Field name made lowercase.
    totdus = models.IntegerField(null=True, db_column='TotDUs', blank=True) # Field name made lowercase.
    pcntdususingsrc = models.FloatField(null=True, db_column='pcntDUsusingsrc', blank=True) # Field name made lowercase.
    nousingsrc = models.IntegerField(null=True, db_column='NoUsingSrc', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'WDrkQlty33WSP'

class Wdrksrc33County(models.Model): 
    countyid = models.IntegerField(null=True, db_column='CountyID', blank=True) # Field name made lowercase.
    countyname = models.CharField(max_length=100, db_column='CountyName') # Field name made lowercase.
    wdrksrc = models.CharField(max_length=61, db_column='WDrkSrc') # Field name made lowercase.
    smpsrc = models.IntegerField(null=True, db_column='SmpSrc', blank=True) # Field name made lowercase.
    smpdus = models.IntegerField(null=True, db_column='SmpDUs', blank=True) # Field name made lowercase.
    totdus = models.IntegerField(null=True, db_column='TotDUs', blank=True) # Field name made lowercase.
    pcntdususingsrc = models.FloatField(null=True, db_column='pcntDUsusingsrc', blank=True) # Field name made lowercase.
    nousingsrc = models.IntegerField(null=True, db_column='NoUsingSrc', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'WDrkSrc33County'

class Wdrksrc33Slum(models.Model): 
    slumid = models.IntegerField(null=True, db_column='SlumID', blank=True) # Field name made lowercase.
    slumname = models.CharField(max_length=100, db_column='SlumName') # Field name made lowercase.
    wdrksrc = models.CharField(max_length=61, db_column='WDrkSrc') # Field name made lowercase.
    smpsrc = models.IntegerField(null=True, db_column='SmpSrc', blank=True) # Field name made lowercase.
    smpdus = models.IntegerField(null=True, db_column='SmpDUs', blank=True) # Field name made lowercase.
    totdus = models.IntegerField(null=True, db_column='TotDUs', blank=True) # Field name made lowercase.
    pcntdususingsrc = models.FloatField(null=True, db_column='pcntDUsusingsrc', blank=True) # Field name made lowercase.
    nousingsrc = models.IntegerField(null=True, db_column='NoUsingSrc', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'WDrkSrc33Slum'

class Wdrksrc33Town(models.Model): 
    townid = models.IntegerField(null=True, db_column='TownID', blank=True) # Field name made lowercase.
    townname = models.CharField(max_length=100, db_column='TownName') # Field name made lowercase.
    wdrksrc = models.CharField(max_length=61, db_column='WDrkSrc') # Field name made lowercase.
    smpsrc = models.IntegerField(null=True, db_column='SmpSrc', blank=True) # Field name made lowercase.
    smpdus = models.IntegerField(null=True, db_column='SmpDUs', blank=True) # Field name made lowercase.
    totdus = models.IntegerField(null=True, db_column='TotDUs', blank=True) # Field name made lowercase.
    pcntdususingsrc = models.FloatField(null=True, db_column='pcntDUsusingsrc', blank=True) # Field name made lowercase.
    nousingsrc = models.IntegerField(null=True, db_column='NoUsingSrc', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'WDrkSrc33Town'

class Wdrksrc33Wsp(models.Model): 
    wspid = models.CharField(max_length=100, db_column='WSPID') # Field name made lowercase.
    wspname = models.CharField(max_length=100, db_column='WSPName') # Field name made lowercase.
    wdrksrc = models.CharField(max_length=61, db_column='WDrkSrc') # Field name made lowercase.
    smpsrc = models.IntegerField(null=True, db_column='SmpSrc', blank=True) # Field name made lowercase.
    smpdus = models.IntegerField(null=True, db_column='SmpDUs', blank=True) # Field name made lowercase.
    totdus = models.IntegerField(null=True, db_column='TotDUs', blank=True) # Field name made lowercase.
    pcntdususingsrc = models.FloatField(null=True, db_column='pcntDUsusingsrc', blank=True) # Field name made lowercase.
    nousingsrc = models.IntegerField(null=True, db_column='NoUsingSrc', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'WDrkSrc33WSP'

class Wdrksrcbyqltycounty37(models.Model): 
    countyid = models.IntegerField(null=True, db_column='CountyID', blank=True) # Field name made lowercase.
    countyname = models.CharField(max_length=100, db_column='CountyName') # Field name made lowercase.
    wdrksrc = models.CharField(max_length=100, db_column='WDrkSrc') # Field name made lowercase.
    wqlty = models.CharField(max_length=100, db_column='WQlty') # Field name made lowercase.
    smpsrc = models.IntegerField(null=True, db_column='SmpSrc', blank=True) # Field name made lowercase.
    smpdus = models.IntegerField(null=True, db_column='SmpDUs', blank=True) # Field name made lowercase.
    totdus = models.IntegerField(null=True, db_column='TotDUs', blank=True) # Field name made lowercase.
    pcntdususingsrc = models.FloatField(null=True, db_column='pcntDUsusingsrc', blank=True) # Field name made lowercase.
    nousingsrc = models.IntegerField(null=True, db_column='NoUsingSrc', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'WDrkSrcByQltyCounty-37'

class Wdrksrcbyqltyslum37(models.Model): 
    slumid = models.IntegerField(null=True, db_column='SlumID', blank=True) # Field name made lowercase.
    slumname = models.CharField(max_length=100, db_column='SlumName') # Field name made lowercase.
    wdrksrc = models.CharField(max_length=100, db_column='WDrkSrc') # Field name made lowercase.
    wqlty = models.CharField(max_length=100, db_column='WQlty') # Field name made lowercase.
    smpsrc = models.IntegerField(null=True, db_column='SmpSrc', blank=True) # Field name made lowercase.
    smpdus = models.IntegerField(null=True, db_column='SmpDUs', blank=True) # Field name made lowercase.
    totdus = models.IntegerField(null=True, db_column='TotDUs', blank=True) # Field name made lowercase.
    pcntdususingsrc = models.FloatField(null=True, db_column='pcntDUsusingsrc', blank=True) # Field name made lowercase.
    nousingsrc = models.IntegerField(null=True, db_column='NoUsingSrc', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'WDrkSrcByQltySlum-37'

class Wdrksrcbyqltytown37(models.Model): 
    townid = models.IntegerField(null=True, db_column='TownID', blank=True) # Field name made lowercase.
    townname = models.CharField(max_length=100, db_column='TownName') # Field name made lowercase.
    wdrksrc = models.CharField(max_length=100, db_column='WDrkSrc') # Field name made lowercase.
    wqlty = models.CharField(max_length=100, db_column='WQlty') # Field name made lowercase.
    smpsrc = models.IntegerField(null=True, db_column='SmpSrc', blank=True) # Field name made lowercase.
    smpdus = models.IntegerField(null=True, db_column='SmpDUs', blank=True) # Field name made lowercase.
    totdus = models.IntegerField(null=True, db_column='TotDUs', blank=True) # Field name made lowercase.
    pcntdususingsrc = models.FloatField(null=True, db_column='pcntDUsusingsrc', blank=True) # Field name made lowercase.
    nousingsrc = models.IntegerField(null=True, db_column='NoUsingSrc', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'WDrkSrcByQltyTown-37'

class Wdrksrcbyqltywsp37(models.Model): 
    wspid = models.CharField(max_length=100, db_column='WSPID') # Field name made lowercase.
    wspname = models.CharField(max_length=100, db_column='WSPName') # Field name made lowercase.
    wdrksrc = models.CharField(max_length=100, db_column='WDrkSrc') # Field name made lowercase.
    wqlty = models.CharField(max_length=100, db_column='WQlty') # Field name made lowercase.
    smpsrc = models.IntegerField(null=True, db_column='SmpSrc', blank=True) # Field name made lowercase.
    smpdus = models.IntegerField(null=True, db_column='SmpDUs', blank=True) # Field name made lowercase.
    totdus = models.IntegerField(null=True, db_column='TotDUs', blank=True) # Field name made lowercase.
    pcntdususingsrc = models.FloatField(null=True, db_column='pcntDUsusingsrc', blank=True) # Field name made lowercase.
    nousingsrc = models.IntegerField(null=True, db_column='NoUsingSrc', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'WDrkSrcByQltyWSP-37'

class Wdrksrcbytrtmthdslum38(models.Model): 
    slumid = models.IntegerField(null=True, db_column='SlumID', blank=True) # Field name made lowercase.
    slumname = models.CharField(max_length=100, db_column='SlumName') # Field name made lowercase.
    wdrksrc = models.CharField(max_length=100, db_column='WDrkSrc') # Field name made lowercase.
    drkwatertrtmthd = models.TextField(db_column='DrkWaterTrtMthd') # Field name made lowercase.
    smpsrc = models.IntegerField(null=True, db_column='SmpSrc', blank=True) # Field name made lowercase.
    smpdus = models.IntegerField(null=True, db_column='SmpDUs', blank=True) # Field name made lowercase.
    totdus = models.IntegerField(null=True, db_column='TotDUs', blank=True) # Field name made lowercase.
    pcntdususingsrc = models.FloatField(null=True, db_column='pcntDUsusingsrc', blank=True) # Field name made lowercase.
    nousingsrc = models.IntegerField(null=True, db_column='NoUsingSrc', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'WDrkSrcByTrtMthdSlum-38'

class Wdrksrcbytrtmthdtown38(models.Model): 
    townid = models.IntegerField(null=True, db_column='TownID', blank=True) # Field name made lowercase.
    townname = models.CharField(max_length=100, db_column='TownName') # Field name made lowercase.
    wdrksrc = models.CharField(max_length=100, db_column='WDrkSrc') # Field name made lowercase.
    drkwatertrtmthd = models.CharField(max_length=65, db_column='DrkWaterTrtMthd') # Field name made lowercase.
    smpsrc = models.IntegerField(null=True, db_column='SmpSrc', blank=True) # Field name made lowercase.
    smpdus = models.IntegerField(null=True, db_column='SmpDUs', blank=True) # Field name made lowercase.
    totdus = models.IntegerField(null=True, db_column='TotDUs', blank=True) # Field name made lowercase.
    pcntdususingsrc = models.FloatField(null=True, db_column='pcntDUsusingsrc', blank=True) # Field name made lowercase.
    nousingsrc = models.IntegerField(null=True, db_column='NoUsingSrc', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'WDrkSrcByTrtMthdTown-38'

class Wdrksrcbytrtmthdwsp38(models.Model): 
    wspid = models.CharField(max_length=100, db_column='WSPID') # Field name made lowercase.
    wspname = models.CharField(max_length=100, db_column='WSPName') # Field name made lowercase.
    wdrksrc = models.CharField(max_length=100, db_column='WDrkSrc') # Field name made lowercase.
    drkwatertrtmthd = models.CharField(max_length=65, db_column='DrkWaterTrtMthd') # Field name made lowercase.
    smpsrc = models.IntegerField(null=True, db_column='SmpSrc', blank=True) # Field name made lowercase.
    smpdus = models.IntegerField(null=True, db_column='SmpDUs', blank=True) # Field name made lowercase.
    totdus = models.IntegerField(null=True, db_column='TotDUs', blank=True) # Field name made lowercase.
    pcntdususingsrc = models.FloatField(null=True, db_column='pcntDUsusingsrc', blank=True) # Field name made lowercase.
    nousingsrc = models.IntegerField(null=True, db_column='NoUsingSrc', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'WDrkSrcByTrtMthdWSP-38'

class Wdrksrccmtaps10D(models.Model): 
    areaid = models.FloatField(null=True, db_column='AreaID', blank=True) # Field name made lowercase.
    areaname = models.CharField(max_length=100, db_column='Areaname') # Field name made lowercase.
    areasmpdus = models.IntegerField(null=True, db_column='AreaSmpDUs', blank=True) # Field name made lowercase.
    dusinsmp = models.IntegerField(null=True, db_column='DUsInSmp', blank=True) # Field name made lowercase.
    pcntdus = models.FloatField(null=True, db_column='pcntDUs', blank=True) # Field name made lowercase.
    dusinarea = models.IntegerField(null=True, db_column='DusInArea', blank=True) # Field name made lowercase.
    smppersons = models.IntegerField(null=True, db_column='SmpPersons', blank=True) # Field name made lowercase.
    totalppleinarea = models.IntegerField(null=True, db_column='TotalPpleinArea', blank=True) # Field name made lowercase.
    pcntpple = models.FloatField(null=True, blank=True)
    totaldusinarea = models.IntegerField(null=True, db_column='TotalDUsInArea', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'WDrkSrcCmTaps-10d'

class Wdrksrcleak(models.Model): 
    areaid = models.FloatField(null=True, db_column='AreaID', blank=True) # Field name made lowercase.
    areaname = models.CharField(max_length=100, db_column='Areaname') # Field name made lowercase.
    areasmpdus = models.IntegerField(null=True, db_column='AreaSmpDUs', blank=True) # Field name made lowercase.
    dusinsmp = models.IntegerField(null=True, db_column='DUsInSmp', blank=True) # Field name made lowercase.
    pcntdus = models.FloatField(null=True, db_column='pcntDUs', blank=True) # Field name made lowercase.
    dusinarea = models.IntegerField(null=True, db_column='DusInArea', blank=True) # Field name made lowercase.
    smppersons = models.IntegerField(null=True, db_column='SmpPersons', blank=True) # Field name made lowercase.
    totalppleinarea = models.IntegerField(null=True, db_column='TotalPpleinArea', blank=True) # Field name made lowercase.
    pcntpple = models.FloatField(null=True, blank=True)
    totaldusinarea = models.IntegerField(null=True, db_column='TotalDUsInArea', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'WDrkSrcLeak'

class Wdrksrcothcon(models.Model): 
    areaid = models.FloatField(null=True, db_column='AreaID', blank=True) # Field name made lowercase.
    areaname = models.CharField(max_length=100, db_column='Areaname') # Field name made lowercase.
    areasmpdus = models.IntegerField(null=True, db_column='AreaSmpDUs', blank=True) # Field name made lowercase.
    dusinsmp = models.IntegerField(null=True, db_column='DUsInSmp', blank=True) # Field name made lowercase.
    pcntdus = models.FloatField(null=True, db_column='pcntDUs', blank=True) # Field name made lowercase.
    dusinarea = models.IntegerField(null=True, db_column='DusInArea', blank=True) # Field name made lowercase.
    smppersons = models.IntegerField(null=True, db_column='SmpPersons', blank=True) # Field name made lowercase.
    totalppleinarea = models.IntegerField(null=True, db_column='TotalPpleinArea', blank=True) # Field name made lowercase.
    pcntpple = models.FloatField(null=True, blank=True)
    totaldusinarea = models.IntegerField(null=True, db_column='TotalDUsInArea', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'WDrkSrcOthCon'

class Wdrksrcpipedcounty(models.Model): 
    countyid = models.IntegerField(null=True, db_column='CountyID', blank=True) # Field name made lowercase.
    countyname = models.CharField(max_length=100, db_column='CountyName') # Field name made lowercase.
    dusinsmp = models.IntegerField(null=True, db_column='DUsInSmp', blank=True) # Field name made lowercase.
    smpdus = models.IntegerField(null=True, db_column='SmpDUs', blank=True) # Field name made lowercase.
    pcntdus = models.FloatField(null=True, db_column='pcntDUs', blank=True) # Field name made lowercase.
    dusinarea = models.IntegerField(null=True, db_column='DusInArea', blank=True) # Field name made lowercase.
    totdus = models.IntegerField(null=True, db_column='TotDUs', blank=True) # Field name made lowercase.
    totalppleinarea = models.IntegerField(null=True, db_column='TotalPpleinArea', blank=True) # Field name made lowercase.
    pcntpop = models.FloatField(null=True, db_column='PcntPop', blank=True) # Field name made lowercase.
    pop = models.IntegerField(null=True, db_column='Pop', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'WDrkSrcPipedCounty'

class Wdrksrcpipedslum(models.Model): 
    slumid = models.IntegerField(null=True, db_column='SlumID', blank=True) # Field name made lowercase.
    slumname = models.CharField(max_length=100, db_column='SlumName') # Field name made lowercase.
    dusinsmp = models.IntegerField(null=True, db_column='DUsInSmp', blank=True) # Field name made lowercase.
    smpdus = models.IntegerField(null=True, db_column='SmpDUs', blank=True) # Field name made lowercase.
    pcntdus = models.FloatField(null=True, db_column='pcntDUs', blank=True) # Field name made lowercase.
    dusinarea = models.IntegerField(null=True, db_column='DusInArea', blank=True) # Field name made lowercase.
    totdus = models.IntegerField(null=True, db_column='TotDUs', blank=True) # Field name made lowercase.
    totalppleinarea = models.IntegerField(null=True, db_column='TotalPpleinArea', blank=True) # Field name made lowercase.
    pcntpop = models.FloatField(null=True, db_column='PcntPop', blank=True) # Field name made lowercase.
    pop = models.IntegerField(null=True, db_column='Pop', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'WDrkSrcPipedSlum'

class Wdrksrcpipedtown(models.Model): 
    townid = models.IntegerField(null=True, db_column='TownID', blank=True) # Field name made lowercase.
    townname = models.CharField(max_length=100, db_column='TownName') # Field name made lowercase.
    dusinsmp = models.IntegerField(null=True, db_column='DUsInSmp', blank=True) # Field name made lowercase.
    smpdus = models.IntegerField(null=True, db_column='SmpDUs', blank=True) # Field name made lowercase.
    pcntdus = models.FloatField(null=True, db_column='pcntDUs', blank=True) # Field name made lowercase.
    dusinarea = models.IntegerField(null=True, db_column='DusInArea', blank=True) # Field name made lowercase.
    totdus = models.IntegerField(null=True, db_column='TotDUs', blank=True) # Field name made lowercase.
    totalppleinarea = models.IntegerField(null=True, db_column='TotalPpleinArea', blank=True) # Field name made lowercase.
    pcntpop = models.FloatField(null=True, db_column='PcntPop', blank=True) # Field name made lowercase.
    pop = models.IntegerField(null=True, db_column='Pop', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'WDrkSrcPipedTown'

class Wdrksrcpipedwsp(models.Model): 
    wspid = models.CharField(max_length=100, db_column='WSPID') # Field name made lowercase.
    wspname = models.CharField(max_length=100, db_column='WSPName') # Field name made lowercase.
    dusinsmp = models.IntegerField(null=True, db_column='DUsInSmp', blank=True) # Field name made lowercase.
    smpdus = models.IntegerField(null=True, db_column='SmpDUs', blank=True) # Field name made lowercase.
    pcntdus = models.FloatField(null=True, db_column='pcntDUs', blank=True) # Field name made lowercase.
    dusinarea = models.IntegerField(null=True, db_column='DusInArea', blank=True) # Field name made lowercase.
    totdus = models.IntegerField(null=True, db_column='TotDUs', blank=True) # Field name made lowercase.
    totalppleinarea = models.IntegerField(null=True, db_column='TotalPpleinArea', blank=True) # Field name made lowercase.
    pcntpop = models.FloatField(null=True, db_column='PcntPop', blank=True) # Field name made lowercase.
    pop = models.IntegerField(null=True, db_column='Pop', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'WDrkSrcPipedWSP'

class Wdrksrcreseller(models.Model): 
    areaid = models.FloatField(null=True, db_column='AreaID', blank=True) # Field name made lowercase.
    areaname = models.CharField(max_length=100, db_column='Areaname') # Field name made lowercase.
    areasmpdus = models.IntegerField(null=True, db_column='AreaSmpDUs', blank=True) # Field name made lowercase.
    dusinsmp = models.IntegerField(null=True, db_column='DUsInSmp', blank=True) # Field name made lowercase.
    pcntdus = models.FloatField(null=True, db_column='pcntDUs', blank=True) # Field name made lowercase.
    dusinarea = models.IntegerField(null=True, db_column='DusInArea', blank=True) # Field name made lowercase.
    smppersons = models.IntegerField(null=True, db_column='SmpPersons', blank=True) # Field name made lowercase.
    totalppleinarea = models.IntegerField(null=True, db_column='TotalPpleinArea', blank=True) # Field name made lowercase.
    pcntpple = models.FloatField(null=True, blank=True)
    totaldusinarea = models.IntegerField(null=True, db_column='TotalDUsInArea', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'WDrkSrcReseller'

class Wdrksrcywell(models.Model): 
    areaid = models.FloatField(null=True, db_column='AreaID', blank=True) # Field name made lowercase.
    areaname = models.CharField(max_length=100, db_column='Areaname') # Field name made lowercase.
    areasmpdus = models.IntegerField(null=True, db_column='AreaSmpDUs', blank=True) # Field name made lowercase.
    dusinsmp = models.IntegerField(null=True, db_column='DUsInSmp', blank=True) # Field name made lowercase.
    pcntdus = models.FloatField(null=True, db_column='pcntDUs', blank=True) # Field name made lowercase.
    dusinarea = models.IntegerField(null=True, db_column='DusInArea', blank=True) # Field name made lowercase.
    smppersons = models.IntegerField(null=True, db_column='SmpPersons', blank=True) # Field name made lowercase.
    totalppleinarea = models.IntegerField(null=True, db_column='TotalPpleinArea', blank=True) # Field name made lowercase.
    pcntpple = models.FloatField(null=True, blank=True)
    totaldusinarea = models.IntegerField(null=True, db_column='TotalDUsInArea', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'WDrkSrcYWell'

class Wfetchdurationdu(models.Model): 
    areaid = models.FloatField(null=True, db_column='AreaID', blank=True) # Field name made lowercase.
    areaname = models.CharField(max_length=100, db_column='Areaname') # Field name made lowercase.
    durationrange = models.CharField(max_length=100, db_column='DurationRange') # Field name made lowercase.
    areasmpdus = models.IntegerField(null=True, db_column='AreaSmpDUs', blank=True) # Field name made lowercase.
    smpdus = models.IntegerField(null=True, db_column='SmpDUs', blank=True) # Field name made lowercase.
    pcntdus = models.FloatField(null=True, db_column='pcntDUs', blank=True) # Field name made lowercase.
    ndus = models.IntegerField(null=True, db_column='NDus', blank=True) # Field name made lowercase.
    numdu = models.IntegerField(null=True, db_column='numDU', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'WFetchDurationDU'

class Wimpdrksrcjmp(models.Model): 
    areaid = models.FloatField(null=True, db_column='AreaID', blank=True) # Field name made lowercase.
    areaname = models.CharField(max_length=100, db_column='Areaname') # Field name made lowercase.
    areasmpdus = models.IntegerField(null=True, db_column='AreaSmpDUs', blank=True) # Field name made lowercase.
    dusinsmp = models.IntegerField(null=True, db_column='DUsInSmp', blank=True) # Field name made lowercase.
    pcntdus = models.FloatField(null=True, db_column='pcntDUs', blank=True) # Field name made lowercase.
    dusinarea = models.IntegerField(null=True, db_column='DusInArea', blank=True) # Field name made lowercase.
    smppersons = models.IntegerField(null=True, db_column='SmpPersons', blank=True) # Field name made lowercase.
    totalppleinarea = models.IntegerField(null=True, db_column='TotalPpleinArea', blank=True) # Field name made lowercase.
    pcntpple = models.FloatField(null=True, blank=True)
    totaldusinarea = models.IntegerField(null=True, db_column='TotalDUsInArea', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'WImpDrkSrcJMP'

class Wimpdrksrcjmp30Mn(models.Model): 
    areaid = models.FloatField(null=True, db_column='AreaID', blank=True) # Field name made lowercase.
    areaname = models.CharField(max_length=100, db_column='Areaname') # Field name made lowercase.
    areasmpdus = models.IntegerField(null=True, db_column='AreaSmpDUs', blank=True) # Field name made lowercase.
    dusinsmp = models.IntegerField(null=True, db_column='DUsInSmp', blank=True) # Field name made lowercase.
    pcntdus = models.FloatField(null=True, db_column='pcntDUs', blank=True) # Field name made lowercase.
    dusinarea = models.IntegerField(null=True, db_column='DusInArea', blank=True) # Field name made lowercase.
    smppersons = models.IntegerField(null=True, db_column='SmpPersons', blank=True) # Field name made lowercase.
    totalppleinarea = models.IntegerField(null=True, db_column='TotalPpleinArea', blank=True) # Field name made lowercase.
    pcntpple = models.FloatField(null=True, blank=True)
    totaldusinarea = models.IntegerField(null=True, db_column='TotalDUsInArea', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'WImpDrkSrcJMP30mn'

class Wimpdrksrcjmpbyqlty(models.Model): 
    areaid = models.FloatField(null=True, db_column='AreaID', blank=True) # Field name made lowercase.
    areaname = models.CharField(max_length=100, db_column='Areaname') # Field name made lowercase.
    wqlty = models.CharField(max_length=100, db_column='WQlty') # Field name made lowercase.
    areasmpdus = models.IntegerField(null=True, db_column='AreaSmpDUs', blank=True) # Field name made lowercase.
    dusinsmp = models.IntegerField(null=True, db_column='DUsInSmp', blank=True) # Field name made lowercase.
    pcntdus = models.FloatField(null=True, db_column='pcntDUs', blank=True) # Field name made lowercase.
    dusinarea = models.IntegerField(null=True, db_column='DusInArea', blank=True) # Field name made lowercase.
    smppersons = models.IntegerField(null=True, db_column='SmpPersons', blank=True) # Field name made lowercase.
    totalppleinarea = models.IntegerField(null=True, db_column='TotalPpleinArea', blank=True) # Field name made lowercase.
    pcntpple = models.FloatField(null=True, blank=True)
    totaldusinarea = models.IntegerField(null=True, db_column='TotalDUsInArea', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'WImpDrkSrcJMPByQlty'

class Wimpdrksrcjmpbytrt(models.Model): 
    areaid = models.FloatField(null=True, db_column='AreaID', blank=True) # Field name made lowercase.
    areaname = models.CharField(max_length=100, db_column='Areaname') # Field name made lowercase.
    wtrtdrk = models.CharField(max_length=100, db_column='WTrtDrk') # Field name made lowercase.
    areasmpdus = models.IntegerField(null=True, db_column='AreaSmpDUs', blank=True) # Field name made lowercase.
    dusinsmp = models.IntegerField(null=True, db_column='DUsInSmp', blank=True) # Field name made lowercase.
    pcntdus = models.FloatField(null=True, db_column='pcntDUs', blank=True) # Field name made lowercase.
    dusinarea = models.IntegerField(null=True, db_column='DusInArea', blank=True) # Field name made lowercase.
    smppersons = models.IntegerField(null=True, db_column='SmpPersons', blank=True) # Field name made lowercase.
    totalppleinarea = models.IntegerField(null=True, db_column='TotalPpleinArea', blank=True) # Field name made lowercase.
    pcntpple = models.FloatField(null=True, blank=True)
    totaldusinarea = models.IntegerField(null=True, db_column='TotalDUsInArea', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'WImpDrkSrcJMPByTrt'

class Wimpdrksrcwstf(models.Model): 
    areaid = models.FloatField(null=True, db_column='AreaID', blank=True) # Field name made lowercase.
    areaname = models.CharField(max_length=100, db_column='Areaname') # Field name made lowercase.
    areasmpdus = models.IntegerField(null=True, db_column='AreaSmpDUs', blank=True) # Field name made lowercase.
    dusinsmp = models.IntegerField(null=True, db_column='DUsInSmp', blank=True) # Field name made lowercase.
    pcntdus = models.FloatField(null=True, db_column='pcntDUs', blank=True) # Field name made lowercase.
    dusinarea = models.IntegerField(null=True, db_column='DusInArea', blank=True) # Field name made lowercase.
    smppersons = models.IntegerField(null=True, db_column='SmpPersons', blank=True) # Field name made lowercase.
    totalppleinarea = models.IntegerField(null=True, db_column='TotalPpleinArea', blank=True) # Field name made lowercase.
    pcntpple = models.FloatField(null=True, blank=True)
    totaldusinarea = models.IntegerField(null=True, db_column='TotalDUsInArea', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'WImpDrkSrcWSTF'

class Wimpdrksrcwstf30Mn(models.Model): 
    areaid = models.FloatField(null=True, db_column='AreaID', blank=True) # Field name made lowercase.
    areaname = models.CharField(max_length=100, db_column='Areaname') # Field name made lowercase.
    areasmpdus = models.IntegerField(null=True, db_column='AreaSmpDUs', blank=True) # Field name made lowercase.
    dusinsmp = models.IntegerField(null=True, db_column='DUsInSmp', blank=True) # Field name made lowercase.
    pcntdus = models.FloatField(null=True, db_column='pcntDUs', blank=True) # Field name made lowercase.
    dusinarea = models.IntegerField(null=True, db_column='DusInArea', blank=True) # Field name made lowercase.
    smppersons = models.IntegerField(null=True, db_column='SmpPersons', blank=True) # Field name made lowercase.
    totalppleinarea = models.IntegerField(null=True, db_column='TotalPpleinArea', blank=True) # Field name made lowercase.
    pcntpple = models.FloatField(null=True, blank=True)
    totaldusinarea = models.IntegerField(null=True, db_column='TotalDUsInArea', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'WImpDrkSrcWSTF30mn'

class Wimpdrksrcwstfbyqlty(models.Model): 
    areaid = models.FloatField(null=True, db_column='AreaID', blank=True) # Field name made lowercase.
    areaname = models.CharField(max_length=100, db_column='Areaname') # Field name made lowercase.
    wqlty = models.CharField(max_length=100, db_column='WQlty') # Field name made lowercase.
    areasmpdus = models.IntegerField(null=True, db_column='AreaSmpDUs', blank=True) # Field name made lowercase.
    dusinsmp = models.IntegerField(null=True, db_column='DUsInSmp', blank=True) # Field name made lowercase.
    pcntdus = models.FloatField(null=True, db_column='pcntDUs', blank=True) # Field name made lowercase.
    dusinarea = models.IntegerField(null=True, db_column='DusInArea', blank=True) # Field name made lowercase.
    smppersons = models.IntegerField(null=True, db_column='SmpPersons', blank=True) # Field name made lowercase.
    totalppleinarea = models.IntegerField(null=True, db_column='TotalPpleinArea', blank=True) # Field name made lowercase.
    pcntpple = models.FloatField(null=True, blank=True)
    totaldusinarea = models.IntegerField(null=True, db_column='TotalDUsInArea', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'WImpDrkSrcWSTFByQlty'

class Wimpdrksrcwstfbytrt(models.Model): 
    areaid = models.FloatField(null=True, db_column='AreaID', blank=True) # Field name made lowercase.
    areaname = models.CharField(max_length=100, db_column='Areaname') # Field name made lowercase.
    wtrtdrk = models.CharField(max_length=100, db_column='WTrtDrk') # Field name made lowercase.
    areasmpdus = models.IntegerField(null=True, db_column='AreaSmpDUs', blank=True) # Field name made lowercase.
    dusinsmp = models.IntegerField(null=True, db_column='DUsInSmp', blank=True) # Field name made lowercase.
    pcntdus = models.FloatField(null=True, db_column='pcntDUs', blank=True) # Field name made lowercase.
    dusinarea = models.IntegerField(null=True, db_column='DusInArea', blank=True) # Field name made lowercase.
    smppersons = models.IntegerField(null=True, db_column='SmpPersons', blank=True) # Field name made lowercase.
    totalppleinarea = models.IntegerField(null=True, db_column='TotalPpleinArea', blank=True) # Field name made lowercase.
    pcntpple = models.FloatField(null=True, blank=True)
    totaldusinarea = models.IntegerField(null=True, db_column='TotalDUsInArea', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'WImpDrkSrcWSTFByTrt'

class Wimpsrcbathwstfcounty(models.Model): 
    countyid = models.IntegerField(null=True, db_column='CountyID', blank=True) # Field name made lowercase.
    countyname = models.CharField(max_length=100, db_column='CountyName') # Field name made lowercase.
    dusinsmp = models.IntegerField(null=True, db_column='DUsInSmp', blank=True) # Field name made lowercase.
    smpdus = models.IntegerField(null=True, db_column='SmpDUs', blank=True) # Field name made lowercase.
    pcntdus = models.FloatField(null=True, db_column='pcntDUs', blank=True) # Field name made lowercase.
    dusinarea = models.IntegerField(null=True, db_column='DusInArea', blank=True) # Field name made lowercase.
    totdus = models.IntegerField(null=True, db_column='TotDUs', blank=True) # Field name made lowercase.
    totalppleinarea = models.IntegerField(null=True, db_column='TotalPpleinArea', blank=True) # Field name made lowercase.
    pcntpop = models.FloatField(null=True, db_column='PcntPop', blank=True) # Field name made lowercase.
    pop = models.IntegerField(null=True, db_column='Pop', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'WImpSrcBathWSTFCounty'

class Wimpsrcbathwstfslum(models.Model): 
    slumid = models.IntegerField(null=True, db_column='SlumID', blank=True) # Field name made lowercase.
    slumname = models.CharField(max_length=100, db_column='SlumName') # Field name made lowercase.
    dusinsmp = models.IntegerField(null=True, db_column='DUsInSmp', blank=True) # Field name made lowercase.
    smpdus = models.IntegerField(null=True, db_column='SmpDUs', blank=True) # Field name made lowercase.
    pcntdus = models.FloatField(null=True, db_column='pcntDUs', blank=True) # Field name made lowercase.
    dusinarea = models.IntegerField(null=True, db_column='DusInArea', blank=True) # Field name made lowercase.
    totdus = models.IntegerField(null=True, db_column='TotDUs', blank=True) # Field name made lowercase.
    totalppleinarea = models.IntegerField(null=True, db_column='TotalPpleinArea', blank=True) # Field name made lowercase.
    pcntpop = models.FloatField(null=True, db_column='PcntPop', blank=True) # Field name made lowercase.
    pop = models.IntegerField(null=True, db_column='Pop', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'WImpSrcBathWSTFSlum'

class Wimpsrcbathwstftown(models.Model): 
    townid = models.IntegerField(null=True, db_column='TownID', blank=True) # Field name made lowercase.
    townname = models.CharField(max_length=100, db_column='TownName') # Field name made lowercase.
    dusinsmp = models.IntegerField(null=True, db_column='DUsInSmp', blank=True) # Field name made lowercase.
    smpdus = models.IntegerField(null=True, db_column='SmpDUs', blank=True) # Field name made lowercase.
    pcntdus = models.FloatField(null=True, db_column='pcntDUs', blank=True) # Field name made lowercase.
    dusinarea = models.IntegerField(null=True, db_column='DusInArea', blank=True) # Field name made lowercase.
    totdus = models.IntegerField(null=True, db_column='TotDUs', blank=True) # Field name made lowercase.
    totalppleinarea = models.IntegerField(null=True, db_column='TotalPpleinArea', blank=True) # Field name made lowercase.
    pcntpop = models.FloatField(null=True, db_column='PcntPop', blank=True) # Field name made lowercase.
    pop = models.IntegerField(null=True, db_column='Pop', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'WImpSrcBathWSTFTown'

class Wimpsrcbathwstfwsp(models.Model): 
    wspid = models.CharField(max_length=100, db_column='WSPID') # Field name made lowercase.
    wspname = models.CharField(max_length=100, db_column='WSPName') # Field name made lowercase.
    dusinsmp = models.IntegerField(null=True, db_column='DUsInSmp', blank=True) # Field name made lowercase.
    smpdus = models.IntegerField(null=True, db_column='SmpDUs', blank=True) # Field name made lowercase.
    pcntdus = models.FloatField(null=True, db_column='pcntDUs', blank=True) # Field name made lowercase.
    dusinarea = models.IntegerField(null=True, db_column='DusInArea', blank=True) # Field name made lowercase.
    totdus = models.IntegerField(null=True, db_column='TotDUs', blank=True) # Field name made lowercase.
    totalppleinarea = models.IntegerField(null=True, db_column='TotalPpleinArea', blank=True) # Field name made lowercase.
    pcntpop = models.FloatField(null=True, db_column='PcntPop', blank=True) # Field name made lowercase.
    pop = models.IntegerField(null=True, db_column='Pop', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'WImpSrcBathWSTFWSP'

class Wimpsrcckgwstfcounty(models.Model): 
    countyid = models.IntegerField(null=True, db_column='CountyID', blank=True) # Field name made lowercase.
    countyname = models.CharField(max_length=100, db_column='CountyName') # Field name made lowercase.
    dusinsmp = models.IntegerField(null=True, db_column='DUsInSmp', blank=True) # Field name made lowercase.
    smpdus = models.IntegerField(null=True, db_column='SmpDUs', blank=True) # Field name made lowercase.
    pcntdus = models.FloatField(null=True, db_column='pcntDUs', blank=True) # Field name made lowercase.
    dusinarea = models.IntegerField(null=True, db_column='DusInArea', blank=True) # Field name made lowercase.
    totdus = models.IntegerField(null=True, db_column='TotDUs', blank=True) # Field name made lowercase.
    totalppleinarea = models.IntegerField(null=True, db_column='TotalPpleinArea', blank=True) # Field name made lowercase.
    pcntpop = models.FloatField(null=True, db_column='PcntPop', blank=True) # Field name made lowercase.
    pop = models.IntegerField(null=True, db_column='Pop', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'WImpSrcCkgWSTFCounty'

class Wimpsrcckgwstfslum(models.Model): 
    slumid = models.IntegerField(null=True, db_column='SlumID', blank=True) # Field name made lowercase.
    slumname = models.CharField(max_length=100, db_column='SlumName') # Field name made lowercase.
    dusinsmp = models.IntegerField(null=True, db_column='DUsInSmp', blank=True) # Field name made lowercase.
    smpdus = models.IntegerField(null=True, db_column='SmpDUs', blank=True) # Field name made lowercase.
    pcntdus = models.FloatField(null=True, db_column='pcntDUs', blank=True) # Field name made lowercase.
    dusinarea = models.IntegerField(null=True, db_column='DusInArea', blank=True) # Field name made lowercase.
    totdus = models.IntegerField(null=True, db_column='TotDUs', blank=True) # Field name made lowercase.
    totalppleinarea = models.IntegerField(null=True, db_column='TotalPpleinArea', blank=True) # Field name made lowercase.
    pcntpop = models.FloatField(null=True, db_column='PcntPop', blank=True) # Field name made lowercase.
    pop = models.IntegerField(null=True, db_column='Pop', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'WImpSrcCkgWSTFSlum'

class Wimpsrcckgwstftown(models.Model): 
    townid = models.IntegerField(null=True, db_column='TownID', blank=True) # Field name made lowercase.
    townname = models.CharField(max_length=100, db_column='TownName') # Field name made lowercase.
    dusinsmp = models.IntegerField(null=True, db_column='DUsInSmp', blank=True) # Field name made lowercase.
    smpdus = models.IntegerField(null=True, db_column='SmpDUs', blank=True) # Field name made lowercase.
    pcntdus = models.FloatField(null=True, db_column='pcntDUs', blank=True) # Field name made lowercase.
    dusinarea = models.IntegerField(null=True, db_column='DusInArea', blank=True) # Field name made lowercase.
    totdus = models.IntegerField(null=True, db_column='TotDUs', blank=True) # Field name made lowercase.
    totalppleinarea = models.IntegerField(null=True, db_column='TotalPpleinArea', blank=True) # Field name made lowercase.
    pcntpop = models.FloatField(null=True, db_column='PcntPop', blank=True) # Field name made lowercase.
    pop = models.IntegerField(null=True, db_column='Pop', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'WImpSrcCkgWSTFTown'

class Wimpsrcckgwstfwsp(models.Model): 
    wspid = models.CharField(max_length=100, db_column='WSPID') # Field name made lowercase.
    wspname = models.CharField(max_length=100, db_column='WSPName') # Field name made lowercase.
    dusinsmp = models.IntegerField(null=True, db_column='DUsInSmp', blank=True) # Field name made lowercase.
    smpdus = models.IntegerField(null=True, db_column='SmpDUs', blank=True) # Field name made lowercase.
    pcntdus = models.FloatField(null=True, db_column='pcntDUs', blank=True) # Field name made lowercase.
    dusinarea = models.IntegerField(null=True, db_column='DusInArea', blank=True) # Field name made lowercase.
    totdus = models.IntegerField(null=True, db_column='TotDUs', blank=True) # Field name made lowercase.
    totalppleinarea = models.IntegerField(null=True, db_column='TotalPpleinArea', blank=True) # Field name made lowercase.
    pcntpop = models.FloatField(null=True, db_column='PcntPop', blank=True) # Field name made lowercase.
    pop = models.IntegerField(null=True, db_column='Pop', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'WImpSrcCkgWSTFWSP'

class Wimpsrcdrkwstfcounty(models.Model): 
    countyid = models.IntegerField(null=True, db_column='CountyID', blank=True) # Field name made lowercase.
    countyname = models.CharField(max_length=100, db_column='CountyName') # Field name made lowercase.
    dusinsmp = models.IntegerField(null=True, db_column='DUsInSmp', blank=True) # Field name made lowercase.
    smpdus = models.IntegerField(null=True, db_column='SmpDUs', blank=True) # Field name made lowercase.
    pcntdus = models.FloatField(null=True, db_column='pcntDUs', blank=True) # Field name made lowercase.
    dusinarea = models.IntegerField(null=True, db_column='DusInArea', blank=True) # Field name made lowercase.
    totdus = models.IntegerField(null=True, db_column='TotDUs', blank=True) # Field name made lowercase.
    totalppleinarea = models.IntegerField(null=True, db_column='TotalPpleinArea', blank=True) # Field name made lowercase.
    pcntpop = models.FloatField(null=True, db_column='PcntPop', blank=True) # Field name made lowercase.
    pop = models.IntegerField(null=True, db_column='Pop', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'WImpSrcDrkWSTFCounty'

class Wimpsrcdrkwstfslum(models.Model): 
    slumid = models.IntegerField(null=True, db_column='SlumID', blank=True) # Field name made lowercase.
    slumname = models.CharField(max_length=100, db_column='SlumName') # Field name made lowercase.
    dusinsmp = models.IntegerField(null=True, db_column='DUsInSmp', blank=True) # Field name made lowercase.
    smpdus = models.IntegerField(null=True, db_column='SmpDUs', blank=True) # Field name made lowercase.
    pcntdus = models.FloatField(null=True, db_column='pcntDUs', blank=True) # Field name made lowercase.
    dusinarea = models.IntegerField(null=True, db_column='DusInArea', blank=True) # Field name made lowercase.
    totdus = models.IntegerField(null=True, db_column='TotDUs', blank=True) # Field name made lowercase.
    totalppleinarea = models.IntegerField(null=True, db_column='TotalPpleinArea', blank=True) # Field name made lowercase.
    pcntpop = models.FloatField(null=True, db_column='PcntPop', blank=True) # Field name made lowercase.
    pop = models.IntegerField(null=True, db_column='Pop', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'WImpSrcDrkWSTFSlum'

class Wimpsrcdrkwstfwsp(models.Model): 
    wspid = models.CharField(max_length=100, db_column='WSPID') # Field name made lowercase.
    wspname = models.CharField(max_length=100, db_column='WSPName') # Field name made lowercase.
    dusinsmp = models.IntegerField(null=True, db_column='DUsInSmp', blank=True) # Field name made lowercase.
    smpdus = models.IntegerField(null=True, db_column='SmpDUs', blank=True) # Field name made lowercase.
    pcntdus = models.FloatField(null=True, db_column='pcntDUs', blank=True) # Field name made lowercase.
    dusinarea = models.IntegerField(null=True, db_column='DusInArea', blank=True) # Field name made lowercase.
    totdus = models.IntegerField(null=True, db_column='TotDUs', blank=True) # Field name made lowercase.
    totalppleinarea = models.IntegerField(null=True, db_column='TotalPpleinArea', blank=True) # Field name made lowercase.
    pcntpop = models.FloatField(null=True, db_column='PcntPop', blank=True) # Field name made lowercase.
    pop = models.IntegerField(null=True, db_column='Pop', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'WImpSrcDrkWSTFWSP'

class Wnocompubpsts10D(models.Model): 
    areaid = models.FloatField(null=True, db_column='AreaID', blank=True) # Field name made lowercase.
    areaname = models.CharField(max_length=100, db_column='AreaName') # Field name made lowercase.
    pubwsptaps = models.IntegerField(null=True, db_column='PubWSPTaps', blank=True) # Field name made lowercase.
    comtaps = models.IntegerField(null=True, db_column='ComTaps', blank=True) # Field name made lowercase.
    nopubcomtaps = models.IntegerField(null=True, db_column='NoPubComTaps', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'WNoComPubPsts-10d'

class Woutletscounty(models.Model): 
    countyid = models.IntegerField(null=True, db_column='CountyID', blank=True) # Field name made lowercase.
    countyname = models.CharField(max_length=100, db_column='CountyName') # Field name made lowercase.
    pubwsptaps = models.IntegerField(null=True, db_column='PubWSPTaps', blank=True) # Field name made lowercase.
    comptaps = models.IntegerField(null=True, db_column='CompTaps', blank=True) # Field name made lowercase.
    privtaps = models.IntegerField(null=True, db_column='PrivTaps', blank=True) # Field name made lowercase.
    pubwaterksks = models.IntegerField(null=True, db_column='PubWaterKsks', blank=True) # Field name made lowercase.
    comwaterksks = models.IntegerField(null=True, db_column='ComWaterKsks', blank=True) # Field name made lowercase.
    privwaterksks = models.IntegerField(null=True, db_column='PrivWaterKsks', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'WOutletsCounty'

class Woutletsslum(models.Model): 
    slumid = models.CharField(max_length=100, db_column='SlumID') # Field name made lowercase.
    slumname = models.CharField(max_length=100, db_column='SlumName') # Field name made lowercase.
    pubwsptaps = models.IntegerField(null=True, db_column='PubWSPTaps', blank=True) # Field name made lowercase.
    comptaps = models.IntegerField(null=True, db_column='CompTaps', blank=True) # Field name made lowercase.
    privtaps = models.IntegerField(null=True, db_column='PrivTaps', blank=True) # Field name made lowercase.
    pubwaterksks = models.IntegerField(null=True, db_column='PubWaterKsks', blank=True) # Field name made lowercase.
    comwaterksks = models.IntegerField(null=True, db_column='ComWaterKsks', blank=True) # Field name made lowercase.
    privwaterksks = models.IntegerField(null=True, db_column='PrivWaterKsks', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'WOutletsSlum'

class Woutletstown(models.Model): 
    townid = models.IntegerField(null=True, db_column='TownID', blank=True) # Field name made lowercase.
    townname = models.CharField(max_length=100, db_column='TownName') # Field name made lowercase.
    pubwsptaps = models.IntegerField(null=True, db_column='PubWSPTaps', blank=True) # Field name made lowercase.
    comptaps = models.IntegerField(null=True, db_column='CompTaps', blank=True) # Field name made lowercase.
    privtaps = models.IntegerField(null=True, db_column='PrivTaps', blank=True) # Field name made lowercase.
    pubwaterksks = models.IntegerField(null=True, db_column='PubWaterKsks', blank=True) # Field name made lowercase.
    comwaterksks = models.IntegerField(null=True, db_column='ComWaterKsks', blank=True) # Field name made lowercase.
    privwaterksks = models.IntegerField(null=True, db_column='PrivWaterKsks', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'WOutletsTown'

class Woutletswsp(models.Model): 
    wspid = models.CharField(max_length=100, db_column='WSPID') # Field name made lowercase.
    wspname = models.CharField(max_length=100, db_column='WSPName') # Field name made lowercase.
    pubwsptaps = models.IntegerField(null=True, db_column='PubWSPTaps', blank=True) # Field name made lowercase.
    comptaps = models.IntegerField(null=True, db_column='CompTaps', blank=True) # Field name made lowercase.
    privtaps = models.IntegerField(null=True, db_column='PrivTaps', blank=True) # Field name made lowercase.
    pubwaterksks = models.IntegerField(null=True, db_column='PubWaterKsks', blank=True) # Field name made lowercase.
    comwaterksks = models.IntegerField(null=True, db_column='ComWaterKsks', blank=True) # Field name made lowercase.
    privwaterksks = models.IntegerField(null=True, db_column='PrivWaterKsks', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'WOutletsWSP'

class Wpconcounty(models.Model): 
    countyid = models.IntegerField(null=True, db_column='CountyID', blank=True) # Field name made lowercase.
    countyname = models.CharField(max_length=100, db_column='CountyName') # Field name made lowercase.
    plotconnected = models.CharField(max_length=100, db_column='Plotconnected') # Field name made lowercase.
    dusinsmp = models.IntegerField(null=True, db_column='DUsInSmp', blank=True) # Field name made lowercase.
    smpdus = models.IntegerField(null=True, db_column='SmpDUs', blank=True) # Field name made lowercase.
    pcntdus = models.FloatField(null=True, db_column='pcntDUs', blank=True) # Field name made lowercase.
    dusinarea = models.IntegerField(null=True, db_column='DusInArea', blank=True) # Field name made lowercase.
    totdus = models.IntegerField(null=True, db_column='TotDUs', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'WPConCounty'

class Wpconmetcounty(models.Model): 
    countyid = models.IntegerField(null=True, db_column='CountyID', blank=True) # Field name made lowercase.
    countyname = models.CharField(max_length=100, db_column='CountyName') # Field name made lowercase.
    plotconmet = models.CharField(max_length=100, db_column='PlotconMet') # Field name made lowercase.
    dusinsmp = models.IntegerField(null=True, db_column='DUsInSmp', blank=True) # Field name made lowercase.
    smpdus = models.IntegerField(null=True, db_column='SmpDUs', blank=True) # Field name made lowercase.
    pcntdus = models.FloatField(null=True, db_column='pcntDUs', blank=True) # Field name made lowercase.
    dusinarea = models.IntegerField(null=True, db_column='DusInArea', blank=True) # Field name made lowercase.
    totdus = models.IntegerField(null=True, db_column='TotDUs', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'WPConMetCounty'

class Wpconmetslum(models.Model): 
    slumid = models.IntegerField(null=True, db_column='SlumID', blank=True) # Field name made lowercase.
    slumname = models.CharField(max_length=100, db_column='SlumName') # Field name made lowercase.
    plotconmet = models.CharField(max_length=100, db_column='PlotconMet') # Field name made lowercase.
    dusinsmp = models.IntegerField(null=True, db_column='DUsInSmp', blank=True) # Field name made lowercase.
    smpdus = models.IntegerField(null=True, db_column='SmpDUs', blank=True) # Field name made lowercase.
    pcntdus = models.FloatField(null=True, db_column='pcntDUs', blank=True) # Field name made lowercase.
    dusinarea = models.IntegerField(null=True, db_column='DusInArea', blank=True) # Field name made lowercase.
    totdus = models.IntegerField(null=True, db_column='TotDUs', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'WPConMetSlum'

class Wpconmettown(models.Model): 
    townid = models.IntegerField(null=True, db_column='TownID', blank=True) # Field name made lowercase.
    townname = models.CharField(max_length=100, db_column='TownName') # Field name made lowercase.
    plotconmet = models.CharField(max_length=100, db_column='PlotconMet') # Field name made lowercase.
    dusinsmp = models.IntegerField(null=True, db_column='DUsInSmp', blank=True) # Field name made lowercase.
    smpdus = models.IntegerField(null=True, db_column='SmpDUs', blank=True) # Field name made lowercase.
    pcntdus = models.FloatField(null=True, db_column='pcntDUs', blank=True) # Field name made lowercase.
    dusinarea = models.IntegerField(null=True, db_column='DusInArea', blank=True) # Field name made lowercase.
    totdus = models.IntegerField(null=True, db_column='TotDUs', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'WPConMetTown'

class Wpconmetwsp(models.Model): 
    wspid = models.CharField(max_length=100, db_column='WSPID') # Field name made lowercase.
    wspname = models.CharField(max_length=100, db_column='WSPName') # Field name made lowercase.
    plotconmet = models.CharField(max_length=100, db_column='PlotconMet') # Field name made lowercase.
    dusinsmp = models.IntegerField(null=True, db_column='DUsInSmp', blank=True) # Field name made lowercase.
    smpdus = models.IntegerField(null=True, db_column='SmpDUs', blank=True) # Field name made lowercase.
    pcntdus = models.FloatField(null=True, db_column='pcntDUs', blank=True) # Field name made lowercase.
    dusinarea = models.IntegerField(null=True, db_column='DusInArea', blank=True) # Field name made lowercase.
    totdus = models.IntegerField(null=True, db_column='TotDUs', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'WPConMetWSP'

class Wpconslum(models.Model): 
    slumid = models.IntegerField(null=True, db_column='SlumID', blank=True) # Field name made lowercase.
    slumname = models.CharField(max_length=100, db_column='SlumName') # Field name made lowercase.
    plotconnected = models.CharField(max_length=100, db_column='Plotconnected') # Field name made lowercase.
    dusinsmp = models.IntegerField(null=True, db_column='DUsInSmp', blank=True) # Field name made lowercase.
    smpdus = models.IntegerField(null=True, db_column='SmpDUs', blank=True) # Field name made lowercase.
    pcntdus = models.FloatField(null=True, db_column='pcntDUs', blank=True) # Field name made lowercase.
    dusinarea = models.IntegerField(null=True, db_column='DusInArea', blank=True) # Field name made lowercase.
    totdus = models.IntegerField(null=True, db_column='TotDUs', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'WPConSlum'

class Wpcontown(models.Model): 
    townid = models.IntegerField(null=True, db_column='TownID', blank=True) # Field name made lowercase.
    townname = models.CharField(max_length=100, db_column='TownName') # Field name made lowercase.
    plotconnected = models.CharField(max_length=100, db_column='Plotconnected') # Field name made lowercase.
    dusinsmp = models.IntegerField(null=True, db_column='DUsInSmp', blank=True) # Field name made lowercase.
    smpdus = models.IntegerField(null=True, db_column='SmpDUs', blank=True) # Field name made lowercase.
    pcntdus = models.FloatField(null=True, db_column='pcntDUs', blank=True) # Field name made lowercase.
    dusinarea = models.IntegerField(null=True, db_column='DusInArea', blank=True) # Field name made lowercase.
    totdus = models.IntegerField(null=True, db_column='TotDUs', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'WPConTown'

class Wpconwsp(models.Model): 
    wspid = models.CharField(max_length=100, db_column='wspID') # Field name made lowercase.
    wspname = models.CharField(max_length=100, db_column='wspName') # Field name made lowercase.
    plotconnected = models.CharField(max_length=100, db_column='Plotconnected') # Field name made lowercase.
    dusinsmp = models.IntegerField(null=True, db_column='DUsInSmp', blank=True) # Field name made lowercase.
    smpdus = models.IntegerField(null=True, db_column='SmpDUs', blank=True) # Field name made lowercase.
    pcntdus = models.FloatField(null=True, db_column='pcntDUs', blank=True) # Field name made lowercase.
    dusinarea = models.IntegerField(null=True, db_column='DusInArea', blank=True) # Field name made lowercase.
    totdus = models.IntegerField(null=True, db_column='TotDUs', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'WPConWSP'

class Wpducondisconnected(models.Model): 
    areaid = models.FloatField(null=True, db_column='AreaID', blank=True) # Field name made lowercase.
    areaname = models.CharField(max_length=100, db_column='Areaname') # Field name made lowercase.
    areasmpdus = models.IntegerField(null=True, db_column='AreaSmpDUs', blank=True) # Field name made lowercase.
    dusinsmp = models.IntegerField(null=True, db_column='DUsInSmp', blank=True) # Field name made lowercase.
    pcntdus = models.FloatField(null=True, db_column='pcntDUs', blank=True) # Field name made lowercase.
    dusinarea = models.IntegerField(null=True, db_column='DUsInArea', blank=True) # Field name made lowercase.
    totaldusinarea = models.IntegerField(null=True, db_column='TotalDUsInArea', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'WPDUConDisconnected'

class Wpaydrkdu(models.Model): 
    areaid = models.FloatField(null=True, db_column='AreaID', blank=True) # Field name made lowercase.
    areaname = models.CharField(max_length=100, db_column='Areaname') # Field name made lowercase.
    wpaydrk = models.CharField(max_length=100, db_column='WPaydrk') # Field name made lowercase.
    areasmpdus = models.IntegerField(null=True, db_column='AreaSmpDUs', blank=True) # Field name made lowercase.
    dus = models.IntegerField(null=True, db_column='DUs', blank=True) # Field name made lowercase.
    pcntdus = models.FloatField(null=True, db_column='pcntDUs', blank=True) # Field name made lowercase.
    ndus = models.IntegerField(null=True, db_column='NDus', blank=True) # Field name made lowercase.
    numdu = models.IntegerField(null=True, db_column='numDU', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'WPayDrkDU'

class Wpaynondrkdu(models.Model): 
    areaid = models.FloatField(null=True, db_column='AreaID', blank=True) # Field name made lowercase.
    areaname = models.CharField(max_length=100, db_column='Areaname') # Field name made lowercase.
    wpaydrk = models.CharField(max_length=100, db_column='WPaydrk') # Field name made lowercase.
    areasmpdus = models.IntegerField(null=True, db_column='AreaSmpDUs', blank=True) # Field name made lowercase.
    dus = models.IntegerField(null=True, db_column='DUs', blank=True) # Field name made lowercase.
    pcntdus = models.FloatField(null=True, db_column='pcntDUs', blank=True) # Field name made lowercase.
    ndus = models.IntegerField(null=True, db_column='NDus', blank=True) # Field name made lowercase.
    numdu = models.IntegerField(null=True, db_column='numDU', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'WPayNonDrkDU'

class Wpipedsrcbath(models.Model): 
    areaid = models.FloatField(null=True, db_column='AreaID', blank=True) # Field name made lowercase.
    areaname = models.CharField(max_length=100, db_column='Areaname') # Field name made lowercase.
    areasmpdus = models.IntegerField(null=True, db_column='AreaSmpDUs', blank=True) # Field name made lowercase.
    dusinsmp = models.IntegerField(null=True, db_column='DUsInSmp', blank=True) # Field name made lowercase.
    pcntdus = models.FloatField(null=True, db_column='pcntDUs', blank=True) # Field name made lowercase.
    dusinarea = models.IntegerField(null=True, db_column='DusInArea', blank=True) # Field name made lowercase.
    smppersons = models.IntegerField(null=True, db_column='SmpPersons', blank=True) # Field name made lowercase.
    totalppleinarea = models.IntegerField(null=True, db_column='TotalPpleinArea', blank=True) # Field name made lowercase.
    pcntpple = models.FloatField(null=True, blank=True)
    totaldusinarea = models.IntegerField(null=True, db_column='TotalDUsInArea', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'WPipedSrcBath'

class Wpipedsrcdrk(models.Model): 
    areaid = models.FloatField(null=True, db_column='AreaID', blank=True) # Field name made lowercase.
    areaname = models.CharField(max_length=100, db_column='Areaname') # Field name made lowercase.
    areasmpdus = models.IntegerField(null=True, db_column='AreaSmpDUs', blank=True) # Field name made lowercase.
    dusinsmp = models.IntegerField(null=True, db_column='DUsInSmp', blank=True) # Field name made lowercase.
    pcntdus = models.FloatField(null=True, db_column='pcntDUs', blank=True) # Field name made lowercase.
    dusinarea = models.IntegerField(null=True, db_column='DusInArea', blank=True) # Field name made lowercase.
    smppersons = models.IntegerField(null=True, db_column='SmpPersons', blank=True) # Field name made lowercase.
    totalppleinarea = models.IntegerField(null=True, db_column='TotalPpleinArea', blank=True) # Field name made lowercase.
    pcntpple = models.FloatField(null=True, blank=True)
    totaldusinarea = models.IntegerField(null=True, db_column='TotalDUsInArea', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'WPipedSrcDrk'

class Wpipedsrcdrkavgpay(models.Model): 
    areaid = models.FloatField(null=True, db_column='AreaID', blank=True) # Field name made lowercase.
    areaname = models.CharField(max_length=100, db_column='Areaname') # Field name made lowercase.
    paymthd = models.CharField(max_length=100, db_column='PayMthd') # Field name made lowercase.
    areasmpdus = models.IntegerField(null=True, db_column='AreaSmpDUs', blank=True) # Field name made lowercase.
    dusinsmp = models.IntegerField(null=True, db_column='DUsInSmp', blank=True) # Field name made lowercase.
    pcntdus = models.FloatField(null=True, db_column='pcntDUs', blank=True) # Field name made lowercase.
    dusinarea = models.IntegerField(null=True, db_column='DusInArea', blank=True) # Field name made lowercase.
    smppersons = models.IntegerField(null=True, db_column='SmpPersons', blank=True) # Field name made lowercase.
    totalppleinarea = models.IntegerField(null=True, db_column='TotalPpleinArea', blank=True) # Field name made lowercase.
    pcntpple = models.FloatField(null=True, blank=True)
    totaldusinarea = models.IntegerField(null=True, db_column='TotalDUsInArea', blank=True) # Field name made lowercase.
    avgpaydrk = models.FloatField(null=True, db_column='AvgPayDrk', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'WPipedSrcDrkAvgPay'

class Wpipedsrcdrktrt(models.Model): 
    areaid = models.FloatField(null=True, db_column='AreaID', blank=True) # Field name made lowercase.
    areaname = models.CharField(max_length=100, db_column='Areaname') # Field name made lowercase.
    areasmpdus = models.IntegerField(null=True, db_column='AreaSmpDUs', blank=True) # Field name made lowercase.
    dusinsmp = models.IntegerField(null=True, db_column='DUsInSmp', blank=True) # Field name made lowercase.
    pcntdus = models.FloatField(null=True, db_column='pcntDUs', blank=True) # Field name made lowercase.
    dusinarea = models.IntegerField(null=True, db_column='DusInArea', blank=True) # Field name made lowercase.
    smppersons = models.IntegerField(null=True, db_column='SmpPersons', blank=True) # Field name made lowercase.
    totalppleinarea = models.IntegerField(null=True, db_column='TotalPpleinArea', blank=True) # Field name made lowercase.
    pcntpple = models.FloatField(null=True, blank=True)
    totaldusinarea = models.IntegerField(null=True, db_column='TotalDUsInArea', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'WPipedSrcDrkTrt'

class WplotconmetDu(models.Model): 
    areaid = models.FloatField(null=True, db_column='AreaID', blank=True) # Field name made lowercase.
    areaname = models.CharField(max_length=100, db_column='Areaname') # Field name made lowercase.
    duconmetered = models.CharField(max_length=100, db_column='DUconmetered') # Field name made lowercase.
    dusinsmp = models.IntegerField(null=True, db_column='DUsInSmp', blank=True) # Field name made lowercase.
    pcntdus = models.FloatField(null=True, db_column='pcntDUs', blank=True) # Field name made lowercase.
    dusinarea = models.IntegerField(null=True, db_column='DUsInArea', blank=True) # Field name made lowercase.
    smpduscon = models.IntegerField(null=True, db_column='SmpDUsCon', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'WPlotConMet-DU'

class WplotconnectedDu(models.Model): 
    areaid = models.FloatField(null=True, db_column='AreaID', blank=True) # Field name made lowercase.
    areaname = models.CharField(max_length=100, db_column='Areaname') # Field name made lowercase.
    plotconnected = models.CharField(max_length=100, db_column='Plotconnected') # Field name made lowercase.
    areasmpdus = models.IntegerField(null=True, db_column='AreaSmpDUs', blank=True) # Field name made lowercase.
    dusinsmp = models.FloatField(null=True, db_column='DUsInSmp', blank=True) # Field name made lowercase.
    pcntdus = models.FloatField(null=True, db_column='pcntDUs', blank=True) # Field name made lowercase.
    dusinarea = models.IntegerField(null=True, db_column='DusInArea', blank=True) # Field name made lowercase.
    totaldusinarea = models.IntegerField(null=True, db_column='TotalDUsInArea', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'WPlotConnected-DU'

class Wrespercomtapcounty(models.Model): 
    countyid = models.IntegerField(null=True, db_column='CountyID', blank=True) # Field name made lowercase.
    countyname = models.CharField(max_length=100, db_column='CountyName') # Field name made lowercase.
    totcomtaps = models.IntegerField(null=True, db_column='TotComTaps', blank=True) # Field name made lowercase.
    pplepercomtap = models.CharField(max_length=100, db_column='PplePerComTap') # Field name made lowercase.
    pop = models.IntegerField(null=True, db_column='Pop', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'WResPerComTapCounty'

class Wrespercomtapslum(models.Model): 
    slumid = models.IntegerField(null=True, db_column='SlumID', blank=True) # Field name made lowercase.
    slumname = models.CharField(max_length=100, db_column='SlumName') # Field name made lowercase.
    totcomtaps = models.IntegerField(null=True, db_column='TotComTaps', blank=True) # Field name made lowercase.
    pplepercomtap = models.CharField(max_length=100, db_column='PplePerComTap') # Field name made lowercase.
    pop = models.IntegerField(null=True, db_column='Pop', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'WResPerComTapSlum'

class Wrespercomtaptown(models.Model): 
    townid = models.IntegerField(null=True, db_column='TownID', blank=True) # Field name made lowercase.
    townname = models.CharField(max_length=100, db_column='TownName') # Field name made lowercase.
    totcomtaps = models.IntegerField(null=True, db_column='TotComTaps', blank=True) # Field name made lowercase.
    pplepercomtap = models.CharField(max_length=100, db_column='PplePerComTap') # Field name made lowercase.
    pop = models.IntegerField(null=True, db_column='Pop', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'WResPerComTapTown'

class Wrespercomtapwsp(models.Model): 
    wspid = models.CharField(max_length=100, db_column='WSPID') # Field name made lowercase.
    wspname = models.CharField(max_length=100, db_column='WSPName') # Field name made lowercase.
    totcomtaps = models.IntegerField(null=True, db_column='TotComTaps', blank=True) # Field name made lowercase.
    pplepercomtap = models.CharField(max_length=100, db_column='PplePerComTap') # Field name made lowercase.
    pop = models.IntegerField(null=True, db_column='Pop', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'WResPerComTapWSP'

class Wresperpubcomkskscounty(models.Model): 
    countyid = models.IntegerField(null=True, db_column='CountyID', blank=True) # Field name made lowercase.
    countyname = models.CharField(max_length=100, db_column='CountyName') # Field name made lowercase.
    totpubcomksks = models.IntegerField(null=True, db_column='TotPubComKsks', blank=True) # Field name made lowercase.
    ppleperpubcomtap = models.CharField(max_length=36, db_column='PplePerPubComTap') # Field name made lowercase.
    pop = models.IntegerField(null=True, db_column='Pop', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'WResPerPubComKsksCounty'

class Wresperpubcomksksslum(models.Model): 
    slumid = models.IntegerField(null=True, db_column='SlumID', blank=True) # Field name made lowercase.
    slumname = models.CharField(max_length=100, db_column='SlumName') # Field name made lowercase.
    totpubcomksks = models.IntegerField(null=True, db_column='TotPubComKsks', blank=True) # Field name made lowercase.
    ppleperpubcomtap = models.CharField(max_length=36, db_column='PplePerPubComTap') # Field name made lowercase.
    pop = models.IntegerField(null=True, db_column='Pop', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'WResPerPubComKsksSlum'

class Wresperpubcomkskstown(models.Model): 
    townid = models.IntegerField(null=True, db_column='TownID', blank=True) # Field name made lowercase.
    townname = models.CharField(max_length=100, db_column='TownName') # Field name made lowercase.
    totpubcomksks = models.IntegerField(null=True, db_column='TotPubComKsks', blank=True) # Field name made lowercase.
    ppleperpubcomtap = models.CharField(max_length=36, db_column='PplePerPubComTap') # Field name made lowercase.
    pop = models.IntegerField(null=True, db_column='Pop', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'WResPerPubComKsksTown'

class Wresperpubcomkskswsp(models.Model): 
    wspid = models.CharField(max_length=100, db_column='WSPID') # Field name made lowercase.
    wspname = models.CharField(max_length=100, db_column='WSPName') # Field name made lowercase.
    totpubcomksks = models.IntegerField(null=True, db_column='TotPubComKsks', blank=True) # Field name made lowercase.
    ppleperpubcomtap = models.CharField(max_length=36, db_column='PplePerPubComTap') # Field name made lowercase.
    pop = models.IntegerField(null=True, db_column='Pop', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'WResPerPubComKsksWSP'

class Wresperpubwspcomtapscounty(models.Model): 
    countyid = models.IntegerField(null=True, db_column='CountyID', blank=True) # Field name made lowercase.
    countyname = models.CharField(max_length=100, db_column='CountyName') # Field name made lowercase.
    totpubcomtaps = models.IntegerField(null=True, db_column='TotPubComTaps', blank=True) # Field name made lowercase.
    ppleperpubcomtap = models.CharField(max_length=34, db_column='PplePerPubComTap') # Field name made lowercase.
    pop = models.IntegerField(null=True, db_column='Pop', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'WResPerPubWSPComTapsCounty'

class Wresperpubwspcomtapsslum(models.Model): 
    slumid = models.IntegerField(null=True, db_column='SlumID', blank=True) # Field name made lowercase.
    slumname = models.CharField(max_length=100, db_column='SlumName') # Field name made lowercase.
    totpubcomtaps = models.IntegerField(null=True, db_column='TotPubComTaps', blank=True) # Field name made lowercase.
    ppleperpubcomtap = models.CharField(max_length=34, db_column='PplePerPubComTap') # Field name made lowercase.
    pop = models.IntegerField(null=True, db_column='Pop', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'WResPerPubWSPComTapsSlum'

class Wresperpubwspcomtapstown(models.Model): 
    townid = models.IntegerField(null=True, db_column='TownID', blank=True) # Field name made lowercase.
    townname = models.CharField(max_length=100, db_column='TownName') # Field name made lowercase.
    totpubcomtaps = models.IntegerField(null=True, db_column='TotPubComTaps', blank=True) # Field name made lowercase.
    ppleperpubcomtap = models.CharField(max_length=34, db_column='PplePerPubComTap') # Field name made lowercase.
    pop = models.IntegerField(null=True, db_column='Pop', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'WResPerPubWSPComTapsTown'

class Wresperpubwspcomtapswsp(models.Model): 
    wspid = models.CharField(max_length=100, db_column='WSPID') # Field name made lowercase.
    wspname = models.CharField(max_length=100, db_column='WSPName') # Field name made lowercase.
    totpubcomtaps = models.IntegerField(null=True, db_column='TotPubComTaps', blank=True) # Field name made lowercase.
    ppleperpubcomtap = models.CharField(max_length=34, db_column='PplePerPubComTap') # Field name made lowercase.
    pop = models.IntegerField(null=True, db_column='Pop', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'WResPerPubWSPComTapsWSP'

class Wresperpubwsptapcounty(models.Model): 
    countyid = models.IntegerField(null=True, db_column='CountyID', blank=True) # Field name made lowercase.
    countyname = models.CharField(max_length=100, db_column='CountyName') # Field name made lowercase.
    tottaps = models.IntegerField(null=True, db_column='TotTaps', blank=True) # Field name made lowercase.
    ppleperpubtap = models.CharField(max_length=100, db_column='PplePerPubTap') # Field name made lowercase.
    pop = models.IntegerField(null=True, db_column='Pop', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'WResPerPubWSPTapCounty'

class Wresperpubwsptapslum(models.Model): 
    slumid = models.IntegerField(null=True, db_column='SlumID', blank=True) # Field name made lowercase.
    slumname = models.CharField(max_length=100, db_column='SlumName') # Field name made lowercase.
    tottaps = models.IntegerField(null=True, db_column='TotTaps', blank=True) # Field name made lowercase.
    ppleperpubtap = models.CharField(max_length=100, db_column='PplePerPubTap') # Field name made lowercase.
    pop = models.IntegerField(null=True, db_column='Pop', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'WResPerPubWSPTapSlum'

class Wresperpubwsptaptown(models.Model): 
    townid = models.IntegerField(null=True, db_column='TownID', blank=True) # Field name made lowercase.
    townname = models.CharField(max_length=100, db_column='TownName') # Field name made lowercase.
    tottaps = models.IntegerField(null=True, db_column='TotTaps', blank=True) # Field name made lowercase.
    ppleperpubtap = models.CharField(max_length=100, db_column='PplePerPubTap') # Field name made lowercase.
    pop = models.IntegerField(null=True, db_column='Pop', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'WResPerPubWSPTapTown'

class Wresperpubwsptapwsp(models.Model): 
    wspid = models.CharField(max_length=100, db_column='WSPID') # Field name made lowercase.
    wspname = models.CharField(max_length=100, db_column='WSPName') # Field name made lowercase.
    tottaps = models.IntegerField(null=True, db_column='TotTaps', blank=True) # Field name made lowercase.
    ppleperpubtap = models.CharField(max_length=100, db_column='PplePerPubTap') # Field name made lowercase.
    pop = models.IntegerField(null=True, db_column='Pop', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'WResPerPubWSPTapWSP'

class Wresperwspkskcounty(models.Model): 
    countyid = models.IntegerField(null=True, db_column='CountyID', blank=True) # Field name made lowercase.
    countyname = models.CharField(max_length=100, db_column='CountyName') # Field name made lowercase.
    totksks = models.IntegerField(null=True, db_column='TotKsks', blank=True) # Field name made lowercase.
    ppleperkiosk = models.CharField(max_length=100, db_column='PplePerKiosk') # Field name made lowercase.
    pop = models.IntegerField(null=True, db_column='Pop', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'WResPerWSPKskCounty'

class Wresperwspkskslum(models.Model): 
    slumid = models.IntegerField(null=True, db_column='SlumID', blank=True) # Field name made lowercase.
    slumname = models.CharField(max_length=100, db_column='SlumName') # Field name made lowercase.
    totksks = models.IntegerField(null=True, db_column='TotKsks', blank=True) # Field name made lowercase.
    ppleperkiosk = models.CharField(max_length=100, db_column='PplePerKiosk') # Field name made lowercase.
    pop = models.IntegerField(null=True, db_column='Pop', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'WResPerWSPKskSlum'

class Wresperwspksktown(models.Model): 
    townid = models.IntegerField(null=True, db_column='TownID', blank=True) # Field name made lowercase.
    townname = models.CharField(max_length=100, db_column='TownName') # Field name made lowercase.
    totksks = models.IntegerField(null=True, db_column='TotKsks', blank=True) # Field name made lowercase.
    ppleperkiosk = models.CharField(max_length=100, db_column='PplePerKiosk') # Field name made lowercase.
    pop = models.IntegerField(null=True, db_column='Pop', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'WResPerWSPKskTown'

class Wresperwspkskwsp(models.Model): 
    wspid = models.CharField(max_length=100, db_column='WSPID') # Field name made lowercase.
    wspname = models.CharField(max_length=100, db_column='WSPName') # Field name made lowercase.
    totksks = models.IntegerField(null=True, db_column='TotKsks', blank=True) # Field name made lowercase.
    ppleperkiosk = models.CharField(max_length=100, db_column='PplePerKiosk') # Field name made lowercase.
    pop = models.IntegerField(null=True, db_column='Pop', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'WResPerWSPKskWSP'

class Wrespercompubpost10D(models.Model): 
    area = models.FloatField(null=True, db_column='Area', blank=True) # Field name made lowercase.
    areaname = models.CharField(max_length=100, db_column='Areaname') # Field name made lowercase.
    areapop = models.IntegerField(null=True, db_column='AreaPop', blank=True) # Field name made lowercase.
    nfacilities = models.IntegerField(null=True, db_column='NFacilities', blank=True) # Field name made lowercase.
    ppleperfacility = models.CharField(max_length=33, db_column='PplePerFacility') # Field name made lowercase.
    class Meta:
        db_table = 'WResperComPubPost-10d'

class Wsrcbathpipedcounty(models.Model): 
    countyid = models.IntegerField(null=True, db_column='CountyID', blank=True) # Field name made lowercase.
    countyname = models.CharField(max_length=100, db_column='CountyName') # Field name made lowercase.
    dusinsmp = models.IntegerField(null=True, db_column='DUsInSmp', blank=True) # Field name made lowercase.
    smpdus = models.IntegerField(null=True, db_column='SmpDUs', blank=True) # Field name made lowercase.
    pcntdus = models.FloatField(null=True, db_column='pcntDUs', blank=True) # Field name made lowercase.
    dusinarea = models.IntegerField(null=True, db_column='DusInArea', blank=True) # Field name made lowercase.
    totdus = models.IntegerField(null=True, db_column='TotDUs', blank=True) # Field name made lowercase.
    totalppleinarea = models.IntegerField(null=True, db_column='TotalPpleinArea', blank=True) # Field name made lowercase.
    pcntpop = models.FloatField(null=True, db_column='PcntPop', blank=True) # Field name made lowercase.
    pop = models.IntegerField(null=True, db_column='Pop', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'WSrcBathPipedCounty'

class Wsrcbathpipedslum(models.Model): 
    slumid = models.IntegerField(null=True, db_column='SlumID', blank=True) # Field name made lowercase.
    slumname = models.CharField(max_length=100, db_column='SlumName') # Field name made lowercase.
    dusinsmp = models.IntegerField(null=True, db_column='DUsInSmp', blank=True) # Field name made lowercase.
    smpdus = models.IntegerField(null=True, db_column='SmpDUs', blank=True) # Field name made lowercase.
    pcntdus = models.FloatField(null=True, db_column='pcntDUs', blank=True) # Field name made lowercase.
    dusinarea = models.IntegerField(null=True, db_column='DusInArea', blank=True) # Field name made lowercase.
    totdus = models.IntegerField(null=True, db_column='TotDUs', blank=True) # Field name made lowercase.
    totalppleinarea = models.IntegerField(null=True, db_column='TotalPpleinArea', blank=True) # Field name made lowercase.
    pcntpop = models.FloatField(null=True, db_column='PcntPop', blank=True) # Field name made lowercase.
    pop = models.IntegerField(null=True, db_column='Pop', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'WSrcBathPipedSlum'

class Wsrcbathpipedtown(models.Model): 
    townid = models.IntegerField(null=True, db_column='TownID', blank=True) # Field name made lowercase.
    townname = models.CharField(max_length=100, db_column='TownName') # Field name made lowercase.
    dusinsmp = models.IntegerField(null=True, db_column='DUsInSmp', blank=True) # Field name made lowercase.
    smpdus = models.IntegerField(null=True, db_column='SmpDUs', blank=True) # Field name made lowercase.
    pcntdus = models.FloatField(null=True, db_column='pcntDUs', blank=True) # Field name made lowercase.
    dusinarea = models.IntegerField(null=True, db_column='DusInArea', blank=True) # Field name made lowercase.
    totdus = models.IntegerField(null=True, db_column='TotDUs', blank=True) # Field name made lowercase.
    totalppleinarea = models.IntegerField(null=True, db_column='TotalPpleinArea', blank=True) # Field name made lowercase.
    pcntpop = models.FloatField(null=True, db_column='PcntPop', blank=True) # Field name made lowercase.
    pop = models.IntegerField(null=True, db_column='Pop', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'WSrcBathPipedTown'

class Wsrcbathpipedwsp(models.Model): 
    wspid = models.CharField(max_length=100, db_column='WspID') # Field name made lowercase.
    wspname = models.CharField(max_length=100, db_column='WspName') # Field name made lowercase.
    dusinsmp = models.IntegerField(null=True, db_column='DUsInSmp', blank=True) # Field name made lowercase.
    smpdus = models.IntegerField(null=True, db_column='SmpDUs', blank=True) # Field name made lowercase.
    pcntdus = models.FloatField(null=True, db_column='pcntDUs', blank=True) # Field name made lowercase.
    dusinarea = models.IntegerField(null=True, db_column='DusInArea', blank=True) # Field name made lowercase.
    totdus = models.IntegerField(null=True, db_column='TotDUs', blank=True) # Field name made lowercase.
    totalppleinarea = models.IntegerField(null=True, db_column='TotalPpleinArea', blank=True) # Field name made lowercase.
    pcntpop = models.FloatField(null=True, db_column='PcntPop', blank=True) # Field name made lowercase.
    pop = models.IntegerField(null=True, db_column='Pop', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'WSrcBathPipedWSP'

class Wsrcckg33County(models.Model): 
    countyid = models.IntegerField(null=True, db_column='CountyID', blank=True) # Field name made lowercase.
    countyname = models.CharField(max_length=100, db_column='CountyName') # Field name made lowercase.
    ckgwatersrc = models.CharField(max_length=100, db_column='CkgWaterSrc') # Field name made lowercase.
    smpsrc = models.IntegerField(null=True, db_column='SmpSrc', blank=True) # Field name made lowercase.
    smpdus = models.IntegerField(null=True, db_column='SmpDUs', blank=True) # Field name made lowercase.
    totdus = models.IntegerField(null=True, db_column='TotDUs', blank=True) # Field name made lowercase.
    pcntusingsrc = models.FloatField(null=True, db_column='PcntUsingSrc', blank=True) # Field name made lowercase.
    nusingsrc = models.IntegerField(null=True, db_column='NUsingSrc', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'WSrcCkg33County'

class Wsrcdrkbhpmpcounty(models.Model): 
    countyid = models.IntegerField(null=True, db_column='CountyID', blank=True) # Field name made lowercase.
    countyname = models.CharField(max_length=100, db_column='CountyName') # Field name made lowercase.
    dusinsmp = models.IntegerField(null=True, db_column='DUsInSmp', blank=True) # Field name made lowercase.
    smpdus = models.IntegerField(null=True, db_column='SmpDUs', blank=True) # Field name made lowercase.
    pcntdus = models.FloatField(null=True, db_column='pcntDUs', blank=True) # Field name made lowercase.
    dusinarea = models.IntegerField(null=True, db_column='DusInArea', blank=True) # Field name made lowercase.
    totdus = models.IntegerField(null=True, db_column='TotDUs', blank=True) # Field name made lowercase.
    totalppleinarea = models.IntegerField(null=True, db_column='TotalPpleinArea', blank=True) # Field name made lowercase.
    pcntpop = models.FloatField(null=True, db_column='PcntPop', blank=True) # Field name made lowercase.
    pop = models.IntegerField(null=True, db_column='Pop', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'WSrcDrkBhPmpCounty'

class Wsrcdrkbhpmpslum(models.Model): 
    slumid = models.IntegerField(null=True, db_column='SlumID', blank=True) # Field name made lowercase.
    slumname = models.CharField(max_length=100, db_column='SlumName') # Field name made lowercase.
    dusinsmp = models.IntegerField(null=True, db_column='DUsInSmp', blank=True) # Field name made lowercase.
    smpdus = models.IntegerField(null=True, db_column='SmpDUs', blank=True) # Field name made lowercase.
    pcntdus = models.FloatField(null=True, db_column='pcntDUs', blank=True) # Field name made lowercase.
    dusinarea = models.IntegerField(null=True, db_column='DusInArea', blank=True) # Field name made lowercase.
    totdus = models.IntegerField(null=True, db_column='TotDUs', blank=True) # Field name made lowercase.
    totalppleinarea = models.IntegerField(null=True, db_column='TotalPpleinArea', blank=True) # Field name made lowercase.
    pcntpop = models.FloatField(null=True, db_column='PcntPop', blank=True) # Field name made lowercase.
    pop = models.IntegerField(null=True, db_column='Pop', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'WSrcDrkBhPmpSlum'

class Wsrcdrkbhpmptown(models.Model): 
    townid = models.IntegerField(null=True, db_column='TownID', blank=True) # Field name made lowercase.
    townname = models.CharField(max_length=100, db_column='TownName') # Field name made lowercase.
    dusinsmp = models.IntegerField(null=True, db_column='DUsInSmp', blank=True) # Field name made lowercase.
    smpdus = models.IntegerField(null=True, db_column='SmpDUs', blank=True) # Field name made lowercase.
    pcntdus = models.FloatField(null=True, db_column='pcntDUs', blank=True) # Field name made lowercase.
    dusinarea = models.IntegerField(null=True, db_column='DusInArea', blank=True) # Field name made lowercase.
    totdus = models.IntegerField(null=True, db_column='TotDUs', blank=True) # Field name made lowercase.
    totalppleinarea = models.IntegerField(null=True, db_column='TotalPpleinArea', blank=True) # Field name made lowercase.
    pcntpop = models.FloatField(null=True, db_column='PcntPop', blank=True) # Field name made lowercase.
    pop = models.IntegerField(null=True, db_column='Pop', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'WSrcDrkBhPmpTown'

class Wsrcdrkbhpmpwsp(models.Model): 
    wspid = models.CharField(max_length=100, db_column='WspID') # Field name made lowercase.
    wspname = models.CharField(max_length=45, db_column='WspName') # Field name made lowercase.
    dusinsmp = models.IntegerField(null=True, db_column='DUsInSmp', blank=True) # Field name made lowercase.
    smpdus = models.IntegerField(null=True, db_column='SmpDUs', blank=True) # Field name made lowercase.
    pcntdus = models.FloatField(null=True, db_column='pcntDUs', blank=True) # Field name made lowercase.
    dusinarea = models.IntegerField(null=True, db_column='DusInArea', blank=True) # Field name made lowercase.
    totdus = models.IntegerField(null=True, db_column='TotDUs', blank=True) # Field name made lowercase.
    totalppleinarea = models.IntegerField(null=True, db_column='TotalPpleinArea', blank=True) # Field name made lowercase.
    pcntpop = models.FloatField(null=True, db_column='PcntPop', blank=True) # Field name made lowercase.
    pop = models.IntegerField(null=True, db_column='Pop', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'WSrcDrkBhPmpWSP'

class Wsrcdrkksk(models.Model): 
    areaid = models.FloatField(null=True, db_column='AreaID', blank=True) # Field name made lowercase.
    areaname = models.CharField(max_length=100, db_column='Areaname') # Field name made lowercase.
    areasmpdus = models.IntegerField(null=True, db_column='AreaSmpDUs', blank=True) # Field name made lowercase.
    dusinsmp = models.IntegerField(null=True, db_column='DUsInSmp', blank=True) # Field name made lowercase.
    pcntdus = models.FloatField(null=True, db_column='pcntDUs', blank=True) # Field name made lowercase.
    dusinarea = models.IntegerField(null=True, db_column='DusInArea', blank=True) # Field name made lowercase.
    smppersons = models.IntegerField(null=True, db_column='SmpPersons', blank=True) # Field name made lowercase.
    totalppleinarea = models.IntegerField(null=True, db_column='TotalPpleinArea', blank=True) # Field name made lowercase.
    pcntpple = models.FloatField(null=True, blank=True)
    totaldusinarea = models.IntegerField(null=True, db_column='TotalDUsInArea', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'WSrcDrkKsk'

class Wsrcdrkleakcounty(models.Model): 
    countyid = models.CharField(max_length=100, db_column='CountyID') # Field name made lowercase.
    countyname = models.CharField(max_length=100, db_column='CountyName') # Field name made lowercase.
    dusinsmp = models.CharField(max_length=100, db_column='DUsInSmp') # Field name made lowercase.
    smpdus = models.CharField(max_length=100, db_column='SmpDUs') # Field name made lowercase.
    pcntdus = models.CharField(max_length=100, db_column='pcntDUs') # Field name made lowercase.
    dusinarea = models.CharField(max_length=100, db_column='DusInArea') # Field name made lowercase.
    totdus = models.CharField(max_length=100, db_column='TotDUs') # Field name made lowercase.
    totalppleinarea = models.CharField(max_length=100, db_column='TotalPpleinArea') # Field name made lowercase.
    pcntpop = models.CharField(max_length=100, db_column='PcntPop') # Field name made lowercase.
    pop = models.CharField(max_length=100, db_column='Pop') # Field name made lowercase.
    class Meta:
        db_table = 'WSrcDrkLeakCounty'

class Wsrcdrkleakslum(models.Model): 
    slumid = models.CharField(max_length=100, db_column='SlumID') # Field name made lowercase.
    slumname = models.CharField(max_length=100, db_column='SlumName') # Field name made lowercase.
    dusinsmp = models.CharField(max_length=100, db_column='DUsInSmp') # Field name made lowercase.
    smpdus = models.CharField(max_length=100, db_column='SmpDUs') # Field name made lowercase.
    pcntdus = models.CharField(max_length=100, db_column='pcntDUs') # Field name made lowercase.
    dusinarea = models.CharField(max_length=100, db_column='DusInArea') # Field name made lowercase.
    totdus = models.CharField(max_length=100, db_column='TotDUs') # Field name made lowercase.
    totalppleinarea = models.CharField(max_length=100, db_column='TotalPpleinArea') # Field name made lowercase.
    pcntpop = models.CharField(max_length=100, db_column='PcntPop') # Field name made lowercase.
    pop = models.CharField(max_length=100, db_column='Pop') # Field name made lowercase.
    class Meta:
        db_table = 'WSrcDrkLeakSlum'

class Wsrcdrkleaktown(models.Model): 
    townid = models.CharField(max_length=100, db_column='TownID') # Field name made lowercase.
    townname = models.CharField(max_length=100, db_column='TownName') # Field name made lowercase.
    dusinsmp = models.CharField(max_length=100, db_column='DUsInSmp') # Field name made lowercase.
    smpdus = models.CharField(max_length=100, db_column='SmpDUs') # Field name made lowercase.
    pcntdus = models.CharField(max_length=100, db_column='pcntDUs') # Field name made lowercase.
    dusinarea = models.CharField(max_length=100, db_column='DusInArea') # Field name made lowercase.
    totdus = models.CharField(max_length=100, db_column='TotDUs') # Field name made lowercase.
    totalppleinarea = models.CharField(max_length=100, db_column='TotalPpleinArea') # Field name made lowercase.
    pcntpop = models.CharField(max_length=100, db_column='PcntPop') # Field name made lowercase.
    pop = models.CharField(max_length=100, db_column='Pop') # Field name made lowercase.
    class Meta:
        db_table = 'WSrcDrkLeakTown'

class Wsrcdrkleakwsp(models.Model): 
    wspid = models.CharField(max_length=100, db_column='WSPID') # Field name made lowercase.
    wspname = models.CharField(max_length=100, db_column='WSPName') # Field name made lowercase.
    dusinsmp = models.CharField(max_length=100, db_column='DUsInSmp') # Field name made lowercase.
    smpdus = models.CharField(max_length=100, db_column='SmpDUs') # Field name made lowercase.
    pcntdus = models.CharField(max_length=100, db_column='pcntDUs') # Field name made lowercase.
    dusinarea = models.CharField(max_length=100, db_column='DusInArea') # Field name made lowercase.
    totdus = models.CharField(max_length=100, db_column='TotDUs') # Field name made lowercase.
    totalppleinarea = models.CharField(max_length=100, db_column='TotalPpleinArea') # Field name made lowercase.
    pcntpop = models.CharField(max_length=100, db_column='PcntPop') # Field name made lowercase.
    pop = models.CharField(max_length=100, db_column='Pop') # Field name made lowercase.
    class Meta:
        db_table = 'WSrcDrkLeakWSP'

class Wsrcdrkspringcounty(models.Model): 
    countyid = models.IntegerField(null=True, db_column='CountyID', blank=True) # Field name made lowercase.
    countyname = models.CharField(max_length=100, db_column='CountyName') # Field name made lowercase.
    dusinsmp = models.IntegerField(null=True, db_column='DUsInSmp', blank=True) # Field name made lowercase.
    smpdus = models.IntegerField(null=True, db_column='SmpDUs', blank=True) # Field name made lowercase.
    pcntdus = models.FloatField(null=True, db_column='pcntDUs', blank=True) # Field name made lowercase.
    dusinarea = models.IntegerField(null=True, db_column='DusInArea', blank=True) # Field name made lowercase.
    totdus = models.IntegerField(null=True, db_column='TotDUs', blank=True) # Field name made lowercase.
    totalppleinarea = models.IntegerField(null=True, db_column='TotalPpleinArea', blank=True) # Field name made lowercase.
    pcntpop = models.FloatField(null=True, db_column='PcntPop', blank=True) # Field name made lowercase.
    pop = models.IntegerField(null=True, db_column='Pop', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'WSrcDrkSpringCounty'

class Wsrcdrkspringslum(models.Model): 
    slumid = models.IntegerField(null=True, db_column='SlumID', blank=True) # Field name made lowercase.
    slumname = models.CharField(max_length=100, db_column='SlumName') # Field name made lowercase.
    dusinsmp = models.IntegerField(null=True, db_column='DUsInSmp', blank=True) # Field name made lowercase.
    smpdus = models.IntegerField(null=True, db_column='SmpDUs', blank=True) # Field name made lowercase.
    pcntdus = models.FloatField(null=True, db_column='pcntDUs', blank=True) # Field name made lowercase.
    dusinarea = models.IntegerField(null=True, db_column='DusInArea', blank=True) # Field name made lowercase.
    totdus = models.IntegerField(null=True, db_column='TotDUs', blank=True) # Field name made lowercase.
    totalppleinarea = models.IntegerField(null=True, db_column='TotalPpleinArea', blank=True) # Field name made lowercase.
    pcntpop = models.FloatField(null=True, db_column='PcntPop', blank=True) # Field name made lowercase.
    pop = models.IntegerField(null=True, db_column='Pop', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'WSrcDrkSpringSlum'

class Wsrcdrkspringtown(models.Model): 
    townid = models.IntegerField(null=True, db_column='TownID', blank=True) # Field name made lowercase.
    townname = models.CharField(max_length=100, db_column='TownName') # Field name made lowercase.
    dusinsmp = models.IntegerField(null=True, db_column='DUsInSmp', blank=True) # Field name made lowercase.
    smpdus = models.IntegerField(null=True, db_column='SmpDUs', blank=True) # Field name made lowercase.
    pcntdus = models.FloatField(null=True, db_column='pcntDUs', blank=True) # Field name made lowercase.
    dusinarea = models.IntegerField(null=True, db_column='DusInArea', blank=True) # Field name made lowercase.
    totdus = models.IntegerField(null=True, db_column='TotDUs', blank=True) # Field name made lowercase.
    totalppleinarea = models.IntegerField(null=True, db_column='TotalPpleinArea', blank=True) # Field name made lowercase.
    pcntpop = models.FloatField(null=True, db_column='PcntPop', blank=True) # Field name made lowercase.
    pop = models.IntegerField(null=True, db_column='Pop', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'WSrcDrkSpringTown'

class Wsrcdrkspringwsp(models.Model): 
    wspid = models.CharField(max_length=100, db_column='WSPID') # Field name made lowercase.
    wspname = models.CharField(max_length=100, db_column='WSPName') # Field name made lowercase.
    dusinsmp = models.IntegerField(null=True, db_column='DUsInSmp', blank=True) # Field name made lowercase.
    smpdus = models.IntegerField(null=True, db_column='SmpDUs', blank=True) # Field name made lowercase.
    pcntdus = models.FloatField(null=True, db_column='pcntDUs', blank=True) # Field name made lowercase.
    dusinarea = models.IntegerField(null=True, db_column='DusInArea', blank=True) # Field name made lowercase.
    totdus = models.IntegerField(null=True, db_column='TotDUs', blank=True) # Field name made lowercase.
    totalppleinarea = models.IntegerField(null=True, db_column='TotalPpleinArea', blank=True) # Field name made lowercase.
    pcntpop = models.FloatField(null=True, db_column='PcntPop', blank=True) # Field name made lowercase.
    pop = models.IntegerField(null=True, db_column='Pop', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'WSrcDrkSpringWSP'

class Wsrcdrkvendorcounty(models.Model): 
    countyid = models.IntegerField(null=True, db_column='CountyID', blank=True) # Field name made lowercase.
    countyname = models.CharField(max_length=100, db_column='CountyName') # Field name made lowercase.
    dusinsmp = models.IntegerField(null=True, db_column='DUsInSmp', blank=True) # Field name made lowercase.
    smpdus = models.IntegerField(null=True, db_column='SmpDUs', blank=True) # Field name made lowercase.
    pcntdus = models.FloatField(null=True, db_column='pcntDUs', blank=True) # Field name made lowercase.
    dusinarea = models.IntegerField(null=True, db_column='DusInArea', blank=True) # Field name made lowercase.
    totdus = models.IntegerField(null=True, db_column='TotDUs', blank=True) # Field name made lowercase.
    totalppleinarea = models.IntegerField(null=True, db_column='TotalPpleinArea', blank=True) # Field name made lowercase.
    pcntpop = models.FloatField(null=True, db_column='PcntPop', blank=True) # Field name made lowercase.
    pop = models.IntegerField(null=True, db_column='Pop', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'WSrcDrkVendorCounty'

class Wsrcdrkvendorslum(models.Model): 
    slumid = models.IntegerField(null=True, db_column='SlumID', blank=True) # Field name made lowercase.
    slumname = models.CharField(max_length=100, db_column='SlumName') # Field name made lowercase.
    dusinsmp = models.IntegerField(null=True, db_column='DUsInSmp', blank=True) # Field name made lowercase.
    smpdus = models.IntegerField(null=True, db_column='SmpDUs', blank=True) # Field name made lowercase.
    pcntdus = models.FloatField(null=True, db_column='pcntDUs', blank=True) # Field name made lowercase.
    dusinarea = models.IntegerField(null=True, db_column='DusInArea', blank=True) # Field name made lowercase.
    totdus = models.IntegerField(null=True, db_column='TotDUs', blank=True) # Field name made lowercase.
    totalppleinarea = models.IntegerField(null=True, db_column='TotalPpleinArea', blank=True) # Field name made lowercase.
    pcntpop = models.FloatField(null=True, db_column='PcntPop', blank=True) # Field name made lowercase.
    pop = models.IntegerField(null=True, db_column='Pop', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'WSrcDrkVendorSlum'

class Wsrcdrkvendortown(models.Model): 
    townid = models.IntegerField(null=True, db_column='TownID', blank=True) # Field name made lowercase.
    townname = models.CharField(max_length=100, db_column='TownName') # Field name made lowercase.
    dusinsmp = models.IntegerField(null=True, db_column='DUsInSmp', blank=True) # Field name made lowercase.
    smpdus = models.IntegerField(null=True, db_column='SmpDUs', blank=True) # Field name made lowercase.
    pcntdus = models.FloatField(null=True, db_column='pcntDUs', blank=True) # Field name made lowercase.
    dusinarea = models.IntegerField(null=True, db_column='DusInArea', blank=True) # Field name made lowercase.
    totdus = models.IntegerField(null=True, db_column='TotDUs', blank=True) # Field name made lowercase.
    totalppleinarea = models.IntegerField(null=True, db_column='TotalPpleinArea', blank=True) # Field name made lowercase.
    pcntpop = models.FloatField(null=True, db_column='PcntPop', blank=True) # Field name made lowercase.
    pop = models.IntegerField(null=True, db_column='Pop', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'WSrcDrkVendorTown'

class Wsrcdrkvendorwsp(models.Model): 
    wspid = models.CharField(max_length=100, db_column='WSPID') # Field name made lowercase.
    wspname = models.CharField(max_length=100, db_column='WSPName') # Field name made lowercase.
    dusinsmp = models.IntegerField(null=True, db_column='DUsInSmp', blank=True) # Field name made lowercase.
    smpdus = models.IntegerField(null=True, db_column='SmpDUs', blank=True) # Field name made lowercase.
    pcntdus = models.FloatField(null=True, db_column='pcntDUs', blank=True) # Field name made lowercase.
    dusinarea = models.IntegerField(null=True, db_column='DusInArea', blank=True) # Field name made lowercase.
    totdus = models.IntegerField(null=True, db_column='TotDUs', blank=True) # Field name made lowercase.
    totalppleinarea = models.IntegerField(null=True, db_column='TotalPpleinArea', blank=True) # Field name made lowercase.
    pcntpop = models.FloatField(null=True, db_column='PcntPop', blank=True) # Field name made lowercase.
    pop = models.IntegerField(null=True, db_column='Pop', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'WSrcDrkVendorWSP'

class Wsrcdrkwellscounty(models.Model): 
    countyid = models.IntegerField(null=True, db_column='CountyID', blank=True) # Field name made lowercase.
    countyname = models.CharField(max_length=100, db_column='CountyName') # Field name made lowercase.
    dusinsmp = models.IntegerField(null=True, db_column='DUsInSmp', blank=True) # Field name made lowercase.
    smpdus = models.IntegerField(null=True, db_column='SmpDUs', blank=True) # Field name made lowercase.
    pcntdus = models.FloatField(null=True, db_column='pcntDUs', blank=True) # Field name made lowercase.
    dusinarea = models.IntegerField(null=True, db_column='DusInArea', blank=True) # Field name made lowercase.
    totdus = models.IntegerField(null=True, db_column='TotDUs', blank=True) # Field name made lowercase.
    totalppleinarea = models.IntegerField(null=True, db_column='TotalPpleinArea', blank=True) # Field name made lowercase.
    pcntpop = models.FloatField(null=True, db_column='PcntPop', blank=True) # Field name made lowercase.
    pop = models.IntegerField(null=True, db_column='Pop', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'WSrcDrkWellsCounty'

class Wsrcdrkwellsslum(models.Model): 
    slumid = models.IntegerField(null=True, db_column='SlumID', blank=True) # Field name made lowercase.
    slumname = models.CharField(max_length=100, db_column='SlumName') # Field name made lowercase.
    dusinsmp = models.IntegerField(null=True, db_column='DUsInSmp', blank=True) # Field name made lowercase.
    smpdus = models.IntegerField(null=True, db_column='SmpDUs', blank=True) # Field name made lowercase.
    pcntdus = models.FloatField(null=True, db_column='pcntDUs', blank=True) # Field name made lowercase.
    dusinarea = models.IntegerField(null=True, db_column='DusInArea', blank=True) # Field name made lowercase.
    totdus = models.IntegerField(null=True, db_column='TotDUs', blank=True) # Field name made lowercase.
    totalppleinarea = models.IntegerField(null=True, db_column='TotalPpleinArea', blank=True) # Field name made lowercase.
    pcntpop = models.FloatField(null=True, db_column='PcntPop', blank=True) # Field name made lowercase.
    pop = models.IntegerField(null=True, db_column='Pop', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'WSrcDrkWellsSlum'

class Wsrcdrkwellstown(models.Model): 
    townid = models.IntegerField(null=True, db_column='TownID', blank=True) # Field name made lowercase.
    townname = models.CharField(max_length=100, db_column='TownName') # Field name made lowercase.
    dusinsmp = models.IntegerField(null=True, db_column='DUsInSmp', blank=True) # Field name made lowercase.
    smpdus = models.IntegerField(null=True, db_column='SmpDUs', blank=True) # Field name made lowercase.
    pcntdus = models.FloatField(null=True, db_column='pcntDUs', blank=True) # Field name made lowercase.
    dusinarea = models.IntegerField(null=True, db_column='DusInArea', blank=True) # Field name made lowercase.
    totdus = models.IntegerField(null=True, db_column='TotDUs', blank=True) # Field name made lowercase.
    totalppleinarea = models.IntegerField(null=True, db_column='TotalPpleinArea', blank=True) # Field name made lowercase.
    pcntpop = models.FloatField(null=True, db_column='PcntPop', blank=True) # Field name made lowercase.
    pop = models.IntegerField(null=True, db_column='Pop', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'WSrcDrkWellsTown'

class Wsrcdrkwellswsp(models.Model): 
    wspid = models.CharField(max_length=100, db_column='WSPID') # Field name made lowercase.
    wspname = models.CharField(max_length=100, db_column='WSPName') # Field name made lowercase.
    dusinsmp = models.IntegerField(null=True, db_column='DUsInSmp', blank=True) # Field name made lowercase.
    smpdus = models.IntegerField(null=True, db_column='SmpDUs', blank=True) # Field name made lowercase.
    pcntdus = models.FloatField(null=True, db_column='pcntDUs', blank=True) # Field name made lowercase.
    dusinarea = models.IntegerField(null=True, db_column='DusInArea', blank=True) # Field name made lowercase.
    totdus = models.IntegerField(null=True, db_column='TotDUs', blank=True) # Field name made lowercase.
    totalppleinarea = models.IntegerField(null=True, db_column='TotalPpleinArea', blank=True) # Field name made lowercase.
    pcntpop = models.FloatField(null=True, db_column='PcntPop', blank=True) # Field name made lowercase.
    pop = models.IntegerField(null=True, db_column='Pop', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'WSrcDrkWellsWSP'

class Wsupsituation8(models.Model): 
    areaid = models.FloatField(null=True, db_column='AreaID', blank=True) # Field name made lowercase.
    arealinkedwater = models.CharField(max_length=100, db_column='AreaLinkedwater') # Field name made lowercase.
    techstat = models.CharField(max_length=100, db_column='TechStat') # Field name made lowercase.
    wnwdist = models.CharField(max_length=100, db_column='WnwDist') # Field name made lowercase.
    mainwatersrc = models.CharField(max_length=100, db_column='MainWaterSrc') # Field name made lowercase.
    maindrkgwatersrc = models.CharField(max_length=100, db_column='MainDrkgWaterSrc') # Field name made lowercase.
    mainwaterprob = models.TextField(db_column='MainWaterProb') # Field name made lowercase.
    class Meta:
        db_table = 'WSupSituation-8'

class Wsupsituation28(models.Model): 
    areaid = models.FloatField(null=True, db_column='AreaID', blank=True) # Field name made lowercase.
    areaname = models.CharField(max_length=100, db_column='Areaname') # Field name made lowercase.
    protectedsrc = models.TextField(db_column='ProtectedSrc') # Field name made lowercase.
    unprotectedsrc = models.TextField(db_column='UnProtectedSrc') # Field name made lowercase.
    class Meta:
        db_table = 'WSupSituation2-8'

class Wsupsituation38D(models.Model): 
    areaid = models.FloatField(null=True, db_column='AreaID', blank=True) # Field name made lowercase.
    illegalcon = models.TextField(db_column='IllegalCon', blank=True) # Field name made lowercase.
    supply24hr = models.TextField(db_column='Supply24hr', blank=True) # Field name made lowercase.
    supplyinfo = models.TextField(db_column='SupplyInfo', blank=True) # Field name made lowercase.
    waterrationing = models.TextField(db_column='Waterrationing', blank=True) # Field name made lowercase.
    wdyspwk = models.TextField(db_column='Wdyspwk', blank=True) # Field name made lowercase.
    rationrem = models.TextField(db_column='RationRem', blank=True) # Field name made lowercase.
    waterpressure = models.TextField(db_column='WaterPressure', blank=True) # Field name made lowercase.
    waterqlty = models.TextField(db_column='WaterQlty', blank=True) # Field name made lowercase.
    wwsptariffpunit = models.TextField(db_column='Wwsptariffpunit', blank=True) # Field name made lowercase.
    wwsptariffp20l = models.TextField(db_column='Wwsptariffp20l', blank=True) # Field name made lowercase.
    wwsptariffpmnth = models.TextField(db_column='Wwsptariffpmnth', blank=True) # Field name made lowercase.
    tariffrem = models.TextField(db_column='TariffRem', blank=True) # Field name made lowercase.
    wsptariffapprvd = models.TextField(db_column='WSPTariffapprvd', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'WSupSituation3-8d'

class Wsupsituationdu(models.Model): 
    areaid = models.FloatField(null=True, db_column='AreaID', blank=True) # Field name made lowercase.
    areaname = models.CharField(max_length=100, db_column='Areaname') # Field name made lowercase.
    wsituation = models.CharField(max_length=100, db_column='Wsituation') # Field name made lowercase.
    areasmpdus = models.IntegerField(null=True, db_column='AreaSmpDUs', blank=True) # Field name made lowercase.
    nousingsrc = models.IntegerField(null=True, db_column='Nousingsrc', blank=True) # Field name made lowercase.
    pcntdus = models.FloatField(null=True, db_column='pcntDUs', blank=True) # Field name made lowercase.
    ndus = models.IntegerField(null=True, db_column='NDus', blank=True) # Field name made lowercase.
    persons = models.FloatField(null=True, blank=True)
    pcntpple = models.FloatField(null=True, blank=True)
    numdu = models.IntegerField(null=True, db_column='NumDU', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'WSupSituationDU'

class Wsupplyinf8E(models.Model): 
    areaid = models.FloatField(null=True, db_column='AreaID', blank=True) # Field name made lowercase.
    waterresellers = models.TextField(db_column='Waterresellers', blank=True) # Field name made lowercase.
    communityschm = models.TextField(db_column='Communityschm', blank=True) # Field name made lowercase.
    ngoscheme = models.TextField(db_column='NGOscheme', blank=True) # Field name made lowercase.
    infwaterqlty = models.TextField(db_column='InfWaterqlty', blank=True) # Field name made lowercase.
    winftariffp20l1 = models.TextField(db_column='Winftariffp20l1', blank=True) # Field name made lowercase.
    winftariffp20l2 = models.TextField(db_column='Winftariffp20l2', blank=True) # Field name made lowercase.
    winftariffp20l3 = models.TextField(db_column='Winftariffp20l3', blank=True) # Field name made lowercase.
    tariffrem = models.TextField(db_column='TariffRem', blank=True) # Field name made lowercase.
    wsupplyproj = models.TextField(db_column='Wsupplyproj') # Field name made lowercase.
    class Meta:
        db_table = 'WSupplyInf-8e'

class Wunreliablesrcbath(models.Model): 
    areaid = models.FloatField(null=True, db_column='AreaID', blank=True) # Field name made lowercase.
    areaname = models.CharField(max_length=100, db_column='Areaname') # Field name made lowercase.
    areasmpdus = models.IntegerField(null=True, db_column='AreaSmpDUs', blank=True) # Field name made lowercase.
    dusinsmp = models.IntegerField(null=True, db_column='DUsInSmp', blank=True) # Field name made lowercase.
    pcntdus = models.FloatField(null=True, db_column='pcntDUs', blank=True) # Field name made lowercase.
    dusinarea = models.IntegerField(null=True, db_column='DusInArea', blank=True) # Field name made lowercase.
    smppersons = models.IntegerField(null=True, db_column='SmpPersons', blank=True) # Field name made lowercase.
    totalppleinarea = models.IntegerField(null=True, db_column='TotalPpleinArea', blank=True) # Field name made lowercase.
    pcntpple = models.FloatField(null=True, blank=True)
    totaldusinarea = models.IntegerField(null=True, db_column='TotalDUsInArea', blank=True) # Field name made lowercase.
    areasmppop = models.IntegerField(null=True, db_column='AreaSmpPop', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'WUnreliableSrcBath'

class Wunreliablesrcdrk(models.Model): 
    areaid = models.FloatField(null=True, db_column='AreaID', blank=True) # Field name made lowercase.
    areaname = models.CharField(max_length=100, db_column='Areaname') # Field name made lowercase.
    areasmpdus = models.IntegerField(null=True, db_column='AreaSmpDUs', blank=True) # Field name made lowercase.
    dusinsmp = models.IntegerField(null=True, db_column='DUsInSmp', blank=True) # Field name made lowercase.
    pcntdus = models.FloatField(null=True, db_column='pcntDUs', blank=True) # Field name made lowercase.
    dusinarea = models.IntegerField(null=True, db_column='DusInArea', blank=True) # Field name made lowercase.
    smppersons = models.IntegerField(null=True, db_column='SmpPersons', blank=True) # Field name made lowercase.
    totalppleinarea = models.IntegerField(null=True, db_column='TotalPpleinArea', blank=True) # Field name made lowercase.
    pcntpple = models.FloatField(null=True, blank=True)
    totaldusinarea = models.IntegerField(null=True, db_column='TotalDUsInArea', blank=True) # Field name made lowercase.
    areasmppop = models.IntegerField(null=True, db_column='AreaSmpPop', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'WUnreliableSrcDrk'

class Wunreliablesrcdrkavgpay(models.Model): 
    areaid = models.FloatField(null=True, db_column='AreaID', blank=True) # Field name made lowercase.
    areaname = models.CharField(max_length=100, db_column='Areaname') # Field name made lowercase.
    paymthd = models.CharField(max_length=100, db_column='PayMthd') # Field name made lowercase.
    areasmpdus = models.IntegerField(null=True, db_column='AreaSmpDUs', blank=True) # Field name made lowercase.
    dusinsmp = models.IntegerField(null=True, db_column='DUsInSmp', blank=True) # Field name made lowercase.
    pcntdus = models.FloatField(null=True, db_column='pcntDUs', blank=True) # Field name made lowercase.
    dusinarea = models.IntegerField(null=True, db_column='DusInArea', blank=True) # Field name made lowercase.
    smppersons = models.IntegerField(null=True, db_column='SmpPersons', blank=True) # Field name made lowercase.
    totalppleinarea = models.IntegerField(null=True, db_column='TotalPpleinArea', blank=True) # Field name made lowercase.
    pcntpple = models.FloatField(null=True, blank=True)
    totaldusinarea = models.IntegerField(null=True, db_column='TotalDUsInArea', blank=True) # Field name made lowercase.
    avgpaydrk = models.FloatField(null=True, db_column='AvgPayDrk', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'WUnreliableSrcDrkAvgPay'

class Wunreliablesrcdrktrt(models.Model): 
    areaid = models.FloatField(null=True, db_column='AreaID', blank=True) # Field name made lowercase.
    areaname = models.CharField(max_length=100, db_column='Areaname') # Field name made lowercase.
    areasmpdus = models.IntegerField(null=True, db_column='AreaSmpDUs', blank=True) # Field name made lowercase.
    dusinsmp = models.IntegerField(null=True, db_column='DUsInSmp', blank=True) # Field name made lowercase.
    pcntdus = models.FloatField(null=True, db_column='pcntDUs', blank=True) # Field name made lowercase.
    dusinarea = models.IntegerField(null=True, db_column='DusInArea', blank=True) # Field name made lowercase.
    smppersons = models.IntegerField(null=True, db_column='SmpPersons', blank=True) # Field name made lowercase.
    totalppleinarea = models.IntegerField(null=True, db_column='TotalPpleinArea', blank=True) # Field name made lowercase.
    pcntpple = models.FloatField(null=True, blank=True)
    totaldusinarea = models.IntegerField(null=True, db_column='TotalDUsInArea', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'WUnreliableSrcDrkTrt'

class Wusersperindcon10D(models.Model): 
    area = models.FloatField(null=True, db_column='Area', blank=True) # Field name made lowercase.
    areaname = models.CharField(max_length=100, db_column='Areaname') # Field name made lowercase.
    areapop = models.IntegerField(null=True, db_column='AreaPop', blank=True) # Field name made lowercase.
    noofsmpcons = models.IntegerField(null=True, db_column='NoofSmpCons', blank=True) # Field name made lowercase.
    smppersons = models.IntegerField(null=True, db_column='SmpPersons', blank=True) # Field name made lowercase.
    totalppleinarea = models.IntegerField(null=True, db_column='TotalPpleinArea', blank=True) # Field name made lowercase.
    noofconsinarea = models.IntegerField(null=True, db_column='NoofConsinArea', blank=True) # Field name made lowercase.
    userspercon = models.FloatField(null=True, db_column='UsersPercon', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'WUsersPerIndCon-10d'

class Wusersperksk(models.Model): 
    areaid = models.FloatField(null=True, db_column='AreaID', blank=True) # Field name made lowercase.
    areaname = models.CharField(max_length=100, db_column='Areaname') # Field name made lowercase.
    areapop = models.IntegerField(null=True, db_column='AreaPop', blank=True) # Field name made lowercase.
    totalppleinarea = models.IntegerField(null=True, db_column='TotalPpleinArea', blank=True) # Field name made lowercase.
    pubwaterksks = models.IntegerField(null=True, db_column='PubWaterKsks', blank=True) # Field name made lowercase.
    usersperksk = models.CharField(max_length=24, db_column='UsersPerKsk') # Field name made lowercase.
    class Meta:
        db_table = 'WUsersPerKsk'

class Wusersperpubtap10D(models.Model): 
    areaid = models.FloatField(null=True, db_column='AreaID', blank=True) # Field name made lowercase.
    areaname = models.CharField(max_length=100, db_column='Areaname') # Field name made lowercase.
    nusers = models.CharField(max_length=100, db_column='NUsers') # Field name made lowercase.
    ntaps = models.IntegerField(null=True, db_column='NTaps', blank=True) # Field name made lowercase.
    usersperpubtap = models.CharField(max_length=100, db_column='UsersPerPubTap') # Field name made lowercase.
    class Meta:
        db_table = 'WUsersPerPubTap-10d'

class Wateroutlets(models.Model): 
    areaid = models.CharField(max_length=100, db_column='AreaID', blank=True) # Field name made lowercase.
    areaname = models.CharField(max_length=100, db_column='AreaName', blank=True) # Field name made lowercase.
    pubwsptaps = models.CharField(max_length=100, db_column='PubWSPTaps', blank=True) # Field name made lowercase.
    comtaps = models.CharField(max_length=100, db_column='ComTaps', blank=True) # Field name made lowercase.
    privtaps = models.CharField(max_length=100, db_column='PrivTaps', blank=True) # Field name made lowercase.
    pubwaterksks = models.CharField(max_length=100, db_column='PubWaterKsks', blank=True) # Field name made lowercase.
    comwaterksks = models.CharField(max_length=100, db_column='ComWaterKsks', blank=True) # Field name made lowercase.
    privwaterksks = models.CharField(max_length=100, db_column='PrivWaterKsks', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'WaterOutlets'

class Waterpaiddu(models.Model): 
    areaid = models.FloatField(null=True, db_column='AreaID', blank=True) # Field name made lowercase.
    areaname = models.CharField(max_length=100, db_column='Areaname') # Field name made lowercase.
    waterpaid = models.CharField(max_length=100, db_column='WaterPaid') # Field name made lowercase.
    areasmpdus = models.IntegerField(null=True, db_column='AreaSmpDUs', blank=True) # Field name made lowercase.
    dusinsmp = models.IntegerField(null=True, db_column='DUsInSmp', blank=True) # Field name made lowercase.
    pcntdus = models.FloatField(null=True, db_column='pcntDUs', blank=True) # Field name made lowercase.
    dusinarea = models.IntegerField(null=True, db_column='DusInArea', blank=True) # Field name made lowercase.
    totaldusinarea = models.IntegerField(null=True, db_column='TotalDUsInArea', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'WaterPaidDU'

class Waterpaymthddu(models.Model): 
    areaid = models.FloatField(null=True, db_column='AreaID', blank=True) # Field name made lowercase.
    areaname = models.CharField(max_length=100, db_column='Areaname') # Field name made lowercase.
    wpaymthd = models.CharField(max_length=100, db_column='WPayMthd') # Field name made lowercase.
    dus = models.IntegerField(null=True, db_column='DUs', blank=True) # Field name made lowercase.
    dusinsmp = models.IntegerField(null=True, db_column='DUsInSmp', blank=True) # Field name made lowercase.
    pcntdus = models.FloatField(null=True, db_column='pcntDUs', blank=True) # Field name made lowercase.
    dusinarea = models.IntegerField(null=True, db_column='DUsInArea', blank=True) # Field name made lowercase.
    totaldusinarea = models.IntegerField(null=True, db_column='TotalDUsInArea', blank=True) # Field name made lowercase.
    wpaid = models.CharField(max_length=100, db_column='Wpaid') # Field name made lowercase.
    class Meta:
        db_table = 'WaterPayMthdDU'

class Waterqlty9(models.Model): 
    areaid = models.FloatField(null=True, db_column='AreaID', blank=True) # Field name made lowercase.
    areaname = models.CharField(max_length=100, db_column='Areaname') # Field name made lowercase.
    waterqlty = models.CharField(max_length=100, db_column='WaterQlty') # Field name made lowercase.
    areasmpdus = models.IntegerField(null=True, db_column='AreaSmpDUs', blank=True) # Field name made lowercase.
    smpusingsrc = models.IntegerField(null=True, db_column='Smpusingsrc', blank=True) # Field name made lowercase.
    pcntplotsusingsrc = models.FloatField(null=True, blank=True)
    ndus = models.IntegerField(null=True, db_column='NDus', blank=True) # Field name made lowercase.
    persons = models.IntegerField(null=True, blank=True)
    pcntppleusingsrc = models.FloatField(null=True, blank=True)
    numdu = models.IntegerField(null=True, db_column='numDU', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'WaterQlty-9'

class Watersrcbath9(models.Model): 
    areaid = models.FloatField(null=True, db_column='AreaID', blank=True) # Field name made lowercase.
    areaname = models.CharField(max_length=100, db_column='Areaname') # Field name made lowercase.
    watersrcbath = models.CharField(max_length=100, db_column='WaterSrcBath') # Field name made lowercase.
    areasmpdus = models.IntegerField(null=True, db_column='AreaSmpDUs', blank=True) # Field name made lowercase.
    smpusingsrc = models.IntegerField(null=True, db_column='Smpusingsrc', blank=True) # Field name made lowercase.
    pcntplotsusingsrc = models.FloatField(null=True, blank=True)
    ndus = models.IntegerField(null=True, db_column='NDus', blank=True) # Field name made lowercase.
    persons = models.FloatField(null=True, blank=True)
    pcntppleusingsrc = models.FloatField(null=True, blank=True)
    numdu = models.IntegerField(null=True, db_column='NumDU', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'WaterSrcBath-9'

class Watersrcckg9(models.Model): 
    areaid = models.FloatField(null=True, db_column='AreaID', blank=True) # Field name made lowercase.
    areaname = models.CharField(max_length=100, db_column='Areaname') # Field name made lowercase.
    ckgwatersrc = models.CharField(max_length=100, db_column='CkgWaterSrc') # Field name made lowercase.
    areasmpdus = models.IntegerField(null=True, db_column='AreaSmpDUs', blank=True) # Field name made lowercase.
    nousingsrc = models.IntegerField(null=True, db_column='Nousingsrc', blank=True) # Field name made lowercase.
    pcntplotsusingsrc = models.FloatField(null=True, blank=True)
    ndus = models.IntegerField(null=True, db_column='NDus', blank=True) # Field name made lowercase.
    persons = models.FloatField(null=True, blank=True)
    pcntppleusingsrc = models.FloatField(null=True, blank=True)
    numdu = models.IntegerField(null=True, db_column='NumDU', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'WaterSrcCkg-9'

class Watersrcdrk9(models.Model): 
    areaid = models.FloatField(null=True, db_column='AreaID', blank=True) # Field name made lowercase.
    areaname = models.CharField(max_length=100, db_column='Areaname') # Field name made lowercase.
    drkgwatersrc = models.CharField(max_length=100, db_column='DrkgWaterSrc') # Field name made lowercase.
    areasmpdus = models.IntegerField(null=True, db_column='AreaSmpDUs', blank=True) # Field name made lowercase.
    smpusingsrc = models.IntegerField(null=True, db_column='Smpusingsrc', blank=True) # Field name made lowercase.
    pcntdususingsrc = models.FloatField(null=True, db_column='pcntDUsusingsrc', blank=True) # Field name made lowercase.
    ndus = models.IntegerField(null=True, db_column='NDus', blank=True) # Field name made lowercase.
    nppleusingsrc = models.IntegerField(null=True, db_column='Nppleusingsrc', blank=True) # Field name made lowercase.
    pcntppleusingsrc = models.FloatField(null=True, blank=True)
    numdu = models.IntegerField(null=True, db_column='NumDU', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'WaterSrcDrk-9'

class Watersrclndry9(models.Model): 
    areaid = models.FloatField(null=True, db_column='AreaID', blank=True) # Field name made lowercase.
    areaname = models.CharField(max_length=100, db_column='Areaname') # Field name made lowercase.
    watersrclndry = models.TextField(db_column='WaterSrcLndry') # Field name made lowercase.
    areasmpdus = models.IntegerField(null=True, db_column='AreaSmpDUs', blank=True) # Field name made lowercase.
    smpusingsrc = models.IntegerField(null=True, db_column='Smpusingsrc', blank=True) # Field name made lowercase.
    pcntplotsusingsrc = models.FloatField(null=True, blank=True)
    ndus = models.IntegerField(null=True, db_column='NDus', blank=True) # Field name made lowercase.
    persons = models.FloatField(null=True, blank=True)
    pcntppleusingsrc = models.FloatField(null=True, blank=True)
    numdu = models.IntegerField(null=True, db_column='NumDU', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'WaterSrcLndry-9'

class Waterstoragedu(models.Model): 
    areaid = models.FloatField(null=True, db_column='AreaID', blank=True) # Field name made lowercase.
    areaname = models.CharField(max_length=100, db_column='Areaname') # Field name made lowercase.
    storagemthd = models.CharField(max_length=100, db_column='StorageMthd') # Field name made lowercase.
    areasmpdus = models.IntegerField(null=True, db_column='AreaSmpDUs', blank=True) # Field name made lowercase.
    smpdus = models.IntegerField(null=True, db_column='SmpDUs', blank=True) # Field name made lowercase.
    pcntdus = models.FloatField(null=True, db_column='pcntDUs', blank=True) # Field name made lowercase.
    ndus = models.IntegerField(null=True, db_column='NDus', blank=True) # Field name made lowercase.
    persons = models.FloatField(null=True, blank=True)
    pcntpple = models.FloatField(null=True, blank=True)
    numdu = models.IntegerField(null=True, db_column='numDU', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'WaterStorageDU'

class Watertrt33County(models.Model): 
    countyid = models.IntegerField(null=True, db_column='CountyID', blank=True) # Field name made lowercase.
    countyname = models.CharField(max_length=100, db_column='CountyName') # Field name made lowercase.
    drkwatertreated = models.CharField(max_length=100, db_column='DrkWaterTreated') # Field name made lowercase.
    smpsrc = models.IntegerField(null=True, db_column='SmpSrc', blank=True) # Field name made lowercase.
    smpdus = models.IntegerField(null=True, db_column='SmpDUs', blank=True) # Field name made lowercase.
    totdus = models.IntegerField(null=True, db_column='TotDUs', blank=True) # Field name made lowercase.
    pcntdususingsrc = models.FloatField(null=True, db_column='pcntDUsusingsrc', blank=True) # Field name made lowercase.
    nousingsrc = models.IntegerField(null=True, db_column='NoUsingSrc', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'WaterTrt33County'

class Watertrt33Slum(models.Model): 
    slumid = models.IntegerField(null=True, db_column='SlumID', blank=True) # Field name made lowercase.
    slumname = models.CharField(max_length=100, db_column='SlumName') # Field name made lowercase.
    drkwatertreated = models.CharField(max_length=100, db_column='DrkWaterTreated') # Field name made lowercase.
    smpsrc = models.IntegerField(null=True, db_column='SmpSrc', blank=True) # Field name made lowercase.
    smpdus = models.IntegerField(null=True, db_column='SmpDUs', blank=True) # Field name made lowercase.
    totdus = models.IntegerField(null=True, db_column='TotDUs', blank=True) # Field name made lowercase.
    pcntdususingsrc = models.FloatField(null=True, db_column='pcntDUsusingsrc', blank=True) # Field name made lowercase.
    nousingsrc = models.IntegerField(null=True, db_column='NoUsingSrc', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'WaterTrt33Slum'

class Watertrt33Town(models.Model): 
    townid = models.IntegerField(null=True, db_column='TownID', blank=True) # Field name made lowercase.
    townname = models.CharField(max_length=100, db_column='TownName') # Field name made lowercase.
    drkwatertreated = models.CharField(max_length=100, db_column='DrkWaterTreated') # Field name made lowercase.
    smpsrc = models.IntegerField(null=True, db_column='SmpSrc', blank=True) # Field name made lowercase.
    smpdus = models.IntegerField(null=True, db_column='SmpDUs', blank=True) # Field name made lowercase.
    totdus = models.IntegerField(null=True, db_column='TotDUs', blank=True) # Field name made lowercase.
    pcntdususingsrc = models.FloatField(null=True, db_column='pcntDUsusingsrc', blank=True) # Field name made lowercase.
    nousingsrc = models.IntegerField(null=True, db_column='NoUsingSrc', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'WaterTrt33Town'

class Watertrt33Wsp(models.Model): 
    wspid = models.CharField(max_length=100, db_column='WSPID') # Field name made lowercase.
    wspname = models.CharField(max_length=100, db_column='WSPName') # Field name made lowercase.
    drkwatertreated = models.CharField(max_length=100, db_column='DrkWaterTreated') # Field name made lowercase.
    smpsrc = models.IntegerField(null=True, db_column='SmpSrc', blank=True) # Field name made lowercase.
    smpdus = models.IntegerField(null=True, db_column='SmpDUs', blank=True) # Field name made lowercase.
    totdus = models.IntegerField(null=True, db_column='TotDUs', blank=True) # Field name made lowercase.
    pcntdususingsrc = models.FloatField(null=True, db_column='pcntDUsusingsrc', blank=True) # Field name made lowercase.
    nousingsrc = models.IntegerField(null=True, db_column='NoUsingSrc', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'WaterTrt33WSP'

class Watertrtdu9(models.Model): 
    areaid = models.FloatField(null=True, db_column='AreaID', blank=True) # Field name made lowercase.
    areaname = models.CharField(max_length=100, db_column='Areaname') # Field name made lowercase.
    drkwatertreated = models.CharField(max_length=100, db_column='DrkWaterTreated') # Field name made lowercase.
    areasmpdus = models.IntegerField(null=True, db_column='AreaSmpDUs', blank=True) # Field name made lowercase.
    smpusingsrc = models.IntegerField(null=True, db_column='Smpusingsrc', blank=True) # Field name made lowercase.
    pcntdus = models.FloatField(null=True, db_column='pcntDUs', blank=True) # Field name made lowercase.
    ndus = models.IntegerField(null=True, db_column='NDus', blank=True) # Field name made lowercase.
    persons = models.FloatField(null=True, blank=True)
    pcntpple = models.FloatField(null=True, blank=True)
    numdu = models.IntegerField(null=True, db_column='numDU', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'WaterTrtDU-9'

class Watertrtmthddu(models.Model): 
    areaid = models.FloatField(null=True, db_column='AreaID', blank=True) # Field name made lowercase.
    areaname = models.CharField(max_length=100, db_column='Areaname') # Field name made lowercase.
    drkwatertrtmthd = models.TextField(db_column='DrkWaterTrtMthd', blank=True) # Field name made lowercase.
    dus = models.IntegerField(null=True, db_column='DUs', blank=True) # Field name made lowercase.
    pcntdus = models.FloatField(null=True, db_column='pcntDUs', blank=True) # Field name made lowercase.
    ndus = models.IntegerField(null=True, db_column='NDus', blank=True) # Field name made lowercase.
    numdu = models.IntegerField(null=True, db_column='numDU', blank=True) # Field name made lowercase.
    ndu = models.IntegerField(null=True, db_column='NDU', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'WaterTrtMthdDU'

class Watertrtstorage(models.Model): 
    areaid = models.FloatField(null=True, db_column='AreaID', blank=True) # Field name made lowercase.
    wspwaterqlty = models.CharField(max_length=100, db_column='WSPWaterQlty') # Field name made lowercase.
    infwaterqlty = models.CharField(max_length=100, db_column='InfWaterQlty') # Field name made lowercase.
    watertreated = models.TextField(db_column='WaterTreated', blank=True) # Field name made lowercase.
    wtrtmethods = models.TextField(db_column='WtrtMethods', blank=True) # Field name made lowercase.
    storagemthd = models.TextField(db_column='StorageMthd', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'WaterTrtStorage'

class Wresidentsperwspksk(models.Model): 
    area = models.FloatField(null=True, db_column='Area', blank=True) # Field name made lowercase.
    areaname = models.CharField(max_length=100, db_column='Areaname') # Field name made lowercase.
    areapop = models.IntegerField(null=True, db_column='AreaPop', blank=True) # Field name made lowercase.
    pubwaterksks = models.IntegerField(null=True, db_column='PubWaterKsks', blank=True) # Field name made lowercase.
    ppleperkiosk = models.CharField(max_length=100, db_column='PplePerKiosk') # Field name made lowercase.
    class Meta:
        db_table = 'WresidentsperWSPKsk'

class AuthGroup(models.Model): 
    name = models.CharField(max_length=80, unique=True)
    class Meta:
        db_table = 'auth_group'

class AuthGroupPermissions(models.Model): 
    group = models.ForeignKey(AuthGroup)
    permission = models.ForeignKey('AuthPermission')
    class Meta:
        db_table = 'auth_group_permissions'

class AuthPermission(models.Model): 
    name = models.CharField(max_length=50)
    content_type = models.ForeignKey('DjangoContentType')
    codename = models.CharField(max_length=100)
    class Meta:
        db_table = 'auth_permission'

class AuthUser(models.Model): 
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField()
    is_superuser = models.BooleanField()
    username = models.CharField(max_length=30, unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=75)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()
    class Meta:
        db_table = 'auth_user'

class AuthUserGroups(models.Model): 
    user = models.ForeignKey(AuthUser)
    group = models.ForeignKey(AuthGroup)
    class Meta:
        db_table = 'auth_user_groups'

class AuthUserUserPermissions(models.Model): 
    user = models.ForeignKey(AuthUser)
    permission = models.ForeignKey(AuthPermission)
    class Meta:
        db_table = 'auth_user_user_permissions'

class DjangoAdminLog(models.Model): 
    action_time = models.DateTimeField()
    user = models.ForeignKey(AuthUser)
    content_type = models.ForeignKey('DjangoContentType', null=True, blank=True)
    object_id = models.TextField(blank=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    class Meta:
        db_table = 'django_admin_log'

class DjangoContentType(models.Model): 
    name = models.CharField(max_length=100)
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    class Meta:
        db_table = 'django_content_type'

class DjangoSession(models.Model):
    session_key = models.CharField(max_length=40, primary_key=True)
    session_data = models.TextField()
    expire_date = models.DateTimeField()
    class Meta:
        db_table = 'django_session'

class DjangoSite(models.Model): 
    domain = models.CharField(max_length=100)
    name = models.CharField(max_length=50)
    class Meta:
        db_table = 'django_site'

class MajidataColumnlabel(models.Model): 
    column_name = models.CharField(max_length=100, blank=True)
    column_label = models.CharField(max_length=100, blank=True)
    class Meta:
        db_table = 'majidata_columnlabel'

class MajitablerelationshipRelations(models.Model): 
    geographic_level = models.SmallIntegerField()
    category = models.SmallIntegerField()
    class Meta:
        db_table = 'majitablerelationship_relations'

class MajitablerelationshipRelationsTable(models.Model): 
    relations = models.ForeignKey(MajitablerelationshipRelations)
    tables = models.ForeignKey('MajitablerelationshipTables')
    class Meta:
        db_table = 'majitablerelationship_relations_table'

class MajitablerelationshipTables(models.Model): 
    name = models.CharField(max_length=100, blank=True)
    user_firendly_name = models.TextField(blank=True)
    class Meta:
        db_table = 'majitablerelationship_tables'

class SouthMigrationhistory(models.Model): 
    app_name = models.CharField(max_length=255)
    migration = models.CharField(max_length=255)
    applied = models.DateTimeField()
    class Meta:
        db_table = 'south_migrationhistory'

