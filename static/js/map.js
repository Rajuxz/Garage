const defaultLatitude = 26.6430564
const defaultLongitude = 87.9892757
let marker = null
let circle = null
let dragging = false // to keep track if user is dragging the marker.

const mapAlert = document.querySelector('#mapAlert') //message
const idLatitude = document.querySelector('#id_latitude') //for hidden latitude field
const idLongitude = document.querySelector('#id_longitude') // for hidden longitude field.

var map = L.map('map').setView([defaultLatitude, defaultLongitude], 13)
L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '..'
}).addTo(map);
marker = L.marker([defaultLatitude, defaultLongitude]).addTo(map)
const success = (position) => {

        const latitude = position.coords.latitude
        const longitude = position.coords.longitude
        const accuracy = position.coords.accuracy
        
        if (marker !== null) { map.removeLayer(marker) }
        if (circle !== null) { map.removeLayer(circle) }
        setLatLng(latitude,longitude)
        //creating marker
        marker = L.marker([latitude, longitude]).addTo(map);
        circle = L.circle([latitude, longitude], { radius: accuracy }).addTo(map);
        map.fitBounds(circle.getBounds())
    
}

const error = (error) => {
    if (error.code === 1) {
        setStyle(mapAlert,'text-danger','text-success')
        setLatLng(defaultLatitude,defaultLongitude)
    } else {
        setStyle(mapAlert,'text-danger','text-success')
        setLatLng(defaultLatitude,defaultLongitude)   
    }
}
navigator.geolocation.watchPosition(success, error, {
    enableHighAccuracy: true,
    timeout: 20000,
    maximumAge: 0
})

const setLatLng = (latitude,longitude)=>{
    idLatitude.value = latitude
    idLongitude.value = longitude
}

const setStyle = (id,toAdd, toRemove)=>{
    id.classList.remove(toRemove)
    id.classList.add(toAdd)
}


