document.addEventListener('DOMContentLoaded', function () {
    var sideNavbar = document.querySelectorAll('.sidenav');
    M.Sidenav.init(sideNavbar);
});

document.addEventListener('DOMContentLoaded', function () {
    var elems = document.querySelectorAll('.modal');
    M.Modal.init(elems);
});

document.addEventListener('DOMContentLoaded', function () {
    for (let guestTable of document.getElementsByClassName("table-dropdown")) {
        guestTable.addEventListener("click", function () {
            document.getElementById("chosen-table").innerHTML = this.innerHTML;
            chosenTable = document.getElementById("chosen-table").innerHTML;
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

document.addEventListener('DOMContentLoaded', function () {
    if (window.location.href.indexOf("payments") > -1) {
        if (document.getElementById("payment-container").textContent.trim() === "") {
            document.getElementById("payment-container").style.display = "none";
            document.getElementById("no-payments").style.display = "block";
        };
    };
});

document.addEventListener('DOMContentLoaded', function () {
    if (window.location.toString().includes("dashboard")) {
        document.getElementById("click-confetti").addEventListener("click", function () {
            confetti({
                particleCount: 150,
                spread: 150,
                origin: {
                    y: 0.7
                }
            });
        })
        if (document.getElementById("dash-checklist").textContent.trim() === "") {
            document.getElementById("dash-checklist").style.display = "none";
            document.getElementById("whats-next").style.borderBottomLeftRadius = "6px";
            document.getElementById("whats-next").style.borderBottomRightRadius = "6px";
            document.getElementById("no-checklist").style.display = "block";
        };
    };
});

document.addEventListener('DOMContentLoaded', function () {
    var elems = document.querySelectorAll('.dropdown-trigger');
    var instances = M.Dropdown.init(elems);
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