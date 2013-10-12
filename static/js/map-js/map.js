var dd ='<sld:StyledLayerDescriptor xsi:schemaLocation="http://www.opengis.net/sld StyledLayerDescriptor.xsd" xmlns:sld="http://www.opengis.net/sld" xmlns:ogc="http://www.opengis.net/ogc" xmlns:xlink="http://www.w3.org/1999/xlink" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" version="1.0.0"><NamedLayer><Name>county</Name><UserStyle><Title>Default Style</Title><FeatureTypeStyle><Rule><Title>4-14</Title><ogc:Filter><ogc:PropertyIsBetween><ogc:PropertyName>Nareas</ogc:PropertyName><ogc:LowerBoundary><ogc:Literal>4</ogc:Literal></ogc:LowerBoundary><ogc:UpperBoundary><ogc:Literal>14</ogc:Literal></ogc:UpperBoundary></ogc:PropertyIsBetween></ogc:Filter><PolygonSymbolizer><Fill><CssParameter name="fill">#fef0d9</CssParameter><CssParameter name="fill-opacity">0.65</CssParameter></Fill></PolygonSymbolizer></Rule><Rule><Title>14-31</Title><ogc:Filter><ogc:PropertyIsBetween><ogc:PropertyName>Nareas</ogc:PropertyName><ogc:LowerBoundary><ogc:Literal>14</ogc:Literal></ogc:LowerBoundary><ogc:UpperBoundary><ogc:Literal>31</ogc:Literal></ogc:UpperBoundary></ogc:PropertyIsBetween></ogc:Filter><PolygonSymbolizer><Fill><CssParameter name="fill">#fdcc8a</CssParameter><CssParameter name="fill-opacity">0.65</CssParameter></Fill></PolygonSymbolizer></Rule><Rule><Title>31-63</Title><ogc:Filter><ogc:PropertyIsBetween><ogc:PropertyName>Nareas</ogc:PropertyName><ogc:LowerBoundary><ogc:Literal>31</ogc:Literal></ogc:LowerBoundary><ogc:UpperBoundary><ogc:Literal>63</ogc:Literal></ogc:UpperBoundary></ogc:PropertyIsBetween></ogc:Filter><PolygonSymbolizer><Fill><CssParameter name="fill">#fc8d59</CssParameter><CssParameter name="fill-opacity">0.65</CssParameter></Fill></PolygonSymbolizer></Rule><Rule><Title>63-116</Title><ogc:Filter><ogc:PropertyIsBetween><ogc:PropertyName>Nareas</ogc:PropertyName><ogc:LowerBoundary><ogc:Literal>63</ogc:Literal></ogc:LowerBoundary><ogc:UpperBoundary><ogc:Literal>116</ogc:Literal></ogc:UpperBoundary></ogc:PropertyIsBetween></ogc:Filter><PolygonSymbolizer><Fill><CssParameter name="fill">#e34a33</CssParameter><CssParameter name="fill-opacity">0.65</CssParameter></Fill></PolygonSymbolizer></Rule><Rule><Title>116-386</Title><ogc:Filter><ogc:PropertyIsBetween><ogc:PropertyName>Nareas</ogc:PropertyName><ogc:LowerBoundary><ogc:Literal>116</ogc:Literal></ogc:LowerBoundary><ogc:UpperBoundary><ogc:Literal>386</ogc:Literal></ogc:UpperBoundary></ogc:PropertyIsBetween></ogc:Filter><PolygonSymbolizer><Fill><CssParameter name="fill">#b30000</CssParameter><CssParameter name="fill-opacity">0.65</CssParameter></Fill></PolygonSymbolizer></Rule></FeatureTypeStyle></UserStyle></NamedLayer></sld:StyledLayerDescriptor>';
OpenLayers.Util.onImageLoadErrorColor = "transparent";
OpenLayers.ProxyHost = "/cgi-bin/proxy.cgi?url=";
Ext.BLANK_IMAGE_URL = 'http://cdnjs.cloudflare.com/ajax/libs/extjs/3.4.1-1/resources/images/default/s.gif';
Ext.namespace("Heron.examples");
Heron.examples.searchPanelConfig = {
	xtype : 'hr_multisearchcenterpanel',
	height : 600,
	hropts : [{
			searchPanel : {
				xtype : 'hr_searchbydrawpanel',
				name : __('Search by Drawing'),
				header : false
			},
			resultPanel : {
				xtype : 'hr_featuregridpanel',
				id : 'hr-featuregridpanel',
				header : false,
				autoConfig : true,
				exportFormats : ['XLS', 'WellKnownText'],
				hropts : {
					zoomOnRowDoubleClick : true,
					zoomOnFeatureSelect : false,
					zoomLevelPointSelect : 8,
					zoomToDataExtent : false
				}
			}
		}, {
			searchPanel : {
				xtype : 'hr_searchbyfeaturepanel',
				name : __('Search by Feature Selection'),
				description : 'Select feature-geometries from one layer and use these to perform a spatial search in another layer.',
				header : false,
				border : false,
				bodyStyle : 'padding: 6px',
				style : {
					fontFamily : 'Verdana, Arial, Helvetica, sans-serif',
					fontSize : '12px'
				}
			},
			resultPanel : {
				xtype : 'hr_featuregridpanel',
				id : 'hr-featuregridpanel',
				header : false,
				border : false,
				autoConfig : true,
				exportFormats : ['XLS', 'WellKnownText'],
				hropts : {
					zoomOnRowDoubleClick : true,
					zoomOnFeatureSelect : false,
					zoomLevelPointSelect : 8,
					zoomToDataExtent : false
				}
			}
		}, {
			searchPanel : {
				xtype : 'hr_gxpquerypanel',
				name : __('Build your own searches'),
				description : 'This search uses both search within Map extent and/or your own attribute criteria',
				header : false,
				border : false,
				caseInsensitiveMatch : true,
				autoWildCardAttach : true
			},
			resultPanel : {
				xtype : 'hr_featuregridpanel',
				id : 'hr-featuregridpanel',
				header : false,
				border : false,
				autoConfig : true,
				exportFormats : ['XLS', 'WellKnownText'],
				hropts : {
					zoomOnRowDoubleClick : true,
					zoomOnFeatureSelect : false,
					zoomLevelPointSelect : 8,
					zoomToDataExtent : true
				}
			}
		}
	]
};
Ext.namespace("Heron.options.map");
Heron.options.map.settings = {
	projection : "EPSG:900913",
	units : 'dd',
	maxExtent : new OpenLayers.Bounds(2563208.7, -490420.0, 5865288.3, 607827.2),
	center : new OpenLayers.LonLat(37.857239, 0.527336).transform(new OpenLayers.Projection("EPSG:4326"), new OpenLayers.Projection("EPSG:900913")),
	maxResolution : 'auto',
	xy_precision : 3,
	max_features : 10,
	zoom : 6,
	theme : null,
	permalinks : {
		paramPrefix : 'map',
		encodeType : false,
		prettyLayerNames : true
	},
};
Ext.namespace("Heron.options.wfs");
Heron.options.wfs.downloadFormats = [{
		name : 'CSV',
		outputFormat : 'csv',
		fileExt : '.csv'
	}, {
		name : 'GML (version 2.1.2)',
		outputFormat : 'text/xml; subtype=gml/2.1.2',
		fileExt : '.gml'
	}, {
		name : 'ESRI Shapefile (zipped)',
		outputFormat : 'SHAPE-ZIP',
		fileExt : '.zip'
	}, {
		name : 'GeoJSON',
		outputFormat : 'json',
		fileExt : '.json'
	}
];
Heron.options.map.layers = [new OpenLayers.Layer.Google("Google Terrain", {
		type : google.maps.MapTypeId.TERRAIN,
		'sphericalMercator' : true,
		isBaseLayer : true,
		attribution : "<a href='http://upande.com'>powered by Upande</a>",
		transitionEffect : 'resize'
	}), new OpenLayers.Layer.Google("Google Streets", {
		'sphericalMercator' : true,
		isBaseLayer : true,
		attribution : "<a href='http://upande.com'>powered by Upande</a>",
		transitionEffect : 'resize',
		visibility : false,
	}), new OpenLayers.Layer.Google("Google Hybrid", {
		type : google.maps.MapTypeId.HYBRID,
		'sphericalMercator' : true,
		isBaseLayer : true,
		attribution : "<a href='http://upande.com'>powered by Upande</a>",
		transitionEffect : 'resize',
		visibility : false
	}), new OpenLayers.Layer.Google("Google Satellite", {
		type : google.maps.MapTypeId.SATELLITE,
		'sphericalMercator' : true,
		isBaseLayer : true,
		attribution : "<a href='http://upande.com'>powered by Upande</a>",
		transitionEffect : 'resize',
		visibility : false,
	}), new OpenLayers.Layer.WMS("County", "http://204.236.224.228:8080/geoserver/wms", {
		layers : "geonode:majidata_counties",
		transparent : true,
		format : 'image/png'
	}, {
		singleTile : false,
		opacity : 0.65,
		isBaseLayer : false,
		visibility : true,
		noLegend : false,
		featureInfoFormat : 'application/vnd.ogc.gml',
		transitionEffect : 'none',
		metadata : {
			wfs : {
				protocol : 'fromWMSLayer',
				downloadFormats : Heron.options.wfs.downloadFormats
			}
		}
	}), new OpenLayers.Layer.WMS("Town", "http://204.236.224.228:8080/geoserver/wms", {
		layers : "geonode:majidata_towns",
		transparent : true,
		format : 'image/png'
	}, {
		singleTile : false,
		opacity : 0.65,
		isBaseLayer : false,
		visibility : true,
		noLegend : false,
		featureInfoFormat : 'application/vnd.ogc.gml',
		transitionEffect : 'none',
		metadata : {
			wfs : {
				protocol : 'fromWMSLayer',
				downloadFormats : Heron.options.wfs.downloadFormats
			}
		}
	}), new OpenLayers.Layer.WMS("Slum", "http://204.236.224.228:8080/geoserver/wms", {
		layers : "geonode:majidata_slums",
		transparent : true,
		format : 'image/png'
	}, {
		singleTile : false,
		opacity : 0.65,
		isBaseLayer : false,
		visibility : true,
		noLegend : false,
		featureInfoFormat : 'application/vnd.ogc.gml',
		transitionEffect : 'none',
		metadata : {
			wfs : {
				protocol : 'fromWMSLayer',
				downloadFormats : Heron.options.wfs.downloadFormats
			}
		}
	}), new OpenLayers.Layer.WMS("Area", "http://204.236.224.228:8080/geoserver/wms", {
		layers : "geonode:majidata_areas",
		transparent : true,
		format : 'image/png'
	}, {
		singleTile : false,
		opacity : 0.65,
		isBaseLayer : false,
		visibility : true,
		noLegend : false,
		featureInfoFormat : 'application/vnd.ogc.gml',
		transitionEffect : 'none',
		metadata : {
			wfs : {
				protocol : 'fromWMSLayer',
				downloadFormats : Heron.options.wfs.downloadFormats
			}
		}
	}), new OpenLayers.Layer.WMS("WSP", "http://204.236.224.228:8080/geoserver/wms", {
		layers : "geonode:majidata_wsp",
		transparent : true,
		format : 'image/png'
	}, {
		singleTile : false,
		opacity : 0.65,
		isBaseLayer : false,
		visibility : true,
		noLegend : false,
		featureInfoFormat : 'application/vnd.ogc.gml',
		transitionEffect : 'none',
		metadata : {
			wfs : {
				protocol : 'fromWMSLayer',
				downloadFormats : Heron.options.wfs.downloadFormats
			}
		}
	}), ];
Heron.options.map.toolbar = [{
		type : "scale",
		options : {
			width : 110
		}
	}, {
		type : "-"
	}, {
		type : "featureinfo",
		options : {
			pressed : true,
			//getfeatureControl : {
			//	hover : true,
			//	drillDown : false,
			//},
		}
	}, {
		type : "-"
	}, {
		type : "pan"
	}, {
		type : "zoomin"
	}, {
		type : "zoomout"
	}, {
		type : "zoomvisible"
	}, {
		type : "-"
	}, {
		type : "zoomprevious"
	}, {
		type : "zoomnext"
	}, {
		type : "-"
	}, {
		type : "measurelength",
		options : {
			geodesic : true
		}
	}, {
		type : "measurearea",
		options : {
			geodesic : true
		}
	}, {
		type : "-"
	}, {
		type : "searchcenter",
		options : {
			tooltip : 'Advanced Search',
			searchWindow : {
				title : __('Advanced Search'),
				x : 100,
				y : undefined,
				width : 360,
				height : 440,
				collapsible : true,
				items : [Heron.examples.searchPanelConfig]
			}
		}
	}, {
		type : "-"
	}, {
		type : "namesearch",
		options : {
			xtype : "gx_geocodercombo",
			id : "cmb_wsp",
			tooltip : 'Find all available WSPs',
			width:120,
			listWidth:250,
			hideTrigger : false,
			srs : "EPSG:900913",
			emptyText : 'Search for a WSP',
			queryParam : "CQL_FILTER",
			store : new Ext.data.Store({
				reader : new GeoExt.data.FeatureReader({}, [{
							name : 'name',
							mapping : 'WSPName'
						}, {
							name : 'bounds',
							convert : function (v, feature) {
								return feature.geometry.getBounds().toArray();
							}
						}
					]),
				proxy : new GeoExt.data.ProtocolProxy({
					protocol : new OpenLayers.Protocol.Script({
						url : "http://204.236.224.228:8080/geoserver/wfs",
						callbackKey : "format_options",
						callbackPrefix : "callback:",
						params : {
							service : "WFS",
							version : "1.1.0",
							srsName : "EPSG:900913",
							request : "GetFeature",
							typeName : "geonode:majidata_wsp",
							outputFormat : "json"
						}
					})
				})
			}),
			listeners : {
				beforequery : function (qe) {
					qe.query = "WSPName like '%" + qe.query + "%'";
				}
			}
		}
	}, {
		type : "-"
	}, {
		type : "namesearch",
		options : {
			xtype : "gx_geocodercombo",
			id : "cmb_county",
			tooltip : 'Find all available Conties',
			width:130,
			listWidth:200,
			hideTrigger : false,
			srs : "EPSG:900913",
			emptyText : 'Search for a County',
			queryParam : "CQL_FILTER",
			store : new Ext.data.Store({
				reader : new GeoExt.data.FeatureReader({}, [{
							name : 'name',
							mapping : 'CountyName'
						}, {
							name : 'bounds',
							convert : function (v, feature) {
								return feature.geometry.getBounds().toArray();
							}
						}
					]),
				proxy : new GeoExt.data.ProtocolProxy({
					protocol : new OpenLayers.Protocol.Script({
						url : "http://204.236.224.228:8080/geoserver/wfs",
						callbackKey : "format_options",
						callbackPrefix : "callback:",
						params : {
							service : "WFS",
							version : "1.1.0",
							srsName : "EPSG:900913",
							request : "GetFeature",
							typeName : "geonode:majidata_counties",
							outputFormat : "json"
						}
					})
				})
			}),
			listeners : {
				beforequery : function (qe) {
					qe.query = "CountyName like '%" + qe.query + "%'";
				}
			}
		}
	}, {
		type : "-"
	}, {
		type : "any",
		options : {
			xtype : "gx_geocodercombo",
			id : "cmb_town",
			tooltip : 'Find all available Towns',
			width:130,
			listWidth:200,
			hideTrigger : false,
			srs : "EPSG:900913",
			emptyText : 'Search for an Town',
			queryParam : "CQL_FILTER",
			store : new Ext.data.Store({
				reader : new GeoExt.data.FeatureReader({}, [{
							name : 'name',
							mapping : 'TownName'
						}, {
							name : 'bounds',
							convert : function (v, feature) {
								return feature.geometry.getBounds().toArray();
							}
						}
					]),
				proxy : new GeoExt.data.ProtocolProxy({
					protocol : new OpenLayers.Protocol.Script({
						url : "http://204.236.224.228:8080/geoserver/wfs",
						callbackKey : "format_options",
						callbackPrefix : "callback:",
						params : {
							service : "WFS",
							version : "1.1.0",
							srsName : "EPSG:900913",
							request : "GetFeature",
							typeName : "geonode:majidata_towns",
							outputFormat : "json"
						}
					})
				})
			}),
			listeners : {
				beforequery : function (qe) {
					qe.query = "TownName like '%" + qe.query + "%'";
				}
			}
		}
	}, {
		type : "-"
	}, {
		type : "namesearch",
		options : {
			xtype : "gx_geocodercombo",
			id : "cmb_slums",
			tooltip : 'Find all available Slums',
			width:120,
			listWidth:200,
			queryMode: 'local',
			hideTrigger : false,
			srs : "EPSG:900913",
			emptyText : 'Search for Slum',
			queryParam : "CQL_FILTER",
			store : new Ext.data.Store({
				reader : new GeoExt.data.FeatureReader({}, [{
							name : 'name',
							mapping : 'Slumname'
						}, {
							name : 'bounds',
							convert : function (v, feature) {
								return feature.geometry.getBounds().toArray();
							}
						}
					]),
				proxy : new GeoExt.data.ProtocolProxy({
					protocol : new OpenLayers.Protocol.Script({
						url : "http://204.236.224.228:8080/geoserver/wfs",
						callbackKey : "format_options",
						callbackPrefix : "callback:",
						params : {
							service : "WFS",
							version : "1.1.0",
							srsName : "EPSG:900913",
							request : "GetFeature",
							typeName : "geonode:majidata_slums",
							outputFormat : "json"
						}
					})
				})
			}),
			listeners : {
				beforequery : function (qe) {
					qe.query = "Slumname like '%" + qe.query + "%'";
				}
			}
		}
	}, {
		type : "-"
	}, {
		type : "namesearch",
		options : {
			xtype : "gx_geocodercombo",
			id : "cmb_areas",
			tooltip : 'Find all available Areas',
			width:130,
			listWidth:200,
			hideTrigger : false,
			srs : "EPSG:900913",
			emptyText : 'Search for an Area',
			queryParam : "CQL_FILTER",
			store : new Ext.data.Store({
				reader : new GeoExt.data.FeatureReader({}, [{
							name : 'name',
							mapping : 'Areaname'
						}, {
							name : 'bounds',
							convert : function (v, feature) {
								return feature.geometry.getBounds().toArray();
							}
						}
					]),
				proxy : new GeoExt.data.ProtocolProxy({
					protocol : new OpenLayers.Protocol.Script({
						url : "http://204.236.224.228:8080/geoserver/wfs",
						callbackKey : "format_options",
						callbackPrefix : "callback:",
						params : {
							service : "WFS",
							version : "1.1.0",
							srsName : "EPSG:900913",
							request : "GetFeature",
							typeName : "geonode:majidata_areas",
							outputFormat : "json"
						}
					})
				})
			}),
			listeners : {
				beforequery : function (qe) {
					qe.query = "Areaname like '%" + qe.query + "%'";
				},
				select: function(combo, record, index) {
					//alert(record);
				}
			}
		}
	}, {
		type : "-"
	}, ];
	
	
//
function highlightWMS(layer, attrib, unitid) {
	clearLayers();
	var sld = '';
	sld += '<sld:StyledLayerDescriptor xsi:schemaLocation="http://www.opengis.net/sld StyledLayerDescriptor.xsd" xmlns:sld="http://www.opengis.net/sld" xmlns:ogc="http://www.opengis.net/ogc" xmlns:xlink="http://www.w3.org/1999/xlink" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" version="1.0.0">';
	sld += '<NamedLayer><Name>' + layer + '</Name><UserStyle><Title>Default Style</Title><FeatureTypeStyle>';
	sld += '<Rule><ogc:Filter>';
	sld += '<ogc:PropertyIsEqualTo><ogc:PropertyName>';
	sld += attrib;
	sld += '</ogc:PropertyName><ogc:Literal>';
	sld += unitid;
	sld += '</ogc:Literal></ogc:PropertyIsEqualTo>';
	sld += '</ogc:Filter>';
	//sld += '<PointSymbolizer><Graphic><Mark><Fill><CssParameter name="fill">#00fd00</CssParameter></Fill></Mark></Graphic></PointSymbolizer>';
	sld += '<LineSymbolizer><Stroke><CssParameter name="stroke">#00fd00</CssParameter></Stroke></LineSymbolizer>';
	sld += '<PolygonSymbolizer><Fill><CssParameter name="fill">#cccccc</CssParameter><CssParameter name="fill-opacity">0.65</CssParameter></Fill></PolygonSymbolizer>';
	sld += '</Rule></FeatureTypeStyle></UserStyle></NamedLayer></sld:StyledLayerDescriptor>';
	var wmslayer = new OpenLayers.Layer.WMS("Selected", "http://204.236.224.228:8080/geoserver/wms", {
			layers : layer,
			format : 'image/png',
			sld_body : sld,
			transparent : true,
			isBaseLayer : false,
			displayInLayerSwitcher : false,
			singleTile : true
		});
	mapPanel.map.addLayer(wmslayer);
}
