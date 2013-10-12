from django.db import connection
from django.db.models import get_model
import simplejson as json
from django.shortcuts import render_to_response
from models import ColumnLabel
from majitables.models import *
from django.conf import settings
from django.http import HttpResponse, Http404
import json

def index(request):
	return render_to_response('home.html')
	
def getcolumns(request):
	json_label = []	
	labels = ColumnLabel.objects.all()
	for label in labels:
		json_label.append({"newname" : label.column_label.encode("utf-8"), "oldname":label.column_name.encode("utf-8")})
	jdata = json.dumps(json_label)
	return HttpResponse(jdata, mimetype='application/json')	

def data_index(request):
	return render_to_response('data.html', {'html_':"<b>Please Select A Table</b>"})

def get_tables(request, geographic_level, category, table):		
	labels = ColumnLabel.objects.all()
	tbl = table.title().replace('-', '')
	tb_class = get_model('majitables','%s'%tbl)
	html = '<table id="table-data" cellpadding="0" cellspacing="0" border="0" style="width:100%;">'
	html +='<thead> <tr>'
	for f in tb_class._meta.fields:
		for la in labels:
			if str(f.name).strip().lower() == str(la.column_name).strip().lower():
				html +='<th>' + str(la.column_label).strip() + '</th>'
			else:
				continue
			break
		else:
			html +='<th>' + str(f.name).strip() + '</th>'
	
	html+='</tr> </thead> <tbody>'
	
	cursor = connection.cursor()
	sql = 'SELECT * FROM "%s"' % table
	cursor.execute(sql)    
	data = cursor.fetchall()
	for d in data:
		html +='<tr>'
		for i in range(0,len(d)):			
			html+='<td> %s </td>' % d[i]
		html+='</tr>'
	"""
	p = ""
	data = list(tb_class.objects.all())
	for d in data:
		for f in tb_class._meta.fields:
			p += str(d[f.name])
	"""
	html+='</tbody> </table>'
	return HttpResponse(html)

def get_table_names(request, geographic_level, category):
	if geographic_level and category :
		if geographic_level == 'county':
			if category == 'general_information':				
				html='<option value="MajidataInfoCounty">General Information on County</option>'			
		
				return HttpResponse(html)
		
			elif category == 'popuplation_and_housing':
				html='<option value="APopDenAvgMinMaxCounty">County with a "high", medium, and low population density</option>'
				html+='<option value="APopDenNAreasCounty">Number of areas with a high population density (more than 5,000 persons per km2) per County</option>'
				html+='<option value="MajidataUrbanPcntPop">Percentage of urban population living in a LIA</option>'
				html+='<option value="PAvgHHDUSzCounty">Average household size per County</option>'
				html+='<option value="PopAreaBySettlementCounty">Population of various types of low income settlements per County</option>'
				html+='<option value="PopAreasByLegalCounty">Legal status of urban low income areas per County</option>'
				html+='<option value="PReligionCounty">Religion of dwelling occupants per County</option>'
				html+='<option value="PopAreaTypeCounty">Number of towns covered by MajiData per County</option>'
				html+='<option value="POwnDUWSrcKskCounty">County dwelling occupants owning the dwelling they live in (using water kiosks)</option>'
				html+='<option value="POwnDUWSrcPipedCounty">County dwelling occupants owning the dwelling they live in (using piped water)</option>'
				html+='<option value="FemHHHsCounty">Percentage of female headed households in urban low income areas per County</option>'
				html+='<option value="AreaDUStatusCounty">Type of dwelling occupants live in (materials used) per County</option>'
				html+='<option value="AreaDUTypeCounty">Type of dwelling occupants are living in (type of housing) per County</option>'
				html+='<option value="AreaHabHseTypeCounty">Main type of housing found in County</option>'
				html+='<option value="AreaHabHsgSitCounty">Housing situation of most residents per County</option>'
				html+='<option value="AreaHabRoofCounty">Main housing materials used for roofing per County</option>'
				html+='<option value="AreaHabWallCounty">Main housing materials used for walling per County</option>'
				html+='<option value="AreaNoSpcKskCounty">Areas that lack space to construct water kiosks per County</option>'
				html+='<option value="AreaNoSpcPubSanCounty">Areas that lack space to construct public sanitation facilities per County</option>'
				html+='<option value="AreaOwnDUCounty"> dwellings that own their the structure they live in per County</option>'
				html+='<option value="AreasSettLocRdRlCounty"> areas located next to a busy road or railway line per County</option>'
				html+='<option value="AreaSubjFldCounty">Areas that are subject to flooding per County</option>'				
		
				return HttpResponse(html)
		
			elif category == 'sanitation_and_public_health':
				html='<option value="SanFacPractCounty">Main sanitation facility or practice used by the occupants of dwellings (households)</option>'
				html+='<option value="SImpJMPCounty"> County residents that use an improved sanitation facility (JMP definition)</option>'
				html+='<option value="SImpJMPSharedCounty"> households that share the improved sanitation facility (JMP definition) they use with others (other households) per County</option>'
				html+='<option value="SNoFacUsedCounty"> households that do not use a sanitation facility per County</option>'
				html+='<option value="SOwnImpJMPCounty"> County residents that use an improved sanitation facility (JMP)  </option>'
				html+='<option value="SownImpNtShCounty">County urban population residing in a low income area with access to improved sanitation (JMP)</option>'
				html+='<option value="SownImpNtShUnpCounty">County urban population residing in unplanned areas with access to improved sanitation (JMP)</option>'
				html+='<option value="SAvgDUsShFacCounty">Average number of dwellings with which a sanitation facility is shared per County</option>'
				html+='<option value="SDUOwnBath45County">Average number of dwellings with which a sanitation facility is shared per County</option>'
				html+='<option value="SDUOwnFac45County"> County residents having a sanitation facility within their house</option>'
				html+='<option value="SDUOwnRPit45County"> dwellings having their own rubbish pit per County</option>'
				html+='<option value="SFacInPlotCounty"> County dwellings having access to  a sanitation facility on their plot /in their block of flats</option>'
				html+='<option value="SFacSharedCounty"> County residents that share their sanitation facility</option>'				
		
				return HttpResponse(html)
		
			elif category == 'summary_sheet':
				html='<option value="SummaryShtCounty">Summary Sheet County</option>'
			
				return HttpResponse(html)
		
			elif category == 'water_supply':
				html='<option value="WDrkSrcByQltyCounty-37">Views of dwelling occupants regarding quality of drinking water used per County</option>'
				html+='<option value="WDrkSrcByTrtMthdCounty-38">Main sources of drinking water by domestic water treatment method (percent distribution of dwellings) per County</option>'
				html+='<option value="WpersonFetching-41">Who fetches water</option>'
				html+='<option value="WDrkWaterTrtMthd-40">WDrkSrcByTrtMthd-38</option>'
				html+='<option value="WOutletsCounty">Public, private and communal water outlets per County</option>'
				html+='<option value="WResPerComTapCounty">County residents per communal taps & public stand post</option>'
				html+='<option value="WResPerPubWSPComTapsCounty">County residents per communal taps & public stand post  per County</option>'
				html+='<option value="WResPerPubWSPTapCounty">County residents per shared communal or public taps (water supplied by WSP/Council)</option>'
				html+='<option value="WResPerWSPKskCounty">County residents per improved water kiosk (properly designed & constructed)</option>'
				html+='<option value="WCkgSrcPipedCounty">County residents having piped water as their main source of water used for cooking</option>'
				html+='<option value="WDrkSrcPipedCounty"> County residents having piped water as their main source of drinking water:</option>'
				html+='<option value="WImpSrcBathWSTFCounty"> County residents using an improved source of water as their main source of water used for bathing</option>'
				html+='<option value="WImpSrcCkgWSTFCounty"> County residents using an improved source of water as their main source of water used for cooking</option>'
				html+='<option value="WImpSrcDrkWSTFCounty"> County residents using an improved source of water as their main source of drinking water</option>'
				html+='<option value="WSrcBathPipedCounty"> County residents having piped water as their main source of water used for bathing:</option>'
				html+='<option value="WSrcDrkLeakCounty"> County residents mainly using Leaks in the distribution network and vandalised pipes to obtain their drinking water</option>'
				html+='<option value="WSrcDrkSpringCounty"> County residents mainly using springs (protected and unprotected) to obtain their drinking water</option>'
				html+='<option value="WSrcDrkVendorCounty"> County residents mainly using the services of vendors to obtain drinking water</option>'
				html+='<option value="WSrcDrkWellsCounty"> County residents mainly using wells (protected and unprotected) to obtain their drinking water</option>'
				html+='<option value="WSrcDrkVendorCounty"> County residents mainly using the services of vendors to obtain drinking water</option>'
				html+='<option value="WSrcDrkWellsCounty"> County residents mainly using wells (protected and unprotected) to obtain their drinking water</option>'
				html+='<option value="WPConCounty">Plots & blocks of flats with a water connection per County</option>'
				html+='<option value="WDUWaterPayCounty">County dwelling occupants paying for the water they use</option>'
				html+='<option value="WPConMetCounty">Percentage of connections (at dwelling/household level) that are metered per County</option>'
				html+='<option value="WAreasMnProb33County">Main water supply problem as perceived by residents per County</option>'
				html+='<option value="WAreasNWLinkCounty">Areas linked to the distribution network per County</option>'
				html+='<option value="WAreasTechstatCounty">Technical state of the water supply infrastructure is good: (according to County residents)</option>'
				html+='<option value="WaterTrt33County">Dwellings treating drinking water per County</option>'
				html+='<option value="WConStatus34County">Current status of the connection per County</option>'
				html+='<option value="WDrkQlty33County">Views of dwelling occupants regarding quality of drinking water used per County</option>'
				html+='<option value="WDrkSrc33County">Main source of drinking water  used by dwellings per County</option>'
				html+='<option value="WDUConCounty">Dwellings with a water connection per County</option>'
				html+='<option value="WDUConMetCounty">Dwellings with a metered water connection per County</option>'
				html+='<option value="WDUWaterPayCounty">Dwellings that are paying for the water they use per County</option>'
				html+='<option value="WPConCounty">Plots & blocks of flats with a water connection per County</option>'
				html+='<option value="WPConMetCounty">Plots & blocks of flats with a metered water connection per County</option>'
				html+='<option value="WImpSrcJmpByQltyCounty">Drinking water from improved water sources (JMP) by assessment of the quality per County</option>'
				html+='<option value="WImpSrcJmpByTrtCounty">Drinking water from improved water sources (JMP) by domestic water treatment per County</option>'
				html+='<option value="WImpSrcWSTFByQltyCounty">Drinking water from improved water sources (WSTF)by assessment of the quality per County</option>'
				html+='<option value="WImpSrcWSTFByTrtCounty">Drinking water from improved water sources (WSTF) by domestic water treatment per County</option>'
				
				return HttpResponse(html)
	
		elif geographic_level == 'area':
			if category == 'general_information':
				html='<option value="AreaList">Area List</option>'
				html+='<option value="AreaList2">AreaList2</option>'
				html+='<option value="AreaPhyChar">AreaPhyChar</option>'
				html+='<option value="DemogTrends">Demographic Trends</option>'
				html+='<option value="DevPlans">Development Plans</option>'
				html+='<option value="LandOwnUse">Land Ownership and Use</option>'
			
				return HttpResponse(html)
				
			elif category == 'popuplation_and_housing':
				html='<option value="AreaDUTypehse">Type of dwelling occupants live in (type of housing) </option>'
				html+='<option value="AreaDUTypeStructure">Type of dwelling occupants are living in (type of structure)</option>'
				html+='<option value="AreaPop">Demographic data </option>'
				html+='<option value="AreaPopDensity">Area Population Density</option>'
				html+='<option value="DemogTrends">Demographic data </option>'
				html+='<option value="HabitationPatterns">Habitation Patterns</option>'
				
				return HttpResponse(html)
				
			elif category == 'sanitation_and_public_health':
				html='<option value="PHlthWasteRds">Type of  Roads</option>'
				html+='<option value="SEIncomeSrcs">Maine Sources of Income</option>'
				html+='<option value="SocioEconInfr">Socio Economic Infrastructure </option>'
				html+='<option value="SWDUHasOwnRpit">Dwelling Has Own Rubbish Pit</option>'
				html+='<option value="SWNoofRubPits">Number of rubbish pits/litter bins/constructed dumpsites (etc.) found on the plot / or belonging to the plot</option>'
				html+='<option value="SWRPitShared">Are the rubbish pits/litter bins/constructed dumpsites (etc.) you use shared with others (e.g. other households)? </option>'
				html+='<option value="Sanitation-12b">Sanitation</option>'
				html+='<option value="SanitationPractice">Main sanitation facility or practice used by the occupants of dwellings (households)</option>'
				html+='<option value="SanitationSewLnk">Area linked to the sewer network</option>'
				html+='<option value="SAvgHHShOwnTlt">Average Household Has Own Toiltet</option>'
				html+='<option value="SDUHasOwnBath">Does the dwelling have its own bathroom</option>'
				html+='<option value="SDUHasOwnFacility">Number and percentage of households that have an improved sanitation facility (JMP definition) </option>'
				html+='<option value="SDuSharesToilet">Do dwelling occupants (households) share the toilet facility they use with others (e.g. other households</option>'
				html+='<option value="SFacTypes">Main type(s) of sanitation facilities found in the area</option>'
				html+='<option value="SImpJMP">Number and percentage of area residents that use an improved sanitation facility (JMP definition) </option>'
				html+='<option value="SImpJMPOwnFac">Number and percentage of households that have an improved sanitation facility (JMP definition)</option>'
				html+='<option value="SImpJMPOwnPlotFac">Number and percentage of households that have an improved sanitation facility (JMP definition)</option>'
				html+='<option value="SImpJMPShFac">Number and percentage of households that share the improved sanitation facility (JMP definition)</option>'
				html+='<option value="SNoFacUsed">Number and percentage of households that do not use a sanitation facility</option>'
				html+='<option value="SNoofBaths">Number of bathrooms found on the plot / in or next to the block (of flats)</option>'
				html+='<option value="SNoofDUShrngTlt">With how many other dwellings do dwelling occupants share the sanitation facility they use? </option>'
				html+='<option value="SNoofFacilities">Number of sanitation facilities (toilets) found on the plot / in or next to the block (of flats)</option>'
				html+='<option value="SPractice">Main sanitation facility or practice used by the occupants of dwellings (households): </option>'
				html+='<option value="SSepBaths">Are there separate bathrooms for men and women? </option>'
				html+='<option value="SSepToilets">Are there separate toilets for men and women</option>'			
			
				return HttpResponse(html)
		
			elif category == 'summary_sheet':
				html='<option value="AreaSummarySheet">Area Summary Sheet</option>'
			
				return HttpResponse(html)
		
			elif category == 'water_supply':
				html='<option value="WaterPaidDU">Are dwelling occupants paying for the water they use</option>'
				html+='<option value="WaterPayMthdDU">How dwelling occupants pay for their water </option>'
				html+='<option value="WaterQlty-9">Opinion of the occupants of dwellings with regard to the quality of the water used for drinking</option>'
				html+='<option value="WaterSrcBath-9">Main source or outlet of water, which is used for bathing, used by the occupants of dwellings (all seasons)</option>'
				html+='<option value="WaterSrcCkg-9">Main source or outlet of water, which is used for cooking, used by the occupants of dwellings (all seasons)</option>'
				html+='<option value="WaterSrcDrk-9">Main source or outlet of water, which is used for drinking, used by the occupants of dwellings (all seasons)</option>'
				html+='<option value="WaterSrcLndry-9">Main source or outlet of water, which is used for laundry, used by the occupants of dwellings (all seasons)</option>'
				html+='<option value="WaterStorageDU">How water is stored in dwellings</option>'
				html+='<option value="WaterTrtDU-9">Are occupants of dwellings treating the water they use for drinking</option>'
				html+='<option value="WaterTrtMthdDU">Which treatment methods are used by occupants of dwellings </option>'
				html+='<option value="WConStatus-DU">Current status of the connection </option>'
				html+='<option value="WConsumption">Last month`s water consumption </option>'
				html+='<option value="WDUOwnCon">Does the dwelling occupied by the household have its own water connection</option>'
				html+='<option value="WDUOwnConMet">Is the water connection metered</option>'
				html+='<option value="WFetchDurationDU">The time it takes households to fetch water and return to their dwelling: </option>'
				html+='<option value="WPayDrkDU">How much are dwelling occupants paying for their drinking water</option>'
				html+='<option value="WPayNonDrkDU">How much are dwelling occupants paying for non-drinking water </option>'
				html+='<option value="WPlotConnected-DU">Does the plot/block (of flats) occupied by the household have a water connection</option>'
				html+='<option value="WSupSituationDU">How dwelling occupants describe their water supply situation</option>'
				html+='<option value="WaterTrtStorage">The most common domestic water treatment methods used by households</option>'
				html+='<option value="WSupplyInf-8e">Data on the current water supply situation </option>'
				html+='<option value="WSupSituation2-8">The protected/unprotected water sources/outlets used by area residents:</option>'
				html+='<option value="WSupSituation3-8d">Data on the current water supply situation </option>'
				html+='<option value="WSupSituation-8">Data on the current water supply situation </option>'
				html+='<option value="WAdeqSupAllKsk">Number of people that can be supplied through existing water kiosks</option>'
				html+='<option value="WAdeqSupImpWSTFSrcs">Number and percentage of area residents that obtain their drinking water from improved water sources (WSTF definition 2)</option>'
				html+='<option value="WAdeqSupPrivCons-10d">Number of people that can be adequately supplied through private connections (yard taps and domestic connections</option>'
				html+='<option value="WAdeqSupPubTap-10d">Number of users per communal tap & public stand post</option>'
				html+='<option value="WAdeqSupWSPKsk">Number of people that can be adequately supplied through improved water kiosks</option>'
				html+='<option value="WaterOutlets">Main source/outlet of water in the area</option>'
				html+='<option value="WDrkSrcCmTaps-10d">Number and percentage of area residents that obtain their drinking water from communal taps & public stand post</option>'
				html+='<option value="WDUOwnCon2-10d">Number and percentage of dwellings or households with their own water connection</option>'
				html+='<option value="WDUOwnConMet2-10d">Number and percentage of dwellings or households with their own water connection</option>'
				html+='<option value="WImpDrkSrcJMP">Number and percentage of area residents that obtain their drinking water from improved drinking water sources (JMP definition1)</option>'
				html+='<option value="WImpDrkSrcJMP30mn">Number and percentage of area residents that obtain their drinking water from improved drinking water sources (WSTF definition2) and who spend 30 minutes or less on fetching water (one round trip)</option>'
				html+='<option value="WImpDrkSrcJMPByQlty">"Number and percentage of area residents that obtain their drinking water from improved drinking water sources (WSTF definition 2) by assessment of the quality of the water used for drinking:"</option>'
				html+='<option value="WImpDrkSrcJMPByTrt">"Number and percentage of area residents that obtain their drinking water from improved drinking water sources (JMP definition1 ) by domestic water treatment:"</option>'
				html+='<option value="WImpDrkSrcWSTF">Number and percentage of area residents that obtain their drinking water from improved drinking water sources (WSTF definition </option>'
				html+='<option value="WImpDrkSrcWSTF30mn">Number and percentage of area residents that obtain their drinking water from improved drinking water sources (WSTF definition2) and who spend 30 minutes or less on fetching water (one round trip</option>'
				html+='<option value="WImpDrkSrcWSTFByQlty">"Number and percentage of area residents that obtain their drinking water from improved drinking water sources (WSTF definition 2)by assessment of the quality of the water used for drinking:"</option>'
				html+='<option value="WImpDrkSrcWSTFByTrt">"Number and percentage of area residents that obtain their drinking water from improved drinking water sources (WSTF definition) by domestic water treatment"</option>'
				html+='<option value="WNoComPubPsts-10d">Number of communal taps & public stand posts in the  area</option>'
				html+='<option value="WPDUConDisconnected">Percentage of connections (at dwelling/household level) that are disconnected</option>'
				html+='<option value="WPipedSrcBath">"WpipedwaterSrcDrkg) -Number and percentage of area residents that obtain their bathing water from  piped water outlet"</option>'
				html+='<option value="WPipedSrcDrk">Number and percentage of area residents that obtain their drinking water from piped water outlets (the piped water source being the main source</option>'
				html+='<option value="WPipedSrcDrkAvgPay">How much do area residents who obtain their drinking water from piped water outlets sources/outlets pay</option>'
				html+='<option value="WPipedSrcDrkTrt">Number and percentage of dwellings/households that obtain their drinking water from highly unreliable sources/outlets that treat their drinking water: </option>'
				html+='<option value="WresidentsperWSPKsk">Number of area residents per water kiosk</option>'
				html+='<option value="WResperComPubPost-10d">Number of LIA residents per improved water kiosk (properly designed & constructed)</option>'
				html+='<option value="WSrcDrkKsk">Number and percentage of area residents that obtain their drinking water from water kiosks in the area</option>'
				html+='<option value="WUnreliableSrcBath">Number and percentage of area residents that obtain their bathing water from highly unreliable sources/outlets</option>'
				html+='<option value="WUnreliableSrcDrk">Number and percentage of area residents that obtain their drinking water from highly unreliable sources/outlets (the unreliable source being the main source)</option>'
				html+='<option value="WUnreliableSrcDrkAvgPay">How much do area residents who obtain their drinking water from piped water outlets sources/outlets pay</option>'
				html+='<option value="WUnreliableSrcDrkTrt">Number and percentage of dwellings/households that obtain their drinking water from highly unreliable sources/outlets that treat their drinking water</option>'
				html+='<option value="WUsersPerIndCon-10d">Number of users (dwelling residents only, neighbourhood sales not included) per connection (at dwelling/household level)</option>'
				html+='<option value="WUsersPerKsk">Number of users per water kiosk</option>'
				html+='<option value="WUsersPerPubTap-10d">Number of users per communal tap & public stand post </option>'
				html+='<option value="WAdeqSupWSPKsk">Number of users per water kiosk</option>'
				html+='<option value="WaterOutlets">Number of public, private and communal water outlets</option>'
				html+='<option value="WDrkSrcCmTaps-10d">Number and percentage of area residents that obtain their drinking water from communal taps & public stand post</option>'
				html+='<option value="WDUOwnCon2-10d">Does the dwelling occupied by the household have its own water connection</option>'
				html+='<option value="WDUOwnConMet2-10d">Is the water connection metered</option>'
				html+='<option value="WImpDrkSrcJMP">Number and percentage of area residents that obtain their drinking water from improved drinking water sources (JMP definition</option>'
				html+='<option value="WImpDrkSrcJMP30mn">Number and percentage of area residents that obtain their drinking water from improved drinking water sources (JMP definition 1) and who spend 30 minutes or less on fetching water (one round trip) (JMP definition</option>'
				html+='<option value="WImpDrkSrcJMPByQlty">"Number and percentage of area residents that obtain their drinking water from improved drinking water sources (JMP definition1) by assessment of the quality of the water used for drinking"</option>'
				html+='<option value="WImpDrkSrcJMPByTrt">"Number and percentage of area residents that obtain their drinking water from improved drinking water sources (JMP definition1 ) by domestic water treatment"</option>'
				html+='<option value="WImpDrkSrcWSTF">Number and percentage of area residents that obtain their drinking water from improved drinking water sources (WSTF definition </option>'
				html+='<option value="WImpDrkSrcWSTF30mn">Number and percentage of area residents that obtain their drinking water from improved drinking water sources (WSTF definition2) and who spend 30 minutes or less on fetching water (one round trip</option>'
				html+='<option value="WImpDrkSrcWSTFByQlty">"Number and percentage of area residents that obtain their drinking water from improved drinking water sources (WSTF definition 2) by assessment of the quality of the water used for drinking "</option>'
				html+='<option value="WImpDrkSrcWSTFByTrt">"Number and percentage of area residents that obtain their drinking water from improved drinking water sources (WSTF definition 2) by domestic water treatment"</option>'
				html+='<option value="WNoComPubPsts-10d">Number of communal taps & public stand posts in the  area</option>'
				html+='<option value="WPDUConDisconnected">Percentage of connections (at dwelling/household level) that are disconnected</option>'
				html+='<option value="WPipedSrcBath">Number and percentage of area residents that obtain their bathing water from  piped water outlets</option>'
				html+='<option value="WPipedSrcDrk">Number and percentage of area residents that obtain their drinking water from piped water outlets (the piped water source being the main source</option>'
				html+='<option value="WPipedSrcDrkAvgPay">How much do area residents who obtain their drinking water from piped water outlets sources/outlets pay</option>'
				html+='<option value="WPipedSrcDrkTrt">Number and percentage of dwellings/households that obtain their drinking water from  piped water outlets that treat their drinking water</option>'
				html+='<option value="WresidentsperWSPKsk">Number of LIA residents per improved water kiosk (properly designed & constructed</option>'
				html+='<option value="WResperComPubPost-10d">Number of area residents per communal taps & public stand post </option>'
				html+='<option value="WSrcDrkKsk">Number and percentage of area residents that obtain their drinking water from water kiosks in the area</option>'
				html+='<option value="WUnreliableSrcBath">Number and percentage of area residents that obtain their bathing water from highly unreliable sources/outlets</option>'
				html+='<option value="WUnreliableSrcDrk">Number and percentage of area residents that obtain their drinking water from highly unreliable sources/outlets (the unreliable source being the main source)</option>'
				html+='<option value="WUnreliableSrcDrkAvgPay">How much do area residents who obtain their drinking water from highly unreliable sources/outlets </option>'
				html+='<option value="WUnreliableSrcDrkTrt">Number and percentage of dwellings/households that obtain their drinking water from highly unreliable sources/outlets that treat their drinking water</option>'
				html+='<option value="WUsersPerIndCon-10d">/ Number of users (dwelling residents only, neighbourhood sales not included) per connection (at dwelling/household level)</option>'
				html+='<option value="WUsersPerKsk">Number of users per communal tap & public stand post</option>'
				html+='<option value="WUsersPerPubTap-10d">Number of users per communal tap & public stand post</option>'
				html+='<option value="WDrkSrcLeak">Number and percentage of area residents that obtain their drinking water from a leak in the distribution network or a vandalised pipe</option>'
				html+='<option value="WDrkSrcOthCon">Number and percentage of area residents that obtain their drinking water from someone else`s connection, outside the plot</option>'
				html+='<option value="WDrkSrcReseller">Number and percentage of area residents that obtain their drinking water from water resellers</option>'
				html+='<option value="WDrkSrcYWell">Number and percentage of area residents that obtain their drinking water from a protected yard well</option>'				
			
				return HttpResponse(html)
	
		elif geographic_level == 'slum':
			if category == 'general_information':
				html='<option value="MajidataInfoSlum">General Information on Slum</option>'
		
				return HttpResponse(html)
		
			elif category == 'popuplation_and_housing':
				html='<option value="APopDenAvgMinMaxSlum">Slum with a "high", medium, and low population density</option>'
				html+='<option value="APopDenNAreasSlum">Number of areas with a high population density (more than 5,000 persons per km2) per Slum</option>'
				html+='<option value="MajidataUrbanPcntPop">Percentage of urban population living in a LIA</option>'
				html+='<option value="PAvgHHDUSzSlum">Average household size per Slum</option>'
				html+='<option value="PopAreaBySettlementSlum">Population of various types of low income settlements per Slum</option>'
				html+='<option value="PopAreasByLegalSlum">Legal status of urban low income areas per Slum</option>'
				html+='<option value="PReligionSlum">Religions of dwelling occupants per Slum</option>'
				html+='<option value="POwnDUWSrcKskSlum">Slum dwelling occupants owning the dwelling they live in (using water kiosks)</option>'
				html+='<option value="POwnDUWSrcSlum">Slum dwelling occupants owning the dwelling they live in (using piped water)</option>'
				html+='<option value="FemHHHsSlum">Percentage of female headed households in urban low income areas per Slum</option>'
				html+='<option value="AreaDUStatusSlum">Type of dwelling occupants live in (materials used) per Slum</option>'
				html+='<option value="AreaDUTypeSlum">Type of dwelling occupants are living in (type of housing) per Slum</option>'
				html+='<option value="AreaHabHseTypeSlum">Main type of housing found in Slum</option>'
				html+='<option value="AreaHabHsgSitSlum">Housing situation of most residents per Slum</option>'
				html+='<option value="AreaHabRoofSlum">Main housing materials used for roofing per Slum</option>'
				html+='<option value="AreaHabWallSlum">Main housing materials used for walling per Slum</option>'
				html+='<option value="AreaNoSpcKskSlum">Areas that lack space to construct water kiosks per Slum</option>'
				html+='<option value="AreaNoSpcPubSanSlum">Areas that lack space to construct public sanitation facilities per Slum</option>'
				html+='<option value="AreaOwnDUSlum"> dwellings that own their the structure they live in per Slum</option>'
				html+='<option value="AreasSettLocRdRlSlum"> areas located next to a busy road or railway line per Slum</option>'
				html+='<option value="AreaSubjFldSlum">Areas that are subject to flooding per Slum</option>'				
			
				return HttpResponse(html)
		
			elif category == 'sanitation_and_public_health':
				html='<option value="SanFacPractSlum">Main sanitation facility or practice used by the occupants of dwellings (households)</option>'
				html+='<option value="SAvgDUSh44Slum">Average number of dwellings a shared sanitation facility is shared per Slum</option>'
				html+='<option value="SImpJMPSharedSlum"> households that share the improved sanitation facility (JMP definition) they use with others (other households) per Slum</option>'
				html+='<option value="SImpJMPSlum"> households that do not use a sanitation facility per Slum</option>'
				html+='<option value="SNoFacUsedSlum"> households that do not use a sanitation facility per Slum</option>'
				html+='<option value="SownImpNtShSlum">Slum urban population residing in a low income area with access to improved sanitation (JMP)</option>'
				html+='<option value="SownImpNtShUnpSlum">Slum urban population residing in unplanned areas with access to improved sanitation (JMP definition)</option>'
				html+='<option value="SAvgDUsShFacSlum">Average number of dwellings with which a sanitation facility is shared per Slum</option>'
				html+='<option value="SDUOwnBath45Slum">Average number of dwellings with which a sanitation facility is shared per Slum</option>'
				html+='<option value="SDUOwnFac45Slum"> Slum residents having a sanitation facility within their house</option>'
				html+='<option value="SDUOwnRPit45Slum"> dwellings having their own rubbish pit per Slum</option>'
				html+='<option value="SFacInPlotSlum"> Slum dwellings having access to  a sanitation facility on their plot /in their block of flats</option>'
				html+='<option value="SFacSharedSlum"> Slum residents that share their sanitation facility</option>'				
			
				return HttpResponse(html)
		
			elif category == 'summary_sheet':
				html='<option value="SummaryShtSlum">Summary Sheet Slum</option>'
		
				return HttpResponse(html)
		
			elif category == 'water_supply':
				html='<option value="WDrkSrcByQltySlum-37">Views of dwelling occupants regarding quality of drinking water used per Slum</option>'
				html+='<option value="WDrkSrcByTrtMthdSlum-38">Main sources of drinking water by domestic water treatment method (percent distribution of dwellings)</option>'
				html+='<option value="WpersonFetching-41">Who fetches water</option>'
				html+='<option value="WDrkWaterTrtMthd-40">Percent distribution of urban households & urban population by treatment of drinking water</option>'
				html+='<option value="WOutletsSlum">Public, private and communal water outlets per Slum</option>'
				html+='<option value="WResPerComTapSlum">Slum residents per communal taps & public stand post</option>'
				html+='<option value="WResPerPubComKsksSlum">Slum residents per improved water kiosk (properly designed & constructed)</option>'
				html+='<option value="WResPerPubWSPComTapsSlum">Slum residents per communal taps & public stand post</option>'
				html+='<option value="WResPerPubWSPTapSlum">Slum residents per shared communal or public taps (water supplied by WSP/Council)</option>'
				html+='<option value="WResPerWSPKskSlum">Slum residents per improved water kiosk (properly designed & constructed)</option>'
				html+='<option value="WCkgSrcPipedSlum"> Slum residents having piped water as their main source of water used for cooking</option>'
				html+='<option value="WDrkSrcPipedSlum"> Slum residents having piped water as their main source of drinking water</option>'
				html+='<option value="WImpSrcBathWSTFSlum"> Slum residents using an improved source of water as their main source of water used for bathing</option>'
				html+='<option value="WImpSrcCkgWSTFSlum"> Slum residents using an improved source of water as their main source of water used for cooking</option>'
				html+='<option value="WImpSrcDrkWSTFSlum"> Slum residents using an improved source of water as their main source of drinking water</option>'
				html+='<option value="WSrcBathPipedSlum"> Slum residents having piped water as their main source of water used for bathing</option>'
				html+='<option value="WSrcDrkBhPmpSlum"> Slum residents mainly using boreholes, and hand pumps to obtain their drinking water</option>'
				html+='<option value="WSrcDrkLeakSlum"> Slum residents mainly using Leaks in the distribution network and vandalised pipes to obtain their drinking water</option>'
				html+='<option value="WSrcDrkSpringSlum"> Slum residents mainly using springs (protected and unprotected) to obtain their drinking water</option>'
				html+='<option value="WSrcDrkVendorSlum"> Slum residents mainly using the services of vendors to obtain drinking water</option>'
				html+='<option value="WSrcDrkWellsSlum"> Slum residents mainly using wells (protected and unprotected) to obtain their drinking water</option>'
				html+='<option value="WSrcDrkSpringSlum"> Slum residents mainly using springs (protected and unprotected) to obtain their drinking water</option>'
				html+='<option value="WSrcDrkVendorSlum"> Slum residents mainly using the services of vendors to obtain drinking water</option>'
				html+='<option value="WSrcDrkWellsSlum"> Slum residents mainly using wells (protected and unprotected) to obtain their drinking water</option>'
				html+='<option value="WDUConSlum">Current status of the connection per Slum</option>'
				html+='<option value="WDUWaterPaySlum">Slum dwelling occupants paying for the water they use</option>'
				html+='<option value="WPConMetSlum">Percentage of connections (at dwelling/household level) that are metered per Slum</option>'
				html+='<option value="WAreasMnProb33Slum">Main water supply problem as perceived by residents per Slum</option>'
				html+='<option value="WAreasNWLinkSlum">Areas linked to the distribution network per Slum</option>'
				html+='<option value="WAreasTechstatSlum">Technical state of the water supply infrastructure is good: (according to Slum residents)</option>'
				html+='<option value="WaterTrt33Slum">Dwellings treating drinking water per Slum</option>'
				html+='<option value="WDrkQlty33Slum">Views of dwelling occupants regarding quality of drinking water used per Slum</option>'
				html+='<option value="WDrkSrc33Slum">Main source of drinking water  used by dwellings per Slum</option>'
				html+='<option value="WDUConSlum">Dwellings with a water connection per Slum</option>'
				html+='<option value="WDUConMetSlum">Dwellings with a metered water connection per Slum</option>'
				html+='<option value="WDUWaterPaySlum">Dwellings that are paying for the water they use per Slum</option>'
				html+='<option value="WPConMetSlum">Plots & blocks of flats with a metered water connection per Slum</option>'
				html+='<option value="WImpSrcJmpByQltySlum">Drinking water from improved water sources (JMP) by assessment of the quality per Slum</option>'
				html+='<option value="WImpSrcJmpByTrtSlum">Drinking water from improved water sources (JMP) by domestic water treatment per Slum</option>'
				html+='<option value="WImpSrcWSTFByQltySlum">Drinking water from improved water sources (WSTF)by assessment of the quality per Slum</option>'
				html+='<option value="WImpSrcWSTFByTrtSlum">Drinking water from improved water sources (WSTF) by domestic water treatment per Slum</option>'				
			
				return HttpResponse(html)
	
		elif geographic_level == 'town':
			if category == 'general_information':
				html='<option value="MajidataInfoTwn">General Information on Town</option>'
				html+='<option value=""></option>'
			
				return HttpResponse(html)
		
			elif category == 'popuplation_and_housing':
				html='<option value="APopDenAvgMinMaxTown">Town with a "high", medium, and low population density</option>'
				html+='<option value="APopDenNAreasTowns">Number of areas with a high population density (more than 5,000 persons per km2) per Town</option>'
				#html+='<option value="MajidataUrbanPcntPop">Percentage of urban population living in a LIA</option>'
				html+='<option value="PAvgHHDUSzTown">Average household size per Town</option>'
				html+='<option value="PopAreaBySettlementTown">Population of various types of low income settlements per Town</option>'
				html+='<option value="PopAreasByLegalTown">Legal status of urban low income areas per Town</option>'
				html+='<option value="PopAreaTypeTown">Number of towns covered by MajiData per Town</option>'
				html+='<option value="PReligionTown">Religions of dwelling occupants per Town</option>'
				html+='<option value="TownsAreas-Counties">Number of towns covered by MajiData</option>'
				html+='<option value="TownsAreas-Towns">Number of towns covered by MajiData</option>'
				html+='<option value="POwnDUWSrcKskTown">Town dwelling occupants owning the dwelling they live in (using water kiosks)</option>'
				html+='<option value="POwnDUWSrcPipedTown">Town dwelling occupants owning the dwelling they live in (using piped water)</option>'
				html+='<option value="FemHHHsTown">Percentage of female headed households in urban low income areas per Town</option>'
				html+='<option value="AreaDUStatusTown">Type of dwelling occupants live in (materials used) per Town</option>'
				html+='<option value="AreaDUTypeTown">Type of dwelling occupants are living in (type of housing) per Town</option>'
				html+='<option value="AreaHabHseTypeTown">Main type of housing found in Town</option>'
				html+='<option value="AreaHabHsgSitTown">Housing situation of most residents per Town</option>'
				html+='<option value="AreaHabRoofTown">Main housing materials used for roofing per Town</option>'
				html+='<option value="AreaHabWallTown">Main housing materials used for walling per Town</option>'
				html+='<option value="AreaNoSpcKskTown">Areas that lack space to construct water kiosks per Town</option>'
				html+='<option value="AreaNoSpcPubSanTown">Areas that lack space to construct public sanitation facilities per Town</option>'
				html+='<option value="AreaOwnDUTown"> dwellings that own their the structure they live in per Town</option>'
				html+='<option value="AreasSettLocRdRlTown"> areas located next to a busy road or railway line per Town</option>'
				html+='<option value="AreaSubjFldTown">Areas that are subject to flooding per Town</option>'				
			
				return HttpResponse(html)
		
			elif category == 'sanitation_and_public_health':
				html='<option value="SanFacPractTown">Main sanitation facility or practice used by the occupants of dwellings (households)</option>'
				html+='<option value="SAvgDUSh44Town">Average number of dwellings a shared sanitation facility is shared per Town</option>'
				html+='<option value="SImpJMPSharedTown"> households that share the improved sanitation facility (JMP definition) they use with others (other households) per Town</option>'
				html+='<option value="SImpJMPTown"> households that do not use a sanitation facility per Town</option>'
				html+='<option value="SNoFacUsedTown"> households that do not use a sanitation facility per Town</option>'
				html+='<option value="SOwnImpJMPTown"> Town residents that use an improved sanitation facility (JMP)  </option>'
				html+='<option value="SownImpNtShTown">Town urban population residing in a low income area with access to improved sanitation (JMP)</option>'
				html+='<option value="SownImpNtShUnpTown">Town urban population residing in unplanned areas with access to improved sanitation (JMP)</option>'
				html+='<option value="SAvgDUsShFacTown">Average number of dwellings with which a sanitation facility is shared per Town</option>'
				html+='<option value="SDUOwnBath45Town">Average number of dwellings with which a sanitation facility is shared per Town</option>'
				html+='<option value="SDUOwnFac45Town"> Town residents having a sanitation facility within their house</option>'
				html+='<option value="SDUOwnRPit45Town"> dwellings having their own rubbish pit per Town</option>'
				html+='<option value="SFacInPlotTown"> Town dwellings having access to  a sanitation facility on their plot /in their block of flats</option>'
				html+='<option value="SFacSharedTown"> Town residents that share their sanitation facility</option>'
				html+='<option value=""></option>'
			
				return HttpResponse(html)
		
			elif category == 'summary_sheet':
				html='<option value="SummaryShtTown">Summary Sheet Town</option>'
			
				return HttpResponse(html)
		
			elif category == 'water_supply':
				html='<option value="WDrkSrcByQltyTown-37">Views of dwelling occupants regarding quality of drinking water used per Town</option>'
				html+='<option value="WDrkSrcByTrtMthd-38">Main sources of drinking water by domestic water treatment method (percent distribution of dwellings)</option>'
				html+='<option value="WpersonFetching-41">Who fetches water</option>'
				html+='<option value="WDrkWaterTrtMthd-40">Percent distribution of urban households & urban population by treatment of drinking water</option>'
				html+='<option value="WOutletsTown">Public, private and communal water outlets per Town</option>'
				html+='<option value="WResPerComTapTown">Town residents per communal taps & public stand post</option>'
				html+='<option value="WResPerPubComKsksTown">Town residents per improved water kiosk (properly designed & constructed)</option>'
				html+='<option value="WResPerPubWSPComTapsTown">Town residents per communal taps & public stand post</option>'
				html+='<option value="WResPerPubWSPTapTown">Town residents per shared communal or public taps (water supplied by WSP/Council)</option>'
				html+='<option value="WResPerWSPKskTown">Town residents per improved water kiosk (properly designed & constructed)</option>'
				html+='<option value="WCkgSrcPipedTown"> Town residents having piped water as their main source of water used for cooking</option>'
				html+='<option value="WDrkSrcPipedTown"> Town residents having piped water as their main source of drinking water</option>'
				html+='<option value="WImpSrcBathWSTFTown"> Town residents using an improved source of water as their main source of water used for bathing:</option>'
				html+='<option value="WImpSrcCkgWSTFTown"> Town residents using an improved source of water as their main source of water used for cooking</option>'
				html+='<option value="WImpSrcDrkWSTFTown"> Town residents using an improved source of water as their main source of drinking water</option>'
				html+='<option value="WSrcBathPipedTown"> Town residents having piped water as their main source of water used for bathing</option>'
				html+='<option value="WSrcDrkBhPmpTown"> Town residents mainly using boreholes, and hand pumps to obtain their drinking water</option>'
				html+='<option value="WSrcDrkLeakTown"> Town residents mainly using Leaks in the distribution network and vandalised pipes to obtain their drinking water</option>'
				html+='<option value="WSrcDrkSpringTown"> Town residents mainly using springs (protected and unprotected) to obtain their drinking water</option>'
				html+='<option value="WSrcDrkWellsTown"> Town residents mainly using wells (protected and unprotected) to obtain their drinking water</option>'
				html+='<option value="WSrcDrkSpringTown"> Town residents mainly using springs (protected and unprotected) to obtain their drinking water</option>'
				html+='<option value="WSrcDrkVendorTown"> Town residents mainly using the services of vendors to obtain drinking water</option>'
				html+='<option value="WSrcDrkWellsTown"> Town residents mainly using wells (protected and unprotected) to obtain their drinking water</option>'
				html+='<option value="WDUConTown">Current status of the connection per Town</option>'
				html+='<option value="WDUWaterPayTown">Town dwelling occupants paying for the water they use</option>'
				html+='<option value="WAreasMnProb33Town">Main water supply problem as perceived by residents per Town</option>'
				html+='<option value="WAreasNWLinkTown">Areas linked to the distribution network per Town</option>'
				html+='<option value="WAreasTechstatTown">Technical state of the water supply infrastructure is good: (according to Town residents)</option>'
				html+='<option value="WaterTrt33Town">Dwellings treating drinking water per Town</option>'
				html+='<option value="WDrkQlty33Town">Views of dwelling occupants regarding quality of drinking water used per Town</option>'
				html+='<option value="WDrkSrc33Town">Main source of drinking water  used by dwellings per Town</option>'
				html+='<option value="WDUConTown">Dwellings with a water connection per Town</option>'
				html+='<option value="WDUConMetTown">Dwellings with a metered water connection per Town</option>'
				html+='<option value="WDUWaterPayTown">Dwellings that are paying for the water they use per Town</option>'
				html+='<option value="WImpSrcJmpByQltyTown">Drinking water from improved water sources (JMP) by assessment of the quality per Town</option>'
				html+='<option value="WImpSrcJmpByTrtTown">Drinking water from improved water sources (JMP) by domestic water treatment per Town</option>'
				html+='<option value="WImpSrcWSTFByQltyTown">Drinking water from improved water sources (WSTF)by assessment of the quality per Town</option>'
				html+='<option value="WImpSrcWSTFByTrtTown">Drinking water from improved water sources (WSTF) by domestic water treatment per Town</option>'				
			
				return HttpResponse(html)
	
		elif geographic_level == 'wsp':
			if category == 'general_information':
				html='<option value="MajidataInfoWSP">General Information on WSP</option>'
			
				return HttpResponse(html)
		
			elif category == 'popuplation_and_housing':
				html='<option value="APopDenAvgMinMaxWSP">WSP with a "high", medium, and low population density</option>'
				html+='<option value="APopDenNAreasWSP">Number of areas with a high population density (more than 5,000 persons per km2) per WSP</option>'
				html+='<option value="MajidataUrbanPcntPop">Percentage of urban population living in a LIA</option>'
				html+='<option value="PAvgHHDUSzWSP">Average household size per WSP</option>'
				html+='<option value="PopAreaBySettlementWSP">Population of various types of low income settlements per WSP</option>'
				html+='<option value="PopAreasByLegalWSP">Legal status of urban low income areas per WSP</option>'
				html+='<option value="PReligionWSP">Religions of dwelling occupants per WSP</option>'
				html+='<option value="POwnDUWSrcKskWSP">WSP dwelling occupants owning the dwelling they live in (using water kiosks)</option>'
				html+='<option value="POwnDUWSrcWSP">WSP dwelling occupants owning the dwelling they live in (using piped water)</option>'
				html+='<option value="FemHHHsWSP">Percentage of female headed households in urban low income areas per WSP</option>'
				html+='<option value="AreaDUStatusWSP">Type of dwelling occupants live in (materials used) per WSP</option>'
				html+='<option value="AreaDUTypeWSP">Type of dwelling occupants are living in (type of housing) per WSP</option>'
				html+='<option value="AreaHabHseTypeWSP">Main type of housing found in WSP</option>'
				html+='<option value="AreaHabHsgSitWSP">Housing situation of most residents per WSP</option>'
				html+='<option value="AreaHabRoofWSP">Main housing materials used for roofing per WSP</option>'
				html+='<option value="AreaHabWallWSP">Main housing materials used for walling per WSP</option>'
				html+='<option value="AreaNoSpcKskWSP">Areas that lack space to construct water kiosks per WSP</option>'
				html+='<option value="AreaNoSpcPubSanWSP">Areas that lack space to construct public sanitation facilities per WSP</option>'
				html+='<option value="AreaOwnDUWSP"> dwellings that own their the structure they live in per WSP</option>'
				html+='<option value="AreasSettLocRdRlWSP"> areas located next to a busy road or railway line per WSP</option>'
				html+='<option value="AreaSubjFldWSP">Areas that are subject to flooding per WSP</option>'				
			
				return HttpResponse(html)
		
			elif category == 'sanitation_and_public_health':
				html='<option value="SanFacPractWSP">Main sanitation facility or practice used by the occupants of dwellings (households)</option>'
				html+='<option value="SAvgDUSh44WSP">Average number of dwellings a shared sanitation facility is shared per WSP</option>'
				html+='<option value="SImpJMPSharedWSP"> households that share the improved sanitation facility (JMP definition) they use with others (other households) per WSP</option>'
				html+='<option value="SImpJMPWSP"> households that do not use a sanitation facility per WSP</option>'
				html+='<option value="SNoFacUsedWSP"> households that do not use a sanitation facility per WSP</option>'
				html+='<option value="SownImpNtShWSP">WSP urban population residing in a low income area with access to improved sanitation (JMP)</option>'
				html+='<option value="SownImpNtShUnpWSP">WSP urban population residing in unplanned areas with access to improved sanitation (JMP definition)</option>'
				html+='<option value="SAvgDUsShFacWSP">Average number of dwellings with which a sanitation facility is shared per WSP</option>'
				html+='<option value="SDUOwnBath45WSP">Average number of dwellings with which a sanitation facility is shared per WSP</option>'
				html+='<option value="SDUOwnFac45WSP"> WSP residents having a sanitation facility within their house</option>'
				html+='<option value="SDUOwnRPit45WSP"> dwellings having their own rubbish pit per WSP</option>'
				html+='<option value="SFacInPlotWSP"> WSP dwellings having access to  a sanitation facility on their plot /in their block of flats</option>'
				html+='<option value="SFacSharedWSP"> WSP residents that share their sanitation facility</option>'
			
				return HttpResponse(html)
		
			elif category == 'summary_sheet':
				html='<option value="SummaryShtWSP">Summary Sheet WSP</option>'
			
				return HttpResponse(html)
		
			elif category == 'water_supply':
				html='<option value="WDrkSrcByQltyWSP-37">Views of dwelling occupants regarding quality of drinking water used per WSP</option>'
				html+='<option value="WDrkSrcByTrtMthd-38">Main sources of drinking water by domestic water treatment method (percent distribution of dwellings)</option>'
				html+='<option value="WpersonFetching-41">Who fetches water</option>'
				html+='<option value="WDrkWaterTrtMthd-40">Percent distribution of urban households & urban population by treatment of drinking water</option>'
				html+='<option value="WOutletsWSP">Public, private and communal water outlets per WSP</option>'
				html+='<option value="WResPerComTapWSP">WSP residents per communal taps & public stand post</option>'
				html+='<option value="WResPerPubComKsksWSP">WSP residents per improved water kiosk (properly designed & constructed)</option>'
				html+='<option value="WResPerPubWSPComTapsWSP">WSP residents per communal taps & public stand post</option>'
				html+='<option value="WResPerPubWSPTapWSP">WSP residents per shared communal or public taps (water supplied by WSP/Council)</option>'
				html+='<option value="WResPerWSPKskWSP">WSP residents per improved water kiosk (properly designed & constructed)</option>'
				html+='<option value="WCkgSrcPipedWSP"> WSP residents having piped water as their main source of water used for cooking</option>'
				html+='<option value="WDrkSrcPipedWSP"> WSP residents having piped water as their main source of drinking water</option>'
				html+='<option value="WImpSrcBathWSTFWSP"> WSP residents using an improved source of water as their main source of water used for bathing</option>'
				html+='<option value="WImpSrcCkgWSTFWSP"> WSP residents using an improved source of water as their main source of water used for cooking</option>'
				html+='<option value="WImpSrcDrkWSTFWSP"> WSP residents using an improved source of water as their main source of drinking water</option>'
				html+='<option value="WSrcBathPipedWSP"> WSP residents having piped water as their main source of water used for bathing</option>'
				html+='<option value="WSrcDrkBhPmpWSP"> WSP residents mainly using boreholes, and hand pumps to obtain their drinking water</option>'
				html+='<option value="WSrcDrkLeakWSP"> WSP residents mainly using Leaks in the distribution network and vandalised pipes to obtain their drinking water</option>'
				html+='<option value="WSrcDrkSpringWSP"> WSP residents mainly using springs (protected and unprotected) to obtain their drinking water</option>'
				html+='<option value="WSrcDrkVendorWSP"> WSP residents mainly using the services of vendors to obtain drinking water</option>'
				html+='<option value="WSrcDrkWellsWSP">WSrcDrkWellsWSP</option>'
				html+='<option value="WSrcDrkSpringWSP"> WSP residents mainly using springs (protected and unprotected) to obtain their drinking water</option>'
				html+='<option value="WSrcDrkVendorWSP"> WSP residents mainly using the services of vendors to obtain drinking water</option>'
			
				return HttpResponse(html)
	else:
		return HttpResponse("")
    





