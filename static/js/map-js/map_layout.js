Ext.namespace("Heron");
Heron.layout = {
	xtype : 'tabpanel',
	id : 'hr-container-main',
	renderTo : 'map',
	activeTab : 0,
	split : false,
	border : false,
	height : mapH,
	items : [{
			xtype : 'panel',
			id : 'Maps',
			title : 'Map',
			layout : 'border',
			region : 'center',
			width : '100%',
			collapsible : false,
			split : false,
			border : false,
			items : [{
					xtype : 'panel',
					id : 'hr-menu-left-container',
					title : 'Layers',
					layout : 'auto',
					region : "west",
					width : 240,
					collapsible : true,
					collapsed : true,
					split : true,
					border : false,
					items : [{
							xtype : 'hr_layertreepanel',
							title : 'Visible Layers',
							height : 220,
							hropts : Heron.options.layertree,
						}, {
							xtype : 'panel',
							title : 'Indicators',
							height : 200,
							items : [indicator_style_form],

						}
					]
				}, {
					xtype : 'panel',
					id : 'hr-map-featureinfo-container',
					layout : 'border',
					region : 'center',
					width : '100%',
					collapsible : false,
					split : false,
					border : false,
					items : [{
							xtype : 'hr_mappanel',
							//title : '&nbsp;',
							id : 'hr-map',
							region : 'center',
							collapsible : false,
							border : false,
							hropts : Heron.options.map
						}, {
							xtype : 'hr_featureinfopanel',
							id : 'hr-feature-info',
							region : "south",
							border : true,
							collapsible : true,
							collapsed : true,
							height : 205,
							split : false,
							showTopToolbar : true,
							exportFormats : ['CSV', 'XLS', 'GMLv2'],
							displayPanels : ['Grid', 'XML'],
							infoFormat : 'application/vnd.ogc.gml',
							discardStylesForDups : true,
							maxFeatures : 10
						}
					]
				}, {
					xtype : 'panel',
					id : 'hr-menu-right-container',
					title : 'Legend',
					layout : 'fit',
					//layout : 'accordion',
					region : "east",
					width : 240,
					collapsible : true,
					split : false,
					border : false,
					items : [{
							xtype : 'hr_layerlegendpanel',
							id : 'hr-layerlegend-panel',
							title : '',
							defaults : {
								useScaleParameter : true,
								baseParams : {
									FORMAT : 'image/png'
								}
							},
							hropts : {
								prefetchLegends : false
							}
						}
					]
				}
			]
		}, {
			xtype : 'panel',
			id : 'charts',
			title : 'Charts',
			layout : 'border',
			split : false,
			border : false,
			items : [{
					xtype : 'panel',
					id : 'hr-menu-left2-container',
					title : 'Indicators',
					layout : 'fit',
					region : "west",
					width : 240,
					collapsible : true,
					collapsed : false,
					split : false,
					border : false,
					items : [indicator_form]
				}, {
					xtype : 'panel',
					id : 'hr-chart-featureinfo-container',
					layout : 'fit',
					autoScroll : true,
					region : 'center',
					collapsible : false,
					split : false,
					border : false,
					items : {
						id : 'majichart',
						title : 'charts',
						store : [],
						animate : true,
						url : 'http://cdnjs.cloudflare.com/ajax/libs/extjs/3.4.1-1/resources/charts.swf',
						//xtype: 'linechart',
						xtype : 'columnchart',
						xField : 'name',
						yField : 'value',
						extraStyle : {
							xAxis : {
								labelRotation : -90,
								padding : 10,
								font : {
									family : 'Tahoma',
									size : 4
								}
							}
						}
					}
				}
			]
		}, {
			xtype : 'panel',
			id : 'mdatatables',
			title : 'Tables',
			padding : 20,
			layout : 'fit',
			split : false,
			border : false,
			renderTo : 'render',
			contentEl : 'majitables',
			//autoScroll:true,
		}
	]

};