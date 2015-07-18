$(document).ready(function () {
    var $map = $("#map");

    var pointArray = [parseFloat($map.data('lat')),parseFloat($map.data('lng'))]

    var point = new ol.geom.Point(pointArray);
    point.transform('EPSG:4326', 'EPSG:3857');
    var pointFeature = new ol.Feature({
        geometry: point,
        name: 'Null Island',
        population: 4000,
        rainfall: 500
    });

    var vectorSource = new ol.source.Vector({
        features: [pointFeature]
    });
    var vectorLayer = new ol.layer.Vector({
        source: vectorSource
    });
    var OSMLayer = new ol.layer.Tile({source: new ol.source.OSM()})
    var map = new ol.Map({
        target: 'map',
        layers: [
            OSMLayer,
            vectorLayer
        ],
        view: new ol.View({
            center: ol.proj.transform(pointArray, 'EPSG:4326', 'EPSG:3857'),
            zoom: 14
        })
    });
});