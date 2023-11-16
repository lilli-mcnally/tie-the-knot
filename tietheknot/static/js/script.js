document.addEventListener('DOMContentLoaded', function () {
    var sideNavbar = document.querySelectorAll('.sidenav');
    M.Sidenav.init(sideNavbar);
});

document.addEventListener('DOMContentLoaded', function () {
    var elems = document.querySelectorAll('.modal');
    M.Modal.init(elems);
});

document.addEventListener('DOMContentLoaded', function () {
    var elems = document.querySelectorAll('.dropdown-trigger');
    var instances = M.Dropdown.init(elems);
});

document.addEventListener('DOMContentLoaded', function () {
    for (let guestTable of document.getElementsByClassName("table-dropdown")) {
        guestTable.addEventListener("click", function () {
            document.getElementById("chosen-table").innerHTML = this.innerHTML;
            document.getElementById("table_number").value = this.innerHTML.trim();
            document.getElementById("chosen-table").style.border = "2px solid #366355";
        })
    }
});