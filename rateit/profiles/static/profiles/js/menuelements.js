const search = document.getElementById("search");
const feed = document.getElementById("feed");
const suggestions = document.getElementById("suggestions");
const explore_ = document.getElementById("explore");
const create = document.getElementById("create");
const profile_ = document.getElementById("profile");
const notification = document.getElementById("notification");
const reels_ = document.getElementById("reels");
const more = document.getElementById("morediv");
var a = 0;
var b = 0;
var c = 0;
var d = 0;

function search_open() {
    notificationclose();
    createclose();
    search.style.display = "flex";
    // Add event listener to detect clicks outside the div
    document.addEventListener('click', clickOutsideSearch);
}
function searchclose() {
    search.style.display = "none"
}
function clickOutsideSearch(event) {
    if (event.target !== search && !search.contains(event.target) && event.target.id !== 'searchopen') {
        // Call your function here
        searchclose();
        // Hide the search div
        search.style.display = "none";
        // Remove event listener for clicks outside the div
        document.removeEventListener('click', clickOutsideSearch);
    }
}

function explore() {
    if (a == 0) {
        feed.style.display = "none";
        suggestions.style.display = "none";
        profile_.style.display = "none";
        reels_.style.display = "none";
        explore_.style.display = "block";
        a = 1;
        b = 0;
    }
    else {
        feed.style.display = "block";
        suggestions.style.display = "flex";
        explore_.style.display = "none";
        a = 0;
    }
}
function opencreate() {
    notificationclose();
    searchclose();
    create.style.display = "flex";
}
function createclose() {
    create.style.display = "none";
}
function profile() {
    if (b == 0) {
        feed.style.display = "none";
        suggestions.style.display = "none";
        explore_.style.display = "none";
        reels_.style.display = "none";
        profile_.style.display = "block";
        b = 1;
        a = 0;
    }
    else {
        feed.style.display = "block";
        suggestions.style.display = "flex";
        profile_.style.display = "none";
        b = 0;
    }
}
function opennotification() {
    createclose();
    searchclose();
    notification.style.display = "flex";
}
function notificationclose() {
    notification.style.display = "none";
}


function reels() {
    if (c == 0) {
        feed.style.display = "none";
        suggestions.style.display = "none";
        explore_.style.display = "none";
        profile_.style.display = "none";
        reels_.style.display = "block";
        b = 0;
        a = 0;
        c = 1;
    }
    else {
        feed.style.display = "block";
        suggestions.style.display = "flex";
        reels_.style.display = "none";
        c = 0;
    }
}
function openmore() {
    if (d == 0) {
        more.style.display = "flex";
        d = 1;
    }
    else {
        more.style.display = "none";
        d = 0;
    }
}










