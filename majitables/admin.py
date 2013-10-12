from django.contrib import admin 
from models import *

class ApopdenavgminmaxcountyAdmin(admin.ModelAdmin):
	list_display = [f.name for f in Apopdenavgminmaxcounty._meta.fields]

admin.site.register(Apopdenavgminmaxcounty, ApopdenavgminmaxcountyAdmin)

class ApopdenavgminmaxslumAdmin(admin.ModelAdmin):
	list_display = [f.name for f in Apopdenavgminmaxslum._meta.fields]

admin.site.register(Apopdenavgminmaxslum, ApopdenavgminmaxslumAdmin)

class ApopdenavgminmaxtownAdmin(admin.ModelAdmin):
	list_display = [f.name for f in Apopdenavgminmaxtown._meta.fields]

admin.site.register(Apopdenavgminmaxtown, ApopdenavgminmaxtownAdmin)

class ApopdennareascountyAdmin(admin.ModelAdmin):
	list_display = [f.name for f in Apopdennareascounty._meta.fields]

admin.site.register(Apopdennareascounty, ApopdennareascountyAdmin)

class ApopdennareasslumAdmin(admin.ModelAdmin):
	list_display = [f.name for f in Apopdennareasslum._meta.fields]

admin.site.register(Apopdennareasslum, ApopdennareasslumAdmin)

class ApopdennareastownsAdmin(admin.ModelAdmin):
	list_display = [f.name for f in Apopdennareastowns._meta.fields]

admin.site.register(Apopdennareastowns, ApopdennareastownsAdmin)

class AreadustatuscountyAdmin(admin.ModelAdmin):
	list_display = [f.name for f in Areadustatuscounty._meta.fields]

admin.site.register(Areadustatuscounty, AreadustatuscountyAdmin)

class AreadustatusslumAdmin(admin.ModelAdmin):
	list_display = [f.name for f in Areadustatusslum._meta.fields]

admin.site.register(Areadustatusslum, AreadustatusslumAdmin)

class AreadustatustownAdmin(admin.ModelAdmin):
	list_display = [f.name for f in Areadustatustown._meta.fields]

admin.site.register(Areadustatustown, AreadustatustownAdmin)

class AreadustatuswspAdmin(admin.ModelAdmin):
	list_display = [f.name for f in Areadustatuswsp._meta.fields]

admin.site.register(Areadustatuswsp, AreadustatuswspAdmin)

class AreadutypecountyAdmin(admin.ModelAdmin):
	list_display = [f.name for f in Areadutypecounty._meta.fields]

admin.site.register(Areadutypecounty, AreadutypecountyAdmin)

class AreadutypeslumAdmin(admin.ModelAdmin):
	list_display = [f.name for f in Areadutypeslum._meta.fields]

admin.site.register(Areadutypeslum, AreadutypeslumAdmin)

class AreadutypestructureAdmin(admin.ModelAdmin):
	list_display = [f.name for f in Areadutypestructure._meta.fields]

admin.site.register(Areadutypestructure, AreadutypestructureAdmin)

class AreadutypetownAdmin(admin.ModelAdmin):
	list_display = [f.name for f in Areadutypetown._meta.fields]

admin.site.register(Areadutypetown, AreadutypetownAdmin)

class AreadutypewspAdmin(admin.ModelAdmin):
	list_display = [f.name for f in Areadutypewsp._meta.fields]

admin.site.register(Areadutypewsp, AreadutypewspAdmin)

class AreadutypehseAdmin(admin.ModelAdmin):
	list_display = [f.name for f in Areadutypehse._meta.fields]

admin.site.register(Areadutypehse, AreadutypehseAdmin)

class AreahabhsetypecountyAdmin(admin.ModelAdmin):
	list_display = [f.name for f in Areahabhsetypecounty._meta.fields]

admin.site.register(Areahabhsetypecounty, AreahabhsetypecountyAdmin)

class AreahabhsetypeslumAdmin(admin.ModelAdmin):
	list_display = [f.name for f in Areahabhsetypeslum._meta.fields]

admin.site.register(Areahabhsetypeslum, AreahabhsetypeslumAdmin)

class AreahabhsetypetownAdmin(admin.ModelAdmin):
	list_display = [f.name for f in Areahabhsetypetown._meta.fields]

admin.site.register(Areahabhsetypetown, AreahabhsetypetownAdmin)

class AreahabhsetypewspAdmin(admin.ModelAdmin):
	list_display = [f.name for f in Areahabhsetypewsp._meta.fields]

admin.site.register(Areahabhsetypewsp, AreahabhsetypewspAdmin)

class AreahabhsgsitcountyAdmin(admin.ModelAdmin):
	list_display = [f.name for f in Areahabhsgsitcounty._meta.fields]

admin.site.register(Areahabhsgsitcounty, AreahabhsgsitcountyAdmin)

class AreahabhsgsitslumAdmin(admin.ModelAdmin):
	list_display = [f.name for f in Areahabhsgsitslum._meta.fields]

admin.site.register(Areahabhsgsitslum, AreahabhsgsitslumAdmin)

class AreahabhsgsittownAdmin(admin.ModelAdmin):
	list_display = [f.name for f in Areahabhsgsittown._meta.fields]

admin.site.register(Areahabhsgsittown, AreahabhsgsittownAdmin)

class AreahabhsgsitwspAdmin(admin.ModelAdmin):
	list_display = [f.name for f in Areahabhsgsitwsp._meta.fields]

admin.site.register(Areahabhsgsitwsp, AreahabhsgsitwspAdmin)

class AreahabroofcountyAdmin(admin.ModelAdmin):
	list_display = [f.name for f in Areahabroofcounty._meta.fields]

admin.site.register(Areahabroofcounty, AreahabroofcountyAdmin)

class AreahabroofslumAdmin(admin.ModelAdmin):
	list_display = [f.name for f in Areahabroofslum._meta.fields]

admin.site.register(Areahabroofslum, AreahabroofslumAdmin)

class AreahabrooftownAdmin(admin.ModelAdmin):
	list_display = [f.name for f in Areahabrooftown._meta.fields]

admin.site.register(Areahabrooftown, AreahabrooftownAdmin)

class AreahabroofwspAdmin(admin.ModelAdmin):
	list_display = [f.name for f in Areahabroofwsp._meta.fields]

admin.site.register(Areahabroofwsp, AreahabroofwspAdmin)

class AreahabwallcountyAdmin(admin.ModelAdmin):
	list_display = [f.name for f in Areahabwallcounty._meta.fields]

admin.site.register(Areahabwallcounty, AreahabwallcountyAdmin)

class AreahabwallslumAdmin(admin.ModelAdmin):
	list_display = [f.name for f in Areahabwallslum._meta.fields]

admin.site.register(Areahabwallslum, AreahabwallslumAdmin)

class AreahabwalltownAdmin(admin.ModelAdmin):
	list_display = [f.name for f in Areahabwalltown._meta.fields]

admin.site.register(Areahabwalltown, AreahabwalltownAdmin)

class AreahabwallwspAdmin(admin.ModelAdmin):
	list_display = [f.name for f in Areahabwallwsp._meta.fields]

admin.site.register(Areahabwallwsp, AreahabwallwspAdmin)

class ArealistAdmin(admin.ModelAdmin):
	list_display = [f.name for f in Arealist._meta.fields]

admin.site.register(Arealist, ArealistAdmin)

class Arealist2Admin(admin.ModelAdmin):
	list_display = [f.name for f in Arealist2._meta.fields]

admin.site.register(Arealist2, Arealist2Admin)

class AreanospckskcountyAdmin(admin.ModelAdmin):
	list_display = [f.name for f in Areanospckskcounty._meta.fields]

admin.site.register(Areanospckskcounty, AreanospckskcountyAdmin)

class AreanospckskslumAdmin(admin.ModelAdmin):
	list_display = [f.name for f in Areanospckskslum._meta.fields]

admin.site.register(Areanospckskslum, AreanospckskslumAdmin)

class AreanospcksktownAdmin(admin.ModelAdmin):
	list_display = [f.name for f in Areanospcksktown._meta.fields]

admin.site.register(Areanospcksktown, AreanospcksktownAdmin)

class AreanospckskwspAdmin(admin.ModelAdmin):
	list_display = [f.name for f in Areanospckskwsp._meta.fields]

admin.site.register(Areanospckskwsp, AreanospckskwspAdmin)

class AreanospcpubsancountyAdmin(admin.ModelAdmin):
	list_display = [f.name for f in Areanospcpubsancounty._meta.fields]

admin.site.register(Areanospcpubsancounty, AreanospcpubsancountyAdmin)

class AreanospcpubsanslumAdmin(admin.ModelAdmin):
	list_display = [f.name for f in Areanospcpubsanslum._meta.fields]

admin.site.register(Areanospcpubsanslum, AreanospcpubsanslumAdmin)

class AreanospcpubsantownAdmin(admin.ModelAdmin):
	list_display = [f.name for f in Areanospcpubsantown._meta.fields]

admin.site.register(Areanospcpubsantown, AreanospcpubsantownAdmin)

class AreanospcpubsanwspAdmin(admin.ModelAdmin):
	list_display = [f.name for f in Areanospcpubsanwsp._meta.fields]

admin.site.register(Areanospcpubsanwsp, AreanospcpubsanwspAdmin)

class AreaownducountyAdmin(admin.ModelAdmin):
	list_display = [f.name for f in Areaownducounty._meta.fields]

admin.site.register(Areaownducounty, AreaownducountyAdmin)

class AreaownduslumAdmin(admin.ModelAdmin):
	list_display = [f.name for f in Areaownduslum._meta.fields]

admin.site.register(Areaownduslum, AreaownduslumAdmin)

class AreaowndutownAdmin(admin.ModelAdmin):
	list_display = [f.name for f in Areaowndutown._meta.fields]

admin.site.register(Areaowndutown, AreaowndutownAdmin)

class AreaownduwspAdmin(admin.ModelAdmin):
	list_display = [f.name for f in Areaownduwsp._meta.fields]

admin.site.register(Areaownduwsp, AreaownduwspAdmin)

class AreaphycharAdmin(admin.ModelAdmin):
	list_display = [f.name for f in Areaphychar._meta.fields]

admin.site.register(Areaphychar, AreaphycharAdmin)

class AreapopAdmin(admin.ModelAdmin):
	list_display = [f.name for f in Areapop._meta.fields]

admin.site.register(Areapop, AreapopAdmin)

class AreapopdensityAdmin(admin.ModelAdmin):
	list_display = [f.name for f in Areapopdensity._meta.fields]

admin.site.register(Areapopdensity, AreapopdensityAdmin)

class AreaprofilesAdmin(admin.ModelAdmin):
	list_display = [f.name for f in Areaprofiles._meta.fields]

admin.site.register(Areaprofiles, AreaprofilesAdmin)

class AreasubjfldcountyAdmin(admin.ModelAdmin):
	list_display = [f.name for f in Areasubjfldcounty._meta.fields]

admin.site.register(Areasubjfldcounty, AreasubjfldcountyAdmin)

class AreasubjfldslumAdmin(admin.ModelAdmin):
	list_display = [f.name for f in Areasubjfldslum._meta.fields]

admin.site.register(Areasubjfldslum, AreasubjfldslumAdmin)

class AreasubjfldtownAdmin(admin.ModelAdmin):
	list_display = [f.name for f in Areasubjfldtown._meta.fields]

admin.site.register(Areasubjfldtown, AreasubjfldtownAdmin)

class AreasubjfldwspAdmin(admin.ModelAdmin):
	list_display = [f.name for f in Areasubjfldwsp._meta.fields]

admin.site.register(Areasubjfldwsp, AreasubjfldwspAdmin)

class AreasummarysheetAdmin(admin.ModelAdmin):
	list_display = [f.name for f in Areasummarysheet._meta.fields]

admin.site.register(Areasummarysheet, AreasummarysheetAdmin)

class AreassettlocrdrlcountyAdmin(admin.ModelAdmin):
	list_display = [f.name for f in Areassettlocrdrlcounty._meta.fields]

admin.site.register(Areassettlocrdrlcounty, AreassettlocrdrlcountyAdmin)

class AreassettlocrdrlslumAdmin(admin.ModelAdmin):
	list_display = [f.name for f in Areassettlocrdrlslum._meta.fields]

admin.site.register(Areassettlocrdrlslum, AreassettlocrdrlslumAdmin)

class AreassettlocrdrltownAdmin(admin.ModelAdmin):
	list_display = [f.name for f in Areassettlocrdrltown._meta.fields]

admin.site.register(Areassettlocrdrltown, AreassettlocrdrltownAdmin)

class AreassettlocrdrlwspAdmin(admin.ModelAdmin):
	list_display = [f.name for f in Areassettlocrdrlwsp._meta.fields]

admin.site.register(Areassettlocrdrlwsp, AreassettlocrdrlwspAdmin)

class DemogtrendsAdmin(admin.ModelAdmin):
	list_display = [f.name for f in Demogtrends._meta.fields]

admin.site.register(Demogtrends, DemogtrendsAdmin)

class DevplansAdmin(admin.ModelAdmin):
	list_display = [f.name for f in Devplans._meta.fields]

admin.site.register(Devplans, DevplansAdmin)

class FemhhhscountyAdmin(admin.ModelAdmin):
	list_display = [f.name for f in Femhhhscounty._meta.fields]

admin.site.register(Femhhhscounty, FemhhhscountyAdmin)

class FemhhhsslumAdmin(admin.ModelAdmin):
	list_display = [f.name for f in Femhhhsslum._meta.fields]

admin.site.register(Femhhhsslum, FemhhhsslumAdmin)

class FemhhhstownAdmin(admin.ModelAdmin):
	list_display = [f.name for f in Femhhhstown._meta.fields]

admin.site.register(Femhhhstown, FemhhhstownAdmin)

class HabitationpatternsAdmin(admin.ModelAdmin):
	list_display = [f.name for f in Habitationpatterns._meta.fields]

admin.site.register(Habitationpatterns, HabitationpatternsAdmin)

class LandownuseAdmin(admin.ModelAdmin):
	list_display = [f.name for f in Landownuse._meta.fields]

admin.site.register(Landownuse, LandownuseAdmin)

class MajidatainfocountyAdmin(admin.ModelAdmin):
	list_display = [f.name for f in Majidatainfocounty._meta.fields]

admin.site.register(Majidatainfocounty, MajidatainfocountyAdmin)

class MajidatainfoslumAdmin(admin.ModelAdmin):
	list_display = [f.name for f in Majidatainfoslum._meta.fields]

admin.site.register(Majidatainfoslum, MajidatainfoslumAdmin)

class MajidatainfotwnAdmin(admin.ModelAdmin):
	list_display = [f.name for f in Majidatainfotwn._meta.fields]

admin.site.register(Majidatainfotwn, MajidatainfotwnAdmin)

class MajidatainfowspAdmin(admin.ModelAdmin):
	list_display = [f.name for f in Majidatainfowsp._meta.fields]

admin.site.register(Majidatainfowsp, MajidatainfowspAdmin)

class PavghhduszcountyAdmin(admin.ModelAdmin):
	list_display = [f.name for f in Pavghhduszcounty._meta.fields]

admin.site.register(Pavghhduszcounty, PavghhduszcountyAdmin)

class PavghhduszslumAdmin(admin.ModelAdmin):
	list_display = [f.name for f in Pavghhduszslum._meta.fields]

admin.site.register(Pavghhduszslum, PavghhduszslumAdmin)

class PavghhdusztownAdmin(admin.ModelAdmin):
	list_display = [f.name for f in Pavghhdusztown._meta.fields]

admin.site.register(Pavghhdusztown, PavghhdusztownAdmin)

class PhlthwasterdsAdmin(admin.ModelAdmin):
	list_display = [f.name for f in Phlthwasterds._meta.fields]

admin.site.register(Phlthwasterds, PhlthwasterdsAdmin)

class PownduwsrckskcountyAdmin(admin.ModelAdmin):
	list_display = [f.name for f in Pownduwsrckskcounty._meta.fields]

admin.site.register(Pownduwsrckskcounty, PownduwsrckskcountyAdmin)

class PownduwsrckskslumAdmin(admin.ModelAdmin):
	list_display = [f.name for f in Pownduwsrckskslum._meta.fields]

admin.site.register(Pownduwsrckskslum, PownduwsrckskslumAdmin)

class PownduwsrcksktownAdmin(admin.ModelAdmin):
	list_display = [f.name for f in Pownduwsrcksktown._meta.fields]

admin.site.register(Pownduwsrcksktown, PownduwsrcksktownAdmin)

class PownduwsrckskwspAdmin(admin.ModelAdmin):
	list_display = [f.name for f in Pownduwsrckskwsp._meta.fields]

admin.site.register(Pownduwsrckskwsp, PownduwsrckskwspAdmin)

class PownduwsrcpipedcountyAdmin(admin.ModelAdmin):
	list_display = [f.name for f in Pownduwsrcpipedcounty._meta.fields]

admin.site.register(Pownduwsrcpipedcounty, PownduwsrcpipedcountyAdmin)

class PownduwsrcpipedslumAdmin(admin.ModelAdmin):
	list_display = [f.name for f in Pownduwsrcpipedslum._meta.fields]

admin.site.register(Pownduwsrcpipedslum, PownduwsrcpipedslumAdmin)

class PownduwsrcpipedtownAdmin(admin.ModelAdmin):
	list_display = [f.name for f in Pownduwsrcpipedtown._meta.fields]

admin.site.register(Pownduwsrcpipedtown, PownduwsrcpipedtownAdmin)

class PownduwsrcpipedwspAdmin(admin.ModelAdmin):
	list_display = [f.name for f in Pownduwsrcpipedwsp._meta.fields]

admin.site.register(Pownduwsrcpipedwsp, PownduwsrcpipedwspAdmin)

class PreligioncountyAdmin(admin.ModelAdmin):
	list_display = [f.name for f in Preligioncounty._meta.fields]

admin.site.register(Preligioncounty, PreligioncountyAdmin)

class PreligionslumAdmin(admin.ModelAdmin):
	list_display = [f.name for f in Preligionslum._meta.fields]

admin.site.register(Preligionslum, PreligionslumAdmin)

class PreligiontownAdmin(admin.ModelAdmin):
	list_display = [f.name for f in Preligiontown._meta.fields]

admin.site.register(Preligiontown, PreligiontownAdmin)

class PreligionwspAdmin(admin.ModelAdmin):
	list_display = [f.name for f in Preligionwsp._meta.fields]

admin.site.register(Preligionwsp, PreligionwspAdmin)

class PopareabysettlementcountyAdmin(admin.ModelAdmin):
	list_display = [f.name for f in Popareabysettlementcounty._meta.fields]

admin.site.register(Popareabysettlementcounty, PopareabysettlementcountyAdmin)

class PopareabysettlementslumAdmin(admin.ModelAdmin):
	list_display = [f.name for f in Popareabysettlementslum._meta.fields]

admin.site.register(Popareabysettlementslum, PopareabysettlementslumAdmin)

class PopareabysettlementtownAdmin(admin.ModelAdmin):
	list_display = [f.name for f in Popareabysettlementtown._meta.fields]

admin.site.register(Popareabysettlementtown, PopareabysettlementtownAdmin)

class PopareatypecountyAdmin(admin.ModelAdmin):
	list_display = [f.name for f in Popareatypecounty._meta.fields]

admin.site.register(Popareatypecounty, PopareatypecountyAdmin)

class PopareatypeslumAdmin(admin.ModelAdmin):
	list_display = [f.name for f in Popareatypeslum._meta.fields]

admin.site.register(Popareatypeslum, PopareatypeslumAdmin)

class PopareatypetownAdmin(admin.ModelAdmin):
	list_display = [f.name for f in Popareatypetown._meta.fields]

admin.site.register(Popareatypetown, PopareatypetownAdmin)

class PopareatypewspAdmin(admin.ModelAdmin):
	list_display = [f.name for f in Popareatypewsp._meta.fields]

admin.site.register(Popareatypewsp, PopareatypewspAdmin)

class PopareasbylegalcountyAdmin(admin.ModelAdmin):
	list_display = [f.name for f in Popareasbylegalcounty._meta.fields]

admin.site.register(Popareasbylegalcounty, PopareasbylegalcountyAdmin)

class PopareasbylegalslumAdmin(admin.ModelAdmin):
	list_display = [f.name for f in Popareasbylegalslum._meta.fields]

admin.site.register(Popareasbylegalslum, PopareasbylegalslumAdmin)

class PopareasbylegaltownAdmin(admin.ModelAdmin):
	list_display = [f.name for f in Popareasbylegaltown._meta.fields]

admin.site.register(Popareasbylegaltown, PopareasbylegaltownAdmin)

class Savgdush44CountyAdmin(admin.ModelAdmin):
	list_display = [f.name for f in Savgdush44County._meta.fields]

admin.site.register(Savgdush44County, Savgdush44CountyAdmin)

class Savgdush44SlumAdmin(admin.ModelAdmin):
	list_display = [f.name for f in Savgdush44Slum._meta.fields]

admin.site.register(Savgdush44Slum, Savgdush44SlumAdmin)

class Savgdush44WspAdmin(admin.ModelAdmin):
	list_display = [f.name for f in Savgdush44Wsp._meta.fields]

admin.site.register(Savgdush44Wsp, Savgdush44WspAdmin)

class SavgdusshfaccountyAdmin(admin.ModelAdmin):
	list_display = [f.name for f in Savgdusshfaccounty._meta.fields]

admin.site.register(Savgdusshfaccounty, SavgdusshfaccountyAdmin)

class SavgdusshfacslumAdmin(admin.ModelAdmin):
	list_display = [f.name for f in Savgdusshfacslum._meta.fields]

admin.site.register(Savgdusshfacslum, SavgdusshfacslumAdmin)

class SavgdusshfacwspAdmin(admin.ModelAdmin):
	list_display = [f.name for f in Savgdusshfacwsp._meta.fields]

admin.site.register(Savgdusshfacwsp, SavgdusshfacwspAdmin)

class SavghhshowntltAdmin(admin.ModelAdmin):
	list_display = [f.name for f in Savghhshowntlt._meta.fields]

admin.site.register(Savghhshowntlt, SavghhshowntltAdmin)

class SavgtltbathAdmin(admin.ModelAdmin):
	list_display = [f.name for f in Savgtltbath._meta.fields]

admin.site.register(Savgtltbath, SavgtltbathAdmin)

class SduhasownbathAdmin(admin.ModelAdmin):
	list_display = [f.name for f in Sduhasownbath._meta.fields]

admin.site.register(Sduhasownbath, SduhasownbathAdmin)

class SduhasownfacilityAdmin(admin.ModelAdmin):
	list_display = [f.name for f in Sduhasownfacility._meta.fields]

admin.site.register(Sduhasownfacility, SduhasownfacilityAdmin)

class Sduownbath45CountyAdmin(admin.ModelAdmin):
	list_display = [f.name for f in Sduownbath45County._meta.fields]

admin.site.register(Sduownbath45County, Sduownbath45CountyAdmin)

class Sduownbath45SlumAdmin(admin.ModelAdmin):
	list_display = [f.name for f in Sduownbath45Slum._meta.fields]

admin.site.register(Sduownbath45Slum, Sduownbath45SlumAdmin)

class Sduownbath45WspAdmin(admin.ModelAdmin):
	list_display = [f.name for f in Sduownbath45Wsp._meta.fields]

admin.site.register(Sduownbath45Wsp, Sduownbath45WspAdmin)

class Sduownfac45CountyAdmin(admin.ModelAdmin):
	list_display = [f.name for f in Sduownfac45County._meta.fields]

admin.site.register(Sduownfac45County, Sduownfac45CountyAdmin)

class Sduownfac45SlumAdmin(admin.ModelAdmin):
	list_display = [f.name for f in Sduownfac45Slum._meta.fields]

admin.site.register(Sduownfac45Slum, Sduownfac45SlumAdmin)

class Sduownfac45WspAdmin(admin.ModelAdmin):
	list_display = [f.name for f in Sduownfac45Wsp._meta.fields]

admin.site.register(Sduownfac45Wsp, Sduownfac45WspAdmin)

class Sduownrpit45CountyAdmin(admin.ModelAdmin):
	list_display = [f.name for f in Sduownrpit45County._meta.fields]

admin.site.register(Sduownrpit45County, Sduownrpit45CountyAdmin)

class Sduownrpit45SlumAdmin(admin.ModelAdmin):
	list_display = [f.name for f in Sduownrpit45Slum._meta.fields]

admin.site.register(Sduownrpit45Slum, Sduownrpit45SlumAdmin)

class Sduownrpit45WspAdmin(admin.ModelAdmin):
	list_display = [f.name for f in Sduownrpit45Wsp._meta.fields]

admin.site.register(Sduownrpit45Wsp, Sduownrpit45WspAdmin)

class SdusharestoiletAdmin(admin.ModelAdmin):
	list_display = [f.name for f in Sdusharestoilet._meta.fields]

admin.site.register(Sdusharestoilet, SdusharestoiletAdmin)

class SeincomesrcsAdmin(admin.ModelAdmin):
	list_display = [f.name for f in Seincomesrcs._meta.fields]

admin.site.register(Seincomesrcs, SeincomesrcsAdmin)

class SfacinplotcountyAdmin(admin.ModelAdmin):
	list_display = [f.name for f in Sfacinplotcounty._meta.fields]

admin.site.register(Sfacinplotcounty, SfacinplotcountyAdmin)

class SfacinplotslumAdmin(admin.ModelAdmin):
	list_display = [f.name for f in Sfacinplotslum._meta.fields]

admin.site.register(Sfacinplotslum, SfacinplotslumAdmin)

class SfacinplotwspAdmin(admin.ModelAdmin):
	list_display = [f.name for f in Sfacinplotwsp._meta.fields]

admin.site.register(Sfacinplotwsp, SfacinplotwspAdmin)

class SfacsharedcountyAdmin(admin.ModelAdmin):
	list_display = [f.name for f in Sfacsharedcounty._meta.fields]

admin.site.register(Sfacsharedcounty, SfacsharedcountyAdmin)

class SfacsharedslumAdmin(admin.ModelAdmin):
	list_display = [f.name for f in Sfacsharedslum._meta.fields]

admin.site.register(Sfacsharedslum, SfacsharedslumAdmin)

class SfacsharedwspAdmin(admin.ModelAdmin):
	list_display = [f.name for f in Sfacsharedwsp._meta.fields]

admin.site.register(Sfacsharedwsp, SfacsharedwspAdmin)

class SfactypesAdmin(admin.ModelAdmin):
	list_display = [f.name for f in Sfactypes._meta.fields]

admin.site.register(Sfactypes, SfactypesAdmin)

class SimpjmpAdmin(admin.ModelAdmin):
	list_display = [f.name for f in Simpjmp._meta.fields]

admin.site.register(Simpjmp, SimpjmpAdmin)

class SimpjmpcountyAdmin(admin.ModelAdmin):
	list_display = [f.name for f in Simpjmpcounty._meta.fields]

admin.site.register(Simpjmpcounty, SimpjmpcountyAdmin)

class SimpjmpownfacAdmin(admin.ModelAdmin):
	list_display = [f.name for f in Simpjmpownfac._meta.fields]

admin.site.register(Simpjmpownfac, SimpjmpownfacAdmin)

class SimpjmpownplotfacAdmin(admin.ModelAdmin):
	list_display = [f.name for f in Simpjmpownplotfac._meta.fields]

admin.site.register(Simpjmpownplotfac, SimpjmpownplotfacAdmin)

class SimpjmpshfacAdmin(admin.ModelAdmin):
	list_display = [f.name for f in Simpjmpshfac._meta.fields]

admin.site.register(Simpjmpshfac, SimpjmpshfacAdmin)

class SimpjmpsharedcountyAdmin(admin.ModelAdmin):
	list_display = [f.name for f in Simpjmpsharedcounty._meta.fields]

admin.site.register(Simpjmpsharedcounty, SimpjmpsharedcountyAdmin)

class SimpjmpsharedslumAdmin(admin.ModelAdmin):
	list_display = [f.name for f in Simpjmpsharedslum._meta.fields]

admin.site.register(Simpjmpsharedslum, SimpjmpsharedslumAdmin)

class SimpjmpsharedwspAdmin(admin.ModelAdmin):
	list_display = [f.name for f in Simpjmpsharedwsp._meta.fields]

admin.site.register(Simpjmpsharedwsp, SimpjmpsharedwspAdmin)

class SimpjmpslumAdmin(admin.ModelAdmin):
	list_display = [f.name for f in Simpjmpslum._meta.fields]

admin.site.register(Simpjmpslum, SimpjmpslumAdmin)

class SimpjmpwspAdmin(admin.ModelAdmin):
	list_display = [f.name for f in Simpjmpwsp._meta.fields]

admin.site.register(Simpjmpwsp, SimpjmpwspAdmin)

class SnofacusedAdmin(admin.ModelAdmin):
	list_display = [f.name for f in Snofacused._meta.fields]

admin.site.register(Snofacused, SnofacusedAdmin)

class SnofacusedcountyAdmin(admin.ModelAdmin):
	list_display = [f.name for f in Snofacusedcounty._meta.fields]

admin.site.register(Snofacusedcounty, SnofacusedcountyAdmin)

class SnofacusedslumAdmin(admin.ModelAdmin):
	list_display = [f.name for f in Snofacusedslum._meta.fields]

admin.site.register(Snofacusedslum, SnofacusedslumAdmin)

class SnofacusedwspAdmin(admin.ModelAdmin):
	list_display = [f.name for f in Snofacusedwsp._meta.fields]

admin.site.register(Snofacusedwsp, SnofacusedwspAdmin)

class SnoofbathsAdmin(admin.ModelAdmin):
	list_display = [f.name for f in Snoofbaths._meta.fields]

admin.site.register(Snoofbaths, SnoofbathsAdmin)

class SnoofdushrngtltAdmin(admin.ModelAdmin):
	list_display = [f.name for f in Snoofdushrngtlt._meta.fields]

admin.site.register(Snoofdushrngtlt, SnoofdushrngtltAdmin)

class SnooffacilitiesAdmin(admin.ModelAdmin):
	list_display = [f.name for f in Snooffacilities._meta.fields]

admin.site.register(Snooffacilities, SnooffacilitiesAdmin)

class SownimpjmpcountyAdmin(admin.ModelAdmin):
	list_display = [f.name for f in Sownimpjmpcounty._meta.fields]

admin.site.register(Sownimpjmpcounty, SownimpjmpcountyAdmin)

class SownimpjmpslumAdmin(admin.ModelAdmin):
	list_display = [f.name for f in Sownimpjmpslum._meta.fields]

admin.site.register(Sownimpjmpslum, SownimpjmpslumAdmin)

class SownimpjmpwspAdmin(admin.ModelAdmin):
	list_display = [f.name for f in Sownimpjmpwsp._meta.fields]

admin.site.register(Sownimpjmpwsp, SownimpjmpwspAdmin)

class SpracticeAdmin(admin.ModelAdmin):
	list_display = [f.name for f in Spractice._meta.fields]

admin.site.register(Spractice, SpracticeAdmin)

class SsepbathsAdmin(admin.ModelAdmin):
	list_display = [f.name for f in Ssepbaths._meta.fields]

admin.site.register(Ssepbaths, SsepbathsAdmin)

class SseptoiletsAdmin(admin.ModelAdmin):
	list_display = [f.name for f in Sseptoilets._meta.fields]

admin.site.register(Sseptoilets, SseptoiletsAdmin)

class SwduhasownrpitAdmin(admin.ModelAdmin):
	list_display = [f.name for f in Swduhasownrpit._meta.fields]

admin.site.register(Swduhasownrpit, SwduhasownrpitAdmin)

class SwnoofrubpitsAdmin(admin.ModelAdmin):
	list_display = [f.name for f in Swnoofrubpits._meta.fields]

admin.site.register(Swnoofrubpits, SwnoofrubpitsAdmin)

class SwrpitsharedAdmin(admin.ModelAdmin):
	list_display = [f.name for f in Swrpitshared._meta.fields]

admin.site.register(Swrpitshared, SwrpitsharedAdmin)

class SanfacpractcountyAdmin(admin.ModelAdmin):
	list_display = [f.name for f in Sanfacpractcounty._meta.fields]

admin.site.register(Sanfacpractcounty, SanfacpractcountyAdmin)

class SanfacpractslumAdmin(admin.ModelAdmin):
	list_display = [f.name for f in Sanfacpractslum._meta.fields]

admin.site.register(Sanfacpractslum, SanfacpractslumAdmin)

class SanfacpractwspAdmin(admin.ModelAdmin):
	list_display = [f.name for f in Sanfacpractwsp._meta.fields]

admin.site.register(Sanfacpractwsp, SanfacpractwspAdmin)

class Sanitation12BAdmin(admin.ModelAdmin):
	list_display = [f.name for f in Sanitation12B._meta.fields]

admin.site.register(Sanitation12B, Sanitation12BAdmin)

class SanitationpracticeAdmin(admin.ModelAdmin):
	list_display = [f.name for f in Sanitationpractice._meta.fields]

admin.site.register(Sanitationpractice, SanitationpracticeAdmin)

class SanitationsewlnkAdmin(admin.ModelAdmin):
	list_display = [f.name for f in Sanitationsewlnk._meta.fields]

admin.site.register(Sanitationsewlnk, SanitationsewlnkAdmin)

class SocioeconinfrAdmin(admin.ModelAdmin):
	list_display = [f.name for f in Socioeconinfr._meta.fields]

admin.site.register(Socioeconinfr, SocioeconinfrAdmin)

class SownimpntshcountyAdmin(admin.ModelAdmin):
	list_display = [f.name for f in Sownimpntshcounty._meta.fields]

admin.site.register(Sownimpntshcounty, SownimpntshcountyAdmin)

class SownimpntshslumAdmin(admin.ModelAdmin):
	list_display = [f.name for f in Sownimpntshslum._meta.fields]

admin.site.register(Sownimpntshslum, SownimpntshslumAdmin)

class SownimpntshunpcountyAdmin(admin.ModelAdmin):
	list_display = [f.name for f in Sownimpntshunpcounty._meta.fields]

admin.site.register(Sownimpntshunpcounty, SownimpntshunpcountyAdmin)

class SownimpntshunpslumAdmin(admin.ModelAdmin):
	list_display = [f.name for f in Sownimpntshunpslum._meta.fields]

admin.site.register(Sownimpntshunpslum, SownimpntshunpslumAdmin)

class SownimpntshunpwspAdmin(admin.ModelAdmin):
	list_display = [f.name for f in Sownimpntshunpwsp._meta.fields]

admin.site.register(Sownimpntshunpwsp, SownimpntshunpwspAdmin)

class SownimpntshwspAdmin(admin.ModelAdmin):
	list_display = [f.name for f in Sownimpntshwsp._meta.fields]

admin.site.register(Sownimpntshwsp, SownimpntshwspAdmin)

class SummaryshtcountyAdmin(admin.ModelAdmin):
	list_display = [f.name for f in Summaryshtcounty._meta.fields]

admin.site.register(Summaryshtcounty, SummaryshtcountyAdmin)

class SummaryshtslumAdmin(admin.ModelAdmin):
	list_display = [f.name for f in Summaryshtslum._meta.fields]

admin.site.register(Summaryshtslum, SummaryshtslumAdmin)

class SummaryshttownAdmin(admin.ModelAdmin):
	list_display = [f.name for f in Summaryshttown._meta.fields]

admin.site.register(Summaryshttown, SummaryshttownAdmin)

class TownsareasCountiesAdmin(admin.ModelAdmin):
	list_display = [f.name for f in TownsareasCounties._meta.fields]

admin.site.register(TownsareasCounties, TownsareasCountiesAdmin)

class TownsareasSlumAdmin(admin.ModelAdmin):
	list_display = [f.name for f in TownsareasSlum._meta.fields]

admin.site.register(TownsareasSlum, TownsareasSlumAdmin)

class TownsareasTownsAdmin(admin.ModelAdmin):
	list_display = [f.name for f in TownsareasTowns._meta.fields]

admin.site.register(TownsareasTowns, TownsareasTownsAdmin)

class TownsareasWspAdmin(admin.ModelAdmin):
	list_display = [f.name for f in TownsareasWsp._meta.fields]

admin.site.register(TownsareasWsp, TownsareasWspAdmin)

class WadeqsupallkskAdmin(admin.ModelAdmin):
	list_display = [f.name for f in Wadeqsupallksk._meta.fields]

admin.site.register(Wadeqsupallksk, WadeqsupallkskAdmin)

class WadeqsupimpwstfsrcsAdmin(admin.ModelAdmin):
	list_display = [f.name for f in Wadeqsupimpwstfsrcs._meta.fields]

admin.site.register(Wadeqsupimpwstfsrcs, WadeqsupimpwstfsrcsAdmin)

class Wadeqsupprivcons10DAdmin(admin.ModelAdmin):
	list_display = [f.name for f in Wadeqsupprivcons10D._meta.fields]

admin.site.register(Wadeqsupprivcons10D, Wadeqsupprivcons10DAdmin)

class Wadeqsuppubtap10DAdmin(admin.ModelAdmin):
	list_display = [f.name for f in Wadeqsuppubtap10D._meta.fields]

admin.site.register(Wadeqsuppubtap10D, Wadeqsuppubtap10DAdmin)

class WadeqsupwspkskAdmin(admin.ModelAdmin):
	list_display = [f.name for f in Wadeqsupwspksk._meta.fields]

admin.site.register(Wadeqsupwspksk, WadeqsupwspkskAdmin)

class Wareasmnprob33CountyAdmin(admin.ModelAdmin):
	list_display = [f.name for f in Wareasmnprob33County._meta.fields]

admin.site.register(Wareasmnprob33County, Wareasmnprob33CountyAdmin)

class Wareasmnprob33SlumAdmin(admin.ModelAdmin):
	list_display = [f.name for f in Wareasmnprob33Slum._meta.fields]

admin.site.register(Wareasmnprob33Slum, Wareasmnprob33SlumAdmin)

class Wareasmnprob33TownAdmin(admin.ModelAdmin):
	list_display = [f.name for f in Wareasmnprob33Town._meta.fields]

admin.site.register(Wareasmnprob33Town, Wareasmnprob33TownAdmin)

class Wareasmnprob33WspAdmin(admin.ModelAdmin):
	list_display = [f.name for f in Wareasmnprob33Wsp._meta.fields]

admin.site.register(Wareasmnprob33Wsp, Wareasmnprob33WspAdmin)

class WareasnwlinkcountyAdmin(admin.ModelAdmin):
	list_display = [f.name for f in Wareasnwlinkcounty._meta.fields]

admin.site.register(Wareasnwlinkcounty, WareasnwlinkcountyAdmin)

class WareasnwlinkslumAdmin(admin.ModelAdmin):
	list_display = [f.name for f in Wareasnwlinkslum._meta.fields]

admin.site.register(Wareasnwlinkslum, WareasnwlinkslumAdmin)

class WareasnwlinktownAdmin(admin.ModelAdmin):
	list_display = [f.name for f in Wareasnwlinktown._meta.fields]

admin.site.register(Wareasnwlinktown, WareasnwlinktownAdmin)

class WareasnwlinkwspAdmin(admin.ModelAdmin):
	list_display = [f.name for f in Wareasnwlinkwsp._meta.fields]

admin.site.register(Wareasnwlinkwsp, WareasnwlinkwspAdmin)

class WareastechstatcountyAdmin(admin.ModelAdmin):
	list_display = [f.name for f in Wareastechstatcounty._meta.fields]

admin.site.register(Wareastechstatcounty, WareastechstatcountyAdmin)

class WareastechstatslumAdmin(admin.ModelAdmin):
	list_display = [f.name for f in Wareastechstatslum._meta.fields]

admin.site.register(Wareastechstatslum, WareastechstatslumAdmin)

class WareastechstattownAdmin(admin.ModelAdmin):
	list_display = [f.name for f in Wareastechstattown._meta.fields]

admin.site.register(Wareastechstattown, WareastechstattownAdmin)

class WareastechstatwspAdmin(admin.ModelAdmin):
	list_display = [f.name for f in Wareastechstatwsp._meta.fields]

admin.site.register(Wareastechstatwsp, WareastechstatwspAdmin)

class WckgsrcpipedcountyAdmin(admin.ModelAdmin):
	list_display = [f.name for f in Wckgsrcpipedcounty._meta.fields]

admin.site.register(Wckgsrcpipedcounty, WckgsrcpipedcountyAdmin)

class WckgsrcpipedslumAdmin(admin.ModelAdmin):
	list_display = [f.name for f in Wckgsrcpipedslum._meta.fields]

admin.site.register(Wckgsrcpipedslum, WckgsrcpipedslumAdmin)

class WckgsrcpipedtownAdmin(admin.ModelAdmin):
	list_display = [f.name for f in Wckgsrcpipedtown._meta.fields]

admin.site.register(Wckgsrcpipedtown, WckgsrcpipedtownAdmin)

class WckgsrcpipedwspAdmin(admin.ModelAdmin):
	list_display = [f.name for f in Wckgsrcpipedwsp._meta.fields]

admin.site.register(Wckgsrcpipedwsp, WckgsrcpipedwspAdmin)

class WconstatusDuAdmin(admin.ModelAdmin):
	list_display = [f.name for f in WconstatusDu._meta.fields]

admin.site.register(WconstatusDu, WconstatusDuAdmin)

class Wconstatus34CountyAdmin(admin.ModelAdmin):
	list_display = [f.name for f in Wconstatus34County._meta.fields]

admin.site.register(Wconstatus34County, Wconstatus34CountyAdmin)

class Wconstatus34SlumAdmin(admin.ModelAdmin):
	list_display = [f.name for f in Wconstatus34Slum._meta.fields]

admin.site.register(Wconstatus34Slum, Wconstatus34SlumAdmin)

class Wconstatus34TownAdmin(admin.ModelAdmin):
	list_display = [f.name for f in Wconstatus34Town._meta.fields]

admin.site.register(Wconstatus34Town, Wconstatus34TownAdmin)

class Wconstatus34WspAdmin(admin.ModelAdmin):
	list_display = [f.name for f in Wconstatus34Wsp._meta.fields]

admin.site.register(Wconstatus34Wsp, Wconstatus34WspAdmin)

class WconsumptionAdmin(admin.ModelAdmin):
	list_display = [f.name for f in Wconsumption._meta.fields]

admin.site.register(Wconsumption, WconsumptionAdmin)

class WduconcountyAdmin(admin.ModelAdmin):
	list_display = [f.name for f in Wduconcounty._meta.fields]

admin.site.register(Wduconcounty, WduconcountyAdmin)

class WduconmetcountyAdmin(admin.ModelAdmin):
	list_display = [f.name for f in Wduconmetcounty._meta.fields]

admin.site.register(Wduconmetcounty, WduconmetcountyAdmin)

class WduconmetslumAdmin(admin.ModelAdmin):
	list_display = [f.name for f in Wduconmetslum._meta.fields]

admin.site.register(Wduconmetslum, WduconmetslumAdmin)

class WduconmettownAdmin(admin.ModelAdmin):
	list_display = [f.name for f in Wduconmettown._meta.fields]

admin.site.register(Wduconmettown, WduconmettownAdmin)

class WduconmetwspAdmin(admin.ModelAdmin):
	list_display = [f.name for f in Wduconmetwsp._meta.fields]

admin.site.register(Wduconmetwsp, WduconmetwspAdmin)

class WduconslumAdmin(admin.ModelAdmin):
	list_display = [f.name for f in Wduconslum._meta.fields]

admin.site.register(Wduconslum, WduconslumAdmin)

class WducontownAdmin(admin.ModelAdmin):
	list_display = [f.name for f in Wducontown._meta.fields]

admin.site.register(Wducontown, WducontownAdmin)

class WduconwspAdmin(admin.ModelAdmin):
	list_display = [f.name for f in Wduconwsp._meta.fields]

admin.site.register(Wduconwsp, WduconwspAdmin)

class WduownconAdmin(admin.ModelAdmin):
	list_display = [f.name for f in Wduowncon._meta.fields]

admin.site.register(Wduowncon, WduownconAdmin)

class Wduowncon210DAdmin(admin.ModelAdmin):
	list_display = [f.name for f in Wduowncon210D._meta.fields]

admin.site.register(Wduowncon210D, Wduowncon210DAdmin)

class WduownconmetAdmin(admin.ModelAdmin):
	list_display = [f.name for f in Wduownconmet._meta.fields]

admin.site.register(Wduownconmet, WduownconmetAdmin)

class Wduownconmet210DAdmin(admin.ModelAdmin):
	list_display = [f.name for f in Wduownconmet210D._meta.fields]

admin.site.register(Wduownconmet210D, Wduownconmet210DAdmin)

class WduwaterpaycountyAdmin(admin.ModelAdmin):
	list_display = [f.name for f in Wduwaterpaycounty._meta.fields]

admin.site.register(Wduwaterpaycounty, WduwaterpaycountyAdmin)

class WduwaterpayslumAdmin(admin.ModelAdmin):
	list_display = [f.name for f in Wduwaterpayslum._meta.fields]

admin.site.register(Wduwaterpayslum, WduwaterpayslumAdmin)

class WduwaterpaytownAdmin(admin.ModelAdmin):
	list_display = [f.name for f in Wduwaterpaytown._meta.fields]

admin.site.register(Wduwaterpaytown, WduwaterpaytownAdmin)

class WduwaterpaywspAdmin(admin.ModelAdmin):
	list_display = [f.name for f in Wduwaterpaywsp._meta.fields]

admin.site.register(Wduwaterpaywsp, WduwaterpaywspAdmin)

class Wdrkqlty33CountyAdmin(admin.ModelAdmin):
	list_display = [f.name for f in Wdrkqlty33County._meta.fields]

admin.site.register(Wdrkqlty33County, Wdrkqlty33CountyAdmin)

class Wdrkqlty33SlumAdmin(admin.ModelAdmin):
	list_display = [f.name for f in Wdrkqlty33Slum._meta.fields]

admin.site.register(Wdrkqlty33Slum, Wdrkqlty33SlumAdmin)

class Wdrkqlty33TownAdmin(admin.ModelAdmin):
	list_display = [f.name for f in Wdrkqlty33Town._meta.fields]

admin.site.register(Wdrkqlty33Town, Wdrkqlty33TownAdmin)

class Wdrkqlty33WspAdmin(admin.ModelAdmin):
	list_display = [f.name for f in Wdrkqlty33Wsp._meta.fields]

admin.site.register(Wdrkqlty33Wsp, Wdrkqlty33WspAdmin)

class Wdrksrc33CountyAdmin(admin.ModelAdmin):
	list_display = [f.name for f in Wdrksrc33County._meta.fields]

admin.site.register(Wdrksrc33County, Wdrksrc33CountyAdmin)

class Wdrksrc33SlumAdmin(admin.ModelAdmin):
	list_display = [f.name for f in Wdrksrc33Slum._meta.fields]

admin.site.register(Wdrksrc33Slum, Wdrksrc33SlumAdmin)

class Wdrksrc33TownAdmin(admin.ModelAdmin):
	list_display = [f.name for f in Wdrksrc33Town._meta.fields]

admin.site.register(Wdrksrc33Town, Wdrksrc33TownAdmin)

class Wdrksrc33WspAdmin(admin.ModelAdmin):
	list_display = [f.name for f in Wdrksrc33Wsp._meta.fields]

admin.site.register(Wdrksrc33Wsp, Wdrksrc33WspAdmin)

class Wdrksrcbyqltycounty37Admin(admin.ModelAdmin):
	list_display = [f.name for f in Wdrksrcbyqltycounty37._meta.fields]

admin.site.register(Wdrksrcbyqltycounty37, Wdrksrcbyqltycounty37Admin)

class Wdrksrcbyqltyslum37Admin(admin.ModelAdmin):
	list_display = [f.name for f in Wdrksrcbyqltyslum37._meta.fields]

admin.site.register(Wdrksrcbyqltyslum37, Wdrksrcbyqltyslum37Admin)

class Wdrksrcbyqltytown37Admin(admin.ModelAdmin):
	list_display = [f.name for f in Wdrksrcbyqltytown37._meta.fields]

admin.site.register(Wdrksrcbyqltytown37, Wdrksrcbyqltytown37Admin)

class Wdrksrcbyqltywsp37Admin(admin.ModelAdmin):
	list_display = [f.name for f in Wdrksrcbyqltywsp37._meta.fields]

admin.site.register(Wdrksrcbyqltywsp37, Wdrksrcbyqltywsp37Admin)

class Wdrksrcbytrtmthdslum38Admin(admin.ModelAdmin):
	list_display = [f.name for f in Wdrksrcbytrtmthdslum38._meta.fields]

admin.site.register(Wdrksrcbytrtmthdslum38, Wdrksrcbytrtmthdslum38Admin)

class Wdrksrcbytrtmthdtown38Admin(admin.ModelAdmin):
	list_display = [f.name for f in Wdrksrcbytrtmthdtown38._meta.fields]

admin.site.register(Wdrksrcbytrtmthdtown38, Wdrksrcbytrtmthdtown38Admin)

class Wdrksrcbytrtmthdwsp38Admin(admin.ModelAdmin):
	list_display = [f.name for f in Wdrksrcbytrtmthdwsp38._meta.fields]

admin.site.register(Wdrksrcbytrtmthdwsp38, Wdrksrcbytrtmthdwsp38Admin)

class Wdrksrccmtaps10DAdmin(admin.ModelAdmin):
	list_display = [f.name for f in Wdrksrccmtaps10D._meta.fields]

admin.site.register(Wdrksrccmtaps10D, Wdrksrccmtaps10DAdmin)

class WdrksrcleakAdmin(admin.ModelAdmin):
	list_display = [f.name for f in Wdrksrcleak._meta.fields]

admin.site.register(Wdrksrcleak, WdrksrcleakAdmin)

class WdrksrcothconAdmin(admin.ModelAdmin):
	list_display = [f.name for f in Wdrksrcothcon._meta.fields]

admin.site.register(Wdrksrcothcon, WdrksrcothconAdmin)

class WdrksrcpipedcountyAdmin(admin.ModelAdmin):
	list_display = [f.name for f in Wdrksrcpipedcounty._meta.fields]

admin.site.register(Wdrksrcpipedcounty, WdrksrcpipedcountyAdmin)

class WdrksrcpipedslumAdmin(admin.ModelAdmin):
	list_display = [f.name for f in Wdrksrcpipedslum._meta.fields]

admin.site.register(Wdrksrcpipedslum, WdrksrcpipedslumAdmin)

class WdrksrcpipedtownAdmin(admin.ModelAdmin):
	list_display = [f.name for f in Wdrksrcpipedtown._meta.fields]

admin.site.register(Wdrksrcpipedtown, WdrksrcpipedtownAdmin)

class WdrksrcpipedwspAdmin(admin.ModelAdmin):
	list_display = [f.name for f in Wdrksrcpipedwsp._meta.fields]

admin.site.register(Wdrksrcpipedwsp, WdrksrcpipedwspAdmin)

class WdrksrcresellerAdmin(admin.ModelAdmin):
	list_display = [f.name for f in Wdrksrcreseller._meta.fields]

admin.site.register(Wdrksrcreseller, WdrksrcresellerAdmin)

class WdrksrcywellAdmin(admin.ModelAdmin):
	list_display = [f.name for f in Wdrksrcywell._meta.fields]

admin.site.register(Wdrksrcywell, WdrksrcywellAdmin)

class WfetchdurationduAdmin(admin.ModelAdmin):
	list_display = [f.name for f in Wfetchdurationdu._meta.fields]

admin.site.register(Wfetchdurationdu, WfetchdurationduAdmin)

class WimpdrksrcjmpAdmin(admin.ModelAdmin):
	list_display = [f.name for f in Wimpdrksrcjmp._meta.fields]

admin.site.register(Wimpdrksrcjmp, WimpdrksrcjmpAdmin)

class Wimpdrksrcjmp30MnAdmin(admin.ModelAdmin):
	list_display = [f.name for f in Wimpdrksrcjmp30Mn._meta.fields]

admin.site.register(Wimpdrksrcjmp30Mn, Wimpdrksrcjmp30MnAdmin)

class WimpdrksrcjmpbyqltyAdmin(admin.ModelAdmin):
	list_display = [f.name for f in Wimpdrksrcjmpbyqlty._meta.fields]

admin.site.register(Wimpdrksrcjmpbyqlty, WimpdrksrcjmpbyqltyAdmin)

class WimpdrksrcjmpbytrtAdmin(admin.ModelAdmin):
	list_display = [f.name for f in Wimpdrksrcjmpbytrt._meta.fields]

admin.site.register(Wimpdrksrcjmpbytrt, WimpdrksrcjmpbytrtAdmin)

class WimpdrksrcwstfAdmin(admin.ModelAdmin):
	list_display = [f.name for f in Wimpdrksrcwstf._meta.fields]

admin.site.register(Wimpdrksrcwstf, WimpdrksrcwstfAdmin)

class Wimpdrksrcwstf30MnAdmin(admin.ModelAdmin):
	list_display = [f.name for f in Wimpdrksrcwstf30Mn._meta.fields]

admin.site.register(Wimpdrksrcwstf30Mn, Wimpdrksrcwstf30MnAdmin)

class WimpdrksrcwstfbyqltyAdmin(admin.ModelAdmin):
	list_display = [f.name for f in Wimpdrksrcwstfbyqlty._meta.fields]

admin.site.register(Wimpdrksrcwstfbyqlty, WimpdrksrcwstfbyqltyAdmin)

class WimpdrksrcwstfbytrtAdmin(admin.ModelAdmin):
	list_display = [f.name for f in Wimpdrksrcwstfbytrt._meta.fields]

admin.site.register(Wimpdrksrcwstfbytrt, WimpdrksrcwstfbytrtAdmin)

class WimpsrcbathwstfcountyAdmin(admin.ModelAdmin):
	list_display = [f.name for f in Wimpsrcbathwstfcounty._meta.fields]

admin.site.register(Wimpsrcbathwstfcounty, WimpsrcbathwstfcountyAdmin)

class WimpsrcbathwstfslumAdmin(admin.ModelAdmin):
	list_display = [f.name for f in Wimpsrcbathwstfslum._meta.fields]

admin.site.register(Wimpsrcbathwstfslum, WimpsrcbathwstfslumAdmin)

class WimpsrcbathwstftownAdmin(admin.ModelAdmin):
	list_display = [f.name for f in Wimpsrcbathwstftown._meta.fields]

admin.site.register(Wimpsrcbathwstftown, WimpsrcbathwstftownAdmin)

class WimpsrcbathwstfwspAdmin(admin.ModelAdmin):
	list_display = [f.name for f in Wimpsrcbathwstfwsp._meta.fields]

admin.site.register(Wimpsrcbathwstfwsp, WimpsrcbathwstfwspAdmin)

class WimpsrcckgwstfcountyAdmin(admin.ModelAdmin):
	list_display = [f.name for f in Wimpsrcckgwstfcounty._meta.fields]

admin.site.register(Wimpsrcckgwstfcounty, WimpsrcckgwstfcountyAdmin)

class WimpsrcckgwstfslumAdmin(admin.ModelAdmin):
	list_display = [f.name for f in Wimpsrcckgwstfslum._meta.fields]

admin.site.register(Wimpsrcckgwstfslum, WimpsrcckgwstfslumAdmin)

class WimpsrcckgwstftownAdmin(admin.ModelAdmin):
	list_display = [f.name for f in Wimpsrcckgwstftown._meta.fields]

admin.site.register(Wimpsrcckgwstftown, WimpsrcckgwstftownAdmin)

class WimpsrcckgwstfwspAdmin(admin.ModelAdmin):
	list_display = [f.name for f in Wimpsrcckgwstfwsp._meta.fields]

admin.site.register(Wimpsrcckgwstfwsp, WimpsrcckgwstfwspAdmin)

class WimpsrcdrkwstfcountyAdmin(admin.ModelAdmin):
	list_display = [f.name for f in Wimpsrcdrkwstfcounty._meta.fields]

admin.site.register(Wimpsrcdrkwstfcounty, WimpsrcdrkwstfcountyAdmin)

class WimpsrcdrkwstfslumAdmin(admin.ModelAdmin):
	list_display = [f.name for f in Wimpsrcdrkwstfslum._meta.fields]

admin.site.register(Wimpsrcdrkwstfslum, WimpsrcdrkwstfslumAdmin)

class WimpsrcdrkwstfwspAdmin(admin.ModelAdmin):
	list_display = [f.name for f in Wimpsrcdrkwstfwsp._meta.fields]

admin.site.register(Wimpsrcdrkwstfwsp, WimpsrcdrkwstfwspAdmin)

class Wnocompubpsts10DAdmin(admin.ModelAdmin):
	list_display = [f.name for f in Wnocompubpsts10D._meta.fields]

admin.site.register(Wnocompubpsts10D, Wnocompubpsts10DAdmin)

class WoutletscountyAdmin(admin.ModelAdmin):
	list_display = [f.name for f in Woutletscounty._meta.fields]

admin.site.register(Woutletscounty, WoutletscountyAdmin)

class WoutletsslumAdmin(admin.ModelAdmin):
	list_display = [f.name for f in Woutletsslum._meta.fields]

admin.site.register(Woutletsslum, WoutletsslumAdmin)

class WoutletstownAdmin(admin.ModelAdmin):
	list_display = [f.name for f in Woutletstown._meta.fields]

admin.site.register(Woutletstown, WoutletstownAdmin)

class WoutletswspAdmin(admin.ModelAdmin):
	list_display = [f.name for f in Woutletswsp._meta.fields]

admin.site.register(Woutletswsp, WoutletswspAdmin)

class WpconcountyAdmin(admin.ModelAdmin):
	list_display = [f.name for f in Wpconcounty._meta.fields]

admin.site.register(Wpconcounty, WpconcountyAdmin)

class WpconmetcountyAdmin(admin.ModelAdmin):
	list_display = [f.name for f in Wpconmetcounty._meta.fields]

admin.site.register(Wpconmetcounty, WpconmetcountyAdmin)

class WpconmetslumAdmin(admin.ModelAdmin):
	list_display = [f.name for f in Wpconmetslum._meta.fields]

admin.site.register(Wpconmetslum, WpconmetslumAdmin)

class WpconmettownAdmin(admin.ModelAdmin):
	list_display = [f.name for f in Wpconmettown._meta.fields]

admin.site.register(Wpconmettown, WpconmettownAdmin)

class WpconmetwspAdmin(admin.ModelAdmin):
	list_display = [f.name for f in Wpconmetwsp._meta.fields]

admin.site.register(Wpconmetwsp, WpconmetwspAdmin)

class WpconslumAdmin(admin.ModelAdmin):
	list_display = [f.name for f in Wpconslum._meta.fields]

admin.site.register(Wpconslum, WpconslumAdmin)

class WpcontownAdmin(admin.ModelAdmin):
	list_display = [f.name for f in Wpcontown._meta.fields]

admin.site.register(Wpcontown, WpcontownAdmin)

class WpconwspAdmin(admin.ModelAdmin):
	list_display = [f.name for f in Wpconwsp._meta.fields]

admin.site.register(Wpconwsp, WpconwspAdmin)

class WpducondisconnectedAdmin(admin.ModelAdmin):
	list_display = [f.name for f in Wpducondisconnected._meta.fields]

admin.site.register(Wpducondisconnected, WpducondisconnectedAdmin)

class WpaydrkduAdmin(admin.ModelAdmin):
	list_display = [f.name for f in Wpaydrkdu._meta.fields]

admin.site.register(Wpaydrkdu, WpaydrkduAdmin)

class WpaynondrkduAdmin(admin.ModelAdmin):
	list_display = [f.name for f in Wpaynondrkdu._meta.fields]

admin.site.register(Wpaynondrkdu, WpaynondrkduAdmin)

class WpipedsrcbathAdmin(admin.ModelAdmin):
	list_display = [f.name for f in Wpipedsrcbath._meta.fields]

admin.site.register(Wpipedsrcbath, WpipedsrcbathAdmin)

class WpipedsrcdrkAdmin(admin.ModelAdmin):
	list_display = [f.name for f in Wpipedsrcdrk._meta.fields]

admin.site.register(Wpipedsrcdrk, WpipedsrcdrkAdmin)

class WpipedsrcdrkavgpayAdmin(admin.ModelAdmin):
	list_display = [f.name for f in Wpipedsrcdrkavgpay._meta.fields]

admin.site.register(Wpipedsrcdrkavgpay, WpipedsrcdrkavgpayAdmin)

class WpipedsrcdrktrtAdmin(admin.ModelAdmin):
	list_display = [f.name for f in Wpipedsrcdrktrt._meta.fields]

admin.site.register(Wpipedsrcdrktrt, WpipedsrcdrktrtAdmin)

class WplotconmetDuAdmin(admin.ModelAdmin):
	list_display = [f.name for f in WplotconmetDu._meta.fields]

admin.site.register(WplotconmetDu, WplotconmetDuAdmin)

class WplotconnectedDuAdmin(admin.ModelAdmin):
	list_display = [f.name for f in WplotconnectedDu._meta.fields]

admin.site.register(WplotconnectedDu, WplotconnectedDuAdmin)

class WrespercomtapcountyAdmin(admin.ModelAdmin):
	list_display = [f.name for f in Wrespercomtapcounty._meta.fields]

admin.site.register(Wrespercomtapcounty, WrespercomtapcountyAdmin)

class WrespercomtapslumAdmin(admin.ModelAdmin):
	list_display = [f.name for f in Wrespercomtapslum._meta.fields]

admin.site.register(Wrespercomtapslum, WrespercomtapslumAdmin)

class WrespercomtaptownAdmin(admin.ModelAdmin):
	list_display = [f.name for f in Wrespercomtaptown._meta.fields]

admin.site.register(Wrespercomtaptown, WrespercomtaptownAdmin)

class WrespercomtapwspAdmin(admin.ModelAdmin):
	list_display = [f.name for f in Wrespercomtapwsp._meta.fields]

admin.site.register(Wrespercomtapwsp, WrespercomtapwspAdmin)

class WresperpubcomkskscountyAdmin(admin.ModelAdmin):
	list_display = [f.name for f in Wresperpubcomkskscounty._meta.fields]

admin.site.register(Wresperpubcomkskscounty, WresperpubcomkskscountyAdmin)

class WresperpubcomksksslumAdmin(admin.ModelAdmin):
	list_display = [f.name for f in Wresperpubcomksksslum._meta.fields]

admin.site.register(Wresperpubcomksksslum, WresperpubcomksksslumAdmin)

class WresperpubcomkskstownAdmin(admin.ModelAdmin):
	list_display = [f.name for f in Wresperpubcomkskstown._meta.fields]

admin.site.register(Wresperpubcomkskstown, WresperpubcomkskstownAdmin)

class WresperpubcomkskswspAdmin(admin.ModelAdmin):
	list_display = [f.name for f in Wresperpubcomkskswsp._meta.fields]

admin.site.register(Wresperpubcomkskswsp, WresperpubcomkskswspAdmin)

class WresperpubwspcomtapscountyAdmin(admin.ModelAdmin):
	list_display = [f.name for f in Wresperpubwspcomtapscounty._meta.fields]

admin.site.register(Wresperpubwspcomtapscounty, WresperpubwspcomtapscountyAdmin)

class WresperpubwspcomtapsslumAdmin(admin.ModelAdmin):
	list_display = [f.name for f in Wresperpubwspcomtapsslum._meta.fields]

admin.site.register(Wresperpubwspcomtapsslum, WresperpubwspcomtapsslumAdmin)

class WresperpubwspcomtapstownAdmin(admin.ModelAdmin):
	list_display = [f.name for f in Wresperpubwspcomtapstown._meta.fields]

admin.site.register(Wresperpubwspcomtapstown, WresperpubwspcomtapstownAdmin)

class WresperpubwspcomtapswspAdmin(admin.ModelAdmin):
	list_display = [f.name for f in Wresperpubwspcomtapswsp._meta.fields]

admin.site.register(Wresperpubwspcomtapswsp, WresperpubwspcomtapswspAdmin)

class WresperpubwsptapcountyAdmin(admin.ModelAdmin):
	list_display = [f.name for f in Wresperpubwsptapcounty._meta.fields]

admin.site.register(Wresperpubwsptapcounty, WresperpubwsptapcountyAdmin)

class WresperpubwsptapslumAdmin(admin.ModelAdmin):
	list_display = [f.name for f in Wresperpubwsptapslum._meta.fields]

admin.site.register(Wresperpubwsptapslum, WresperpubwsptapslumAdmin)

class WresperpubwsptaptownAdmin(admin.ModelAdmin):
	list_display = [f.name for f in Wresperpubwsptaptown._meta.fields]

admin.site.register(Wresperpubwsptaptown, WresperpubwsptaptownAdmin)

class WresperpubwsptapwspAdmin(admin.ModelAdmin):
	list_display = [f.name for f in Wresperpubwsptapwsp._meta.fields]

admin.site.register(Wresperpubwsptapwsp, WresperpubwsptapwspAdmin)

class WresperwspkskcountyAdmin(admin.ModelAdmin):
	list_display = [f.name for f in Wresperwspkskcounty._meta.fields]

admin.site.register(Wresperwspkskcounty, WresperwspkskcountyAdmin)

class WresperwspkskslumAdmin(admin.ModelAdmin):
	list_display = [f.name for f in Wresperwspkskslum._meta.fields]

admin.site.register(Wresperwspkskslum, WresperwspkskslumAdmin)

class WresperwspksktownAdmin(admin.ModelAdmin):
	list_display = [f.name for f in Wresperwspksktown._meta.fields]

admin.site.register(Wresperwspksktown, WresperwspksktownAdmin)

class WresperwspkskwspAdmin(admin.ModelAdmin):
	list_display = [f.name for f in Wresperwspkskwsp._meta.fields]

admin.site.register(Wresperwspkskwsp, WresperwspkskwspAdmin)

class Wrespercompubpost10DAdmin(admin.ModelAdmin):
	list_display = [f.name for f in Wrespercompubpost10D._meta.fields]

admin.site.register(Wrespercompubpost10D, Wrespercompubpost10DAdmin)

class WsrcbathpipedcountyAdmin(admin.ModelAdmin):
	list_display = [f.name for f in Wsrcbathpipedcounty._meta.fields]

admin.site.register(Wsrcbathpipedcounty, WsrcbathpipedcountyAdmin)

class WsrcbathpipedslumAdmin(admin.ModelAdmin):
	list_display = [f.name for f in Wsrcbathpipedslum._meta.fields]

admin.site.register(Wsrcbathpipedslum, WsrcbathpipedslumAdmin)

class WsrcbathpipedtownAdmin(admin.ModelAdmin):
	list_display = [f.name for f in Wsrcbathpipedtown._meta.fields]

admin.site.register(Wsrcbathpipedtown, WsrcbathpipedtownAdmin)

class WsrcbathpipedwspAdmin(admin.ModelAdmin):
	list_display = [f.name for f in Wsrcbathpipedwsp._meta.fields]

admin.site.register(Wsrcbathpipedwsp, WsrcbathpipedwspAdmin)

class Wsrcckg33CountyAdmin(admin.ModelAdmin):
	list_display = [f.name for f in Wsrcckg33County._meta.fields]

admin.site.register(Wsrcckg33County, Wsrcckg33CountyAdmin)

class WsrcdrkbhpmpcountyAdmin(admin.ModelAdmin):
	list_display = [f.name for f in Wsrcdrkbhpmpcounty._meta.fields]

admin.site.register(Wsrcdrkbhpmpcounty, WsrcdrkbhpmpcountyAdmin)

class WsrcdrkbhpmpslumAdmin(admin.ModelAdmin):
	list_display = [f.name for f in Wsrcdrkbhpmpslum._meta.fields]

admin.site.register(Wsrcdrkbhpmpslum, WsrcdrkbhpmpslumAdmin)

class WsrcdrkbhpmptownAdmin(admin.ModelAdmin):
	list_display = [f.name for f in Wsrcdrkbhpmptown._meta.fields]

admin.site.register(Wsrcdrkbhpmptown, WsrcdrkbhpmptownAdmin)

class WsrcdrkbhpmpwspAdmin(admin.ModelAdmin):
	list_display = [f.name for f in Wsrcdrkbhpmpwsp._meta.fields]

admin.site.register(Wsrcdrkbhpmpwsp, WsrcdrkbhpmpwspAdmin)

class WsrcdrkkskAdmin(admin.ModelAdmin):
	list_display = [f.name for f in Wsrcdrkksk._meta.fields]

admin.site.register(Wsrcdrkksk, WsrcdrkkskAdmin)

class WsrcdrkleakcountyAdmin(admin.ModelAdmin):
	list_display = [f.name for f in Wsrcdrkleakcounty._meta.fields]

admin.site.register(Wsrcdrkleakcounty, WsrcdrkleakcountyAdmin)

class WsrcdrkleakslumAdmin(admin.ModelAdmin):
	list_display = [f.name for f in Wsrcdrkleakslum._meta.fields]

admin.site.register(Wsrcdrkleakslum, WsrcdrkleakslumAdmin)

class WsrcdrkleaktownAdmin(admin.ModelAdmin):
	list_display = [f.name for f in Wsrcdrkleaktown._meta.fields]

admin.site.register(Wsrcdrkleaktown, WsrcdrkleaktownAdmin)

class WsrcdrkleakwspAdmin(admin.ModelAdmin):
	list_display = [f.name for f in Wsrcdrkleakwsp._meta.fields]

admin.site.register(Wsrcdrkleakwsp, WsrcdrkleakwspAdmin)

class WsrcdrkspringcountyAdmin(admin.ModelAdmin):
	list_display = [f.name for f in Wsrcdrkspringcounty._meta.fields]

admin.site.register(Wsrcdrkspringcounty, WsrcdrkspringcountyAdmin)

class WsrcdrkspringslumAdmin(admin.ModelAdmin):
	list_display = [f.name for f in Wsrcdrkspringslum._meta.fields]

admin.site.register(Wsrcdrkspringslum, WsrcdrkspringslumAdmin)

class WsrcdrkspringtownAdmin(admin.ModelAdmin):
	list_display = [f.name for f in Wsrcdrkspringtown._meta.fields]

admin.site.register(Wsrcdrkspringtown, WsrcdrkspringtownAdmin)

class WsrcdrkspringwspAdmin(admin.ModelAdmin):
	list_display = [f.name for f in Wsrcdrkspringwsp._meta.fields]

admin.site.register(Wsrcdrkspringwsp, WsrcdrkspringwspAdmin)

class WsrcdrkvendorcountyAdmin(admin.ModelAdmin):
	list_display = [f.name for f in Wsrcdrkvendorcounty._meta.fields]

admin.site.register(Wsrcdrkvendorcounty, WsrcdrkvendorcountyAdmin)

class WsrcdrkvendorslumAdmin(admin.ModelAdmin):
	list_display = [f.name for f in Wsrcdrkvendorslum._meta.fields]

admin.site.register(Wsrcdrkvendorslum, WsrcdrkvendorslumAdmin)

class WsrcdrkvendortownAdmin(admin.ModelAdmin):
	list_display = [f.name for f in Wsrcdrkvendortown._meta.fields]

admin.site.register(Wsrcdrkvendortown, WsrcdrkvendortownAdmin)

class WsrcdrkvendorwspAdmin(admin.ModelAdmin):
	list_display = [f.name for f in Wsrcdrkvendorwsp._meta.fields]

admin.site.register(Wsrcdrkvendorwsp, WsrcdrkvendorwspAdmin)

class WsrcdrkwellscountyAdmin(admin.ModelAdmin):
	list_display = [f.name for f in Wsrcdrkwellscounty._meta.fields]

admin.site.register(Wsrcdrkwellscounty, WsrcdrkwellscountyAdmin)

class WsrcdrkwellsslumAdmin(admin.ModelAdmin):
	list_display = [f.name for f in Wsrcdrkwellsslum._meta.fields]

admin.site.register(Wsrcdrkwellsslum, WsrcdrkwellsslumAdmin)

class WsrcdrkwellstownAdmin(admin.ModelAdmin):
	list_display = [f.name for f in Wsrcdrkwellstown._meta.fields]

admin.site.register(Wsrcdrkwellstown, WsrcdrkwellstownAdmin)

class WsrcdrkwellswspAdmin(admin.ModelAdmin):
	list_display = [f.name for f in Wsrcdrkwellswsp._meta.fields]

admin.site.register(Wsrcdrkwellswsp, WsrcdrkwellswspAdmin)

class Wsupsituation8Admin(admin.ModelAdmin):
	list_display = [f.name for f in Wsupsituation8._meta.fields]

admin.site.register(Wsupsituation8, Wsupsituation8Admin)

class Wsupsituation28Admin(admin.ModelAdmin):
	list_display = [f.name for f in Wsupsituation28._meta.fields]

admin.site.register(Wsupsituation28, Wsupsituation28Admin)

class Wsupsituation38DAdmin(admin.ModelAdmin):
	list_display = [f.name for f in Wsupsituation38D._meta.fields]

admin.site.register(Wsupsituation38D, Wsupsituation38DAdmin)

class WsupsituationduAdmin(admin.ModelAdmin):
	list_display = [f.name for f in Wsupsituationdu._meta.fields]

admin.site.register(Wsupsituationdu, WsupsituationduAdmin)

class Wsupplyinf8EAdmin(admin.ModelAdmin):
	list_display = [f.name for f in Wsupplyinf8E._meta.fields]

admin.site.register(Wsupplyinf8E, Wsupplyinf8EAdmin)

class WunreliablesrcbathAdmin(admin.ModelAdmin):
	list_display = [f.name for f in Wunreliablesrcbath._meta.fields]

admin.site.register(Wunreliablesrcbath, WunreliablesrcbathAdmin)

class WunreliablesrcdrkAdmin(admin.ModelAdmin):
	list_display = [f.name for f in Wunreliablesrcdrk._meta.fields]

admin.site.register(Wunreliablesrcdrk, WunreliablesrcdrkAdmin)

class WunreliablesrcdrkavgpayAdmin(admin.ModelAdmin):
	list_display = [f.name for f in Wunreliablesrcdrkavgpay._meta.fields]

admin.site.register(Wunreliablesrcdrkavgpay, WunreliablesrcdrkavgpayAdmin)

class WunreliablesrcdrktrtAdmin(admin.ModelAdmin):
	list_display = [f.name for f in Wunreliablesrcdrktrt._meta.fields]

admin.site.register(Wunreliablesrcdrktrt, WunreliablesrcdrktrtAdmin)

class Wusersperindcon10DAdmin(admin.ModelAdmin):
	list_display = [f.name for f in Wusersperindcon10D._meta.fields]

admin.site.register(Wusersperindcon10D, Wusersperindcon10DAdmin)

class WusersperkskAdmin(admin.ModelAdmin):
	list_display = [f.name for f in Wusersperksk._meta.fields]

admin.site.register(Wusersperksk, WusersperkskAdmin)

class Wusersperpubtap10DAdmin(admin.ModelAdmin):
	list_display = [f.name for f in Wusersperpubtap10D._meta.fields]

admin.site.register(Wusersperpubtap10D, Wusersperpubtap10DAdmin)

class WateroutletsAdmin(admin.ModelAdmin):
	list_display = [f.name for f in Wateroutlets._meta.fields]

admin.site.register(Wateroutlets, WateroutletsAdmin)

class WaterpaidduAdmin(admin.ModelAdmin):
	list_display = [f.name for f in Waterpaiddu._meta.fields]

admin.site.register(Waterpaiddu, WaterpaidduAdmin)

class WaterpaymthdduAdmin(admin.ModelAdmin):
	list_display = [f.name for f in Waterpaymthddu._meta.fields]

admin.site.register(Waterpaymthddu, WaterpaymthdduAdmin)

class Waterqlty9Admin(admin.ModelAdmin):
	list_display = [f.name for f in Waterqlty9._meta.fields]

admin.site.register(Waterqlty9, Waterqlty9Admin)

class Watersrcbath9Admin(admin.ModelAdmin):
	list_display = [f.name for f in Watersrcbath9._meta.fields]

admin.site.register(Watersrcbath9, Watersrcbath9Admin)

class Watersrcckg9Admin(admin.ModelAdmin):
	list_display = [f.name for f in Watersrcckg9._meta.fields]

admin.site.register(Watersrcckg9, Watersrcckg9Admin)

class Watersrcdrk9Admin(admin.ModelAdmin):
	list_display = [f.name for f in Watersrcdrk9._meta.fields]

admin.site.register(Watersrcdrk9, Watersrcdrk9Admin)

class Watersrclndry9Admin(admin.ModelAdmin):
	list_display = [f.name for f in Watersrclndry9._meta.fields]

admin.site.register(Watersrclndry9, Watersrclndry9Admin)

class WaterstorageduAdmin(admin.ModelAdmin):
	list_display = [f.name for f in Waterstoragedu._meta.fields]

admin.site.register(Waterstoragedu, WaterstorageduAdmin)

class Watertrt33CountyAdmin(admin.ModelAdmin):
	list_display = [f.name for f in Watertrt33County._meta.fields]

admin.site.register(Watertrt33County, Watertrt33CountyAdmin)

class Watertrt33SlumAdmin(admin.ModelAdmin):
	list_display = [f.name for f in Watertrt33Slum._meta.fields]

admin.site.register(Watertrt33Slum, Watertrt33SlumAdmin)

class Watertrt33TownAdmin(admin.ModelAdmin):
	list_display = [f.name for f in Watertrt33Town._meta.fields]

admin.site.register(Watertrt33Town, Watertrt33TownAdmin)

class Watertrt33WspAdmin(admin.ModelAdmin):
	list_display = [f.name for f in Watertrt33Wsp._meta.fields]

admin.site.register(Watertrt33Wsp, Watertrt33WspAdmin)

class Watertrtdu9Admin(admin.ModelAdmin):
	list_display = [f.name for f in Watertrtdu9._meta.fields]

admin.site.register(Watertrtdu9, Watertrtdu9Admin)

class WatertrtmthdduAdmin(admin.ModelAdmin):
	list_display = [f.name for f in Watertrtmthddu._meta.fields]

admin.site.register(Watertrtmthddu, WatertrtmthdduAdmin)

class WatertrtstorageAdmin(admin.ModelAdmin):
	list_display = [f.name for f in Watertrtstorage._meta.fields]

admin.site.register(Watertrtstorage, WatertrtstorageAdmin)

class WresidentsperwspkskAdmin(admin.ModelAdmin):
	list_display = [f.name for f in Wresidentsperwspksk._meta.fields]

admin.site.register(Wresidentsperwspksk, WresidentsperwspkskAdmin)
