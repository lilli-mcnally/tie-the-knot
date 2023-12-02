// Opens the side navigation for mobile and tablet devices
document.addEventListener('DOMContentLoaded', function () {
    var sideNavbar = document.querySelectorAll('.sidenav');
    M.Sidenav.init(sideNavbar);
});

// To open all modals
document.addEventListener('DOMContentLoaded', function () {
    var elems = document.querySelectorAll('.modal');
    M.Modal.init(elems);
});

// For the table name input box on Add and Edit Guest pages
document.addEventListener('DOMContentLoaded', function () {
    for (let guestTable of document.getElementsByClassName("table-dropdown")) {
        guestTable.addEventListener("click", function () {
            // Grabs the text on the clicked button as a string
            document.getElementById("chosen-table").innerHTML = this.innerHTML;
            chosenTable = document.getElementById("chosen-table").innerHTML;
            // Changes the input to either None or the text on the button
            if (chosenTable == "None") {
                document.getElementById("chosen-table").style.display = "none";
                document.getElementById("table_name").value = this.innerHTML.trim();
            } else {
                document.getElementById("table_name").value = this.innerHTML.trim();
                document.getElementById("chosen-table").style.border = "2px solid #366355";
                document.getElementById("chosen-table").style.display = "block";
            };
        });
    };
});

// Display for the Dashboard
document.addEventListener('DOMContentLoaded', function () {
    if (window.location.toString().includes("dashboard")) {
        document.getElementById("click-confetti").addEventListener("click", function () {
            // Set the display for the confetti dependent on screen size
            if (window.innerWidth < 400) {
                confetti({
                    particleCount: 200,
                    spread: 50,
                    origin: {
                        y: 0.8
                    },
                    scalar: 0.8
                });
            } else if (window.innerWidth < 800) {
                confetti({
                    particleCount: 200,
                    spread: 100,
                    origin: {
                        y: 0.7
                    },
                    scalar: 1
                });
            } else if (window.innerWidth < 1500) {
                confetti({
                    particleCount: 300,
                    spread: 125,
                    origin: {
                        y: 0.7
                    },
                    scalar: 1
                });
            } else {
                confetti({
                    particleCount: 350,
                    spread: 150,
                    origin: {
                        y: 0.5
                    },
                    scalar: 1.3,
                });
            }
        })
        // Changes the checklist items css dependent on if there's anything in the checklist table
        if (document.getElementById("dash-checklist").textContent.trim() === "") {
            document.getElementById("dash-checklist").style.display = "none";
            document.getElementById("whats-next").style.borderBottomLeftRadius = "6px";
            document.getElementById("whats-next").style.borderBottomRightRadius = "6px";
            document.getElementById("no-checklist").style.display = "block";
        };
    };
});

// Removes the Unassigned Guests div if no guests in this catagory
document.addEventListener('DOMContentLoaded', function () {
    if (window.location.toString().includes("table_plan")) {
        if (document.getElementById("no-guest") == null) {
            document.getElementById("no-guest-container").style.display = "none";
        };
    };
});

// Either shows table dropdown or no tables message on Guest pages
document.addEventListener('DOMContentLoaded', function () {
    var elems = document.querySelectorAll('.dropdown-trigger');
    M.Dropdown.init(elems);
    if (window.location.href.indexOf("add_guests") != -1) {
        console.log(document.getElementById("chosen-table"))
        chosenTable = document.getElementById("chosen-table").innerHTML;
        if (chosenTable == "None") {
            document.getElementById("chosen-table").style.display = "none";
        }
    } else if (window.location.href.indexOf("edit_guests") != -1) {
        console.log(document.getElementById("chosen-table"))
        chosenTable = document.getElementById("chosen-table").innerHTML;
        if (chosenTable == "None") {
            document.getElementById("chosen-table").style.display = "none";
        }
    };
});