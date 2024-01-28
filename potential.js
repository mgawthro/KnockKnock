// Populate map and apartments API data
var map = L.map('map').setView([42.2808, -83.7430], 14);
var myAPIkey = "36fc6ce18849487b8fdad29829ac9555";
var mapURL = `https://maps.geoapify.com/v1/tile/klokantech-basic/{z}/{x}/{y}.png?apiKey=${myAPIkey}`;

L.tileLayer(mapURL, {
    attribution: 'Powered by Geoapify | © OpenMapTiles © OpenStreetMap contributors',
    apiKey: myAPIkey,
    mapStyle: "klokantech-basic",
}).addTo(map);

var marker;

const addressSearchControl = L.control.addressSearch(myAPIkey, {
    position: 'topright',
    resultCallback: (address) => {
        if (marker) {
            marker.remove();
        }
        if (!address) return;
        marker = L.marker([address.lat, address.lon]).addTo(map);
        if (address.bbox && address.bbox.lat1 !== address.bbox.lat2 && address.bbox.lon1 !== address.bbox.lon2) {
            map.fitBounds([[address.bbox.lat1, address.bbox.lon1], [address.bbox.lat2, address.bbox.lon2]], { padding: [100, 100] });
        } else {
            map.setView([address.lat, address.lon], 15);
        }
        //going to have leasing info
        // var popupContent = "<div>Resigning</div>";
        // marker.bindPopup(popupContent);
        marker.on('click', () => {
            popupDiv();
        });
    },
});
map.addControl(addressSearchControl);

// Sample data to send in the POST request
const postData = { key1: 'value1', key2: 'value2' };

// Make a POST request to the Flask backend
fetch('http://127.0.0.1:5000/potential', {
    method: 'POST',
    headers: {
        'Content-Type': 'application/json',
    },
    body: JSON.stringify(postData),
})
.then(response => response.json())
.then(data => {
    const dataList = document.getElementById('dataList');
        data.data.forEach(item => {
            const listItem = document.createElement('li');
            listItem.textContent = item;
            dataList.appendChild(listItem);
        });
})
.catch(error => console.error('Error:', error));

popupDiv = () => {
    var otr = document.createElement("div");
    otr.setAttribute("class", "popup");
    otr.innerHTML =  "<h2>" + "House Details: " +"</h2>" 
        + "<br>"+ "</br>"
        + "<div>" 

        + "</div>";
    document.body.appendChild(otr);
    var mapDiv = document.getElementById("out-map");
    mapDiv.style.transition = "transform 0.5s";
    mapDiv.style.transform = "translate(-0%, -13%)";
}