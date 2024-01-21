// Set up prerequisite variables.
let player1 = document.getElementById("player1");
let player2 = document.getElementById("player2");
let player3 = document.getElementById("player3");
let player4 = document.getElementById("player4");
let player1Chosen = document.getElementById("player1Chosen");
let player2Chosen = document.getElementById("player2Chosen");
let player3Chosen = document.getElementById("player3Chosen");
let player4Chosen = document.getElementById("player4Chosen");
const decreaseButton = document.getElementById('decrease');
const increaseButton = document.getElementById('increase');
const valueSpan = document.getElementById('value');
let value = 5;
let platform1 = document.getElementById("platform1");
let platform2 = document.getElementById("platform2");
let platform3 = document.getElementById("platform3");
let platform4 = document.getElementById("platform4");
let platform5 = document.getElementById("platform5");
let pinApSouthEast = document.getElementById("pinApSouthEast");
let pinApNorthEast = document.getElementById("pinApNorthEast");
let pinOceCentral = document.getElementById("pinOceCentral");
let pinEuCentral = document.getElementById("pinEuCentral");
let pinEuWest = document.getElementById("pinEuWest");
let pinUsEast = document.getElementById("pinUsEast");
let pinUsWest = document.getElementById("pinUsWest");
let pinLaSouth = document.getElementById("pinLaSouth");
let survivorMMRColSpan = document.getElementsByClassName("survivorMMRColSpan");
let survivorPartySize = 4;

function hoverOnPlayers(number) {
    // Player 1.
    if(number >= 1) {
        player1.style.height = "400px";
        player1.style.filter = "grayscale(0)";
    }
    // Player 2.
    if(number >= 2) {
        player2.style.height = "400px";
        player2.style.filter = "grayscale(0)";
    }
    // Player 3.
    if(number >= 3) {
        player3.style.height = "400px";
        player3.style.filter = "grayscale(0)";
    }
    // Player 4.
    if(number == 4) {
        player4.style.height = "400px";
        player4.style.filter = "grayscale(0)";
    }
};

function hoverOffPlayers() {
    // Player 1.
    player1.style.height = "300px";
    player1.style.filter = "grayscale(1)";
    player1.style.transition = "0.5s";
    // Player 2.
    player2.style.height = "300px";
    player2.style.filter = "grayscale(1)";
    player2.style.transition = "0.5s";
    // Player 3.
    player3.style.height = "300px";
    player3.style.filter = "grayscale(1)";
    player3.style.transition = "0.5s";
    // Player 4.
    player4.style.height = "300px";
    player4.style.filter = "grayscale(1)";
    player4.style.transition = "0.5s";
};

function loadSurvivorsInParty() {
    // Player 1.
    if(survivorPartySize >= 1) {
        player1Chosen.style.height = "400px";
        player1Chosen.style.filter = "grayscale(0)";
    }
    // Player 2.
    if(survivorPartySize >= 2) {
        player2Chosen.style.height = "400px";
        player2Chosen.style.filter = "grayscale(0)";
    }
    // Player 3.
    if(survivorPartySize >= 3) {
        player3Chosen.style.height = "400px";
        player3Chosen.style.filter = "grayscale(0)";
    }
    // Player 4.
    if(survivorPartySize == 4) {
        player4Chosen.style.height = "400px";
        player4Chosen.style.filter = "grayscale(0)";
    }
    // Column spans.
    Array.prototype.forEach.call(survivorMMRColSpan, item => item.setAttribute("colspan",survivorPartySize));
};

decreaseButton.addEventListener('click', () => {
    if (value > 1) {
        value--;
        valueSpan.textContent = value;
    }
});

increaseButton.addEventListener('click', () => {
    if (value < 10) {
        value++;
        valueSpan.textContent = value;
    }
});

// function hoverOnButton() {
//     this.background-color = "#79070781";
//     this.transition = "0.3s";
// }

// function hoverOffButton() {
//     this.background-color = "#ffffff81";
//     this.transition = "0.3s";
// }

function hoverOnPlatform(number) {
    switch(number) {
        case 1:
            platform1.style.height = "150px";
            break;
        case 2:
            platform2.style.height = "150px";
            break;
        case 3:
            platform3.style.height = "150px";
            break;
        case 4:
            platform4.style.height = "150px";
            break;
        case 5:
            platform5.style.height = "150px";
            break;
    }
};

function hoverOffPlatform() {
    // Platform 1.
    platform1.style.height = "100px";
    platform1.style.transition = "0.5s";
    // Platform 2.
    platform2.style.height = "100px";
    platform2.style.transition = "0.5s";
    // Platform 3.
    platform3.style.height = "100px";
    platform3.style.transition = "0.5s";
    // Platform 4.
    platform4.style.height = "100px";
    platform4.style.transition = "0.5s";
    // Platform 5.
    platform5.style.height = "100px";
    platform5.style.transition = "0.5s";
};

function hoverOnPin(name) {
    switch(name) {
        case 'pinApSouthEast':
            pinApSouthEast.style.height = '6rem';
            break;
        case 'pinApNorthEast':
            pinApNorthEast.style.height = '6rem';
            break;
        case 'pinOceCentral':
            pinOceCentral.style.height = '6rem';
            break;
        case 'pinEuCentral':
            pinEuCentral.style.height = '6rem';
            break;
        case 'pinEuWest':
            pinEuWest.style.height = '6rem';
            break;
        case 'pinUsEast':
            pinUsEast.style.height = '6rem';
            break;
        case 'pinUsWest':
            pinUsWest.style.height = '6rem';
            break;
        case 'pinLaSouth':
            pinLaSouth.style.height = '6rem';
            break;
    }
};

function hoverOffPin() {
    pinApSouthEast.style.height = '4rem';
    pinApNorthEast.style.height = '4rem';
    pinOceCentral.style.height = '4rem';
    pinEuCentral.style.height = '4rem';
    pinEuWest.style.height = '4rem';
    pinUsEast.style.height = '4rem';
    pinUsWest.style.height = '4rem';
    pinLaSouth.style.height = '4rem';
};
